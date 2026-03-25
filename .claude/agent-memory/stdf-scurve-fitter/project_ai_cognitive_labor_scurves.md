---
name: AI Cognitive Labor S-Curve Parameters
description: Fitted S-curve parameters for AI substitution of human cognitive labor (05a); key data construction methodology and upstream discrepancies
type: project
---

**Analysis date:** 2026-03-25
**Output:** `output/ai-cognitive-labor/agents/05a-scurve-fitter.md`

## Fitted Parameters (Primary)
- L = 88% (fixed -- 12% structurally resistant: legal liability, medical diagnosis, in-person care)
- k = 0.5903 (empirically fitted; steeper than physical disruptions)
- x0 = 2028.6
- R-squared = 0.9910
- Data points: 7 (2019-2025)

## Key Upstream Discrepancy
Tipping-synthesizer estimated provisional k=0.35 (Big Bang pattern assumption). Empirical fit returns k=0.5903. The R-squared for k=0.35 forced to data is 0.8772 vs 0.9910 for empirical fit. The steeper k is explained by Stellar technology (zero marginal cost, no infrastructure buildout lag) -- adoption is supply-unconstrained unlike physical disruptions. The discrepancy is correctly flagged in the output as an upstream discrepancy.

## Data Construction Note
No direct primary-source time series for "cognitive task substitution share" exists. The 2019-2025 series is a constructed proxy triangulated from:
- McKinsey State of AI surveys (T3, annual) for enterprise deployment depth
- GitHub Copilot code share (46% among active users in 2025, T3)
- Clio 2024 Legal Trends Report (T3)
- BLS labor market data (T1) as sanity check

Key calibration: "using AI tools" (augmentation) != "AI substituting labor" (substitution). 2025 anchor of 9.0% discounts enterprise tool adoption rate (78%) by deployment depth (~17% EBIT impact firms) and task weighting.

## Projections (Primary L=88)
- 5yr (2031): 70.6% [66.9%, 74.0%]
- 10yr (2036): 86.9% [86.3%, 87.3%]
- 20yr (2046): 88.0%
- 80% completion: 2032.5 (range 2031.8-2034.0 from L uncertainty)

## Phase Classification
- 2025: tipping (9.0%, in 5-15% band)
- 2026: tipping/rapid_growth boundary (~13.2% model-derived; 15% threshold crossed ~Q4 2025)
- 5% threshold crossed: 2023.9
- 50% threshold crossed: 2029.1

## L Sensitivity
- L=83: k=0.5926, x0=2028.5, 80% yr=2034.0
- L=88 primary: k=0.5903, x0=2028.6, 80% yr=2032.5
- L=93: k=0.5884, x0=2028.7, 80% yr=2031.8

## Lessons
- Free-L diagnostic returned L=14.4%, confirming pre-inflection divergence (consistent with feedback memory on this issue)
- The "using AI tools" vs "AI substituting tasks" distinction is analytically critical for this sector -- always clarify metric definition
- McKinsey State of AI is best available T3 source for annual enterprise AI adoption anchors

**Why:** AI cognitive labor is a novel disruption type with no direct primary-source market share timeseries. Future analyses will face the same measurement problem.
**How to apply:** When no direct market share series exists, construct a proxy series from multiple T1/T3 anchors and document the construction methodology explicitly. The constructed series should be calibrated against measurable sector proxies.
