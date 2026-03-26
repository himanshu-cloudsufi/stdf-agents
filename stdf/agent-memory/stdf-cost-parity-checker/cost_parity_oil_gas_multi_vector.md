---
name: Cost Parity — Oil and Gas Demand Disruption (Multi-Vector)
description: Three-vector cost parity results for oil/gas demand disruption: EV vs ICE (MET 2020-2021), Solar+BESS vs NGCC (MET 2023-2024), Heat pump vs gas furnace (NOT_MET)
type: project
---

Oil and gas demand disruption — three simultaneous vectors, each with a different parity status.

**V1 — BEV vs ICE TCO ($/mile):**
- Status: MET — threshold 2020–2021, back-extrapolated from 2022 anchor (uncertainty ±1–2 yr)
- 2024: EV $0.319/mile vs ICE $0.850/mile (EV 62.5% below ICE)
- Confidence 0.65 — constrained by 3-pt back-extrapolation; battery pack fit R²=0.957 (10 pts)

**V2 — Solar PV + 4hr BESS vs NGCC LCOE ($/MWh):**
- Status: MET — threshold 2023–2024, confirmed by direct observed data
- 2024: $70.0/MWh combined vs $76.0/MWh NGCC (7.9% below)
- Confidence 0.82 — BESS R²=0.900 (6 pts) + observed 2024 crossover; solar full-series R²=0.756 flagged
- Solar alone crossed NGCC in 2016; combined threshold is the binding determination for dispatchable capacity

**V3 — Air source heat pump vs gas furnace ($/kWh thermal):**
- Status: NOT_MET — no threshold on any forward cost curve under US average energy prices
- 2024: HP $0.0776/kWh_th vs gas $0.0391/kWh_th (HP 98.5% more expensive, ratio 1.985×)
- Break-even electricity: $0.088/kWh vs actual $0.176/kWh (2× gap); HP installed costs rising +89% since 2010
- Confidence 0.60 — T3 data only, no learning curve, cost direction inverted

**Multi-vector aggregate confidence: 0.69**

**Why:** The V2 threshold is margin-thin (7.9% gap). Any significant fall in Henry Hub gas prices could temporarily reverse it. Downstream S-curve modeling should treat V2 MET as a recent and fragile crossing, not a deeply established one.

**How to apply:** When evaluating multi-vector disruptions, one NOT_MET vector does not invalidate MET vectors — each vector feeds its own S-curve adoption model. The tipping synthesizer must handle partial-vector conditions.
