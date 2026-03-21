---
name: liion_vs_leadacid_capability_benchmarks
description: Li-ion vs lead-acid battery capability benchmarks across 13 dimensions for 4 application segments (SLI, telecom, datacenter UPS, forklift), with validated thresholds and parity years (validated 2026-03-20)
type: project
---

## Li-ion vs Lead-Acid Battery Capability Benchmarks

**Context:** Lead demand decline analysis. Disruptor = LFP/NMC Li-ion. Incumbent = lead-acid (SLI, VRLA, deep-cycle, flooded).

### Key Catalog Files Used
- `data/battery_pack/energy_density/Lithium_Ion_Battery_Pack_Battery_Energy_Density_USA.json` — clean energy density trajectory (use USA, not Global — Global has 2021/2024 anomalies)
- `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Li-ion global pack cost 2010-2024
- `data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json` — Lead-acid USA pack cost
- `data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json` — SLI unit cost (factory wholesale)
- `data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json` — LFP SLI unit cost trajectory (decelerating fit R²=0.997)

### Validated Thresholds and Parity Status (2024)

| Dimension | Li-ion 2024 | Lead-acid 2024 | Threshold | MET? | Parity Year |
|---|---|---|---|---|---|
| energy_density_Wh_kg | 195 Wh/kg | 35-50 Wh/kg | >80 Wh/kg | YES | Pre-2010 |
| cycle_life_cycles_80pct_DoD | 5,000 | 200-800 | 1,500 (forklift), 2,000 (stationary) | YES | 2015-2017 |
| round_trip_efficiency_pct | 97-98% | 70-85% | >90% | YES | ~2010 |
| self_discharge_pct_per_month | 1.0% | 3-5% | <3% | YES | ~2014 |
| operating_temp_range | -20 to +60°C | -40 to +60°C | -20 to +50°C mainstream | YES (mainstream) | ~2020 |
| charge_rate_C | 1-3C | 0.1-0.3C | 1C | YES | ~2016 |
| cost_per_kwh_upfront_USD | $115/kWh | $130-180/kWh | <$200/kWh (stationary) | YES | ~2018-2019 |
| SLI_battery_unit_cost_USD | $100 (China), $180 (USA) | $25 (China), $55 (USA) | <$55 (China), <$75 (USA) | NO | USA ~2027-2028, China ~2031 |
| levelized_cost_per_cycle | $0.023/kWh/cycle | $0.36-0.60/kWh/cycle | <$0.60 | YES | ~2014 |
| weight_kg_per_kWh | 5.8 kg/kWh | 20-25 kg/kWh | <10 kg/kWh | YES | Pre-2010 |
| recycling_rate_pct | 30% | 97-99% | ≥70% (EU reg threshold) | NO | ~2029 |
| calendar_life_yr | 12-15 yr | 3-8 yr | ≥10 yr | YES | ~2020 |
| maintenance_hrs_per_yr | 0.1 hrs | 0.5-6 hrs | <0.5 hrs | YES | ~2018 |

### Application Segment Parity Status (2024)
- **Telecom UPS**: ACHIEVED (~2021) — all technical + cost dimensions met
- **Datacenter UPS**: ACHIEVED (~2021)
- **Forklift/motive**: ACHIEVED (~2019-2020, TCO parity established)
- **Stationary industrial**: ACHIEVED (~2020)
- **Automotive SLI**: NOT YET — blocked by unit price (4x gap) and extreme cold performance; mass-market parity 2027-2031

### Convergence Pattern: Sequential
- Technical dimensions crossed 2010-2020
- Levelized cost crossed ~2014
- Pack cost per kWh crossed ~2018-2019
- SLI unit price last blocker: 2027-2031 by region

### Key Analytical Notes
- **Use SLI unit cost ($/battery), NOT cost/kWh, for automotive segment** — consumers buy on per-unit price, not kWh economics
- Lead-acid pack cost trajectory is nearly flat ($300 → $180 over 14 yrs); Li-ion dropped $1,321/kWh in same period
- Li-ion levelized cost parity crossed first (~2014) — this is why B2B segments (telecom, forklift) adopted first
- Recycling rate is the only purely non-economic blocker remaining (regulatory, not performance)
- Global Li-ion Energy Density dataset has anomalous values in 2021 (270) and 2024 (285) — use USA series for clean trajectory
