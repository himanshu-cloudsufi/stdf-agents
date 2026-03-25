# Energy Findings

## Executive summary

Energy is the strongest migrated sector in the new STDF system.

Compared with copper, artificial labor, and lithium/lead, the new `.claude` STDF agents already cover a much larger share of the energy workflow natively. The dedicated energy-dispatch and gas-supply decomposition agents align well with the old energy-sector prompt logic and with STDF-style analysis of multi-vector disruption.

Practical conclusion:

- Energy can mostly live natively in the new STDF platform.
- The remaining work is less about porting a hidden sector engine and more about improving productization, retrieval, calibration assets, and scenario packaging.

## What the old energy layer contributed

The old system had:

- an energy-sector subagent prompt
- sector reports for energy-family analysis
- business-facing narrative framing around dispatch, demand growth, and regional disruption

The old energy layer was useful, but it was not the same kind of deterministic standalone engine that existed for artificial labor, copper, or lithium/lead.

That matters because it means migration risk is lower here.

## What the new STDF system has today

The new system already has first-class support for the core energy problem:

- demand decomposition
- stream forecasting
- energy dispatch
- gas-supply decomposition
- regional demand analysis
- cost and tipping analysis for relevant technologies

This aligns well with the kind of questions the old energy prompt system was answering:

- dispatch shifts
- coal/gas displacement
- power-demand additions from EVs, data centers, and heat pumps
- regional demand balances
- multi-vector disruption pathways

## What is still missing

### 1. Report retrieval and standard answer modes

The new system should still add:

- report lookup for standard sector questions
- canonical packaged answer templates for recurring energy queries

### 2. Calibration asset management

Energy analysis often depends on regional calibration assets:

- generation mix
- dispatch stack assumptions
- fuel costs
- capacity factors
- curtailment assumptions

The new platform should make these versioned and easily inspectable.

### 3. Scenario packaging

The old system was relatively good at turning a model into a narrative business output. The new system should preserve that by adding energy-oriented scenario packages and report templates.

### 4. Downstream business modules

Energy is also a prime input into:

- commodity views
- value-chain views
- investment implications
- company impacts

Those extensions are not yet first-class in the new system.

## Recommended target architecture

Energy should be treated differently from the other sectors in this audit:

- keep the new native STDF agents as the primary engine
- add better calibration data management
- add report lookup and scenario templates
- add downstream business-output modules where needed

Suggested supporting additions:

- `stdf-energy-report-lookup`
- `stdf-energy-scenario-packager`
- `stdf-energy-company-impact`

## What to keep from the old system

Keep these ideas:

- standard sector-report packaging
- recurring question templates
- business-facing narrative structures for dispatch and demand balance

Do not over-preserve old energy prompt logic where the new STDF agents already have a cleaner implementation.

## Validation requirements

Energy validation should focus on:

- dispatch balance consistency
- fuel displacement accounting
- reconciliation between power demand additions and generation response
- region-specific calibration sanity
- scenario reproducibility

## Recommendation

Energy is the sector where the new STDF platform is already closest to the desired end state. It should be used as the template for how a mature native-STDF sector should look, while still adding report retrieval and better packaging on top.
