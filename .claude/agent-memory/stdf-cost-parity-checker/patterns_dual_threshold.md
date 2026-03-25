---
name: Dual Threshold Pattern — TCO vs. Purchase Price Parity
description: Cost-fitter outputs often include two distinct parity thresholds: service-level TCO and vehicle purchase price. How to handle both.
type: feedback
---

In disruptions where vehicle capital cost is a major TCO component (e.g., heavy trucks, aircraft, industrial equipment), the cost-fitter will often report TWO competitive threshold years:

1. **Service-level TCO parity** — the primary criterion for criterion 5.3. This is the CNY/km (or equivalent) crossover including energy, maintenance, and capital depreciation. This is the binding criterion for MET/NOT_MET/IMMINENT determination.
2. **Purchase-price parity** — an intermediate threshold. Often lags TCO parity because BEV vehicles may have higher upfront cost but lower running costs.

**Pattern observed in bev-trucks-china:** TCO parity crossed 2019–2020 (MET) while purchase-price parity crossed 2024–2025. TCO parity is always the primary determination for criterion 5.3.

**How to apply:** Always anchor the 5.3 status to the service-level TCO threshold. Report purchase-price parity as secondary evidence in the Evidence section. If the cost-fitter only provides purchase price (no TCO), flag this as a data gap and note that the TCO determination is not directly available — lower confidence accordingly.
