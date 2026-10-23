"""Resume OCL web-image downloads and report unavailable images."""

import argparse
import json
import tempfile
import time
from pathlib import Path

import requests
from PIL import Image
from tqdm import tqdm


IMAGE_ERRORS = (OSError, ValueError, SyntaxError, Image.DecompressionBombError)


def validate_image(path):
    with Image.open(path) as image:
        image.load()


def download_image(session, url, destination, timeout=20, retries=2):
    """Return a status and failed attempts, preserving existing files on failure."""
    destination = Path(destination)
    if destination.is_file():
        try:
            validate_image(destination)
            return "skipped", []
        except IMAGE_ERRORS:
            pass

    destination.parent.mkdir(parents=True, exist_ok=True)
    # Many old HTTP image URLs now require HTTPS. Keep HTTP as a fallback.
    candidates = ["https://" + url[7:], url] if url.startswith("http://") else [url]
    errors = []
    for candidate in candidates:
        for attempt in range(retries + 1):
            temporary = None
            try:
                with session.get(
                    candidate, stream=True, timeout=(min(10, timeout), timeout)
                ) as response:
                    response.raise_for_status()
                    with tempfile.NamedTemporaryFile(
                        dir=destination.parent,
                        prefix="." + destination.name + ".",
                        suffix=".part",
                        delete=False,
                    ) as handle:
                        temporary = Path(handle.name)
                        for chunk in response.iter_content(chunk_size=65536):
                            handle.write(chunk)
                validate_image(temporary)
                # Publish only a complete, decodable image, on the same filesystem.
                temporary.replace(destination)
                return "downloaded", errors
            except (requests.RequestException,) + IMAGE_ERRORS as error:
                errors.append(
                    {"url": candidate, "attempt": attempt + 1, "error": str(error)}
                )
                retryable = isinstance(error, requests.RequestException)
                if isinstance(error, requests.HTTPError):
                    status = error.response.status_code
                    retryable = status in (408, 429) or 500 <= status < 600
                if not retryable or attempt == retries:
                    break
                time.sleep(min(2 ** attempt, 5))
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
    return "failed", errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-root", type=Path, default=Path(__file__).resolve().parent
    )
    parser.add_argument("--timeout", type=float, default=20, help="Socket timeout in seconds")
    parser.add_argument("--retries", type=int, default=2, help="Extra attempts per URL")
    parser.add_argument("--limit", type=int, help="Process only the first N entries")
    args = parser.parse_args(argv)
    if args.timeout <= 0 or args.retries < 0 or (args.limit is not None and args.limit <= 0):
        parser.error("timeout and limit must be positive; retries must be non-negative")

    root = args.data_root.expanduser().resolve()
    with (root / "resources" / "url_to_filename.json").open(encoding="utf-8") as handle:
        entries = json.load(handle)
    entries = entries[:args.limit]
    counts = {"downloaded": 0, "skipped": 0, "failed": 0}
    failures = []
    interrupted = False
    with requests.Session() as session:
        session.headers.update(
            {"User-Agent": "Mozilla/5.0 (compatible; OCL-image-downloader/1.0)"}
        )
        try:
            with tqdm(entries, desc="Web images", unit="image", ncols=100) as progress:
                for url, name in progress:
                    status, errors = download_image(
                        session, url, root / name, timeout=args.timeout, retries=args.retries
                    )
                    counts[status] += 1
                    if status == "failed":
                        failures.append({"url": url, "name": name, "attempts": errors})
                        tqdm.write("Failed {}: {}".format(name, errors[-1]["error"]))
                    progress.set_postfix(counts, refresh=False)
        except KeyboardInterrupt:
            interrupted = True

    report = {
        "requested": len(entries),
        **counts,
        "pending": len(entries) - sum(counts.values()),
        "interrupted": interrupted,
        "failures": failures,
    }
    report_path = root / "web_download_failures.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        "Downloaded: {downloaded}; already valid: {skipped}; failed: {failed}; "
        "pending: {pending}.".format(**report)
    )
    print("Report: {}. Rerun to retry missing or invalid images.".format(report_path))
    return 130 if interrupted else (1 if failures else 0)


if __name__ == "__main__":
    raise SystemExit(main())
