---
name: lead_demand_regional_adoption
description: Regional BEV new-vehicle S-curve fits and phase classifications for lead-demand-decline pipeline run; 2024 observed figures and inflection years per region
type: project
---

BEV new vehicle sales market share and S-curve fits (L=85% fixed, 2024 observed), from Rethinkx catalog [T2]:
- China: 26.82% (rapid_growth), x0=2025.4, k=0.4089, R2=0.9551
- Europe: 18.62% (rapid_growth), x0=2027.2, k=0.3558, R2=0.9548
- USA: 9.15% (tipping), x0=2029.6, k=0.3635, R2=0.9760
- RoW: 4.91% (rupture), x0=2029.6, k=0.4999, R2=0.9941
- India: ~2.1% (rupture), T3 only, no fit

Year-behind-leader (China 2024 = 26.82% = reference):
- Europe: ~1.8 yr behind China
- USA: ~4.1 yr behind China
- RoW: ~4.2 yr behind China

**Why:** Pipeline run for lead acid battery demand decline; BEV-only share is the correct lead displacement metric (not NEV which includes PHEVs)

**How to apply:** When running STDF on any battery or automotive lead-acid disruption, use these 2024 baselines. China NEV=47.9% but BEV=26.82% -- the distinction matters for SLI displacement. Global 11.96% (scurve-fitter) uses a wider denominator than the regional sum of 15.0%.
