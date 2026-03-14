"""STDF v2 Upstream Reader.

Higher-level reader that uses markdown_parser to read and extract structured
data from upstream agent output files. Used by tipping-point, adoption-scurve,
and synthesizer agents to consume file-based inter-agent outputs.
"""

import re
from pathlib import Path

from lib.markdown_parser import (
    extract_key_values,
    extract_table,
    parse_agent_file,
)


def read_upstream(filepath: str) -> dict:
    """Read an agent output file and parse it.

    Returns the parsed dict produced by ``parse_agent_file``.
    Raises FileNotFoundError if *filepath* does not exist.
    """
    path = Path(filepath)
    text = path.read_text(encoding="utf-8")
    return parse_agent_file(text)


def read_all_upstream(filepaths: list[str]) -> dict[str, dict]:
    """Read multiple upstream agent files and return them keyed by agent slug.

    The key is derived from the filename: e.g.
    ``"01-domain-disruption.md"`` -> ``"domain_disruption"``.

    Returns dict[str, dict] where values are the parsed agent dicts.
    """
    results: dict[str, dict] = {}
    for fp in filepaths:
        parsed = read_upstream(fp)
        slug = _filename_to_slug(Path(fp).stem)
        results[slug] = parsed
    return results


def _filename_to_slug(stem: str) -> str:
    """Convert a filename stem like '01-domain-disruption' to 'domain_disruption'."""
    # Strip leading digit prefix (e.g. "01-", "02-")
    cleaned = re.sub(r"^\d+-", "", stem)
    return cleaned.replace("-", "_")


def get_cost_trajectory(upstream: dict) -> list[dict]:
    """Extract the disruptor cost trajectory table from a parsed cost-curve output.

    Searches for sections whose heading contains 'Disruptor' and 'Cost' and
    'Trajectory', falling back to the first table found under 'Agent Output'.
    """
    sections = upstream.get("sections", {})
    for heading, content in sections.items():
        if "disruptor" in heading.lower() and "cost" in heading.lower():
            table = extract_table(content)
            if table:
                return table
    # Fallback: try known heading names
    for candidate in ("Disruptor Cost Trajectory", "Cost Trajectory"):
        table = extract_table(_sections_text(sections), heading=candidate)
        if table:
            return table
    return []


def get_capability_dimensions(upstream: dict) -> list[dict]:
    """Extract the capability dimensions table from a parsed capability output.

    Searches for a section whose heading contains 'Capability Dimensions'
    or 'Multi-Dimensional'.
    """
    sections = upstream.get("sections", {})
    for candidate in ("Capability Dimensions", "Multi-Dimensional Assessment"):
        for heading, content in sections.items():
            if candidate.lower() in heading.lower():
                table = extract_table(content)
                if table:
                    return table
    return []


def get_scurve_parameters(upstream: dict) -> dict:
    """Extract S-curve parameters as a key-value dict from a parsed adoption output."""
    sections = upstream.get("sections", {})
    for heading in sections:
        if "s-curve" in heading.lower() and "param" in heading.lower():
            return extract_key_values(sections[heading])
    # Fallback: check Key Findings
    return extract_key_values(sections.get("Key Findings", ""))


def get_tipping_conditions(upstream: dict) -> list[dict]:
    """Extract the tipping conditions table from a parsed tipping-point output."""
    sections = upstream.get("sections", {})
    for heading, content in sections.items():
        if "tipping" in heading.lower() and "condition" in heading.lower():
            table = extract_table(content)
            if table:
                return table
    return []


def get_regional_breakdown(upstream: dict) -> list[dict]:
    """Extract the regional breakdown table from a parsed adoption-scurve output."""
    sections = upstream.get("sections", {})
    for heading, content in sections.items():
        if "regional" in heading.lower():
            table = extract_table(content)
            if table:
                return table
    return []


def _sections_text(sections: dict[str, str]) -> str:
    """Reassemble all sections into a single text block for fallback searching."""
    parts = []
    for heading, content in sections.items():
        parts.append(f"### {heading}\n\n{content}")
    return "\n\n".join(parts)
