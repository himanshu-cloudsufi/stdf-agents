---
name: Automotive/BEV catalog coverage map
description: Which catalog files exist for BEV vs ICE cost analysis, their time ranges, and known gaps
type: reference
---

## Battery Pack Cost
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx, 2010–2024, $/kWh, 15 points
- `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — Rethinkx, 2019–2024, $/kWh
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_USA.json` — Database, 2010–2025
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Database, 2010–2025

## BEV Vehicle Purchase Price
- `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — Database, 2010–2025, USD
- `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json` — Database, 2010–2025, USD
- `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_Europe.json` — Database, 2010–2025, USD
- `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` — Database, 2013–2025

## ICE Vehicle Purchase Price
- `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Hatchback)_USA.json` — Database, 2010–2025
- `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — Database, 2010–2025
- `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` — Database, 2010–2025
- China and Europe variants available for all three segments

## ICE Operating Cost
- `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` — AAA/Goldman Sachs, 2022–2025 only (SPARSE)
- `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` — same source, 2022–2025 only

## Fuel Cost
- `data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json` — WorldBank.Org, 2015–2025, $/Liter (multi-series → compute median by year)
- China, Germany variants available

## BEV Operating Inputs
- `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json` — FuelEconomy.Gov, 2015–2024, kWh/100km
- `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_USA.json` — IEA [CAUTION], 2015–2024, kWh

## Known Gaps
- No electricity retail price series in catalog (needed for BEV $/km)
- No ICE fuel consumption (L/100km) time series in catalog (only all-in $/mile 2022+)
- No pre-2010 BEV vehicle price data
- No pre-2015 BEV energy consumption data
