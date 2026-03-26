---
name: Tony's marginal cost framework — override for energy disruption analyses
description: Tony rejects LCOE as the primary metric; use marginal cost as the decisive competitive threshold in energy analyses
type: feedback
---

**Rule:** When Tony overrides the cost metric to "marginal cost," the decisive threshold is when SWB's amortized capital cost per MWh falls BELOW the incumbent's marginal fuel+O&M cost per MWh.

**Why:** Tony's framing is that SWB wins when it's cheaper to BUILD NEW SWB from scratch than to just pay the fuel bill on an existing incumbent asset. This is the economic kill condition for the incumbent — not when new SWB beats new incumbent on LCOE, but when new SWB beats the running cost of the already-sunk incumbent. LCOE comparisons are useful context but not the primary signal.

**How to apply:**
- Compute two thresholds: (1) SWB amortized capex vs. SOFC/gas marginal cost — Tony's primary threshold; (2) SWB amortized capex vs. full incumbent LCOE — secondary / standard comparison
- Frame the primary result as: "At this crossover, building new SWB is cheaper than paying the fuel bill on an existing [incumbent]"
- SOFC marginal cost formula: `(NG_$/MMBtu / (293.07 × efficiency)) × 1000 + variable_O&M_$/MWh`
- Use variable O&M only in marginal cost (fixed O&M is sunk); acknowledge that the fixed/variable O&M split is often unobserved and must be estimated
- Note: Tony's threshold typically arrives 8–12 years LATER than the standard LCOE parity year because the incumbent marginal cost is much lower than its full LCOE
