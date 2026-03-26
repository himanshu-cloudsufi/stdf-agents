---
name: Bloom Energy SOFC vs SWB catalog coverage
description: Catalog coverage for Bloom Energy SOFC disruption by solar+wind+battery; key curve paths, T3 sources for SOFC cost data, unit conversion requirements, EIA caution tag patterns
type: reference
---

## Disruption: Bloom Energy SOFC (incumbent) vs. SWB (disruptor)
Analysis date: 2026-03-25
Output: output/bloom-energy-sofc-disruption/agents/02a-cost-researcher.md

## Catalog Coverage (T2 — all Rethinkx)

### Disruptor (SWB) — Strong catalog coverage
- `data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_USA.json` — $/kW, 2010–2024, 15 pts
- `data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json` — $/kW, 2010–2024, 15 pts
- `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Stationary_Storage_Cost_Global.json` — $/kWh, 2010–2024, 15 pts
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — $/kWh, 2010–2024, 15 pts
- `data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json` — $/kWh, 2019–2024, 6 pts
- `data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_USA.json` — $/kWh, 2019–2024, 6 pts (NOTE: USA series has 2021–2022 spike; global series is monotone)
- `data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` — $/kWh, 2019–2024, 6 pts
- `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — %, 2010–2024

### Incumbent (SOFC/Natural Gas) — Partial catalog coverage
- `data/natural_gas/cost/Natural_Gas_Price_USA.json` — $/MMBtu, 1997–2024, 28 pts [CAUTION: EIA source — historical data only]
- NO SOFC/fuel cell installed cost curves in catalog — must use T3 web sources

## T3 Sources for SOFC Capital Cost

| Year | Cost ($/kW) | Source |
|------|-------------|--------|
| 2008–2009 | ~9,500–9,900 | Hindenburg Research (2019): https://hindenburgresearch.com/bloom-energy-a-clean-energy-darling-wilting-to-its-demise/ |
| 2010 | ~7,000–8,000 | Wikipedia + Hindenburg |
| 2015 | ~4,500–6,000 | DOE expert elicitation / ScienceDirect 2021: https://www.sciencedirect.com/science/article/abs/pii/S0306261921010084 |
| 2020 | ~2,400–3,500 | Same ScienceDirect source (23-expert elicitation, median $2,400/kW) |
| 2022 | ~3,000–4,000 | Wikipedia synthesis |
| 2024 | ~3,000–4,000 | SemiAnalysis / analyst sources |

## Unit Conversion Requirements

- Solar PV catalog data is in $/kW installed — needs CF + CRF to convert to $/kWh LCOE
- Battery catalog data is in $/kWh storage capacity — needs cycle assumptions + sizing ratio
- SOFC LCOE must be constructed: Capital component + Fuel component + O&M
  - CF = ~97% (on-site baseload)
  - Efficiency = 58% (Bloom SOFC electrical efficiency)
  - CRF = 10% (20-year life)
  - O&M = $0.024/kWh (observed from T3 sources)
  - Fuel = NG_price / (0.58 * 293.07 kWh/MMBtu)

## SOFC LCOE Model-Derived Results (2024 USD)
At 2024 Henry Hub price ($2.19/MMBtu):
- Capital: $0.041/kWh
- Fuel: $0.013/kWh
- O&M: $0.024/kWh
- Total: ~$0.078/kWh

At 2022 Henry Hub spike ($6.45/MMBtu): LCOE rises to ~$0.103/kWh

## C&I Commercial Solar Benchmark (NREL T3)
- 2022: $1.99/Wdc; 2023: $1.78/Wdc (200 kW rooftop)
- Utility-scale catalog is ~1.5x cheaper (lower soft costs)
- For distributed gen comparison, use NREL commercial benchmark NOT catalog utility-scale

## Key Data Gaps
1. No Bloom 10-K production cost/watt data — SEC EDGAR returned 403 errors
2. Lazard discontinued distributed generation section after 2019 (no recent fuel cell LCOE series)
3. BESS turnkey data starts 2019 only; pre-2019 requires inference from pack costs + BoS markup
4. No SOFC degradation / stack replacement cost quantified (5%/yr degradation, ~10-12yr replacement)

## EIA CAUTION Tag Pattern
The vocabulary scanner checks per-line. ANY line containing `\bEIA\b` without `[CAUTION: EIA` on the same line is a violation. Fix: write `[CAUTION: EIA source — historical data only]` on the same line as every EIA reference.

**Why:** The stdf_validate.py hook uses line-by-line checking in scan_banned_sources(). The phrase "with CAUTION tag" does NOT satisfy the pattern — must contain literal `[CAUTION: EIA`.
