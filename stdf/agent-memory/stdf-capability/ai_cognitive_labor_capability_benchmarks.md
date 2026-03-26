---
name: ai_cognitive_labor_capability_benchmarks
description: AI vs human cognitive labor capability benchmarks — 10 dimensions, all thresholds, trajectories, parity years, and curve fits (validated 2026-03-25)
type: project
---

AI disruption of cognitive labor capability benchmarks. Technology classification: Stellar (AL — Artificial Labor). Jevons Paradox must NOT be applied.

**Why:** AI has zero marginal cost characteristics — no physical throughput constraint. Efficiency gains do not rebound into increased cognitive labor demand in the same way X-Flow technologies would.

**How to apply:** Use these benchmarks as baseline for any future AI/AL capability analysis. Update parity years as new benchmark data becomes available.

---

## Dimension Set (10 dimensions)

| Dimension | AI 2025 | Human Baseline | Threshold | Met | Parity Year |
|-----------|---------|----------------|-----------|-----|-------------|
| coding_quality_humaneval_pct | 100% | 72% | 80% | YES | 2022 |
| reasoning_knowledge_mmlu_pct | 92.3% | 89% | 89% | YES | 2024 |
| math_problem_solving_pct | 97.9% | 90% | 90% | YES | 2024 |
| abstract_reasoning_arc_pct | 75.7% | 85% | 60% | YES | 2024 |
| multimodal_visual_reasoning_pct | 85% | 85% | 75% | YES | 2022 |
| throughput_tokens_per_sec | 1,000 TPS | ~0.06 TPS | 50 TPS | YES | 2023 |
| agentic_task_duration_50pct_reliability_s | 1,800s (30 min) | N/A | 3,600s at 80% | NO | ~2026 [model-derived] |
| inference_cost_per_million_tokens_usd | $0.50/M | N/A | $1.00/M | YES | 2024 |
| availability_hrs_per_year | 8,760 | 2,080 | 8,760 | YES | structural |
| output_consistency_pct_reproducibility | 97% | 82% | 90% | YES | structural |

## Key Trajectories

- HumanEval: 32% (2021) → 100% (2024), linear accelerating, R²=0.781
- MMLU: 33% (2019) → 92.3% (2024), linear, R²=0.969
- MATH: 9% (2021) → 97.9% (2025), linear, R²=0.880
- ARC-AGI: 1% (2019) → 75.7% (2024), exponential, R²=0.895
- Q-AR Multimodal: 15% (2018) → 85% (2024), R²=0.635 [low conf — architecture-era jump 2018→2019]
- TPS throughput: 15 (2021) → 1,000 (2025), exponential, R²=0.996
- HCAST agentic: 3s (2019) → 1,800s (2025), exponential, R²=0.999, doubling every ~7.6 months
- Token cost: $60/M (2021) → $0.50/M (2025), decelerating exponential decline, R²=0.997

## Agentic Task Duration Milestones (model-derived from HCAST exponential)

- 1 hour (3,600s): ~2026
- 8 hours / 1 day (28,800s): ~2028
- 40 hours / 1 week (144,000s): ~2030

## Convergence Pattern

Sequential — core task quality 2022-2024, throughput/cost 2023-2025, extended agentic autonomy 2026.

## Labor Impact Data (Stanford, USA)

- Software developer early career (22-25): headcount declined 17% from 2022-2025 (normalized index 1.0 → 0.83)
- Customer service early career (22-25): headcount declined 11% from 2022-2025 (normalized index 1.0 → 0.89)

## Cost Efficiency

- Code review task (5,000 tokens): $0.0025 AI vs $12.67 human (junior) = 5,067× cost advantage
- AI effective hourly rate: $0.05/hr (2025) vs $35-86/hr human knowledge worker

## Data Sources in Catalog

- Stanford AI Index: data/artificial_intelligence/performance_benchmark/ (6 series)
- METR: data/artificial_intelligence/capability/ (2 series: HCAST and SWE-Bench)
- RethinkX: data/agentic_ai/capability/ (2 series: 50% and 80% reliability)
- Internal DB: data/artificial_intelligence/cost/ and performance_rate/
- Stanford: data/artificial_intelligence/labor_impact/ (labor headcount series by occupation)
