---
name: Vehicle Capability Data Sources
description: Reliable data sources for vehicle capability benchmarks — validated sources for BEV/ICE performance, cost, infrastructure, and safety dimensions
type: reference
---

## Catalog Sources (T2 — use first)

| Dimension | File | Notes |
|-----------|------|-------|
| Battery energy density (Wh/kg) | data/battery_pack/energy_density/Lithium_Ion_Battery_Pack_Battery_Energy_Density_USA.json | USA data most reliable; Global file has anomalous 2021/2024 spike |
| Battery pack cost ($/kWh) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json | Rethinkx source; 2019–2024 |
| BEV median purchase price USA | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | 2010–2025 |
| ICE median purchase price USA | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | 2010–2025 |
| BEV lowest cost entry USA | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | 2010–2025 |
| EV public charging points USA | data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_USA.json | 2015–2024 |
| EV public charging points Global | data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json | 2015–2024 |
| BEV median China | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | 2010–2025; most advanced price curve |
| PHEV TCO | data/passenger_cars/cost/Passenger_Vehicle_(PHEV)_TCO_*.json | Chimera data — use for comparison only, not disruptor |
| BEV annual sales | data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_*.json | Rethinkx |

## Web Sources (T3 — gap-fill only)

| Dimension | Source | URL |
|-----------|--------|-----|
| Range trajectory | IEA Global EV data [CAUTION: IEA] | iea.org/reports/global-ev-outlook-2024 |
| Range trajectory (academic) | ScienceDirect 2025 | sciencedirect.com/science/article/pii/S1361920925005826 |
| Charging speed historical | US DOT | transportation.gov/rural/ev/toolkit/ev-basics/charging-speeds |
| Acceleration benchmarks | InsideEVs | insideevs.com/news/709122/ |
| Maintenance cost | Consumer Reports 2020 | advocacy.consumerreports.org/wp-content/uploads/2020/10/EV-Ownership-Cost-Final-Report-1.pdf |
| Maintenance cost | DOE EERE | betterenergy.org/blog/consumer-reports-study... |
| Cold weather | DOE VTO 2024 | energy.gov/sites/default/files/2024-10/Impact_of_Cold_Ambient_Temperature_on_BEV_Performance_v15 |
| Towing | Arval UK | arval.co.uk/news-insights/new-electric-vehicle-research-reveals-towing-range-data |
| Model count | ICCT 2025 | theicct.org/publication/us-passenger-ev-sales-and-model-availability-through-2024-apr25/ |
| Infrastructure | AFDC | afdc.energy.gov/fuels/electricity-infrastructure-trends |

## Key Thresholds (validated)

- Range: 350 km (daily + weekly use without anxiety)
- Charge time: 30 min for 10–80% DCFC (acceptable road stop)
- Purchase price ratio: ≤1.20x BEV/ICE
- TCO ratio: ≤1.00x (parity)
- Maintenance: ≤$0.050/mile
- Infrastructure: ≥100k public stations (USA functional coverage)
- Acceleration: ≤7.0 sec 0–100 kph
- Cold weather retention: ≥70% at −15°C
- Towing range at max load: ≥200 km
- Model count: ≥200 global models
- Energy density: ≥200 Wh/kg

**Why:** Derived analytically during BEV/ICE capability analysis 2026-03-27
**How to apply:** Use as starting thresholds; adjust for commercial/fleet vs. consumer segments
