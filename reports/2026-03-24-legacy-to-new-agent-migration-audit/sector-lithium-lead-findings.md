# Lithium and Lead Findings

## Executive summary

Lithium and lead are partially migrated in the new STDF system, but the migration is incomplete.

The new system has enough generic demand, tipping, and regional analysis capability to handle parts of the battery demand problem. It also appears to have absorbed some lead-specific thinking into agent memory and generic downstream-demand logic. Even so, the old `lithium-ion-demand` skill contains a much richer and more operationally specific sector model.

Practical conclusion:

- Lithium/lead should be treated as a partially migrated sector, not a completed migration.
- The new STDF platform needs an explicit battery demand engine with separate lithium-ion and lead business rules.
- The old report-first behavior should be preserved for standard base-case questions.

## What the old lithium-ion-demand skill contains

The old skill is broader than the name suggests. It covers:

- lithium-ion demand
- lead-acid demand
- TaaS overlays
- automotive and non-automotive segments
- replacement and OEM pathways
- base-case reporting using precomputed assets

Important business logic includes:

- base-case answers should come from the canonical report when possible
- lead queries should show both base-case and TaaS-case views
- B2C segments should be framed around price parity
- B2B segments should be framed around cost parity
- BESS should not be modeled with LCOE/SCOE shortcuts
- segment coverage includes passenger, commercial, 2W, 3W, forklift, BESS, telecom UPS, data center UPS, 12V auxiliary, SLI, VRLA, LAB, and related demand trees

The old lead reporting also contains explicit driver mapping and calibration conventions that make the outputs reproducible.

## What the new STDF system has today

The new system has solid generic pieces for this domain:

- cost, tipping, adoption, and S-curve logic
- fleet and demand modeling
- stream forecasting
- regional demand analysis
- commodity-oriented decomposition

It also appears to have some meaningful lead-specific domain memory and prior analysis patterns.

That is a good base, but it is not yet the same thing as a canonical battery-demand engine.

## What is missing

### 1. Report-first retrieval

The old skill knows when not to recompute. For standard base-case questions, it can answer from a canonical precomputed report.

The new system does not appear to have an equivalent first-class report lookup layer.

### 2. Explicit lead query policy

The old system had important user-facing rules, especially:

- show base plus TaaS views for lead queries
- preserve segment logic rather than collapsing to a single top-line number

These should exist as deterministic policy, not as optional stylistic behavior.

### 3. Segment-specific business logic

The old battery skill contains hard-won sector logic for:

- OEM versus replacement pathways
- starter battery versus auxiliary battery logic
- non-automotive industrial and stationary segments
- chemistry and use-case distinctions

The new system can reason about these domains, but it does not appear to encode them as a documented first-class engine.

### 4. Explicit parity policy

The old distinction between:

- B2C price parity
- B2B cost parity

is important and should remain part of the canonical model. The new generic parity framework does not appear to enforce this sector-specific policy.

## Recommended target architecture

### Transitional step

Short term:

- Continue using the old `lithium-ion-demand` engine or its precomputed report assets as the canonical source for base cases and sector-standard queries.
- Let the new STDF system handle cross-sector synthesis, extensions, and validation around that output.

### Long-term first-class engine

Build `stdf-agents/lib/sector/battery_demand/` with submodules such as:

- `liion_segments.py`
- `lead_segments.py`
- `taas_overlay.py`
- `oem_replacement.py`
- `parity_policy.py`
- `report_lookup.py`
- `reporting.py`

Recommended agents:

- `stdf-battery-demand-modeler`
- `stdf-lead-demand-modeler`
- `stdf-battery-report-lookup`
- `stdf-battery-synthesizer`

## What to port from the old system

Port these first:

- report-first base-case workflow
- lead base plus TaaS output contract
- OEM/replacement split logic
- segment dictionary and demand tree
- B2C versus B2B parity policy
- BESS modeling exclusions and guardrails
- driver mapping and calibration conventions for lead reporting

## What the new system can already support well

The new system is already a good host for:

- adoption and parity mechanics
- regional tipping views
- demand decomposition and stream forecasting
- cross-sector synthesis involving transport, energy, and stationary storage

That means the migration here is not a restart. It is a codification problem.

## Validation requirements

The new battery path should have parity tests for:

- lithium-ion base cases
- lead base-case demand
- lead TaaS overlay outputs
- OEM versus replacement splits
- key segment subtotals
- region-specific parity milestones where they are canonical

It should also validate that:

- lead answers always include the required dual-view when applicable
- BESS outputs do not use prohibited parity shortcuts
- user-facing summaries can trace back to the underlying segment tables

## Recommendation

Lithium and lead should be formalized as an explicit sector engine in the new STDF platform. The old battery skill still contains too much sector logic and too much report productization to be retired safely.
