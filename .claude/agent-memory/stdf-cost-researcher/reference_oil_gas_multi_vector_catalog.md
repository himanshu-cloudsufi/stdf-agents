---
name: reference_oil_gas_multi_vector_catalog
description: Catalog coverage and key sources for oil/gas demand disruption multi-vector analysis (transport, power generation, heating)
type: reference
---

## Oil and Gas Demand Disruption — Multi-Vector Catalog Reference

### Vector 1: Transport (BEV vs ICE)

**Well-covered in catalog (T2):**
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — 15 pts, 2010–2024, $/kWh, source: Rethinkx
- `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — 6 pts, 2019–2024, $/kWh
- `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Stationary_Storage_Cost_Global.json` — 15 pts, 2010–2024, $/kWh
- `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` — 13 pts, 2013–2025, $
- `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — 16 pts, 2010–2025, $
- `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` — 4 pts, 2022–2025, $/mile (source: AAA, Goldman Sachs)
- `data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json` — 2016–2025, $/Liter

**Gaps:** No pre-2022 EV TCO per mile series. No continuous ICE median vehicle purchase price series.

### Vector 2: Power Generation (Solar PV + BESS vs Natural Gas)

**Well-covered in catalog (T2):**
- `data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json` — 15 pts, 2010–2024, $/kW, source: Rethinkx
- `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — 15 pts, 2010–2024, %, source: Rethinkx
- `data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json` — 6 pts, 2019–2024, $/kWh, source: Rethinkx
- `data/natural_gas/cost/Natural_Gas_Price_USA.json` — 28 pts, 1997–2024, USD/MMBTU, source: EIA
- `data/natural_gas/cost/Natural_Gas_Price_Europe.json` — 35 pts, 1990–2024, USD/MMBTU
- `data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_USA.json` — 19 pts, 2006–2024
- `data/crude_oil/cost/Crude_Oil_Brent_Price_Global.json` — 35 pts, 1990–2024, $/BBL

**Must web-search (T3):**
- Solar PV LCOE in $/MWh: Lazard LCOE+ annual reports (v3.0–v17.0, 2009–2024). URL: lazard.com/research-insights/levelized-cost-of-energyplus-lcoeplus/
- IRENA global weighted average solar LCOE: IRENA RPGC annual reports. URL: irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023
- NGCC LCOE in $/MWh: Lazard LCOE+ same series. Key data: 2009=$83, 2014=$65, 2016=$63, 2018=$58, 2020=$59, 2021=$60, 2023=$70, 2024=$76 (all $/MWh, US unsubsidized mean)
- Lazard uses standardized $3.45/MMBTU gas assumption for year-over-year CCGT comparison

### Vector 3: Heating (ASHP vs Gas Furnace)

**Catalog has:**
- `data/electricity/cost/Electricity_Residential_Price_USA.json` — 45 pts, 1980–2024, $/kWh — essential for heat pump operating cost
- Natural gas prices above (gas furnace operating cost)

**Must web-search (T3) — no catalog data exists:**
- ASHP installed costs: NESCAUM "Heat Pumps in the Northeast and Mid-Atlantic" (Oct 2024): nescaum.org
- NEEP 2016 Market Strategy Report: historical 2015 ASHP costs
- Key finding: ASHP installed costs have RISEN from ~$4,500 (2010) to ~$8,500 (2024) in nominal terms — unusual vs. other disruptors. Disruption economics rest on operating efficiency (COP 2.5–3.5 vs. gas AFUE 0.80–0.97), not capital cost decline.
- Gas furnace installed: $2,800 (2010) → $5,800 (2024) — also rising. Source: HomeAdvisor/Angi.

### Key unit conversions needed by cost-fitter
- Solar $/kW → $/MWh LCOE: use capacity factor from catalog + financial assumptions
- BESS $/kWh → combined solar+BESS $/MWh: requires system sizing model
- EV vehicle $ → $/mile TCO: use annual mileage (15k/yr), lifetime (10–15 yr), electricity cost
- ASHP installed $ → $/kWh thermal: use COP + annual heat load + electricity price
- Gas furnace installed $ → $/kWh thermal: use AFUE + annual heat load + gas price
