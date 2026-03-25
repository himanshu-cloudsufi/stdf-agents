---
name: oil_disruption_capability_benchmarks
description: Full oil disruption capability benchmarks: transport + power generation + heating sectors, all dimensions and thresholds (validated 2026-03-20)
type: reference
---

## Oil Market Disruption — Three-Sector Capability Reference (validated 2026-03-20)

### Sector 1: Transport (BEV vs ICE Passenger Car) — 9 Dimensions

7 of 9 thresholds MET. Convergence: sequential (dimensions crossed 2013–2024).

| Dimension | BEV 2024 | ICE 2024 | Threshold | Met |
|---|---|---|---|---|
| range_km | 455 km | ~800 km | 350 km | YES (2021) |
| charge_time_min (DC fast 0-80%) | 18–30 min | 3–5 min | 45 min | YES (2019) |
| acceleration_0_60_sec | 5.5 sec mainstream | 6.5 sec midsize | 7.0 sec | YES (2017) |
| maintenance_cost_usd_mile | $0.078 | $0.101 | ≤$0.101 | YES (~2015) |
| fuel_cost_usd_km | $0.029 | $0.087 | ≤$0.087 | YES (2013) |
| model_count globally | ~500 | >1,200 | ≥200 | YES (2022) |
| towing_capability_kg | 4,536 kg | 5,000–8,000 kg | 3,500 kg | YES (2022) |
| tco_usd_mile 7yr fleet avg | $0.761 | $0.633 | ≤$0.633 | APPROACHING ~2026-2027 |
| cold_range_loss_pct at −7°C | 25% | <3% | ≤20% | APPROACHING ~2027 |

Key trajectories:
- Range: 130 (2012) → 165 (2015) → 250 (2019) → 455 (2024); exponential R²=0.990
- Charge time: 90 (2012) → 45 (2019) → 20 (2024) min; decelerating R²=0.985
- Model count: 25 (2015) → 70 (2019) → 350 (2023) → 500 (2024); exponential R²=0.997
- Cold range loss: 41% (2015) → 35% (2019) → 25% (2024); decelerating R²=0.992
- Fuel cost advantage: BEV 3.0× cheaper per km at US avg electricity price

### Sector 2: Power Generation (Solar+BESS vs Natural Gas) — 11 Dimensions

9 of 11 thresholds MET. Convergence: sequential (dimensions crossed 2018–2023).

| Dimension | Solar+BESS 2024 | Gas Peaker 2024 | Threshold | Met |
|---|---|---|---|---|
| installed_cost_usd_kw | $700/kW | $700–$900/kW | <$1,000/kW | YES (2020) |
| bess_cost_usd_kwh (2hr) | $269 global; $101 China | n/a | <$300/kWh | YES (2023) |
| bess_installed_gwh global | 370 GWh | n/a | >100 GWh | YES (2021) |
| lcoe_usd_mwh system | ~$120/MWh blended | $110–$228 avg $160 | ≤$160/MWh | YES (2022) |
| ramp_rate response | <100 ms BESS | 10–30 min cold start | ≤5 min | YES (2018) |
| build_time_months | 12–24 months | 24–48 months | ≤24 months | YES (2020) |
| fuel_price_volatility_index | 0.0 (no fuel) | 1.0 (fully exposed) | <0.5 | YES (structural) |
| scalability_gw_yr | 451 GW/yr (2024) | ~20 GW/yr global | >50 GW/yr | YES (2020) |
| land_use_acres_gwh | ~7 acres/GWh | ~0.5–2 acres/GWh | ≤10 acres/GWh | YES |
| dispatchability_index | ~70% seasonal avg | ~100% | ≥80% | APPROACHING ~2027-2028 |
| capacity_factor_pct standalone | 16.3% | 37.2% | System metric applies | NOT MET (physics bound) |

Key trajectories:
- Solar cost: $5,310 (2010) → $2,090 (2015) → $1,161 (2019) → $700 (2024) $/kW; decelerating R²=0.991; −87% over 14yr
- BESS capacity: 0.19 (2010) → 3.19 (2015) → 22.6 (2019) → 370 (2024) GWh; exponential R²=0.998; CAGR 71.6%
- BESS cost: $441 (2019) → $314 (2021) → $269 (2024) $/kWh; decelerating R²=0.864
- Solar deployment: 50 (2015) → 119 (2019) → 330 (2023) → 451 (2024) GW/yr; exponential R²=0.983
- Solar CF (standalone): bounded ~13–18% physics range; linear R²=0.307; not a capability dimension

### Sector 3: Heating (ASHP vs Gas Furnace) — 10 Dimensions

8 of 10 thresholds MET. Convergence: divergent (performance MET, capital cost NOT MET).

| Dimension | ASHP 2024 | Gas Furnace 2024 | Threshold | Met |
|---|---|---|---|---|
| COP_mild at +7°C | 3.5 seasonal avg | 0.97 AFUE equiv | ≥2.5 | YES since 2010 |
| COP_cold at −15°C | 2.1 (ccASHP) | 0.85 equiv | ≥1.75 | YES (~2022) |
| cooling_capability | Full A/C 25+ SEER | Heating only | Dual heat+cool | YES (structural) |
| op_cost_usd_kwh_thermal | $0.046 US; £0.093 UK | $0.047 US; £0.148 UK | ≤incumbent | YES (MET UK, borderline US) |
| noise_dba outdoor | 40–55 dBA modern | 55–70 dBA indoor | ≤55 dBA | YES (2018) |
| lifespan_yr | 15–20 yr inverter | 20–30 yr gas | ≥15 yr | YES |
| space_requirement_sqm | 0.8 sqm outdoor unit | 0.3–0.5 sqm indoor | ≤1.5 sqm | YES |
| upfront_cost_ratio gross | 5.0× gross; ~2.0× net w/subsidy | 1.0× | <3.0× gross | NOT MET; model-derived crossing ~2036 |
| install_complexity ducted retrofit | 3.5/5 (ductwork+panel) | 1.5/5 | ≤2.5/5 | NOT MET |
| install_complexity ductless mini-split | 2.0/5 | 1.5/5 | ≤2.5/5 | YES (2022) |

Key trajectories:
- COP mild: 2.5 (2010) → 2.8 (2015) → 3.2 (2020) → 3.5 (2024); exponential R²=0.994
- COP cold: 1.2 (2015) → 1.4 (2018) → 1.7 (2020) → 2.1 (2024); exponential R²=0.987
- Upfront cost ratio: 6.4× (2015) → 5.6× (2020) → 5.0× (2024); decelerating R²=0.990; model-derived ~2036 gross
- EU HP market share: 8% (2013) → 14% (2018) → 24% (2023); exponential R²=0.997; model-derived 50% ~2030
- US operating cost: ASHP $0.046 vs gas $0.047/kWh thermal — borderline, gas-price sensitive
- UK operating cost: ASHP £0.093 vs oil boiler £0.148 per kWh thermal — clearly MET (37% cheaper)
- COP efficiency advantage: 3.6× at mild climate; 2.5× at −15°C cold climate

### Key Data Sources
- STDF catalog: `data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json` (Rethinkx)
- STDF catalog: `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` (Rethinkx)
- STDF catalog: `data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_Global.json` (Rethinkx)
- STDF catalog: `data/energy_storage/adoption/Battery_Energy_Storage_System_Installed_Capacity_Global.json` (Rethinkx)
- STDF catalog: `data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` (Rethinkx)
- STDF catalog: `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json` (FuelEconomy.gov)
- STDF catalog: `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_USA.json` (IEA)
- DOE FOTW #1375 (Dec 2024): Median EV range MY2024 = 283 mi = 455 km
- AAA Annual Driving Cost Study 2024: EV $0.078/mile vs ICE $0.101/mile maintenance
- Vincentric 2024: segment-level TCO; sedan/SUV already below ICE
- Lazard LCOE+ June 2024: gas peaker $110–$228/MWh; solar standalone $29–$92/MWh
- PNNL-37127: DOE cold climate heat pump field study COP benchmarks
- ENERGY STAR ccASHP designation: COP ≥ 1.75 at 5°F (−15°C)
- EHPA Market Data 2024: European heat pump sales 2010–2024
