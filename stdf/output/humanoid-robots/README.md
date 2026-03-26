# STDF Analysis: Humanoid Robot Cost Curve — 20 Years

**Preset:** COST_FOCUS | **Date:** 2026-03-19 | **Confidence:** 0.71

---

## Results Summary

Humanoid robots have already crossed cost parity with US manufacturing labor (2020–2021). The 2024 Unitree G1 at $10.76/hr sits at 25.4% of the $42.40/hr labor benchmark. All 8 capability dimensions for logistics/warehouse met competitive thresholds in 2023–2025. Rupture window: 2026–2030.

| Metric | Value |
|--------|-------|
| Learning rate (service-level) | 23.67%/yr |
| Learning rate (hardware) | 32.07%/yr |
| Cost parity vs labor | Crossed 2020–2021 |
| Cost parity vs industrial arms | Model-derived 2030–2031 |
| Capability convergence | 8/8 dimensions MET (logistics/warehouse) |
| Exponential fit R² | 0.9528 |

---

## Pipeline Execution

| Tier | Agent | Criticality | Status | Confidence |
|------|-------|-------------|--------|------------|
| 1 | cost-researcher | CRITICAL | PASS | 0.72 |
| 1 | capability | HIGH | PASS | 0.72 |
| 2 | cost-fitter | CRITICAL | PASS | 0.70 |
| Final | synthesizer | CRITICAL | PASS | 0.71 |

**Skipped (by preset):** domain-disruption, cost-parity-checker, capability-parity-checker, adoption-readiness-checker, tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst

---

## Validation

| Check | Result |
|-------|--------|
| Banned vocabulary | 0 violations |
| Forecast language | 0 violations |
| Full guardrail check | PASS (all 5 files) |

---

## Output Files

| File | Description | Size |
|------|-------------|------|
| [`00-final-synthesis.md`](00-final-synthesis.md) | Executive summary | 4.7 KB |
| [`agents/02a-cost-researcher.md`](agents/02a-cost-researcher.md) | Raw cost data collection | 23.4 KB |
| [`agents/02b-cost-fitter.md`](agents/02b-cost-fitter.md) | Exponential fit, learning rate, thresholds | 23.8 KB |
| [`agents/03-capability.md`](agents/03-capability.md) | 8-dimension capability benchmark | 24.2 KB |
| [`agents/06-synthesizer.md`](agents/06-synthesizer.md) | Detailed synthesis with conflict resolution | 12.0 KB |

---

## Next Steps

To complete the full 7-phase analysis:
```
/stdf "Humanoid robot disruption of manufacturing labor"
```
This adds: tipping-point synthesis, S-curve adoption modeling, regional dynamics, and incumbent decline analysis.
