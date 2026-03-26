"""STDF v2 Guardrails — Validation Module.

Provides validation functions for banned vocabulary, banned sources,
forecast language, date consistency, and citation provenance. Used by
both the Claude Code hooks (hard enforcement) and the orchestrator
pipeline validation (soft audit).
"""

import re

from lib.vocabulary import scan_banned, scan_banned_sources


# ---------------------------------------------------------------------------
# Forecast language patterns
# ---------------------------------------------------------------------------

FORECAST_KEYWORDS = re.compile(
    r"\b(forecast|projected|outlook|expected\s+to\s+reach|will\s+reach|estimated\s+to\s+reach)\b",
    re.IGNORECASE,
)

# Anti-pattern phrases that should never appear in STDF output
ANTI_PATTERNS = re.compile(
    r"\b(linear\s+extrapolation|linear\s+growth|green\s+hydrogen|net\s+zero\s+target)\b",
    re.IGNORECASE,
)

# Banned scenario-label language
SCENARIO_TERMS = re.compile(
    r"\b(base\s+case|bull\s+case|bear\s+case|optimistic\s+scenario|pessimistic\s+scenario|"
    r"best\s+case|worst\s+case|base\s+scenario|conservative\s+scenario|aggressive\s+scenario|"
    r"scenario\s+range)\b",
    re.IGNORECASE,
)

# Year pattern (4-digit years 2000-2099)
YEAR_PATTERN = re.compile(r"\b(20\d{2})\b")


def validate_banned_vocabulary(text: str) -> list[dict]:
    """Check for banned STDF vocabulary terms.

    Returns list of {"term": str, "replacement": str, "count": int}.
    """
    hits = scan_banned(text)
    return [
        {"term": h["term"], "replacement": h["replacement"], "count": len(h["positions"])}
        for h in hits
    ]


def validate_banned_sources(text: str) -> list[dict]:
    """Check for banned source URLs/references.

    Returns list of {"pattern": str, "reason": str}.
    """
    hits = scan_banned_sources(text)
    return [{"pattern": h["pattern"], "reason": h["reason"]} for h in hits]


def validate_no_forecast_language(text: str) -> list[dict]:
    """Scan for forecast keywords near future year references.

    Returns list of {"keyword": str, "context_snippet": str, "issue": str}.
    """
    results = []
    for m in FORECAST_KEYWORDS.finditer(text):
        keyword = m.group(0)
        # Get surrounding context (100 chars each direction)
        start = max(0, m.start() - 100)
        end = min(len(text), m.end() + 100)
        context = text[start:end].replace("\n", " ").strip()
        results.append({
            "keyword": keyword,
            "context_snippet": context,
            "issue": f"Forecast language '{keyword}' detected",
        })
    return results


def validate_anti_patterns(text: str) -> list[dict]:
    """Scan for anti-pattern phrases that violate STDF rules.

    Returns list of {"phrase": str, "context_snippet": str, "issue": str}.
    """
    results = []
    for m in ANTI_PATTERNS.finditer(text):
        phrase = m.group(0)
        start = max(0, m.start() - 60)
        end = min(len(text), m.end() + 60)
        context = text[start:end].replace("\n", " ").strip()
        results.append({
            "phrase": phrase,
            "context_snippet": context,
            "issue": f"Anti-pattern phrase '{phrase}' detected",
        })
    return results


def validate_scenario_labels(text: str) -> list[dict]:
    """Scan for banned scenario-label language."""
    results = []
    for m in SCENARIO_TERMS.finditer(text):
        phrase = m.group(0)
        start = max(0, m.start() - 60)
        end = min(len(text), m.end() + 60)
        context = text[start:end].replace("\n", " ").strip()
        results.append({
            "phrase": phrase,
            "context_snippet": context,
            "issue": f"Banned scenario label '{phrase}' — use parameter values instead",
        })
    return results


def validate_date_consistency(text: str, analysis_date: str) -> list[dict]:
    """Flag future-dated data presented as observed.

    Looks for years after the analysis date that appear near '[observed]'
    or in data tables without [model-derived] tags.

    Returns list of {"year_found": str, "context": str, "issue": str}.
    """
    if not analysis_date:
        return []

    try:
        analysis_year = int(analysis_date[:4])
    except (ValueError, IndexError):
        return []

    results = []
    for m in YEAR_PATTERN.finditer(text):
        year = int(m.group(1))
        if year > analysis_year:
            # Check if this future year is near "[observed]"
            start = max(0, m.start() - 80)
            end = min(len(text), m.end() + 80)
            context = text[start:end]
            if "[observed]" in context.lower():
                results.append({
                    "year_found": str(year),
                    "context": context.replace("\n", " ").strip(),
                    "issue": f"Year {year} is after analysis date {analysis_date} but tagged as [observed]",
                })
    return results


def validate_citation_provenance(text: str) -> list[dict]:
    """Check for tables with data rows missing source entries.

    Looks for markdown table rows where a 'Source' column is empty.

    Returns list of {"location": str, "issue": str}.
    """
    results = []
    lines = text.splitlines()
    header_indices: list[int] = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        if "|" in stripped and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r"^\|[\s\-:|]+\|$", next_line):
                header_indices.append(i)

    for hdr_idx in header_indices:
        header = lines[hdr_idx].strip()
        cells = [c.strip() for c in header.strip("|").split("|")]
        source_col = None
        for j, cell in enumerate(cells):
            if cell.lower() == "source":
                source_col = j
                break

        if source_col is None:
            continue

        # Check data rows
        row_idx = hdr_idx + 2
        while row_idx < len(lines):
            row = lines[row_idx].strip()
            if not row or "|" not in row:
                break
            row_cells = [c.strip() for c in row.strip("|").split("|")]
            if source_col < len(row_cells) and not row_cells[source_col]:
                results.append({
                    "location": f"line {row_idx + 1}",
                    "issue": f"Empty Source column in table row at line {row_idx + 1}",
                })
            row_idx += 1

    return results


def validate_data_type_tags(text: str, analysis_date: str) -> list[dict]:
    """Flag future-year numbers in prose/tables lacking data-type tags."""
    if not analysis_date:
        return []
    try:
        analysis_year = int(analysis_date[:4])
    except (ValueError, IndexError):
        return []

    results = []
    lines = text.splitlines()
    section_tagged = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Track section-level tags
        if "all values" in stripped.lower() and ("[model-derived]" in stripped.lower() or "[observed]" in stripped.lower()):
            section_tagged = True
            continue
        # Reset section tag at new headers or blank lines between sections
        if stripped.startswith("#") or (not stripped and i + 1 < len(lines) and lines[i + 1].strip().startswith("#")):
            section_tagged = False
            continue
        if section_tagged:
            continue
        # Skip headers, separators, source lines
        if stripped.startswith("#") or stripped.startswith("|--") or stripped.startswith("- ["):
            continue
        # Find future-year references
        future_years = re.findall(r"\b(20[3-9]\d|202[7-9])\b", stripped)
        if not future_years:
            continue
        has_tag = "[model-derived]" in stripped or "[observed]" in stripped
        if has_tag:
            continue
        # Check for numerical values on the line
        has_numbers = bool(re.search(r"\d+\.\d+%|\d+\.\d+ [A-Z]|[\$]\d|CNY [\d,]|\d+,\d{3}", stripped))
        if has_numbers:
            results.append({
                "line": i + 1,
                "context": stripped[:100],
                "issue": f"Line {i+1}: future-year numbers without data-type tag",
            })
    return results


def full_guardrail_check(text: str, analysis_date: str = None) -> dict:
    """Run all guardrail checks on the given text.

    Returns:
        {
            "pass": bool,
            "critical_violations": [...],  # banned vocab, banned sources, anti-patterns
            "warnings": [...],             # forecast language, missing provenance, date issues
            "report": str                  # human-readable markdown report
        }
    """
    critical: list[dict] = []
    warnings: list[dict] = []

    # Critical checks
    banned_vocab = validate_banned_vocabulary(text)
    for v in banned_vocab:
        critical.append({
            "type": "banned_vocabulary",
            "detail": f"Banned term '{v['term']}' ({v['count']}x) → {v['replacement']}",
        })

    banned_src = validate_banned_sources(text)
    for v in banned_src:
        critical.append({
            "type": "banned_source",
            "detail": f"Banned source pattern '{v['pattern']}' → {v['reason']}",
        })

    anti = validate_anti_patterns(text)
    for v in anti:
        critical.append({
            "type": "anti_pattern",
            "detail": v["issue"],
        })

    scenarios = validate_scenario_labels(text)
    for v in scenarios:
        critical.append({
            "type": "scenario_label",
            "detail": v["issue"],
        })

    # Warnings
    forecast = validate_no_forecast_language(text)
    for v in forecast:
        warnings.append({
            "type": "forecast_language",
            "detail": v["issue"],
        })

    if analysis_date:
        date_issues = validate_date_consistency(text, analysis_date)
        for v in date_issues:
            warnings.append({
                "type": "date_consistency",
                "detail": v["issue"],
            })

    provenance = validate_citation_provenance(text)
    for v in provenance:
        warnings.append({
            "type": "missing_provenance",
            "detail": v["issue"],
        })

    if analysis_date:
        tag_issues = validate_data_type_tags(text, analysis_date)
        for v in tag_issues:
            warnings.append({
                "type": "untagged_projection",
                "detail": v["issue"],
            })

    # Build report
    lines = ["## Guardrail Validation Report", ""]
    if critical:
        lines.append(f"**CRITICAL violations: {len(critical)}**")
        for c in critical:
            lines.append(f"- [{c['type']}] {c['detail']}")
    else:
        lines.append("**CRITICAL violations: 0**")
    lines.append("")

    if warnings:
        lines.append(f"**Warnings: {len(warnings)}**")
        for w in warnings:
            lines.append(f"- [{w['type']}] {w['detail']}")
    else:
        lines.append("**Warnings: 0**")
    lines.append("")

    passed = len(critical) == 0
    lines.append(f"**Result: {'PASS' if passed else 'FAIL'}**")

    return {
        "pass": passed,
        "critical_violations": critical,
        "warnings": warnings,
        "report": "\n".join(lines),
    }
