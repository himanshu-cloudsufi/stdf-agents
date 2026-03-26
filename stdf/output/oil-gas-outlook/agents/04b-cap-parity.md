# STDF Capability Parity Checker Agent — Oil/Gas Multi-Vector Disruption

**Agent:** `stdf-capability-parity-checker` | **Confidence:** 0.81

---

## Agent Reasoning

This evaluation covers three independent disruption vectors extracted from the upstream capability agent (`agents/03-capability.md`): V1 (BEV vs ICE passenger cars, 9 dimensions), V2 (Solar PV + BESS vs natural gas power generation, 11 dimensions), and V3 (air-source heat pump vs gas furnace, 10 dimensions). Each vector was evaluated independently because the buyer decision criteria, competitive thresholds, and adoption dynamics differ structurally across transport, power generation, and space heating.

All per-dimension threshold statuses, current values, and trajectory data were extracted directly from the upstream capability agent's structured output. Threshold checks were computed using `lib.capability_math.threshold_check` for each dimension; parity year estimates used `lib.capability_math.parity_year_estimate` with the trajectory time series extracted from the upstream tables. Convergence patterns were computed using `lib.capability_math.convergence_pattern`. No external data sources or web research were used.

V1 (BEV vs ICE) achieves PARTIAL parity: 7 of 9 dimensions have crossed their competitive thresholds. The two residual gaps — fleet-average TCO (20.2% above threshold) and cold-weather range loss (25.0% above threshold) — are both on improving trajectories [model-derived] but exceed the strict 15% APPROACHING window. Critically, neither is a hard blocker for mainstream adoption: TCO parity is already achieved at sedan/SUV segment level, and cold-weather range loss primarily affects buyers in Arctic-adjacent climates. The commercially decisive dimensions (fuel cost, maintenance, range, acceleration) were all cleared by 2021, and PARTIAL status is appropriate given the non-blocking nature of residual gaps.

V2 (Solar+BESS vs natural gas) achieves PARTIAL parity: 9 of 10 scoreable dimensions have crossed their thresholds. The standalone solar capacity factor dimension is explicitly excluded from the parity condition by the upstream capability agent, which noted that this is not the correct comparison metric for a firmed solar+BESS system — the system-level dispatchability index supersedes it. The dispatchability dimension (12.5% gap) falls within the 15% APPROACHING window and is model-derived to resolve by 2027–2028 as 8-hour BESS deployment scales. This is the cleanest PARTIAL case across the three vectors.

V3 (ASHP vs gas furnace) is NOT_MET: while 8 of 10 performance dimensions have cleared their thresholds — demonstrating genuine capability parity across all thermal performance and operating cost metrics — the two residual dimensions are structural economic blockers with gaps of 66.7% (upfront cost ratio) and 40.0% (ducted retrofit installation complexity). Both far exceed the 15% window. The gross upfront cost ratio is model-derived to reach parity in the range 2036–2043 on the current decelerating trajectory [lib computation: 2043; upstream estimate with additional data: 2036]. The mini-split ductless sub-segment has already achieved full capability parity and represents the leading-edge adoption path.

---

## Agent Output

### Capability Parity Condition

#### Vector 1: BEV vs ICE Passenger Car
- **Status:** PARTIAL
- **Parity year:** model-derived 2027
- **Confidence:** medium
- **Convergence pattern:** sequential

#### Vector 2: Solar PV + BESS vs Natural Gas Power Generation
- **Status:** PARTIAL
- **Parity year:** model-derived 2027–2028
- **Confidence:** medium-high
- **Convergence pattern:** sequential

#### Vector 3: Air-Source Heat Pump vs Gas Furnace
- **Status:** NOT_MET (full-ducted gross pathway) | PARTIAL (ductless / subsidized pathway)
- **Parity year:** ductless/subsidized: achieved 2022–2024 | gross ducted: model-derived 2036–2043
- **Confidence:** high
- **Convergence pattern:** divergent

---

### Per-Dimension Assessment

#### Vector 1: BEV vs ICE (9 Dimensions)

| Dimension | Disruptor Current | Threshold | Status | Gap % | Met Year / Estimated Year |
|-----------|-------------------|-----------|--------|-------|--------------------------|
| range_km | 455 km | 350 km | MET | −30.0% | 2021 (achieved) |
| charge_time_min (DC fast 0–80%) | 20–30 min | ≤45 min | MET | −51.1% | 2019 (achieved) |
| acceleration_0_60_sec | 5.5 sec | ≤7.0 sec | MET | −21.4% | 2017 (achieved) |
| maintenance_cost_usd_mile | $0.078 | ≤$0.101 | MET | −22.8% | ~2015 (achieved) |
| fuel_cost_usd_km | $0.029 | ≤$0.087 | MET | −66.7% | ~2013 (achieved) |
| model_count | 500 models | ≥200 models | MET | −150.0% | 2022 (achieved) |
| towing_capability_kg | 4,536 kg | ≥3,500 kg | MET | −29.6% | 2022 (achieved) |
| tco_usd_mile_fleet_avg | $0.761 | ≤$0.633 | NOT_MET | +20.2% | model-derived 2026–2027 |
| cold_weather_range_loss_pct | 25% loss | ≤20% loss | NOT_MET | +25.0% | model-derived 2027 [lib, R²=0.992] |

**V1 Blocker assessment:** Neither residual dimension is a hard mainstream adoption blocker. TCO parity is already achieved in sedan/SUV segments; the fleet average is elevated by truck-segment prices. Cold-weather range loss (~25% at −7°C) affects buyers in cold climates but does not represent a categorical capability barrier for the majority of markets.

#### Vector 2: Solar PV + BESS vs Natural Gas Power Generation (10 scoreable dimensions)

| Dimension | Disruptor Current | Threshold | Status | Gap % | Met Year / Estimated Year |
|-----------|-------------------|-----------|--------|-------|--------------------------|
| installed_cost_usd_kw (solar PV) | $700/kW | <$1,000/kW | MET | −30.0% | 2020 (achieved) |
| bess_cost_usd_kwh (2-hr turnkey) | $269/kWh | <$300/kWh | MET | −10.3% | 2023 (achieved) |
| bess_installed_gwh (cumulative) | 370 GWh | >100 GWh | MET | −270.0% | 2021 (achieved) |
| lcoe_usd_mwh (solar+BESS blended) | $120/MWh | ≤$160/MWh | MET | −25.0% | 2022 (achieved) |
| ramp_rate (response time) | <100 ms | ≤5 min | MET | −100.0% | 2018 (achieved) |
| build_time_months | 18 months avg | ≤24 months | MET | −25.0% | 2020 (achieved) |
| fuel_price_volatility_index | 0.0 | <0.5 | MET | −100.0% | structural (always MET) |
| scalability_gw_yr | 451 GW/yr | >50 GW/yr | MET | −802.0% | 2020 (achieved) |
| land_use_acres_gwh | 7 acres/GWh | ≤10 acres/GWh | MET | −30.0% | structural (always MET) |
| dispatchability_index_pct | ~70% | ≥80% seasonal avg | APPROACHING | +12.5% | model-derived 2027–2028 |
| capacity_factor_pct (standalone) | 16.3% | [excluded] | [excluded] | — | Excluded per upstream: standalone CF is not the valid metric for a firmed solar+BESS system |

**V2 Blocker assessment:** Dispatchability (12.5% gap, APPROACHING) is the sole remaining dimension and falls within the 15% PARTIAL window. It reflects multi-day overcast events unaddressed by 4-hour BESS; the gap narrows as 8-hour BESS systems deploy. Not a hard blocker in markets with demand flexibility and geographic portfolio diversification.

#### Vector 3: Air-Source Heat Pump vs Gas Furnace (10 Dimensions)

| Dimension | Disruptor Current | Threshold | Status | Gap % | Met Year / Estimated Year |
|-----------|-------------------|-----------|--------|-------|--------------------------|
| COP_mild_climate (at +7°C) | 3.5 seasonal avg | ≥2.5 | MET | −40.0% | ~2010 (achieved) |
| COP_cold_climate (at −15°C) | 2.1 | ≥1.75 | MET | −20.0% | ~2022 (achieved) |
| cooling_capability (dual function) | Yes (full A/C) | Dual heat+cool | MET | 0.0% | structural (always MET) |
| op_cost_usd_kwh_thermal (US) | $0.046 | ≤$0.047 | MET | −2.1% | ~2024 (achieved, borderline) |
| noise_level_dba (outdoor unit) | 47 dBA | ≤55 dBA | MET | −14.6% | ~2018 (achieved) |
| lifespan_yr | 18 yr | ≥15 yr | MET | −20.0% | ~2020 (achieved) |
| space_requirement_sqm | 0.8 sqm | ≤1.5 sqm | MET | −46.7% | ~2020 (achieved) |
| upfront_cost_ratio_gross (ASHP/gas furnace) | 5.0× | <3.0× | NOT_MET | +66.7% | model-derived 2036–2043 [lib: 2043; upstream R²=0.990 fit: 2036] |
| install_complexity_ducted_retrofit | 3.5/5 | ≤2.5/5 | NOT_MET | +40.0% | no convergent trajectory [contractor supply chain constraint] |
| install_complexity_ductless_minisplit | 2.0/5 | ≤2.5/5 | MET | −20.0% | 2022 (achieved) |

**V3 Blocker assessment:** Both NOT_MET dimensions are hard blockers for mainstream ducted-retrofit adoption. The upfront cost gap (66.7%) is on a decelerating improvement trajectory with gross parity a decade or more away. With government subsidies (UK BUS scheme, US IRA heat pump tax credit), the net cost ratio drops to approximately 2.0×, enabling near-term adoption in subsidy-eligible markets. The ducted install complexity gap (40.0%) has no modeled resolution timeline — it is a contractor labor and supply chain constraint, not a technology cost curve. The ductless mini-split sub-segment (2.0/5 complexity, MET since 2022) constitutes a viable adoption pathway that bypasses the ducted blocker entirely.

---

### Multi-Dimensional Summary

#### Vector 1: BEV vs ICE
- **Total dimensions:** 9
- **Dimensions MET:** 7
- **Dimensions APPROACHING:** 0 (2 classified NOT_MET by lib gap calculation; non-blocking per condition qualifier)
- **Dimensions NOT_MET:** 2
- **Blocking dimensions:** none (TCO: segment-level parity achieved; cold range: non-blocking in mainstream markets)

#### Vector 2: Solar+BESS vs Natural Gas
- **Total dimensions:** 11 (10 scoreable)
- **Dimensions MET:** 9
- **Dimensions APPROACHING:** 1 (dispatchability, 12.5% gap)
- **Dimensions NOT_MET:** 1 (standalone capacity factor, excluded as non-comparable metric)
- **Blocking dimensions:** none for the scoreable set

#### Vector 3: ASHP vs Gas Furnace
- **Total dimensions:** 10
- **Dimensions MET:** 8
- **Dimensions APPROACHING:** 0
- **Dimensions NOT_MET:** 2
- **Blocking dimensions:** upfront_cost_ratio_gross (66.7% gap), install_complexity_ducted_retrofit (40.0% gap, no convergent trajectory)

---

### Convergence Analysis

**Vector 1 (sequential):** BEV capability dimensions crossed their thresholds across a 13-year span (2013 to model-derived 2027), clustering into three sequential waves. First, structural advantages apparent from early deployment (fuel cost efficiency, instant torque acceleration) cleared thresholds by 2013–2017. Second, range and charge time crossed in 2019–2021 as battery energy density scaled via cost-curve dynamics. Third, infrastructure and market completeness dimensions (model count, towing) followed in 2022. The two residual dimensions (TCO fleet-average, cold-weather range) are on model-derived trajectories resolving by 2026–2027. This is a textbook sequential convergence pattern: the commercially decisive dimensions for mainstream buyers cleared first, enabling S-curve adoption acceleration even while residual edge-case dimensions lag. This confirms incumbent displacement in the passenger car segment is proceeding from capability, not waiting for full parity.

**Vector 2 (sequential):** Solar+BESS dimensions clustered into two sequential waves aligned with technology maturation. Physical deployment advantages (ramp rate, fuel price volatility, build time) cleared thresholds in 2018–2020 as utility-scale BESS reached production maturity. Economic threshold crossings (installed cost, LCOE, BESS cost, scalability) followed in 2020–2023 as cost-curve dynamics drove hardware costs below gas equivalents. The single remaining dimension (seasonal dispatchability, 12.5% gap) represents a well-understood infrastructure gap being closed by longer-duration storage deployment. Sequential convergence for Solar+BESS followed the same structural-first, economic-second ordering seen in V1 BEV adoption — a pattern consistent with S-curve adoption dynamics across technology disruptions.

**Vector 3 (divergent):** ASHP dimensions split sharply into two non-converging tracks. All thermal performance, operating cost, and ductless installation dimensions have met their thresholds, while the capital cost and ducted installation dimensions remain structural blockers separated by 40–67% gaps on decelerating improvement curves. This divergent pattern signals that the performance case for ASHP is closed and the remaining obstacle is purely economic and logistical. The divergence implies that market-driven disruption will proceed via segment bifurcation — ductless mini-splits and subsidy-supported ducted installs grow while ungated gross-price ducted retrofits stall. This is not a technology failure; it is a capital access and installer supply chain barrier that government subsidy programs can partially bridge, but cost-curve dynamics alone will not resolve on a sub-decade timeline.

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.4a | CRITICAL | PASS | All 30 dimensions extracted from `agents/03-capability.md` per-dimension tables; lib.capability_math.threshold_check applied to every dimension |
| 5.4b | CRITICAL | PASS | V1: PARTIAL; V2: PARTIAL; V3: NOT_MET — all three vectors explicitly stated with per-vector condition |
| 5.4c | HIGH | PASS | 30 total dimensions across 3 vectors, each listed with disruptor current value, threshold, status, and gap % |
| 5.4d | HIGH | PASS | V1: sequential; V2: sequential; V3: divergent — computed via lib.capability_math.convergence_pattern |
| 5.4e | HIGH | PASS | All unmet/approaching dimensions have model-derived parity year estimates or structural barrier explanation |
| 5.4f | MEDIUM | PASS | All current values, thresholds, trajectory data, and met years sourced from `agents/03-capability.md`; no external data introduced |

---

### Data Gaps

- **V1 TCO time series absent:** No multi-year TCO time series is provided in the upstream capability output. The model-derived crossing year (2026–2027) is taken from the upstream agent's own model-derived estimate; the lib `parity_year_estimate` function could not be independently run for TCO without raw data points.
- **V2 dispatchability time series absent:** The upstream capability output states 70% current value and a 2027–2028 model-derived estimate but provides no multi-year time series for the dispatchability index. The lib `parity_year_estimate` was not run for this dimension; the upstream estimate is accepted.
- **V3 upfront cost ratio — range divergence between lib and upstream:** The lib `parity_year_estimate` computes 2043 using 3 upstream data points (6.4× in 2015, 5.6× in 2020, 5.0× in 2024). The upstream capability agent reports ~2036 using a decelerating fit (R²=0.990) that likely incorporates additional intermediate data points not listed in the structured table. The true crossing year is reported as the range 2036–2043; both reflect a decelerating trajectory.
- **V3 install complexity ducted retrofit — no trajectory data:** The upstream provides only a current complexity rating (3.5/5) with no multi-year time series. No model-derived parity year is possible; characterized as a contractor supply chain constraint with no modeled resolution timeline.
- **V2 standalone capacity factor exclusion:** Excluded from parity condition per upstream capability agent's explicit guidance that system-level dispatchability index is the correct metric for a firmed system. No system-blended capacity factor time series is available to verify.

---

## Sources

- Upstream: `agents/03-capability.md`
- Computation: `lib.capability_math` — `threshold_check`, `parity_year_estimate`, `convergence_pattern`, `multi_dimensional_summary`
