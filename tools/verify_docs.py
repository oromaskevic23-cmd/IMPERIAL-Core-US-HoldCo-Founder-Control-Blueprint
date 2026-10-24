#!/usr/bin/env python3
"""Reproducible public-docs hygiene checks (stdlib only).

Checks evidence-bearing DOCUMENTATION, not actual runtime security or corporate legality.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "README.md",
    "ARCHITECTURE.md",
    "founder.html",
    "index.html",
    "assets/site.css",
    "docs/FOUNDER_PROFILE.md",
    "docs/US_HOLDCO_EQUITY.md",
    "docs/GOVERNANCE.md",
    "docs/ENTERPRISE_PORTFOLIO_AUDIT.md",
    "docs/UNIVERSAL_NCA_CORPORATION.md",
)
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")
HTML_LINK = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
JSON_LD = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.I | re.S,
)
BANNED_VARIANTS = re.compile(r"\b(?:Veleon\s+Max|Velion\s+Max)\b", re.I)


def local_target(source: Path, url: str, root: Path) -> Path | None:
    """Return a local path, rejecting path escape; ignore remote and anchor-only URLs."""
    url = url.strip().split(" ", 1)[0]
    parts = urlsplit(url)
    if not parts.path or parts.scheme or parts.netloc or url.startswith("//"):
        return None
    path = unquote(parts.path)
    if path.startswith("/"):
        return None  # Site-root URLs may use future production domains
    dest = (source.parent / path).resolve()
    if not dest.is_relative_to(root.resolve()):
        raise ValueError(f"relative link escapes repository: {url}")
    return dest


def validate(root: Path) -> list[str]:
    issues: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            issues.append(f"MISSING REQUIRED: {name}")

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for link in MARKDOWN_LINK.findall(content):
            try:
                dest = local_target(path, link, root)
                if dest is not None and not dest.exists():
                    issues.append(f"{path.relative_to(root)}: broken local link {link}")
            except ValueError as exc:
                issues.append(f"{path.relative_to(root)}: {exc}")

    for name in ("index.html", "founder.html"):
        path = root / name
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        if "<title>" not in content or 'name="description"' not in content:
            issues.append(f"{name}: missing title or search description")
        matches = JSON_LD.findall(content)
        if len(matches) != 1:
            issues.append(f"{name}: expected exactly one JSON-LD block")
        for payload in matches:
            try:
                data = json.loads(payload)
                if data.get("@context") != "https://schema.org":
                    issues.append(f"{name}: missing schema.org context")
                if name == "founder.html":
                    person = data.get("mainEntity", {})
                    if data.get("@type") != "ProfilePage" or person.get("@type") != "Person":
                        issues.append(f"{name}: not a ProfilePage of a Person")
                    if person.get("name") != "Alexander Romaskevich":
                        issues.append(f"{name}: canonical author mismatch")
            except (ValueError, AttributeError, TypeError) as exc:
                issues.append(f"{name}: invalid JSON-LD ({exc})")
        for link in HTML_LINK.findall(content):
            try:
                dest = local_target(path, link, root)
                if dest is not None and not dest.exists():
                    issues.append(f"{name}: broken local asset/link {link}")
            except ValueError as exc:
                issues.append(f"{name}: {exc}")

    if (root / "README.md").is_file():
        text = (root / "README.md").read_text(encoding="utf-8")
        if "VELEON" not in text or "NCA" not in text:
            issues.append("README.md: missing VELEON or NCA canonical terms")
        if "proposed" not in text.lower():
            issues.append("README.md: missing proposed-status legal qualification")

    for name in ("README.md", "ARCHITECTURE.md", "docs/FOUNDER_PROFILE.md"):
        p = root / name
        if p.is_file() and BANNED_VARIANTS.search(p.read_text(encoding="utf-8")):
            issues.append(f"{name}: obsolete intelligence name found")

    return issues


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    issues = validate(root)
    if issues:
        for problem in issues:
            print("FAIL:", problem)
        return 1
    print("PASS: required documents, links, local assets, founder JSON-LD and canonical naming")
    print("NOTE: This does not verify deployment, legal incorporation, photo indexing, or runtime security.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
