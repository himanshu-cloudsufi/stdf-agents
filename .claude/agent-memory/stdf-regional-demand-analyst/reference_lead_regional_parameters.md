---
name: Lead regional demand parameters
description: Regional market shares, S-curve parameters, threshold crossing years, and India 2W/3W concentration finding from lead (Pb) demand disaggregation run (2026-03-20)
type: reference
---

## Run context
- Pipeline slug: `lead-demand-decline`
- Analysis date: 2026-03-20
- Global 2026 baseline: 11,095 kt (model); 2024 observed: 12,259 kt

## Regional market shares (2026 baseline, 5-region)
- China: 32.4% (3,598 kt)
- USA: 15.2% (1,689 kt)
- Europe: 15.3% (1,700 kt)
- India: 15.2% (1,681 kt)
- RoW: 21.9% (2,428 kt)

## Segment concentration by region
- India is structurally different: 64% of its lead demand is 2W SLI (43%) + 3W SLI (22%). PC SLI is only 14%.
- China/USA/Europe: PC replacement SLI dominates (29–30%), followed by non-battery floor (16–21%).
- India 2W market: ~21M units/year, ~55% of global 2W lead demand → 718 kt baseline (2026).
- India 3W market: ~70% of global 3W lead demand → 364 kt baseline (2026).

## Regional BEV new-car S-curve parameters (from 05b-regional-adopter, T2-fitted)
- China: L=85%, k=0.4089, x0=2025.4 (R²=0.955) — past inflection
- USA: L=85%, k=0.3635, x0=2029.6 (R²=0.976) — pre-inflection
- Europe: L=85%, k=0.3558, x0=2027.2 (R²=0.955) — pre-inflection
- RoW: L=85%, k=0.4999, x0=2029.6 (R²=0.994) — pre-inflection
- India (T3 estimate): L=70%, k=0.18, x0=2034.0 — price-sensitivity ceiling

## India 2W EV S-curve (critical for lead; very high uncertainty)
- Parameters: L=60%, k=0.20, x0=2028.0
- Anchored to SIAM 6–7% 2W EV share in 2024 [T3]
- Ceiling sensitivity: if L=75–80%, India threshold crossing advances from 2031 to 2028–2029

## 10% decline threshold crossing years (from 2026 regional baseline)
- China: ~2028.1 (first; fast BEV S-curve + telecom LFP past inflection)
- Europe: ~2028.9
- USA: ~2029.6
- RoW: ~2029.7
- India: ~2031.0 (last; 2W/3W incumbent retention)
- Global (vs. 2024 observed): 2027 (stream-forecaster answer)

## Regional CAGR 2026–2036
- China: −4.7%/yr
- RoW: −4.6%/yr
- Europe: −4.1%/yr
- USA: −4.0%/yr
- India: −2.6%/yr (slowest)

## Reconciliation scalars (regional bottom-up vs. stream-forecaster global)
- 2026: 1.0001 (perfect)
- 2031: 1.046
- 2036: 1.040
- 2046: 1.044
(~4–5% gap at all forward horizons; within normal bottom-up disaggregation uncertainty)

## Non-SLI regional share adjustments vs. global (T3 only)
- China telecom LFP: ~50% (global 33%) → x0 shifted 1.5yr ahead of global
- USA datacenter UPS LFP: ~50% (global 37%) → x0 shifted 1.4yr ahead of global
- These two adjustments together explain China's faster decline vs. expected from BEV S-curve alone
