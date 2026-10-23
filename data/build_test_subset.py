"""Create a compact upload directory using hard links to audited OCL data."""

import argparse
import json
import os
from pathlib import Path
import tempfile

from audit_test_data import save


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "test_subset")
    args = parser.parse_args()
    output = args.output.expanduser().resolve()
    if output == root or root.is_relative_to(output):
        parser.error("The subset must be a separate directory")
    reports = root / "transfer_lists"
    audit = json.loads((reports / "data_audit.json").read_text())
    urls = {name: url for url, name in
            json.loads((root / "resources/url_to_filename.json").read_text())}
    unresolved_web = {name: {"name": name, "url": urls.get(name), "reason": "missing"}
                      for name in audit["missing_images"] if name.startswith("from_web/")}
    for error in audit["crop_errors"]:
        name = error["image_name"]
        if name.startswith("from_web/"):
            unresolved_web[name] = {"name": name, "url": urls.get(name),
                                    "reason": "image dimensions incompatible with annotated object",
                                    "image_size": error.get("image_size"), "box": error["box"]}
    save(reports / "unresolved_web_images.json",
         json.dumps(list(unresolved_web.values()), indent=2) + "\n")
    marker = output / ".ocl-subset.json"
    if output.exists() and not marker.is_file():
        raise ValueError(f"Refusing to alter an existing unmanaged directory: {output}")
    previous = json.loads(marker.read_text()) if marker.is_file() else {"linked_files": {}}
    output.mkdir(parents=True, exist_ok=True)
    if not marker.is_file():
        save(marker, json.dumps(previous) + "\n")
    names = (reports / "test_data.txt").read_text().splitlines()
    linked = dict(previous["linked_files"])
    missing = []
    for name in names:
        source = root / name
        if not source.is_file():
            missing.append(name)
            continue
        destination = output / name
        stat = source.stat()
        identity = [stat.st_dev, stat.st_ino]
        if destination.exists():
            old = destination.stat()
            if [old.st_dev, old.st_ino] == identity:
                linked[name] = identity
                continue
            if linked.get(name) != [old.st_dev, old.st_ino]:
                raise ValueError(f"Unexpected file change in subset: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
            temporary = Path(handle.name)
        temporary.unlink()
        try:
            os.link(source, temporary)
            temporary.replace(destination)
        finally:
            temporary.unlink(missing_ok=True)
        linked[name] = identity
        if len(linked) % 1000 == 0:
            save(marker, json.dumps({"linked_files": linked}) + "\n")
    save(marker, json.dumps({"linked_files": linked}) + "\n")
    for source in reports.iterdir():
        if source.is_file() and source.suffix in (".json", ".jsonl", ".txt", ".sha256"):
            save(output / "transfer_lists" / source.name, source.read_text())
    scripts = ["audit_test_data.py", "download_imagenet_subset.py", "extract_imagenet_subset.py",
               "download_selected_web.py", "download_web_images.py", "recover_web_images.py"]
    for name in scripts:
        save(output / name, (root / name).read_text())
    payload = sum((root / name).stat().st_size for name in names if (root / name).is_file())
    manifest = {
        "ready_for_full_evaluation": audit["ready_for_full_evaluation"],
        "required_files": len(names), "linked_files": len(names) - len(missing),
        "missing_files": missing, "payload_bytes": payload,
        "selection": "All objects from the top ten categories across train + val + test",
        "storage": "Hard links locally; ordinary files when transferred with rsync",
    }
    save(reports / "subset_manifest.json", json.dumps(manifest, indent=2) + "\n")
    save(output / "transfer_lists/subset_manifest.json", json.dumps(manifest, indent=2) + "\n")
    status = "READY" if audit["ready_for_full_evaluation"] else "INCOMPLETE - do not report full-test metrics yet"
    text = f"""# OCL top-ten evaluation data

Status: {status}.

Selection: train + val + test annotations are merged; categories are ranked by
object-instance count. Every selected object belongs to the evaluation set.
Required images: {audit['required_images']}. Missing files: {len(missing)}.
Selected objects: {audit['selected_objects']}; the existing DataLoader excludes
{len(audit['excluded_invalid_boxes'])} zero-area/invalid box before evaluation.
Image and metadata payload currently present: {payload / 1024**3:.3f} GiB.

See transfer_lists/data_audit.json for missing files, crop errors and label checks.
transfer_lists/test_data.txt retains ALL required paths, including missing ones.
The annotation files and raw image dimensions are preserved.

## Upload from the project root

Replace USER, HOST and REMOTE_PROJECT with your SSH destination:

    rsync -av --partial --info=progress2 --exclude=.ocl-subset.json data/test_subset/ USER@HOST:REMOTE_PROJECT/data/

The destination data directory contains COCO/, ImageNet/, aPY/, from_web/ and
resources/, matching the relative paths in the annotations. Large source archives,
unselected images, and local COCO symlinks are absent from this upload directory.
The local files are hard-linked, so do not edit them in place: that also changes
the source files. Uploading with rsync produces ordinary files on the server.

## Verify on the server

From REMOTE_PROJECT/data with Pillow installed:

    sha256sum --quiet -c transfer_lists/available_files.sha256
    python audit_test_data.py

Checksum success validates the transferred available files; the audit separately
checks completeness and object crops, returning nonzero if anything is blocked.
It needs no CLIP weights, torch or network access.

## Remaining issues

Some original web URLs are no longer available. See web_download_report.json and
web_recovery_report.json under transfer_lists/ for attempts and recovered sources.
These are historical attempt reports; data_audit.json shows the current state.
unresolved_web_images.json lists missing or unusable web images with original URLs
so that the exact originals can be requested from an existing dataset backup.
The OCL author previously supplied missing originals on request in issue 1:
https://github.com/silicx/ObjectConceptLearning/issues/1

Some ImageNet boxes do not intersect the original-size images. The selected
ImageNet coordinates are concentrated near a 256 x 256 frame, but the correct
resize/crop convention has not been confirmed from the official code or paper.
Confirm that convention before trusting image crops or evaluation metrics.
The audit reports concrete failures; no speculative coordinate rewrite is applied.
"""
    save(output / "README.md", text)
    save(reports / "DATA_STATUS.md", text)
    print(f"Subset: {output}")
    print(f"Linked {len(names) - len(missing)}/{len(names)} files; payload {payload / 1024**3:.3f} GiB")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()
