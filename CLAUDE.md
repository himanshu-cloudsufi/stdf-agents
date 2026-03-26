# STDF v2 Agents -- Claude Code Implementation

STDF (Seba Technology Disruption Framework) v2 multi-agent pipeline with dynamic DAG orchestration. 22 agents, 15 lib modules, 956 empirical curves.

## STDF Pipeline

All pipeline definitions live in `stdf/`. See `stdf/orchestrator.md` for the full execution guide (presets, DAG resolution, tier execution, validation).

Agent Registry (DAG source of truth): `stdf/references/agent-registry.md`

### Rules
- File-based communication only -- agents write files, downstream agents read files
- Never skip the synthesizer -- raw agent outputs are not user-facing
- CRITICAL failure = pipeline stop
- Agent Registry is the single source of truth -- resolve DAG dynamically every time

## Key Directories

| Path | Purpose |
|------|---------|
| `stdf/` | STDF pipeline definitions (agents, orchestrator, rules, references, memory) |
| `stdf/agents/` | 22 agent definitions (18 pipeline + 4 utility) |
| `stdf/shared-rules.md` | Vocabulary, guardrails, computation rules (read by all agents) |
| `stdf/agent-memory/` | Persistent per-agent memory |
| `stdf/references/` | Agent registry, energy methodology docs |
| `server/` | Claude Agent SDK server |
| `lib/` | 15 Python computation modules (math, parsing, validation) |
| `data/` | 956 empirical time series curves (JSON, sector-organized) |
| `output/<slug>/` | Pipeline run outputs (one dir per analysis) |
| `scripts/` | CLI utilities (`query_curves.py`, `validate_pipeline.py`, `display_curve.py`) |

## Conventions
- Always use python3
