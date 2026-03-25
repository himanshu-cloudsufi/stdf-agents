# STDF Capability Parity Checker Agent — Lithium-Ion vs Lead-Acid: Capability Parity Condition

**Agent:** `stdf-capability-parity-checker` | **Confidence:** 0.84

**Analysis Date:** 2026-03-20

---

## Agent Reasoning

The capability agent's output (`03-capability.md`) covers 13 dimensions across five application segments — automotive SLI, telecom UPS, datacenter UPS, stationary industrial backup, and forklift/motive power. The upstream analysis identifies 11 of 13 dimensions as meeting their competitive thresholds, with two binding blockers remaining: (1) SLI battery unit cost, where LFP at $100/unit (China) and $180/unit (USA) is 4x and 3.3x above lead-acid at $25 and $55 respectively; and (2) recycling rate, where Li-ion at 30% sits 57.1% below the 70% regulatory procurement threshold. All other 11 dimensions — energy density, cycle life, round-trip efficiency, self-discharge, operating temperature (mainstream climates), charge rate, cost per kWh (stationary), levelized cost per cycle, weight, calendar life, and maintenance — have crossed their competitive thresholds, with the earliest crossings occurring before 2010 and the latest around 2020.

Evaluation logic: 11/13 dimensions are MET (84.6%), which exceeds the 2/3 threshold required for PARTIAL status. The two below-threshold dimensions carry gap percentages of 140% (SLI USA unit cost), 300% (SLI China unit cost), and 57.1% (recycling rate) — all far beyond the 15% APPROACHING proximity condition. However, this is a segmented market where the two blocking dimensions apply exclusively to the automotive SLI segment, not to the four other segments where full capability parity was achieved by 2019-2021. The correct ruling is **PARTIAL**: the disruptor is functionally viable for the majority of lead-acid applications and the market-driven disruption is already underway in telecom, datacenter, stationary backup, and forklift markets. S-curve adoption is visibly underway in all non-SLI segments. Incumbent displacement in automotive SLI is gated by unit cost and recycling infrastructure — both driven by cost-curve dynamics with model-derived crossing years of 2027-2031 depending on geography.

The convergence pattern is **sequential** across three temporal clusters. The `lib.capability_math.convergence_pattern` function returns "divergent" because met_year values span more than five years (pre-2010 to 2031), but this is a multi-cluster sequential pattern — not a genuine two-track divergence. Cluster 1 (pre-2010 to ~2014) captures structural physics advantages of Li-ion chemistry. Cluster 2 (2014-2020) captures operational and economic dimensions that enabled commercial incumbent displacement in cycling applications. Cluster 3 (2027-2031) captures the remaining price and regulatory infrastructure barriers specific to the automotive SLI mass market.

---

## Agent Output

### Capability Parity Condition

- **Status:** PARTIAL
- **Parity year:** 2019-2021 (achieved, non-SLI segments); model-derived crossing 2027-2028 (automotive SLI USA/Europe); model-derived crossing 2030-2031 (automotive SLI China)
- **Confidence:** medium-high (0.84)
- **Convergence pattern:** sequential (3-cluster; lib classification "divergent" overridden — see Convergence Analysis)

### Per-Dimension Assessment

| Dimension | Disruptor Current | Threshold | Status | Gap % | Achieved / Model-Derived Crossing |
|-----------|------------------|-----------|--------|-------|----------------------------------|
| energy_density_Wh_kg | 195 Wh/kg | >80 Wh/kg | MET | 0% | pre-2010 (achieved) |
| cycle_life_cycles | 5,000 cycles | ≥2,000 cycles | MET | 0% | 2017 (achieved) |
| round_trip_efficiency_pct | 97.5% | >90% | MET | 0% | ~2010 (achieved) |
| self_discharge_pct_month | 1.0%/month | <3%/month | MET | 0% | ~2014 (achieved) |
| operating_temp_mainstream | −20°C to +60°C discharge | −20°C to +50°C | MET | 0% | ~2020 (achieved) |
| charge_rate_C | 3.0C | ≥1C | MET | 0% | ~2016 (achieved) |
| cost_per_kwh_upfront_USD | $115/kWh | <$200/kWh | MET | 0% | ~2018-2019 (achieved) |
| levelized_cost_per_cycle | $0.023/kWh/cycle | <$0.60/kWh/cycle | MET | 0% | ~2014 (achieved) |
| weight_kg_per_kwh | 5.8 kg/kWh | <10 kg/kWh | MET | 0% | pre-2010 (achieved) |
| calendar_life_yr | 13.5 years | ≥10 years | MET | 0% | ~2020 (achieved) |
| maintenance_hrs_yr | 0.1 hrs/yr | <0.5 hrs/yr | MET | 0% | ~2018 (achieved) |
| SLI_unit_cost_USD (USA) | $180/unit | ≤$75/unit | NOT_MET | 140.0% | model-derived 2027-2028 |
| SLI_unit_cost_USD (China) | $100/unit | ≤$25/unit | NOT_MET | 300.0% | model-derived 2030-2031 |
| recycling_rate_pct | 30% | ≥70% | NOT_MET | 57.1% | model-derived ~2029 |

**Note on dimension count:** The upstream capability agent scores 13 dimensions; SLI unit cost is split here into regional variants (USA and China) to reflect materially different thresholds and crossing timelines, bringing the count to 14. The upstream 11/13 MET result is confirmed — both regional SLI cost variants are NOT_MET, consistent with the upstream blocker list.

### Multi-Dimensional Summary

- **Total dimensions (including regional split):** 14
- **Dimensions MET:** 11 (78.6%)
- **Dimensions APPROACHING:** 0
- **Dimensions NOT_MET:** 3 (SLI_unit_cost_USA, SLI_unit_cost_China, recycling_rate_pct)
- **Blocking dimensions:** SLI_unit_cost (automotive SLI only), recycling_rate_pct (EU/regulated-market procurement)

**Per-application segment status:**

| Segment | Applicable Dims | MET | Status | Achieved / Model-Derived Year |
|---------|----------------|-----|--------|-------------------------------|
| Telecom UPS | 11 | 11 | MET | 2021 (achieved) |
| Datacenter UPS | 11 | 11 | MET | 2021 (achieved) |
| Stationary industrial backup | 11 | 11 | MET | 2020 (achieved) |
| Forklift / motive power | 11 | 11 | MET | 2019 (achieved) |
| Automotive SLI (USA/Europe) | 13 | 10 | PARTIAL | model-derived crossing 2027-2028 |
| Automotive SLI (China) | 13 | 10 | PARTIAL | model-derived crossing 2030-2031 |

### Convergence Analysis

Dimensions crossed their competitive thresholds in three sequential clusters, driven by cost-curve dynamics at each stage. Cluster 1 (pre-2010 to ~2014) includes the structural physics advantages of Li-ion — energy density, weight, round-trip efficiency, and self-discharge — which were met from early commercial LFP deployment and represent baseline Li-ion chemistry superiority, not a capability trajectory requiring convergence. Cluster 2 (2014-2020) captured operational and economic dimensions: levelized cost per cycle (2014), charge rate (2016), cost per kWh upfront (2018-2019), maintenance (2018), and calendar life (2020). The crossing of this cluster is what enabled S-curve adoption inflection in telecom, datacenter, and forklift markets around 2018-2021 — incumbent displacement was unlocked by economics, not electrochemistry. Cluster 3 (2027-2031) is the price and regulatory infrastructure phase: SLI unit cost must fall from $100-180/unit to $25-75/unit via continued cost-curve dynamics, and recycling rate must climb from 30% to 70% via infrastructure build-out. These are not technical barriers — they are manufacturing scale and end-of-life infrastructure constraints with fixed lead times decoupled from cell chemistry improvements. The sequential structure implies that the automotive SLI disruption clock runs on factory output economics and regulatory enforcement schedules, not on further electrochemical development.

The lib function `convergence_pattern` returns "divergent" because met_year values span over five years (pre-2010 to 2031). This is a known library behavior for multi-cluster sequential patterns (see agent memory: `project_convergence_patterns.md`). The classification is overridden to "sequential" based on the three-cluster structure observed in the data. This is not a genuine two-track divergence (as seen in the ASHP heating case where two tracks have no expected convergence) — all three clusters are on converging trajectories; they simply resolve on different timescales.

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.4a | CRITICAL | PASS | All 13 upstream dimensions extracted with threshold status; regional SLI split documented |
| 5.4b | CRITICAL | PASS | Status: PARTIAL — explicitly stated with segment-level justification |
| 5.4c | HIGH | PASS | 14 dimension rows with current value, threshold, gap %, and MET/NOT_MET status |
| 5.4d | HIGH | PASS | Convergence: sequential (3-cluster); lib "divergent" label noted and overridden with rationale |
| 5.4e | HIGH | PASS | All MET dims have achieved years; NOT_MET dims have model-derived crossing years from upstream |
| 5.4f | MEDIUM | PASS | All figures sourced to `03-capability.md`; no independent data introduced by this agent |

### Data Gaps

- **SLI USA unit cost crossing year:** `lib.capability_math.parity_year_estimate` returns 2025 when run on the China-based LFP SLI trajectory ($100 current, threshold $75). This underestimates because the USA current price is $180/unit, not $100/unit. The upstream capability agent's regional decelerating fit gives 2027-2028 for USA and is adopted here as the more accurate model-derived estimate.
- **Recycling rate regional divergence:** The 30% global average and ~2029 crossing year may diverge regionally post-2026. EU regulatory enforcement is likely to accelerate recycling investment; China may lag given a different regulatory schedule. Global average used throughout.
- **Cold-climate SLI (extreme cold, below −20°C):** R²=0.900 for cold lower-bound trajectory — below the 0.95 preferred threshold. Cold-climate SLI crossing timing (2028-2032) carries higher uncertainty than other model-derived years, per upstream capability agent's data gap disclosure.

---

## Sources

- Upstream: `output/lead-demand-decline/agents/03-capability.md`
- lib functions: `lib.capability_math.threshold_check`, `lib.capability_math.parity_year_estimate`, `lib.capability_math.convergence_pattern`, `lib.capability_math.multi_dimensional_summary`
