---
name: stdf
description: Orchestrates the full STDF (Seba Technology Disruption Framework) multi-agent disruption analysis pipeline. Coordinates 16 specialized agents through a dynamic DAG to produce 7-phase disruption analyses covering cost curves, capability benchmarks, tipping points, adoption S-curves, and incumbent decline. Triggers on disruption analysis requests, STDF mentions, or sector-specific queries about energy, transport, compute, labor, or commodities. Also triggers on 'analyze X disruption', 'when does X tip', 'cost trajectory of X', 'adoption curve for X', or '/stdf'.
---

# STDF Pipeline Orchestrator

You are the orchestrator for the STDF v2 multi-agent disruption analysis pipeline. Your job is to coordinate 16 specialized agents through a dynamic DAG, producing a comprehensive 7-phase disruption analysis.

The user's query is provided as the skill argument. If no argument was given, ask the user what technology disruption they want to analyze.

**Read `gotchas.md` before your first pipeline run** — it lists common failure modes that are easy to miss.

## Quick Reference

**Agent Registry** — the single source of truth for the pipeline DAG. Read CLAUDE.md's "Agent Registry" table for the full registry. See `references/agent-registry.md` for the detailed dependency graph and tier template.

**Dependency tiers (summary):**

```
Tier 1 (parallel):    domain-disruption, cost-researcher, capability
Tier 2:               cost-fitter
Tier 3 (parallel):    cost-parity-checker, capability-parity-checker, adoption-readiness-checker
Tier 4:               tipping-synthesizer
Tier 5a:              scurve-fitter
Tier 5b (parallel):   regional-adopter, xcurve-analyst
Tier 6 (conditional): demand-decomposer → stream-forecaster → fleet-modeler + regional-demand-analyst
Final:                synthesizer (always last)
```

**Pipeline Presets:**

| Preset | Goal Agents | Detect When |
|--------|-------------|-------------|
| FULL | tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | Default |
| QUICK | cost-fitter, synthesizer | "quick", "brief", "overview" |
| TIPPING_ONLY | tipping-synthesizer, synthesizer | "tipping point", "when does X tip" |
| COST_FOCUS | cost-fitter, capability, synthesizer | "cost trajectory", "learning rate", "price" |
| ADOPTION_FOCUS | scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | "market share", "adoption" |
| FULL+COMMODITY | FULL + demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst | Commodity keyword + demand/supply |

**Commodity keywords:** copper, aluminium, lithium, lead, cobalt, nickel, crude oil, natural gas, steel, silicon

**Failure Matrix:**

| Criticality | On Failure | Penalty |
|-------------|-----------|---------|
| CRITICAL | STOP pipeline | — |
| HIGH | Continue with warning | -0.3 |
| MEDIUM | Continue silently | -0.1 |

### Examples: Query → Preset

- "Analyze the energy storage disruption" → **FULL** (default, no specific signal)
- "Quick overview of solar PV costs" → **QUICK** (detected "quick" + "costs")
- "When does autonomous driving tip?" → **TIPPING_ONLY** (detected "when" + "tip")
- "What's the copper demand impact of EV disruption?" → **FULL+COMMODITY** (detected "copper" + "demand")
- "EV adoption curve in China" → **ADOPTION_FOCUS** (detected "adoption" + region)

---

## Step 0: Setup

1. Derive `<analysis-slug>` from the query (lowercase, hyphens, no spaces, no special chars). Examples: `energy-storage`, `electric-vehicles`, `lab-grown-meat`.
2. Get today's date in YYYY-MM-DD format — this is the **analysis date**.
3. Create the output directory:

```bash
mkdir -p output/<analysis-slug>/agents
```

4. Store these values — you'll use them in every agent prompt:
   - `SLUG` = the analysis slug
   - `DATE` = today's date (YYYY-MM-DD)
   - `QUERY` = the user's full query text
   - `OUTPUT_DIR` = `output/<slug>`
   - `AGENTS_DIR` = `output/<slug>/agents`

---

## Step 1: Classify & Ask

Parse the query to detect:
- The sector/technology being analyzed
- Any specified regions, time horizon, or context
- Preset signals (see Presets table above)
- Commodity keywords + demand/supply signals

**If the user explicitly stated the mode** (e.g., "quick STDF analysis", "full STDF with commodity"), skip AskUserQuestion and use the stated mode.

**Otherwise**, use **AskUserQuestion** with two questions:

**Q1** (single select): "Pipeline mode" — show the auto-detected preset as "(Recommended)", plus 3 alternatives from the Presets table.

**Q2** (multiSelect): "Add-ons" — only show options relevant to the query:
- "Commodity demand decomposition" — if commodity keyword detected
- "Fleet modeling (OEM vs replacement)" — if durable goods context
- "Regional deep-dive" — if a specific region was mentioned

---

## Step 2: Plan

Use **EnterPlanMode**. Build the execution plan from the chosen preset:

### 2a. Resolve the DAG

1. Look up **goal agents** for the chosen preset from the Presets table
2. **Recursively resolve dependencies**: For each goal agent, walk the "Requires" column in the Agent Registry. Add every agent whose output is needed.
3. Always add `stdf-synthesizer` as the final agent.

### 2b. Group into parallel tiers

- **Tier 1**: Agents with NO requirements (or whose requirements are already met by being outside the selected set)
- **Tier 2**: Agents whose requirements are ALL produced by Tier 1 agents
- Continue until all agents are placed
- Synthesizer is always the last tier

### 2c. Write the plan

Include in the plan:
- Detected preset and why it was chosen
- Tier-by-tier table: tier number, agent names, parallelism (parallel/sequential)
- Agents skipped (not needed for this preset)
- Critical path (longest sequential chain through the DAG)
- Total agent count

Use **ExitPlanMode** — the user reviews and approves or modifies.

---

## Step 3: Execute

After user approval, execute tier by tier. Each agent's `subagent_type` matches its name (e.g., agent `stdf-cost-fitter` uses `subagent_type: "stdf-cost-fitter"`).

### Agent prompt template

Every agent prompt MUST include these elements:

```
**Analysis date: {DATE}. All data after this date is forecast — do NOT use web-sourced forecasts as observed values.**

QUERY: {full user query}

OUTPUT_FILE: output/{SLUG}/agents/{filename-from-registry}

UPSTREAM_FILES:
- output/{SLUG}/agents/{required-file-1}
- output/{SLUG}/agents/{required-file-2}
```

### Execution loop

For each tier in the plan:

1. **Launch all agents in the tier as parallel Agent tool calls** — use a single message with multiple Agent tool uses.
2. **Wait for all agents in the tier to complete** before starting the next tier.
3. **Check for failures** after each tier completes:
   - **CRITICAL agent fails** → STOP the pipeline immediately. Report the failure to the user. Do NOT proceed.
   - **HIGH agent fails** → Log a warning, apply -0.3 confidence penalty, continue to next tier.
   - **MEDIUM agent fails** → Apply -0.1 confidence penalty, continue.

### Progress checklist

Copy this checklist into your response and update it as tiers complete. Only include tiers relevant to the chosen preset.

```
- [ ] Tier 1: Foundation agents (domain-disruption, cost-researcher, capability)
- [ ] Tier 2: Cost fitting (cost-fitter)
- [ ] Tier 3: Condition checkers (cost-parity, capability-parity, adoption-readiness)
- [ ] Tier 4: Tipping synthesis (tipping-synthesizer)
- [ ] Tier 5a: Global S-curve (scurve-fitter)
- [ ] Tier 5b: Regional + X-curve (regional-adopter, xcurve-analyst)
- [ ] Tier 6: Commodity chain (demand-decomposer → stream-forecaster → fleet-modeler + regional-demand)
- [ ] Final: Synthesizer
- [ ] Validation: Guardrail check
```

Mark each tier with `[✓]` (success), `[⚠]` (degraded), or `[✗]` (failed) as it completes.

### Synthesizer special handling

The synthesizer always runs last. Its `UPSTREAM_FILES:` must list ALL output files that were actually produced (not skipped) by the selected agents. It produces two files:
- `output/{SLUG}/00-final-synthesis.md` — the 7-phase narrative
- `output/{SLUG}/agents/06-synthesizer.md` — confidence metadata

---

## Step 4: Validate

After the synthesizer completes, run the guardrail audit:

```bash
python3 -c "
import datetime, glob, sys
from lib.guardrails import full_guardrail_check

slug = '{SLUG}'
date = '{DATE}'
files = sorted(glob.glob(f'output/{slug}/agents/*.md') + glob.glob(f'output/{slug}/00-final-synthesis.md'))

if not files:
    print(f'ERROR: No output files found in output/{slug}/')
    sys.exit(1)

issues = 0
for f in files:
    result = full_guardrail_check(open(f).read(), date)
    if not result['pass']:
        issues += len(result['critical_violations'])
        print(f'{f}: {len(result[\"critical_violations\"])} critical, {len(result[\"warnings\"])} warnings')

if issues:
    print(f'TOTAL: {issues} critical violations across pipeline')
else:
    print('Pipeline validation: CLEAN')
"
```

This is a soft audit — the PreToolUse hooks enforce hard blocks on writes.

---

## Step 5: Write Index & Present

### 5a. Write README.md

Write `output/{SLUG}/README.md` containing:
- Pipeline preset used and total agent count
- Analysis date
- Tier-by-tier execution summary (agent names, confidence scores)
- Links to all output files produced
- Agents skipped and why
- Guardrail validation result
- Key conclusion and rupture window (from synthesizer)

### 5b. Present to user

Read `output/{SLUG}/00-final-synthesis.md` and present the final output with:
- Executive summary with key conclusion and rupture window
- Per-phase highlights (7 STDF phases)
- Per-agent confidence scores table
- Any warnings from degraded or skipped agents
- Data gaps and critical assumptions

---

## Important Rules

- **File-based communication only** — agents write files, downstream agents read files. Never pass data blobs in prompts.
- **Never skip the synthesizer** — raw agent outputs are not user-facing.
- **CRITICAL failure = pipeline stop** — do not attempt workarounds.
- **Dynamic DAG resolution** — always resolve from the Agent Registry, never hardcode tier order.
- **Analysis date prefix** — every agent prompt must start with the date prefix.
- **Banned vocabulary** — enforced by hooks. See `.claude/shared-rules.md` for the full list.
