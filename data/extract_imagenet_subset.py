"""Extract the OCL image manifest without expanding the whole ImageNet dataset."""

from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tarfile
import tempfile


def load_manifest(path: Path) -> list[str]:
    names = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not names or len(names) != len(set(names)):
        raise ValueError("The image manifest must be non-empty and contain no duplicates.")
    for name in names:
        path_parts = PurePosixPath(name).parts
        if (
            PurePosixPath(name).is_absolute()
            or ".." in path_parts
            or not (
                (len(path_parts) == 3 and path_parts[0] == "train")
                or (len(path_parts) == 2 and path_parts[0] == "val")
            )
        ):
            raise ValueError(f"Unexpected ImageNet path: {name}")
    return names


def copy_image(archive: tarfile.TarFile, member: tarfile.TarInfo, destination: Path) -> bool:
    if not member.isfile() or member.size <= 0:
        raise ValueError(f"Expected a non-empty image file: {member.name}")
    if destination.is_file() and destination.stat().st_size == member.size:
        return False

    destination.parent.mkdir(parents=True, exist_ok=True)
    source = archive.extractfile(member)
    if source is None:
        raise ValueError(f"Cannot read archive member: {member.name}")

    temporary = None
    try:
        # Publish only complete files so an interrupted extraction can be rerun.
        with source, tempfile.NamedTemporaryFile(
            dir=destination.parent, prefix=f".{destination.name}.", suffix=".part", delete=False
        ) as output:
            temporary = Path(output.name)
            shutil.copyfileobj(source, output, length=1024 * 1024)
        if temporary.stat().st_size != member.size:
            raise ValueError(f"Incomplete archive member: {member.name}")
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return True


def extract_images(
    archive: tarfile.TarFile,
    requested: dict[str, str],
    output_dir: Path,
    found: set[str],
) -> tuple[int, int]:
    remaining = dict(requested)
    copied = skipped = 0
    for member in archive:
        relative = remaining.pop(PurePosixPath(member.name).name, None)
        if relative is None:
            continue
        if copy_image(archive, member, output_dir / relative):
            copied += 1
        else:
            skipped += 1
        found.add(relative)
        if not remaining:
            break
    return copied, skipped


def extract_subset(archive_dir: Path, output_dir: Path, names: list[str]) -> tuple[int, int]:
    train = {}
    val = {}
    for name in names:
        parts = PurePosixPath(name).parts
        if parts[0] == "train":
            train.setdefault(f"{parts[1]}.tar", {})[parts[2]] = name
        else:
            val[parts[1]] = name

    found = set()
    copied = skipped = 0
    if train:
        total_classes = len(train)
        completed_classes = 0
        with tarfile.open(archive_dir / "ILSVRC2012_img_train.tar", mode="r:") as outer:
            for member in outer:
                requested = train.pop(PurePosixPath(member.name).name, None)
                if requested is None:
                    continue
                if not member.isfile():
                    raise ValueError(f"Expected a class archive: {member.name}")
                class_file = outer.extractfile(member)
                if class_file is None:
                    raise ValueError(f"Cannot read class archive: {member.name}")
                # Uncompressed nested tar files support seeking; no class tar is written to disk.
                with class_file, tarfile.open(fileobj=class_file, mode="r:") as inner:
                    new, existing = extract_images(inner, requested, output_dir, found)
                copied += new
                skipped += existing
                completed_classes += 1
                if completed_classes == 1 or completed_classes % 10 == 0 or not train:
                    print(
                        f"Train classes: {completed_classes}/{total_classes}; "
                        f"images copied: {copied}; size-matched existing images: {skipped}",
                        flush=True,
                    )
                if not train:
                    break

    if val:
        with tarfile.open(archive_dir / "ILSVRC2012_img_val.tar", mode="r:") as archive:
            new, existing = extract_images(archive, val, output_dir, found)
        copied += new
        skipped += existing

    missing = sorted(set(names) - found)
    if missing:
        raise ValueError(
            f"{len(missing)} requested images were not found in the archives: {missing[:10]}"
        )
    print(f"Complete: {len(found)} images; copied={copied}; size-matched existing={skipped}.")
    print(f"Output directory: {output_dir.resolve()}")
    return copied, skipped


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-dir", type=Path, default=data_dir / "imagenet_archives")
    parser.add_argument("--output-dir", type=Path, default=data_dir / "ImageNet")
    parser.add_argument(
        "--manifest", type=Path, default=data_dir / "transfer_lists" / "imagenet_required.txt"
    )
    args = parser.parse_args()
    names = load_manifest(args.manifest.expanduser())
    extract_subset(args.archive_dir.expanduser(), args.output_dir.expanduser(), names)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, tarfile.TarError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
