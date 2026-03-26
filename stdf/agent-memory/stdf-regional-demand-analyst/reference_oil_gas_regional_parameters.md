---
name: oil_gas_regional_demand_parameters
description: Regional market size splits, S-curve parameters, and structural findings from oil/gas demand disruption disaggregation run (2026-03-20)
type: reference
---

## Oil Regional Demand Parameters (2026 baseline, mb/d)

Regional market size splits used for disaggregation (reconciled to 07b global 99.6 mb/d):

| Region | Total 2026 | V1 transport split | V2 oil power split | V3 heating oil split | Floor split |
|--------|-----------|-------------------|-------------------|---------------------|------------|
| China  | 15.1 | 24% | 5% | 2% | 15% |
| Europe | 14.8 | 18% | 20% | 55% | 11% |
| USA    | 21.0 | 22% | 15% | 35% | 19% |
| RoW    | 48.7 | 36% | 60% | 8% | 55% |

V1 total transport oil 2026: 36.8 mb/d. V2 oil power 2026: 3.9 mb/d. V3 heating oil 2026: 3.9 mb/d. Structural floor 2026: 54.9 mb/d.

CAGR 2026–2046 (oil): China -1.66%/yr, Europe -1.99%/yr, USA -1.83%/yr, RoW -1.26%/yr.

## Gas Regional Demand Parameters (2026 baseline, bcm/yr)

| Region | Total 2026 | V2 gas power split | V3 gas heating split | Floor split |
|--------|-----------|-------------------|---------------------|------------|
| China  |   378 | 8% | 7% | 12% |
| Europe |   737 | 16% | 38% | 14% |
| USA    | 1,045 | 30% | 36% | 20% |
| RoW    | 1,775 | 46% | 19% | 54% |

V2 total gas power 2026: 1,546 bcm. V3 total gas heating 2026: 648 bcm. Structural floor 2026: 1,742 bcm.

CAGR 2026–2046 (gas): China -1.54%/yr, Europe -2.18%/yr, USA -2.57%/yr, RoW -1.82%/yr.

**USA is fastest-declining gas market** because it has the largest gas-powered grid (est. 464 bcm gas power in 2026, ~30% of global).

## V3 HP Stock S-Curve Parameters (Estimated for China, USA, RoW)

Only Europe has a fitted V3 S-curve (R²=0.9987, L=33.01%, k=0.1393, x0=2028.9). Others estimated from lag offsets:

- China: L=28%, k=0.1393, x0=2034.0 (5yr lag; lower ceiling because HP displaces coal district heating in north China, not gas)
- USA: L=30%, k=0.1393, x0=2035.0 (6yr lag)
- RoW: L=25%, k=0.1393, x0=2038.0 (9yr lag)

**China gas V3 destruction is structurally limited** — China's HP market is the world's largest by installed capacity (>250 GW), but displaces coal, not gas, in northern regions.

## Reconciliation Scalars

Regional bottom-up projections reconcile to 07b global totals with these year-specific scalars:
- Oil: 2026=1.079, 2031=1.071, 2036=1.046, 2046=1.046
- Gas: 2026=1.000, 2031=1.047, 2036=0.996, 2046=1.006

Scalars within ~8% for oil (dominated by V1 transport oil regional split estimation error) and ~5% for gas. These are within acceptable calibration range given regional market size uncertainty of ±3–5 pp.

## Key Asymmetric Findings

1. **China leads oil disruption but contributes least gas disruption** — V1 EV fleet inflection at x0=2023.7 drives fast oil destruction; but coal-dominated grid means solar PV (V2) does not destroy gas.
2. **USA is largest single gas destruction market** — gas-heavy electricity grid (40% from gas) + second-largest HP adoption trajectory = 424 bcm destroyed by 2046 (32% of global).
3. **RoW oil-fired power persists longer** — oil-fired generation concentrated in Middle East/Africa where solar infrastructure deployment lags the S-curve k parameter suggests.
