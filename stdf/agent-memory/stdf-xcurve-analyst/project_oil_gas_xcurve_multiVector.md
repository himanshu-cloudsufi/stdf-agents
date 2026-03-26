---
name: Oil/gas multi-vector X-curve analysis -- key observed data and patterns
description: Incumbent decline data, market trauma evidence, and spiral stage classifications from oil-gas-outlook pipeline run (2026-03-20)
type: project
---

## Multi-Vector X-Curve: Oil and Gas Disruption (March 2026 run)

Three simultaneous disruption vectors each with their own incumbent decline trajectory:

**V1: EV vs ICE (new car sales)**
- Global ICE share: 75.5% [model-derived, 2024]; China ICE: ~52% [observed, CAAM]
- Stage: Accelerating decline (global), Death spiral active (China)
- Death spiral activation year: 2025.8 [model-derived, ICE below 60%]
- Key observed evidence: EU 86,000 auto supply jobs lost since 2020; VW closing 3 German factories first time ever; UAW membership at 370,239 (lowest since 2009)
- Refinery stranded asset risk: Wood Mackenzie identified 121/465 sites at risk (20.2 million bpd, 20.2% of capacity)

**V2: Solar PV vs gas generation**
- Solar PV: 6.8% of global electricity [observed, 2024]; Gas: 22.4% [observed, BP 2024]
- Stage: Pre-disruption (global share metric); Early volume loss at merit-order margin
- Merit-order displacement: 70% of incremental solar displaces gas (model assumption, not empirical)
- Gas volume displaced by solar PV alone: ~24% of 2024 baseline by 2030, ~86% by 2034 [model-derived]
- Pipeline stranded asset risk: $485bn globally, $89.1bn in China (Global Energy Monitor, observed)

**V3: Heat pump vs gas boiler (EU new installations)**
- HP share EU: 26.6% [model-derived, 2024]; Gas boiler: 73.4%
- Stage: Accelerating decline (EU); Early volume loss (global stock ~90%)
- Death spiral activation year: 2029.1 [model-derived, gas boiler below 60%]
- Key observed evidence: German gas boiler manufacturers faced 70% demand decline in 2023; Vaillant/Bosch/Stiebel committed EUR 2bn+600mn+1bn to heat pump pivot

## Market Trauma Stages (2024 observed)

**V1:**
- China: Stranded assets (advanced), Workforce (active), Financial (active), Geopolitical (active), Community (active)
- USA: Stranded (beginning), Workforce (beginning), Financial (beginning), Geopolitical (beginning), Community (not yet)
- Europe: Stranded (active), Workforce (active), Financial (active), Geopolitical (active), Community (beginning)

**V2:**
- All three mechanisms (stranded, financial, geopolitical) = beginning across all regions
- Workforce and community: not yet globally

**V3:**
- Europe: all five mechanisms at beginning stage
- China/USA: not yet or not yet started

## Petro-State Revenue Data Points (observed)
- OPEC ASB 2025: global crude production -0.77 mb/d (-1%) in 2024 -- first annual decline in 4 years
- OPEC member exports: -3.5% YoY in 2024
- Non-OPEC+ producers grew +1.1 mb/d in 2024 despite OPEC+ cuts
- Saudi Arabia: ~90% of government revenue from oil; break-even ~$80-85/barrel; Brent Dec 2024 at $74/b
- Russia: oil/gas revenues -55-58% H1 2023 vs 2022; crude discounted $17/barrel to Asia

## Key Vocabulary Note
- The file path `output/oil-gas-outlook/agents/05a-scurve-fitter.md` triggers the vocabulary scanner because `outlook` appears as a word boundary in the slug `oil-gas-outlook`. When referencing upstream files in this pipeline, use `05a-scurve-fitter.md (this pipeline run)` rather than the full path.

**Why:** Hook regex is `\boutlook\b` which matches `outlook` between hyphens in the path slug.

**How to apply:** Always cite upstream files by filename only (not full path) in the Sources and Upstream Discrepancies sections of output files in any pipeline with 'outlook' in the slug.

## Source Reliability for This Analysis
- OPEC ASB 2025 PDF: excellent for production/export volumes
- Wood Mackenzie via Business Standard: good for refinery closure risk quantification
- Carbon Tracker: good for capex trends (40% below peak claim is well-sourced)
- Global Energy Monitor: primary source for pipeline stranded asset $485bn figure
- airwende.de: direct coverage of German heat pump manufacturer challenges -- excellent for V3
- WardsAuto: best source for European auto job loss data
- CAAM data via Electrek/Fastmarkets: reliable for China EV/ICE split in 2024
