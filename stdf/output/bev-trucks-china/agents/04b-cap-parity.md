# STDF Capability Parity Checker Agent — BEV vs LNG/NG Heavy Trucks, China

**Agent:** `stdf-capability-parity-checker` | **Confidence:** 0.72

**Analysis date:** 2026-03-20 | **Upstream:** `03-capability.md`

---

## Agent Reasoning

The upstream capability output (`03-capability.md`) assessed 11 performance dimensions comparing BEV heavy trucks against LNG/NG incumbents in China's >14t GVW tractor-trailer segment. All 11 dimensions were extracted using `lib.upstream_reader.get_capability_dimensions`, yielding per-dimension current values, thresholds, and trajectory data. Seven dimensions returned MET status from the capability agent (range_km_urban, refuel_recharge_time_min, energy_efficiency_pct, lifecycle_emissions_pct_reduction, noise_dba, torque_gradeability_pct, battery_warranty_km). Three returned NOT_MET (range_km_longhaul, payload_penalty_t, infrastructure_swap_per_50km) and one returned APPROACHING (cold_weather_range_retention_pct).

Formal threshold checks using `lib.capability_math.threshold_check` confirmed these designations and quantified gap percentages: range_km_longhaul at 20.0%, payload_penalty_t at 33.3%, infrastructure_swap_per_50km at 23.0%, and cold_weather_range_retention_pct at 3.5%. Parity year estimates via `lib.capability_math.parity_year_estimate` derived curve-fitted crossing years of 2026 for range_km_longhaul, 2026 for payload_penalty_t, 2025 for infrastructure_swap_per_50km, and 2026 for cold_weather_range_retention_pct. Applying the aggregate condition logic: met count is 7 of 11 (below the 2/3 threshold of 7.33), and all three NOT_MET dimensions carry gaps exceeding 15% — each condition independently triggers NOT_MET status. The convergence pattern is classified as divergent by `lib.capability_math.convergence_pattern`, reflecting the wide spread between early-crossing structural dimensions (efficiency, torque, noise — met 2015) and the 2025–2026 cluster of remaining blockers. A critical segment note from upstream must be carried through: the urban/regional sub-segment (<300 km/day routes) achieved full capability parity in 2022 across all relevant dimensions; the NOT_MET determination applies specifically to the long-haul full-network parity condition.

---

## Agent Output

### Capability Parity Condition

- **Status:** NOT_MET
- **Parity year:** curve-fitted 2026 (long-haul full-network parity; last dimensions: range_km_longhaul and payload_penalty_t)
- **Confidence:** medium
- **Convergence pattern:** sequential (urban parity 2022; 3-blocker cluster resolving 2025–2026; structural advantages met 2015)
- **Segment qualification:** urban/regional (<300 km/day) — full capability parity MET since 2022; long-haul (>500 km/day) — NOT_MET, curve-fitted crossing 2026

---

### Per-Dimension Assessment

| Dimension | Disruptor Current | Threshold | Status | Gap % | Parity Year |
|-----------|-------------------|-----------|--------|-------|-------------|
| energy_efficiency_pct | 88.5% tank-to-wheel | >50% | MET | 0% | 2015 (achieved) |
| noise_dba | 66 dBA at 50 kph | <72 dBA | MET | 0% | 2015 (achieved) |
| torque_gradeability_pct | 30%+ grade | >25% grade | MET | 0% | 2015 (achieved) |
| refuel_recharge_time_min | 4 min (battery swap) | <30 min | MET | 0% | 2022 (achieved) |
| range_km_urban | 400 km | 300 km | MET | 0% | 2022 (achieved) |
| battery_warranty_km | 1,500,000 km | >500,000 km | MET | 0% | 2022 (achieved) |
| lifecycle_emissions_pct_reduction | 59% below diesel | >50% | MET | 0% | 2024 (achieved) |
| cold_weather_range_retention_pct | 82% at -10C | >85% | APPROACHING | 3.5% | curve-fitted 2026 |
| range_km_longhaul | 400 km | 500 km | NOT_MET | 20.0% | curve-fitted 2026 |
| infrastructure_swap_per_50km | 0.77 stations/50km | >=1.0/50km | NOT_MET | 23.0% | curve-fitted 2025 |
| payload_penalty_t | -2.0t vs LNG | <1.5t gap | NOT_MET | 33.3% | curve-fitted 2026 |

---

### Multi-Dimensional Summary

- **Total dimensions:** 11
- **Dimensions MET:** 7
- **Dimensions APPROACHING:** 1 (cold_weather_range_retention_pct, gap 3.5%)
- **Dimensions NOT_MET:** 3
- **Blocking dimensions:** range_km_longhaul, payload_penalty_t, infrastructure_swap_per_50km

---

### Convergence Analysis

The 11 dimensions crossed or are crossing thresholds in a sequential pattern spanning over a decade. The first cluster — energy_efficiency_pct, noise_dba, and torque_gradeability_pct — represent structural physics advantages that BEV held from first deployment (curve-fitted met year: ~2015), requiring no trajectory improvement. The second cluster — range_km_urban, refuel_recharge_time_min (via battery swap), and battery_warranty_km — crossed their thresholds in 2022 as LFP battery cost-curve dynamics enabled viable pack sizes and CATL's cell chemistry advances unlocked longevity. lifecycle_emissions_pct_reduction crossed in 2024 as China's grid carbon intensity fell to the level where the BEV lifecycle advantage exceeded the 50% threshold. The remaining four dimensions (including the APPROACHING cold_weather dimension) cluster tightly in 2025–2026, all driven by the same underlying LFP battery cost-curve dynamics: larger packs close the range gap, lighter cell-to-pack structures shrink payload penalty, and exponential swap-station buildout closes the infrastructure gap. The pattern implies adoption timing is already bifurcated: urban/regional incumbent displacement is underway — driven by market-driven disruption economics, not mandate effects — with BEV reaching 13% share in 2024 (20.9% in December 2024), while long-haul S-curve adoption is in its early-growth phase and the trajectory implies acceleration once the 2026 full-parity crossing is reached. The market-driven disruption of LNG/NG incumbents by BEV follows the same cost-curve dynamics pattern observed in stellar energy and passenger BEV sectors: structural performance advantages clear first, infrastructure and range close on an exponential curve, and adoption inflects before full-dimensional parity is technically achieved.

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.4a | CRITICAL | PASS | All 11 dimensions extracted from 03-capability.md with threshold status via lib.upstream_reader |
| 5.4b | CRITICAL | PASS | Status: NOT_MET (7/11 MET; 3 gaps >15%) |
| 5.4c | HIGH | PASS | 11 dimensions listed with current values, thresholds, gap %, and status |
| 5.4d | HIGH | PASS | Convergence: sequential (structural advantages 2015 → urban cluster 2022 → 3-blocker cluster 2025–2026) |
| 5.4e | HIGH | PASS | All 4 non-MET dimensions carry curve-fitted crossing years (2025 or 2026); MET dimensions carry achieved years |
| 5.4f | MEDIUM | PASS | All figures sourced from 03-capability.md; computation via lib.capability_math |

---

### Data Gaps

- **Payload penalty trajectory (MEDIUM confidence):** No primary aggregate OEM data exists on payload penalty by year; values in upstream derived from battery energy density catalog combined with cell-to-pack architecture estimates. Actual 2024 value may range 1.5–2.5t; if already at 1.5t, payload dimension would reclassify to MET and aggregate condition would shift toward PARTIAL.
- **Cold weather retention (MEDIUM confidence):** Upstream data extrapolated from general LFP cold performance characteristics to Chinese-market truck configurations. Actual retention may differ by plus or minus 2–5 percentage points.
- **Infrastructure swap distribution (MEDIUM confidence):** Station density modeled as uniform across highway network; major freight corridor density (~1.0+/50km) already meets threshold per upstream, but secondary highway coverage lags. Full-network NOT_MET designation reflects the average, not major-corridor status.
- **Convergence pattern library output:** `lib.capability_math.convergence_pattern` returned "divergent" based on the wide spread of met_year values (2015 through curve-fitted 2026). The narrative pattern is more precisely described as sequential with a terminal simultaneous cluster; this distinction is preserved in the analysis.

---

## Sources

- Upstream: `output/bev-trucks-china/agents/03-capability.md`
- Computation: `lib.capability_math.threshold_check`, `parity_year_estimate`, `convergence_pattern`, `multi_dimensional_summary`
- Parsing: `lib.upstream_reader.read_upstream`, `get_capability_dimensions`
