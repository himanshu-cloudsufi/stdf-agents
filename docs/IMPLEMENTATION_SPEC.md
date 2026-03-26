# Implementation Spec: STDF v2 Eval Gap Fixes (Consolidated)

**Source:** `EVAL_AUDIT_REPORT.md` (lead-demand-decline run) + `eval_gap_analysis.md` (202 sessions) + prior `AUDIT_REPORT.md` (bev-trucks-china)
**Date:** 2026-03-20
**Ship plan:** 3 PRs by layer
**Scope:** Existing 16 agents, shared-rules + companion files, lib modules
**Validation:** Dry-run cost-fitter + synthesizer on existing lead-demand upstream data

---

## Design Decisions (consolidated from both interviews)

| # | Decision | Choice | Source |
|---|----------|--------|--------|
| 1 | Fix scope | **Prompts + lib + shared-rules** (full pass) | Lead interview |
| 2 | Data-type tagging style | **Hybrid** — tables get section-level header tag; prose gets inline per-value tags | BEV interview |
| 3 | Synthesis tagging policy | **Agent attribution OK** — `(agent-name)` accepted in synthesis; agent files must use `[observed]`/`[model-derived]` | Lead interview |
| 4 | Sensitivity/scenario labels | **Ban all scenario-like labels** — use parameter values only (L=85%, r=0.10); "confidence range" replaces "scenario range" | Both |
| 5 | TCO / cost aggregation | **No TCO allowed** — disaggregated cost stack only | BEV interview |
| 6 | Cost parity metric | **Purchase price crossover** as default; domain-disruption specifies per analysis | BEV interview |
| 7 | IEA/EIA/BNEF/OPEC policy | **Match shared-rules (relaxed)** — allowed if tagged `[CAUTION: {org} source]`, violation only if tag missing | Lead interview |
| 8 | STDF glossary/concepts | **Core 10-15, reference only** — agents check definitions for accuracy, don't have to use exact phrasing | Lead interview |
| 9 | Cost rules file | **Separate shared-cost-rules.md** with 4 rules: cost/price, consumer vs commercial, LCOE limitations, no TCO | Lead interview |
| 10 | Jevons Paradox handling | **Warn and self-classify** — agent self-classifies X-Flow/Stellar if orchestrator tag missing, emits warning | Lead interview |
| 11 | Domain-disruption completeness | **End-use cross-reference** — verify every segment >5% has a disruption assessment | Lead interview |
| 12 | Learning rate plausibility | **In lib/cost_curve_math.py** — new `plausibility_check()` function | Lead interview |
| 13 | Orchestrator auto-detect | **Skip confirm for obvious** presets — high-confidence matches proceed without asking | Lead interview |
| 14 | Synthesizer consistency | **Pre-conclusion audit** — verify no entity marked "benefiting" is also a disruption victim | Lead interview |
| 15 | Phase 1 hard gate | **Yes** — pause after Phase 1, show disruption map + classifications for user approval | BEV interview |
| 16 | User override mechanism | **Append override section** to domain-disruption.md; downstream agents read and apply | BEV interview |
| 17 | New agents | **Deferred** — existing 16 only; labor/macro/investment agents are separate project | Lead interview |
| 18 | Validation approach | **Dry-run cost-fitter + synthesizer** against existing lead-demand upstream data | Lead interview |

---

## PR1: Shared Files + Lib Changes

### 1.1 Create `shared-glossary.md`

New file: `.claude/shared-glossary.md`

**Contents — STDF concept definitions:**

| Term | Definition |
|------|-----------|
| **God Parity** | When rooftop solar cost < transmission & distribution (T&D) costs alone, making centralized utilities structurally uncompetitive regardless of generation source |
| **X-Flow** | Technologies involving physical resource throughput (oil, gas, coal, minerals). Cost reduction follows material and process learning. Jevons Paradox applies. |
| **Stellar** | Technologies with zero or near-zero marginal cost at scale (solar PV, wind, batteries, AI/software). Cost follows exponential learning curves. Jevons Paradox does NOT apply. |
| **Hybrid** | Technologies with both X-Flow and Stellar components (e.g., BEV trucks: Stellar battery + X-Flow minerals). Classification follows the dominant cost driver. |
| **SWB** | Solar + Wind + Batteries convergence combination |
| **BSAF** | Battery-Swap + Autonomous driving + Fleet-management software convergence |
| **Chimera** | A technology that combines characteristics of both disruptor and incumbent. Typically shows a hump-shaped adoption curve — rises then falls as the pure disruptor overtakes it. |
| **Convergence** | When multiple independent disruptions combine to create emergent capabilities exceeding the sum of parts |
| **Artificial Labor (AL)** | AI systems performing cognitive tasks previously done by humans. A Stellar technology — Jevons Paradox does not apply. |
| **Cost-curve dynamics** | The mechanism by which cumulative production drives cost reduction via learning effects. Replaces "Wright's Law" — never use that term. |
| **Incumbent displacement** | The process by which disruptors capture market share from incumbents. Replaces "phase-out", "retirement", "transition". |
| **S-curve adoption** | The logistic growth pattern of technology adoption. Replaces "linear growth", "gradual adoption". |
| **Disruption** | Technology-driven market transformation following S-curve dynamics. Replaces "transition" in all contexts. |
| **AI Capability Improvement** | The rate at which AI systems improve performance. NOT "AI Capability Growth" — growth implies quantity, improvement implies quality. |
| **Digital worker** | Token supply equivalent (Epoch AI concept) — the computational output of AI measured in human-equivalent task units. NOT unemployment/displacement. |

### 1.2 Create `shared-cost-rules.md`

New file: `.claude/shared-cost-rules.md`

**Contents:**

```markdown
# STDF Cost Analysis Rules

Read by: cost-researcher, cost-fitter, cost-parity-checker, demand-decomposer,
         stream-forecaster, fleet-modeler, regional-demand-analyst, synthesizer

## Rule 1: No TCO Aggregation (STRICT)

NEVER aggregate cost components into a single "Total Cost of Ownership" (TCO),
"lifecycle cost", or "all-in cost" figure. Present each cost component as a
separate line item:

- **Purchase price** (hardware sticker price in local currency)
- **Energy cost per unit of service** ($/kWh, CNY/km, etc.)
- **Maintenance cost per unit of service** (if sourced; drop if unsourced)
- **Battery/consumable replacement cost** (if applicable, with timing)
- **Infrastructure cost allocation** (if applicable)

Each component must have its own source citation. Unsourced components are
DROPPED, not estimated. If a component is material but unsourced, note it in
Data Gaps.

## Rule 2: Cost Parity Metric

The cost parity metric is specified by the /stdf skill classification step in
the domain-disruption output file, under `## Classification Overrides` or
`## Handoff Context > Cost Metric`.

**Default hierarchy:**
1. Purchase price crossover (consumer markets, fleet markets with high
   upfront sensitivity)
2. Dominant operating cost component crossover (fleet/enterprise markets
   where operating cost drives procurement — e.g., energy $/km for trucking)
3. Service-level unit crossover (utility/infrastructure markets with no
   meaningful "purchase price" — e.g., $/kWh delivered for grid storage)

The cost-fitter MUST compute the crossover for the metric specified. It MAY
additionally compute other crossovers as supplementary information but must
clearly label which is the PRIMARY parity metric.

## Rule 3: Market Type Classification

The market type (consumer / fleet / enterprise / utility) determines which
cost component is the dominant purchase criterion:

| Market Type | Dominant Cost Component | Rationale |
|-------------|----------------------|-----------|
| Consumer | Purchase price | Consumers optimize on sticker price, not lifetime economics |
| Fleet | Dominant operating cost (energy/km, $/kWh) | Fleet operators optimize on operating margin per unit of service |
| Enterprise | Purchase price + operating cost (varies) | Enterprise procurement balances capex vs opex |
| Utility | Service-level cost ($/kWh delivered, $/MW capacity) | Utilities procure on levelized service cost |

The cost-fitter highlights the dominant component per the market type
classification but ALWAYS shows all disaggregated components.

## Rule 4: No Scenario Labels (STRICT)

NEVER use scenario labels in cost projections:
- Banned: "base case", "bull case", "bear case", "optimistic", "pessimistic",
  "conservative", "aggressive", "best case", "worst case"

For parameter sensitivity analysis:
- Use parameter values as labels: "r=0.10", "L=85%", "k=0.72"
- Present as: "Primary: X (range: Y–Z from [parameter] uncertainty)"
- Single primary estimate with range, not three named scenarios
```

### 1.3 Modify `shared-rules.md`

**Changes:**

1. **Add file routing header:**
```markdown
## Companion Files
- `.claude/shared-glossary.md` — STDF concept definitions (read by all agents)
- `.claude/shared-cost-rules.md` — Cost analysis rules (read by cost-chain agents)
```

2. **Add to Banned Vocabulary table:**

| Banned Term | Use Instead |
|---|---|
| TCO / total cost of ownership | Disaggregated cost stack (see shared-cost-rules.md) |
| lifecycle cost | Disaggregated cost components |
| base case / bull case / bear case | Parameter value labels (L=85%, r=0.10) |
| optimistic scenario / pessimistic scenario | Parameter sensitivity range |
| AI Capability Growth | "AI Capability Improvement" |

3. **Add Jevons Paradox rule:**
```markdown
## Context-Dependent Rules

### Jevons Paradox
- **X-Flow technologies** (physical resource throughput): Jevons Paradox
  MAY be referenced. Tag: "demand elasticity via Jevons effect (X-Flow)".
- **Stellar technologies** (solar, wind, battery, AI/AL): Jevons Paradox
  MUST NOT be used. These technologies have zero/near-zero marginal cost;
  demand scaling follows different economics.
- **Gate:** The /stdf skill classification step assigns each technology
  an X-Flow/Stellar/Hybrid tag. Downstream agents check this tag before
  invoking Jevons.
```

4. **Add IEA/EIA/BNEF/OPEC source rule (replace current ban):**
```markdown
### Banned Organization Policy (UPDATED)
IEA, EIA, BNEF, and OPEC sources are permitted ONLY under ALL of these conditions:
1. The data is OBSERVED and HISTORICAL (not a forecast or scenario)
2. Tagged with `[CAUTION: {org} source — historical data only]`
3. A primary government source was searched first and not found
4. The data point is NOT used as a basis for forward projections

If ANY condition fails → DISCARD the data point.
```

5. **Add data-type tagging enforcement rule:**
```markdown
## Data-Type Tagging (MANDATORY)

Every numerical value in output must be tagged as `[observed]` or `[model-derived]`.

### Tagging rules by output format:
- **Prose/narrative:** Tag each number inline: "86.4% [model-derived]"
- **Tables with mixed data types:** Include a `Data Type` column as the
  last column
- **Tables where ALL values share the same data type:** Use a header
  annotation instead of a column:
  `**All values in this table: [model-derived] from upstream S-curve parameters**`
- **Tables with mixed types but no column:** This is NON-COMPLIANT

### Self-check before output:
Every agent MUST verify: are there any tables or prose sections containing
future-year numbers without data-type tags? If yes, fix before writing.
```

### 1.4 Modify `lib/vocabulary.py`

**Changes:**

1. **Add to `BANNED_TERMS`:**
```python
"total cost of ownership": "disaggregated cost stack",
"TCO": "disaggregated cost components",
"lifecycle cost": "disaggregated cost components",
"base case": "parameter value (e.g., L=85%)",
"bull case": "parameter value",
"bear case": "parameter value",
"optimistic scenario": "parameter sensitivity range",
"pessimistic scenario": "parameter sensitivity range",
"best case": "parameter value",
"worst case": "parameter value",
"AI capability growth": "AI capability improvement",
```

2. **Populate `BANNED_SOURCE_PATTERNS`:**
```python
BANNED_SOURCE_PATTERNS = [
    {"pattern": r"iea\.org", "reason": "IEA source — use primary government data; if unavoidable, tag [CAUTION: IEA source]"},
    {"pattern": r"eia\.gov", "reason": "EIA source — use primary government data"},
    {"pattern": r"bnef\.com", "reason": "BNEF source — use primary data"},
    {"pattern": r"opec\.org", "reason": "OPEC source — use primary data"},
]
```

Note: These will trigger as warnings, not hard blocks — agents that legitimately use IEA historical data with the `[CAUTION:]` tag will see the warning but the `[CAUTION:]` tag indicates intentional use.

### 1.5 Modify `lib/guardrails.py`

**Changes:**

1. **Add `validate_anti_scenario_terms(text)`:**
```python
def validate_anti_scenario_terms(text):
    """Scan for banned scenario-label language."""
    terms = [
        "base case", "bull case", "bear case",
        "optimistic scenario", "pessimistic scenario",
        "best case", "worst case", "base scenario",
        "conservative scenario", "aggressive scenario",
    ]
    violations = []
    for term in terms:
        if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
            violations.append({"term": term, "issue": "Banned scenario label — use parameter values"})
    return violations
```

2. **Add `validate_data_type_tags(text, analysis_date)`:**
```python
def validate_data_type_tags(text, analysis_date):
    """Flag lines with future-year numbers lacking [observed]/[model-derived] tags."""
    issues = []
    analysis_year = int(analysis_date[:4])
    for i, line in enumerate(text.split('\n')):
        # Skip headers, separators, source sections
        if line.startswith('#') or line.startswith('|--') or 'source' in line.lower()[:15]:
            continue
        # Check for section-level tag (covers all lines until next section)
        # ... (check if within a tagged section)
        # Find future-year references
        future_years = re.findall(r'20[3-9]\d|20[2-9][7-9]', line)
        if future_years:
            has_tag = '[model-derived]' in line or '[observed]' in line
            has_section_tag = False  # Check preceding lines for section-level tag
            if not has_tag and not has_section_tag:
                nums = re.findall(r'\d+\.?\d*%|\$[\d,]+|\d+\.\d+ [A-Z]', line)
                if nums:
                    issues.append({"line": i+1, "issue": f"Future year with untagged numbers: {line.strip()[:80]}"})
    return issues
```

3. **Add both to `full_guardrail_check()`:**
   - `validate_anti_scenario_terms` → critical violations
   - `validate_data_type_tags` → warnings (not critical, to avoid blocking on edge cases initially)

---

## PR2: Agent Prompt Changes

### 2.1 `stdf-domain-disruption.md`

**Add to output requirements:**

```markdown
### New Required Section: Technology Flow Classification

After the Disruption Map, include a dedicated section:

## Technology Flow Classification

For each technology in the Disruption Map, classify:

| Technology | Flow Type | Reasoning |
|-----------|-----------|-----------|
| [disruptor] | Stellar / X-Flow / Hybrid | One-line reasoning citing the dominant cost mechanism |
| [incumbent] | Stellar / X-Flow / Hybrid | One-line reasoning |
| [chimera] | Stellar / X-Flow / Hybrid | One-line reasoning |

Full reasoning paragraph for each classification explaining:
- Why this technology is X-Flow (physical throughput) or Stellar (zero marginal cost)
- For Hybrid: which component dominates the cost structure
- Implications for downstream analysis (Jevons applicability, cost metric choice)
```

**Add to Handoff Context requirements:**
```markdown
### Handoff Context must include:
- `Cost Metric Recommendation`: which cost metric the /stdf skill should
  use for parity (purchase price, $/kWh, $/km, etc.) with justification
- `Market Type Recommendation`: consumer / fleet / enterprise / utility
  with justification
```

**Add shared file routing:**
```markdown
### Shared Files
Read at start of every run:
- `.claude/shared-rules.md`
- `.claude/shared-glossary.md`
```

### 2.2 `stdf-cost-researcher.md`

**Changes:**
- Add: "Read `.claude/shared-cost-rules.md` at start of every run"
- Add: "Present cost data as DISAGGREGATED components. Never aggregate into TCO."
- Add: "If a cost component (e.g., maintenance) has no source, note it in Data Gaps. Do NOT provide an unsourced estimate."
- Add IEA source rule: "IEA/EIA/BNEF/OPEC historical data permitted only with `[CAUTION: {org} source]` tag and after primary source search"

### 2.3 `stdf-cost-fitter.md`

**Changes:**
- Add: "Read `.claude/shared-cost-rules.md` at start of every run"
- Remove: All TCO model construction logic
- Add: "Present cost analysis as disaggregated cost stack. Compute crossovers per component, not aggregated."
- Add: "The primary cost parity metric is specified in the domain-disruption handoff context. Compute the crossover for THAT metric."
- Add: "Label sensitivity analysis rows by parameter values (r=0.10, L=85%), NEVER by scenario names (conservative, optimistic)"
- Replace: `competitive_threshold` documentation to reference purchase price crossover as default

### 2.4 `stdf-cost-parity-checker.md`

**Changes:**
- Add: "Read `.claude/shared-cost-rules.md` at start of every run"
- Change: "Cost parity = crossover of the cost metric specified in domain-disruption handoff. Default: purchase price. Read the `Cost Metric` field from 01-domain-disruption.md handoff context."
- Remove: Any TCO-based parity logic

### 2.5 `stdf-scurve-fitter.md`

**Changes:**
- Add: "NEVER use scenario labels. Label sensitivity rows by parameter values: L=85%, L=90% (primary), L=95%. Not Conservative/Primary/Optimistic."
- Add data-type tagging rule: "Every projection table MUST have either a Data Type column (for mixed tables) or a section header annotation (for uniform model-derived tables)."
- Add: "Read `.claude/shared-glossary.md` at start of every run"

### 2.6 `stdf-stream-forecaster.md` (math agent)

**Add mandatory output template:**
```markdown
### Output Table Template (REQUIRED)

Every projection table MUST follow this structure. For tables where ALL
values are model-derived, use a header annotation:

**All values: [model-derived] from upstream S-curve (L={L}, k={k}, x0={x0})**

| Horizon | Year | Incumbent (kt) | Disruptor (kt) | Chimera (kt) | Total (kt) |
|---------|------|----------------|----------------|--------------|------------|

For tables with mixed observed/model-derived values, add a Data Type column:

| Year | Value | Unit | Data Type |
|------|-------|------|-----------|
```

### 2.7 `stdf-fleet-modeler.md` (math agent)

**Add mandatory output template:**
```markdown
### Output Table Template (REQUIRED)

**All values: [model-derived] from stock-flow model with upstream sales projections**

| Year | Fleet | Sales | Scrappage | Net Change | OEM Demand | Replacement Demand | Total |
|------|-------|-------|-----------|------------|------------|-------------------|-------|

For the OEM/Replacement split summary, use the same header annotation pattern.
No TCO figures. If material intensity is computed, cite the source per-value.
```

### 2.8 `stdf-regional-demand-analyst.md` (math agent with web)

**Add mandatory output template:**
```markdown
### Output Table Template (REQUIRED)

Regional projection tables:

**All projections: [model-derived] from regional S-curve parameters (see 05b)**

| Region | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) | Unit |
|--------|------|-------------|-------------|-------------|------|

Mixed tables (observed base year + projections) MUST use Data Type column.
```

### 2.9 `stdf-xcurve-analyst.md`

**Changes:**
- Add data-type tagging: "The X-curve decline table is [model-derived] from the disruptor S-curve mirror. Use a header annotation."
- Add: "Read `.claude/shared-glossary.md` at start of every run"

### 2.10 `stdf-capability-parity-checker.md`

**Changes:**
- Add: "Read `.claude/shared-glossary.md` at start of every run"
- Add: "Check the X-Flow/Stellar classification from domain-disruption. If any capability dimension invokes Jevons Paradox, verify it applies only to X-Flow technologies."

### 2.11 `stdf-synthesizer.md`

**Changes:**
- Add: "Read `.claude/shared-cost-rules.md` and `.claude/shared-glossary.md` at start of every run"
- Add: "NEVER aggregate cost components into TCO in the synthesis. Present the disaggregated cost stack as the cost-fitter produced it."
- Add: "Check for User Overrides section in 01-domain-disruption.md. If present, apply overrides to the synthesis narrative."
- Add: "Verify data-type tags in your own output: every future-year number in prose must have `[model-derived]` inline."
- Add: "Label sensitivity as parameter ranges, not scenario names."

### 2.12 All 16 Agent Definitions — File Routing Update

Add to each agent's header/preamble which shared files it reads:

| Agent | Reads |
|-------|-------|
| domain-disruption | shared-rules, shared-glossary |
| cost-researcher | shared-rules, shared-glossary, shared-cost-rules |
| capability | shared-rules, shared-glossary |
| cost-fitter | shared-rules, shared-glossary, shared-cost-rules |
| cost-parity-checker | shared-rules, shared-cost-rules |
| capability-parity-checker | shared-rules, shared-glossary |
| adoption-readiness-checker | shared-rules, shared-glossary |
| tipping-synthesizer | shared-rules, shared-glossary, shared-cost-rules |
| scurve-fitter | shared-rules, shared-glossary |
| regional-adopter | shared-rules, shared-glossary |
| xcurve-analyst | shared-rules, shared-glossary |
| demand-decomposer | shared-rules, shared-glossary, shared-cost-rules |
| stream-forecaster | shared-rules, shared-glossary, shared-cost-rules |
| fleet-modeler | shared-rules, shared-glossary, shared-cost-rules |
| regional-demand-analyst | shared-rules, shared-glossary, shared-cost-rules |
| synthesizer | shared-rules, shared-glossary, shared-cost-rules |

---

## PR3: /stdf Skill Changes

### 3.1 Classification Step (New — between Step 1 and Step 2)

After the `/stdf` skill parses the query and before entering Plan Mode, add a **Classification Step**:

1. Read the domain-disruption agent's handoff context (specifically: Cost Metric Recommendation, Market Type Recommendation)
2. Read the domain-disruption agent's Technology Flow Classification section
3. Classify:
   - **Flow type** per technology: X-Flow / Stellar / Hybrid
   - **Cost metric** for parity: purchase price / $/kWh / $/km / etc.
   - **Market type**: consumer / fleet / enterprise / utility
4. Present to user for approval (hard gate)

### 3.2 Phase 1 Hard Gate (Modified Step 3)

After Phase 1 agents complete (domain-disruption, cost-researcher, capability all finish):

1. Read `01-domain-disruption.md` output
2. Run the classification step (3.1 above) using domain-disruption's recommendations
3. Present to user via `AskUserQuestion`:
   - Disruption map summary (3-line: disruptors, incumbents, chimeras)
   - Flow classification (X-Flow/Stellar per technology)
   - Cost metric (which metric for parity)
   - Market type (consumer/fleet/enterprise/utility)
4. **WAIT for user approval**
5. If user approves: write classifications to `01-domain-disruption.md` under `## Classification Overrides` section; continue to Phase 2
6. If user overrides:
   - Append `## User Overrides` section to `01-domain-disruption.md` with corrections
   - If override changes disruptor/incumbent definition: **re-run cost-researcher and capability** with override context
   - If override changes only flow type / cost metric / market type: **continue to Phase 2** without re-running

### 3.3 Validation Step (Modified Step 4)

Add to the existing validation step:
- Run `validate_anti_scenario_terms()` on all output files
- Run `validate_data_type_tags()` on all output files
- Report findings as warnings (not blockers for initial rollout)

---

## NEW Work Items (from lead-demand-decline audit)

### NEW-1: `lib/cost_curve_math.py` — Learning rate plausibility check

**Priority:** P1

Add function:
```python
def plausibility_check(learning_rate_pct, technology_class):
    """
    Check if a derived learning rate falls within historical bounds.

    Technology classes and historical bounds (per-year):
        batteries: 12-28%
        solar_pv: 18-32%
        wind: 8-18%
        compute: 25-50%
        generic: 5-35%

    Returns: dict with status (NORMAL/CAUTION/IMPLAUSIBLE),
             bounds, and explanation.
    """
```
- `plausibility_check(16.81, "batteries")` → `{"status": "NORMAL"}`
- `plausibility_check(5.5, "batteries")` → `{"status": "CAUTION"}`
- `plausibility_check(55.0, "batteries")` → `{"status": "IMPLAUSIBLE"}`

### NEW-2: `stdf-domain-disruption.md` — End-use completeness cross-reference

**Priority:** P1

Add after the disruption vector mapping section:
> **Completeness Cross-Reference (MANDATORY):**
> After mapping all disruption vectors, perform a completeness check:
> 1. Look up the commodity/sector's end-use breakdown (from catalog or web)
> 2. List every end-use segment that represents >5% of total demand
> 3. Verify each has either: a mapped disruption vector, or an explicit "no disruptor identified" assessment
> 4. If any segment >5% is missing, flag it as a data gap and attempt to assess it
>
> Present as a table:
> | End-Use Segment | % of Demand | Disruption Vector Mapped? | Assessment |
> Example: T-25 eval failure — 12V SLI vector was missed because no completeness check was performed.

### NEW-3: `stdf-cost-fitter.md` — Plausibility check + confidence range

**Priority:** P1

Add:
> After deriving the learning rate, call `lib.cost_curve_math.plausibility_check(learning_rate_pct, technology_class)`. If status is CAUTION or IMPLAUSIBLE, document in your output and Data Gaps section. An IMPLAUSIBLE learning rate should trigger re-investigation of data inputs before accepting.

Global replace in prompt: "scenario range" → "confidence range"

### NEW-4: `stdf-synthesizer.md` — Pre-conclusion consistency audit

**Priority:** P0

Add before the Phase 7 writing instructions:
> **Pre-Conclusion Consistency Audit (MANDATORY):**
> Before writing Phase 7 (Synthesis & Tipping Point) and the Key Conclusion:
> 1. List every technology, company, or sector mentioned as "benefiting" or "growing" in your draft
> 2. Cross-check each against X-curve analyst (05c) and domain-disruption (01):
>    - Entity identified as disruption victim? → CONTRADICTION — rewrite
>    - Entity identified as incumbent in decline? → CONTRADICTION — rewrite
> 3. Cross-check positioning implications against cost-parity (04a) findings
> 4. Document: "Consistency audit: [N] entities checked, [M] contradictions found and resolved"
>
> This prevents recommending positions contradicting the pipeline's own findings (ref: R-42 eval — "long nuclear" while pipeline showed battery disruption).

Add:
> In the final synthesis (00-final-synthesis.md), you may attribute data to upstream agents by name: "(stream-forecaster)", "(cost-fitter)". This is accepted as equivalent to [observed]/[model-derived] tagging IN THE SYNTHESIS ONLY.

### NEW-5: `/stdf` SKILL.md — X-Flow/Stellar classification + auto-detect

**Priority:** P1

1. **X-Flow/Stellar classification in Step 1:**
   > After detecting sector and preset, classify the primary technology as:
   > - **X-Flow:** physical resource throughput (oil, gas, coal, metals)
   > - **Stellar:** zero-marginal-cost flows (solar, wind, batteries, AI/AL)
   > - **Hybrid:** mixed (e.g., hydrogen = X-Flow production + Stellar electrolysis)
   > Pass to ALL downstream agents as: `Technology class: [X-Flow|Stellar|Hybrid]`

2. **Auto-detect without confirmation:**
   > If the query clearly maps to a single preset with high confidence, skip AskUserQuestion and proceed. Log: "Auto-detected preset: [PRESET] (high confidence)".
   > Still ask when: multiple presets could apply, query is ambiguous, or commodity add-on is possible but not certain.

3. **Replace "scenario range" → "confidence range"** in all output templates.

### NEW-6: Global find/replace across all agent prompts

**Priority:** P2

- "scenario range" → "confidence range" in all 16 agent .md files and skill .md files
- Cost-chain agents (cost-researcher, cost-fitter, cost-parity-checker, demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst, synthesizer): add reference to `shared-cost-rules.md`
- All agents: ensure reference to `shared-glossary.md`

### NEW-7: Jevons Paradox self-classification in agents

**Priority:** P2

Add to all agents that might reference demand elasticity or Jevons:
> If the orchestrator did not provide an X-Flow/Stellar tag, self-classify the technology from the disruption map and emit: "X-Flow/Stellar tag not provided by orchestrator; self-classified as [type]." Check shared-glossary.md for definitions. If technology is Stellar, Jevons Paradox MUST NOT be referenced.

Primarily affects: stdf-capability, stdf-xcurve-analyst, stdf-stream-forecaster, stdf-synthesizer.

---

## Validation Plan

**Dry-run validation** on existing lead-demand upstream data:

### Test 1: Cost-fitter dry-run
Re-run `stdf-cost-fitter` reading existing `02a-cost-researcher.md`. Verify:
- Learning rate plausibility check appears in output
- "confidence range" used (not "scenario range")
- shared-cost-rules.md unit hierarchy followed
- No TCO aggregation

### Test 2: Synthesizer dry-run
Re-run `stdf-synthesizer` reading all existing lead-demand agent outputs. Verify:
- Pre-conclusion consistency audit documented
- Agent attribution used for data provenance
- "confidence range" used throughout
- Zero banned vocabulary or anti-patterns

### Test 3: Guardrail validation
Run `lib.guardrails.full_guardrail_check()` on both dry-run outputs. Verify:
- Zero critical violations
- Anti-scenario detection catches "base case", "scenario range"
- Banned source detection catches untagged BNEF/IEA references

### Test 4: Cross-run comparison (lead-demand-decline)
Compare new dry-run outputs against original lead-demand-decline outputs:
- Source tagging coverage: should improve from 21% to >50% in synthesis
- Scenario language: should drop from 4 instances to 0
- BNEF mentions: should be properly tagged or removed

---

## Execution Order

| Step | Work Items | Dependencies | Files Changed |
|------|-----------|-------------|---------------|
| 1 | Create shared-glossary.md + shared-cost-rules.md (1.1, 1.2) | None | 2 new |
| 2 | Update shared-rules.md (1.3) — already partially done | None | 1 |
| 3 | Update lib/vocabulary.py (1.4) | None | 1 |
| 4 | Update lib/guardrails.py (1.5) + lib/cost_curve_math.py (NEW-1) | Step 3 | 2 |
| 5 | Agent prompts: domain-disruption (2.1 + NEW-2) | Steps 1-2 | 1 |
| 6 | Agent prompts: cost-chain (2.2-2.4 + NEW-3) | Steps 1-2 | 3 |
| 7 | Agent prompts: synthesizer (2.11 + NEW-4) | Steps 1-2 | 1 |
| 8 | Agent prompts: S-curve, X-curve, math agents (2.5-2.10) | Steps 1-2 | 6 |
| 9 | Agent prompts: remaining + global replacements (2.12 + NEW-6 + NEW-7) | Steps 1-2 | 5 |
| 10 | Skill changes: /stdf + gotchas (3.1-3.3 + NEW-5) | Steps 1-4 | 2 |
| 11 | Dry-run validation (Tests 1-4) | All above | 0 (test only) |

**Total: ~24 files** (2 new, 3 lib, 16 agents, 2 skills, 1 shared-rules)

---

## Files Modified Summary

### PR1: Shared Files + Lib (6 files)
| File | Action |
|------|--------|
| `.claude/shared-glossary.md` | **CREATE** — STDF concept definitions (10-15 core terms) |
| `.claude/shared-cost-rules.md` | **CREATE** — Cost analysis rules (4 rules) |
| `.claude/shared-rules.md` | **MODIFY** — Already partially updated; verify companion file refs, banned terms, Jevons, IEA policy, data-type tagging |
| `lib/vocabulary.py` | **MODIFY** — Add banned terms (scenario labels, AI terminology), populate BANNED_SOURCE_PATTERNS (context-aware) |
| `lib/guardrails.py` | **MODIFY** — Add validate_anti_scenario_terms, validate_data_type_tags, update source validation |
| `lib/cost_curve_math.py` | **MODIFY** — Add plausibility_check() function |

### PR2: Agent Prompts (16 files)
| File | Action | Key Changes |
|------|--------|-------------|
| `stdf-domain-disruption.md` | **MODIFY** | Flow Classification + end-use completeness cross-reference + handoff requirements |
| `stdf-cost-researcher.md` | **MODIFY** | No TCO, disaggregated stack, IEA CAUTION rule, shared-cost-rules ref |
| `stdf-cost-fitter.md` | **MODIFY** | Plausibility check, no TCO, confidence range, shared-cost-rules ref |
| `stdf-cost-parity-checker.md` | **MODIFY** | Purchase price parity default, read cost metric from upstream |
| `stdf-capability-parity-checker.md` | **MODIFY** | Jevons gate check, self-classify warning |
| `stdf-scurve-fitter.md` | **MODIFY** | No scenario labels, data-type tagging, confidence range |
| `stdf-xcurve-analyst.md` | **MODIFY** | Data-type tagging, Jevons self-classify |
| `stdf-stream-forecaster.md` | **MODIFY** | Mandatory output template, Jevons self-classify |
| `stdf-fleet-modeler.md` | **MODIFY** | Mandatory output template |
| `stdf-regional-demand-analyst.md` | **MODIFY** | Mandatory output template |
| `stdf-synthesizer.md` | **MODIFY** | Pre-conclusion audit, agent attribution policy, no TCO, check overrides |
| `stdf-adoption-readiness-checker.md` | **MODIFY** | File routing |
| `stdf-tipping-synthesizer.md` | **MODIFY** | File routing |
| `stdf-capability.md` | **MODIFY** | File routing, Jevons self-classify |
| `stdf-demand-decomposer.md` | **MODIFY** | File routing, shared-cost-rules ref |
| `stdf-regional-adopter.md` | **MODIFY** | File routing |

### PR3: Skill Changes (2 files)
| File | Action | Key Changes |
|------|--------|-------------|
| `.claude/skills/stdf/SKILL.md` | **MODIFY** | X-Flow/Stellar classification, auto-detect, Phase 1 hard gate, override mechanism, confidence range |
| `.claude/skills/stdf/gotchas.md` | **MODIFY** | Hard gate notes, override flow, Jevons tag reminder, confidence range |

---

## Out of Scope (Deferred)

| Item | Reason |
|------|--------|
| New agents (labor-impact, macro-impact, investment-analyst) | Separate project — existing 16 only |
| Data catalog additions (2W/3W, AI compute, pharma) | Data curation project, not prompt fix |
| Monthly resolution in scurve_math | Architectural change to lib |
| Run comparison skill (/stdf-compare) | New feature, not a fix |
| Retroactive data-type tag format in agent prompts | Trust shared-rules.md (interview decision) |
