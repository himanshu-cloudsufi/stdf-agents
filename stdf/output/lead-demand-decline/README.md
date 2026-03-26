# STDF Analysis — Lead (Pb) Demand Decline via Lithium-Ion Battery Disruption

**Preset:** FULL+COMMODITY | **Agents:** 16/16 | **Date:** 2026-03-20
**Output directory:** `output/lead-demand-decline`
**Mean confidence:** 0.82 | **Guardrail validation:** 17/17 PASS

---

## Pipeline Execution Summary

| Agent | Confidence | Status | Duration (s) | Output File |
| --- | --- | --- | --- | --- |
| stdf-domain-disruption | 0.82 | OK | 0.0 | [agents/01-domain-disruption.md](agents/01-domain-disruption.md) |
| stdf-cost-researcher | 0.88 | OK | 0.0 | [agents/02a-cost-researcher.md](agents/02a-cost-researcher.md) |
| stdf-cost-fitter | 0.87 | OK | 0.0 | [agents/02b-cost-fitter.md](agents/02b-cost-fitter.md) |
| stdf-capability | 0.82 | OK | 0.0 | [agents/03-capability.md](agents/03-capability.md) |
| stdf-cost-parity-checker | 0.87 | OK | 0.0 | [agents/04a-cost-parity.md](agents/04a-cost-parity.md) |
| stdf-capability-parity-checker | 0.84 | OK | 0.0 | [agents/04b-cap-parity.md](agents/04b-cap-parity.md) |
| stdf-adoption-readiness-checker | 0.82 | OK | 0.0 | [agents/04c-adopt-readiness.md](agents/04c-adopt-readiness.md) |
| stdf-tipping-synthesizer | 0.82 | OK | 0.0 | [agents/04d-tipping-synthesizer.md](agents/04d-tipping-synthesizer.md) |
| stdf-scurve-fitter | 0.82 | OK | 0.0 | [agents/05a-scurve-fitter.md](agents/05a-scurve-fitter.md) |
| stdf-regional-adopter | 0.75 | OK | 0.0 | [agents/05b-regional-adopter.md](agents/05b-regional-adopter.md) |
| stdf-xcurve-analyst | 0.74 | OK | 0.0 | [agents/05c-xcurve-analyst.md](agents/05c-xcurve-analyst.md) |
| stdf-synthesizer | 0.82 | OK | 0.0 | [agents/06-synthesizer.md](agents/06-synthesizer.md) |
| stdf-demand-decomposer | 0.85 | OK | 0.0 | [agents/07a-demand-decomposer.md](agents/07a-demand-decomposer.md) |
| stdf-stream-forecaster | 0.82 | OK | 0.0 | [agents/07b-stream-forecaster.md](agents/07b-stream-forecaster.md) |
| stdf-fleet-modeler | 0.80 | OK | 0.0 | [agents/07c-fleet-modeler.md](agents/07c-fleet-modeler.md) |
| stdf-regional-demand-analyst | 0.74 | OK | 0.0 | [agents/07d-regional-demand.md](agents/07d-regional-demand.md) |

## Output Files

- [Final Synthesis](00-final-synthesis.md)
- [stdf-domain-disruption](agents/01-domain-disruption.md)
- [stdf-cost-researcher](agents/02a-cost-researcher.md)
- [stdf-cost-fitter](agents/02b-cost-fitter.md)
- [stdf-capability](agents/03-capability.md)
- [stdf-cost-parity-checker](agents/04a-cost-parity.md)
- [stdf-capability-parity-checker](agents/04b-cap-parity.md)
- [stdf-adoption-readiness-checker](agents/04c-adopt-readiness.md)
- [stdf-tipping-synthesizer](agents/04d-tipping-synthesizer.md)
- [stdf-scurve-fitter](agents/05a-scurve-fitter.md)
- [stdf-regional-adopter](agents/05b-regional-adopter.md)
- [stdf-xcurve-analyst](agents/05c-xcurve-analyst.md)
- [stdf-synthesizer](agents/06-synthesizer.md)
- [stdf-demand-decomposer](agents/07a-demand-decomposer.md)
- [stdf-stream-forecaster](agents/07b-stream-forecaster.md)
- [stdf-fleet-modeler](agents/07c-fleet-modeler.md)
- [stdf-regional-demand-analyst](agents/07d-regional-demand.md)

## Key Conclusion

Global lead demand drops 10% below its 2024 baseline of 12,259 kt by 2027 (median path, scenario range 2027.4-2028.8). The decline is driven by five parallel disruption vectors: BEV displacement of ICE vehicles (eliminating SLI battery demand), LFP-UPS displacing VRLA in telecom and datacenter, EV forklifts displacing lead-acid traction, and emerging LFP SLI aftermarket substitution. Non-SLI segments (37.5% of demand) have already tipped; automotive SLI (62.5%) tips regionally from 2026-2032. The structural floor is approximately 6,276 kt by 2046.

## Guardrail Validation

All 17 output files pass full guardrail checks: zero banned vocabulary, zero banned sources, zero forecast language violations, zero anti-patterns.

## Agents Skipped

None — FULL+COMMODITY preset uses all 16 agents.

## Critical Path (Tier Structure)

| Tier | Agents | Mode |
|------|--------|------|
| 1 | domain-disruption, cost-researcher, capability | Parallel |
| 2 | cost-fitter | Sequential |
| 3 | cost-parity-checker, capability-parity-checker, adoption-readiness-checker | Parallel |
| 4 | tipping-synthesizer | Sequential |
| 5a | scurve-fitter | Sequential |
| 5b | regional-adopter, xcurve-analyst | Parallel |
| 6a | demand-decomposer | Sequential |
| 6b | stream-forecaster | Sequential |
| 6c | fleet-modeler, regional-demand-analyst | Parallel |
| Final | synthesizer | Sequential |

## Lead Demand Trajectory

| Year | Demand (kt) | vs. 2024 Baseline |
|------|------------|-------------------|
| 2024 | 12,259 | baseline |
| 2026 | 11,095 | -9.5% |
| **2027** | **~11,033** | **-10.0%** |
| 2031 | 9,205 | -24.9% |
| 2036 | 7,272 | -40.7% |
| 2046 | 6,276 | -48.8% |
