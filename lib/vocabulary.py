"""STDF v2 Vocabulary Enforcement Module.

Scans agent output text for banned vocabulary and validates that required
STDF terminology is used consistently. All 6 STDF agents must check their
output against these rules before finalizing.
"""

import re

# Banned terms mapped to their recommended replacements.
BANNED_TERMS: dict[str, str] = {
    "transition": '"disruption"',
    "renewable energy": '"stellar energy" or specific technology name',
    "net zero": "Omit; frame in terms of cost-curve superiority",
    "green": "Omit",
    "sustainable": "Omit",
    "sustainability": "Omit",
    "hydrogen economy": "Specify production method and its cost curve",
    "wright's law": '"cost-curve dynamics" or "learning rate" with specific percentage',
    "IEA": "Do not cite — use primary data",
    "EIA": "Do not cite — use primary data",
    "BNEF": "Do not cite — use primary data",
    "OPEC": "Do not cite — use primary data",
    "clean energy": "Name the specific technology",
    "decarbonization": '"displacement of fossil-fuel incumbents" or name the specific disruption',
}

# Required terms that should appear in every compliant agent output.
REQUIRED_TERMS: list[str] = [
    "disruption",
    "stellar energy",
    "cost-curve dynamics",
    "market-driven disruption",
    "incumbent displacement",
    "S-curve adoption",
]


def scan_banned(text: str) -> list[dict]:
    """Return list of banned terms found in *text* (case-insensitive, whole-word).

    Each entry: {"term": str, "replacement": str, "positions": list[int]}.
    """
    results = []
    lower_text = text.lower()
    for term, replacement in BANNED_TERMS.items():
        pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        positions = [m.start() for m in pattern.finditer(text)]
        if positions:
            results.append({"term": term, "replacement": replacement, "positions": positions})
    return results


def check_required(text: str) -> list[dict]:
    """Check whether each required term appears in *text* (case-insensitive).

    Returns list of {"term": str, "present": bool}.
    """
    lower_text = text.lower()
    return [
        {"term": term, "present": term.lower() in lower_text}
        for term in REQUIRED_TERMS
    ]


def vocabulary_report(text: str) -> str:
    """Return a human-readable markdown report of vocabulary compliance.

    Suitable for appending to the bottom of an agent output file.
    """
    banned_hits = scan_banned(text)
    required_checks = check_required(text)

    lines = ["## Vocabulary Compliance Report", ""]

    # --- Banned terms section ---
    if banned_hits:
        lines.append(f"**Banned terms found: {len(banned_hits)}**")
        lines.append("")
        lines.append("| Banned Term | Occurrences | Replacement |")
        lines.append("|---|---|---|")
        for hit in banned_hits:
            count = len(hit["positions"])
            lines.append(f"| {hit['term']} | {count} | {hit['replacement']} |")
    else:
        lines.append("**Banned terms found: 0** — all clear.")
    lines.append("")

    # --- Required terms section ---
    missing = [r for r in required_checks if not r["present"]]
    if missing:
        lines.append(f"**Required terms missing: {len(missing)}**")
        lines.append("")
        for m in missing:
            lines.append(f"- [ ] {m['term']}")
    else:
        lines.append("**Required terms: all present.**")
    lines.append("")

    return "\n".join(lines)
