# STDF Regional Demand Analyst Agent — Lead (Pb) Demand Decline

**Agent:** `stdf-regional-demand-analyst` | **Confidence:** 0.74

**Analysis Date:** 2026-03-20

---

## Agent Reasoning

Lead demand disaggregation requires modeling five regions — China, USA, Europe, India, and RoW — across eleven market segments simultaneously, because each region carries a structurally different exposure to the S-curve adoption dynamics that are compressing incumbent lead-acid demand. The global aggregates from the stream-forecaster (07b) mask two critical asymmetries: (1) China is already past the BEV new-vehicle S-curve inflection (x0=2025.4) while India's car segment is pre-inflection, and (2) India's lead demand is dominated (64%) by 2-wheeler and 3-wheeler segments that face a separate Li-ion disruption vector than passenger cars — making India structurally different from any other region.

For each region, the disruptor material intensity is identically 0.0 kg Pb per unit across all eleven segments (BEV, LFP-UPS, LFP traction batteries, Li-ion 2W/3W — none contain lead). This means regional demand is entirely a function of incumbent retention: `Demand_region(t) = Σ [Market_size_region(seg,t) × (1 − S_region(seg,t)) × MI_incumbent_region(seg)]`. Region-specific S-curve parameters were sourced from the regional-adopter (05b) for the BEV new-vehicle and BEV fleet segments (T2-fitted, R²≥0.955). For telecom UPS, datacenter UPS, and forklift segments, global S-curve parameters from the stream-forecaster were adjusted by region using the T3-sourced Li-ion share estimates in the regional-adopter (China leads telecom; USA leads datacenter UPS). For 2-wheeler and 3-wheeler segments, region-specific S-curves were estimated with China assigned a more advanced 2W electrification profile (L=70%, x0=2025) consistent with its domestic e-bike market dominance, and India's 2W assigned a tipping-phase profile (L=60%, k=0.20, x0=2028) consistent with the 6–7% 2W EV share in 2024 [T3, SIAM].

Regional market sizes were allocated from the T2 catalog vehicle sales denominators (from the regional-adopter) for the passenger car and PHEV chimera segments. For 2W, 3W, and forklift segments, regional shares were estimated using global industry reports (T3) with India receiving 55% of 2W volume and 70% of 3W volume, consistent with India's status as the world's largest 2-wheeler market (~21M units/year). Reconciliation scalars were applied at each horizon (2031: ×1.046, 2036: ×1.040, 2046: ×1.044) to ensure global regional sums exactly match the stream-forecaster's validated global totals. Confidence is rated 0.74, slightly below the stream-forecaster's 0.82, due to three T3-only segments (non-SLI regional splits, India 2W/3W) and the high sensitivity of India's demand trajectory to the 2W Li-ion S-curve ceiling, which carries very high uncertainty.

The 10% global decline question (vs. 2024 baseline of 12,259 kt) was already answered by the stream-forecaster: the global threshold of 11,033 kt is crossed in 2027. At the regional level, China crosses its own 10%-decline-from-2026 threshold earliest (~2028.1), followed by Europe (~2028.9), USA (~2029.6), RoW (~2029.7), and India last (~2031.0). India's lag is structural: with 64% of its lead demand in 2W/3W segments that face a slower and lower-ceiling S-curve adoption than passenger cars, India's decline is the most gradual of all five regions and India is the only region where lead demand does not fall below 2026 levels until near 2031.

---

## Agent Output

### Key Findings
- **Commodity:** Lead (Pb)
- **Regions analyzed:** China, USA, Europe, India, RoW (5 regions)
- **Largest demand region (current):** China (3,598 kt — 32.4% of global)
- **Slowest declining region:** India (CAGR −2.6%/yr 2026–2036; threshold ~2031.0)
- **Fastest declining region (absolute kt):** China (−1,370 kt by 2036 vs. 2026)
- **First region to cross 10%-decline-from-2026 threshold:** China (~2028.1)
- **Global 10% decline vs. 2024 baseline:** 2027 (stream-forecaster answer; confirmed)
- **Confidence:** 0.74

---

### Regional Demand Breakdown

| Region | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) | Key Driver |
|--------|------------------:|------------------:|------------------:|------------------:|------------|
| China  | 3,598 | 2,733 | 2,228 | 2,033 | PC replacement SLI (30%) + non-battery floor (18%) |
| USA    | 1,689 | 1,457 | 1,121 |   925 | PC replacement SLI (29%) + non-battery floor (16%) |
| Europe | 1,700 | 1,407 | 1,120 |   978 | PC replacement SLI (29%) + non-battery floor (21%) |
| India  | 1,681 | 1,512 | 1,288 | 1,063 | 2-Wheeler SLI (43%) + 3-Wheeler SLI (22%) |
| RoW    | 2,428 | 2,096 | 1,514 | 1,277 | PC replacement SLI (29%) + commercial vehicle (12%) |
| **Global** | **11,095** | **9,205** | **7,272** | **6,276** | — |

*All values [model-derived], reconciled to stream-forecaster global totals.*

*2024 observed global baseline: 12,259 kt [T2: catalog, observed]. Global 10% decline threshold (vs. 2024): 11,033 kt — crossed in 2027 per stream-forecaster median path.*

---

### Regional S-Curve Parameters

#### BEV New-Vehicle Sales (affects new-car SLI segment)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | R² | Source |
|--------|------------|----------------|-----------------|-----|--------|
| China  | 85.0% | 0.4089 | 2025.4 | 0.955 | 05b-regional-adopter [T2, model-derived] |
| USA    | 85.0% | 0.3635 | 2029.6 | 0.976 | 05b-regional-adopter [T2, model-derived] |
| Europe | 85.0% | 0.3558 | 2027.2 | 0.955 | 05b-regional-adopter [T2, model-derived] |
| India  | 70.0% | 0.1800 | 2034.0 | n/a | T3 estimate; L=70% reflects price-sensitivity ceiling |
| RoW    | 85.0% | 0.4999 | 2029.6 | 0.994 | 05b-regional-adopter [T2, model-derived] |

#### BEV Fleet Share (affects aftermarket replacement SLI; lags new-car x0 by ~3yr)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | Source |
|--------|------------|----------------|-----------------|--------|
| China  | 80.0% | 0.4155 | 2028.4 | Derived from global fleet params; China new-car x0 +3yr [model-derived] |
| USA    | 80.0% | 0.3635 | 2032.6 | USA new-car x0 +3yr [model-derived] |
| Europe | 80.0% | 0.3558 | 2030.2 | Europe new-car x0 +3yr [model-derived] |
| India  | 65.0% | 0.1800 | 2037.0 | India estimate +3yr; lower ceiling [model-derived] |
| RoW    | 80.0% | 0.4999 | 2032.6 | RoW new-car x0 +3yr [model-derived] |

#### 2-Wheeler Li-ion Disruption (India-critical segment)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | Source |
|--------|------------|----------------|-----------------|--------|
| China  | 70.0% | 0.2500 | 2025.0 | T3 estimate; China e-bike market dominance [model-derived] |
| USA    | 20.0% | 0.1200 | 2035.0 | T3 estimate; low 2W market share [model-derived] |
| Europe | 25.0% | 0.1500 | 2033.0 | T3 estimate; consistent with global [model-derived] |
| India  | 60.0% | 0.2000 | 2028.0 | T3; anchored to SIAM 6–7% 2W EV share 2024 [model-derived] |
| RoW    | 30.0% | 0.1500 | 2034.0 | T3 estimate [model-derived] |

---

### Regional Material Intensity

Lead (Pb) is unique: the disruptor material intensity is 0.0 kg/unit across ALL segments and ALL regions. There is no Li-ion chemistry that contains lead. Regional differences in material intensity are therefore entirely on the incumbent side.

| Region | Incumbent MI — Passenger Car SLI (kg/vehicle) | Note |
|--------|----------------------------------------------:|------|
| China  | ~11 kg | Smaller average vehicle (sedan/compact dominant) |
| USA    | ~14 kg | Larger average vehicle (SUV/truck dominant, larger group-31 batteries) |
| Europe | ~12 kg | Mid-size mix; similar to global average |
| India  | ~10 kg | Smaller vehicles; often 35–55 Ah batteries |
| RoW    | ~12 kg | Blended — includes Japan, Korea (smaller), SE Asia |

*Note: The regional demand model applies per-segment market-size allocation rather than explicit per-unit MI × units, because global driver baselines from 07b are already in kt and incorporate the relevant MI coefficients. The MI variation above is qualitative context explaining the directional basis for market-size allocations. No numerical recomputation of MI by region was performed beyond the upstream stream-forecaster's global MI assumptions.*

---

### Demand Projections Summary (Global, reconciled)

| Horizon | Year | Total Demand (kt) | vs 2026 | vs 2024 | CI P10–P90 (kt) |
|---------|------|------------------:|--------:|--------:|-----------------|
| Baseline | 2026 | 11,095 | — | −9.5% | — |
| +5yr    | 2031 | 9,205 | −17.0% | −24.9% | 8,762–9,648 |
| +10yr   | 2036 | 7,272 | −34.5% | −40.7% | 6,966–7,578 |
| +20yr   | 2046 | 6,276 | −43.4% | −48.8% | 6,069–6,483 |

*2024 observed: 12,259 kt [T2: catalog, observed]. All values at +5yr and beyond are [model-derived].*

---

### Regional Share Evolution

| Region | 2026 Share (%) | 2031 Share (%) | 2036 Share (%) | 2046 Share (%) |
|--------|---------------:|---------------:|---------------:|---------------:|
| China  | 32.4 | 29.7 | 30.6 | 32.4 |
| USA    | 15.2 | 15.8 | 15.4 | 14.7 |
| Europe | 15.3 | 15.3 | 15.4 | 15.6 |
| India  | 15.2 | 16.4 | 17.7 | 16.9 |
| RoW    | 21.9 | 22.8 | 20.8 | 20.3 |

*Key dynamics:*
- *China's share dips 2026→2031 (from 32.4% to 29.7%) as its fast BEV S-curve adoption compresses lead demand faster than other regions, then partially recovers toward its structural floor (non-battery + forklift) share.*
- *India's share rises 2026→2036 (from 15.2% to 17.7%) — India is the slowest-declining region, defended by its large 2W/3W incumbent base. India's lead market is becoming proportionally more important globally as faster regions decline more rapidly.*
- *Europe and USA shares remain relatively stable (15±1%) because their S-curve adoption trajectories and market sizes produce roughly proportional declines.*

---

### Regional 10% Decline Threshold (from 2026 baseline)

| Region | 2026 Base (kt) | 10% Threshold (kt) | Crossing Year | Lead vs. Global |
|--------|---------------:|-------------------:|:-------------:|-----------------|
| China  | 3,598 | 3,238 | ~2028.1 | 1.1yr ahead of global |
| Europe | 1,700 | 1,530 | ~2028.9 | 0.3yr ahead of global |
| USA    | 1,689 | 1,520 | ~2029.6 | 0.4yr behind global |
| RoW    | 2,428 | 2,185 | ~2029.7 | 0.5yr behind global |
| India  | 1,681 | 1,513 | ~2031.0 | 1.8yr behind global |

*Global 10% decline vs. 2024 baseline (12,259 kt → 11,033 kt): crossed 2027 per stream-forecaster.*
*Regional thresholds above measure each region's own 10% decline from its 2026 model level.*

**China crosses first (~2028.1).** China's BEV new-car S-curve adoption inflection at 2025.4 means peak BEV acceleration in new-vehicle sales has already passed. With BEV new-car share already at 47.7% in 2026 (model-derived from regional S-curve), the new-vehicle SLI segment is collapsing rapidly. The combination of fast new-vehicle incumbent displacement AND accelerated telecom/datacenter LFP-UPS adoption (China at ~50% Li-ion for telecom vs. global 33%) drives China's 10% threshold crossing approximately 2 years ahead of India.

**India crosses last (~2031.0).** With 64% of India's lead demand concentrated in 2-wheeler (43%) and 3-wheeler (22%) segments — both in early-to-mid S-curve adoption phases — India's overall decline is the most gradual. The 2W EV S-curve adoption inflection is estimated at 2028, meaning the steepest displacement pressure on India's largest lead segment begins only in 2028–2031.

---

### Per-Region Demand Confidence Intervals

| Region | +5yr 2031 P50 (kt) | P10 (kt) | P90 (kt) | +10yr 2036 P50 (kt) | P10 (kt) | P90 (kt) |
|--------|-------------------:|---------:|---------:|--------------------:|---------:|---------:|
| China  | 2,733 | 2,602 | 2,864 | 2,228 | 2,134 | 2,322 |
| USA    | 1,457 | 1,387 | 1,527 | 1,121 | 1,074 | 1,168 |
| Europe | 1,407 | 1,339 | 1,475 | 1,120 | 1,073 | 1,167 |
| India  | 1,512 | 1,439 | 1,585 | 1,288 | 1,234 | 1,342 |
| RoW    | 2,096 | 1,995 | 2,197 | 1,514 | 1,450 | 1,578 |

*CI bounds propagated from stream-forecaster Monte Carlo widths (±4.8% at +5yr, ±4.2% at +10yr, ±3.3% at +20yr). India's CI is likely understated given the very high parametric uncertainty in the 2W/3W S-curves, which carry no upstream T2 fit.*

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.9 | HIGH | PASS | Regional demand breakdown (China, USA, Europe, RoW) with region-specific parameters | Five regions covered (China, USA, Europe, India, RoW) with per-region S-curve parameters for all five displacement vectors. Regional shares evolve dynamically across horizons — not fixed percentages. Region-specific market concentrations applied (India 2W/3W; USA larger SLI batteries). |

---

### Data Gaps

1. **Non-SLI regional market splits are T3 only.** Telecom UPS, datacenter UPS, and forklift regional demand splits (China/USA/Europe/India/RoW) are estimated from industry reports (Interact Analysis, Wood Mackenzie [T3]). No T2 catalog regional breakdown exists for these segments. The directional ordering (China leads telecom LFP; USA leads datacenter LFP) is consistent across T3 sources, but the absolute kt estimates carry material uncertainty.

2. **India 2W and 3W S-curve parameters have very high uncertainty.** The India 2W EV S-curve (L=60%, k=0.20, x0=2028) is estimated from the 6–7% 2W EV share in 2024 [T3: SIAM] with no T2 fit. The ceiling parameter (60%) is particularly uncertain — if cost-curve dynamics accelerate India's 2W EV adoption faster (ceiling 75–80%), India's threshold crossing year advances to 2028–2029 rather than 2031.

3. **RoW composition heterogeneity.** Japan's hybrid-dominant BEV adoption (~3% BEV share in 2024) suppresses the RoW aggregate. A Japan-specific sub-regional series would sharpen the RoW demand picture. Southeast Asia's 2W market (large, pre-tipping) is pooled into RoW's conservative 2W parameters.

4. **China non-battery lead demand share assumed at 38%.** China is the world's largest lead producer and recycler. Its non-battery share of 38% (638 kt) is a T3-estimated allocation. The actual share depends on China's export volumes and ammunition/alloys production, which are not in the T2 catalog.

5. **India BEV passenger car ceiling estimated at L=70%.** Lower than the global/other-region L=85% because of income constraints in the mass market. This ceiling assumption is a key sensitivity for India's PC SLI trajectory at +20yr.

---

### Critical Assumptions

1. **Disruptor material intensity = 0.0 kg Pb per unit, all regions, all segments.** LFP chemistry, BEV powertrain, and Li-ion 2W batteries contain no lead. [observed, T1: NREL, T2: catalog]

2. **Regional S-curve lag structure: new-car inflection → fleet inflection ~+3 years.** Consistent with the global stream-forecaster's calibrated lag (2028.83 → 2031.77 = +2.94yr). Applied uniformly to all regions. Lag may be shorter in China (faster fleet turnover) and longer in India (older fleet stock).

3. **India represents 55% of global 2W lead demand and 70% of global 3W lead demand.** India is the world's largest 2W market (~21M units/year) [T3: SIAM, observed]. Sensitivity: ±10pp on India's 2W share moves India's total 2026 demand by ±130 kt.

4. **China telecom LFP inflection shifted 1.5yr ahead of global** (x0=2023.3 vs. global 2024.84). Anchored to China's ~50% Li-ion telecom share in 2024 [T3: Interact Analysis] vs. global 33% [T2: stream-forecaster]. This single parameter explains ~160 kt of China's faster decline relative to other regions.

5. **USA datacenter UPS inflection shifted 1.4yr ahead of global** (x0=2023.5 vs. global 2024.90). Anchored to hyperscaler (AWS, Google, Microsoft, Meta) early LFP adoption reported at ~50% Li-ion share in USA datacenters [T3: Wood Mackenzie Data Center Storage Report 2024].

6. **Reconciliation scalars applied uniformly within each horizon.** At +5yr the scalar is 1.046, meaning this bottom-up regional model produces ~4.6% less global demand than the stream-forecaster's top-down S-curve model. This gap is within normal model uncertainty for a bottom-up regional disaggregation. Scalars are applied proportionally by region (no selective regional adjustment).

---

## Sources

- Upstream: `output/lead-demand-decline/agents/07b-stream-forecaster.md` — Global demand totals by segment, S-curve parameters, chimera schedule, all eleven market products [model-derived]
- Upstream: `output/lead-demand-decline/agents/05b-regional-adopter.md` — Regional BEV S-curve fits (China, USA, Europe, RoW), adoption phase classifications, non-SLI T3 regional Li-ion estimates [T2 + T3]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_China.json` — China vehicle sales denominator, 23.9M (2024) [Rethinkx, observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_USA.json` — USA vehicle sales denominator, 13.1M (2024) [Rethinkx, observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_Europe.json` — Europe vehicle sales denominator, 11.8M (2024) [Rethinkx, observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_Rest_of_World.json` — RoW vehicle sales, 24.5M (2024) [Rethinkx, observed]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — Global lead demand 12,259 kt (2024) [Rethinkx, observed]
- [T3] India 2W EV share ~6–7% (2024): Society of Indian Automobile Manufacturers (SIAM), retrieved 2026-03-20 [observed]
- [T3] India total 2W sales ~21M units/year (2024): SIAM annual report, retrieved 2026-03-20 [observed]
- [T3] China telecom UPS Li-ion share ~50% (2024): Interact Analysis Energy Storage Report (2024) [observed]
- [T3] USA datacenter UPS Li-ion share ~50% (2024): Wood Mackenzie Data Center Storage Report (2024) [observed]
- Computation: inline python3 — regional S-curve adoption projection, reconciliation scalars, threshold crossing interpolation [model-derived]
- Computation: `lib.demand_math.regional_demand_split` — cross-check of regional share allocations [model-derived]
