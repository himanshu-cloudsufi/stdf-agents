#!/usr/bin/env python3
"""Token-based keyword search over data/index.json."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data" / "index.json"


def normalize(text: str) -> str:
    """Lowercase, replace hyphens/underscores with spaces, collapse whitespace."""
    return text.lower().replace('-', ' ').replace('_', ' ').strip()


def load_index():
    with open(INDEX) as f:
        return json.load(f)


def search(entries, query: str):
    """Score entries by token match count against dataset_name + description."""
    tokens = normalize(query).split()
    if not tokens:
        return entries

    scored = []
    for entry in entries:
        text = normalize(
            f"{entry.get('dataset_name', '')} {entry.get('description', '')}"
        )
        hits = sum(1 for t in tokens if t in text)
        if hits > 0:
            scored.append((hits, entry))
    scored.sort(key=lambda x: -x[0])
    return [e for _, e in scored]


def filter_entries(entries, type_=None, sector=None, region=None, units=None):
    result = entries
    if type_:
        t = type_.lower()
        result = [e for e in result if e.get("type", "").lower() == t]
    if sector:
        s = sector.lower()
        result = [e for e in result if s in e.get("level_name", "").lower()]
    if region:
        r = region.lower()
        result = [e for e in result if r in e.get("region", "").lower()]
    if units:
        u = units.lower()
        result = [e for e in result if u in e.get("units", "").lower()]
    return result


def print_table(entries, detail=False):
    print(f"**Found {len(entries)} curve(s)**\n")
    print("| # | Dataset | Type | Units | Region | Sector | Source | File |")
    print("|---|---------|------|-------|--------|--------|--------|------|")
    for i, e in enumerate(entries, 1):
        print(
            f"| {i} | {e['dataset_name']} | {e.get('type', '')} | "
            f"{e.get('units', '')} | {e.get('region', '')} | "
            f"{e.get('level_name', '')} | {e.get('source', '')} | "
            f"`{e.get('file_path', '')}`|"
        )
    print()

    if detail:
        for e in entries:
            fp = (ROOT / e.get("file_path", "")).resolve()
            # Prevent path traversal outside project root
            if not str(fp).startswith(str(ROOT.resolve())):
                print(f"Skipping unsafe path: {e.get('file_path', '')}")
                continue
            if fp.exists():
                with open(fp) as f:
                    curve = json.load(f)
                print(f"### {e['dataset_name']}")
                print(f"- **Description:** {e.get('description', 'N/A')}")
                print(f"- **Type:** {e.get('type', 'N/A')}")
                print(f"- **Units:** {e.get('units', 'N/A')}")
                print(f"- **Region:** {e.get('region', 'N/A')}")
                print(f"- **Sector:** {e.get('level_name', 'N/A')}")
                print(f"- **Source:** {e.get('source', 'N/A')}")
                print()
                if "X" in curve and "Y" in curve:
                    print("| Year | Value |")
                    print("|------|-------|")
                    for x, y in zip(curve["X"], curve["Y"]):
                        print(f"| {x} | {y} |")
                    print()


def list_field(entries, field: str, label: str):
    counts = {}
    for e in entries:
        val = e.get(field, "") or ""
        if val:
            counts[val] = counts.get(val, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: -x[1])
    print(f"| {label} | Count |")
    print("|---|---|")
    for val, count in sorted_items:
        print(f"| {val} | {count} |")


def main():
    parser = argparse.ArgumentParser(description="Query STDF curves data catalog")
    parser.add_argument("--search", help="Keyword search (dataset name + description)")
    parser.add_argument("--type", dest="type_", help="Filter by curve type")
    parser.add_argument("--sector", help="Filter by sector (level_name)")
    parser.add_argument("--region", help="Filter by region")
    parser.add_argument("--units", help="Filter by units")
    parser.add_argument("--dataset", help="Exact dataset name lookup")
    parser.add_argument("--detail", action="store_true", help="Show full X/Y data")
    parser.add_argument("--limit", type=int, default=20, help="Max results (default: 20)")
    parser.add_argument("--list-sectors", action="store_true", help="List all sectors")
    parser.add_argument("--list-types", action="store_true", help="List all curve types")
    parser.add_argument("--list-regions", action="store_true", help="List all regions")
    args = parser.parse_args()

    entries = load_index()

    # List modes
    if args.list_sectors:
        list_field(entries, "level_name", "Sector")
        return
    if args.list_types:
        list_field(entries, "type", "Type")
        return
    if args.list_regions:
        list_field(entries, "region", "Region")
        return

    # Exact dataset lookup
    if args.dataset:
        matches = [e for e in entries if e["dataset_name"] == args.dataset]
        if not matches:
            # Fallback: case-insensitive substring
            d = args.dataset.lower()
            matches = [e for e in entries if d in e["dataset_name"].lower()]
        if not matches:
            print(f"No dataset found matching '{args.dataset}'")
            return
        print_table(matches, detail=args.detail)
        return

    # Search + filter
    if args.search:
        entries = search(entries, args.search)
    entries = filter_entries(entries, args.type_, args.sector, args.region, args.units)

    if not entries:
        print("No matching curves found.")
        return

    entries = entries[:args.limit]
    print_table(entries, detail=args.detail)


if __name__ == "__main__":
    main()
