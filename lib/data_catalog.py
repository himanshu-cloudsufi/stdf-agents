"""Data catalog access for the STDF v2 empirical time series curves.

Provides programmatic access to the 956 curated curves stored in data/.
Used by agents: domain-disruption, cost-curve, capability, adoption-scurve.

Usage:
    from lib.data_catalog import search_curves, load_curve, get_xy_data

    results = search_curves("lithium-ion battery", type_="cost")
    curve = load_curve(results[0]["file_path"])
    x, y = get_xy_data(results[0]["file_path"])
"""

import json
from functools import lru_cache
from pathlib import Path
from typing import Optional

_DEFAULT_ROOT = Path(__file__).resolve().parent.parent


def _resolve_root(root: Optional[Path] = None) -> Path:
    """Return the project root directory."""
    return Path(root) if root is not None else _DEFAULT_ROOT


@lru_cache(maxsize=1)
def _cached_index(index_path: str) -> list[dict]:
    """Internal cached loader keyed by resolved index path string."""
    with open(index_path) as f:
        return json.load(f)


def load_index(root: Optional[Path] = None) -> list[dict]:
    """Load and return the full index manifest (metadata only, no X/Y data).

    Results are cached at the module level after the first call.

    Args:
        root: Project root directory. Defaults to two levels up from this file.

    Returns:
        List of metadata dicts, one per curve. Each dict contains:
        dataset_name, type, units, region, level_name, source, description, file_path.
    """
    index_path = _resolve_root(root) / "data" / "index.json"
    return _cached_index(str(index_path))


def _normalize(text: str) -> str:
    """Lowercase text, replace hyphens/underscores with spaces, collapse whitespace."""
    return text.lower().replace("-", " ").replace("_", " ").strip()


def search_curves(
    query: str,
    type_: Optional[str] = None,
    sector: Optional[str] = None,
    region: Optional[str] = None,
    limit: int = 20,
    root: Optional[Path] = None,
) -> list[dict]:
    """Token-based keyword search over index entries.

    Matches query tokens against each entry's dataset_name + description.
    Results are sorted by number of token hits (descending).

    Args:
        query: Space-separated keywords to search for.
        type_: Filter by curve type (e.g. "cost", "adoption", "capability").
        sector: Filter by sector / level_name (substring match).
        region: Filter by region (substring match).
        limit: Maximum number of results to return. Defaults to 20.
        root: Project root directory.

    Returns:
        List of metadata dicts matching the query, sorted by relevance.
    """
    entries = load_index(root)

    # Apply filters first to narrow the search space
    entries = _filter_entries(entries, type_=type_, sector=sector, region=region)

    # Tokenize query and score
    tokens = _normalize(query).split()
    if not tokens:
        return entries[:limit]

    scored = []
    for entry in entries:
        text = _normalize(
            f"{entry.get('dataset_name', '')} {entry.get('description', '')}"
        )
        hits = sum(1 for t in tokens if t in text)
        if hits > 0:
            scored.append((hits, entry))

    scored.sort(key=lambda x: -x[0])
    return [entry for _, entry in scored[:limit]]


def _filter_entries(
    entries: list[dict],
    type_: Optional[str] = None,
    sector: Optional[str] = None,
    region: Optional[str] = None,
) -> list[dict]:
    """Apply optional filters to a list of index entries.

    All filter comparisons are case-insensitive. Sector and region use
    substring matching; type uses exact matching.
    """
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
    return result


def load_curve(file_path: str, root: Optional[Path] = None) -> dict:
    """Load a single curve JSON file with full X/Y arrays.

    Args:
        file_path: Relative path from the project root (as stored in index.json),
                   e.g. "data/5g_network/adoption/5G_Network_5G_Coverage_Land_Area_China.json".
        root: Project root directory.

    Returns:
        Full curve dict including dataset_name, description, X, Y, type, units,
        source, region, category, entity_type, level_name.
    """
    resolved_root = _resolve_root(root)
    full_path = (resolved_root / file_path).resolve()
    # Prevent path traversal outside project root
    if not str(full_path).startswith(str(resolved_root.resolve())):
        raise ValueError(f"Path traversal detected: {file_path} escapes project root")
    with open(full_path) as f:
        return json.load(f)


def get_curves_by_sector(
    sector: str,
    type_: Optional[str] = None,
    root: Optional[Path] = None,
) -> list[dict]:
    """Get all index entries for a sector, optionally filtered by type.

    Args:
        sector: Sector name (level_name) to match (case-insensitive substring).
        type_: Optional curve type filter (exact match).
        root: Project root directory.

    Returns:
        List of matching metadata dicts (no X/Y data).
    """
    entries = load_index(root)
    return _filter_entries(entries, type_=type_, sector=sector)


def get_xy_data(
    file_path: str, root: Optional[Path] = None
) -> tuple[list, list]:
    """Load a curve file and return just the (X, Y) arrays.

    Args:
        file_path: Relative path from the project root (as stored in index.json).
        root: Project root directory.

    Returns:
        Tuple of (X, Y) where X and Y are lists (typically years and values).

    Raises:
        KeyError: If the curve file does not contain X or Y fields.
    """
    curve = load_curve(file_path, root)
    return curve["X"], curve["Y"]


def list_sectors(root: Optional[Path] = None) -> list[str]:
    """Return sorted unique sector names (level_name) from the index.

    Args:
        root: Project root directory.

    Returns:
        Sorted list of unique sector name strings.
    """
    entries = load_index(root)
    sectors = {e.get("level_name", "") for e in entries if e.get("level_name")}
    return sorted(sectors)


def list_types(root: Optional[Path] = None) -> list[str]:
    """Return sorted unique curve type names from the index.

    Args:
        root: Project root directory.

    Returns:
        Sorted list of unique type strings (e.g. "adoption", "cost", "capability").
    """
    entries = load_index(root)
    types = {e.get("type", "") for e in entries if e.get("type")}
    return sorted(types)


def find_cost_curves(
    query: str,
    sector: Optional[str] = None,
    limit: int = 20,
    root: Optional[Path] = None,
) -> list[dict]:
    """Shortcut to search for cost curves matching a query.

    Args:
        query: Space-separated keywords to search for.
        sector: Optional sector filter (substring match on level_name).
        limit: Maximum number of results. Defaults to 20.
        root: Project root directory.

    Returns:
        List of cost-curve metadata dicts, sorted by relevance.
    """
    return search_curves(query, type_="cost", sector=sector, limit=limit, root=root)


def find_adoption_curves(
    query: str,
    sector: Optional[str] = None,
    limit: int = 20,
    root: Optional[Path] = None,
) -> list[dict]:
    """Shortcut to search for adoption curves matching a query.

    Args:
        query: Space-separated keywords to search for.
        sector: Optional sector filter (substring match on level_name).
        limit: Maximum number of results. Defaults to 20.
        root: Project root directory.

    Returns:
        List of adoption-curve metadata dicts, sorted by relevance.
    """
    return search_curves(
        query, type_="adoption", sector=sector, limit=limit, root=root
    )
