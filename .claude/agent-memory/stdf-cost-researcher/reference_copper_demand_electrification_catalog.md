---
name: reference_copper_demand_electrification_catalog
description: Catalog coverage and T1/T3 sources for copper demand analysis driven by electrification (EV, solar, wind, BESS); key curve paths, copper intensity data, demand share percentages, LCOE sources, data gaps
type: reference
---

## Copper Demand Electrification Analysis — Catalog Reference

### Copper Sector (data/copper/) — Very Rich Coverage

**Price and Cost:**
- `data/copper/cost/Copper_Price_Global.json` — $/lb, 1990–2024, 35 pts, source "Database". MUST convert to $/tonne (multiply by 2,204.62).
- `data/copper/cost/Copper_Copper_Mining_Cost_Global.json` — $/tonne, 2012–2024, 13 pts, source "Database". Mining cost is RISING (2012: $2,600 → 2024: $4,600) — model as upward slope, not flat or declining.
- Also available: China, Europe, USA variants of both.

**2024 copper values:**
- LME spot global: $4.147/lb = $9,142/tonne [T2]
- Mining cost global: $4,600/tonne [T2]

**Demand and Adoption:**
- `data/copper/adoption/Copper_Annual_Consumption_Global.json` — kt, 1990–2024, 35 pts. 2024: 27,347 kt
- `data/copper/adoption/Copper_EV_Demand_Percentage_Global.json` — %, 2015–2024. EV share: 1.0% (2015) → 5.0% (2024)
- `data/copper/adoption/Copper_Solar_Demand_Percentage_Global.json` — %, 2015–2024. Solar share: 0.7% (2015) → 2.0% (2024)
- `data/copper/adoption/Copper_Wind_Turbines_Percentage_Global.json` — %, 2015–2024. Wind share: 0.7% (2015) → 1.5% (2024)
- `data/copper/adoption/Copper_Electrical_Demand_Percentage_Global.json` — %, 2000–2024. ~33–35% of total demand (stable)
- `data/copper/adoption/Copper_Demand_Transportation_Percentage_Global.json` — %, 2000–2024. 10–15% of total demand (rising slowly)
- All regional variants available (China, Europe, USA, Rest of World)
- WARNING: These percentage series are "Database" source with no named methodology — cross-check with ICSG for validation before using in stream-forecaster.

**Recycling:**
- `data/copper/recycle_rate/Copper_Annual_Recycling_Rate_Global.json` — %/year, available for all regions.

### Disruptor Technology Costs — Fully Covered in Catalog

- Li-ion battery pack global median: 15 pts 2010–2024, source Rethinkx [T2]. 2024: $115/kWh
- Li-ion battery pack passenger BEV: 6 pts 2019–2024, source Rethinkx [T2]. 2024: $97/kWh
- Solar PV installed cost global: 15 pts 2010–2024, source Rethinkx [T2]. 2024: $700/kW
- Onshore wind installed cost global: 41 pts 1984–2024, source Rethinkx [T2]. 2024: $1,041/kW
- Offshore wind installed cost global: 25 pts 2000–2024, source Rethinkx [T2]. 2024: $2,852/kW
- BESS 2-hr turnkey global: 6 pts 2019–2024, source Rethinkx [T2]. 2024: $269/kWh
- Solar PV module (mainstream, Europe): 8 pts 2017–2024, source Rethinkx [T2]. 2024: $0.15/W

### LCOE Data ($/MWh) — NOT in Catalog, Must Use IRENA T1

IRENA Renewable Power Generation Costs annual reports are the T1 source for LCOE. All have CAUTION tag required.

**Solar PV LCOE (global weighted avg):**
- 2010: $460/MWh, 2018: $85/MWh, 2020: $57/MWh, 2022: $49/MWh, 2023: $44/MWh, 2024: $43/MWh
- Note: IRENA 2010 baseline varies between reports ($417–$460/MWh) — use $460 from 2023 report.
- Intermediate years (2012, 2014, 2016) only available as chart-reads: ~$310, ~$220, ~$150.

**Onshore wind LCOE (global weighted avg):**
- 2010: $89/MWh, 2016: $70/MWh, 2019: $53/MWh, 2020: $39/MWh, 2021: $33/MWh, 2023: $33/MWh, 2024: $34/MWh
- Lazard LCOE+ v3.0 (2009): $135/MWh — for pre-IRENA anchor [T3 CAUTION].

**Offshore wind LCOE (global weighted avg):**
- 2010: $203/MWh, 2022: $80/MWh, 2023: $75/MWh, 2024: $79/MWh
- Intermediate years NOT precisely documented from public summaries.

**Gas peaker LCOE (USA, new-build):**
- Lazard LCOE+ v3.0 (2009): ~$150/MWh midpoint; v17.0 (2023): $115–221/MWh [T3 CAUTION]
- Gas CCGT: $83/MWh (2009) → $76/MWh (2023) — rising then declining, now flat [T3 CAUTION]
- IRENA global weighted avg fossil fuel cost (2024): $100/MWh [different concept from Lazard new-build]

### Solar PV Module Price Pre-2010 (T3 Only)

Approximate nominal $/W values (NREL composite, Nemet 2009, Farmer & Lafond 2016):
- 2000: ~$5.0/W, 2004: ~$3.5/W, 2008: ~$4.2/W (ANOMALY — polysilicon shortage above trend), 2010: ~$1.8/W
- WARNING: 2008 is above the learning curve trend — exclude from curve fitting.

### Copper Intensity per Technology (T3 — CDA/ICA Sources)

- ICE vehicle: ~23 kg/vehicle (Copper Development Association)
- BEV: ~83 kg/vehicle (CDA) — but declining toward ~45–70 kg; treat as ceiling
- Solar PV: ~5.0 tonnes/MW (ICA/CDA)
- Onshore wind: ~3.0 t/MW central estimate; range 2.2–4.8 t/MW (wide uncertainty)
- Offshore wind: ~9.5 t/MW (includes submarine cables)
- Li-ion battery stationary: ~200 kg/MW
- Electric bus BEV: ~224–369 kg/bus

**KEY CONFLICT:** Onshore wind copper intensity has wide disagreement (2.2–14.9 t/MW across sources). Use 3.0 t/MW as central estimate but flag as ±50% uncertainty.

**KEY RISK:** BEV copper intensity declining due to thrifting — Benchmark Minerals 2024 reports ~70 kg/BEV already (vs CDA 83 kg). No time-series of the decline exists; only snapshot. Treat as structural downside risk for copper demand modeling.

### Capacity Factor Data in Catalog

- Solar PV capacity factor global: `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — 15 pts, 2010–2024. 2024: 16.3%
- Natural gas capacity factor USA: `data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_USA.json` — 19 pts, 2006–2024. 2024: 35.8%
- NO wind capacity factor series in catalog — use IRENA: 34% onshore (2024), up from 27% in 2010

### Natural Gas Price (Incumbent Fuel Cost)

- `data/natural_gas/cost/Natural_Gas_Price_USA.json` — source US Energy Information Administration [CAUTION: EIA source], $/MMBTU, 1997–2024. 2024: $2.19/MMBTU
- `data/natural_gas/cost/Natural_Gas_Price_Europe.json` — source FRED, $/MMBTU, 1990–2024. 2024: $10.89/MMBTU (highly volatile — 2021 spike to $15.9, 2022 spike to $37.5)

### Multi-Vector Analysis Pattern

When copper is the commodity being analyzed (not just one technology disruption), the structure is:
1. Collect cost data for ALL demand-driving disruptive technologies separately
2. Each technology needs its own service-level unit ($/MWh for generation, $/vehicle for transport)
3. Copper intensity per technology unit is the bridge from technology deployment to copper demand
4. The demand-decomposer combines: deployment_volume * intensity_per_unit = copper_demand
5. The cost-fitter upstream must model the S-curve adoption for each technology
6. This is a "commodity demand through disruption" pipeline pattern, not a simple parity comparison

### Data NOT Available in Catalog

- LCOE data in $/MWh for any technology — must use IRENA T1 or Lazard T3
- Solar module prices pre-2017 — T3 only (NREL composite)
- Copper intensity time-series (declining trend) — only point-in-time data from CDA/ICA
- EV charging infrastructure copper demand — no data found anywhere
- Wind capacity factor series — no catalog data; use IRENA 27→34% trend narrative
