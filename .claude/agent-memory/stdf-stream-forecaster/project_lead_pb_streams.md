---
name: lead-Pb stream forecast results
description: Three-stream demand projections for lead (Pb) across 10 market products — chimera peak year (2031, 72 kt), threshold crossing year (2027), CI widths, structural floor dynamics, zero-content disruptor case, at +5/10/20yr horizons
type: project
---

Lead demand disruption analysis (pipeline run: lead-demand-decline, 2026-03-20).
Ten market products across four L1 sectors. BEV, LFP-UPS, and LFP motive all contain 0.0 kg Pb — disruptor stream is structurally zero. All disruption appears as incumbent compression.

**Why:** This is the reference implementation for a zero-content disruptor commodity. The structural insight: when disruptors carry zero material intensity, the three-stream framework still matters because (a) the chimera stream (PHEVs) creates a real demand hump, and (b) showing the zero disruptor stream explicitly is a substantive modeling result, not a gap.

**How to apply:** Use these calibrated parameters and stream dynamics as priors for any future lead, vanadium, or other commodity where the disruptor technology contains zero of the commodity.

---

## S-Curve Parameters Applied

| S-curve | L (%) | k | x0 | Source |
|---|---|---|---|---|
| BEV new-car sales | 85.0 | 0.3492 | 2028.83 | 05a-scurve-fitter |
| BEV fleet share | 80.0 | 0.4155 | 2031.77 | 05a-scurve-fitter |
| Telecom LFP-UPS | 85.0 | 0.3659 | 2024.84 | 05a-scurve-fitter |
| Datacenter LFP-UPS | 90.0 | 0.2569 | 2024.90 | 05a-scurve-fitter |
| EV forklift new-sales | 70.66 | 0.1891 | 2009.61 | 05a-scurve-fitter |
| BEV commercial vehicle | 65.0 | 0.20 | 2033.83 | Conservative estimate |
| Li-ion 2-wheeler | 25.0 | 0.15 | 2033.00 | Conservative estimate |
| Electric 3-wheeler | 20.0 | 0.12 | 2035.00 | Conservative estimate |

Key: BEV fleet S-curve (x0=2031.77) is ~3yr lag behind new-sales S-curve (x0=2028.83). This lag is the dominant reason the replacement stream (3,280 kt in 2026) declines much more slowly than the new-vehicle stream (750 kt in 2026 → 411 kt in 2031).

---

## Stream Outcomes (kt)

| Driver | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|---|---:|---:|---:|---:|
| PC new SLI (I) | 750 | 411 | 209 | 148 |
| PC replacement SLI (I) | 3,280 | 2,390 | 1,172 | 782 |
| PHEV SLI (C, chimera) | 54 | 72 | 36 | 7 |
| CV SLI (I) | 1,362 | 1,173 | 929 | 618 |
| 2W SLI (I) | 1,305 | 1,247 | 1,182 | 1,090 |
| 3W SLI (I) | 520 | 506 | 490 | 461 |
| Telecom VRLA (I) | 441 | 209 | 149 | 136 |
| Datacenter UPS (I) | 245 | 128 | 75 | 52 |
| Forklift traction (I) | 877 | 828 | 808 | 797 |
| Other industrial (I) | 579 | 585 | 591 | 602 |
| Non-battery floor (I) | 1,681 | 1,656 | 1,631 | 1,583 |
| **Total** | **11,095** | **9,205** | **7,272** | **6,276** |

- Disruptor stream = 0 kt at all horizons (BEV/LFP contain no Pb)
- 2024 observed: 12,259 kt
- 10% threshold (11,033 kt) crossed in **2027**

## Chimera Dynamics

| Type | Peak Year | Peak Demand | 2046 |
|---|---|---|---|
| PHEV 12V SLI | 2031 | 72 kt | 7 kt |

PHEV calibration: 3.25M units in 2024 × 12 kg Pb = 39 kt (observed anchor). Schedule: 4.5M (2026), 6.0M (2031 peak), 3.0M (2036), 0.6M (2046).

## Confidence Interval Widths (kt)

- +5yr (2031): P10=8,739, P50=9,196, P90=9,616 | width=877 kt (10%)
- +10yr (2036): P10=7,016, P50=7,292, P90=7,633 | width=617 kt (8%)
- +20yr (2046): P10=6,081, P50=6,284, P90=6,493 | width=413 kt (7%)

CIs narrow at longer horizons — structural decline dominates. Main CI driver at +5yr: CV/2W/3W with no upstream S-curve fits (3,478 kt aggregate, high parameter uncertainty).

## Forklift Modeling Note

Forklift S-curve near-saturation (L=70.66%, x0=2009.61). Incumbent projection uses ratio method: demand(t) = 913 kt × (1−EV_share(t)) / (1−EV_share(2024)). This correctly scales from the 2024 anchor. Do NOT use project_demand_from_scurve directly for forklift because that function assumes 100% addressable market, not the already-displaced market share.

## Structural Floor Composition at +20yr (2046)

Non-battery lead (1,583 kt) + 2W SLI (1,090 kt) + 3W SLI (461 kt) + forklift traction (797 kt) + other industrial (602 kt) = 4,533 kt stable/slow-moving base. These five segments represent 72% of 2046 total demand.
