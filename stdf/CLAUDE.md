# STDF v2 -- Self-Contained Analysis System

STDF (Seba Technology Disruption Framework) v2 multi-agent pipeline with dynamic DAG orchestration. 22 agents, 15 lib modules, 956 empirical curves.

## Running an Analysis

Read `orchestrator.md` for the full pipeline execution guide. Use the Agent tool to launch subagents by `subagent_type` (e.g., `stdf-cost-fitter`).

Agent Registry (DAG source of truth): `references/agent-registry.md`

## Key Directories

| Path | Purpose |
|------|---------|
| `.claude/agents/` | 22 agent definitions (18 pipeline + 4 utility) |
| `shared-rules.md` | Vocabulary, guardrails, computation rules (read by all agents) |
| `agent-memory/` | Persistent per-agent memory |
| `references/` | Agent registry, energy methodology docs |
| `lib/` | 15 Python computation modules (math, parsing, validation) |
| `data/` | 956 empirical time series curves (JSON, sector-organized) |
| `output/<slug>/` | Pipeline run outputs (one dir per analysis) |
| `scripts/` | CLI utilities (`query_curves.py`, `validate_pipeline.py`, `display_curve.py`) |
| `orchestrator.md` | Full pipeline execution guide (presets, DAG, tiers, validation) |
| `gotchas.md` | Common failure modes |

## Pipeline Rules

- File-based communication only -- agents write files, downstream agents read files
- Never skip the synthesizer -- raw agent outputs are not user-facing
- CRITICAL failure = pipeline stop
- Agent Registry is the single source of truth -- resolve DAG dynamically every time
- Always use python3
