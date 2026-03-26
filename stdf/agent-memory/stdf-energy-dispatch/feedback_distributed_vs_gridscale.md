---
name: Distributed vs Grid-Scale Dispatch Adaptation
description: When the analysis target is distributed/on-site generation, the 9-step pipeline must be adapted — the merit order is the on-site stack, not regional coal/gas
type: feedback
---

The standard 9-step SWB merit order pipeline models coal/gas displacement across a national/regional grid. When the query concerns distributed on-site power generation (e.g., Bloom Energy SOFC, diesel generators, CHP), the pipeline must adapt:

1. Unit of analysis shifts from national GWh to site-level MWh (e.g., 1 MW data center = 8,760 MWh/yr)
2. The merit order stack changes from coal/gas/SWB to: Solar ($0/MWh) → BESS (SCOE cycling cost, $5–14/MWh) → On-site gas (SOFC/CHP marginal, $23–48/MWh) → Grid ($80–120/MWh C&I) → Diesel backup ($200–300/MWh)
3. The key variable becomes BESS duration (hours), not SWB capacity share — because duration determines what fraction of 24/7 load SWB can serve without gas backup
4. The "non-SWB baseline" (Step 3 in standard pipeline) = grid backup + diesel, NOT hydro/nuclear
5. Energy balance still validates at site level: SWB + gas incumbent + grid backup = total site demand

**Why:** The Bloom Energy SOFC analysis (2026-03-25 run) had this exact adaptation requirement. The standard grid pipeline would have produced meaningless national coal/gas displacement numbers instead of the actionable on-site dispatch model the user needed.

**How to apply:** At the start of any energy dispatch run, check whether the incumbent is a distributed/on-site generator (fuel cell, diesel, CHP, reciprocating engine). If yes, switch to site-level dispatch stack and focus on BESS duration coverage fractions.
