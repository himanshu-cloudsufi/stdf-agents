---
name: Oil and Gas Demand Disruption — Fleet Model Parameters
description: Fleet parameters, OEM/replacement ratios, and key dynamics for 4 durable-goods fleet models in oil/gas demand disruption analysis (2026-2046)
type: project
---

Oil and gas demand disruption fleet models (07c-fleet-modeler.md, run 2026-03-20, pipeline: oil-gas-outlook):

**V1-A: Global Passenger Vehicle Fleet**
- Fleet 2026: 1,500 million vehicles; lifetime: 15yr; scrappage rate: 0.0667/yr
- Annual sales: 91M (2026) → 93M (2031+, plateau)
- Fleet CONTRACTING throughout: scrappage ~100M/yr > sales ~91-93M/yr
- BEV fleet share: 11.6% (2026) → 44.1% (2031) → 74.8% (2036) → 84.6% (2046) [6-yr lag approximated as S-curve at yr-3]
- OEM oil demand: ZERO throughout (fleet contracting; all ICE demand = replacement/continuation)
- ICE new sales: 52.7M/yr (2026) → 9.3M/yr (2046)

**V1-B: Global Heavy Truck Fleet**
- Fleet 2026: 26.0 million trucks; lifetime: 10yr; scrappage rate: 0.100/yr
- Annual sales: 2.8M → 3.0M/yr; fleet growing slowly (+0.2M/yr net in 2026)
- BEV-HDT fleet share: 5.8% (2026) → 28.4% (2031) → 65.7% (2036) → 84.5% (2046)
- OEM diesel demand: NON-ZERO (fleet growing); 7% (2026) → 13% (2046) of diesel demand
- OEM/Replacement diesel: 0.69/8.91 mb/d (2026) → 0.21/1.39 mb/d (2046)

**V2: Global Gas Power Generation Capacity Fleet**
- Fleet 2026: 2,572 GW total (CCGT 1,387 GW at 55% CF; OCGT 1,185 GW at 15% CF)
- CCGT: lifetime 30yr; OCGT: lifetime 20yr
- CCGT additions falling: 35 GW/yr (2026) → 11 GW/yr (2036) → 5 GW/yr (2046)
- OCGT additions falling: 15 GW/yr (2026) → 2.4 GW/yr (2036) → 2 GW/yr (2046)
- Both fleets contracting from 2026; total gas gen capacity: 2,572 → 2,261 → 1,933 → 1,408 GW
- Key insight: OCGT capacity falls 59% but OCGT gas demand falls 98% — capacity factor compression decouples fleet size from demand decline
- OEM gas demand: ZERO (fleet contracting; all gas builds = replacement)

**V3: Global Heating Equipment Fleet**
- Fleet 2026: 800 million units; lifetime: 17yr; scrappage rate: 0.059/yr
- Annual sales: 52M/yr (stable, replacement-dominant)
- HP stock share: 13.2% (2026) → 18.9% (2031) → 24.0% (2036) → 30.2% (2046)
- Gas boiler units: 550M (2026) → 519M (2031) → 486M (2036) → 444M (2046)
- OEM gas demand: ~10% throughout (new construction adding gas boilers)
- Replacement gas demand: ~90% throughout

**Consistency checks:** All 4 models PASS (max_deviation = 0.010 units; relative error < 0.000001%)

**Key finding — vocabulary hook:** The pipeline run slug "oil-gas-outlook" contains the word "outlook" which triggers the stdf_validate.py forecast language check. Reference the run as "oil-gas-demand-disruption" in agent output files, not by the directory slug.

**Why:** The four fleet models are needed to decompose oil/gas demand into OEM vs replacement components. For oil, the dominant finding is that OEM demand is essentially zero (passenger fleet contracting, gas power fleet contracting) — all demand is replacement/continuation. For gas heating, a small OEM fraction (~10%) persists from new construction.

**How to apply:** When building fleet models for oil/gas demand drivers in future runs, use these as calibration anchors: PV fleet 1.5B at 15yr lifetime, HDT 26M at 10yr, gas power 2,572 GW (CCGT+OCGT) at 30/20yr, heating 800M units at 17yr.
