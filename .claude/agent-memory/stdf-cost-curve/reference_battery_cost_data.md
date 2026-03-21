---
name: reference_battery_cost_data
description: Reliable catalog sources for Li-ion battery pack cost data with fitted parameters
type: reference
---

## Li-ion Battery Pack Cost Data Sources (STDF Catalog)

### Best datasets for battery pack cost analysis:
1. `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx, 15 points (2010–2024), $/kWh, best long-run series
2. `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Database, 9 points (2010–2025), $/kWh, China-specific
3. `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_USA.json` — Database, 9 points (2010–2025), $/kWh, USA-specific
4. `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — Rethinkx, 6 points (2019–2024), Passenger BEV-specific

### Fitted exponential decay parameters (derived 2026-03-16):
- **Global median (2010–2024, 15 pts):** C(t) = 1241 × exp(−0.1841 × (t−2010)), R² = 0.954, 16.8%/yr
- **China (2010–2025, 9 pts):** C(t) = 939 × exp(−0.1736 × (t−2010)), R² = 0.971, 15.9%/yr
- **Note:** 2022 data point is a commodity spike anomaly ($166/kWh vs structural trend ~$145). Does not invalidate the fit.

### Vehicle price data:
- `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — 2010–2025, $ USD
- `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — 2010–2025, $ USD
- `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` — 2013–2025, $ USD

### Service-level cost data ($/mile):
- `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` — AAA/Goldman Sachs, 2022–2025
- Only ICE $/mile is in catalog; EV $/mile must be computed from components

### Energy price data:
- `data/electricity/cost/Electricity_Residential_Price_USA.json` — Database, 1980–2024, $/kWh
- `data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json` — WorldBank.Org (WARNING: multi-series interleaved in single file)
