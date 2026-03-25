---
name: reference_ai_cognitive_labor_catalog_coverage
description: Catalog coverage for AI disruption of cognitive labor analysis; AI inference cost curves, GPU pricing, training costs, labor impact data, BLS OEWS sources for knowledge worker wages
type: reference
---

## Catalog Coverage — AI / Artificial Labor (AL) Disruption of Cognitive Labor

### AI Inference Cost Curves (Tier 2, T1 provenance)

- `data/artificial_intelligence/cost/Artificial_General_Intelligence_Average_Token_Cost_Global.json` — AGI average token cost 2021–2025, $/M tokens, source "Database" (5 clean annual points)
- `data/artificial_intelligence/cost/Artificial_Intelligence_Inference_Price_(GPT-3.5)_Global.json` — GPT-3.5 pricing 2023–2024, $/M tokens, source Stanford/Epoch AI
- `data/artificial_intelligence/cost/Artificial_Intelligence_Inference_Price_(GPT-4)_Global.json` — GPT-4 pricing 2023–2024, $/M tokens, source Stanford/Epoch AI

### GPU Cloud Pricing (Tier 2, T3 provenance — cloud market aggregators)

- `data/artificial_intelligence/cost/GPU_NVIDIA_Tesla_V100_Cloud_On-Demand_Price_Global.json` — V100 $/hr 2018–2025
- `data/artificial_intelligence/cost/GPU_NVIDIA_A100_Tensor_Core_Cloud_On-Demand_Price_Global.json` — A100 $/hr 2020–2025
- `data/artificial_intelligence/cost/GPU_NVIDIA_H100_Tensor_Core_Cloud_On-Demand_Price_Global.json` — H100 $/hr 2022–2025

### Training Cost Curves (Tier 2, T1 provenance — Epoch AI)

- `data/artificial_intelligence/cost/Artificial_Intelligence_Cloud_Compute_Cost_for_Training_Global.json` — Cloud training cost per run 2016–2023, $
- `data/artificial_intelligence/cost/Artificial_Intelligence_Amortized_hardware_and_energy_cost_for_Training_Global.json` — Amortized HW+energy training cost 2016–2023, $
- **CRITICAL WARNING:** Training costs are INCREASING over time (3.5x/year per Epoch AI). Do NOT use as the disruption cost curve. Use inference costs instead.

### GPU Performance per Dollar (Tier 2, T1 provenance — Epoch AI)

- `data/artificial_intelligence/performance_benchmark/Artificial_Intelligence_Max_GPU_Computational_Performance_Per_Dollar_Global.json` — FLOP/s per constant 2024 USD, 2008–2022

### Agentic AI Cost Curves (Tier 2, source "Database")

- `data/agentic_ai/cost/Agentic_AI_Deployment_Cost_Global.json` — Total deployment cost 2021–2025, $ (aggregate market metric, NOT $/token — caution for parity analysis)
- `data/agentic_ai/cost/Agentic_AI_Hardware_Cost_Global.json` — Hardware cost 2021–2025, $
- `data/agentic_ai/cost/Agentic_AI_Software_Cost_Global.json` — Software cost 2021–2025, $
- Regional variants available for USA, China, Europe, Rest of World

### Labor Impact Curves (Tier 2, source Stanford)

- `data/artificial_intelligence/labor_impact/` — Normalized headcount (employment change index) for: Customer Service, Software Developer, Service Clerk, Marketing/Sales Manager, Stock Clerk, Health Aides, First-Line Production Supervisors — all USA, by career stage age group, normalized to Oct 2022 = 1.0
- These are EMPLOYMENT LEVEL indices, not wage/cost data. Useful for capability parity and adoption agents, not cost parity.

## Incumbent Data — NOT in Catalog

Knowledge worker wages are NOT in the local catalog. Must be web-sourced from BLS OEWS (T1).

### Key BLS OEWS Sources Used (T1)

- Software Developers (SOC 15-1252): Mean $99K–$133K range 2012–2024 (slowly rising, ~3% CAGR)
- Customer Service Reps (SOC 43-4051): Mean $33K–$43K range 2015–2024 (~2.5% CAGR)
- Paralegals (SOC 23-2011): Mean $52K–$65K range 2015–2024 (~2.7% CAGR)
- Financial Analysts (SOC 13-2051): Only 2024 median retrieved ($101,350) — time series gap

## Key Unit Confusion Patterns

1. **$/1K tokens vs. $/M tokens**: OpenAI historical pricing is quoted per 1K tokens. Catalog and Stanford AI Index use $/M tokens. Always convert: multiply per-1K price × 1000 to get $/M.
2. **AGI average vs. MMLU-parity floor**: The catalog "average" ($0.50/M tokens in 2025) is across all frontier models. The Stanford MMLU-parity floor ($0.07/M tokens in Oct 2024) represents the cheapest capable model. Both are valid but measure different things.
3. **Training cost vs. inference cost**: Training costs are INCREASING. Inference costs are DECREASING. The disruption thesis relies on inference costs. Never conflate them.
4. **Annual wage vs. hourly**: BLS OEWS uses 2,080 hours/year for annualization. Always note conversion.

## Historical AI Pricing Anchors (T3 web sources)

- GPT-3 Davinci original launch (2020–2021): $0.06/1K tokens = $60/M tokens
- GPT-3 Davinci after Sep 2022 price cut: $0.02/1K tokens = $20/M tokens
- GPT-3.5 Turbo launch (Mar 2023): $0.002/1K tokens = $2/M tokens
- Stanford AI Index headline: 280x decline from $20/M (Nov 2022) to $0.07/M (Oct 2024) at MMLU parity

## Stanford AI Index 2025 Key Data Points

Source: https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development
- Nov 2022: $20/M tokens for MMLU-parity (GPT-3.5 class)
- Oct 2024: $0.07/M tokens for MMLU-parity (Gemini-1.5-Flash-8B)
- May 2024: $15/M tokens for GPQA >50% level
- Dec 2024: $0.12/M tokens for GPQA >50% level (Phi-4)
- Hardware cost declining 30%/year; energy efficiency improving 40%/year
