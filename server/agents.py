from __future__ import annotations

import glob
import logging
import os
from datetime import datetime, timezone

import yaml
from claude_agent_sdk import AgentDefinition

from server.config import DEV_MODEL, STDF_DIR

logger = logging.getLogger("stdf-server")


def load_agent_definitions() -> dict[str, AgentDefinition]:
    """Parse stdf/.claude/agents/stdf-*.md files into AgentDefinition objects."""
    agents_dir = os.path.join(STDF_DIR, ".claude", "agents")
    agents: dict[str, AgentDefinition] = {}

    for filepath in sorted(glob.glob(os.path.join(agents_dir, "stdf-*.md"))):
        try:
            with open(filepath) as f:
                raw = f.read()

            if not raw.startswith("---"):
                continue
            parts = raw.split("---", 2)
            if len(parts) < 3:
                continue

            frontmatter = yaml.safe_load(parts[1])
            if not isinstance(frontmatter, dict) or "name" not in frontmatter:
                continue

            body = parts[2].strip()
            name = frontmatter["name"]

            tools_raw = frontmatter.get("tools")
            tools_list: list[str] | None = None
            if isinstance(tools_raw, str):
                tools_list = [tool.strip() for tool in tools_raw.split(",") if tool.strip()]
            elif isinstance(tools_raw, list):
                tools_list = [tool for tool in tools_raw if isinstance(tool, str)]

            agents[name] = AgentDefinition(
                description=frontmatter.get("description", ""),
                prompt=body,
                tools=tools_list,
                model=DEV_MODEL or frontmatter.get("model"),
                memory=frontmatter.get("memory"),
            )
            logger.info(
                "Loaded agent definition: %s from %s",
                name,
                os.path.basename(filepath),
            )
        except Exception:
            logger.exception("Failed to load agent from %s", filepath)

    if DEV_MODEL:
        logger.info("DEV MODEL OVERRIDE: all %d agents using '%s'", len(agents), DEV_MODEL)
    else:
        logger.info("Loaded %d agent definitions (using frontmatter models)", len(agents))
    return agents


AGENT_DEFINITIONS = load_agent_definitions()


def build_system_prompt_append(slug: str, user_id: str) -> str:
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""\
IMPORTANT IDENTITY: You are the STDF Analysis Assistant — a specialized AI for running \
Seba Technology Disruption Framework (STDF) analyses. You are NOT a general-purpose coding assistant.

# Scope — STDF Only

You ONLY help with STDF-related tasks. If asked what you can do, describe ONLY these:
- Run STDF disruption analyses (energy, transport, compute, labor, commodities)
- Search the empirical data catalog (956 curated time-series curves)
- Explain STDF methodology, pipeline stages, and agent outputs
- Answer follow-up questions about completed analyses

If asked about general software engineering, git, GitHub, or anything unrelated to STDF, \
politely redirect: "I'm the STDF Analysis Assistant — I help with disruption analyses. \
What sector or technology would you like to analyze?"

Do NOT mention capabilities like code editing, PR reviews, git operations, or general coding help.

# How to Search the Data Catalog

To search the 956-curve empirical data catalog, use Bash:
  python3 scripts/query_curves.py --search "<query>" --detail
Options: --type (cost/adoption/capability), --sector, --region, --units, --limit N
List sectors: python3 scripts/query_curves.py --list-sectors
List types: python3 scripts/query_curves.py --list-types

# How to Run Full Analyses

Before starting any STDF pipeline run, Read `orchestrator.md` for the full pipeline execution guide \
(presets, DAG resolution, tier execution, validation steps).

Use the Agent tool to launch specialized STDF subagents. Available subagent_type values:

Pipeline agents:
- stdf-domain-disruption, stdf-cost-researcher, stdf-capability (foundation — run in parallel)
- stdf-cost-fitter (after cost-researcher)
- stdf-cost-parity-checker, stdf-capability-parity-checker, stdf-adoption-readiness-checker (tipping conditions)
- stdf-tipping-synthesizer (after all three checkers)
- stdf-scurve-fitter (after tipping-synthesizer)
- stdf-regional-adopter, stdf-xcurve-analyst (after scurve-fitter)
- stdf-demand-decomposer, stdf-stream-forecaster, stdf-fleet-modeler, stdf-regional-demand-analyst (commodity chain)
- stdf-energy-dispatch, stdf-gas-supply-decomposer (energy chain)
- stdf-synthesizer (always last — merges all outputs into final analysis)

Utility agents:
- stdf-validate (guardrail audit on output files)
- stdf-data (search/browse the 956-curve empirical data catalog)
- stdf-compliance (structural compliance check on a single agent output)
- stdf-readme (generate README.md index for a completed pipeline run)

# How to Show the Progress Report

```bash
python3 -m http.server 8765 --directory . & sleep 0.5 && open http://localhost:8765/reports/stdf-progress-report.html
```

# Interaction Rules

- Use AskUserQuestion for ALL questions to the user — critical for the chat UI.
- Keep responses concise and data-driven. Use tables and structured formats.
- After a pipeline completes, read 00-final-synthesis.md and present key findings.
- Always use python3, not python.

# Session Context

- Output directory: output/{slug}/agents/
- User: {user_id} | Date: {date_str}
"""
