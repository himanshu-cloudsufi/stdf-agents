---
name: analysis_bev_trucks_china
description: Transportation sector — BEV heavy trucks displacing LNG/CNG and diesel trucks in China (March 2026)
type: project
---

Analysis of BEV-HDT disruption of LNG/CNG and diesel incumbent heavy trucks in China's heavy-duty truck market (~900k units/yr).

**Key findings:**
- Sector: Transportation; sub-domains: heavy-duty long-haul freight, regional distribution, captive fleet logistics
- Primary disruptors: LFP-battery BEV tractor-trailers, battery-swap BEV HDTs
- Primary incumbents: LNG-fueled tractor-trailers, CNG-fueled trucks, diesel ICE HDTs
- Central chimera: LNG/CNG heavy trucks — achieved ~29% market share in 2024 but structurally dependent on fossil gas supply chain and volatile pricing; cannot replicate BEV cost-curve dynamics
- Convergence label: BSAF = Battery-Swap + Autonomous driving + Fleet-management software
- Secondary convergence: LFP-Grid = LFP battery scale + solar PV/wind grid electricity

**Key data points (observed):**
- BEV-HDT China market share: 9.2% full-year 2024; 20.9% December 2024; 22% H1 2025; >50% December 2025
- BEV-HDT two-year CAGR (2022-2024): 174% (11k → 82.5k units)
- LFP commercial pack cost: $177/kWh (2018) → $90/kWh (2024); 10.7%/yr decline, R²=0.803 [Rethinkx catalog]
- BEV vs diesel TCO advantage: ~CNY 100/100km = ~USD 14,000/yr at 100k km/yr
- LNG-diesel price differential collapsed ~two-thirds by May 2025 vs 2024 peak

**Data scope note:**
Rethinkx catalog shows 40,446 heavy-duty NGV sales in China (2024) — this is a narrower scope than ICCT/WoodMac figures (~261,000 LNG HDTs in 2024). Both cited with scope flags. This discrepancy should be flagged to cost-fitter and demand-decomposer agents.

**Output file:** output/bev-trucks-china/agents/01-domain-disruption.md

**Why:** User requested China-specific HDT analysis focused on tri-incumbent structure (diesel + LNG chimera + BEV disruptor).
**How to apply:** If downstream agents run on this topic, the data-scope discrepancy for NGV figures is the key gap to resolve. BSAF convergence is the dominant emergent capability to model.
