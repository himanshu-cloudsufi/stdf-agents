---
name: EV vs ICE S-curve parameters (2025 fit)
description: Fitted logistic S-curve parameters for BEV adoption displacing ICE passenger cars, fitted March 2026 using 2010-2025 data
type: reference
---

## Fitted S-Curve Parameters — BEV disrupting ICE passenger cars

**Methodology:** Fixed-L logistic fit using scipy curve_fit (k and x0 fitted, L domain-informed)
**Data:** 16 annual data points per region (2010–2025); market shares computed from Rethinkx catalog sales + web research 2025

| Region | L (%) | k | x0 | R² | RMSE (pp) |
|--------|-------|---|----|----|-----------|
| Global | 88    | 0.3460 | 2028.57 | 0.9785 | 0.877 |
| China  | 93    | 0.3535 | 2026.42 | 0.9566 | 2.293 |
| Europe | 88    | 0.2893 | 2028.74 | 0.9098 | 2.195 |
| USA    | 82    | 0.2671 | 2032.47 | 0.8956 | 1.017 |

**Why:** Free 3-parameter fit with early-growth data consistently hits L constraint boundaries; fixed-L approach with domain-reasoned ceiling is more reliable.

**Why L values chosen:**
- Global 88%: PHEVs retain 5-8%, niche ICE in developing markets 4-7%
- China 93%: near-full displacement expected given policy + cost + infrastructure
- Europe 88%: similar to global but strong regulatory 2035 ICE ban backstop
- USA 82%: geographic dispersion, political headwinds, weaker entry-level BEV supply

## 2025 Market Share Baselines (computed from Rethinkx + web)
- Global BEV: 18.7% (13.7M BEV / ~73M total new car sales)
- China BEV: 32.0% (H1 30.8%; NEV including PHEV ~50%)
- Europe BEV: ~19.0% (H1 17.5%; UK near 30%)
- USA BEV: ~7.5% (down from 9.2% in 2024 due to federal tax credit expiry Sep 2025)
- Norway: ~85%+ (saturation phase)

## ICE Decline Empirical Data (Rethinkx catalog)
- Global ICE peak: 85.3M units (2017) → 55.7M (2024): -34.6%
- China ICE peak: 23.6M (2017) → 12.6M (2024): -46.7%
- Europe ICE peak: 15.4M (2017) → 8.6M (2024): -43.7%
- USA ICE peak: 16.4M (2015) → 11.6M (2024): -29.3%

## Projections (5/10/20-year, BEV market share %)
5-year (2031): Global 62 [58,65], China 78 [74,81], Europe 58 [52,65], USA 33 [24,40]
10-year (2036): Global 82 [80,83], China 90 [88,91], Europe 78 [73,82], USA 59 [51,67]
20-year (2046): Global 88, China 93, Europe 87, USA 80
