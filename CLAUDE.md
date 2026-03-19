# STDF v2 Agents — Claude Code Implementation

STDF (Seba Technology Disruption Framework) v2 multi-agent pipeline with dynamic DAG orchestration. 16 agents, 5 skills, 14 lib modules, 956 empirical curves.

## Agent Registry

The single source of truth for pipeline DAG resolution. The `/stdf` skill walks the "Requires" column recursively to resolve execution order.

| Agent | Produces | Requires | Criticality | Tags |
|-------|----------|----------|-------------|------|
| stdf-domain-disruption | 01-domain-disruption.md | — | HIGH | foundation |
| stdf-cost-researcher | 02a-cost-researcher.md | — | CRITICAL | foundation |
| stdf-capability | 03-capability.md | — | HIGH | foundation |
| stdf-cost-fitter | 02b-cost-fitter.md | 02a-cost-researcher.md | CRITICAL | cost |
| stdf-cost-parity-checker | 04a-cost-parity.md | 02b-cost-fitter.md | CRITICAL | tipping |
| stdf-capability-parity-checker | 04b-cap-parity.md | 03-capability.md | HIGH | tipping |
| stdf-adoption-readiness-checker | 04c-adopt-readiness.md | 01-domain-disruption.md, 02b-cost-fitter.md | HIGH | tipping |
| stdf-tipping-synthesizer | 04d-tipping-synthesizer.md | 04a-cost-parity.md, 04b-cap-parity.md, 04c-adopt-readiness.md | CRITICAL | tipping |
| stdf-scurve-fitter | 05a-scurve-fitter.md | 04d-tipping-synthesizer.md, 02b-cost-fitter.md | HIGH | adoption |
| stdf-regional-adopter | 05b-regional-adopter.md | 05a-scurve-fitter.md | MEDIUM | adoption |
| stdf-xcurve-analyst | 05c-xcurve-analyst.md | 05a-scurve-fitter.md | MEDIUM | adoption |
| stdf-demand-decomposer | 07a-demand-decomposer.md | 05a-scurve-fitter.md, 01-domain-disruption.md | CRITICAL | commodity |
| stdf-stream-forecaster | 07b-stream-forecaster.md | 07a-demand-decomposer.md | HIGH | commodity |
| stdf-fleet-modeler | 07c-fleet-modeler.md | 07b-stream-forecaster.md | MEDIUM | commodity |
| stdf-regional-demand-analyst | 07d-regional-demand.md | 07b-stream-forecaster.md, 05b-regional-adopter.md | HIGH | commodity |
| stdf-synthesizer | 00-final-synthesis.md, 06-synthesizer.md | all selected outputs | CRITICAL | always |

## Pipeline Presets

| Preset | Goal Agents | Detect When |
|--------|-------------|-------------|
| FULL | tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | Default for any STDF query |
| QUICK | cost-fitter, synthesizer | "quick", "brief", "overview", "cost of X" |
| TIPPING_ONLY | tipping-synthesizer, synthesizer | "tipping point", "when does X tip" |
| COST_FOCUS | cost-fitter, capability, synthesizer | "cost trajectory", "learning rate", "price" |
| ADOPTION_FOCUS | scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | "market share", "adoption", "when will X reach" |
| FULL+COMMODITY | FULL + demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst | Commodity keyword (copper, lithium, etc.) + demand/supply |

## Pipeline Execution

Orchestration lives in `/stdf` skill (`.claude/skills/stdf.md`). Use `/stdf "query"` to run.

### Failure Matrix

| Criticality | On Failure | Confidence Penalty | Pipeline Effect |
|-------------|-----------|-------------------|----------------|
| CRITICAL | **HARD FAIL** — stop pipeline | — | Report failure, no synthesis |
| HIGH | Continue with warning | -0.3 | Degraded output, noted in README |
| MEDIUM | Continue silently | -0.1 | Minor gap, noted in synthesis |

### Rules
- File-based communication only — agents write files, downstream agents read files
- Never skip the synthesizer — raw agent outputs are not user-facing
- CRITICAL failure = pipeline stop
- Agent Registry is the single source of truth — resolve DAG dynamically every time

## Skills

| Skill | Description |
|-------|-------------|
| `/stdf "query"` | Full pipeline — preset detection, DAG resolution, agent execution, validation |
| `/stdf-validate [path]` | Guardrail audit (banned vocab, forecast language, sources) |
| `/stdf-data "query"` | Search/browse the 956-curve empirical data catalog |
| `/stdf-compliance <file>` | Compliance checklist evaluation for a specific agent output |
| `/stdf-readme [dir]` | Generate/regenerate README.md index for a pipeline run |

## Usage

```
/stdf "Analyze the energy storage disruption"
/stdf-data "lithium battery cost"
/stdf-validate output/energy-storage/
/stdf-compliance output/energy-storage/agents/02b-cost-fitter.md
/stdf-readme output/energy-storage/
```

Headless: `claude -p "Analyze the energy storage disruption using the STDF framework"`

## Key Directories

| Path | Purpose |
|------|---------|
| `.claude/skills/` | 5 pipeline skills (slash commands) |
| `.claude/agents/` | 16 agent definitions |
| `.claude/shared-rules.md` | Vocabulary, guardrails, computation rules (read by all agents) |
| `.claude/agent-memory/` | Persistent per-agent memory |
| `lib/` | 14 Python computation modules (math, parsing, validation) |
| `data/` | 956 empirical time series curves (JSON, sector-organized) |
| `output/<slug>/` | Pipeline run outputs (one dir per analysis) |
| `scripts/` | CLI utilities (`query_curves.py`, `build_data.py`) |

## Conventions
- Always use python3
