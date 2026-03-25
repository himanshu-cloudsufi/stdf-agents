---
name: humanoid-robots-cost-fit-2026
description: Validated exponential fit parameters, learning rates, conversion assumptions, and threshold years for humanoid robot cost analysis (2026-03-19 run)
type: reference
---

## Humanoid Robot Cost Curve — Validated Parameters

**Primary fit:** Commercial-era service-level $/hr, 2013–2024
- C0 = 305.60 $/hr, r = 0.2701/yr, ref_year = 2013, R² = 0.9528
- Learning rate: 23.67%/year (service-level); 32.07%/year (hardware $/unit)

**Service-level unit:** $/hour-equivalent (cost of one hour of general factory labor)

**Conversion formula:** $/hr = hardware_cost / (depr_life × util_hrs_yr) + maint_cost / util_hrs_yr
- Mid scenario: 7yr life, 3000 hrs/yr, $30K/yr maint
- 2024 G1 ($16K hardware) → $10.76/hr mid; $21.60/hr conservative; $5.40/hr optimistic

**Incumbent:**
- US labor: linear_rising, slope=$0.8196/hr/yr, R²=0.9427, intercept=-1618.72
- Industrial arm: flat at $2.81/hr (75K/unit ÷ 12yr × 4000hr + $5K/yr ÷ 4000hr)

**Thresholds (model-derived):**
- Competitive vs labor: 2020–2021 at $37.50/hr
- Inflection vs labor: 2021–2024 (robot at 50–70% of labor)
- Competitive vs industrial arm: 2030–2031 at $2.81/hr

**Key pitfalls:**
- 2000–2013 R&D plateau makes 5-point full fit low quality (R²=0.7294); use commercial-era only
- 2024 G1 actual ($10.76/hr) is 45% below model — cost curve accelerating; thresholds are conservative
- Maintenance cost time series does not exist pre-2024; only Goldman Sachs 2024 estimate available
- "projected/projection" triggers the forecast language block — use "model output", "forward curve", "model-derived"
