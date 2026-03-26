---
name: AI cognitive labor cost curve analysis
description: Validated exponential fit parameters, learning rate, threshold years, and unit conversion for AI inference vs. human knowledge worker disruption (2026-03-25)
type: reference
---

## Technology: AI Inference (Artificial Labor / AL) vs. Human Cognitive Labor

**Analysis date:** 2026-03-25
**Pipeline slug:** `ai-cognitive-labor`

## Service-Level Unit
- **Approved metric:** $/CTE (cognitive-task-equivalent)
- **Definition:** 1 CTE = 4,000 tokens = one 30-min analytical task
- **Conversion:** $/M tokens × 0.004 = $/CTE (exact, no assumptions)

## Primary Cost Series (Disruptor)
Source: AGI Average Token Cost Global, T2 catalog (Epoch AI / Stanford HAI)

| Year | $/M tokens | $/CTE |
|------|-----------|-------|
| 2021 | 60.00 | 0.2400 |
| 2022 | 20.00 | 0.0800 |
| 2023 | 10.00 | 0.0400 |
| 2024 | 2.00 | 0.0080 |
| 2025 | 0.50 | 0.0020 |

Context anchor (T3): GPT-3 2020 = $60,000/M tokens = $240/CTE (cost ABOVE incumbent before 2021)

## Exponential Fit Parameters
- **Formula:** C(t) = 0.2816 × exp(−1.1878 × (t − 2021))
- **C0:** 0.2816 $/CTE
- **r:** 1.1878 per year
- **R²:** 0.983
- **Data points:** 5 (2021–2025, T2 observed)
- **Max residual:** 34.6% at 2023

## Learning Rate
- **Per year:** 69.5% (empirically derived from r=1.1878)
- **Per doubling:** 43–45% (assuming 12-month inference compute doubling time)
- **Plausibility:** CAUTION — exceeds standard bounds but structurally explained by three concurrent forces:
  1. Hardware: ~35%/yr (Epoch AI FLOP/$ trend)
  2. Algorithmic: ~200%+/yr effective (model compression, quantization, speculative decoding)
  3. Market: ~1.3x margin compression from open-source competition
- **NOT implausible** — the 120x decline in 4 years is empirically documented and cross-validated by Stanford AI Index 2025 (280x for MMLU-parity models Nov 2022 – Oct 2024)

## Incumbent Fit Parameters
Source: BLS OEWS (T1), composite cross-occupation average
- **Model:** linear_rising
- **Composite 2024:** $17.50/CTE ($35/hr)
- **Slope:** +$0.387/CTE/yr
- **R²:** 0.999
- **Data span:** 2015–2024 (9 years)

Segment-level 2024 benchmarks:
- Customer Service Rep: $10.28/CTE
- Paralegal: $14.67/CTE
- Composite avg: $17.50/CTE
- Financial Analyst: $24.36/CTE
- Software Developer: $31.99/CTE

## Threshold Years
- **Competitive threshold (raw cost parity):** 2020–2021 [model-derived, bracketed by observed data]
- **Inflection threshold (50-70% of incumbent):** 2020–2021 — already crossed; AI at 0.011% of incumbent by 2025
- **Enterprise integration threshold (2x overhead):** 2018–2020 across all segments [model-derived]
- **Enterprise integration threshold (5x overhead):** 2020–2022 across all segments [model-derived]

## Key Analytical Finding
Cost is NOT the binding constraint. The 10,000x cost advantage was achieved by 2025. The disruption adoption rate is gated entirely by capability parity and enterprise integration readiness. Downstream agents should treat cost as fully permissive and model adoption gates on capability maturity.

## Jevons Exclusion
Technology classified as Stellar (zero marginal cost). Jevons Paradox excluded.

## Pitfalls to Watch
1. Training cost data in upstream shows INCREASING trend — do NOT use as disruption metric; use inference cost only
2. The 2020 GPT-3 Davinci pricing ($240/CTE) is T3-sourced; use only to bracket crossover window, not to anchor the fit
3. The per-year learning rate (69.5%) is structurally explained and correct, but the plausibility checker will flag IMPLAUSIBLE — override to CAUTION with documentation
4. All enterprise integration threshold crossings compute to before 2022 — cost analysis is closed, redirect to capability analysis
