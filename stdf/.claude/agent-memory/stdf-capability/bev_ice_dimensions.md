---
name: BEV vs ICE Capability Dimensions
description: Validated 12-dimension capability framework for BEV vs ICE disruption analysis with thresholds, trajectories, and parity years
type: project
---

## Validated Dimension Set (BEV vs ICE, as of 2024-03-27)

**Jevons classification:** Hybrid (dominant Stellar). Jevons excluded.

### Dimensions That Met Threshold (10 of 12 as of 2024)

| Dimension | BEV 2024 | ICE Baseline | Threshold | Met Year | Curve |
|-----------|----------|-------------|-----------|----------|-------|
| range_km | 455 km | 600–800 km | 350 km | 2022 | exponential, R²=0.987 |
| charge_time_min (10–80% DCFC) | 22 min | 4 min refuel | ≤30 min | 2023 | decelerating, R²=0.997 |
| purchase_price_ratio | 1.07x | 1.00x | ≤1.20x | 2023 | decelerating, R²=0.995 |
| tco_5yr_ratio | 0.85x | 1.00x | ≤1.00x | 2022 | decelerating, R²=0.994 |
| maintenance_cost_per_mile | $0.031 | $0.061 | ≤$0.050 | 2019 | decelerating, R²=0.939 |
| charging_infrastructure_USA | 200k | 150k gas stations | ≥100k | 2020 | exponential, R²=0.994 |
| acceleration_0_100kph | 3.5 sec | 7–8 sec | ≤7.0 sec | 2018 | decelerating, R²=0.995 |
| cold_weather_range_retention | 72% at -15C | 85–90% | ≥70% | 2024 | exponential, R²=0.998 |
| model_availability | 785 models | ~2000+ | ≥200 models | 2021 | exponential, R²=0.996 |
| NVH | Structurally superior | Baseline | At-or-above | 2010 (by design) | N/A |

### APPROACHING Dimensions (2 of 12)

| Dimension | BEV 2024 | Threshold | Est. Met Year | Curve |
|-----------|----------|-----------|--------------|-------|
| battery_energy_density_Wh_kg | 195 Wh/kg | 200 Wh/kg | 2025 | linear, R²=0.983 |
| towing_range_km (max load) | 180 km | 200 km | 2026 | linear, R²=0.995 |

### Key TCO Calculation (USA, 2024)
- BEV: $31,000 + (5yr × 15k mi × $0.04/mi electricity) + (5yr × 15k mi × $0.031/mi maintenance) = $36,325
- ICE: $29,000 + (5yr × 15k mi × $0.12/mi fuel) + (5yr × 15k mi × $0.061/mi maintenance) = $42,575
- BEV saves $6,250 over 5 years; ratio 0.853

### Convergence Pattern
Sequential — final wide-population blocker (cold weather retention) crossed in 2024.
Full parity estimated 2026 (towing range).

**Why:** Validated from full catalog + web research run on 2026-03-27
**How to apply:** Use this dimension set as starting point for any BEV/EV capability analysis; adjust thresholds per market segment (commercial fleet, heavy-duty towing use different thresholds)
