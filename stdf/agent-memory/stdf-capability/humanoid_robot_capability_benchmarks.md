---
name: humanoid_robot_capability_benchmarks
description: Validated humanoid robot capability thresholds, trajectories, and dimension definitions for logistics/warehouse disruption analysis (validated 2026-03-19)
type: project
---

Humanoid robots (Atlas, Optimus Gen2, Figure 02, Unitree H1, Agility Digit, Apptronik Apollo) reach capability parity vs. incumbents (human workers / industrial robots) across 8 dimensions for logistics/warehouse use case as of 2024–2025.

**Why:** Simultaneous convergence pattern (7 of 8 dimensions in 2023–2024 window) signals S-curve adoption entry point. Key finding for downstream cost and adoption agents.

**How to apply:** Use these threshold values and trajectory data points when revisiting humanoid robot analysis. Confidence ceiling is 0.72 — bounded to logistics/warehouse segment. Precision assembly and home assistance not yet at parity.

## Competitive Thresholds (Logistics/Warehouse)

| Dimension | Threshold | Crossed | Curve | R² |
|-----------|-----------|---------|-------|----|
| locomotion_speed_m_s | 1.4 m/s | 2019 | exponential | 0.995 |
| payload_kg | 20 kg | 2022 | linear | 1.000 |
| endurance_hr | 4.0 hr | 2024 (boundary) | exponential | 0.992 |
| dexterity_hand_dof | 16 DoF | 2022 | exponential | 0.995 |
| autonomy_task_horizon_s | 1,800 s | 2024–2025 | exponential | 0.999 |
| versatility_task_count | 10 categories | 2024 | exponential | 0.996 |
| safety_collision_speed_m_s | 0.25 m/s | 2024 | decelerating | 0.987 |
| throughput_picks_hr | 35 picks/hr | 2024 | exponential | 0.996 |

## Key Trajectory Data Points

- Locomotion: 1.0 (2016) → 1.5 (2018) → 1.8 (2020) → 2.5 (2022) → 3.3 (2024) m/s
- Payload: 10 (2018) → 15 (2020) → 20 (2022) → 25 (2024) kg
- Endurance: 0.5 (2018) → 1.0 (2019) → 1.5 (2021) → 2.0 (2022) → 4.0 (2024) hr
- Dexterity: 4 (2013) → 7 (2016) → 10 (2018) → 12 (2020) → 16 (2022) → 22 (2024) DoF
- Autonomy: 2 (2019) → 9 (2020) → 23 (2021) → 36 (2022) → 540 (2023) → 2340 (2024) → 8220 (2025) s
- Versatility: 2 (2016) → 3 (2018) → 5 (2020) → 8 (2022) → 15 (2024) task categories
- Safety: 0.50 (2018) → 0.35 (2020) → 0.28 (2022) → 0.22 (2024) m/s
- Throughput: 10 (2020) → 15 (2021) → 20 (2022) → 30 (2023) → 40 (2024) picks/hr

## Platform Reference (2024)
- Unitree H1: 3.3 m/s walk, 30 kg payload, <4 hr battery
- Tesla Optimus Gen2: 2.24 m/s, 20 kg, ~2 hr, 22 DoF hands
- Atlas electric: ~2.5 m/s, 25 kg, ~1 hr
- Figure 02: 25 kg, 16 DoF, revenue-generating Dec 2024
- Apptronik Apollo: 0.94 m/s, 25 kg, 4 hr (hot-swap), ISO-compliant safety
- Agility Digit: ~1.5 m/s, 16 kg, 8 hr (swap), 100k+ totes deployed (Amazon)

## Data Sources
- METR HCAST benchmark — best autonomy time series (T1, Stanford AI Index 2024)
- T2 catalog: data/artificial_intelligence/capability/ (autonomy_task_horizon)
- T2 catalog: data/robot/adoption/ (market context)
- T3 web: manufacturer spec pages, The Robot Report, IEEE Spectrum

## Structural Caveats
- Endurance at boundary: 0% margin, requires battery-swap infrastructure
- Throughput: threshold set at logistics economics floor (35 picks/hr), NOT human parity (80–120 picks/hr)
- Precision assembly: thresholds not met — different analysis required
- Safety curve is decelerating (not exponential) — approaching physical ISO floor
