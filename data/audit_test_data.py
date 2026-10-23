"""Validate all OCL top-ten test images and create a minimal transfer manifest."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path, PurePosixPath
import pickle
import tempfile

from PIL import Image


def save(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(path)


def audit(root: Path, workers: int) -> dict:
    resources = root / "resources"
    vocabulary = {
        kind: json.loads((resources / f"OCL_class_{kind}.json").read_text())
        for kind in ("object", "attribute", "affordance")
    }
    annotations = []
    for split in ("train", "val", "test"):
        with (resources / f"OCL_annot_{split}.pkl").open("rb") as handle:
            annotations.extend(pickle.load(handle))
    counts = Counter(obj["obj"] for row in annotations for obj in row["objects"])
    selected = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10])
    if len(selected) != 10 or not set(selected).issubset(vocabulary["object"]):
        raise ValueError("Invalid category vocabulary or fewer than ten categories")
    objects = defaultdict(list)
    excluded = []
    label_errors = []
    selected_count = 0
    for row in annotations:
        name = row["name"]
        parts = PurePosixPath(name)
        if parts.is_absolute() or ".." in parts.parts or "\n" in name:
            raise ValueError(f"Unsafe image path: {name!r}")
        for index, obj in enumerate(row["objects"]):
            if obj["obj"] not in selected:
                continue
            selected_count += 1
            objects[name]
            box = obj.get("box")
            if box is not None and (
                len(box) != 4 or not all(math.isfinite(value) for value in box)
                or box[2] <= box[0] or box[3] <= box[1]
            ):
                excluded.append({"image_name": name, "object_index": index,
                                 "category": obj["obj"], "box": list(box)})
                continue
            for field, kind in (("attr", "attribute"), ("aff", "affordance")):
                if any(not isinstance(i, int) or not 0 <= i < len(vocabulary[kind])
                       for i in obj[field]):
                    label_errors.append({"image_name": name, "object_index": index,
                                         "field": field, "ids": obj[field]})
            objects[name].append((index, obj))
    names = sorted(objects)
    reports = root / "transfer_lists"
    expected = set((reports / "ocl_non_imagenet.txt").read_text().splitlines())
    expected.update("ImageNet/" + name for name in
                    (reports / "imagenet_required.txt").read_text().splitlines())
    if expected != set(names):
        raise ValueError("Existing transfer manifests disagree with the annotation selection")

    def inspect(name):
        path = root / name
        result = {"name": name}
        if not path.is_file():
            return {**result, "status": "missing"}
        try:
            content = path.read_bytes()
            with Image.open(io.BytesIO(content)) as image:
                image.load()
                width, height = image.size
                image.convert("RGB")
            result.update(size_bytes=len(content), width=width, height=height,
                          sha256=hashlib.sha256(content).hexdigest())
            crop_errors = []
            for index, obj in objects[name]:
                box = obj.get("box", (0, 0, width, height))
                left, top, right, bottom = box
                if min(width, right) <= max(0, left) or min(height, bottom) <= max(0, top):
                    crop_errors.append({"object_index": index, "box": list(box),
                                        "category": obj["obj"]})
            return {**result, "status": "valid", "crop_errors": crop_errors}
        except (OSError, ValueError, SyntaxError, Image.DecompressionBombError) as error:
            return {**result, "status": "corrupt", "error": str(error)}

    results = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(inspect, name) for name in names]
        for future in as_completed(futures):
            result = future.result()
            results[result["name"]] = result
            if len(results) % 5000 == 0:
                print(f"Validated {len(results)}/{len(names)} images", flush=True)
    ordered = [results[name] for name in names]
    missing = [r["name"] for r in ordered if r["status"] == "missing"]
    corrupt = [r for r in ordered if r["status"] == "corrupt"]
    crop_errors = [{"image_name": r["name"], "image_size": [r["width"], r["height"]], **error}
                   for r in ordered for error in r.get("crop_errors", [])]
    imagenet_rows = [r for r in ordered if r["name"].startswith("ImageNet/")
                     and r["status"] == "valid"]
    imagenet_boxes = [obj["box"] for name in names if name.startswith("ImageNet/")
                      for _, obj in objects[name] if "box" in obj]
    by_source = {}
    for source in sorted({name.split("/")[0] for name in names}):
        rows = [r for r in ordered if r["name"].startswith(source + "/")]
        by_source[source] = dict(Counter(r["status"] for r in rows))
        by_source[source]["required"] = len(rows)
    ready = not (missing or corrupt or crop_errors or label_errors)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "ready_for_full_evaluation": ready,
        "selection_splits": ["train", "val", "test"],
        "count_unit": "object_instance", "selected_categories": selected,
        "selected_objects": selected_count,
        "expected_evaluation_objects": selected_count - len(excluded),
        "objects_blocked_by_missing_or_corrupt_images": sum(
            len(objects[r["name"]]) for r in ordered if r["status"] != "valid"
        ),
        "required_images": len(names), "sources": by_source,
        "valid_image_bytes": sum(r.get("size_bytes", 0) for r in ordered if r["status"] == "valid"),
        "vocabulary_sizes": {key: len(value) for key, value in vocabulary.items()},
        "excluded_invalid_boxes": excluded,
        "missing_images": missing, "corrupt_images": corrupt,
        "crop_errors": crop_errors, "label_errors": label_errors,
        "imagenet_coordinate_diagnostic": {
            "selected_boxes": len(imagenet_boxes),
            "maximum_box_coordinate": max((max(box) for box in imagenet_boxes), default=None),
            "available_images_not_256_square": sum(
                (r["width"], r["height"]) != (256, 256) for r in imagenet_rows
            ),
            "note": "Coordinates appear based on a 256-square frame. The correct resize/crop convention remains unconfirmed; no transform was applied.",
        },
        "transfer_manifest_keeps_missing_paths": True,
    }
    metadata = ["resources/OCL_annot_" + split + ".pkl" for split in ("train", "val", "test")]
    metadata += ["resources/OCL_class_" + kind + ".json" for kind in vocabulary]
    metadata += ["resources/url_to_filename.json"]
    save(reports / "test_images.txt", "\n".join(names) + "\n")
    save(reports / "test_data.txt", "\n".join(sorted(names + metadata)) + "\n")
    save(reports / "missing_images.txt", "".join(name + "\n" for name in missing))
    save(reports / "test_image_integrity.jsonl", "".join(json.dumps(r) + "\n" for r in ordered))
    checksums = [f"{r['sha256']}  {r['name']}\n" for r in ordered if r["status"] == "valid"]
    checksums += [f"{hashlib.sha256((root / name).read_bytes()).hexdigest()}  {name}\n"
                  for name in metadata]
    save(reports / "available_files.sha256", "".join(checksums))
    save(reports / "data_audit.json", json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ("missing_images", "corrupt_images")}, indent=2))
    print(f"Report: {reports / 'data_audit.json'}")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    if not 1 <= args.workers <= 32:
        parser.error("Use 1..32 workers")
    report = audit(args.data_root.resolve(), args.workers)
    return 0 if report["ready_for_full_evaluation"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
