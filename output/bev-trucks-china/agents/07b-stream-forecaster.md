# STDF Stream Forecaster Agent — BEV Heavy Trucks Displacing LNG/Diesel Trucks (China)

**Agent:** `stdf-stream-forecaster` | **Confidence:** 0.82 | **Analysis date:** 2026-03-20

---

## Agent Reasoning

The three-stream decomposition tracks incumbent (diesel trucks declining), disruptor (BEV trucks growing), and chimera (LNG trucks — hump-shaped) as parallel commodity demand streams. Each is computed using S-curve adoption per the upstream scurve-fitter (L=0.90, k=0.7227, x0=2026.59), not GDP-linked proxies. The total demand for each commodity is the sum of its three streams; the mix shift is the analytic signal that matters most. This is a market-driven disruption propelled by cost-curve dynamics in LFP battery manufacturing — not policy mandates. Incumbent displacement of diesel and LNG trucks follows S-curve adoption. Note: stellar energy (solar PV, wind) vocabulary is inapplicable in this ground transport context; this analysis covers lithium, copper, natural gas, and diesel demand streams only.

The chimera stream requires explicit hump-shape modeling because LNG trucks captured a rising market share through roughly 2023 — driven by LNG's cost-per-km advantage over diesel — but are now falling as BEV trucks achieve superior total cost of ownership. The chimera share function is `C(t) = C_peak × S_chimera(t) × (1 − S_bev(t))`, where `S_chimera` uses L=0.999, k=0.80, x0=2020.0 (a rapid early rise with full saturation) and `S_bev` is the disruptor S-curve. The `(1 − S_bev(t))` term compresses chimera share as BEV adoption accelerates. S-curve model-derived peak occurs at 2023.3 at a 25.8% share (232,529 units), consistent with the ICCT-observed 2024 LNG peak of ~29% share — a <3.2 pp discrepancy explained by the model's symmetric S-chimera saturating slightly below the empirical peak before the BEV S-curve suppresses it. C_peak=0.30 is set at the ceiling, so the model slightly underestimates the observed 2024 LNG share but correctly reproduces the peak-then-decline trajectory. By 2031 (+5yr), the chimera share S-curve implies only 4.1% (37,000 units) as the BEV S-curve has surpassed its inflection year (2026.59) and is past 86% market share.

For **lithium**, the incumbent and chimera streams are identically zero at all horizons — neither diesel nor LNG trucks carry traction batteries. All lithium demand flows through the disruptor stream. Swap station infrastructure (scaling at the ratio of 600 stations per 198,000 BEV units, each station requiring ~11,280 kg LCE across 50 CATL 75# blocks) is included within the disruptor stream, as it is enabling infrastructure co-scaling with disruptor fleet growth. For **copper**, all three streams are non-zero because all three powertrain types use copper, though the intensity is 3.6× higher for BEV trucks (100 kg/unit) than for LNG or diesel (27.5 kg/unit). The total copper stream rises monotonically as the BEV intensity premium more than offsets the declining unit counts of incumbent and chimera fleets.

For **natural gas**, the LNG chimera stream represents active LNG consumption by the remaining LNG truck fleet. The disruptor stream represents the annual volume of LNG displaced by BEV trucks (using the 24.7% LNG-fraction of total BEV displacement from the decomposer). These two streams cross between 2026 and 2027 — the chimera LNG consumption exceeds displacement in 2026 (net demand is positive at +1.12 Mt), but from 2027 onward, displacement exceeds residual consumption and net natural gas demand from this segment is structurally negative. For **diesel**, the incumbent stream captures fuel consumed by remaining diesel trucks; the disruptor stream captures annual diesel displaced by BEV additions. LNG chimera trucks do not consume diesel, so that stream is zero.

Confidence intervals were propagated using a Monte Carlo sweep across 27 parameter combinations (L × k × x0 at 3 values each), covering P10–P90 range. The +5yr horizon shows narrower CI than the current year because by 2031 the S-curve's rapid-growth phase has passed its inflection and the trajectory is more tightly determined. The current-year CI is wide because the S-curve is near its inflection point in 2026.59, where small parameter shifts produce large unit-count differences.

---

## Agent Output

### Key Findings
- **Commodity:** Lithium (LCE), Copper (Cu), Natural Gas (LNG), Diesel
- **Streams modeled:** Incumbent, Disruptor, Chimera (all four commodities)
- **Net direction — Lithium:** growing (100 kt → 254 kt LCE; disruptor stream only)
- **Net direction — Copper:** growing (48 kt → 84 kt Cu; BEV intensity premium drives rise despite market maturation)
- **Net direction — Natural Gas (LNG):** hump-then-collapse (chimera consumption falls from 2.07 Mt to 0.32 Mt; displacement by BEV exceeds consumption from ~2027 onward)
- **Net direction — Diesel:** incumbent decline + displacement growth (net diesel demand collapses 84% from 2026 to 2046)
- **Chimera peak year:** 2023.3 (S-curve model-derived; 25.8% share, 232,529 units) [model-derived]
- **Confidence:** 0.82

---

### Technology Stream Demand — Lithium (kt LCE/yr)

| Stream | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|---------------:|------------:|-------------:|-------------:|
| Incumbent (diesel) | 0.00 | 0.00 | 0.00 | 0.00 |
| Disruptor (BEV + infra) | 100.52 | 244.40 | 254.20 | 254.49 |
| Chimera (LNG trucks) | 0.00 | 0.00 | 0.00 | 0.00 |
| **Total** | **100.52** | **244.40** | **254.20** | **254.49** |

Note: Incumbent and chimera streams are identically zero — neither diesel nor LNG trucks carry traction batteries. Disruptor stream includes BEV vehicle batteries (280 kg LCE/unit × BEV units) plus swap-station LFP block infrastructure (scaling proportionally with BEV fleet at 0.00303 stations/unit, each station ~11,280 kg LCE). Infrastructure component: 10.94 kt (2026) → 27.69 kt (2046).

---

### Technology Stream Demand — Copper (kt Cu/yr)

| Stream | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|---------------:|------------:|-------------:|-------------:|
| Incumbent (diesel) | 11.21 | 2.35 | 1.75 | 1.73 |
| Disruptor (BEV + infra) | 32.07 | 77.97 | 81.10 | 81.19 |
| Chimera (LNG trucks) | 4.74 | 1.01 | 0.75 | 0.74 |
| **Total** | **48.02** | **81.33** | **83.60** | **83.66** |

Note: All three streams non-zero because all powertrain types use copper. BEV intensity is 100 kg/unit vs. 27.5 kg/unit for LNG and diesel. Disruptor stream includes BEV truck copper (100 kg/unit × BEV units) plus swap station infra (10 kg/station) and depot charging ports (20 kg/port). The 3.6× intensity gap drives copper total demand upward despite BEV fleet approaching market saturation.

---

### Technology Stream Demand — Natural Gas / LNG (Mt LNG/yr)

| Stream | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|---------------:|------------:|-------------:|-------------:|
| Incumbent (diesel) | 0.00 | 0.00 | 0.00 | 0.00 |
| Chimera — LNG consumed | 2.07 | 0.44 | 0.33 | 0.32 |
| Disruptor — LNG displaced | 0.95 | 2.31 | 2.40 | 2.40 |
| **Net LNG demand impact** | **+1.12** | **−1.87** | **−2.07** | **−2.08** |

Note: Incumbent stream is zero because diesel trucks consume no natural gas. Chimera stream represents LNG actively consumed by the surviving LNG truck fleet. Disruptor stream represents LNG displaced per year by new BEV additions (using LNG fraction 24.7% of total BEV displacement × 12,000 kg LNG/truck-year). Streams cross between 2026 and 2027 — from that point, displacement permanently exceeds chimera consumption and the segment is a net negative driver of LNG demand. By +5yr (2031), the chimera fleet has collapsed to ~37,000 units (from ~172,000 in 2026).

---

### Technology Stream Demand — Diesel (Mbbl/yr)

| Stream | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|---------------:|------------:|-------------:|-------------:|
| Incumbent — consumed | 16.65 | 3.49 | 2.60 | 2.57 |
| Chimera — consumed | 0.00 | 0.00 | 0.00 | 0.00 |
| Disruptor — displaced | 9.84 | 23.93 | 24.89 | 24.92 |
| **Net diesel change** | **+6.81** | **−20.44** | **−22.29** | **−22.34** |

Note: Chimera stream is zero — LNG trucks run on natural gas, not diesel. Disruptor displacement uses the 75.3% diesel fraction of BEV total displacement × 6,500 L/truck-year / 159.1 L/bbl. Net diesel demand impact turns structurally negative as BEV scale overwhelms the declining incumbent consumption. By 2031, annual diesel displacement from BEV truck additions (23.93 Mbbl) is 6.9× the residual incumbent consumption (3.49 Mbbl).

---

### Per-Driver Stream Breakdown

#### Heavy Tractor-Trailer 49t (Primary Driver — ~97% of lithium and copper demand)

Market: 900,000 units/year total China HDT (primary segment)

| Stream | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| Units — Disruptor (BEV) | 319,940 | 777,880 | 809,099 | 809,999 |
| Units — Chimera (LNG) | 172,425 | 36,594 | 27,243 | 26,973 |
| Units — Incumbent (Diesel) | 407,635 | 85,526 | 63,658 | 63,027 |
| Market share BEV (%) | 35.5% | 86.4% | 89.9% | 90.0% |
| Market share LNG (%) | 19.2% | 4.1% | 3.0% | 3.0% |
| Market share Diesel (%) | 45.3% | 9.5% | 7.1% | 7.0% |

S-curve dynamics: The BEV S-curve crosses its inflection point at 2026.59 and reaches 86.4% share by 2031 — a five-year surge from 35.5% to 86.4% concentrated in the steepest portion of the logistic curve. By 2036, the S-curve model implies the market is within 0.1 pp of its ceiling (L=90%), after which BEV share is effectively flat.

**Lithium — 49t tractor (kt LCE/yr)**

| Stream | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| Incumbent | 0.00 | 0.00 | 0.00 | 0.00 |
| Disruptor (vehicles only) | 89.58 | 217.81 | 226.55 | 226.80 |
| Chimera | 0.00 | 0.00 | 0.00 | 0.00 |

**Copper — 49t tractor (kt Cu/yr)**

| Stream | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| Incumbent | 11.21 | 2.35 | 1.75 | 1.73 |
| Disruptor (vehicles only) | 31.99 | 77.79 | 80.91 | 81.00 |
| Chimera | 4.74 | 1.01 | 0.75 | 0.74 |

#### Swap Station + Depot Charging Infrastructure (Enabling Disruptor Stream)

Infrastructure demand scales proportionally with annual BEV fleet additions at the observed 2025 build ratio (600 swap stations per 198,000 BEV trucks; 2,000 depot charging ports per 198,000 BEV trucks). This is classified within the disruptor stream.

| Metric | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| New swap stations/yr | 970 | 2,357 | 2,452 | 2,455 |
| Li from infra (kt LCE) | 10.94 | 26.59 | 27.66 | 27.69 |
| Cu from infra (kt Cu) | 0.08 | 0.18 | 0.18 | 0.18 |

---

### S-Curve Parameters Used

| Parameter | Value | Source |
|-----------|-------|--------|
| L — BEV ceiling | 0.90 | 05a-scurve-fitter.md [model-derived, R²=0.9950] |
| k — BEV growth rate | 0.7227 | 05a-scurve-fitter.md [model-derived] |
| x0 — BEV inflection year | 2026.59 | 05a-scurve-fitter.md [model-derived] |
| L — Chimera (LNG) ceiling | 0.999 | Specified in prompt [model-derived] |
| k — Chimera growth rate | 0.80 | Specified in prompt [model-derived] |
| x0 — Chimera inflection year | 2020.0 | Specified in prompt [model-derived] |
| C_peak — max chimera fraction | 0.30 | Specified in prompt [model-derived] |
| LNG fraction of BEV displacement | 0.247 | 07a-demand-decomposer.md [model-derived] |
| Diesel fraction of BEV displacement | 0.753 | 07a-demand-decomposer.md [model-derived] |

---

### Confidence Intervals

#### Lithium Total (kt LCE/yr)

| Horizon | Year | P50 (kt) | P10 (kt) | P90 (kt) |
|---------|------|----------:|---------:|---------:|
| Current | 2026 | 100.52 | 61.61 | 153.79 |
| +5yr | 2031 | 243.59 | 227.07 | 261.10 |
| +10yr | 2036 | 254.20 | 239.98 | 268.39 |
| +20yr | 2046 | 254.49 | 240.35 | 268.63 |

#### Copper Total (kt Cu/yr)

| Horizon | Year | P50 (kt) | P10 (kt) | P90 (kt) |
|---------|------|----------:|---------:|---------:|
| Current | 2026 | 48.02 | 39.01 | 60.35 |
| +5yr | 2031 | 81.14 | 77.32 | 85.19 |
| +10yr | 2036 | 83.60 | 80.31 | 86.88 |
| +20yr | 2046 | 83.66 | 80.39 | 86.94 |

#### LNG Chimera Consumption (Mt LNG/yr)

| Horizon | Year | P50 (Mt) | P10 (Mt) | P90 (Mt) |
|---------|------|----------:|---------:|---------:|
| Current | 2026 | 2.07 | 1.46 | 2.51 |
| +5yr | 2031 | 0.45 | 0.25 | 0.64 |
| +10yr | 2036 | 0.33 | 0.16 | 0.49 |
| +20yr | 2046 | 0.32 | 0.16 | 0.49 |

#### Diesel Incumbent Consumption (Mbbl/yr)

| Horizon | Year | P50 (Mbbl) | P10 (Mbbl) | P90 (Mbbl) |
|---------|------|------------:|-----------:|-----------:|
| Current | 2026 | 16.65 | 11.79 | 20.21 |
| +5yr | 2031 | 3.57 | 1.97 | 5.07 |
| +10yr | 2036 | 2.60 | 1.31 | 3.90 |
| +20yr | 2046 | 2.57 | 1.29 | 3.86 |

#### Diesel Displaced by BEV (Mbbl/yr)

| Horizon | Year | P50 (Mbbl) | P10 (Mbbl) | P90 (Mbbl) |
|---------|------|------------:|-----------:|-----------:|
| Current | 2026 | 9.84 | 6.03 | 15.06 |
| +5yr | 2031 | 23.85 | 22.23 | 25.57 |
| +10yr | 2036 | 24.89 | 23.50 | 26.28 |
| +20yr | 2046 | 24.92 | 23.53 | 26.30 |

CI methodology: 27-parameter Monte Carlo sweep (L ∈ {0.85, 0.90, 0.95}, k ∈ {0.65, 0.7227, 0.80}, x0 ∈ {2025.5, 2026.59, 2027.5}), P10/P50/P90 from 27 draws. Chimera S-curve parameters held fixed; BEV S-curve parameters varied. Current-year CI is wide (P10–P90 spans 2.5× for lithium) because the S-curve is near its inflection in 2026.59, amplifying parameter sensitivity. The +5yr and beyond CIs are significantly narrower because the S-curve trajectory is more determined once past inflection.

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.3 | HIGH | **PASS** | Each major demand driver follows full disruption process | All four commodity demand drivers (Li, Cu, LNG, diesel) computed via explicit S-curve disruption dynamics. Each driver has incumbent/disruptor/chimera stream separation with time-varying shares |
| 6.6 | HIGH | **PASS** | Three parallel technology streams tracked | All four commodities have explicit incumbent, disruptor, and chimera streams. Tables show each stream separately at all four time horizons. Totals are sums of streams, not stand-alone estimates |

---

### Data Gaps

1. **Swap station infra scaling ratio.** The 600 stations/198,000 BEV units ratio for 2025 is used as a fixed scaling factor across all horizons. Actual infrastructure build may lag or lead BEV fleet growth nonlinearly as the network matures and utilization improves. This introduces ±30% uncertainty on the infrastructure component of lithium demand (which is 10.9% of total at current rates).

2. **Chimera S-curve peak calibration.** The model-derived chimera peak at 2023.3 (25.8% share) slightly undershoots the ICCT-observed 2024 LNG peak of ~29% share. The C_peak=0.30 ceiling is consistent with the observed peak approaching but not reaching 30%. The 3.2 pp gap introduces a small systematic undercount in the 2026 chimera stream (LNG fleet ~172,000 units vs. ~180,000 if the observed peak is used). This affects only the 2026 copper and LNG chimera stream values, not the +5yr onward trajectories where the chimera is already in rapid decline.

3. **BEV heavy rigid truck (>14t) stream not separately modeled.** The decomposer identified 10,800 units/year of BEV heavy rigid trucks with 160 kg LCE/unit and 60 kg Cu/unit, contributing ~2.7% of total lithium demand. These are not separately stream-forecasted here and are excluded from the per-driver tables. Including them would add ~1.73 kt LCE/yr and ~0.65 kt Cu/yr at current S-curve implied scale — a <2% uplift to totals.

4. **LNG displacement fraction held constant.** The 24.7% LNG fraction of BEV displacement is held fixed across all horizons. As the BEV disruption penetrates deeper into long-haul routes (where LNG dominance is highest), this fraction may rise in the +5yr to +10yr window before declining again as long-haul BEV share itself saturates. No segment-level S-curve differentiation is available at this stage; the constant fraction is a simplifying assumption that understates LNG displacement in the 2028–2033 window.

---

### Critical Assumptions

1. **Total market size fixed at 900,000 units/year.** The China HDT market is assumed to remain at 900,000 units/year across all horizons. Any structural demand growth (freight volume growth) or contraction (modal shift to rail) would scale all streams proportionally. A 10% market contraction would reduce all commodity demand figures by 10%.

2. **Material intensity coefficients held constant.** BEV intensity (280 kg LCE/unit, 100 kg Cu/unit) is held fixed. The decomposer notes battery kWh may decline with efficiency gains; a 20% reduction in average pack size to 280 kWh would reduce Li intensity to 224 kg/unit and cut the disruptor Li stream by ~20% from the +5yr horizon onward.

3. **Chimera S-curve parameters not uncertain.** The Monte Carlo sweep varies only BEV S-curve parameters. Chimera S-curve uncertainty (k_chimera, x0_chimera) would widen the LNG chimera stream CIs. Given the chimera stream is already empirically past peak (2024 observed LNG peak confirmed), parameter uncertainty there is less consequential for +5yr onward projections.

4. **LFP chemistry 100%.** All BEV heavy trucks assumed to use LFP cathode chemistry. Any shift toward NMC blending would change the LCE-per-kWh coefficient upward (NMC uses ~1.1–1.4 kg LCE/kWh vs. LFP at 0.8 kg LCE/kWh), increasing the lithium demand in the disruptor stream.

5. **Incumbent diesel consumption rate.** The 6,500 L/truck-year diesel consumption figure is applied to all surviving incumbent trucks at all horizons. Fuel efficiency improvements in remaining diesel trucks are not modeled; efficiency gains would reduce this rate, reducing the incumbent diesel demand stream slightly.

---

## Sources

- Upstream: `output/bev-trucks-china/agents/07a-demand-decomposer.md` — S-curve parameters (L=90%, k=0.7227, x0=2026.59); material intensity coefficients (Li: 280 kg LCE/BEV truck; Cu: 100 kg BEV vs. 27.5 kg LNG/diesel); LNG displacement fraction (24.7%); swap station build ratio (600 stations/198,000 units) [model-derived, observed basis]
- Upstream: `output/bev-trucks-china/agents/05a-scurve-fitter.md` — BEV S-curve parameters sourced via demand decomposer; R²=0.9950 [model-derived]
- Computation: `lib.demand_math.project_demand_from_scurve`, `lib.demand_math.aggregate_demand_by_technology`; all numerical results via python3 per STDF Computation Rule 1
- Chimera S-curve specification: L=0.999, k=0.80, x0=2020.0, C_peak=0.30 — specified in agent prompt, consistent with ICCT LNG share data showing peak ~2024 [model-derived]
- LCE per swap station: 50 blocks × 282 kWh × 0.8 kg LCE/kWh = 11,280 kg LCE/station [T3: CATL 75# block spec, 2025, observed via 07a]
- Diesel energy density: 159.1 L/bbl — standard petroleum conversion [physical constant]
- LNG fraction (24.7%) of BEV displacement: computed in 07a from segment-level LNG:diesel displacement fractions (long-haul 80:20, captive 40:60, urban 15:85) applied to BEV unit distribution across segments [model-derived]
