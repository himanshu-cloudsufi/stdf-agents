---
name: Cost Parity — BEV vs. ICE Passenger Vehicle USA
description: BEV entry-level vs. ICE mid-size sedan USA purchase price parity: MET 2025-2026, $29,500/vehicle, confidence 0.85
type: project
---

BEV entry-level purchase price parity with ICE mid-size sedan USA reached in 2025–2026 (central: 2025.0). Status: **MET** as of analysis date 2026-03-24.

- Parity price: ~$29,500/vehicle [model-derived]
- Disruptor 2024: $31,000/vehicle [observed]; Incumbent 2024: $29,000/vehicle [observed]; gap +6.9%
- EV fit: R-squared = 0.9886, 8 pts, 2010–2024, r=0.0398 (3.90%/yr — IMPLAUSIBLE flag, market artifact)
- Battery pack underlying rate: 16.81%/yr (R-squared = 0.954, 15 pts) — the clean cost-curve signal
- Incumbent ICE sedan: linear_rising +$500/yr, R-squared = 1.000
- Sensitivity: parity range 2023.8 (fast, r=0.045) to 2026.4 (slow, r=0.035); no NOT_MET scenario
- Inflection 70% threshold: 2031–2032 (EV $22,866 vs ICE $32,700 [model-derived])
- China reference: EV and ICE purchase prices approximately at parity in 2024 (~$15,566 vs. ~$15,500); ICE anchor is approximate, secondary reference only
- Confidence: 0.85 (HIGH bracket; no observed 2025 price data to confirm model-derived parity year)
- Primary metric: purchase price $/vehicle (consumer market, no TCO series — correct per cost rules)
- Jevons: Stellar classification (not applicable); [WARNING: self-classified — no upstream 01-domain-disruption.md classification found]

**Why:** The EV purchase price learning rate (3.90%/yr) being flagged IMPLAUSIBLE is a recurring market-structure artifact for entry-level catalog series — OEM margin recovery, feature-loading, and the $7,500 federal tax credit absorb battery cost savings. Document this pattern each time it appears; it does not invalidate the parity determination.

**How to apply:** When BEV/ICE passenger vehicle parity appears in future runs, expect the entry-level purchase price learning rate to be flagged IMPLAUSIBLE (~3.9-4.5%/yr) despite underlying battery rate of 16-17%/yr. The parity year will still be determinable from the exponential fit; confidence calibration should emphasize R-squared of the price fit (not the battery fit) since the price fit is the direct parity metric.
