"""Recover missing OCL web originals from their CDN alias or public archives."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import io
import json
from pathlib import Path
import pickle
import threading
import time
from urllib.parse import urlsplit, urlunsplit

from PIL import Image
import requests

from download_imagenet_subset import atomic_write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retry-transient", action="store_true")
    parser.add_argument("--request-delay", type=float, default=2.0)
    parser.add_argument("--timeout", type=float, default=20)
    args = parser.parse_args()
    if args.request_delay < 1 or args.timeout <= 0:
        parser.error("Use a request delay of at least one second and a positive timeout")
    root = Path(__file__).resolve().parent
    reports = root / "transfer_lists"
    report_path = reports / "web_recovery_report.json"
    previous = json.loads(report_path.read_text()) if report_path.is_file() else {}
    saved_results = {r["name"]: r for r in previous.get("results", [])}
    wanted = {n for n in (reports / "ocl_non_imagenet.txt").read_text().splitlines()
              if n.startswith("from_web/")}
    categories = set(json.loads((reports / "selection.json").read_text())["selected_categories"])
    boxes = {}
    for split in ("train", "val", "test"):
        with (root / "resources" / f"OCL_annot_{split}.pkl").open("rb") as handle:
            for row in pickle.load(handle):
                if row["name"] in wanted:
                    boxes.setdefault(row["name"], []).extend(
                        obj["box"] for obj in row["objects"]
                        if obj["obj"] in categories and "box" in obj
                    )
    urls = {name: url for url, name in
            json.loads((root / "resources/url_to_filename.json").read_text())}

    def validate(content, name):
        with Image.open(io.BytesIO(content)) as image:
            image.load()
            width, height = image.size
            for left, top, right, bottom in boxes.get(name, []):
                if right > left and bottom > top and (
                    min(width, right) <= max(0, left) or min(height, bottom) <= max(0, top)
                ):
                    raise ValueError("Image dimensions cannot contain an annotated object")

    pending = []
    for name in sorted(wanted):
        try:
            validate((root / name).read_bytes(), name)
        except (OSError, ValueError, SyntaxError, Image.DecompressionBombError):
            pending.append(name)
    if args.retry_transient:
        pending = [name for name in pending if name not in saved_results or any(
            token in attempt.get("error", "")
            for attempt in saved_results[name].get("attempts", [])
            for token in ("429", "500", "502", "503", "504", "timed out", "Connection", "SSL")
        )]
    local = threading.local()
    schedule_lock = threading.Lock()
    next_request = 0.0

    def get(session, url, **kwargs):
        nonlocal next_request
        with schedule_lock:
            when = max(time.monotonic(), next_request)
            next_request = when + args.request_delay
        time.sleep(max(0, when - time.monotonic()))
        return session.get(url, **kwargs)

    def recover(name):
        result = {"name": name, "original_url": urls.get(name), "attempts": []}
        if name not in urls:
            return {**result, "status": "unavailable", "error": "No URL in official mapping"}
        if not hasattr(local, "session"):
            local.session = requests.Session()
            local.session.headers["User-Agent"] = "Mozilla/5.0 (compatible; OCL-image-recovery/1.0)"
        session = local.session

        def fetch_image(url):
            try:
                with get(session, url, stream=True, timeout=(8, args.timeout)) as response:
                    response.raise_for_status()
                    content = bytearray()
                    for block in response.iter_content(65536):
                        content.extend(block)
                        if len(content) > 32 * 1024 * 1024:
                            raise ValueError("Image response exceeds 32 MiB")
                validate(content, name)
                atomic_write(root / name, content)
                result.update(status="recovered", recovered_from=url, size_bytes=len(content))
                return True
            except (requests.RequestException, OSError, ValueError, SyntaxError,
                    Image.DecompressionBombError) as error:
                result["attempts"].append({"url": url, "error": str(error)})
                return False

        parts = urlsplit(urls[name])
        if parts.netloc.endswith(".images-amazon.com"):
            alias = urlunsplit(("https", "m.media-amazon.com", parts.path, parts.query, ""))
            if fetch_image(alias):
                return result
        # Request an archived copy of this exact original URL, preserving the
        # annotated image identity rather than substituting a similar photo.
        try:
            response = get(session, "https://archive.org/wayback/available",
                                   params={"url": urls[name], "timestamp": "20220101"},
                                   timeout=(8, args.timeout))
            response.raise_for_status()
            snapshot = response.json().get("archived_snapshots", {}).get("closest")
            if snapshot and snapshot.get("available") and str(snapshot.get("status")) == "200":
                stamp = snapshot["timestamp"]
                if not stamp.isdigit():
                    raise ValueError("Invalid archive timestamp")
                archived = f"https://web.archive.org/web/{stamp}id_/{urls[name]}"
                result["snapshot"] = snapshot
                if fetch_image(archived):
                    return result
            else:
                result["attempts"].append({"source": "Internet Archive", "error": "No snapshot available"})
        except (requests.RequestException, ValueError) as error:
            result["attempts"].append({"source": "Internet Archive", "error": str(error)})
        return {**result, "status": "unavailable"}

    with (reports / "web_download.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SystemExit("Another selected-web download is running")
        results = dict(saved_results)
        completed = 0
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = [pool.submit(recover, name) for name in pending]
            for future in as_completed(futures):
                result = future.result()
                results[result["name"]] = result
                completed += 1
                report = {"requested": len(set(saved_results) | set(pending)),
                          "recovered": sum(r["status"] == "recovered" for r in results.values()),
                          "pending": len(pending) - completed,
                          "results": sorted(results.values(), key=lambda r: r["name"])}
                atomic_write(report_path,
                             (json.dumps(report, indent=2) + "\n").encode())
                if completed % 10 == 0 or completed == len(pending):
                    print(f"Recovery {completed}/{len(pending)}; recovered {report['recovered']}", flush=True)
        return 1 if any(r["status"] == "unavailable" for r in results.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
