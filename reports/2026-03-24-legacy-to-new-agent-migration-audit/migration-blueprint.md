# Migration Blueprint

## Executive recommendation

Do not migrate the old system verbatim.

Do not rebuild the old capabilities from a blank slate either.

Use this rule:

- rebuild workflow and orchestration natively in the new STDF platform
- preserve old sector logic as the reference specification
- wrap old sector engines temporarily where necessary
- delete old paths only after regression parity is proven

This is the cleanest way to get a better architecture without losing validated business logic.

## Four-way split

Every legacy asset should fall into one of four buckets:

1. Rebuild fresh in the new system
2. Extract and preserve as canonical logic
3. Wrap temporarily as a canonical backend
4. Delete after parity is achieved

## 1. Rebuild Fresh

These should be redesigned natively for the new `.claude` STDF stack rather than ported line-by-line.

### Orchestration and request handling

Rebuild fresh:

- `main_agent_system.txt`
- `planner_system.txt`
- `reformulator_system.txt`
- `clarification_system.txt`

Why:

- The new STDF orchestrator is structurally better.
- The old prompt wording is not the asset; the decision logic is.
- Routing and clarification should live as structured orchestration behavior, not as long free-text prompts.

What to keep from the old system:

- skill-sovereignty rule
- sector detection logic
- terminology preservation
- ambiguity detection
- escalation criteria for clarification

Target implementation:

- add `stdf-intent-router`
- add `stdf-clarifier`
- extend `.claude/skills/stdf/SKILL.md` to enforce canonical-engine routing

### Semantic QA and provenance

Rebuild fresh:

- `evaluator_system.txt`
- `citation_builder_system.txt`
- `trace_explain_system.txt`

Why:

- The new system already has stronger structural validation and hook support.
- What is missing is a native semantic review and provenance layer.

What to keep from the old system:

- semantic drift checks
- tool-grounding checks
- citation completeness expectations
- trace/provenance explanation expectations

Target implementation:

- add `stdf-semantic-reviewer`
- add `stdf-provenance-builder`
- add `stdf-trace-explainer`

### Report retrieval and product modules

Rebuild fresh:

- `report_knowledge_lookup_system.txt`
- `feedback_loop_subagent_system.txt`
- `value_investment_subagent_system.txt`
- `company_analysis_subagent_system.txt`
- `vca_company_subagent_system.txt`
- `stellar_subagent_system.txt`
- `web_search_subagent_system.txt`

Why:

- These are product/output modes, not core sector engines.
- They should be downstream modules on top of the new STDF pipeline.

What to keep from the old system:

- output mode definitions
- retrieval behavior
- business framing conventions
- question templates and expected deliverables

Target implementation:

- `stdf-report-lookup`
- `stdf-feedback-loop-analyst`
- `stdf-investment-synthesizer`
- `stdf-company-impact-analyst`
- `stdf-vca-analyst`
- `stdf-research-delta-finder`

## 2. Extract And Preserve As Canonical Logic

These are the actual capabilities. They should be preserved exactly in behavior even if the implementation is rewritten.

### Artificial labor

Extract and preserve:

- occupation/task/subtask taxonomy
- capability-gating rules
- cost-parity logic
- adoption ceilings
- replacement versus productivity split
- scenario configuration schema
- output semantics for FTE and productivity

Why:

- This is the model.
- Replacing it with generic cost/capability prompts would not be equivalent.

Target implementation:

- `stdf-agents/lib/sector/artificial_labor/`
- sector datasets and parameter files under versioned data paths
- regression fixtures against known old outputs

### Lithium and lead

Extract and preserve:

- segment dictionary
- OEM versus replacement logic
- base-case report-first behavior
- lead base plus TaaS dual-output policy
- B2C price-parity vs B2B cost-parity policy
- BESS exclusions and guardrails
- canonical driver mapping and calibration logic

Why:

- This is not just sector context; it is behaviorally significant model policy.

Target implementation:

- `stdf-agents/lib/sector/battery_demand/`
- report lookup index for base cases
- explicit output contracts for lead and lithium responses

### Copper

Extract and preserve:

- four-bucket decomposition
- transport demand logic
- generation demand logic
- T&D demand logic
- copper intensity coefficients
- residual balancing and reconciliation

Why:

- The four-bucket decomposition is the canonical structure of the model.

Target implementation:

- `stdf-agents/lib/sector/copper/`
- explicit reconciliation tests

## 3. Wrap Temporarily

These old assets should remain callable as temporary canonical backends while the new native engines are built.

### Wrap now

Wrap these immediately:

- `skills/.claude/skills/artificial-labor/run_forecast.py`
- `skills/.claude/skills/lithium-ion-demand/run_forecast.py`
- `skills/.claude/skills/copper-forecast/run_forecast.py`

Why:

- This prevents capability regression while migration is underway.
- It also gives you a parity oracle for testing the new native engines.

How to wrap:

- add a canonical-engine selector in the new orchestrator
- define one wrapper per legacy engine
- standardize wrapper output into new STDF file contracts

Recommended temporary wrapper behavior:

- user asks a sector question
- router identifies canonical engine requirement
- wrapper runs the old engine or retrieves the old report asset
- new STDF agents consume that result for synthesis, validation, and optional downstream outputs

### Wrap report assets too

Temporarily wrap:

- `stdf-agents/old_prompts/sector_reports/family1-labor-report.txt`
- `stdf-agents/old_prompts/sector_reports/family2-energy-report.txt`
- `stdf-agents/old_prompts/sector_reports/family3-lead-report.txt`

Why:

- Some old capabilities are not about recomputation. They are about fast, canonical answer retrieval.

Target implementation:

- `stdf-report-lookup` with an indexed map from query type to canonical report sections

## 4. Delete After Parity

These should be deleted only after the new system fully replaces them.

### Delete last

Delete only after parity and adoption:

- old sector prompt wrappers that duplicate new native sector agents
- old report lookup prompt logic once report retrieval is backed by a new index/service
- old evaluator prompt once semantic review is native and tested
- duplicate sector business rules embedded in prompt text
- any duplicated coefficients or taxonomies once they exist in a single new canonical source

### Never delete before these gates pass

Required gates:

- native engine reproduces old outputs on agreed benchmark scenarios
- new output schema is stable
- provenance and validation work end-to-end
- orchestrator consistently routes to the correct path
- user-facing answers are at least as complete as the old path

## Asset-by-asset recommendation

| Asset | Action | Notes |
| --- | --- | --- |
| `main_agent_system.txt` | Rebuild fresh | Preserve route policy, not wording |
| `planner_system.txt` | Rebuild fresh | Preserve skill-sovereignty and multi-skill planning rules |
| `reformulator_system.txt` | Rebuild fresh | Preserve intent normalization and routing hints |
| `clarification_system.txt` | Rebuild fresh | Preserve ambiguity thresholds |
| `evaluator_system.txt` | Rebuild fresh | Preserve semantic QA criteria |
| `citation_builder_system.txt` | Rebuild fresh | Preserve provenance contract |
| `trace_explain_system.txt` | Rebuild fresh | Preserve explainability contract |
| `report_knowledge_lookup_system.txt` | Rebuild fresh | Preserve retrieval behavior |
| `stdf_subagent_system.txt` | Do not migrate directly | New STDF agents already supersede it |
| `energy_sector_subagent_system.txt` | Do not migrate directly | New energy agents largely replace it |
| `artificial_labor_subagent_system.txt` | Extract logic, then rebuild | Preserve labor business logic |
| `lithium_ion_subagent_system.txt` | Extract logic, then rebuild | Preserve sector rules and report behavior |
| `copper_forecast_subagent_system.txt` | Extract logic, then rebuild | Preserve four-bucket structure |
| `feedback_loop_subagent_system.txt` | Rebuild fresh | Downstream business module |
| `value_investment_subagent_system.txt` | Rebuild fresh | Downstream business module |
| `company_analysis_subagent_system.txt` | Rebuild fresh | Downstream business module |
| `vca_company_subagent_system.txt` | Rebuild fresh | Downstream business module |
| `stellar_subagent_system.txt` | Rebuild fresh selectively | Only if still needed as a distinct mode |
| `web_search_subagent_system.txt` | Rebuild fresh selectively | Use current STDF search rules as base |
| `copper-forecast` skill | Wrap now, reimplement later | Canonical engine today |
| `artificial-labor` skill | Wrap now, reimplement later | Highest-priority canonical engine |
| `lithium-ion-demand` skill | Wrap now, reimplement later | Canonical engine with report assets |

## Build order

This is the recommended sequence.

### Phase 1: Protect correctness

Build first:

- canonical-engine routing in the new orchestrator
- temporary wrappers for the three legacy sector engines
- basic report lookup wrapper for existing canonical reports

Outcome:

- the new shell can operate safely without losing sector correctness

### Phase 2: Restore the missing operating system

Build next:

- `stdf-intent-router`
- `stdf-clarifier`
- `stdf-semantic-reviewer`
- `stdf-provenance-builder`
- `stdf-trace-explainer`

Outcome:

- the new system regains the missing meta-layer from the old stack

### Phase 3: Native sector engine migration

Build in this order:

1. artificial labor
2. lithium/lead
3. copper

Reason:

- artificial labor has the largest missing logic surface
- lithium/lead has both model depth and high-value report behavior
- copper is important but structurally simpler to port after the first two

### Phase 4: Downstream business modules

Build last:

- feedback loop
- investment
- company impact
- VCA

Outcome:

- business-facing outputs return without contaminating the core modeling layer

## Suggested file layout in the new system

### Agents

Add under `stdf-agents/.claude/agents/`:

- `stdf-intent-router.md`
- `stdf-clarifier.md`
- `stdf-semantic-reviewer.md`
- `stdf-provenance-builder.md`
- `stdf-trace-explainer.md`
- `stdf-report-lookup.md`
- `stdf-artificial-labor-modeler.md`
- `stdf-battery-demand-modeler.md`
- `stdf-copper-demand-modeler.md`

### Libraries

Add under `stdf-agents/lib/sector/`:

- `artificial_labor/`
- `battery_demand/`
- `copper/`

Each sector package should own:

- formulas
- coefficients
- taxonomy/schema definitions
- calibration helpers
- report formatting helpers

### Data and tests

Add:

- versioned sector parameter files
- benchmark scenarios
- parity fixtures against old outputs
- integration tests covering orchestrator routing

## What to treat as the source of truth during migration

Until parity exists:

- old sector engines are the truth for sector numbers
- old reports are the truth for standard base-case retrieval
- new orchestrator is the truth for workflow control
- new validation stack is the truth for guardrails

After parity exists:

- new sector packages become the truth
- old engines become removable

## Kill criteria for old paths

An old path should be deleted only when all of the following are true:

- there is a native new-system replacement
- benchmark outputs match or are accepted as intentionally improved
- validation coverage exists
- report/provenance behavior is preserved
- no active orchestrator path still depends on the old asset

## Bottom line

Rebuild the system architecture.

Do not rebuild the sector capabilities from memory.

For the sector engines, use the old system as a specification and temporary backend until the new native implementations have proven parity.
