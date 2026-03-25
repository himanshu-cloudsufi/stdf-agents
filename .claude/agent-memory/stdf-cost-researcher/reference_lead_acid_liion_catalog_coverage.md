---
name: reference_lead_acid_liion_catalog_coverage
description: Catalog coverage and T1/T3 sources for lead-acid vs. lithium-ion battery disruption analysis (lead demand decline use case)
type: reference
---

## Catalog Coverage for Lead-Acid vs. Li-Ion Battery Analysis

### Li-Ion Battery Pack Cost Curves (data/battery_pack/cost/)
- `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx/BNEF, $/kWh, 2010–2024, 15 annual pts. PRIMARY disruptor curve.
- `Lithium_Ion_Battery_Pack_Median_Cost_China.json` — 2010–2024, 8 pts (every 2 yrs)
- `Lithium_Ion_Battery_Pack_Median_Cost_USA.json` — 2010–2024, 8 pts
- `Lithium-Ion_Battery_Pack_(Stationary_storage)_Cost_China.json` — 2010–2024, 15 pts, source "Database"
- `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — 2019–2024, 6 pts
- `Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_Global.json` — 2018–2024, 7 pts
- `12V_Lithium_Ion_SLI_Battery_Cost_China.json` — $/battery (60Ah), 2010–2024 HISTORICAL ONLY. Source: CBB Battery/Made-in-China.com. WARNING: 2025–2040 values are model-derived, exclude them.
- `12V_Lithium_Ion_SLI_Battery_Cost_USA.json` — same structure, same warning

### Lead-Acid Battery Pack Cost Curves (data/battery_pack/cost/)
- `Lead_Acid_Battery_Pack_Median_Cost_USA.json` — $/kWh, 2010–2023 (use through 2023 only; 2024+ may be model-derived)
- `Lead_Acid_Battery_Pack_Median_Cost_China.json` — same structure
- `Lead_Acid_Battery_Pack_Median_Cost_Europe.json` — same structure
- `Lead_Acid_Battery_Pack_Median_Cost_Rest_of_World.json` — same structure
- `12V_Lead_Acid_SLI_Battery_Cost_China.json` — $/battery (60Ah), 2010–2024. Very flat ~$25–$30 China, ~$55–$70 USA
- `12V_Lead_Acid_SLI_Battery_Cost_USA.json` — same structure

### BESS System-Level Curves (data/energy_storage/cost/)
- `Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` — Rethinkx, $/kWh, 2019–2024. Use for stationary Li-ion vs. VRLA UPS comparison.
- `Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json` — same structure
- Also available: China, Europe, USA variants of both

### Forklift Cost Curves (data/forklift/cost/)
- `Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json` — $/unit, 2010–2024
- Same series for USA, Europe, Rest of World
- NO lead-acid forklift battery cost curve exists in catalog — use T3 benchmark: $2,000–$8,000 per 48V/600Ah pack

### Lead Sector (data/lead/)
- `data/lead/cost/Lead_Cost_Global.json` — Rethinkx, $/tonne, 1998–2024. Full commodity price history.
- `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — Rethinkx, 2010–2024, total lead demand in kt
- Also: motive power, stationary, non-battery demand breakdowns

### Key Gaps Requiring T1/T3 Sources
1. Lead-acid VRLA UPS system-level cost time series — NOT in catalog. Use PNNL ESGC 2020 ($170–236/kWh installed, 2020 data point) as T1 anchor (PDF not parseable; use secondary citations).
2. Lead-acid forklift pack cost — NOT in catalog. T3: $2,000–$8,000/pack for 48V/600Ah (2024).
3. Levelized cost per cycle data — T3 only. PowerTech Systems (2015): AGM ~EUR 0.42/kWh-cycle, LFP ~EUR 0.15/kWh-cycle.

### Reliable T1 Source: BLS PPI
- FRED series PCU3359113359111: Lead-Acid Battery PPI (Dec 1984=100), 2000–2024 annual averages
  - 2010: 181.9, 2015: 198.1, 2018: 218.8, 2020: 213.0, 2022: 250.3, 2024: 260.7
  - URL: https://fred.stlouisfed.org/data/PCU3359113359111.txt (text download gives full series)

### Unit Confusion Patterns
- Catalog lead-acid pack curves are $/kWh nameplate. VRLA cycle life is 200–1,500 cycles @50% DoD, so levelized cost is 3–10x the nameplate $/kWh.
- SLI batteries: levelized cost framing is NOT appropriate (float service, essentially infinite cycle life). Use $/unit directly.
- Forklift Li-ion catalog is $/unit (full pack), not $/kWh. Typical 48V/600Ah Li-ion = 28.8 kWh.

### Key Data Points (2024)
- Li-ion global median: $115/kWh (Rethinkx T2)
- Li-ion China: $94/kWh (Rethinkx T2)
- Lead-acid USA pack: $180/kWh (2023, catalog T2)
- Lead-acid China pack: $140/kWh (2023, catalog T2)
- BESS 2-hr turnkey: $269/kWh (2024, Rethinkx T2)
- 12V SLI lead-acid China: $25/battery ($35/kWh); Li-ion equivalent: $100/battery ($139/kWh) — 4x premium persists at end of 2024.
