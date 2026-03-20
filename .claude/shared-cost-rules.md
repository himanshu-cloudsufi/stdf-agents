# STDF Cost Analysis Rules

**Read by all cost-chain agents** (cost-researcher, cost-fitter, cost-parity-checker, tipping-synthesizer, demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst, synthesizer).

---

## Rule 1: No TCO Aggregation

Never aggregate costs into a single TCO (Total Cost of Ownership) figure. Present a disaggregated cost stack with each component as a separate item:

- **Purchase price** (per vehicle, per unit, per kW, etc.)
- **Energy cost per unit of service** (per km, per kWh delivered, etc.)
- **Maintenance cost per unit of service** — only if sourced; if unsourced, list in Data Gaps
- **Consumable replacement** (battery mid-life replacement, etc.) — only if sourced

Unsourced cost components MUST be dropped from the analysis and noted in the Data Gaps section. Never estimate or assume a cost component.

## Rule 2: Cost Parity Metric

The cost metric used for parity comparison is specified by the `/stdf` skill classification step (from domain-disruption handoff context).

Default hierarchy when no classification is available:
1. **Purchase price** (most directly observable, least assumption-laden)
2. **Dominant operating cost** (energy cost per unit of service)
3. **Service-level unit cost** (cost per km, cost per kWh delivered)

Never select the parity metric ad hoc — always trace it to the domain-disruption classification or use the default hierarchy.

## Rule 3: Market Type Classification

The market type determines which cost component dominates purchase decisions:

| Market Type | Dominant Cost Component | Example |
|------------|------------------------|---------|
| **Consumer** | Purchase price (upfront cost sensitivity) | Passenger cars, home solar |
| **Fleet** | Total operating cost per unit of service | Trucking, ride-hailing, bus fleets |
| **Enterprise** | Service-level unit cost + reliability | Data centers, industrial equipment |
| **Utility** | Levelized cost per unit of output (LCOE, LCOS) | Grid-scale generation, storage |

The market type is classified in the domain-disruption handoff context. Downstream agents use this to weight cost components appropriately.

## Rule 4: No Scenario Labels

Never use scenario labels in cost analysis or any STDF output:

**Banned:** "base case", "bull case", "bear case", "optimistic scenario", "pessimistic scenario", "best case", "worst case", "conservative scenario", "aggressive scenario"

**Instead:** Label by parameter values. Example:
- "L=85% (primary), L=90% (sensitivity)" — not "conservative" / "optimistic"
- "Learning rate r=0.10 (range: 0.08–0.12)" — not "base case (range: bear–bull)"
