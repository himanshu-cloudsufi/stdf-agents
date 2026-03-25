---
name: BEV Trucks China — Fleet Model Parameters
description: Fleet model parameters, OEM/replacement ratios, and mid-life battery uplift for BEV HDT disruption in China (2026-2046)
type: project
---

China heavy-duty truck fleet model (07c-fleet-modeler.md, run 2026-03-20):
- Total market: 900,000 units/yr (fixed assumption)
- Fleet entering 2025: 8,000,000 total (219,264 BEV | 1,145,250 LNG | 6,635,486 diesel)
- Truck lifetime: 8 years → scrappage rate = 0.125/yr
- Steady-state fleet: 900,000 × 8 = 7,200,000 units (fleet contracts from 8M as it equilibrates)
- BEV fleet entering 2025 derived from cumulative S-curve, 2017–2024: ~219,264 units
- LNG fleet peaks ~2027 at 1,231,000 units, then declines monotonically

**OEM vs Replacement shares (lithium, truck-sales component only):**
| Year | OEM% | Replacement% |
| 2026 | 85% | 15% |
| 2031 | 60% | 40% |
| 2036 | 32% | 68% |
| 2046 | 9%  | 91% |

**Mid-life battery replacement uplift (lithium only):**
- Intensity: 175 kWh × 0.8 kg LCE/kWh = 140 kg LCE per event
- Rate: 50% of 4-yr-old + 5-yr-old BEV cohorts per year
- Uplift: +3 kt LCE (2026) → +55 kt (2031) → +110 kt (2036) → +113 kt (2046)
- At steady state: ~33% of total lithium demand
- Total lithium (fleet model) vs stream-forecaster: +32–34% at +10yr/+20yr horizons (mid-life battery uplift not captured in flow-based stream-forecaster)

**Copper:** No mid-life replacement uplift. Fleet model matches stream-forecaster exactly at all horizons.

**Consistency check:** All three fleet models PASS. Floating-point max deviation = 0.01 unit (relative <0.000001%) — artifact only, not a modeling error.

**Why:** The fleet model adds mid-life battery replacement demand that flow-based stream-forecasters miss. This is the key analytical contribution and should be flagged in any commodity synthesis for lithium.

**How to apply:** When running future fleet models for BEV durable goods, always add a mid-life replacement demand layer on top of the stream-forecaster's annual sales figures. For 8-yr lifetime trucks with 50% replacement rate at year 4–5, the steady-state uplift is approximately equal to (0.50 × 2 cohorts × battery intensity / new-truck intensity) of truck-sales lithium demand.
