"""Resume only the web images needed by the OCL top-ten evaluation."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import json
from pathlib import Path
import threading

import requests

from download_imagenet_subset import atomic_write
from download_web_images import IMAGE_ERRORS, download_image, validate_image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=12)
    parser.add_argument("--retries", type=int, default=1)
    args = parser.parse_args()
    if not 1 <= args.workers <= 32 or args.timeout <= 0 or args.retries < 0:
        parser.error("Use 1..32 workers, a positive timeout, and non-negative retries.")
    root = Path(__file__).resolve().parent
    reports = root / "transfer_lists"
    with (reports / "web_download.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SystemExit("A selected-web download is already running.")
        required = {
            name for name in (reports / "ocl_non_imagenet.txt").read_text().splitlines()
            if name.startswith("from_web/")
        }
        entries = json.loads((root / "resources/url_to_filename.json").read_text())
        urls = {name: url for url, name in entries}
        local = threading.local()

        def fetch(name):
            if (root / name).is_file():
                try:
                    validate_image(root / name)
                    return name, "skipped", []
                except IMAGE_ERRORS:
                    pass
            if name not in urls:
                return name, "failed", [{"error": "No source URL in OCL metadata"}]
            if not hasattr(local, "session"):
                local.session = requests.Session()
                local.session.headers["User-Agent"] = "Mozilla/5.0 (compatible; OCL-image-downloader/1.0)"
            status, errors = download_image(
                local.session, urls[name], root / name,
                timeout=args.timeout, retries=args.retries,
            )
            return name, status, errors

        counts = {"downloaded": 0, "skipped": 0, "failed": 0}
        failures = []
        report = reports / "web_download_report.json"

        def save():
            result = {
                "requested": len(required), **counts,
                "pending": len(required) - sum(counts.values()),
                "failures": sorted(failures, key=lambda item: item["name"]),
            }
            atomic_write(report, (json.dumps(result, indent=2) + "\n").encode())

        try:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = [pool.submit(fetch, name) for name in sorted(required)]
                for future in as_completed(futures):
                    name, status, errors = future.result()
                    counts[status] += 1
                    if status == "failed":
                        failures.append({"name": name, "url": urls.get(name), "attempts": errors})
                    completed = sum(counts.values())
                    if completed % 25 == 0 or completed == len(required):
                        save()
                        print(f"Web images {completed}/{len(required)}: {counts}", flush=True)
        finally:
            save()
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
