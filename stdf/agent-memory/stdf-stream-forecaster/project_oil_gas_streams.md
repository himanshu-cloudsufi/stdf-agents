---
name: oil-gas multi-vector stream forecast results
description: Three-stream demand projections for oil (mb/d) and gas (bcm/yr) across V1/V2/V3 disruption vectors — chimera peaks, CI widths, structural floor dynamics, S-curve parameters used at +5/10/20yr horizons
type: project
---

Oil and gas demand disruption analysis (pipeline run: oil-gas-demand-disruption, 2026-03-20).
Three disruption vectors simultaneously: V1 (BEV displacing oil in road transport), V2 (solar+BESS displacing gas in power), V3 (ASHP displacing gas in heating).

**Why:** This is the reference implementation for a dual-commodity, multi-vector stream forecast. The key structural insight is that disruptor streams are identically zero for both commodities — BEV/SWB/ASHP consume electricity, not oil or gas. All disruption appears as incumbent stream compression.

**How to apply:** Use these calibrated parameters and stream ratios as priors for any future oil or gas commodity demand analysis.

---

## S-Curve Parameters Applied

| S-curve | L (%) | k | x0 | Lag | Source |
|---|---|---|---|---|---|
| V1 BEV passenger car (new sales) | 85.0 | 0.3836 | 2027.8 | 6yr rolling avg | 05a-scurve-fitter |
| V1 total EV (incl PHEV) new sales | 90.0 | 0.4281 | 2026.3 | 6yr rolling avg | 05a-scurve-fitter |
| V1 BEV-HDT (commercial truck) | 85.0 | 0.3836 | 2030.8 | 4yr rolling avg | 05a shifted +3yr |
| V1 BEV-LCV | 85.0 | 0.3836 | 2029.8 | 5yr rolling avg | 05a shifted +2yr |
| V2 solar generation share | 45.0 | 0.2279 | 2031.6 | none (instantaneous) | 05a-scurve-fitter |
| V3 HP global stock share | 33.01 | 0.1388 | 2028.9 | none (already stock) | fitted to 07a breakpoints, R²=1.00 |

Key: V3 HP stock S-curve must be fitted secondarily from decomposer breakpoints — the upstream 05a S-curve gives EU *new installation* share, not global stock share. The fitted stock S-curve (L=33%, not 79%) is what should be applied to gas heating demand volumes.

---

## Oil Stream Outcomes (mb/d)

| Segment | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|---|---:|---:|---:|---:|
| Passenger ICE (I) | 21.3 | 10.3 | 4.1 | 2.8 |
| PHEV (C, chimera) | 2.1 | 4.2 | 2.8 | 1.4 |
| HDT diesel (I) | 9.6 | 7.0 | 3.4 | 1.6 |
| LCV (I) | 3.8 | 2.7 | 1.3 | 0.6 |
| Oil power (I) | 3.9 | 3.5 | 3.1 | 2.7 |
| Heating oil (I) | 3.9 | 3.6 | 3.4 | 3.1 |
| Structural floor (I) | 54.9 | 56.3 | 57.7 | 60.7 |
| **Total** | **99.6** | **87.7** | **75.8** | **73.0** |

- Disruptor stream = 0.0 mb/d at all horizons
- PHEV chimera peak: 2031 at 4.2 mb/d (4.8% of total)
- Structural floor is 54% of total in 2026, rising to 74% by 2046

## Gas Stream Outcomes (bcm/yr)

| Segment | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|---|---:|---:|---:|---:|
| CCGT (I) | 1,157 | 858 | 479 | 148 |
| OCGT (I) | 373 | 220 | 26 | 8 |
| Residential gas (I) | 498 | 466 | 436 | 401 |
| Commercial gas (I) | 142 | 133 | 125 | 114 |
| Gas chimera (C, total) | 22 | 35 | 22 | 5 |
| Structural floor (I) | 1,742 | 1,788 | 1,834 | 1,928 |
| **Total** | **3,935** | **3,497** | **2,920** | **2,601** |

- OCGT is most acutely exposed: 98% collapse 2024→2046
- Gas chimera peak: 2030–2031 at 36 bcm (<1% of total)
- Structural floor is 44% of total in 2026, rising to 74% by 2046

## Chimera Dynamics

| Type | Peak Year | Peak | 2046 |
|---|---|---|---|
| PHEV vehicles (oil) | 2031 | 4.2 mb/d | 1.4 mb/d |
| Gas+solar hybrid power | 2030 | 25 bcm | 2 bcm |
| Dual-fuel heating | 2031 | 11 bcm | 2 bcm |

## Confidence Interval Widths

### Oil (mb/d)
- +5yr: P10=82.5, P50=87.7, P90=93.2 | width=10.7 mb/d (12%)
- +10yr: P10=70.5, P50=75.8, P90=81.6 | width=11.1 mb/d (15%)
- +20yr: P10=65.8, P50=73.0, P90=80.4 | width=14.6 mb/d (20%)
- Floor growth rate (0.5±0.3%/yr) is the dominant uncertainty at +20yr (±7.2 mb/d)

### Gas (bcm/yr)
- +5yr: P10=3,280, P50=3,497, P90=3,690 | width=410 bcm (12%)
- +10yr: P10=2,710, P50=2,920, P90=3,180 | width=470 bcm (16%)
- +20yr: P10=2,390, P50=2,601, P90=2,860 | width=470 bcm (18%)
- Solar displacement ratio uncertainty (±10pp) dominates at +10yr; floor at +20yr

## Displacement Ratios Used

| Vector | Ratio | Basis |
|---|---|---|
| Solar-to-gas displacement | 0.55 TWh gas per TWh solar | global average; ±10pp uncertainty |
| Gas intensity weighted | 0.2039 bcm/TWh | 75% CCGT (0.1841) + 25% OCGT (0.2633) |
| OCGT exposure vs CCGT | 1.35× / 0.88× | merit order position |
| Oil power exposure | 1.5× average | highest marginal cost fuel |
| PHEV gasoline fraction | 40% of ICE intensity | 4.53 vs 11.32 bbl/vehicle-yr |
