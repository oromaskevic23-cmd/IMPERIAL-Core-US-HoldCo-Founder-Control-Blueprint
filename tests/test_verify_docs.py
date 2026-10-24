"""Tests for public-document integrity validation (standard library only)."""
import tempfile
import unittest
from pathlib import Path

from tools.verify_docs import local_target, validate


class LinkChecks(unittest.TestCase):
    def test_internal_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "docs" / "sample.md"
            self.assertEqual(local_target(source, "../README.md#top", root), root / "README.md")

    def test_anchor_only(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertIsNone(local_target(root / "README.md", "#section", root))

    def test_remote_is_not_a_local_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertIsNone(local_target(root / "README.md", "https://github.com/", root))

    def test_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            root.mkdir()
            with self.assertRaises(ValueError):
                local_target(root / "docs" / "link.md", "../../../etc/passwd", root)

    def test_empty_repository_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            errors = validate(Path(temp))
            self.assertTrue(any("MISSING REQUIRED: README.md" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
