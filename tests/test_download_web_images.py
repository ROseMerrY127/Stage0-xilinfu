"""Offline download regressions; no remote hosts or model weights required."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests
from PIL import Image

from data import download_web_images as downloader


def image_bytes():
    buffer = io.BytesIO()
    Image.new("RGB", (4, 4), "red").save(buffer, format="JPEG")
    return buffer.getvalue()


def response(status=200, body=None, url="https://example.org/image.jpg"):
    result = requests.Response()
    result.status_code = status
    result.url = url
    result._content = image_bytes() if body is None else body
    result._content_consumed = True
    return result


class DownloadTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.target = self.root / "from_web" / "image.jpg"
        self.session = Mock()

    def test_http_urls_try_https_first_and_use_timeouts(self):
        self.session.get.return_value = response()
        status, errors = downloader.download_image(
            self.session, "http://example.org/image.jpg", self.target, timeout=3
        )
        self.assertEqual((status, errors), ("downloaded", []))
        self.session.get.assert_called_once_with(
            "https://example.org/image.jpg", stream=True, timeout=(3, 3)
        )
        downloader.validate_image(self.target)
        self.assertEqual(list(self.target.parent.iterdir()), [self.target])

    def test_https_failure_falls_back_to_original_url(self):
        self.session.get.side_effect = [response(404), response()]
        status, errors = downloader.download_image(
            self.session, "http://example.org/image.jpg", self.target
        )
        self.assertEqual(status, "downloaded")
        self.assertEqual(len(errors), 1)
        self.assertIn("404", errors[0]["error"])
        self.assertEqual(self.session.get.call_args.args[0], "http://example.org/image.jpg")

    def test_existing_valid_image_is_preserved_without_network(self):
        self.target.parent.mkdir()
        self.target.write_bytes(image_bytes())
        old_bytes = self.target.read_bytes()
        status, _ = downloader.download_image(self.session, "https://example.org/image.jpg", self.target)
        self.assertEqual(status, "skipped")
        self.session.get.assert_not_called()
        self.assertEqual(self.target.read_bytes(), old_bytes)

    def test_successful_html_response_is_rejected(self):
        self.session.get.return_value = response(body=b"<html>Access denied</html>")
        status, errors = downloader.download_image(self.session, "https://example.org/image.jpg", self.target)
        self.assertEqual(status, "failed")
        self.assertTrue(errors)
        self.assertFalse(self.target.exists())
        self.assertEqual(list(self.target.parent.iterdir()), [])

    def test_corrupt_existing_file_is_replaced_by_valid_image(self):
        self.target.parent.mkdir()
        self.target.write_bytes(b"broken image")
        self.session.get.return_value = response()
        status, _ = downloader.download_image(self.session, "https://example.org/image.jpg", self.target)
        self.assertEqual(status, "downloaded")
        downloader.validate_image(self.target)

    def test_truncated_download_does_not_publish_partial_file(self):
        broken = response()

        def chunks(**kwargs):
            yield b"partial image"
            raise requests.ConnectionError("connection dropped")

        broken.iter_content = chunks
        self.session.get.return_value = broken
        status, _ = downloader.download_image(
            self.session, "https://example.org/image.jpg", self.target, retries=0
        )
        self.assertEqual(status, "failed")
        self.assertFalse(self.target.exists())
        self.assertEqual(list(self.target.parent.iterdir()), [])

    @patch.object(downloader.time, "sleep")
    def test_timeout_and_server_error_are_retried(self, sleep):
        self.session.get.side_effect = [requests.Timeout("timed out"), response(503), response()]
        status, errors = downloader.download_image(self.session, "https://example.org/image.jpg", self.target)
        self.assertEqual(status, "downloaded")
        self.assertEqual(len(errors), 2)
        self.assertEqual(self.session.get.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    @patch.object(downloader.time, "sleep")
    def test_retries_are_bounded(self, sleep):
        self.session.get.side_effect = requests.Timeout("timed out")
        status, errors = downloader.download_image(
            self.session, "https://example.org/image.jpg", self.target, retries=1
        )
        self.assertEqual(status, "failed")
        self.assertEqual(len(errors), 2)
        self.assertEqual(self.session.get.call_count, 2)
        sleep.assert_called_once_with(1)

    def run_main(self, effects, entries):
        resources = self.root / "resources"
        resources.mkdir()
        (resources / "url_to_filename.json").write_text(json.dumps(entries))
        self.session.get.side_effect = effects
        with patch.object(downloader.requests, "Session") as session_factory:
            session_factory.return_value.__enter__.return_value = self.session
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                code = downloader.main(["--data-root", str(self.root), "--retries", "0"])
        report = json.loads((self.root / "web_download_failures.json").read_text())
        return code, report

    def test_batch_continues_after_404_and_reports_original_mapping(self):
        entries = [
            ["https://example.org/missing.jpg", "from_web/missing.jpg"],
            ["https://example.org/good.jpg", "from_web/good.jpg"],
        ]
        code, report = self.run_main([response(404), response()], entries)
        self.assertEqual(code, 1)
        self.assertEqual(report["downloaded"], 1)
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["pending"], 0)
        self.assertEqual(report["failures"][0]["url"], entries[0][0])
        self.assertEqual(report["failures"][0]["name"], entries[0][1])
        self.assertIn("404", report["failures"][0]["attempts"][0]["error"])
        downloader.validate_image(self.root / entries[1][1])

    def test_interrupt_saves_failure_report_and_pending_count(self):
        entries = [
            ["https://example.org/missing.jpg", "from_web/missing.jpg"],
            ["https://example.org/pending.jpg", "from_web/pending.jpg"],
        ]
        code, report = self.run_main([response(404), KeyboardInterrupt()], entries)
        self.assertEqual(code, 130)
        self.assertTrue(report["interrupted"])
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["pending"], 1)


if __name__ == "__main__":
    unittest.main()
