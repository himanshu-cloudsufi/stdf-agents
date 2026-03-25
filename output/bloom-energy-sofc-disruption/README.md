# STDF Analysis: Bloom Energy SOFC Disruption by SWB

**Pipeline:** ENERGY_FULL | **Agents:** 13 of 18 (4 commodity skipped, 1 synthesizer) | **Date:** 2026-03-25
**Confidence:** 0.702 | **Rupture Window:** 2028-2032 | **Validation:** CLEAN (0 critical)

---

## Key Conclusion

**Short Bloom Energy in 2028-2030.** Revenue peaks ~$3.0-3.2B in 2027-2028 (AI data center tailwind), then structurally declines as SWB reaches LCOE parity in 2031-2032. The $2.2B convertible note due 2030 compounds equity risk at onset of order collapse. 63-73% stock downside as market re-rates from growth (125x P/E) to declining services annuity (15-20x P/E).

## User Override

Cost metric: **Marginal cost** (not LCOE). Dual thresholds reported throughout.

---

## Execution Summary

| Tier | Agent(s) | Status | Confidence |
|------|----------|--------|------------|
| Tier 1 | domain-disruption, cost-researcher, capability | OK | 0.80, 0.74, 0.74 |
| Gate | Classification approved (marginal cost override) | OK | -- |
| Tier 2 | cost-fitter | OK | 0.72 |
| Tier 3 | cost-parity-checker, cap-parity-checker, adopt-readiness-checker | OK | 0.70, 0.72, 0.74 |
| Tier 4 | tipping-synthesizer | OK | 0.72 |
| Tier 5a | scurve-fitter | OK | 0.62 |
| Tier 5b | regional-adopter, xcurve-analyst, energy-dispatch | OK | 0.52, 0.58, 0.71 |
| Tier 6 | gas-supply-decomposer | OK | 0.82 |
| Final | synthesizer | OK | 0.702 (agg) |

**Skipped:** demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst (commodity chain -- not triggered)

---

## Output Files

| File | Agent | Description |
|------|-------|-------------|
| [00-final-synthesis.md](00-final-synthesis.md) | synthesizer | 7-phase disruption narrative |
| [agents/01-domain-disruption.md](agents/01-domain-disruption.md) | domain-disruption | Disruption map, flow classification, chimeras |
| [agents/02a-cost-researcher.md](agents/02a-cost-researcher.md) | cost-researcher | Historical cost data (SWB + SOFC) |
| [agents/02b-cost-fitter.md](agents/02b-cost-fitter.md) | cost-fitter | Exponential fits, learning rates, dual thresholds |
| [agents/03-capability.md](agents/03-capability.md) | capability | 10-dimension capability benchmarking |
| [agents/04a-cost-parity.md](agents/04a-cost-parity.md) | cost-parity-checker | LCOE parity 2031-2032, marginal kill 2038-2042 |
| [agents/04b-cap-parity.md](agents/04b-cap-parity.md) | cap-parity-checker | PARTIAL -- 6/9 dimensions, parity 2027 |
| [agents/04c-adopt-readiness.md](agents/04c-adopt-readiness.md) | adopt-readiness-checker | NOT_MET -- trajectory 2028 |
| [agents/04d-tipping-synthesizer.md](agents/04d-tipping-synthesizer.md) | tipping-synthesizer | Tipping 2031-2032, short window 2028-2030 |
| [agents/05a-scurve-fitter.md](agents/05a-scurve-fitter.md) | scurve-fitter | L=70, k=0.196, x0=2034.7 |
| [agents/05b-regional-adopter.md](agents/05b-regional-adopter.md) | regional-adopter | USA 2032.5, Korea 2031.3, Europe 2026.8 |
| [agents/05c-xcurve-analyst.md](agents/05c-xcurve-analyst.md) | xcurve-analyst | Revenue peak, death spiral, 63-73% downside |
| [agents/06-synthesizer.md](agents/06-synthesizer.md) | synthesizer | Confidence metadata, conflict resolution |
| [agents/08a-energy-dispatch.md](agents/08a-energy-dispatch.md) | energy-dispatch | On-site merit order, BESS duration pathway |
| [agents/08b-gas-supply.md](agents/08b-gas-supply.md) | gas-supply-decomposer | 0.19% of US gas; fuel cost exposure only |

---

## Guardrail Validation

```
Pipeline validation: CLEAN (117 warnings, 0 critical violations)
All 15 output files passed vocabulary, forecast language, and citation checks.
```

---

## Data Gaps

- No authoritative SOFC capital cost time series (T3 secondary sources only, 6 anchor points)
- No direct enterprise BTM market share series for SWB (proxy construction, scurve-fitter confidence 0.62)
- Korea/Europe enterprise BTM data extremely sparse (regional-adopter confidence 0.52)
- Bloom does not disclose per-kW installed cost or revenue breakdown by end-use segment
- SWB LCOE for 24/7 data center grade has wide geographic uncertainty ($30-70/MWh range)
