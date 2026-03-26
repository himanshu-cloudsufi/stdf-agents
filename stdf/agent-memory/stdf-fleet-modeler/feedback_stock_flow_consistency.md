---
name: Stock-Flow Consistency — Floating-Point Artifact
description: lib.demand_math.validate_stock_flow_consistency may return consistent=False due to floating-point accumulation; max_deviation 0.01 on large fleets is PASS
type: feedback
---

`validate_stock_flow_consistency` returns `consistent=False` when max_deviation > 0 (any nonzero). The function flags deviations of 0.01 unit on fleets of millions. This is a floating-point accumulation artifact in the iterative scrappage formula (fleet × 0.125), not a modeling error.

**Why:** Confirmed on three independent fleet models (BEV, LNG, diesel) for China HDT. Max deviation = 0.01 unit at year-indices 7 and 17; relative error <0.000001%. The identity Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) holds to machine precision.

**How to apply:** When the consistency check returns `consistent=False` with `max_deviation` ≤ 0.01, report as PASS in compliance output. Always state the relative deviation, not just the absolute value, so reviewers can confirm it is a rounding artifact rather than a structural error. If max_deviation > 1.0, investigate as a real violation.
