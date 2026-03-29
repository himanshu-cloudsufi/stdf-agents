# STDF v2 -- Self-Contained Analysis System

STDF (Seba Technology Disruption Framework) v2 multi-agent pipeline with dynamic DAG orchestration. 24 agents, 15 lib modules, 956 empirical curves.

**Read `gotchas.md` before your first pipeline run** -- it lists common failure modes that are easy to miss.

## Key Directories

| Path | Purpose |
|------|---------|
| `.claude/agents/` | 24 agent definitions (18 pipeline + 1 research + 1 evaluator + 4 utility) |
| `shared-philosophy.md` | WHY behind the rules -- Tony's intellectual framework, axioms, epistemology (read by all agents) |
| `shared-rules.md` | Vocabulary, guardrails, disruption dynamics rules, computation rules (read by all agents) |
| `shared-glossary.md` | STDF concept definitions (read by all agents) |
| `shared-cost-rules.md` | Cost analysis rules (read by cost-chain agents) |
| `agent-memory/` | Persistent per-agent memory |
| `references/` | Agent registry, energy methodology docs |
| `lib/` | 15 Python computation modules (math, parsing, validation) |
| `data/` | 956 empirical time series curves (JSON, sector-organized) |
| `output/<slug>/` | Pipeline run outputs (one dir per analysis) |
| `scripts/` | CLI utilities (`query_curves.py`, `validate_pipeline.py`, `display_curve.py`) |
| `gotchas.md` | Common failure modes |

## Pipeline Rules

- File-based communication only -- agents write files, downstream agents read files
- Never skip the synthesizer -- raw agent outputs are not user-facing
- CRITICAL failure = pipeline stop
- Agent Registry is the single source of truth -- resolve DAG dynamically every time
- Always use python3

---

## Orchestration Principles

These five principles guide all orchestration decisions. When in doubt, return to these.

1. **SEBA First (NON-NEGOTIABLE).** When ANY query could be analyzed through mainstream economics (Phillips curve, Laffer curve, supply-demand equilibrium, GDP growth models, etc.), route through the SEBA disruption lens FIRST. Mainstream economics frameworks may provide context for understanding policymaker reaction functions, but they must NEVER be the primary analytical frame. The edge is in seeing what mainstream economists cannot: disruption dynamics. If a query about unemployment, inflation, energy prices, or GDP arrives, the first analytical move is always: "What disruption dynamics are at work here?" — not "What does conventional macroeconomics say?" See `shared-philosophy.md` for the full epistemological argument.

2. **Reason from the question to the agents.** When you receive a query, determine what analytical outputs the question needs to be answered. Then identify which agents produce those outputs. Then resolve the DAG backward from those goal agents to find all their dependencies. The agent set emerges from reasoning, not from keyword matching.

2. **The DAG is the only hard sequencing constraint.** Dependencies between agents are non-negotiable -- cost-fitter always runs after cost-researcher, tipping-synthesizer always after the three checkers, etc. But there is no mandatory numbered-step sequence beyond what the DAG dictates. You invoke capabilities (setup, classification approval, planning, execution, evaluation, presentation) as the situation requires.

3. **Exercise judgment on process gates.** The Phase 1 Hard Gate (classification approval), plan mode, and AskUserQuestion are tools for quality assurance. Use them when their value exceeds their cost:
   - Complex scope (FULL, ENERGY, COMMODITY, 8+ agents): always confirm classification and always use plan mode.
   - Limited scope (5 or fewer agents, obvious configuration): confirmation and plan mode are optional -- justify your choice.
   - When in doubt, ask.

4. **Fill gaps proactively.** If a specialist agent flags a data gap that would materially weaken downstream analysis, or if the query needs context outside any specialist's scope, inject the `stdf-research` agent to fill the gap before continuing.

---

## Quick Reference

**Agent Registry** -- the single source of truth for the pipeline DAG. Read `references/agent-registry.md` for the full registry with the detailed dependency graph and tier template.

**Dependency tiers (summary):**

```
Tier 1 (parallel):    domain-disruption, cost-researcher, capability
Tier 2:               cost-fitter
Tier 3 (parallel):    cost-parity-checker, capability-parity-checker, adoption-readiness-checker
Tier 4:               tipping-synthesizer
Tier 5a:              scurve-fitter
Tier 5b (parallel):   regional-adopter, xcurve-analyst
Tier 6 (conditional): demand-decomposer -> stream-forecaster -> fleet-modeler + regional-demand-analyst
Tier 7 (conditional): energy-dispatch -> gas-supply-decomposer
Flex:                 research (any tier -- injected when data gaps need filling)
Final:                synthesizer (always second-to-last)
Eval:                 evaluator (Haiku -- always last)
```

**Example Configurations:**

These are common agent configurations that recur across analyses. If your reasoned agent set matches one, use its label. They are reference shortcuts, not the primary selection mechanism -- the primary mechanism is Principle 1 (reason from the question to the agents).

| Configuration | Goal Agents | Example Trigger |
|---------------|-------------|-----------------|
| FULL | tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | Comprehensive disruption analysis with no specific focus |
| QUICK | cost-fitter, synthesizer | Cost overview, brief analysis, quick assessment |
| TIPPING_ONLY | tipping-synthesizer, synthesizer | Tipping point timing questions |
| COST_FOCUS | cost-fitter, capability, synthesizer | Cost trajectory, learning rate, price dynamics |
| ADOPTION_FOCUS | scurve-fitter, regional-adopter, xcurve-analyst, synthesizer | Market share, adoption curves |
| FULL+COMMODITY | FULL + demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst | Commodity demand/supply impact |
| ENERGY_FULL | FULL + energy-dispatch, gas-supply-decomposer | Energy sector dispatch, merit order, SWB displacement |
| ENERGY_GAS | FULL + energy-dispatch, gas-supply-decomposer | LNG/natural gas supply displacement |
| CUSTOM | Varies -- orchestrator lists goal agents explicitly | Query does not match any known configuration |

**Commodity keywords:** copper, aluminium, lithium, lead, cobalt, nickel, crude oil, natural gas, steel, silicon

**Energy keywords:** electricity generation, merit order, dispatch, SWB, grid, coal displacement, gas displacement, LNG, power generation, fossil fuel displacement

**Failure Matrix:**

| Criticality | On Failure | Penalty |
|-------------|-----------|---------|
| CRITICAL | STOP pipeline | -- |
| HIGH | Continue with warning | -0.3 |
| MEDIUM | Continue silently | -0.1 |

### Examples: Query -> Reasoning -> Configuration

- "Analyze the energy storage disruption" -- Comprehensive analysis with no specific focus. Needs domain mapping, cost dynamics, capability benchmarking, tipping conditions, adoption curves, incumbent decline. -> **FULL** (12 agents)

- "Quick overview of solar PV costs" -- Asks specifically about cost dynamics. Needs cost data and curve fitting, nothing else. -> **QUICK** (3 agents, auto-confirm)

- "When does autonomous driving tip?" -- Asks specifically about the tipping point. Needs the full tipping condition chain but not adoption curves or regional breakdown. -> **TIPPING_ONLY** (9 agents)

- "What's the copper demand impact of EV disruption?" -- Comprehensive analysis plus commodity demand decomposition. -> **FULL+COMMODITY** (16 agents)

- "Analyze SWB disruption of gas-fired power generation" -- Full analysis plus energy dispatch modeling. -> **ENERGY_FULL** (14 agents)

- "What is the capability gap between BEVs and ICE, and when does it close?" -- Asks specifically about capability, not cost or adoption. Goal agents: capability, capability-parity-checker, synthesizer. -> **CUSTOM** (5 agents: domain-disruption, cost-researcher, capability, capability-parity-checker, synthesizer)

---

## Step 0: Setup

1. Derive `<analysis-slug>` from the query (lowercase, hyphens, no spaces, no special chars). Examples: `energy-storage`, `electric-vehicles`, `lab-grown-meat`.
2. Get today's date in YYYY-MM-DD format -- this is the **analysis date**.
3. Create the output directory:

```bash
mkdir -p output/<analysis-slug>/agents
```

4. Store these values -- you'll use them in every agent prompt:
   - `SLUG` = the analysis slug
   - `DATE` = today's date (YYYY-MM-DD)
   - `QUERY` = the user's full query text
   - `OUTPUT_DIR` = `output/<slug>`
   - `AGENTS_DIR` = `output/<slug>/agents`

---

## Phase 1: Analyze Query & Select Agents

### 1a. Determine Goal Agents (ALWAYS)

1. Read the user's query carefully. Identify:
   - The sector or technology being analyzed
   - Any specified regions, time horizon, or context
   - What analytical outputs the question requires to be answered
   - **Convergence detection:** Does the query involve multiple sectors or technologies that could interact? (e.g., energy + transport, AI + labor, energy + AI + food). If yes, flag for cross-sector convergence analysis — this may require broader agent coverage than a single-sector analysis.
   - **SEBA-first check (Principle 1 enforcement):** Could this query be answered using mainstream economics (Phillips curve, Laffer curve, supply-demand equilibrium, GDP models)? If yes, the analysis MUST begin with: "What disruption dynamics are at work here?" Frame the entire response through cost-curve dynamics and STDF methodology. Mainstream economics may appear ONLY as a secondary section explaining policymaker reaction functions — never as the primary analytical frame. If the initial agent outputs return mainstream-first analysis, re-run the agent with explicit SEBA-first instructions.

2. Reason about which agents produce those outputs:
   - Does the question need cost dynamics? -> cost-researcher, cost-fitter
   - Does it need tipping point analysis? -> tipping-synthesizer (and its full dependency chain)
   - Does it need adoption curves? -> scurve-fitter
   - Does it need regional breakdown? -> regional-adopter
   - Does it need incumbent decline modeling? -> xcurve-analyst
   - Does it need commodity demand analysis? -> demand-decomposer and chain
   - Does it need energy dispatch/merit order? -> energy-dispatch, gas-supply-decomposer
   - Does it need supplementary research outside any specialist's scope? -> stdf-research

3. Resolve the DAG backward from goal agents. For each goal agent, walk the "Requires" column in the Agent Registry. Add every dependency.

4. Always add synthesizer (second-to-last) and evaluator (last).

5. Check if the resolved agent set matches a known configuration (see Example Configurations table). If it does, use that label. If not, label it "CUSTOM" and list the goal agents.

### 1b. Confirm with User (CONDITIONAL)

- **6+ agents or any FULL/ENERGY/COMMODITY configuration:** Use **AskUserQuestion**. Present the reasoned agent set with a 2-3 sentence explanation of why these agents are needed. Show the matched configuration label (or CUSTOM). Offer 2-3 alternative configurations as options.

- **5 or fewer agents where the configuration is obvious from the query:** You may auto-confirm. State the reasoning in your response (e.g., "The question asks specifically about cost dynamics, so I'm running QUICK: cost-researcher, cost-fitter, synthesizer, evaluator.").

- **Ambiguous queries:** Always ask. When in doubt, ask.

---

## Phase 1c: Classification Approval (after Tier 1 completes)

After Tier 1 agents finish (domain-disruption, cost-researcher, capability), review the domain-disruption output for classification data. Whether you present this for user approval depends on scope and risk of misclassification:

**MANDATORY** (always present for approval):
- FULL, ENERGY_FULL, ENERGY_GAS, FULL+COMMODITY configurations
- Any CUSTOM configuration with 8+ agents
- Any query where the sector is ambiguous or involves multiple sectors
- When domain-disruption lacks flow classification

**OPTIONAL** (may auto-approve with stated reasoning):
- QUICK, COST_FOCUS configurations
- CUSTOM configurations with 5 or fewer agents
- Queries where the sector, flow type, cost metric, and market type are all unambiguous

When auto-approving, state your reasoning (e.g., "Domain-disruption classified solar PV as Stellar with $/kWh cost metric and utility market type. This is straightforward for a solar cost analysis, so I'm proceeding without classification confirmation.").

### Gate procedure (when executed)

1. **Read** `output/{SLUG}/agents/01-domain-disruption.md` -- extract:
   - Disruption Map (disruptors, incumbents, chimeras)
   - Technology Flow Classification (if present)
   - Cost Metric Recommendation (from handoff context)
   - Market Type Recommendation (from handoff context)

2. **Classify** (if domain-disruption didn't already):
   - Flow type per technology: X-Flow / Stellar / Hybrid
   - Cost metric for parity: purchase price / $/kWh / $/km
   - Market type: consumer / fleet / enterprise / utility

3. **Present for approval** via AskUserQuestion:

   Q1: "Disruption scope" -- show extracted disruptors/incumbents, ask if correct
   Q2: "Cost parity metric" -- show recommendation + alternatives
   Q3: "Market type" -- show recommendation + alternatives

4. **If user approves:** Append `## Classification Overrides` section to 01-domain-disruption.md with the confirmed classifications. Continue to Phase 2 (Plan).

5. **If user overrides:**
   - Append `## User Overrides` section to 01-domain-disruption.md
   - If override changes disruptor/incumbent definition -> re-run cost-researcher and capability
   - If override changes only flow type / cost metric / market type -> continue without re-run

---

## Phase 2: Plan (CONDITIONAL)

**REQUIRED** when the agent set contains 6 or more agents. **OPTIONAL** when 5 or fewer agents and the configuration is obvious. When skipping plan mode, state the tier-by-tier execution sequence in your response before proceeding.

When using plan mode, use **EnterPlanMode** and build the execution plan:

### 2a. Resolve the DAG

1. From the goal agents determined in Phase 1a, **recursively resolve dependencies**: walk the "Requires" column in the Agent Registry. Add every agent whose output is needed.
2. Always add `stdf-synthesizer` as the final pipeline agent, followed by `stdf-evaluator`.

### 2b. Group into parallel tiers

- **Tier 1**: Agents with NO requirements (or whose requirements are already met by being outside the selected set)
- **Tier 2**: Agents whose requirements are ALL produced by Tier 1 agents
- Continue until all agents are placed
- Synthesizer is always second-to-last; evaluator is always last

### 2c. Write the plan

Include in the plan:
- Configuration label and reasoning for why these agents are needed
- Tier-by-tier table: tier number, agent names, parallelism (parallel/sequential)
- Agents skipped (not needed for this configuration)
- Critical path (longest sequential chain through the DAG)
- Total agent count

Use **ExitPlanMode** -- the user reviews and approves or modifies.

### 2d. Research injection points

While planning, identify potential research injection points -- places between tiers where supplementary research might be needed. Do not necessarily plan to use them, but note them. Common patterns:
- After Tier 1, if domain-disruption flags data gaps that affect downstream accuracy
- After Tier 4 (tipping-synthesizer), if tipping conditions depend on data not covered by any specialist
- Before Tier 6 or 7 (commodity/energy chains), if the query requires regulatory, geopolitical, or supply chain context

---

## Phase 3: Execute

Execute tier by tier. Each agent's `subagent_type` matches its name (e.g., agent `stdf-cost-fitter` uses `subagent_type: "stdf-cost-fitter"`).

### Agent prompt template

Every agent prompt MUST include these elements:

```
**Analysis date: {DATE}. All data after this date is forecast -- do NOT use web-sourced forecasts as observed values.**

QUERY: {full user query}

OUTPUT_FILE: output/{SLUG}/agents/{filename-from-registry}

UPSTREAM_FILES:
- output/{SLUG}/agents/{required-file-1}
- output/{SLUG}/agents/{required-file-2}
```

### Execution loop

For each tier in the plan:

1. **Launch all agents in the tier as parallel Agent tool calls** -- use a single message with multiple Agent tool uses.
2. **Wait for all agents in the tier to complete** before starting the next tier.
3. **Check for failures** after each tier completes:
   - **CRITICAL agent fails** -> STOP the pipeline immediately. Report the failure to the user. Do NOT proceed.
   - **HIGH agent fails** -> Log a warning, apply -0.3 confidence penalty, continue to next tier.
   - **MEDIUM agent fails** -> Apply -0.1 confidence penalty, continue.

### Agent re-run

If an agent's output is weak (low confidence, critical compliance criteria borderline, or data gaps that could be filled with a better prompt), you may re-run that individual agent with an adjusted prompt. You do not need to restart the entire tier. State the reason for re-run in your response.

### Research injection

Between tiers, if you determine that supplementary research would materially improve downstream quality, inject the `stdf-research` agent before continuing to the next tier:

```
**Analysis date: {DATE}. All data after this date is forecast -- do NOT use web-sourced forecasts as observed values.**

QUERY: {full user query}
RESEARCH_TOPIC: {specific topic to research}
CONTEXT: {why this research is needed -- which agent flagged the gap, what downstream agent will benefit}

OUTPUT_FILE: output/{SLUG}/agents/09-research-{topic-slug}.md

UPSTREAM_FILES:
- output/{SLUG}/agents/{relevant upstream files}
```

### Progress checklist

Copy this checklist into your response and update it as tiers complete. Only include tiers relevant to the chosen configuration.

```
- [ ] Tier 1: Foundation agents (domain-disruption, cost-researcher, capability)
- [ ] Phase 1 Gate: Classification approved (or auto-approved with reasoning)
- [ ] Tier 2: Cost fitting (cost-fitter)
- [ ] Tier 3: Condition checkers (cost-parity, capability-parity, adoption-readiness)
- [ ] Tier 4: Tipping synthesis (tipping-synthesizer)
- [ ] Tier 5a: Global S-curve (scurve-fitter)
- [ ] Tier 5b: Regional + X-curve (regional-adopter, xcurve-analyst)
- [ ] Tier 6: Commodity chain (demand-decomposer -> stream-forecaster -> fleet-modeler + regional-demand)
- [ ] Tier 7: Energy chain (energy-dispatch -> gas-supply-decomposer)
- [ ] Research: Supplementary research (if injected)
- [ ] Final: Synthesizer
- [ ] Evaluation: stdf-evaluator (Haiku)
```

Mark each tier with `[x]` (success), `[!]` (degraded), or `[X]` (failed) as it completes.

### Synthesizer special handling

The synthesizer runs after all analysis agents complete. Its `UPSTREAM_FILES:` must list ALL output files that were actually produced (not skipped) by the selected agents -- including any research agent outputs (`09-research-*.md`). It produces two files:
- `output/{SLUG}/00-final-synthesis.md` -- the 7-phase narrative
- `output/{SLUG}/agents/06-synthesizer.md` -- confidence metadata

---

## Phase 4: Evaluate

After the synthesizer completes, launch the **stdf-evaluator** agent (Haiku) to review the final report against all STDF guardrails.

```
Agent tool:
  subagent_type: stdf-evaluator
  model: haiku
  prompt: |
    OUTPUT_DIR: output/{SLUG}
    DATE: {DATE}

    Evaluate the final synthesis at output/{SLUG}/00-final-synthesis.md
    against all STDF guardrails. Write your report to output/{SLUG}/agents/07-evaluation.md.
```

The evaluator checks: banned vocabulary, hedging phrases, tone, terminology preservation, disruption dynamics guardrails (no mainstream anchoring, no constraint invention, no clipping, no incumbent protection, no long tail, S-curve thresholds, market trauma, chimera recognition, feedback loop consistency, data confidence tiers), analytical integrity, banned sources, and data-type tagging.

**On PASS:** Continue to Phase 5.

**On FAIL:** Read `output/{SLUG}/agents/07-evaluation.md` for the violation list. Fix the critical violations in `00-final-synthesis.md` directly, then re-run the evaluator. If the second pass still fails, present the violations to the user.

---

## Phase 5: Write Index & Present

### 5a. Write README.md

Write `output/{SLUG}/README.md` containing:
- Configuration used (label + reasoning) and total agent count
- Analysis date
- Tier-by-tier execution summary (agent names, confidence scores)
- Links to all output files produced
- Agents skipped and why
- Research injections used (if any) and their topics
- Evaluation result (from evaluator)
- Key conclusion and rupture window (from synthesizer)

### 5b. Present to user

Read `output/{SLUG}/00-final-synthesis.md` and present the final output with:
- Executive summary with key conclusion and rupture window
- Per-phase highlights (7 STDF phases)
- Per-agent confidence scores table
- Any warnings from degraded or skipped agents
- Supplementary research topics covered (if any)
- Data gaps and critical assumptions

---

## Important Rules

- **File-based communication only** -- agents write files, downstream agents read files. Never pass data blobs in prompts.
- **Never skip the synthesizer** -- raw agent outputs are not user-facing.
- **Never skip the evaluator** -- every synthesis must be evaluated before presenting to the user.
- **CRITICAL failure = pipeline stop** -- do not attempt workarounds.
- **Dynamic DAG resolution** -- always resolve from the Agent Registry, never hardcode tier order.
- **Analysis date prefix** -- every agent prompt must start with the date prefix.
- **Banned vocabulary** -- enforced by the evaluator agent. See `shared-rules.md` for the full list.
- **Agent re-run is permitted** -- if an agent's output is weak, you may re-run it individually without restarting the tier. State the reason.
- **Research injection is permitted** -- you may insert `stdf-research` between tiers when data gaps are identified. Include its output in the synthesizer's UPSTREAM_FILES.
- **Process gate justification** -- when you skip a user-facing gate (classification approval, plan mode), state your reasoning. This creates an audit trail.
- **Philosophy reference** -- when agents face edge cases not covered by specific rules, they should reason from `shared-philosophy.md`. The philosophy encodes the WHY behind the rules, enabling correct reasoning at novel situations.
- **SEBA First** -- every analysis must begin with the SEBA disruption lens. Mainstream economics (Phillips curve, Laffer curve, supply-demand equilibrium) may appear as secondary context for policymaker reaction functions, but never as the primary analytical frame.
