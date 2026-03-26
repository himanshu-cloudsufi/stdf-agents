---
name: BEV Heavy Trucks China Regional Adoption (2025)
description: Sub-national regional adoption data for BEV-HDT in China, 5 regions, 2025 market shares and S-curve fits
type: project
---

BEV-HDT China regional breakdown completed 2026-03-20 for pipeline run `bev-trucks-china`.

**Regional market shares (2025, model-derived, scaled to national 22.0% anchor):**
- Eastern China (YRD): 30.3% -- rapid_growth, x0=2026.13 (leader, 0.46yr ahead of global)
- Southern China (PRD): 26.5% -- rapid_growth, x0=2026.44 (0.28yr behind YRD)
- Northern China (BTH): 22.7% -- rapid_growth, x0=2026.57 (matches global, 0.61yr behind YRD)
- Central China (Hubei/Henan/Chongqing): 18.0% -- rapid_growth, x0=2027.09 (1.07yr behind YRD)
- Western China (Sichuan/Yunnan/Xinjiang/Gansu): 9.5% -- tipping, x0=2027.86 (2.24yr behind YRD)

**Global anchor:** L=90, k=0.7227, x0=2026.59 (from 05a-scurve-fitter)

**Key structural drivers per region:**
- YRD: swap infrastructure density, e-commerce captive fleets (JD.com, Cainiao)
- PRD: BYD home territory, Guangdong MIIT records, Shenzhen/Guangzhou port density
- BTH: winter cold penalty -15 to -25% range at -10°C sustains LNG niche; L ceiling 88%
- Central: inland swap gap; longer haul distances; Wuhan/Chongqing hub partially compensates
- Western: sparse infrastructure (SPIC 170 stations announced but not operational 2024); mining haul LNG entrenched; L ceiling 80%

**Data calibration note:** Raw regional shares summed to 23.25% weighted average; scaled by 0.9462 to match 22.0% global. Phase classifications unchanged by scaling.

**Why:** Pipeline run required within-China geographic disaggregation, not standard cross-national (China/USA/Europe). Compliance criterion 4.6 flagged as CONDITIONAL-PASS.

**How to apply:** For future BEV-HDT China runs, use these regional shares as starting priors. Western China data quality remains low-medium -- flag explicitly in any downstream demand decomposition.
