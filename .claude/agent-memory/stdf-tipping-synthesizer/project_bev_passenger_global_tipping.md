---
name: BEV passenger vehicle global tipping synthesis
description: Global BEV passenger vehicle tipping synthesis: condition years, regional sequence (China 2024, Europe 2027, USA 2028), binding constraint (co-binding), provisional S-curve params, key quantitative anchors
type: project
---

## Run context
Pipeline run: `give-me-tipping-point-of-ev-vehicles-20260323-200327` (analysis date 2026-03-24)
Output: `agents/04d-tipping-synthesizer.md`

## Tipping Point Summary
- **Global tipping year:** 2027–2028 (central 2028) [model-derived]
- **Binding constraint:** co-binding — capability_parity (fleet-avg TCO gap) + adoption_readiness (USA DCFC corridor), both closing 2028
- **Confidence:** 0.88 (mean of 0.85, 0.92, 0.87 from three checkers)

## Condition Years
| Condition | Status | Year |
|---|---|---|
| Cost parity (BEV entry-level vs. ICE mid-size USA) | MET | 2025.0 |
| Capability parity (9/10 dims; fleet-avg TCO last) | PARTIAL | 2028 |
| Adoption readiness (global; China MET 2024) | NOT_MET global | 2028 |

## Regional Tipping Sequence
- **China: 2024** — all 3 conditions MET. 98% highway coverage, 12.82M charging points, NEV dual-credit mandates. China leads global by 4 years.
- **Europe: 2027** — AFIR closes corridor gap by 2026–2027; fleet-avg TCO resolves ~1yr ahead of global.
- **USA: 2028** — co-bound by 59.1% corridor coverage (model-derived 80% threshold in 2028 at 5.3 pp/yr) + 100% Section 301 tariff adding 1–2 yr friction vs. Europe.

## Key Quantitative Anchors (model-derived)
- BEV entry-level purchase price 2024: $31,000 [observed]; 2028: $26,438 [model-derived]
- ICE mid-size purchase price 2024: $29,000 [observed]; 2028: $31,000 [model-derived]
- Cost gap 2028: BEV $4,562 cheaper than ICE [model-derived]
- Battery pack cost: $115/kWh (2024, observed) → $91/kWh (2028, model-derived) via 16.81%/yr learning rate
- 60 kWh pack cost savings 2024→2028: ~$1,400/vehicle [model-derived]
- BEV energy cost/mile: $0.046/mile (2028) vs. ICE $0.135/mile (2028) [model-derived]
- Annual fuel savings per vehicle (12,000 mi/yr) by 2028: ~$1,070/yr [model-derived]
- Fleet-avg TCO: BEV $0.761/mile (2024) → $0.633/mile threshold crossing 2028 [model-derived, capability checker]
- ICE global sales 2024: ~54M; 2028 at 30% BEV share: ~45.5M (16% decline) [model-derived]
- ICE plant utilization: 87.5% (2024) → 74% (2028); fixed cost/unit: $500 → $593 (+$93) [model-derived]
- Global BEV cumulative production: ~50M (2024) → ~110M (2028) = 1.14 doublings [model-derived]

## Provisional S-Curve Parameters (for downstream scurve-fitter)
These are estimates from analogues — NOT formally fitted. Scurve-fitter should validate.
- L = 92% (maximum market saturation — leaves ~8% for PHEVs, FCEVs, niche applications)
- k = 0.30 (growth rate, based on China passenger BEV S-curve trajectory)
- x0 = 2028 (inflection midpoint, coincides with global tipping year)
- 80% global share milestone: 2033–2036, central 2034 [model-derived, provisional]
- Regional 80% milestones: China ~2030–2031; Europe ~2032–2033; USA ~2034–2036

## Key Pattern: Co-Binding at Same Year
Capability_parity and adoption_readiness resolved at the same year (2028) from shared underlying mechanism: battery cost-curve dynamics drive both fleet-avg TCO improvement (capability) and infrastructure investment returns (adoption). This is the co-binding convergence pattern. The compressed uncertainty window (2027–2028 vs. wider range) is the signature of co-binding. Warrants 1-year conservative acceleration to lower bound (2027).

## Jevons Classification
BEV = Hybrid (Stellar-dominant). Jevons Paradox NOT applied. Confirmed in Classification Overrides of 01-domain-disruption.md.
