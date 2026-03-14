"""STDF v2 Markdown Parser.

Parses structured markdown output files written by STDF agents. Downstream
agents (tipping-point, adoption-scurve, synthesizer) use these functions to
extract tables, key-value pairs, and metadata from upstream agent output files.

The expected markdown format is documented in CLAUDE.md under
"File Format for Agent Outputs".
"""

import re


def parse_agent_file(text: str) -> dict:
    """Parse a full STDF agent output file into a structured dict.

    Returns a dict with keys:
        agent_name  — str, the agent slug (e.g. "stdf-cost-curve")
        confidence  — float or None
        reasoning   — str, content of the "Agent Reasoning" section
        sections    — dict[str, str], heading text -> raw content underneath
        sources     — list[str], bulleted source entries
    """
    result: dict = {
        "agent_name": None,
        "confidence": None,
        "reasoning": "",
        "sections": {},
        "sources": [],
    }

    # --- Agent name from header metadata line ---
    name_match = re.search(r"\*\*Agent:\*\*\s*`([^`]+)`", text)
    if name_match:
        result["agent_name"] = name_match.group(1).strip()

    # --- Confidence ---
    result["confidence"] = extract_confidence(text)

    # --- Reasoning ---
    reasoning = extract_section(text, "Agent Reasoning")
    if reasoning is not None:
        # Strip trailing horizontal rules left over from the section boundary
        result["reasoning"] = re.sub(r"\n---\s*$", "", reasoning).strip()

    # --- All ## and ### sections ---
    # We split on headings of level 2 or 3 and collect them.
    heading_pattern = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)
    matches = list(heading_pattern.finditer(text))
    for i, m in enumerate(matches):
        heading_text = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        # Remove trailing horizontal rule if present
        content = re.sub(r"\n---\s*$", "", content).strip()
        result["sections"][heading_text] = content

    # --- Sources ---
    sources_text = extract_section(text, "Sources")
    if sources_text is not None:
        # Each source is a bullet line: "- ..." or "* ..."
        for line in sources_text.splitlines():
            stripped = line.strip()
            if stripped.startswith(("- ", "* ")):
                result["sources"].append(stripped[2:].strip())

    return result


def extract_section(text: str, heading: str) -> str | None:
    """Extract content under a specific markdown heading (## or ###).

    Returns the text between *heading* and the next heading of the same or
    higher level, or None if the heading is not found.
    """
    # Escape the heading for regex safety
    escaped = re.escape(heading)
    # Match the heading at level 2 or 3
    pattern = re.compile(
        r"^(#{2,3})\s+" + escaped + r"\s*$",
        re.MULTILINE,
    )
    m = pattern.search(text)
    if m is None:
        return None

    level = len(m.group(1))  # 2 or 3
    start = m.end()

    # Find the next heading of same or higher (fewer #) level
    next_heading = re.compile(
        r"^#{2," + str(level) + r"}\s+",
        re.MULTILINE,
    )
    n = next_heading.search(text, pos=start)
    end = n.start() if n else len(text)

    return text[start:end].strip()


def extract_table(text: str, heading: str = None) -> list[dict]:
    """Extract a markdown table into a list of row dicts.

    If *heading* is given, only search within that section. Keys are the
    column headers (stripped of whitespace). Rows are returned in order.
    Returns an empty list if no table is found.
    """
    scope = text
    if heading is not None:
        section = extract_section(text, heading)
        if section is None:
            return []
        scope = section

    # Find a markdown table: header row, separator row, then data rows.
    lines = scope.splitlines()
    tables: list[list[str]] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # A table header row has pipes and at least one cell
        if "|" in line:
            # Check if the next line is a separator (e.g. |---|---|)
            if i + 1 < len(lines) and re.match(
                r"^\s*\|[\s\-:|]+\|\s*$", lines[i + 1]
            ):
                tables.append(_parse_table_block(lines, i))
                i += 1
                continue
        i += 1

    if not tables:
        return []
    # Return the first table found in scope
    return tables[0]


def _parse_table_block(lines: list[str], start: int) -> list[dict]:
    """Parse a markdown table starting at *start* index in *lines*."""
    header_cells = _split_row(lines[start])
    # Skip separator line (start + 1)
    rows: list[dict] = []
    i = start + 2
    while i < len(lines):
        line = lines[i].strip()
        if not line or "|" not in line:
            break
        cells = _split_row(line)
        row = {}
        for j, h in enumerate(header_cells):
            row[h] = cells[j] if j < len(cells) else ""
        rows.append(row)
        i += 1
    return rows


def _split_row(line: str) -> list[str]:
    """Split a markdown table row into stripped cell values."""
    # Remove leading/trailing pipe and split on pipes
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in stripped.split("|")]


def extract_key_values(text: str, heading: str = None) -> dict:
    """Extract bold key-value pairs like ``- **Key:** value`` into a dict.

    If *heading* is given, only search within that section. Keys are
    lower-cased and stripped. Values are stripped strings.
    """
    scope = text
    if heading is not None:
        section = extract_section(text, heading)
        if section is None:
            return {}
        scope = section

    result: dict = {}
    # Match both formats:
    #   - **Key:** value   (colon inside bold — standard STDF format)
    #   - **Key**: value   (colon outside bold — alternative format)
    pattern = re.compile(r"[-*]\s+\*\*(.+?)(?::\*\*|\*\*:)\s*(.+)")
    for m in pattern.finditer(scope):
        key = m.group(1).strip()
        value = m.group(2).strip()
        result[key] = value
    return result


def extract_confidence(text: str) -> float | None:
    """Extract the confidence score from the agent header metadata line.

    Looks for ``**Confidence:** <number>`` and returns it as a float,
    or None if not found.
    """
    m = re.search(r"\*\*Confidence:\*\*\s*([\d.]+)", text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None
