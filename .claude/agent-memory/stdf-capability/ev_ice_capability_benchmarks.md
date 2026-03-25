---
name: ev_ice_capability_benchmarks
description: Validated EV vs ICE capability thresholds, trajectories, and parity years for 15 dimensions (updated 2026-03-21, third pass — full set)
type: reference
---

## EV vs ICE Passenger Car — Capability Dimension Reference (validated 2026-03-21)

### Range (range_km)
- Threshold: 350 km (mainstream buyer objection floor)
- Threshold crossed: 2018 (USA avg fleet, computed from IEA pack size / FuelEconomy.gov efficiency)
- 2024 value: 486 km (USA avg, IEA 87 kWh pack / 17.9 kWh/100km); 455 km median (DoE FOTW #1374)
- Trajectory: linear, R²=0.938; 216 (2015) → 312 (2017) → 367 (2018) → 400 (2020) → 486 (2024)
- ICE incumbent: ~800 km full tank
- Range derived from pack_kWh ÷ efficiency_kWh/km using catalog values; NOT manufacturer-claimed WLTP

### DC Fast Charging Time (charge_time_min, 0-80%)
- Threshold: 45 min (mainstream convenience — fits meal break / shopping trip)
- Threshold crossed: 2019
- 2024 value: 18 min mainstream 800V; 9 min BYD Flash Charging
- Trajectory: decelerating, R²=0.972; 90 (2012) → 60 (2015) → 50 (2018) → 45 (2019) → 18 (2024)
- ICE: 3–5 min refuel (structural gap remains; but home charging is asymmetric advantage)

### Acceleration (acceleration_0_60_sec)
- Threshold: 7.0 sec (match avg midsize ICE)
- Threshold crossed: pre-2017 (structural BEV advantage: instant torque at 0 RPM)
- 2024 values: 5.5 sec mainstream; 2.8 sec performance tier
- ICE avg midsize 2024: 6.5 sec
- Trajectory: decelerating, R²=0.965; 7.5 (2015) → 6.5 (2018) → 6.0 (2020) → 5.5 (2024)

### Energy Efficiency (energy_efficiency_kWh_100km)
- Threshold: <30 kWh/100km
- Threshold crossed: pre-2015
- 2024 values: USA 17.9 (FuelEconomy.gov); EU 16.4 (ICCT); China 12.2 (DieselNet)
- ICE equivalent: ~67.5 kWh/100km primary energy (7.5 L/100km × 9 kWh/L)
- BEV 3.77x more efficient at primary energy level
- Trajectory: decelerating, R²=0.993; 20.8 (2015) → 19.3 (2019) → 17.9 (2024)

### Maintenance Cost (maintenance_cost_usd_mile)
- Threshold: at or below ICE ($0.101/mile)
- Threshold crossed: ~2015
- 2024 values: EV $0.078/mile vs ICE $0.101/mile (22.8% BEV saving)
- Sources: AAA annual study, U.S. DoE (6.1 vs 10.1 cents/mile)
- Trajectory: decelerating, R²=0.993; $0.090 (2015) → $0.086 (2018) → $0.078 (2024)

### TCO SUV Segment (tco_suv_segment_usd_mile)
- Threshold: at or below ICE-SUV ($0.68/mile)
- Threshold crossed: 2023
- 2024: BEV-SUV $0.61/mile vs ICE-SUV $0.68/mile = 10.3% BEV advantage (Vincentric 2024)
- Trajectory: decelerating, R²=0.995; $0.85 (2018) → $0.76 (2020) → $0.65 (2023) → $0.61 (2024)

### TCO Fleet Average (tco_fleet_avg_usd_mile)
- Threshold: at or below ICE fleet avg ($0.633/mile)
- Status: NOT MET — $0.761/mile vs $0.633/mile = 20.2% BEV premium (2024)
- Trajectory: decelerating, R²=0.972; $0.95 (2019) → $0.85 (2021) → $0.761 (2024)
- Estimated parity year: 2028 [model-derived]
- Blockers: purchase price premium (~$10k), higher insurance (~30% above ICE), faster depreciation (52% vs 39% 3yr)

### Cold Weather Range Retention (cold_weather_range_retention_pct)
- Threshold: ≥70% retention at −7°C/20°F
- Threshold crossed: 2022
- 2024 value: 78% retention (22% loss at −7°C)
- Trajectory: exponential, R²=0.994; 59% (2018) → 64% (2020) → 72% (2022) → 78% (2024)
- Data source: AAA Cold Weather EV Range Study (2019, 2022, 2024 editions) [T3]
- ICE: 100% (no cold-weather fuel loss)

### Battery Longevity (battery_capacity_retention_pct at 100k miles)
- Threshold: ≥80% at 100k miles (≤20% capacity loss)
- Threshold crossed: ~2019
- 2024 value: 90% (10% loss) fleet avg; LFP: 91% (9% loss); NMC Gen3: 88%
- Trajectory: linear, R²=0.924; 70% (2015) → 84% (2019) → 87% (2021) → 90% (2024)
- Data source: Recurrent.com 2024 Battery Degradation Study, 10,000+ vehicles [T3]

### Charging Infrastructure (charging_infra_global_public_chargers)
- Threshold: >500k global public chargers (viable network)
- Threshold crossed: 2018 (550k)
- 2024 value: 5.44M global; 200k USA; 1M+ Europe; 3M+ China
- CAGR 2015–2024: 45.7% (29.6x growth from 184k)
- Trajectory: exponential, R²=0.997 — strongest fit in full EV dimension set
- Source: STDF catalog [T2: Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json]

### Model Variety (model_variety_distinct_bev_models)
- Threshold: 300 distinct models (covers 4+ body styles, 3+ price segments)
- Threshold crossed: 2021 (~350 models)
- 2024 value: ~550 BEV models vs ~1,200 ICE models
- Trajectory: linear, R²=0.987; 60 (2015) → 180 (2018) → 350 (2021) → 550 (2024)
- Remaining gaps: minivan, sub-$20k US entry-level

### Towing Capacity (tow_capacity_lb, pickup segment)
- Threshold: 5,000 lb (mainstream utility; >90% of towers stay below this)
- Threshold crossed: 2022 (F-150 Lightning 7,700 lb, Rivian R1T 7,700 lb)
- 2024 value: 14,000 lb (Ram 1500 REV) — EXCEEDS ICE F-150 max (13,200 lb)
- Trajectory: linear, R²=0.997, n=3; 0 (2019) → 7,700 (2022) → 14,000 (2024)
- CRITICAL compound caveat: at max tow load, range drops to ~160 km (well below 300 km threshold)

### Range Under Max Tow (range_under_max_tow_km) — compound
- Threshold: 300 km at rated tow load (usable towing day)
- Status: NOT MET (structural)
- 2024 value: ~160 km at max rated load (F-150 Lightning at 7,700 lb)
- Best-case single data point: Cybertruck at 3,500 lb ~350 km (close to threshold at mid-load)
- No parity year estimated — structural battery energy density constraint

### L2 ADAS Availability (adas_l2_availability_mn_new_cars_yr)
- Threshold: ≥20M L2 cars sold globally per year
- Threshold crossed: 2021
- 2024 value: 36M L2 cars sold/yr (IDTechEx [T2])
- Trajectory: linear, R²=0.999; 15M (2020) → 26M (2022) → 36M (2024)
- BEV structural advantage: OTA updates enable ADAS upgrades vs ICE hardware-swap requirement

### Vehicle Lifespan (vehicle_lifespan_yrs)
- Threshold: >12 years effective lifespan (match ICE fleet avg)
- Status: MET
- 2024 value: 18–25 yrs estimated [model-derived] for LFP-equipped BEVs (Recurrent 2024)
- ICE: 12–15 years average fleet lifespan
- Battery replacement cost: $8k–15k (NMC); $5k–9k (LFP) — one-time, comparable to engine overhaul

## Overall Convergence Pattern (updated 2026-03-21, third pass)
- 13 of 15 dimensions: threshold MET
- 2 unmet: tco_fleet_avg (est. 2028 [model-derived]), range_under_max_tow_km (structural)
- Convergence type: SEQUENTIAL-CLUSTERED (8-year window 2015–2023)
  - Leading (2015): energy_efficiency, maintenance_cost
  - Middle (2017–2019): acceleration, range_km, charging_infra, charge_time, battery_longevity
  - Late (2021–2023): model_variety, adas_l2, cold_weather, tow_capacity, tco_suv_segment
  - Unmet: tco_fleet_avg, range_under_max_tow_km

### Cargo Space (cargo_space_L, sedan)
- Threshold: ≥450 L (match ICE sedan trunk avg)
- Threshold crossed: pre-2015 (structural frunk advantage from first purpose-built BEV platforms)
- 2024 value: 649 L total (Model 3: 561 rear + 88 frunk) vs ICE 450 L; Model Y 2041 L vs ICE SUV 1800 L
- Trajectory: structural architectural advantage — not time-improving, one-time gain from skateboard platform design
- ICE: 450 L sedan, 1800 L SUV (trunk only)

## lib.capability_math API Signatures (validated 2026-03-23)
- fit_trajectory(years, values) → dict with keys: curve_type, params, r_squared, projected_values
  - curve_type values: 'linear', 'exponential', 'decelerating'
  - NOTE: key is 'r_squared' NOT 'r2'
- threshold_check(current_value, threshold, higher_is_better=True) → dict with keys: status, gap_pct, current, threshold
  - status values: 'MET', 'NOT_MET'
  - NOTE: does NOT accept historical years/values — just current scalar value
- parity_year_estimate(years, values, threshold, higher_is_better=True) → float year or None
- convergence_pattern(dimensions) → str ('simultaneous', 'sequential', 'divergent')
  - dimensions: list of dicts with keys: dimension (str), met_year (int or None), status (str)
  - NOTE: returns 'divergent' when some dimensions have met_year=None; this is accurate but note
    that 7-year sequential window (2015-2022) with 2 structural lags is best described as
    "sequential with structural lags" in prose, not just "divergent"

## Vocabulary / Compliance Notes
- IEA must be tagged: [CAUTION: IEA source — historical data only] wherever cited
- IEA hook: scan_banned_sources() checks per-LINE — each line mentioning IEA must have [CAUTION:] tag
  on the SAME line. Multi-line strings are split and checked line by line.
- "projected" is banned — use "estimated [model-derived]"
- "Outlook" triggers forecast keyword ban — avoid in output files
- BEV classification: Hybrid (dominant Stellar); Jevons Paradox does NOT apply
- Required terms: disruption, stellar energy, cost-curve dynamics, market-driven disruption, incumbent displacement, S-curve adoption — all must appear in output
- Validate draft with: python3 -c "from lib.vocabulary import scan_banned_sources, scan_banned; ..."
  before writing to catch hook violations before the write attempt
