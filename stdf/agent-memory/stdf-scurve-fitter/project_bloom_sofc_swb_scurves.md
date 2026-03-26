---
name: Bloom Energy SOFC SWB Disruption S-Curve
description: Fitted S-curve for SWB share in enterprise reliability-grade on-site power (Bloom SOFC disruption); proxy series construction method; x0 discrepancy with tipping-synthesizer
type: project
---

S-curve for SWB (solar+BESS) share of new enterprise reliability-grade C&I on-site power procurement (displacing gas-based generation including Bloom SOFC).

**Fitted parameters (L=70 fixed):** k=0.1960 (+/-0.0072), x0=2034.7 (+/-0.48 years), R²=0.9927, RMSE=0.165pp, 9 data points (2016-2024).

**Key milestone years:**
- 10% share: 2025.6 (already in tipping zone)
- 25% share: 2031.7 (±0.1yr across L scenarios — very stable; aligned with LCOE parity 2031-2032)
- 50% share: 2039.4 (±0.8yr from L sensitivity)
- ~66% practical saturation: 2049.7

**Short thesis entry window (2028-2030):** SWB at 14.8-19.9% share [model-derived]

**Proxy construction method:**
- Market = SWB-capable (solar + 8-hour-grade BESS) / (SWB + gas CHP/SOFC ~700 MW/yr)
- NOT all commercial solar — only co-deployed solar+BESS 24/7-reliability fraction
- C&I BESS 145 MW in 2024 (ACP/Wood Mackenzie observed); gas base from DG survey [CAUTION: EIA source]
- Commercial solar 2,118 MWdc (SEIA 2024 YIR observed)
- Current share 7.5% (2024) — tipping phase (5-15% boundary)

**x0 discrepancy with tipping-synthesizer:** Provisional x0=2031.5 vs fitted x0=2034.7 (+3.2yr). Reason: tipping-synthesizer set x0 as cost parity year (trigger); data fit shows mathematical inflection (50% of L=35% share) lags trigger by ~3yr due to enterprise multi-year procurement cycles. Both values correct for their roles.

**Free-L behavior:** Converged to L=20.4% (economically implausible). All 9 data points are pre-inflection. Fixed L=70 per domain knowledge and feedback_free_l_divergence rule.

**Why:** Bloom Energy SOFC short thesis analysis, analysis date 2026-03-25.

**How to apply:** When analyzing enterprise-grade on-site power disruptions (fuel cells, gas CHP, gensets), use this proxy construction approach. The key insight: the "enterprise reliability-grade" segment is a small fraction of total C&I solar — denominator must reflect gas-based alternatives (~700 MW/yr new builds), not all C&I new capacity.
