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
    "clean energy": "Name the specific technology",
    "decarbonization": '"displacement of fossil-fuel incumbents" or name the specific disruption',
    "base case": 'Parameter value label (e.g., L=85%)',
    "bull case": "Parameter value label",
    "bear case": "Parameter value label",
    "optimistic scenario": "Parameter sensitivity range",
    "pessimistic scenario": "Parameter sensitivity range",
    "best case": "Parameter value label",
    "worst case": "Parameter value label",
    "ai capability growth": '"AI capability improvement"',
}

# Banned source URL/name patterns — URLs are always violations.
BANNED_SOURCE_PATTERNS: list[tuple[str, str]] = [
    (r"iea\.org", "IEA source — use primary government data; if unavoidable, tag [CAUTION: IEA source]"),
    (r"eia\.gov", "EIA source — use primary government data; if unavoidable, tag [CAUTION: EIA source]"),
    (r"bnef\.com", "BNEF source — use primary data; if unavoidable, tag [CAUTION: BNEF source]"),
    (r"opec\.org", "OPEC source — use primary data; if unavoidable, tag [CAUTION: OPEC source]"),
]

# Banned organization name patterns — inline mentions are violations UNLESS
# the same line contains a [CAUTION: {org}...] tag.
BANNED_ORG_NAMES: list[tuple[str, str]] = [
    (r"\bIEA\b", "IEA"),
    (r"\bBNEF\b", "BNEF"),
    (r"\bEIA\b", "EIA"),
    (r"\bOPEC\b", "OPEC"),
]

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


def scan_banned_sources(text: str) -> list[dict]:
    """Scan for banned organization URLs and inline org name references.

    URLs (e.g., iea.org) are always violations.
    Inline org names (e.g., "IEA") are violations ONLY if the same line
    does NOT contain a ``[CAUTION: {org}`` tag.

    Returns list of {"pattern": str, "reason": str, "positions": list[int]}.
    """
    results = []

    # 1. URL pattern checks — always violations
    for pattern_str, reason in BANNED_SOURCE_PATTERNS:
        pattern = re.compile(pattern_str, re.IGNORECASE)
        positions = [m.start() for m in pattern.finditer(text)]
        if positions:
            results.append({"pattern": pattern_str, "reason": reason, "positions": positions})

    # 2. Org name checks — violation only if same line lacks [CAUTION: {org}...] tag
    lines = text.splitlines()
    for org_pattern_str, org_name in BANNED_ORG_NAMES:
        org_re = re.compile(org_pattern_str)
        violation_positions = []
        caution_tag = f"[CAUTION: {org_name}"
        for line in lines:
            if caution_tag in line:
                continue  # line has the required CAUTION tag — not a violation
            for m in org_re.finditer(line):
                # Compute absolute position in full text
                line_start = text.find(line)
                violation_positions.append(line_start + m.start())
        if violation_positions:
            results.append({
                "pattern": org_pattern_str,
                "reason": f"{org_name} mentioned without [CAUTION: {org_name} ...] tag",
                "positions": violation_positions,
            })

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
