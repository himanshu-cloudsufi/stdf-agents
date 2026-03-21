---
name: bev_ng_truck_china_benchmarks
description: Validated BEV vs LNG/NG heavy truck capability benchmarks for China, all 11 dimensions with thresholds and trajectories (validated 2026-03-19)
type: reference
---

## BEV vs LNG Heavy-Duty Trucks, China — Capability Dimension Reference (validated 2026-03-19)

**Segment:** Class 8 equivalent (>14t GVW) tractor-trailers, China market
**Disruptor:** BEV (LFP battery, primarily XCMG/SANY/FAW/CATL platform)
**Incumbent:** LNG/CNG heavy trucks

### Range — Urban (range_km_urban)
- Threshold: 300 km (urban/regional routes, mainstream viability)
- Threshold crossed: 2022
- 2024 BEV value: 400 km (282–423 kWh pack, 140 kWh/100km at 40t GVW)
- LNG 2024: 800–1,000 km
- Trajectory: 120 (2018) → 200 (2020) → 280 (2022) → 400 (2024); exponential R²=0.98

### Range — Long-Haul (range_km_longhaul)
- Threshold: 500 km (long-haul corridors, eliminates refuel stop outside driver rest)
- Threshold NOT YET MET (gap: 20% in 2024)
- Curve-fitted crossing year: 2026
- Same trajectory as urban range above

### Payload Penalty (payload_penalty_t)
- Threshold: <1.5t below LNG equivalent (commercial insignificance for most operators)
- 2024 BEV value: ~2.0t penalty
- Trajectory: −4.5t (2020) → −3.0t (2022) → −2.5t (2023) → −2.0t (2024); decelerating R²=0.98
- Curve-fitted crossing year: 2025
- China NEV trucks get +2t GVW allowance (46t vs 44t) partly offsetting technical penalty

### Refueling/Recharging Time (refuel_min)
- Threshold: <30 min
- Met via plug-in fast charge: ~2022 (DC 250 kW → 30 min; Huawei 1.44 MW → 20 min in 2024)
- Met via battery swap: 2022 (3–5 min; CATL EVOGO 100 seconds)
- Trajectory: 120 min (2018) → 60 min (2021) → 20 min (2024); decelerating R²=0.99
- LNG: 15–20 min — matched by both BEV pathways

### Energy Efficiency (energy_efficiency_pct)
- Threshold: >50% tank-to-wheel
- Met well before 2015 (structural BEV advantage)
- 2024 BEV: 87–90% vs LNG: 35–40%
- Primary energy consumption: BEV 155.6 kWh/100km vs LNG 234 kWh/100km at 40t GVW (33.5% BEV advantage)

### Lifecycle Emissions (lifecycle_reduction_pct)
- Threshold: >50% lifecycle reduction vs diesel baseline
- Threshold crossed: 2024
- 2024 BEV: 90 g CO2e/tonne-km = 59% reduction vs diesel (220 g)
- 2024 LNG: 180 g CO2e/tonne-km = 18% reduction (includes methane slip at 2.3%)
- BEV trajectory: 115 (2018) → 95 (2022) → 90 (2024) g CO2e/tonne-km; decelerating R²=0.98

### Noise (noise_dba)
- Threshold: <72 dBA at 50 kph (urban night delivery permit level)
- Met: structural BEV advantage from first deployment (2018)
- 2024 BEV: ~66 dBA; LNG: ~82 dBA
- Commercial implication: BEV gets night delivery windows; 15–20% higher urban fleet utilization

### Torque/Gradeability (gradeability_pct)
- Threshold: >25% grade (construction, mountain, port access)
- Met: structural BEV advantage from first deployment
- 2024 BEV: >30%; LNG: 20–22%

### Cold Weather Range Retention (cold_retention_pct at -10C)
- Threshold: >85% retention (<15% range loss at -10°C)
- 2024 BEV: 82% retention (APPROACHING, gap 3.5%)
- Curve-fitted crossing year: 2025
- Trajectory: 65% (2018) → 72% (2021) → 82% (2024); exponential R²=0.996
- Geographic note: blocker only in NE China (~15% of freight routes); Central/South China effectively met already

### Infrastructure — Battery Swap Density (swap_stations_per_50km)
- Threshold: ≥1 station per 50km on major freight corridors
- 2024: ~2,000 stations total; 0.77/50km network-wide; ~1.0+ on major routes
- Swap station trajectory: 200 (2022) → 800 (2023) → 2,000 (2024); exponential R²=0.99
- Curve-fitted crossing year for full network (2,600 stations): 2025
- LNG: 6,500 stations; 2.5/50km corridor
- CATL announced 1,000 new swap stations in 2025

### Battery Warranty (warranty_km)
- Threshold: >500,000 km or 8 years
- Threshold crossed: 2022
- 2024 BEV: 500k–1.5M km (CATL pre-lithiation LFP)
- Trajectory: 150k (2018) → 300k (2020) → 500k (2022) → 1,500k (2024); exponential R²=0.98

### Overall Convergence Pattern
- 7 of 11 dimensions: threshold met
- Convergence type: SEQUENTIAL → approaching simultaneous terminal phase
- Urban/regional segment: FULL PARITY since 2022
- Long-haul segment: full parity crossing-year estimate 2026
- Blocking dimensions resolving 2025–2026: range_km_longhaul, payload_penalty_t, infrastructure_swap_full_network

### Key Data Sources
- ICCT ZE-MHDV China 2024 report (March 2025)
- CATL EVOGO battery swap specs (2022, 2024)
- China catalog: Commercial_Vehicle_(EV)_Annual_Sales_China.json, Lithium_Ion_Battery_Pack_Battery_Energy_Density_China.json, Passenger_Vehicle_(EV)_Public_Charging_Points_China.json
- BEV commercial vehicle sales China 2024: 380,250 units (exponential R²=0.98)
- Heavy truck BEV market share: 13% full-year 2024; 20.9% in December 2024
