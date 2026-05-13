#!/usr/bin/env python3
"""Prepare a temporary MkDocs source tree from tracked vault files."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"

COPY_FILES = [
    "Home.md",
    "AGENTS.md",
    "CLAUDE.md",
    "TASKS.md",
    "README.md",
]

COPY_DIRS = [
    "Areas",
    "Projects",
    "Resources",
    "Schemas",
    "Templates",
    "memory",
    "Excalidraw",
    "images",
]

EXCLUDED_PREFIXES = {
    ("Projects", "2026 Taxes.md"),
    ("Projects", "Proposal"),
}


def copy_path(rel_path: str) -> None:
    src = ROOT / rel_path
    dest = DEST / rel_path
    if src.is_dir():
        shutil.copytree(src, dest)
    elif src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def prune_excluded_paths() -> None:
    for prefix in EXCLUDED_PREFIXES:
        target = DEST.joinpath(*prefix)
        if target.is_dir():
            shutil.rmtree(target, ignore_errors=True)
        elif target.exists():
            target.unlink()


def main() -> int:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True, exist_ok=True)

    for rel_path in COPY_FILES:
        copy_path(rel_path)
    for rel_path in COPY_DIRS:
        copy_path(rel_path)
    prune_excluded_paths()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
