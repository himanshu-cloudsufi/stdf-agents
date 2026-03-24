# STDF Analysis: BEV Truck Costs in China

**Preset:** QUICK | **Agents:** 3/16 | **Date:** 2026-03-20 | **Pipeline Confidence:** 0.815

---

## Key Conclusion

BEV heavy trucks are achieving market-driven disruption of diesel incumbents in China through structural cost-curve dynamics in LFP battery packs. Per-km energy cost parity was crossed before 2019 (35.7% BEV advantage in 2024). Purchase price parity crossed in 2024 for 282 kWh short-haul tractors; 440 kWh long-haul tractors on trajectory to parity in 2026–2027. LFP battery packs declined 91.5% from $1,100/kWh (2010) to $94/kWh (2024) with 16.66%/yr learning rate.

**Rupture Window:** UNAVAILABLE — requires FULL preset
**Tipping Year:** UNAVAILABLE — requires FULL preset

---

## Agent Results

| Agent | Confidence | Status | Duration | Output File |
|-------|-----------|--------|----------|-------------|
| stdf-cost-researcher | 0.82 | OK | 627s | [02a-cost-researcher.md](agents/02a-cost-researcher.md) |
| stdf-cost-fitter | 0.81 | OK | 324s | [02b-cost-fitter.md](agents/02b-cost-fitter.md) |
| stdf-synthesizer | 0.815 | OK | 598s | [06-synthesizer.md](agents/06-synthesizer.md) |

**Total pipeline duration:** ~26 min

## Output Files

- [Final Synthesis](00-final-synthesis.md) — Executive summary and full cost analysis
- [Cost Researcher](agents/02a-cost-researcher.md) — Raw cost data collection (21 purchase price + 10 fuel price data points)
- [Cost Fitter](agents/02b-cost-fitter.md) — Exponential fits, learning rates, competitive thresholds
- [Synthesizer](agents/06-synthesizer.md) — Agent metadata and confidence breakdown

---

## Guardrail Validation

| File | Status |
|------|--------|
| 00-final-synthesis.md | PASS |
| agents/02a-cost-researcher.md | PASS |
| agents/02b-cost-fitter.md | PASS |
| agents/06-synthesizer.md | PASS |

**Result:** 4/4 files pass all guardrails (banned vocabulary, forecast language, source attribution)

---

## Critical Path

```
Tier 1: cost-researcher (CRITICAL)
  └─→ Tier 2: cost-fitter (CRITICAL)
        └─→ Final: synthesizer (CRITICAL)
```

All 3 agents sequential — no parallelism possible in QUICK preset.

---

## Agents Skipped (not needed for QUICK preset)

| Agent | Criticality | Reason |
|-------|-------------|--------|
| stdf-domain-disruption | HIGH | Not in QUICK DAG |
| stdf-capability | HIGH | Not in QUICK DAG |
| stdf-cost-parity-checker | CRITICAL | Not in QUICK DAG |
| stdf-capability-parity-checker | HIGH | Not in QUICK DAG |
| stdf-adoption-readiness-checker | HIGH | Not in QUICK DAG |
| stdf-tipping-synthesizer | CRITICAL | Not in QUICK DAG |
| stdf-scurve-fitter | HIGH | Not in QUICK DAG |
| stdf-regional-adopter | MEDIUM | Not in QUICK DAG |
| stdf-xcurve-analyst | MEDIUM | Not in QUICK DAG |
| stdf-demand-decomposer | CRITICAL | Not in QUICK DAG (commodity) |
| stdf-stream-forecaster | HIGH | Not in QUICK DAG (commodity) |
| stdf-fleet-modeler | MEDIUM | Not in QUICK DAG (commodity) |
| stdf-regional-demand-analyst | HIGH | Not in QUICK DAG (commodity) |

---

## Data Flags

- T3 CNY transaction fit R²=0.753 — below 0.80 quality threshold (only 4 data points, 2021–2024)
- No LNG truck price series available — competing technology (~29% China HCV share) not modeled
- No pre-2020 T3 observed transaction anchors
- No maintenance cost time series
