---
name: Oil and Gas Demand — Multi-Vector Disruption Analysis (March 2026)
description: Key data anchors for three-vector oil/gas disruption analysis: transport BEV, gas power generation SWB, and gas heating ASHP
type: project
---

Analysis completed: March 2026. Output: `output/oil-gas-outlook/agents/01-domain-disruption.md`

Sector: Energy (primary) + Transportation (co-primary for Vector 1)
Sub-domains: road transport petroleum (passenger + commercial), gas CCGT/OCGT power generation, gas residential/commercial heating

**Why:** Multi-vector oil/gas query requiring decomposition across three structurally distinct disruption dynamics. Prior memory (`analysis_oil_market_disruption.md`) covers similar ground but at higher abstraction; this adds computed learning rates and precise vector-level decomposition.

**How to apply:** When a query asks about oil demand, gas demand, or energy commodity disruption with transport + power + heating scope, use these data anchors. Note: petrochemical feedstocks and aviation/marine fuels are explicitly excluded from scope.

---

## Vector 1 Key Data: BEV disruption of petroleum road transport

- BEV global annual sales: 244,000 (2015) → 11,000,000 (2024); CAGR 52.7% [T2: Rethinkx]
- BEV new car market share 2024: ~12.9% globally; China ~35% BEV; Europe ~15%; USA ~8%
- PHEV China 2024: 4.9M sales = 41.2% of China NEV market — confirmed chimera
- Li-ion battery pack: $1,436/kWh (2010) → $115/kWh (2024); annual decay 18.4%, R²=0.954; per-doubling learning rate ~17.7%
- Cumulative BEV fleet (2010–2024 sales): ~39.6M units; fleet share ~2.6% of 1.5B total
- USA transport petroleum: peaked 13.54 Mbpd (2007) → 12.24 Mbpd (2024); −9.6%
- Disruption type: From Above; S-curve position: Growth phase globally

## Vector 2 Key Data: Solar PV + BESS disruption of gas power generation

- Solar PV installed capacity: 41 GW (2010) → 1,865 GW (2024); 45× growth, CAGR 31.3%
- Solar PV installed cost: $5,310/kW (2010) → $700/kW (2024); −87%; annual decay 14.6%, R²=0.986; learning rate per doubling 30.8%
- BESS installed global: 193 MWh (2010) → 370,112 MWh (2024); 1,918× growth, CAGR 71.6%
- 2-hr BESS turnkey cost: $441/kWh (2019) → $269/kWh (2024); −39%; annual decay 8.7%, R²=0.873 (weak fit — note in data gaps)
- Gas power gen: peaked 6.31 TWh×10³ (2022) → 6.28 TWh×10³ (2024); first post-peak signal
- Gas installed capacity still growing: 1,403 GW (2010) → 1,958 GW (2024), but utilization falling (implied CF ~36.7%)
- LCOE comparison: Solar PV $25–49/MWh (2024); CCGT at EU gas ($10.89/MMBtu) = $101–111/MWh; CCGT at US gas ($2.19/MMBtu) = $40–50/MWh
- Convergence: SWB (solar + wind + BESS) — named convergence label
- Disruption type: Systemic; S-curve position: Solar post-inflection; gas generation in early-erosion phase

## Vector 3 Key Data: ASHP disruption of gas heating

- NO catalog heat pump cost or adoption curve — data gap for cost-fitter agent
- Gas heating estimated at ~1,067 BCM/yr (26% of 4,103 BCM total, 2023)
- US residential gas: ~$2.19/MMBtu wholesale, ~$14/MMBtu delivered residential
- EU gas: $10.89/MMBtu (2024); peaked $37.52/MMBtu (2022)
- ASHP operating economics (computed, model-derived):
  - US retail prices: HP $0.037/kWh-heat vs gas $0.053/kWh-heat → HP 30% cheaper on opex
  - EU retail prices: HP $0.086/kWh-heat vs gas $0.111/kWh-heat → HP 23% cheaper on opex
  - Barrier: ASHP capex $8–20k vs gas furnace $2–5k; payback 7–37 years depending on market
- Hybrid heat pump (ASHP + gas backup): confirmed chimera — retains gas infrastructure
- Disruption type: From Below; S-curve position: Early growth (~10% of global heating served, 2023)
- Key dynamic: 15–20yr replacement cycle constrains disruption velocity; peak gas heating demand unlikely before 2032–2037

## Systemic Convergence

- SWB: Solar PV + Wind + BESS → 24/7 dispatchable electricity disrupting CCGT/OCGT
- SWB-EV: SWB + BEV charging → transport-energy decoupling from petroleum
- ASHP-SWB: ASHP + rooftop solar + residential BESS → building heat decoupled from gas
- SWB-EV-ASHP: Full systemic convergence — all four household energy services decoupled from fossil incumbents simultaneously

## Gas Demand Context

- Global gas consumption 2023: 4,103 BCM (EIA). Power ~36% (1,477 BCM), heating ~26% (1,067 BCM), industrial ~38% (1,559 BCM)
- Gas consumption CAGR 2000–2023: 2.2%; slowing to near-zero post-2021
- Power sector gas has peaked (2022); heating and industrial gas still growing
