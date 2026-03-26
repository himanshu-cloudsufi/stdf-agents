---
name: Oil/Gas Multi-Vector S-Curve Parameters
description: Fitted S-curve parameters for three oil/gas disruption vectors (EV, solar, heat pump); key data sources and metrics chosen
type: project
---

Fitted 2026-03-20 for the oil-gas pipeline run.

**V1: EV all-types share of new passenger car sales (global)**
- Data: Rethinkx catalog, 2010-2024, 15 pts
- L=90 (fixed; free-L returned implausible 34.4), k=0.4281, x0=2026.3, R2=0.9902
- 2024 share: 23.89% (rapid_growth phase)
- BEV-only supplementary: L=85, k=0.3836, x0=2027.8, R2=0.9736 (2012-2024, 13 pts)
- 80% absolute share year: 2031.1

**V2: Solar PV share of global electricity generation**
- Data: Rethinkx catalog (solar GWh) + BP Statistical Review (total TWh), 2010-2024, 15 pts
- Metric chosen: generation share (not capacity additions -- capacity additions series has a kink; free-L diverged to L=8.9M on that series)
- L=45 (fixed; free-L gave 30.77 which understimates given established cost superiority), k=0.2279, x0=2031.6, R2=0.9965
- 2024 share: 6.92% (tipping phase)
- Solar matches current gas generation share (~22.4%) at: 2031.5

**V3: Heat pump share of new heating installations (Europe)**
- Data: EHPA annual statistics, 2013-2023, 11 pts
- Free-L converged (not a divergence case) to L=79.13, k=0.1393, x0=2028.9, R2=0.9987
- 2023 EU share: 24.0% (rapid_growth); global stock: ~10% (tipping)
- EU inflection at 2028.9 -- acceleration not yet arrived even in leading market

**Key upstream discrepancy noted:**
Tipping synthesizer (04d) used L=85, k=0.30, x0=2027.5 for V2 (capacity additions metric).
Our L=45, x0=2031.6 uses generation share -- correct for demand displacement.
These are not conflicting; they measure different things.

**Why:** Recorded for future oil/gas or energy disruption runs -- generation share is always the correct V2 metric, not capacity additions.

**How to apply:** When fitting solar adoption for power generation disruption, always use solar generation share / total electricity generation as the adoption metric. The capacity additions series has a structural kink (2023 saw an anomalous jump) that breaks S-curve fitting.
