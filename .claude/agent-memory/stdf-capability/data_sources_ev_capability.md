---
name: data_sources_ev_capability
description: Reliable data sources for EV/ICE capability metrics available in the STDF catalog and web
type: reference
---

## STDF Catalog — Key EV Capability Files

### Energy Efficiency
- `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json` — FuelEconomy.gov; 2015–2024; kWh/100km; linear −0.31/yr
- `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_Europe.json` — ICCT; 2015–2024; kWh/100km
- `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_China.json` — DieselNet; 2015–2024; kWh/100km

### Battery Pack Size (proxy for range potential)
- `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_USA.json` — IEA; 2015–2024; kWh; linear +3.9 kWh/yr
- `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_China.json` — IEA; 2015–2024; kWh

### Charging Infrastructure
- `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json` — Database; 2015–2024; units; CAGR 45.7%
- `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_USA.json` — Database; 2015–2024; units

### Autonomous Driving Readiness
- `data/autonomous_vehicle/safety_incidents/Autonomous_Vehicle_Disengagements_per_Million_Miles_Global.json` — MDPI Study; 2018–2022
- `data/autonomous_vehicle/adoption/Autonomous_Passenger_Car_Annual_Sales_(L2)_Global.json` — IDTechEx; 2020–2025; Million Units
- `data/passenger_cars/cost/Autonomous_Vehicle_LiDAR_(High_End_Spinning)_Price_USA.json` — Database; 2018–2025; USD; fell $60k→$9k (−85%)
- `data/passenger_cars/cost/Autonomous_Vehicle_LiDAR_(Low_Cost_ADAS)_Price_China.json` — Database; 2018–2025; USD; fell $2k→$250

### Cost Benchmarks
- `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` — AAA, Goldman Sachs; 2022–2025
- `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` — Database; 2010–2025

## Web Sources — Not in Catalog but Reliable
- AAA annual study "Your Driving Costs": maintenance EV $0.078/mile vs ICE $0.101/mile (2024)
- Vincentric 2024 EV Cost of Ownership Analysis: segment-level TCO comparisons
- U.S. DoE FOTW #1374 (Dec 2024): median EV range MY2024 = 283 miles = 455 km
- InsideEVs: historical range data 2012–2024
- ICCT: real-world CO2 / efficiency values Europe
- PMC article 10358619: BEV NVH recent progress
- S&P Global: OTA/software-defined vehicle analysis
- IDTechEx: autonomous passenger car sales by SAE level
- Roland Berger EV Charging Index 2024: global infrastructure deployment
