---
name: Confidence Scoring Patterns — Cost Parity Checker
description: How to derive confidence score for cost parity condition from cost-fitter output quality signals
type: feedback
---

Confidence for the cost parity condition should be derived from the primary exponential fit R-squared used to anchor the TCO or price trajectory, not the upstream agent's reported overall confidence score.

Rules observed in practice:
- R-squared >= 0.90 and 5+ data points → HIGH confidence bracket → score in 0.80–0.92 range
- R-squared 0.80–0.90 → MEDIUM → score in 0.65–0.79 range
- R-squared < 0.80 or 3 or fewer data points → LOW → score below 0.65

When cost parity is already confirmed MET by observed data (not forward-curve extrapolation), add +0.05 to 0.10 to the computed confidence — the observed confirmation reduces model risk.

The upstream agent's overall confidence (e.g., 0.74 for bev-trucks-china) should act as a cap or floor check, not the primary input.

**Why:** The cost-fitter often reports a blended confidence that includes data gaps not directly relevant to the parity year determination (e.g., maintenance cost uncertainty). The cost parity checker's confidence should focus specifically on the quality of the fit used to determine the threshold year.

**How to apply:** Always read the specific R-squared for the fit that directly anchors the competitive threshold or TCO crossover, not the agent's headline confidence number.
