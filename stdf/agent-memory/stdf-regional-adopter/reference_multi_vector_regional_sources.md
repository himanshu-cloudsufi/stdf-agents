---
name: multi-vector regional adoption data sources
description: Reliable and sparse data sources for V1 EV, V2 solar, V3 heat pump regional adoption analysis
type: reference
---

## V1 (EV) Regional Sources -- RELIABLE (T2 catalog)

Rethinkx catalog has per-region annual sales for all 4 regions (China, Europe, USA, Rest of World) 2010-2024:
- `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Annual_Sales_[Region].json`
- `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_[Region].json`

Cross-validate with CPCA (China Passenger Car Association) for China denominator. China catalog total=23.86M (passenger cars only) vs CPCA ~27-31M (all vehicles). Use catalog for internal consistency.

## V2 (Solar) Regional Sources -- RELIABLE (T1 + T2)

- Rethinkx catalog: `data/energy_generation/adoption/Solar_Annual_Power_Generation_[Region].json` for solar TWh
- Total electricity generation denominators: BP Statistical Review (T1) for China/Europe/USA; Ember GER for RoW
- Cross-check: Ember European Electricity Review 2025 independently confirms EU solar at 11% (304 TWh, 2024) -- matches catalog 10.48% closely

## V2 BESS Regional -- RELIABLE (T2 catalog)

- `data/energy_storage/adoption/Battery_Energy_Storage_System_Installed_Capacity_[Region].json`
- China, Europe, USA, Rest of World series available 2010-2024

## V3 (Heat Pump) Regional Sources -- MIXED QUALITY

- Europe: EHPA annual statistics -- RELIABLE (T1), 2013-2023 time series, URL: https://www.ehpa.org/market-data/
- USA: AHRI Monthly Shipment Reports -- RELIABLE (T1), URL: https://www.ahrinet.org/analytics/statistics
  NOTE: AHRI metric = share of cooling equipment, not full heating installed base. Use ~10% for stock-level metric.
- China: SPARSE -- no T1/T2 time series for "new heating installation share" metric
  Use IIR (https://iifiir.org) and IEA Future of Heat Pumps in China for qualitative framing only
  Estimate ~12% with ±5pp uncertainty (T3)

## Key metric distinctions

- V3 Europe: "share of new heating installations" (EHPA -- flow metric)
- V3 USA: "share of HVAC cooling equipment shipments" (AHRI) OR "heat pump as % of full HVAC installed base" (~10%)
- V3 China: installed capacity stock (not comparable to EU flow metric)
- These metrics are NOT directly comparable across regions -- always flag this in output
