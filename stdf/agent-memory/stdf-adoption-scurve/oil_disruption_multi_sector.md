---
name: Oil disruption multi-sector S-curve analysis (2026-03-16)
description: S-curve parameters and X-curve data for oil demand disruption across transport, power generation, and heating sectors; includes fleet displacement math and oil demand peak analysis
type: reference
---

## Analysis Context

Oil market disruption requires three simultaneous S-curve models, not one. Key insight: global oil demand is still at all-time highs (103.37 Mbpd in 2024) because petrochemical growth offsets transport/power displacement. The demand peak is still ahead (2027–2030 estimate from tipping point agent).

## Sector 1: Transport — BEV New-Sales Market Share

**Fitted parameters (March 2026, 11 pts/region, 2015-2025):**

| Region | L (%) | k | x0 | R² |
|--------|-------|---|----|----|
| Global | 88 | 0.3439 | 2028.60 | 0.9722 |
| China | 93 | 0.3501 | 2026.44 | 0.9426 |
| Europe | 88 | 0.2894 | 2028.74 | 0.9097 |
| USA | 82 | 0.2620 | 2032.64 | 0.8596 |

**Note:** USA R²=0.86 is lower because 2025 data shows a dip (7.5% from 9.2% in 2024) due to federal tax credit expiry Sep 2025 — not a structural reversal. Widen USA CIs by ×2.

**2025 market shares:** Global 18.7%, China 32.0%, Europe 19.0%, USA 7.5%

**Cross-check vs prior memory run:** k values within ±0.01, x0 within ±0.2yr — consistent. This run used 11 points (2015–2025 with 2025 web-sourced) vs prior 16 points (2010–2025). Slight difference because prior run included low-share 2010-2014 data.

## Sector 2: Power Generation — Solar PV Share of Electricity

**Fitted parameters (March 2026, 15 pts, 2010-2024):**
- L=30%, k=0.2467, x0=2029.04, R²=0.9945

**2024 baselines:** Global solar 6.99%, China ~7-8%, USA 7.9%, EU >10%

**Oil-fired power generation displacement (substantially complete):**
- Global: 865,454 GWh (2007) → 616,500 GWh (2024): −28.8%, −1.98%/yr
- China: 17,100 GWh (2006) → 700 GWh (2024): −96%
- Europe: 158,748 GWh (2006) → 35,400 GWh (2024): −78%
- USA: 44,460 GWh (2006) → 12,800 GWh (2024): −71%
- Oil-fired = 2.02% of global electricity in 2024 — residual/stranded status

## Sector 3: Heating — Heat Pump Share of New Installations

**WARNING: Sparse data.** Only EHPA Europe data available in catalog.
- Europe S-curve: L=70%, k=0.1294, x0=2028.52, R²=0.911, 7 pts — indicative only
- Europe 2024: ~22% (down from 24% in 2023 due to −22% unit sales decline)
- USA 2024: ~30% of HVAC shipments
- China 2024: ~8% heating equipment (growing 12-13%/yr)
- No catalog data for HP — use web-sourced EHPA/web research for this sector

## Oil Demand X-Curve Key Numbers

**Global oil consumption (Mbpd):**
- 2024 all-time high: 103.37 Mbpd (still rising due to petrochemical offset)
- Annual growth rate 2019–2024: +3.0% net (from COVID trough)
- Growth rate falling: ~2.5 Mbpd/yr (2000–2014) → ~0.3 Mbpd/yr (2019–2024)

**Regional demand peaks:**
- USA transport: 13.57 Mbpd (2006) → 12.24 Mbpd (2024): −9.8%
- Europe total: 15.18 Mbpd (2017) → 14.31 Mbpd (2024): −5.7%
- China total: 16.86 Mbpd (2023) → 16.72 Mbpd (2024): −0.8% (possible demand plateau)

## Fleet Displacement Math

Per-vehicle oil displacement: ~10 bbl/yr (12,000 km/yr, 8L/100km ICE equiv = 960L = ~6 bbl; used 10 bbl as more conservative US-weighted average)

| Year | BEV Fleet (M) | Displaced (Mbpd) | % of 57 Mbpd transport demand |
|------|--------------|------------------|-----------------------------|
| 2025 | 50 | 1.4 | 2.4% |
| 2030 | 210 | 5.8 | 10.1% |
| 2035 | 500 | 13.7 | 24.0% |

Structural demand peak occurs when displacement (5.8 Mbpd in 2030) exceeds petrochemical growth offset (~4.5 Mbpd total 2024–2030) → consistent with 2027–2030 tipping range.

## Adoption Phase Summary (2025/2026)

- Transport (BEV): rapid_growth globally; China rapid_growth (32%); Europe rapid_growth (19%); USA tipping (7.5%)
- Power generation (solar): tipping globally (6.99%); EU rapid_growth (>10%); China/USA tipping (~8%)
- Oil-fired power: saturation of disruption (completion stage)
- Building heating (HP): rupture-tipping globally (~10% stock); Europe early rapid_growth (22% new installs)
