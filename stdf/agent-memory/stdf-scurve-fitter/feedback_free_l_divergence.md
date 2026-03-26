---
name: Free-L Divergence for Pre-Inflection Data
description: Free-L logistic fitting diverges when all data points are pre-inflection; always fix L for early-stage S-curves
type: feedback
---

When fitting a logistic S-curve where all observed data points fall before the inflection (x0), the free-L optimizer will diverge to astronomically large L values (e.g., 9.7 million% for BEV trucks China 2020-2025). This is mathematically correct behavior — the optimizer cannot distinguish a curve approaching 90% from one approaching 9,700,000% using only the exponential growth phase.

**Why:** Demonstrated on BEV heavy trucks China (2020-2025, 6 data points, all pre-inflection at x0≈2026.6). Free-L produced L=9,699,640%, k=0.6278, x0=2045 — clearly nonsensical.

**How to apply:** For any technology where current adoption < 30-40% and no post-inflection data exists, always fix L based on domain knowledge before running fit_scurve. Run free-L first as a diagnostic — if L >> 200%, it has diverged. Then fix L and report it with justification. Run L sensitivity at 3 scenarios (conservative/primary/optimistic). Typically ±5pp from primary L covers the range.
