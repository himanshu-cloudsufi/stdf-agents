"""STDF v2 README Writer.

Generates the pipeline README.md index file (Step 7 of the STDF pipeline).
The README summarises the full pipeline run with agent statuses, confidence
scores, durations, and links to all output files.
"""

from datetime import date


def write_readme(
    slug: str,
    topic: str,
    agent_results: list[dict],
    output_dir: str,
    conclusion: str = "",
) -> str:
    """Build the full README.md content for a pipeline run.

    Parameters
    ----------
    slug : str
        The analysis slug (e.g. "energy-storage").
    topic : str
        Human-readable topic description.
    agent_results : list[dict]
        Each dict must have keys: ``agent_name`` (str), ``confidence``
        (float or None), ``status`` ("OK" | "FAILED" | "DEGRADED"),
        ``duration_s`` (float), ``file_path`` (str, relative to output dir).
    output_dir : str
        The output directory path (used only for display, not I/O).
    conclusion : str, optional
        Key conclusion text. If empty a placeholder is inserted.

    Returns
    -------
    str
        The complete README.md content.
    """
    today = date.today().isoformat()
    lines: list[str] = []

    # --- Title ---
    lines.append(f"# STDF Analysis — {topic}")
    lines.append("")
    lines.append(f"**Run date:** {today}  ")
    lines.append(f"**Output directory:** `{output_dir}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Pipeline Execution Summary Table ---
    lines.append("## Pipeline Execution Summary")
    lines.append("")
    lines.append("| Agent | Confidence | Status | Duration (s) | Output File |")
    lines.append("| --- | --- | --- | --- | --- |")
    for r in agent_results:
        name = r["agent_name"]
        conf = f"{r['confidence']:.2f}" if r.get("confidence") is not None else "N/A"
        status = r.get("status", "OK")
        dur = f"{r['duration_s']:.1f}" if r.get("duration_s") is not None else "N/A"
        fpath = r.get("file_path", "")
        link = f"[{fpath}]({fpath})" if fpath else "—"
        lines.append(f"| {name} | {conf} | {status} | {dur} | {link} |")
    lines.append("")

    # --- Output File Links ---
    lines.append("## Output Files")
    lines.append("")
    lines.append(f"- [Final Synthesis](00-final-synthesis.md)")
    for r in agent_results:
        fpath = r.get("file_path", "")
        if fpath:
            lines.append(f"- [{r['agent_name']}]({fpath})")
    lines.append("")

    # --- Key Conclusion ---
    lines.append("## Key Conclusion")
    lines.append("")
    if conclusion:
        lines.append(conclusion)
    else:
        lines.append("_See [00-final-synthesis.md](00-final-synthesis.md) for the full 7-phase narrative._")
    lines.append("")

    return "\n".join(lines)
