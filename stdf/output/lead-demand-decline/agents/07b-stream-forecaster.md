# STDF Stream Forecaster Agent — Lead (Pb) Demand Decline

**Agent:** `stdf-stream-forecaster` | **Confidence:** 0.82

**Analysis Date:** 2026-03-20

---

## Agent Reasoning

Lead demand is a zero-content disruptor case: BEV, LFP-UPS, and LFP motive power each carry exactly 0.0 kg Pb per unit, so the disruptor stream is identically zero at all horizons. All disruption dynamics appear entirely as incumbent stream compression — a structural feature that distinguishes this analysis from commodities where the disruptor technology retains partial material content. The three-stream framework is still required because the chimera stream (PHEV/48V mild-hybrid vehicles retaining a 12V SLI battery) creates a genuine hump-shape in demand that runs counter to the main incumbent decline. Without isolating it, total demand appears to decline more smoothly than it actually does.

The 10-driver decomposition from the upstream demand decomposer was ingested directly and each driver was computed independently using S-curve adoption rates from the upstream scurve-fitter. Five drivers have upstream-fitted S-curve parameters (BEV new sales, BEV fleet share, telecom LFP-UPS, datacenter LFP-UPS, EV forklift); three drivers (commercial vehicle, 2-wheeler, 3-wheeler) use conservative S-curves estimated from the disruption phase noted in 07a (pre-disruption / early rupture) and carry wider confidence intervals accordingly. Two drivers — other industrial stationary (577 kt) and non-battery uses (1,691 kt) — are held near-constant at +0.2%/yr and −0.3%/yr secular rates respectively, consistent with the 2015–2024 CAGR observed in the catalog.

The incumbent declining stream is dominated by two sub-drivers that move at very different rates: passenger car new-vehicle SLI declines fast (BEV_new S-curve with x0=2028.83, already 23% BEV share in 2026) but represents only 810 kt; passenger car aftermarket replacement SLI is 3,377 kt but lags the fleet S-curve (x0=2031.77, 6.7% BEV fleet share in 2026). This lag structure means the replacement stream is still large in 2031 (2,390 kt) even as the new-vehicle stream has collapsed to 411 kt. The 2031 incumbent total is dominated by the still-large replacement pool, not by new-vehicle SLI. By 2036, BEV fleet penetration reaches 68% and the replacement stream contracts sharply to 1,172 kt — that is the decade when lead demand breaks structurally.

The chimera hump-shape is modeled as the PHEV new-vehicle SLI stream. PHEVs retain a standard 12V SLI battery (12.0 kg Pb per vehicle), making them indistinguishable from ICE incumbents in material content but sourced differently in the market: PHEVs are a chimera that displaces ICE incumbents early (capturing share before full BEVs dominate) and is then itself displaced by BEVs later. The chimera demand follows the calibrated PHEV sales schedule: 4.5M vehicles in 2026 (54 kt Pb), peaking at 6.0M in 2031 (72 kt Pb), then declining to 3.0M in 2036 (36 kt) and 0.6M in 2046 (7 kt). This peak-at-2031 hump is driven by the interplay of PHEVs growing their early-EV market share while BEV new sales concurrently capture the majority of the electrification wave. Monte Carlo confidence intervals were computed over 1,000 draws perturbing all S-curve parameters (k ±12%, L ±0.03, x0 ±1yr for fitted curves; larger perturbations for conservatively estimated curves), with PHEV volume uncertainty of ±20%.

---

## Agent Output

### Key Findings
- **Commodity:** Lead (Pb)
- **Streams modeled:** Incumbent (declining), Disruptor (zero — LFP/BEV contain no lead), Chimera (PHEV SLI hump)
- **Net direction:** Declining — strongly and structurally
- **10% decline threshold crossing:** 2027 (median path; already within 0.6% of threshold at 2026 model value of 11,095 kt)
- **Chimera peak year:** 2031 at 72 kt (PHEV SLI; 0.78% of total 2031 demand)
- **Chimera significance:** Minimal — the chimera adds at most 72 kt to a total that falls by ~3,054 kt over 2026–2031. The hump shape is real but small relative to incumbent compression.
- **Confidence:** 0.82

### Technology Stream Demand
| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent | 11,041 | 9,133 | 7,236 | 6,269 |
| Disruptor | 0 | 0 | 0 | 0 |
| Chimera (PHEV SLI) | 54 | 72 | 36 | 7 |
| **Total** | **11,095** | **9,205** | **7,272** | **6,276** |

*2024 observed baseline: 12,259 kt [T2: catalog, observed]. Model current value at 2026 = 11,095 kt (−9.5% from 2024 observed). S-curve disruption in BEV new sales (23.1% share in 2026) and stationary LFP-UPS displacement (51%+ LFP share in telecom and datacenter) is already materially eroding demand. The 10% decline threshold (11,033 kt) is crossed in 2027 [model-derived].*

### Per-Driver Stream Breakdown

#### Passenger Car — New-Vehicle SLI (ICE incumbent)
*2024 observed: 810 kt | BEV new-sales S-curve: L=85%, k=0.3492, x0=2028.83*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (ICE SLI) | 750 | 411 | 209 | 148 |
| Disruptor (BEV, 0 kg Pb) | 0 | 0 | 0 | 0 |
| Chimera | 0 | 0 | 0 | 0 |
| BEV new-sales share (%) | 23.1% | 57.9% | 78.6% | 84.8% |

*Fastest-declining individual driver. New-vehicle SLI demand falls 73% from its 2026 model level by 2036 as BEV surpasses 78% of new passenger car sales [model-derived from upstream S-curve].*

#### Passenger Car — Aftermarket Replacement SLI
*2024 observed: 3,377 kt | Fleet S-curve: L=80%, k=0.4155, x0=2031.77 | Replacement cycle: 4.5yr*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (ICE fleet replacement) | 3,280 | 2,390 | 1,172 | 782 |
| Disruptor (BEV fleet, 0 kg Pb) | 0 | 0 | 0 | 0 |
| BEV fleet share (%) | 6.7% | 33.7% | 68.2% | 79.8% |

*Largest single driver. Fleet share lags new-sales share by ~3 years due to vehicle lifetime averaging 12–15yr. Still 2,390 kt in 2031 because the ICE fleet turns over slowly. The sharpest decline occurs 2031–2036 as the 2024–2030 BEV new-sales surge enters the fleet replacement pool [model-derived].*

#### Passenger Car — New-Vehicle PHEV SLI (Chimera)
*2024 observed: ~39 kt (3.25M PHEVs × 12 kg Pb) | Calibrated PHEV sales schedule*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Chimera (PHEV 12V SLI) | 54 | 72 | 36 | 7 |
| PHEV sales implied (M vehicles) | 4.5M | 6.0M | 3.0M | 0.6M |

*Hump peaks 2031 at 72 kt as PHEVs reach maximum market penetration before BEV S-curve displacement accelerates. By 2046, residual PHEV volume (0.6M/yr globally) contributes only 7 kt. Note: chimera demand is additive to — not a reallocation of — the ICE incumbent stream; PHEVs displace ICE incumbents, not BEVs.*

#### Commercial Vehicle SLI (New + Replacement)
*2024 observed: 1,535 kt | Conservative S-curve: L=65%, k=0.20, x0=2033.83 (estimated — no upstream fit)*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (CV ICE/diesel SLI) | 1,362 | 1,173 | 929 | 618 |
| Disruptor (BEV CV, 0 kg Pb) | 0 | 0 | 0 | 0 |
| BEV CV share (%) | 11.5% | 23.5% | 39.4% | 59.8% |

*Slower S-curve adoption than passenger cars. Commercial fleets have longer replacement cycles, higher upfront cost sensitivity, and limited charging infrastructure for long-haul routes. The conservative L=65% ceiling reflects heavy-duty and long-haul segments unlikely to fully electrify by 2046 [model-derived, high uncertainty].*

#### 2-Wheeler SLI (New + Replacement)
*2024 observed: 1,395 kt | Conservative S-curve: L=25%, k=0.15, x0=2033 (no upstream fit — data gap)*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (lead-acid 2W SLI) | 1,305 | 1,247 | 1,182 | 1,090 |
| Disruptor (Li-ion e-2W, 0 kg Pb) | 0 | 0 | 0 | 0 |
| Li-ion 2W share (%) | 5.1% | 10.6% | 15.3% | 21.9% |

*The most stable major demand driver. Li-ion 2W disruption is asymmetric across geographies — advanced in China, nascent in India/SE Asia. Low-cost lead-acid 2W batteries remain competitive in price-sensitive markets. The 25% ceiling is a conservative bound; upside risk exists if cost-curve dynamics accelerate in Indian and Southeast Asian markets (analogous to the stellar energy cost curve inflection that drove solar adoption in those same geographies). [model-derived, very high uncertainty]*

#### 3-Wheeler SLI (New + Replacement)
*2024 observed: 548 kt | Conservative S-curve: L=20%, k=0.12, x0=2035 (no upstream fit)*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (lead-acid 3W SLI) | 520 | 506 | 490 | 461 |
| Disruptor (electric 3W, 0 kg Pb) | 0 | 0 | 0 | 0 |
| Electric 3W share (%) | 2.8% | 7.6% | 10.6% | 15.8% |

*Even slower displacement than 2W. Auto-rickshaws in South Asia have specific duty-cycle and affordability characteristics; LFP traction costs have not yet reached parity for multi-shift operators relying on rapid lead-acid swap charging [model-derived, very high uncertainty].*

#### Telecom Tower — VRLA Backup Power
*2024 observed: 907 kt | Upstream-fitted S-curve: L=85%, k=0.3659, x0=2024.84*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (VRLA per site) | 441 | 209 | 149 | 136 |
| Disruptor (LFP-UPS, 0 kg Pb) | 0 | 0 | 0 | 0 |
| LFP share of new capacity (%) | 51.4% | 76.9% | 83.6% | 85.0% |

*Disruption is already past inflection. The S-curve inflection was x0=2024.84 and the curve is in its steep phase. From 907 kt in 2024 to 209 kt in 2031 is a 77% collapse in seven years. The 136 kt residual by 2046 represents legacy VRLA replacement in older towers not yet upgraded to LFP [model-derived from upstream S-curve].*

#### Datacenter — UPS VRLA
*2024 observed: 503 kt | Upstream-fitted S-curve: L=90%, k=0.2569, x0=2024.90*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (VRLA UPS) | 245 | 128 | 75 | 52 |
| Disruptor (LFP UPS, 0 kg Pb) | 0 | 0 | 0 | 0 |
| LFP share of new capacity (%) | 51.3% | 74.5% | 85.1% | 89.6% |

*Second-fastest structural collapse after telecom. LFP UPS adoption in datacenters is driven by total cost of ownership (footprint, cycle life, and float-charging efficiency) — a market-driven disruption with no policy mandate dependency. This is incumbent displacement by a lower-cost technology, not a regulatory phase-out. The 90% ceiling and lower k produce a slower long-run saturation than telecom, but by 2046 datacenter lead demand reaches only 52 kt — a 90% reduction from the 503 kt 2024 observed [model-derived from upstream S-curve].*

#### Industrial Forklift — Lead-Acid Traction Battery
*2024 observed: 913 kt | Upstream-fitted S-curve: L=70.66%, k=0.1891, x0=2009.61 (near-saturation)*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (lead-acid traction) | 877 | 828 | 808 | 797 |
| Disruptor (LFP motive, 0 kg Pb) | 0 | 0 | 0 | 0 |
| EV forklift share of new sales (%) | 67.6% | 69.4% | 70.2% | 70.6% |

*Counter-intuitively stable. The S-curve ceiling at 70.66% means EV forklift share of new sales plateaus near its current level. Lead-acid traction batteries retain ~30% of the forklift market (heavy-duty outdoor applications, cost-sensitive tier-3 markets). Because the fleet contains both old lead-acid and newer EV forklifts with long service lives, the replacement pool for lead-acid batteries remains substantial. Forklift lead demand erodes slowly from 877 kt to 797 kt by 2046 [model-derived from upstream S-curve].*

#### Other Industrial Stationary
*2024 observed: 577 kt | No S-curve available; held at +0.2%/yr secular growth*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Incumbent (VRLA/flooded, misc.) | 579 | 585 | 591 | 602 |

*Grid backup, emergency lighting, and railway signaling batteries. Insufficient sub-product data to fit individual S-curves. Displacement is beginning in grid-scale BESS applications but the installed base is long-lived. Conservative assumption: net-flat with slow growth from new installations roughly offsetting partial LFP displacement in new projects [model-derived, held at secular rate].*

#### Non-Battery Lead — Structural Floor
*2024 observed: 1,691 kt | Secular decline: −0.3%/yr (observed 2015–2024 CAGR) [T2: catalog]*

| Stream | Current 2026 (kt) | +5yr / 2031 (kt) | +10yr / 2036 (kt) | +20yr / 2046 (kt) |
|--------|------------------:|------------------:|------------------:|------------------:|
| Structural floor (no disruptor) | 1,681 | 1,656 | 1,631 | 1,583 |

*Ammunition, radiation shielding, cable sheathing, and lead alloys have no identified lithium-ion substitution pathway. This 13.8% of demand is correctly treated as a structural floor. It is slowly eroding (−0.3%/yr, primarily from cable sheathing substitution by HDPE) but will not be affected by the S-curve adoption dynamics governing the battery segments [T2: catalog CAGR, observed].*

---

### S-Curve Parameters Used
| S-Curve | L (ceiling) | k (growth rate) | x0 (inflection year) | Source | Fit Quality |
|---------|:-----------:|:---------------:|:--------------------:|--------|-------------|
| BEV new-car sales | 0.85 | 0.3492 | 2028.83 | 05a-scurve-fitter | Upstream-fitted [model-derived] |
| BEV fleet share | 0.80 | 0.4155 | 2031.77 | 05a-scurve-fitter | Upstream-fitted [model-derived] |
| Telecom LFP-UPS share | 0.85 | 0.3659 | 2024.84 | 05a-scurve-fitter | Upstream-fitted [model-derived] |
| Datacenter LFP-UPS share | 0.90 | 0.2569 | 2024.90 | 05a-scurve-fitter | Upstream-fitted [model-derived] |
| EV forklift new-sales share | 0.7066 | 0.1891 | 2009.61 | 05a-scurve-fitter | Upstream-fitted [model-derived] |
| BEV commercial vehicle | 0.65 | 0.20 | 2033.83 | Conservative estimate (07a phase: early rupture) | No upstream fit — high uncertainty |
| Li-ion 2-wheeler | 0.25 | 0.15 | 2033.00 | Conservative estimate (07a phase: pre-disruption) | No upstream fit — very high uncertainty |
| Electric 3-wheeler | 0.20 | 0.12 | 2035.00 | Conservative estimate (07a phase: pre-disruption) | No upstream fit — very high uncertainty |
| PHEV chimera (hump schedule) | N/A | N/A | N/A | Calibrated to 2024 observed ~39 kt; schedule-based hump | Anchored to observed 2024 PHEV sales [observed] |
| Non-battery secular decline | −0.3%/yr | — | — | T2 catalog CAGR 2015–2024 [observed] | Observed historical trend |

---

### Confidence Intervals
| Horizon | Year | Total P50 (kt) | CI Low P10 (kt) | CI High P90 (kt) | Width | Width % |
|---------|------|---------------:|----------------:|------------------:|-------|---------|
| Current | 2026 | 11,095 | — | — | — | — |
| +5yr | 2031 | 9,196 | 8,739 | 9,616 | 877 kt | 10% |
| +10yr | 2036 | 7,292 | 7,016 | 7,633 | 617 kt | 8% |
| +20yr | 2046 | 6,284 | 6,081 | 6,493 | 413 kt | 7% |

*Confidence intervals narrow at longer horizons because the structural nature of the decline dominates. At +20yr, even the fast-adoption (P10, low demand) and slow-adoption (P90, high demand) scenarios both produce totals well below 8,000 kt. The key uncertainty at +20yr is not whether demand falls but how large the structural floor is — dominated by the 2W/3W/forklift segments with uncertain but bounded S-curve ceilings, and the non-battery floor. The widest relative uncertainty at +5yr comes from CV, 2W, and 3W S-curve parameter uncertainty (no upstream fits for these three drivers). Monte Carlo N=1,000 draws; all values [model-derived].*

---

### 10% Decline Threshold: When Does Pb Demand Fall 10% Below 2024?

| Metric | Value |
|--------|-------|
| 2024 observed baseline | 12,259 kt [T2: catalog, observed] |
| 10% decline threshold | 11,033 kt |
| 2026 model demand | 11,095 kt (−9.5% from 2024) [model-derived] |
| **Median threshold crossing year** | **2027** [model-derived] |
| 2027 model demand | 10,794 kt (−12.0% from 2024) [model-derived] |
| Probability below 11,033 kt by 2031 | 100% (all 1,000 Monte Carlo paths) |

**Answer: The 10% demand decline relative to 2024 is crossed in 2027 on the median path. The model already shows lead demand at 11,095 kt in 2026 — a mere 62 kt above the threshold — driven by telecom and datacenter LFP-UPS disruption (which is past inflection) and BEV new-car sales already at 23% share. The threshold is not a distant future event; it is imminent and highly certain.**

The key S-curve dynamics driving the near-term crossing:
1. **Telecom VRLA collapse**: From 907 kt (2024) to 441 kt (2026), with LFP share past 51%. This single driver contributed approximately −460 kt in two years [model-derived].
2. **Datacenter UPS displacement**: From 503 kt (2024) to 245 kt (2026), similarly past inflection [model-derived].
3. **BEV new-vehicle SLI**: BEV share of new passenger car sales reached 23.1% by 2026, removing 810→750 kt in new-vehicle SLI demand [model-derived].

These three vectors together account for approximately 970 kt of the ~1,164 kt decline from 2024 to 2026 that brings demand to within 62 kt of the 10% threshold.

---

### Annual Demand Trajectory (Median Path)
| Year | Total Demand (kt) | vs 2024 (%) | Note |
|------|------------------:|:-----------:|------|
| 2024 | 12,259 | 0.0% | Observed baseline [T2: catalog, observed] |
| 2025 | 11,363 | −7.3% | S-curve computed [model-derived] |
| 2026 | 11,095 | −9.5% | Model current [model-derived] |
| **2027** | **10,794** | **−12.0%** | **10% threshold crossed** [model-derived] |
| 2028 | 10,453 | −14.7% | [model-derived] |
| 2029 | 10,070 | −17.9% | [model-derived] |
| 2030 | 9,651 | −21.3% | [model-derived] |
| 2031 | 9,205 | −24.9% | +5yr horizon [model-derived] |
| 2036 | 7,272 | −40.7% | +10yr horizon [model-derived] |
| 2046 | 6,276 | −48.8% | +20yr horizon [model-derived] |

---

### Compliance Checklist
| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.3 | HIGH | PASS | Each major demand driver follows full disruption process | All 10 market products assessed individually with incumbent, disruptor, and chimera streams. Five drivers use upstream-fitted S-curves; three use conservative estimates with stated uncertainty; two held at secular rate (no disruptor applicable). |
| 6.6 | HIGH | PASS | Three parallel technology streams tracked | Incumbent, Disruptor, and Chimera streams computed at all horizons. Disruptor stream is structurally zero (LFP/BEV have 0 kg Pb content); this is a substantive result, not a modeling omission. Chimera stream (PHEV SLI) peaks 2031 at 72 kt and is modeled as a genuine hump-shape separate from the incumbent. |

---

### Data Gaps

1. **No upstream S-curve fits for commercial vehicle, 2-wheeler, and 3-wheeler BEV/Li-ion disruption.** These three drivers represent 3,478 kt (31% of 2026 model demand) and use conservatively estimated S-curves. The CI width contribution from these three segments accounts for the majority of the ±9% spread at the +5yr horizon.

2. **PHEV global sales schedule carries ±20% uncertainty.** The chimera schedule is calibrated to the 2024 observed ~39 kt anchor but PHEV market trajectories are sensitive to BEV cost curves and OEM strategy. The 72 kt chimera peak in 2031 could be 58–86 kt at P10/P90.

3. **Forklift lead-acid traction battery fleet size estimated.** The 4.5M fleet assumption used to derive the 913 kt baseline carries ±22% uncertainty (range: 830–1,304 kg/unit per-vehicle intensity). The forklift driver is therefore the largest single source of uncertainty in the +20yr estimate.

4. **Other industrial stationary (579 kt) lacks sub-product breakdown.** Grid backup BESS LFP disruption is beginning but cannot be quantified without sub-product unit sales data. The near-flat assumption may understate the decline in this segment by 2036–2046.

5. **Non-battery demand assumed to decline at historical rate (−0.3%/yr).** Any acceleration in cable sheathing substitution (e.g., regulatory restrictions on lead cable) would reduce this structural floor faster than modeled.

---

### Critical Assumptions

1. **BEV = 0.0 kg Pb per vehicle at all horizons.** Confirmed by stoichiometry. Some BEV models use a small LFP 12V auxiliary battery; lead content = 0.0 kg in all cases. [observed]

2. **LFP-UPS (telecom, datacenter) = 0.0 kg Pb per installation.** LiFePO4 chemistry contains no lead. [observed]

3. **LFP motive traction battery = 0.0 kg Pb per forklift unit.** Confirmed by chemistry. [observed]

4. **ICE passenger car fleet grows at 0.5%/yr in total size through 2046.** Modest assumption given flattening total vehicle demand in mature markets offset by growth in developing regions. The BEV fleet share applies to the growing total fleet.

5. **Passenger car SLI replacement cycle: 4.5 years.** Standard lead-acid SLI service life. ±0.5yr translates to ±6% on replacement demand volume. [T2: catalog-consistent]

6. **PHEV chimera peak: 6.0M vehicles in 2031.** Based on the logistical constraint that PHEVs grow as early BEV alternatives but are displaced by the BEV S-curve surpassing 57% new-sales share by 2031. Calibrated to 2024 observed 3.25M PHEVs × 12 kg = 39 kt. [observed anchor, model-derived schedule]

7. **EV forklift S-curve ceiling: L=70.66%.** This ceiling means 29.3% of the forklift market remains lead-acid (heavy outdoor applications, cost-sensitive tier-3 markets). The plateau is visible in the data — the S-curve inflection was 2009.61 and growth has been decelerating since 2015. [T2: upstream-fitted]

8. **Non-battery demand is a structural floor, declining at −0.3%/yr.** No substitution pathway for lead in ammunition, radiation shielding, cable sheathing, and alloys has been identified. [T2: catalog CAGR 2015–2024, observed]

---

## Sources

- Upstream: `output/lead-demand-decline/agents/07a-demand-decomposer.md` — All 10 market products, 2024 demand baselines, material intensity coefficients, disruption status, and S-curve phase tags [model-derived from T2]
- Upstream: `output/lead-demand-decline/agents/05a-scurve-fitter.md` (via 07a) — S-curve parameters (L, k, x0) for BEV new-sales, BEV fleet, telecom LFP-UPS, datacenter LFP-UPS, EV forklift [model-derived]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — Total global lead demand 2010–2024, 12,259 kt (2024), Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Sales_Cars_Global.json` — PC new-vehicle SLI demand, 810 kt (2024) [observed]
- [T2] `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_Cars_Global.json` — PC replacement SLI, 3,377 kt (2024) [observed]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand-Non-battery_uses_Global.json` — Non-battery floor, 1,691 kt (2024) [observed]
- Computation: `lib.demand_math.project_demand_from_scurve` — per-driver stream demand at +5/10/20yr horizons [model-derived]
- Computation: Monte Carlo (N=1,000) via inline python3 on all S-curve parameters — confidence interval generation [model-derived]
- Computation: Annual trajectory model (2024–2046) via inline python3 — threshold crossing year identification [model-derived]
