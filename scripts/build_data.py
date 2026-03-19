#!/usr/bin/env python3
"""Split curves_catalog.json into per-curve files and build data/index.json."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "curves_catalog.json"
OVERRIDES = ROOT / "data" / "overrides.json"
DATA_DIR = ROOT / "data"


def sanitize_filename(name: str) -> str:
    """Replace characters unsafe for filenames: / + % : & @"""
    return re.sub(r'[/+%:&@]', '_', name)


def slugify(value: str) -> str:
    """Convert a field value to a directory slug: lowercase, spaces/hyphens to underscores.

    Strips path separators and '..' to prevent path traversal.
    """
    slug = value.strip().lower().replace(' ', '_').replace('-', '_')
    # Remove path traversal and separator characters
    slug = slug.replace('..', '').replace('/', '').replace('\\', '')
    return slug


def main():
    with open(CATALOG) as f:
        curves = json.load(f)

    # Load overrides if present
    overrides = {}
    if OVERRIDES.exists():
        with open(OVERRIDES) as f:
            overrides = json.load(f)

    # Apply overrides
    for curve in curves:
        name = curve["dataset_name"]
        if name in overrides:
            for field, value in overrides[name].items():
                curve[field] = value

    index = []
    sector_dirs = set()

    for curve in curves:
        sector_slug = slugify(curve.get("level_name", "") or "unknown")
        type_slug = slugify(curve.get("type", "") or "unknown")
        safe_name = sanitize_filename(curve["dataset_name"])

        rel_path = f"data/{sector_slug}/{type_slug}/{safe_name}.json"
        abs_path = ROOT / rel_path

        # Write individual curve file
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        with open(abs_path, "w") as f:
            json.dump(curve, f, indent=2)

        sector_dirs.add(sector_slug)

        # Build index entry (no X/Y)
        entry = {k: v for k, v in curve.items() if k not in ("X", "Y")}
        entry["file_path"] = rel_path
        index.append(entry)

    # Write index
    index_path = DATA_DIR / "index.json"
    with open(index_path, "w") as f:
        json.dump(index, f, indent=2)

    print(f"{len(curves)} curves written to {len(sector_dirs)} sector dirs")
    print(f"Index: {index_path} ({len(index)} entries)")


if __name__ == "__main__":
    main()
