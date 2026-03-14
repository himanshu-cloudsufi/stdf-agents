# STDF v2 Agents — Claude Code Implementation

This is a fresh implementation of the STDF (Seba Technology Disruption Framework) v2 multi-agent pipeline using Claude Code agents.

## Architecture

```
Claude Code (main session, reads CLAUDE.md for pipeline logic)
    ├── stdf-domain-disruption  (sonnet, memory:project)        — Cat 1: Sector, disruptions, convergence
    ├── stdf-cost-curve         (sonnet, memory:project, orange) — Cat 2: Cost trajectories, learning rates
    ├── stdf-capability         (sonnet, memory:project, purple) — Cat 3: Multi-dimensional capability comparison
    ├── stdf-adoption-scurve    (sonnet, memory:project, green)  — Cat 4: S-curve adoption, regional breakdown
    ├── stdf-tipping-point      (sonnet, memory:project, cyan)   — Cat 5: Tipping conditions synthesis
    └── stdf-synthesizer        (sonnet, memory:project, pink)   — Merges all 5 into 7-phase narrative
```

All agents use web research tools (WebSearch, WebFetch), Bash (python3 for computation), and file tools (Read, Write, Edit, Glob, Grep). Each agent maintains persistent memory at `.claude/agent-memory/<agent-name>/`.

## File-Based Inter-Agent Communication

**All data transfer between agents MUST go through files.** Agents do NOT receive upstream outputs via prompt context. Instead:

1. Each agent **writes** its structured markdown output + reasoning to a file in the run's output directory.
2. Downstream agents **read** upstream files from disk before starting their analysis.
3. The orchestrator (main Claude Code session) creates the output directory and tells each agent the file paths.

### Output Directory Convention

Each pipeline run creates a directory:
```
output/<analysis-slug>/
├── README.md                              — Index with pipeline summary + agent trace links
├── 00-final-synthesis.md                  — Full 7-phase STDF narrative (written by synthesizer)
└── agents/
    ├── 01-domain-disruption.md            — Domain agent output + reasoning + sources
    ├── 02-cost-curve.md                   — Cost curve agent output + reasoning + sources
    ├── 03-capability.md                   — Capability agent output + reasoning + sources
    ├── 04-tipping-point.md                — Tipping point agent output + reasoning + sources
    ├── 05-adoption-scurve.md              — Adoption S-curve agent output + reasoning + sources
    └── 06-synthesizer.md                  — Synthesizer metadata + confidence breakdown
```

The `<analysis-slug>` is derived from the query (e.g., `electric-vehicles`, `energy-storage`, `lab-grown-meat`).

### File Format for Agent Outputs

Every agent output file MUST contain these sections:

```markdown
# STDF [Agent Name] Agent — [Topic]

**Agent:** `[agent-name]` | **Confidence:** [score]

---

## Agent Reasoning
[2-4 paragraphs explaining the agent's analytical approach, key decisions, and why]

---

## Agent Output

[Structured markdown with labeled sections, key-value pairs, and tables.
Each agent has its own output template — see individual agent definitions.]

---

## Sources
[Bulleted list of all sources cited]
```

### How Agents Read Upstream Files

When an agent prompt includes `UPSTREAM_FILES:`, the agent MUST:
1. Use the `Read` tool to read each listed file path before starting analysis.
2. Extract data from the structured markdown sections (tables, key-value pairs) in the "Agent Output" section of each upstream file.
3. Use the extracted data as its primary input — do NOT re-research what upstream agents have already quantified.

### Why File-Based Communication

- **Transparency:** Every intermediate result is persisted and inspectable.
- **Reproducibility:** Re-running a downstream agent reads the same upstream files.
- **Debuggability:** When an agent produces unexpected output, you can inspect exactly what it received.
- **Context efficiency:** Agents read only what they need, avoiding prompt bloat.
- **Audit trail:** The output directory is a complete record of the analysis.

## STDF Pipeline Execution

When the user asks for an STDF disruption analysis of any sector or technology, execute this pipeline directly (no orchestrator agent needed — you have the Agent tool).

### Step 0: Create Output Directory
```bash
mkdir -p output/<analysis-slug>/agents
```
Derive `<analysis-slug>` from the query (lowercase, hyphens, no spaces). Example: `electric-vehicles`, `energy-storage`.

### Step 1: Parse the Query
Extract from the user's query:
- The sector/technology to analyze
- Any specified regions, time horizon, or context
- Whether this is a focused single-technology or broad sector analysis

### Step 2: Phase 1 — Run 3 Agents in Parallel
Launch these three agents **simultaneously** using the Agent tool. Each agent prompt MUST include the output file path:

1. **stdf-domain-disruption** (Cat 1): "Analyze the disruption landscape for [SECTOR]. Identify all disruptions, disruptors, incumbents, chimeras, and convergence combinations. **Write your full output (reasoning + structured markdown + sources) to `output/<slug>/agents/01-domain-disruption.md`.**"

2. **stdf-cost-curve** (Cat 2): "Analyze cost curve dynamics for [DISRUPTOR vs INCUMBENT]. Build historical cost trajectories, derive learning rate from data, identify competitive threshold. **Write your full output (reasoning + structured markdown + sources) to `output/<slug>/agents/02-cost-curve.md`.**"

3. **stdf-capability** (Cat 3): "Compare capabilities of [DISRUPTOR vs INCUMBENT] across multiple dimensions. Include historical trajectories and threshold assessments. **Write your full output (reasoning + structured markdown + sources) to `output/<slug>/agents/03-capability.md`.**"

Include the user's full query and any context in each agent invocation.

### Step 3: Collect Phase 1 Results
Verify each output file was written. If any agent fails:
- **cost_curve failure → HARD FAIL** the pipeline (CRITICAL agent)
- domain_disruption or capability failure → continue with degraded confidence (-0.3 penalty)

### Step 4: Phase 2 — Tipping Point (Sequential)
Launch **stdf-tipping-point** (Cat 5) with file paths to read:
"Synthesize upstream analyses to determine the tipping point. **UPSTREAM_FILES:** Read `output/<slug>/agents/01-domain-disruption.md`, `output/<slug>/agents/02-cost-curve.md`, `output/<slug>/agents/03-capability.md`. Determine when all 3 tipping conditions (cost parity, capability parity, adoption readiness) are met. **Write your full output to `output/<slug>/agents/04-tipping-point.md`.**"

If tipping_point fails → HARD FAIL the pipeline.

### Step 5: Phase 3 — Adoption S-Curve (Sequential)
Launch **stdf-adoption-scurve** (Cat 4) with file paths to read:
"Model adoption dynamics using S-curves. **UPSTREAM_FILES:** Read `output/<slug>/agents/01-domain-disruption.md`, `output/<slug>/agents/02-cost-curve.md`, `output/<slug>/agents/03-capability.md`, `output/<slug>/agents/04-tipping-point.md`. Fit logistic S-curve, provide regional breakdown (China, USA, Europe minimum), map X-curve. **Write your full output to `output/<slug>/agents/05-adoption-scurve.md`.**"

If adoption fails → continue with degraded confidence (-0.25 penalty)

### Step 6: Synthesize
Launch **stdf-synthesizer** with file paths to all 5 outputs:
"Merge all 5 STDF subagent outputs into a unified 7-phase analysis. **UPSTREAM_FILES:** Read `output/<slug>/agents/01-domain-disruption.md`, `output/<slug>/agents/02-cost-curve.md`, `output/<slug>/agents/03-capability.md`, `output/<slug>/agents/04-tipping-point.md`, `output/<slug>/agents/05-adoption-scurve.md`. Produce a coherent narrative, key conclusion with rupture window, and aggregated confidence score. **Write the 7-phase narrative to `output/<slug>/00-final-synthesis.md` and agent metadata to `output/<slug>/agents/06-synthesizer.md`.**"

### Step 7: Write Index & Present Results
Write `output/<slug>/README.md` with:
- Pipeline execution summary (agent IDs, durations, confidence scores)
- Links to all output files
- Key conclusion and rupture window

Present the final synthesized output to the user with:
- Executive summary with key conclusion and rupture window
- Per-phase narrative (7 phases)
- Per-subagent confidence scores
- Any warnings from degraded subagents
- Data gaps and critical assumptions

### Important Pipeline Rules
- ALWAYS run Phase 1 agents in parallel (3 simultaneous Agent calls)
- ALWAYS use file-based communication — agents write to files, downstream agents read from files
- NEVER pass large data blobs in agent prompts — use file paths instead
- Tipping point runs BEFORE adoption (adoption needs tipping context); adoption runs BEFORE synthesizer
- NEVER skip the synthesizer — raw subagent outputs are not user-facing
- If a CRITICAL agent fails, stop the pipeline and report the failure
- ALWAYS write a README.md index at the end linking all output files with agent trace IDs

## Agent Compliance System

Each agent enforces a compliance criteria checklist with severity levels:
- **CRITICAL** — Hard-fail gates. Violation makes entire output NON-COMPLIANT.
- **HIGH** — Must be satisfied. Failure significantly degrades output quality.
- **MEDIUM** — Should be addressed when data permits.

Key compliance gates per agent:
| Agent | CRITICAL Criteria |
|-------|------------------|
| cost-curve | 2.1: Historical disruptor cost trajectory (min 3 pts, 5+ yrs); 2.5: Service-level units only |
| capability | 3.1: Min 3 capability dimensions identified; 3.2: Historical trajectory data |
| adoption-scurve | 4.1: S-curve model required (NO linear extrapolation) |
| tipping-point | 5.1: Explicit tipping year/range + conditions; 5.2: All 3 conditions checked |
| domain-disruption | 1.3: All disruptions mapped; 1.4: Specific disruptor technologies named |

### Banned Vocabulary (all agents)
Never use: transition, renewable energy, net zero, green, sustainable, hydrogen economy, Wright's Law, IEA, EIA, BNEF, OPEC, clean energy, decarbonization

### Required Vocabulary (all agents)
Use instead: disruption, stellar energy, cost-curve dynamics, market-driven disruption, incumbent displacement, S-curve adoption

## Agent Output Contracts

All agents produce structured markdown with labeled sections, key-value pairs, and tables. Key output sections per agent:

- **domain-disruption**: Key Findings (sector, sub-domains, confidence), Disruption Map table, Narrative, Handoff Context
- **cost-curve**: Key Findings, Disruptor/Incumbent Cost Trajectory tables, Exponential Fit, Learning Rate, Competitive Threshold, Inflection Threshold, Compliance Checklist table
- **capability**: Capability Dimensions table (dimension, values, threshold, met status, trajectory), Multi-Dimensional Assessment, Narrative, Handoff Context
- **adoption-scurve**: Key Findings (market share, phase), S-Curve Parameters, Projections table, Regional Breakdown table, X-Curve Decline, Market Trauma table
- **tipping-point**: Tipping Point (year, confidence), Tipping Conditions table, Regional Assessment table, Post-Tipping Dynamics, Completion Timeline, Compliance Checklist
- **synthesizer**: Confidence Breakdown table, Aggregated Confidence, Key Conclusion, Handoff Context (writes 7-phase narrative to `00-final-synthesis.md`)

## Agent Memory

Each agent has persistent project-scoped memory at `.claude/agent-memory/<agent-name>/`. Agents build institutional knowledge across conversations:
- Domain-disruption: disruption patterns, convergence combinations, sector-specific data
- Cost-curve: cost data points, learning rates, reliable data sources
- Capability: performance benchmarks, trajectory data, threshold patterns
- Adoption: market share data, fitted S-curve parameters, regional dynamics
- Tipping-point: binding constraints by sector, regional tipping sequences, convergence acceleration patterns
- Synthesizer: common subagent conflicts, effective narrative structures, confidence calibration

## Directory Structure

```
CLAUDE.md                        — Pipeline orchestration logic + conventions
.claude/
  shared-rules.md                — Shared vocabulary, guardrails, and memory system (read by all agents)
  agents/                        — 6 agent definitions (reference shared-rules.md for common rules)
    stdf-domain-disruption.md
    stdf-cost-curve.md
    stdf-capability.md
    stdf-adoption-scurve.md
    stdf-tipping-point.md
    stdf-synthesizer.md
  agent-memory/                  — Persistent per-agent memory (project-scoped)
    stdf-domain-disruption/
    stdf-cost-curve/
    stdf-capability/
    stdf-adoption-scurve/
    stdf-tipping-point/
    stdf-synthesizer/
output/                          — Pipeline run outputs (one directory per analysis)
  <analysis-slug>/               — e.g., electric-vehicles/, energy-storage/
    README.md                    — Index: pipeline summary, agent trace IDs, links
    00-final-synthesis.md        — Final 7-phase narrative (written by synthesizer)
    agents/
      01-domain-disruption.md    — Agent output + reasoning + sources + trace ID
      02-cost-curve.md
      03-capability.md
      04-tipping-point.md
      05-adoption-scurve.md
      06-synthesizer.md
data/                            — 956 empirical time series curves (per-curve JSON files)
  index.json                     — Metadata-only manifest (no X/Y data, includes file paths)
  overrides.json                 — Corrections for misclassified curves
  <sector_slug>/                 — e.g., passenger_cars/, battery_pack/, energy_generation/
    <type_slug>/                 — e.g., cost/, adoption/, capability/
      <dataset_name>.json        — Single curve with full X/Y arrays
prompts/                         — Raw prompt files (pre-agent-format reference)
scripts/
  stdf_v2_cc.py                  — Python orchestrator script (alternative to Claude Code pipeline)
  build_data.py                  — Rebuilds data/ tree + index.json from overrides
  query_curves.py                — Token-based keyword search over data/index.json
```

## Empirical Data Catalog

`data/` contains 956 curated empirical time series curves, organized as individual JSON files in a sector-first directory tree.

### Directory Structure

```
data/
  index.json                                    — Metadata-only manifest (no X/Y data)
  overrides.json                                — Corrections for misclassified curves
  <sector_slug>/
    <type_slug>/
      <dataset_name>.json                       — Single curve with full X/Y arrays
```

Sector slugs: `passenger_cars`, `battery_pack`, `energy_generation`, `uav`, `compute_chipsets`, etc.
Type slugs: `cost`, `adoption`, `capability`, `performance_benchmark`, `labor_impact`, `market_share`, etc.

### Agent Access Pattern

1. **Read `data/index.json`** — metadata manifest with file paths for all 956 curves
2. **Read individual curve files** — `data/<sector>/<type>/<name>.json`
3. **Glob for browsing** — `data/<sector>/<type>/*.json`
4. **Keyword search** — `python3 scripts/query_curves.py --search "query" --type cost`

### Query Script

```bash
python3 scripts/query_curves.py --search "lithium-ion battery" --type cost
python3 scripts/query_curves.py --type adoption --sector "Passenger Cars" --detail
python3 scripts/query_curves.py --list-sectors
python3 scripts/query_curves.py --list-types
python3 scripts/query_curves.py --dataset "Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global" --detail
```

### Rebuilding After Catalog Changes

If individual curve files are edited/added, rebuild the index:
```bash
python3 scripts/build_data.py
```

## Usage

### Interactive (within Claude Code)
Ask for an STDF analysis directly:
```
Analyze the energy storage disruption using the STDF framework
```
Claude Code will execute the pipeline above automatically.

### Headless CLI
```bash
claude -p "Analyze the energy storage disruption using the STDF framework"
```

## Conventions
- Always use python3
- Never add Co-Authored-By lines to commits
- PRs target the development branch
