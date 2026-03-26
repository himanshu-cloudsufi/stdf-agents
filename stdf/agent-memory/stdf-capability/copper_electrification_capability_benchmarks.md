---
name: copper_electrification_capability_benchmarks
description: Copper demand capability benchmarks across 5 electrification disruptions: BEV/ICE, solar PV, wind, BESS, grid infrastructure — copper intensity factors, all thresholds, trajectory data (validated 2026-03-25)
type: reference
---

## Copper Demand from Electrification — Capability Reference (validated 2026-03-25)

### Key Copper Intensity Factors

| Technology | Copper Intensity | Incumbent | Multiplier |
|---|---|---|---|
| BEV | 83 kg/vehicle | ICE 23 kg/vehicle | 3.6x |
| Solar PV | ~5.5 t/MW | Gas ~1.5 t/MW | 3.7x |
| Onshore Wind | ~8 t/MW | Gas ~1.5 t/MW | 5.3x |
| Offshore Wind | ~15 t/MW | Gas ~1.5 t/MW | 10.0x |
| BESS | ~1.0 t/MWh | n/a | — |
| Grid reinforcement | ~2 kt/GW | n/a | — |

### Aggregate Electrification Copper Demand 2024

| Source | kt | Method |
|---|---|---|
| Solar PV deployment | 2,480 | 451 GW × 5.5 t/MW |
| Wind deployment | 1,200 | 120 GW × 10 t/MW blended |
| Grid reinforcement | 1,000 | 500 GW × 2 kt/GW |
| BEV incremental | 660 | 11M × 60 kg |
| BESS | 181 | 181 GWh × 1 t/MWh |
| **TOTAL** | **5,522** | |
| Share of global supply | **~20.4%** | vs ~27,000 kt global |

### Key Trajectory Data

**Solar PV installed cost:** $5,310 (2010) → $2,090 (2015) → $1,161 (2019) → $700 (2024); decelerating, R²=0.991
- Catalog: data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx)

**Onshore wind installed cost:** $2,272 (2010) → $1,911 (2015) → $1,552 (2020) → $1,041 (2024); decelerating, R²=0.946
- Catalog: data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx)

**Offshore wind installed cost:** $5,409 (2010) → $4,263 (2019) → $2,852 (2024); decelerating, R²=0.946
- Catalog: data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx)

**BESS 2hr turnkey cost:** $441 (2019) → $314 (2021) → $269 (2024); decelerating, R²=0.864
- Catalog: data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json

**BESS cumulative capacity:** 3.2 (2015) → 22.6 (2019) → 189 (2023) → 370 (2024) GWh; exponential, R²=0.998
- Catalog: data/energy_storage/adoption/Battery_Energy_Storage_System_Installed_Capacity_Global.json
- CAGR 2019–2024: 74.9%

**BEV global annual sales:** 5k (2010) → 244k (2015) → 1.6M (2019) → 11M (2024); exponential, R²=0.969
- CAGR 2015–2024: 52.7%
- Catalog: data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json

**Solar PV capacity factor:** 13.8% (2010) → 16.5% (2015) → 17.9% (2018) → 16.3% (2024); bounded linear, R²=0.820
**Onshore wind CF:** 27.3% (2010) → 29.1% (2015) → 35.7% (2019) → 34.0% (2024); linear, R²=0.820
**Offshore wind CF:** ~40–42% (2010–2024); flat, R²=0.300 (resource-bounded ceiling)
**Gas CF:** mean 38.3%, σ=0.9% (effectively flat 2006–2024)

### Threshold Status Summary

**BEV vs ICE (7 dims):** 6 MET, 1 NOT MET (ev_tco_fleet_avg: parity 2028)
**Solar PV (6 dims):** 5 MET, 1 APPROACHING (solar_dispatchability: ~2026 with BESS)
**Wind (6 dims):** 6 MET
**BESS (6 dims):** 6 MET
**Grid infrastructure (5 dims):** All structural — all YES
**Aggregate: 29/31 MET**

### Parity Year Estimates [model-derived]
- ev_tco_fleet_avg_usd_mile: 2028
- BESS cost to $200/kWh: 2027
- Solar cost to $500/kW: 2027
- Onshore wind cost to $800/kW: 2027
- Solar 4hr dispatchability (with BESS): ~2026

### IEA Citation Format (Critical — hook enforcement)
- WRONG: '[T3: CAUTION: IEA source]' — the '[' must be immediately before 'CAUTION'
- CORRECT: '[CAUTION: IEA source — historical data only][T3]'
- The hook checks `'[CAUTION: IEA' in line` — must start with '[CAUTION:'

### Jevons Classification
- Solar PV, Wind, BESS: Stellar — Jevons does NOT apply
- BEV: Hybrid (dominant Stellar) — Jevons does NOT apply
- Copper itself: X-Flow — Jevons MAY apply (displacement could reduce per-unit intensity)

### Data Sources
- Wood Mackenzie / CRU Copper Intensity Report 2023: per-vehicle and per-MW copper intensity
- All STDF catalog curves above: Rethinkx source, Tier 2
- Lazard LCOE v17 (June 2024): LCOE benchmarks
- AAA Annual Driving Cost Study 2024: EV/ICE operating cost
