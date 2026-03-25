# Artificial Labor Findings

## Executive summary

Artificial labor is the most under-migrated sector in the new STDF system.

The old `artificial-labor` skill is not just a themed prompt. It is a bottom-up simulation framework with a real domain model. The new STDF agent family has enough generic primitives to support labor analysis conceptually, but it does not currently encode the labor-specific machinery that makes the old results credible.

Practical conclusion:

- Do not retire the old artificial-labor model yet.
- Add a first-class artificial-labor engine to the new STDF platform.
- Until that port is complete, the new orchestrator should directly treat the existing labor model as canonical for labor questions.

## What the old artificial-labor skill contains

The old skill encodes a specific business model for AI-driven labor displacement and productivity:

- bottom-up modeling across occupations, tasks, and subtasks
- a large occupation/task/subtask dataset
- capability gating tied to task-time thresholds and model performance
- cost-parity tipping logic
- post-tipping adoption curves
- replacement versus productivity split
- sector or occupation-specific adoption ceilings
- scenario controls and parameter overrides
- output discipline around FTE displacement and productivity, not simplistic unemployment claims

This is a materially richer model than generic STDF reasoning about cost and capability.

## What the new STDF system has today

The new system has some reusable pieces that are useful for labor:

- capability analysis
- cost research and fitting
- capability parity and cost parity checks
- adoption readiness
- tipping synthesis
- S-curve support

It also appears to have some labor/robotics-related source memory and terminology coverage.

That is not enough to replace the old labor engine.

## What is missing

### 1. Labor taxonomy

There is no visible first-class equivalent of:

- occupation-to-task mappings
- task-to-subtask decomposition
- task duration distributions
- wage or loaded compensation mapping at task/occupation level

Without this, labor analysis stays qualitative or overly aggregated.

### 2. Labor-specific capability gating

The old model appears to evaluate whether a given AI system can handle a task based on task duration and capability thresholds. That is much more specific than a generic "capability parity" narrative.

The new STDF system does not appear to expose this as a labor-specific coded rule set.

### 3. Replacement versus productivity split

This is a central labor business rule. The old model distinguishes:

- direct labor replacement
- productivity augmentation

The new STDF system does not appear to encode this distinction as a canonical output contract.

### 4. Adoption ceilings and sector controls

Labor adoption is not a simple global S-curve. The old system has ceilings and scenario controls. Those are not currently first-class in the new STDF labor path.

### 5. Output semantics

Labor outputs need to stay disciplined:

- FTE affected
- task share automated
- productivity gain
- sector/occupation attribution

The new system risks collapsing these into broader disruption language.

## Recommended target architecture

### Transitional step

Short term:

- Route labor questions to the old `artificial-labor` engine as the canonical computational backend.
- Let the new STDF orchestrator wrap around that output for synthesis, validation, and cross-sector framing.

This should be treated as transitional, not the long-term end state.

### Long-term first-class engine

Build `stdf-agents/lib/sector/artificial_labor/` with modules such as:

- `taxonomy.py`
- `capability_gate.py`
- `labor_costs.py`
- `adoption.py`
- `impact_split.py`
- `scenario.py`
- `reporting.py`

Expected owned business logic:

- occupation/task/subtask hierarchy
- capability thresholds
- labor cost assumptions and loaded-cost transformations
- parity/tipping rules
- replacement/productivity allocation
- adoption ceilings and scenario modifiers

### Recommended new agents

- `stdf-artificial-labor-modeler`
- `stdf-artificial-labor-impact-synthesizer`
- `stdf-artificial-labor-reporter`

The modeler should compute. The synthesizer should interpret. The reporter should package outputs for user-facing results.

## What to port from the old system

Port these first:

- canonical dataset structure
- scenario config schema
- capability-gating logic
- replacement/productivity split logic
- output schema for monthly or yearly FTE results
- explicit instruction that results represent automation potential and labor impact, not direct unemployment forecasts

## What not to do

Do not answer artificial-labor questions with only:

- generic cost-parity analysis
- generic capability parity analysis
- generic adoption curves

Those are components, not the labor model.

## Validation requirements

The new labor path should have regression tests that prove parity against known legacy outputs for:

- base case
- aggressive and conservative scenarios
- occupation-group slices
- productivity-only and replacement-heavy mixes

It should also validate that:

- totals reconcile to occupational components
- productivity and replacement shares sum correctly
- no unsupported unemployment claims are emitted

## Recommendation

Artificial labor should be treated as a dedicated migration program, not as a small extension to the generic STDF flow. This is the highest-priority sector gap in the new system.
