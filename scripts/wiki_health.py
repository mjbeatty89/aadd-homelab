#!/usr/bin/env python3
"""Lightweight health checks for the em0lab Obsidian wiki."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IGNORED_DIRS = {
    ".git",
    ".obsidian",
    ".smart-env",
    ".site",
    ".site-src",
    "Logs",
    "Sources/Raw",
    "images",
}

IGNORED_PATHS = {
    ("Projects", "Proposal"),
    ("Projects", "2026 Taxes.md"),
}

DURABLE_FRONTMATTER_DIRS = {
    "Wiki",
    "Schemas",
}

REQUIRED_FRONTMATTER_KEYS = {
    "type",
    "status",
    "owner",
    "created",
    "updated",
    "tags",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in IGNORED_DIRS for part in rel_parts):
            continue
        if any(rel_parts[: len(prefix)] == prefix for prefix in IGNORED_PATHS):
            continue
        files.append(path)
    return sorted(files)


def note_names(markdown_files: list[Path]) -> set[str]:
    names: set[str] = set()
    for path in markdown_files:
        rel = path.relative_to(ROOT).with_suffix("")
        names.add(str(rel))
        names.add(path.stem)
    return names


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def frontmatter_keys(text: str) -> set[str]:
    if not has_frontmatter(text):
        return set()
    block = text.split("\n---\n", 1)[0].removeprefix("---\n")
    keys: set[str] = set()
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            keys.add(line.split(":", 1)[0].strip())
    return keys


def needs_frontmatter(path: Path) -> bool:
    rel_parts = path.relative_to(ROOT).parts
    return rel_parts[0] in DURABLE_FRONTMATTER_DIRS


def check_frontmatter(markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in markdown_files:
        if not needs_frontmatter(path):
            continue
        text = path.read_text(encoding="utf-8")
        keys = frontmatter_keys(text)
        missing = REQUIRED_FRONTMATTER_KEYS - keys
        if missing:
            errors.append(
                f"{path.relative_to(ROOT)} missing frontmatter keys: "
                + ", ".join(sorted(missing))
            )
    return errors


def check_wikilinks(markdown_files: list[Path], names: set[str]) -> list[str]:
    errors: list[str] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            if target not in names:
                errors.append(f"{path.relative_to(ROOT)} has broken wikilink [[{target}]]")
    return errors


def main() -> int:
    markdown_files = iter_markdown_files()
    names = note_names(markdown_files)
    errors = []
    errors.extend(check_frontmatter(markdown_files))
    errors.extend(check_wikilinks(markdown_files, names))

    if errors:
        print("wiki-health found issues:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"wiki-health passed: {len(markdown_files)} markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
