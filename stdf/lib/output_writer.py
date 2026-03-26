"""STDF v2 Output Writer.

Writes agent output files with the standard STDF header format. All 6 agents
produce output using the same template structure documented in CLAUDE.md.
"""

import textwrap

# Map agent slugs to human-readable display names.
AGENT_DISPLAY_NAMES: dict[str, str] = {
    "stdf-domain-disruption": "Domain Disruption",
    "stdf-cost-researcher": "Cost Researcher",
    "stdf-cost-fitter": "Cost Fitter",
    "stdf-capability": "Capability",
    "stdf-cost-parity-checker": "Cost Parity Checker",
    "stdf-capability-parity-checker": "Capability Parity Checker",
    "stdf-adoption-readiness-checker": "Adoption Readiness Checker",
    "stdf-tipping-synthesizer": "Tipping Synthesizer",
    "stdf-scurve-fitter": "S-Curve Fitter",
    "stdf-regional-adopter": "Regional Adopter",
    "stdf-xcurve-analyst": "X-Curve Analyst",
    "stdf-demand-decomposer": "Demand Decomposer",
    "stdf-stream-forecaster": "Stream Forecaster",
    "stdf-fleet-modeler": "Fleet Modeler",
    "stdf-regional-demand-analyst": "Regional Demand Analyst",
    "stdf-synthesizer": "Synthesizer",
}


def _display_name(agent_name: str) -> str:
    """Resolve *agent_name* to its display name, with a sensible fallback."""
    if agent_name in AGENT_DISPLAY_NAMES:
        return AGENT_DISPLAY_NAMES[agent_name]
    # Fallback: strip "stdf-" prefix and title-case
    cleaned = agent_name.replace("stdf-", "").replace("-", " ")
    return cleaned.title()


def build_header(agent_name: str, topic: str, confidence: float) -> str:
    """Return the standard STDF agent output header block.

    Format:
        # STDF [Display Name] Agent -- [Topic]

        **Agent:** `[agent-name]` | **Confidence:** [confidence]

        ---
    """
    display = _display_name(agent_name)
    return textwrap.dedent(f"""\
        # STDF {display} Agent — {topic}

        **Agent:** `{agent_name}` | **Confidence:** {confidence}

        ---
    """)


def build_reasoning_section(reasoning: str) -> str:
    """Return the Agent Reasoning section block.

    Format:
        ## Agent Reasoning

        [reasoning text]

        ---
    """
    return f"## Agent Reasoning\n\n{reasoning.strip()}\n\n---\n"


def build_sources_section(sources: list[str]) -> str:
    """Return the Sources section with a bulleted list.

    Format:
        ## Sources

        - source 1
        - source 2
    """
    if not sources:
        return "## Sources\n\n- No sources cited.\n"
    bullets = "\n".join(f"- {s}" for s in sources)
    return f"## Sources\n\n{bullets}\n"


def build_agent_output(
    agent_name: str,
    topic: str,
    confidence: float,
    reasoning: str,
    output_body: str,
    sources: list[str],
) -> str:
    """Assemble a complete agent output file from all parts.

    *output_body* is the pre-formatted markdown content for the
    ``## Agent Output`` section (tables, key-value pairs, narrative, etc.).

    Returns the full file content ready to be written to disk.
    """
    parts = [
        build_header(agent_name, topic, confidence),
        "",
        build_reasoning_section(reasoning),
        "",
        "## Agent Output\n",
        output_body.strip(),
        "",
        "---\n",
        build_sources_section(sources),
    ]
    return "\n".join(parts)


def table_to_markdown(headers: list[str], rows: list[list[str]]) -> str:
    """Convert headers and rows to a markdown table string.

    Returns a table with a pipe-delimited header row, a separator row with
    dashes, and one row per entry in *rows*. All cells are stripped of
    leading/trailing whitespace.
    """
    # Normalise everything to strings
    str_headers = [str(h).strip() for h in headers]
    str_rows = [[str(cell).strip() for cell in row] for row in rows]

    header_line = "| " + " | ".join(str_headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in str_headers) + " |"
    data_lines = []
    for row in str_rows:
        # Pad row to match header count if needed
        padded = row + [""] * (len(str_headers) - len(row))
        data_lines.append("| " + " | ".join(padded[: len(str_headers)]) + " |")

    return "\n".join([header_line, sep_line] + data_lines) + "\n"


def key_values_to_markdown(kvs: dict) -> str:
    """Convert a dict to bullet-point bold-key markdown.

    Format per entry: ``- **Key:** value``

    Returns the full block as a string with a trailing newline.
    """
    if not kvs:
        return ""
    lines = [f"- **{k}:** {v}" for k, v in kvs.items()]
    return "\n".join(lines) + "\n"
