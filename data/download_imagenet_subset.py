"""Download selected ImageNet images using cached tar offsets and HTTP Range.

The first index scan reads ahead to reduce request overhead. These temporary
blocks can contain unselected images, but are never written to disk.
"""

from __future__ import annotations

import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import fcntl
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tarfile
import tempfile
import threading
import time

import requests
from PIL import Image

from extract_imagenet_subset import load_manifest


BASE_URL = "https://image-net.org/data/ILSVRC/2012"
PATTERNS = {
    "classes": re.compile(r"n\d{8}\.tar"),
    "train": re.compile(r"n\d{8}_\d+\.JPEG"),
    "val": re.compile(r"ILSVRC2012_val_\d{8}\.JPEG"),
}


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=path.parent, prefix=f".{path.name}.", suffix=".part", delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


class RangeClient:
    def __init__(self, timeout: float, retries: int) -> None:
        self.timeout = timeout
        self.retries = retries
        self.local = threading.local()
        self.stop = threading.Event()
        self.lock = threading.Lock()
        self.requests = 0
        self.bytes = 0

    def fetch(self, url: str, start: int, end: int, identity: dict | None = None) -> tuple[bytes, dict]:
        if start < 0 or end < start:
            raise ValueError(f"Invalid byte range: {start}-{end}")
        if not hasattr(self.local, "session"):
            self.local.session = requests.Session()
        headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"}
        if identity:
            if identity.get("etag") and not identity["etag"].startswith("W/"):
                headers["If-Match"] = identity["etag"]
            elif identity.get("last_modified"):
                headers["If-Unmodified-Since"] = identity["last_modified"]
        for attempt in range(self.retries + 1):
            if self.stop.is_set():
                raise InterruptedError("Download stopped")
            try:
                with self.lock:
                    self.requests += 1
                with self.local.session.get(
                    url, headers=headers, stream=True, timeout=(self.timeout, self.timeout)
                ) as response:
                    if response.status_code == 429 or response.status_code >= 500:
                        response.raise_for_status()
                    if response.status_code != 206:
                        raise ValueError(
                            f"Expected HTTP 206 for {url}, got {response.status_code}. "
                            "Refusing a response that could download the entire archive."
                        )
                    match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", response.headers.get("Content-Range", ""))
                    if not match or (int(match[1]), int(match[2])) != (start, end):
                        raise ValueError("The server returned an incorrect Content-Range.")
                    metadata = {
                        "url": url,
                        "size": int(match[3]),
                        "etag": response.headers.get("ETag"),
                        "last_modified": response.headers.get("Last-Modified"),
                    }
                    if end >= metadata["size"]:
                        raise ValueError("The range extends beyond the archive.")
                    if identity and metadata != identity:
                        raise ValueError("The remote archive changed; rerun to rebuild its cached indexes.")
                    if response.headers.get("Content-Encoding", "identity") != "identity":
                        raise ValueError("Encoded HTTP responses cannot be used for tar offsets.")
                    chunks = []
                    received = 0
                    for chunk in response.iter_content(chunk_size=64 * 1024):
                        if self.stop.is_set():
                            raise InterruptedError("Download stopped")
                        received += len(chunk)
                        with self.lock:
                            self.bytes += len(chunk)
                        if received > end - start + 1:
                            raise ValueError("The server sent more bytes than requested.")
                        chunks.append(chunk)
                    if received != end - start + 1:
                        raise requests.exceptions.ChunkedEncodingError("Incomplete range response")
                    return b"".join(chunks), metadata
            except requests.RequestException as error:
                if attempt == self.retries:
                    raise RuntimeError(f"Range request failed after retries: {error}") from error
                if self.stop.wait(min(2 ** attempt, 8)):
                    raise InterruptedError("Download stopped") from error
        raise RuntimeError("Unreachable retry state")


class RemoteArchive:
    def __init__(self, client: RangeClient, url: str) -> None:
        self.client = client
        self.first_header, self.identity = client.fetch(url, 0, 511)
        if not self.identity["etag"] and not self.identity["last_modified"]:
            raise ValueError("The archive needs an ETag or Last-Modified value for reliable cache reuse.")
        self.size = self.identity["size"]

    def read(self, offset: int, size: int) -> bytes:
        if size <= 0 or offset < 0 or offset + size > self.size:
            raise ValueError(f"Invalid archive read: offset={offset}, size={size}")
        if offset == 0 and size == 512:
            return self.first_header
        return self.client.fetch(
            self.identity["url"], offset, offset + size - 1, self.identity
        )[0]


def parse_header(block: bytes) -> tarfile.TarInfo:
    member = tarfile.TarInfo.frombuf(block, "utf-8", "strict")
    if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
        raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
    return member


def index_members(
    source: RemoteArchive,
    cache: Path,
    start: int,
    scan_end: int,
    data_end: int,
    kind: str,
    needed: set[str],
    scan_chunk_size: int,
) -> dict:
    signature = {
        "version": 1, "source": source.identity, "start": start,
        "scan_end": scan_end, "data_end": data_end, "kind": kind,
    }
    state = {}
    if cache.is_file():
        state = json.loads(cache.read_text(encoding="utf-8"))
    if state.get("signature") != signature:
        state = {"signature": signature, "cursor": start,
                 "complete": False, "members": {}}
    if needed.issubset(state["members"]) or state["complete"]:
        return state["members"]
    processed = 0
    last_saved = time.monotonic()
    try:
        while state["cursor"] + 512 <= scan_end:
            if source.client.stop.is_set():
                raise InterruptedError("Indexing stopped")
            offset = state["cursor"]
            block_end = min(scan_end, offset + scan_chunk_size)
            block = source.read(offset, block_end - offset)
            relative = 0
            while relative + 512 <= len(block):
                header = block[relative : relative + 512]
                absolute = offset + relative
                if header == bytes(512):
                    state["complete"] = True
                    state["cursor"] = scan_end
                    break
                member = parse_header(header)
                name = PurePosixPath(member.name).name
                next_header = absolute + 512 + ((member.size + 511) // 512) * 512
                if member.size < 0 or next_header > data_end:
                    raise ValueError(f"Tar member exceeds its archive: {member.name}")
                if member.isfile() and PATTERNS[kind].fullmatch(name):
                    entry = {"offset": absolute + 512, "size": member.size}
                    if name in state["members"] and state["members"][name] != entry:
                        raise ValueError(f"Duplicate tar member name: {name}")
                    state["members"][name] = entry
                processed += 1
                # If the next header is outside this block, skip the unneeded
                # image payload and request the next block at that exact header.
                if next_header + 512 > block_end:
                    state["cursor"] = next_header
                    break
                relative = next_header - offset
                state["cursor"] = next_header
                if needed.issubset(state["members"]):
                    break
            else:
                state["cursor"] = block_end
            if state["complete"] or needed.issubset(state["members"]):
                break
            if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
                atomic_write(cache, json.dumps(state).encode("utf-8"))
                if kind == "classes":
                    print(f"Outer index: {len(state['members'])} classes cached; "
                          f"HTTP requests: {source.client.requests}", flush=True)
                last_saved = time.monotonic()
        if state["cursor"] + 512 > scan_end:
            state["complete"] = True
    finally:
        atomic_write(cache, json.dumps(state).encode("utf-8"))
    return state["members"]


def valid_image(path: Path, expected_size: int) -> bool:
    if not path.is_file() or path.stat().st_size != expected_size:
        return False
    try:
        with Image.open(path) as image:
            image.load()
        return True
    except (OSError, ValueError, Image.DecompressionBombError):
        return False


def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
    members = index_members(
        source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
    )
    found = {}
    downloaded = existing = 0
    for name in sorted(set(requested).intersection(members)):
        relative = requested[name]
        entry = members[name]
        if not (0 < entry["size"] <= 128 * 1024 * 1024):
            raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
        found[relative] = entry["size"]
        if args.index_only:
            continue
        destination = args.output_dir / relative
        if valid_image(destination, entry["size"]):
            existing += 1
            continue
        content = source.read(entry["offset"], entry["size"])
        with Image.open(io.BytesIO(content)) as image:
            image.load()
        atomic_write(destination, content)
        downloaded += 1
    return found, downloaded, existing


def process_val_partition(source, cache, start, end, requested, args):
    """Locate a checked tar header after a byte boundary, then scan this part."""
    first_header = None
    if cache.is_file():
        state = json.loads(cache.read_text(encoding="utf-8"))
        signature = state.get("signature", {})
        if (
            signature.get("source") == source.identity
            and signature.get("kind") == "val"
            and signature.get("scan_end") == end
            and start <= signature.get("start", -1) <= end
        ):
            first_header = signature["start"]
    if first_header is None:
        cursor = start
        while cursor + 512 <= end and first_header is None:
            block = source.read(cursor, min(256 * 1024, end - cursor))
            for relative in range(0, len(block) - 511, 512):
                header = block[relative:relative + 512]
                try:
                    member = parse_header(header)
                except (tarfile.TarError, ValueError, UnicodeError):
                    continue
                following = cursor + relative + 512 + ((member.size + 511) // 512) * 512
                if (
                    member.isfile() and PATTERNS["val"].fullmatch(member.name)
                    and 0 < member.size <= 128 * 1024 * 1024
                    and following + 512 <= source.size
                ):
                    # A checksum and the following header rule out JPEG payload
                    # bytes accidentally resembling a tar member at a boundary.
                    next_block = source.read(following, 512)
                    try:
                        next_member = None if next_block == bytes(512) else parse_header(next_block)
                    except (tarfile.TarError, ValueError, UnicodeError):
                        continue
                    if next_member is None or PATTERNS["val"].fullmatch(next_member.name):
                        first_header = cursor + relative
                        break
            cursor += len(block)
        if first_header is None:
            first_header = end
    return process_group(
        source, cache, first_header, end, source.size, "val", requested, args,
        512 if args.header_only else args.val_chunk_mib * 1024 * 1024,
    )


def val_jobs(source, requested, args):
    cache = args.index_dir / "val.json"
    legacy = json.loads(cache.read_text(encoding="utf-8")) if cache.is_file() else {}
    expected_signature = {
        "version": 1, "source": source.identity, "start": 0,
        "scan_end": source.size, "data_end": source.size, "kind": "val",
    }
    if legacy.get("signature") != expected_signature:
        legacy = {"cursor": 0, "members": {}, "complete": False}
    known = {name: path for name, path in requested.items() if name in legacy["members"]}
    jobs = []
    if known:
        jobs.append((process_group, source, cache, 0, source.size, source.size,
                     "val", known, args, 512))
    remaining = {name: path for name, path in requested.items() if name not in known}
    if remaining and not legacy["complete"]:
        start = legacy["cursor"]
        blocks = (source.size - start) // 512
        boundaries = [start + (blocks * part // args.val_parts) * 512
                      for part in range(args.val_parts + 1)]
        print(f"Validation: {len(known)} target offsets cached; "
              f"scanning the remainder in {args.val_parts} parts.", flush=True)
        for begin, end in zip(boundaries, boundaries[1:]):
            if begin < end:
                jobs.append((process_val_partition, source,
                             args.index_dir / "val_parts" / f"{begin}-{end}.json",
                             begin, end, remaining, args))
    return jobs


def run(args) -> int:
    names = load_manifest(args.manifest)
    if args.limit is not None:
        names = names[:args.limit]
    train = {}
    val = {}
    for name in names:
        parts = PurePosixPath(name).parts
        if parts[0] == "train":
            train.setdefault(parts[1] + ".tar", {})[parts[2]] = name
        else:
            val[parts[1]] = name
    client = RangeClient(args.timeout, args.retries)
    jobs = []
    if train:
        source = RemoteArchive(client, args.train_url)
        print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
        outer = index_members(
            source,
            args.index_dir / "train_outer.json",
            0,
            source.size,
            source.size,
            "classes",
            set(train),
            512,
        )
        missing_classes = sorted(set(train) - set(outer))
        if missing_classes:
            raise ValueError(f"Classes missing from training archive: {missing_classes}")
        class_bytes = sum(outer[name]["size"] for name in train)
        print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB.", flush=True)
        if args.header_only:
            print("Indexing headers only: low bandwidth, but many HTTP requests.", flush=True)
        else:
            print("Read-ahead indexing can transfer much of this data without storing it.", flush=True)
        for name, requested in sorted(train.items()):
            entry = outer[name]
            jobs.append((process_group, source, args.index_dir / "train" / f"{name}.json",
                         entry["offset"], entry["offset"] + entry["size"],
                         entry["offset"] + entry["size"], "train", requested, args,
                         512 if args.header_only else args.train_chunk_mib * 1024 * 1024))
    if val:
        source = RemoteArchive(client, args.val_url)
        jobs.extend(val_jobs(source, val, args))
    found = {}
    downloaded = existing = completed = 0
    errors = []
    executor = ThreadPoolExecutor(max_workers=args.workers)
    pending = {executor.submit(job[0], *job[1:]) for job in jobs}
    last_progress = time.monotonic()
    try:
        while pending:
            done, pending = wait(pending, timeout=10, return_when=FIRST_COMPLETED)
            for future in done:
                completed += 1
                try:
                    images, new, old = future.result()
                    if set(images).intersection(found):
                        raise ValueError("The same image appeared in more than one archive partition.")
                    found.update(images)
                    downloaded += new
                    existing += old
                except Exception as error:
                    errors.append(str(error))
                    print(f"Group failed; rerun will reuse saved progress: {error}", file=sys.stderr, flush=True)
            if done or time.monotonic() - last_progress >= 20:
                print(f"Groups {completed}/{len(jobs)}; images {len(found)}/{len(names)}; "
                      f"HTTP requests {client.requests}; received {client.bytes / 1024**2:.1f} MiB", flush=True)
                last_progress = time.monotonic()
    except BaseException:
        client.stop.set()
        raise
    finally:
        executor.shutdown(wait=True, cancel_futures=True)
    missing = sorted(set(names) - set(found))
    report = {
        "mode": "index_only" if args.index_only else "download",
        "requested_images": len(names), "completed_images": len(found),
        "downloaded_images": downloaded, "existing_images": existing,
        "selected_image_bytes": sum(found.values()), "http_requests": client.requests,
        "received_bytes": client.bytes, "missing_images": missing, "errors": errors,
    }
    atomic_write(args.index_dir / "last_run.json", json.dumps(report, indent=2).encode("utf-8"))
    print(f"Selected image bytes: {sum(found.values()) / 1024**3:.3f} GiB")
    print(f"Report: {args.index_dir / 'last_run.json'}")
    if missing or errors:
        print(f"Incomplete: {len(missing)} images; first missing paths: {missing[:10]}", file=sys.stderr)
        return 1
    action = "indexed" if args.index_only else "downloaded or verified"
    print(f"Complete: {len(names)} images {action}.")
    return 0


def main() -> int:
    data = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=data / "transfer_lists" / "imagenet_required.txt")
    parser.add_argument("--output-dir", type=Path, default=data / "ImageNet")
    parser.add_argument("--index-dir", type=Path, default=data / "imagenet_index")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--train-chunk-mib", type=int, default=8)
    parser.add_argument("--val-chunk-mib", type=int, default=64)
    parser.add_argument("--val-parts", type=int, default=32)
    parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
    parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
    parser.add_argument(
        "--header-only", action="store_true",
        help="Index with 512-byte header reads; less bandwidth, many more HTTP requests",
    )
    parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")
    parser.add_argument("--val-url", default=f"{BASE_URL}/ILSVRC2012_img_val.tar")
    args = parser.parse_args()
    if (
        not 1 <= args.workers <= 64
        or args.timeout <= 0
        or args.retries < 0
        or args.train_chunk_mib < 1
        or args.val_chunk_mib < 1
        or not 1 <= args.val_parts <= 128
    ):
        parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    for name in ("manifest", "output_dir", "index_dir"):
        setattr(args, name, getattr(args, name).expanduser().resolve())
    args.index_dir.mkdir(parents=True, exist_ok=True)
    with (args.index_dir / "download.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("Another download is already using this index directory.")
        return run(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted. Rerun the same command to reuse cached indexes and complete images.", file=sys.stderr)
        raise SystemExit(130)
    except (OSError, ValueError, RuntimeError, tarfile.TarError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
