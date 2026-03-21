---
name: Oil Market Disruption — Domain Analysis (March 2026)
description: Key data anchors and findings from the oil/petroleum market disruption analysis for reuse in future analyses
type: project
---

Analysis completed: March 2026. Sector: Energy. Sub-domains: transportation fuels (road), oil-fired power generation, building heating (oil boilers), petrochemical feedstocks.

Output written to: `output/oil-market-disruption/agents/01-domain-disruption.md`

**Key cost data anchors (from local catalog + web research, March 2026):**
- Brent crude oil price: $23.76/bbl (1990) → $96.94/bbl (2008 peak) → $41.96/bbl (2020) → $100.93/bbl (2022) → $80.33/bbl (2024) [T2: Database catalog]
- Utility-scale solar PV installed cost: $5,310/kW (2010) → $700/kW (2024); 87% decline [T2: Rethinkx]
- Solar PV LCOE: ~$49/MWh global weighted avg (2023); $29–$96/MWh range (2024) [T3: IRENA/Lazard]
- Oil-fired peaker LCOE: $110–$228/MWh (2024) [T3: Lazard]
- 2-hr BESS turnkey cost China: $205/kWh (2019) → $101/kWh (2024); 51% decline [T2: Rethinkx]
- Li-ion battery pack: ~$1,436/kWh (2010) → $115/kWh (2024); 92% decline [T2: Rethinkx]
- BEV global annual sales: 244,000 (2015) → 11,000,000 (2024); CAGR 52.7% [T2: Rethinkx]
- Oil-fired global power generation: 851,630 GWh (2006) → 616,500 GWh (2024); 28% decline [T2: Rethinkx]
- Solar PV global installed capacity: 41 GW (2010) → 1,865 GW (2024); 45x growth [T2: Rethinkx]
- Onshore wind global installed capacity: 178 GW (2010) → 1,053 GW (2024) [T2: Rethinkx]
- USA transportation oil demand: peaked 13.54 Mbpd (2007) → 12.24 Mbpd (2024); 9.6% structural decline [T2: Database]
- Global crude oil consumption: 70 Mbpd (1995) → 103.4 Mbpd (2024); still growing due to petrochemicals [T2: Database]

**Key adoption data anchors:**
- Global BEV fleet: ~39M vehicles (2024) vs. ~1.5B total fleet (~2.6% fleet share)
- China NEV share of new sales: ~50% (2025, BEV ~35%, PHEV ~15%)
- Solar power generation: 29 TWh (2010) → 2,131 TWh (2024); 73x in 14 years
- Heat pump global sales: ~7M units (2022), declined to ~6M (2024); China alone growing at 12–13%
- Heat pumps serve ~10% of global building heating need (2023)

**Key convergence labels:**
- SWB: Solar PV + Wind + BESS → 24/7 dispatchable electricity at $30–$80/MWh; displaces oil-fired peakers ($110–$228/MWh)
- SWB-EV: Solar + Wind + BESS + BEV charging → transportation system decoupled from petroleum
- ASHP-SWB: Air-source heat pump + rooftop solar PV + residential BESS → building heating decoupled from oil/gas
- SWB-EV-TaaS: Solar + Wind + BESS + BEV + autonomous mobility platforms → systemic oil demand destruction

**Chimeras confirmed:**
- PHEV: retains ICE drivetrain; structurally cannot reach BEV cost floor
- NGV (compressed natural gas vehicles): plateauing; losing to CEV cost curves
- Hybrid heat pump (ASHP + gas backup): retains gas infrastructure dependency
- Blue hydrogen heavy transport: requires fossil fuel feedstock + CCS; structural chimera

**S-curve positions:**
- BEV new car share: ~14–16% globally (2025); mid-growth; China at inflection
- Solar PV power generation: post-inflection globally; passing 40% of new capacity additions
- Oil-fired power generation disruption: near-complete in OECD; mid-stage in ME/Africa/SE Asia
- ASHP building heating: early-to-mid growth globally (~10% of heating need)
- Petrochemical oil demand: growing; not within 5-year disruption horizon

**Key supply-side instability finding:**
- Each oil price shock (2008, 2011–14 era, 2022) permanently reduces the baseline oil demand that recovers post-shock
- Supply instability amplifies cost-comparison advantage of disruptors and accelerates S-curve adoption timing
- Incumbent cartel managed supply cuts to hold $80–$90/bbl create conditions for disruptor cost advantage to widen

**Why:** These data points are frequently needed by downstream agents (cost-curve, tipping-point, adoption). Saves re-research time.

**How to apply:** When an Energy sector or oil/petroleum query arrives, check these anchors first before re-searching. Note data gaps: no local catalog data for heat pump cost curves, petrochemical feedstocks, maritime/aviation oil demand.
