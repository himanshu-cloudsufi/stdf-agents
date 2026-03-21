---
name: BEV Heavy Trucks China S-Curve Parameters
description: Fitted logistic S-curve parameters for BEV heavy truck adoption in China, 2020-2025 data, output file 05a-scurve-fitter.md
type: project
---

Fitted S-curve for BEV heavy truck (49t GVW) market share of new HDT sales in China.

**Primary parameters (L=90 fixed):**
- L = 90.0% (fixed; free-L diverges for pre-inflection data)
- k = 0.7227 (1-sigma ±0.0381)
- x0 = 2026.59 (1-sigma ±0.12 yr)
- R-squared = 0.9950
- Data points: 6 (2020–2025)

**Key milestones [model-derived]:**
- 25% adoption: 2025.3
- 50% (inflection): 2026.9
- 80% completion: 2029.5
- Current phase: rapid_growth (22.0% observed H1 2025)

**Historical data points used:**
- 2020: 1.0% | 2021: 2.0% | 2022: 3.5% | 2023: 6.5% | 2024: 11.0% | 2025: 22.0%
- Sources: ICCT March 2025 (2022-2024), IEEFA Aug 2025 (H1 2025)

**Upstream discrepancy with tipping-synthesizer:**
- Synthesizer provisional k=0.30 vs fitted k=0.7227 (2.41x steeper) — due to synthesizer lacking H1 2025 data point
- Synthesizer provisional 80% year = 2031.6; fitted = 2029.5 (2.1 yr earlier)
- Fitted parameters supersede synthesizer provisionals per downstream agent protocol

**Catalog corroboration:**
- `data/commercial_vehicle/adoption/Commercial_Vehicle_(EV)_Annual_Sales_China.json` (Database/Rethinkx) — all-commercial EV share 3.47% (2022), 5.98% (2023), 9.08% (2024) confirms trend direction
- HDT BEV adoption outpacing all-commercial EV by 1.01-1.21x (2022-2024)

**L justification:** 10% residual for Western China remote corridors (no swap coverage by 2030), oversize/hazmat loads, cold-chain apps, long-term LNG supply contracts. More conservative than synthesizer's L=95.

**Why:** BEV HDT China is a live rapid-growth S-curve case study with excellent data quality (R²=0.9950). Parameters are well-constrained except L (domain assumption). Downstream agents should use these parameters, not synthesizer provisionals.

**How to apply:** In future bev-trucks-china analyses, start with L=90 as primary, k≈0.72, x0≈2026.6. Watch for post-2025 data to constrain L empirically.
