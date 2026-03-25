# Copper Findings

## Executive summary

Copper is only partially represented in the new STDF system.

The new agent stack can model parts of the copper story through generic fleet, demand, regional, and commodity-style reasoning. That is useful, but it is not the same as the old canonical copper model. The old `copper-forecast` skill defines a specific decomposition and reconciliation framework that the new system does not yet reproduce explicitly.

Practical conclusion:

- Copper should not be considered fully migrated.
- The new system needs a first-class copper engine or a direct transitional invocation of the existing copper model.

## What the old copper skill contains

The old copper model is built around a canonical four-bucket decomposition:

- transportation
- grid generation
- grid transmission and distribution
- legacy residual demand

That matters because it avoids double counting and gives a disciplined explanation for where demand comes from.

Important business logic in the old skill includes:

- transport demand tied to regional powertrain mix and S-curve adoption
- differential-evolution S-curve fitting for EV-related transitions
- explicit copper intensity coefficients by powertrain and category
- special handling for PHEV and NGV shares
- grid generation demand by power technology build-out
- T&D demand linked to grid expansion and material intensity
- residual balancing to ensure totals reconcile

This is a genuine sector engine, not a formatting layer.

## What the new STDF system has today

The new STDF system provides useful generic components:

- demand decomposition
- fleet modeling
- regional demand analysis
- stream forecasting
- adoption and S-curve tools
- generic commodity-chain and downstream demand reasoning

These components can support copper analysis, but they do not presently enforce the old copper-specific decomposition or reconciliation rules.

## What is missing

### 1. Canonical four-bucket structure

The new system does not appear to require copper analysis to flow through:

- transportation
- grid generation
- grid T&D
- residual

That makes outputs harder to compare with legacy work and easier to drift.

### 2. Transport-specific coefficients and vehicle classes

The old model is explicit about vehicle-level or powertrain-level copper demand assumptions. The new system does not appear to encode that as first-class copper logic.

### 3. Residual balancing

Residual balancing is not optional bookkeeping. It is what keeps the copper model reconciled. The new system needs the same accounting discipline if it is going to replace the old skill.

### 4. Copper-specific output contract

The new generic outputs are not enough. Copper needs a standard output schema with:

- demand by bucket
- regional breakdowns
- technology contribution
- copper intensity assumptions
- residual/reconciliation checks

## Recommended target architecture

### Transitional step

Short term:

- Route copper questions that need canonical numbers through the existing `copper-forecast` engine.
- Use the new STDF system for framing, validation, synthesis, and cross-sector linkage.

### Long-term first-class engine

Build `stdf-agents/lib/sector/copper/` with modules such as:

- `transport.py`
- `generation.py`
- `td.py`
- `residual.py`
- `coefficients.py`
- `reconciliation.py`

Recommended sector agents:

- `stdf-copper-demand-modeler`
- `stdf-copper-transport-modeler`
- `stdf-copper-grid-modeler`
- `stdf-copper-synthesizer`

## What to port from the old system

Port these first:

- four-bucket decomposition contract
- copper intensity coefficient tables
- transport powertrain logic
- regional mapping and regional mix logic
- residual balancing logic
- standard intermediate-output tables for auditability

## What the new system can keep using

Keep using the new generic STDF components for:

- adoption and tipping logic
- regionalization framework
- S-curve support
- shared validation and provenance rules

The right design is not to duplicate those generic pieces inside a copper-specific prompt. The right design is to connect copper-specific sector math to the existing STDF platform.

## Validation requirements

The new copper path should have parity tests for:

- transport demand outputs
- generation-related copper demand
- T&D demand outputs
- regional totals
- grand-total reconciliation against the residual bucket

It should also assert that:

- totals match the sum of buckets
- coefficients used are versioned and explicit
- no bucket is silently omitted in user-facing reporting

## Recommendation

Copper should be migrated as a first-class sector engine inside the STDF platform. Until that happens, the old copper model remains the safer canonical source for production analysis.
