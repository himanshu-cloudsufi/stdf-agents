# STDF Analysis — BEV Displacement of ICE Passenger Vehicles — Tipping Point Analysis

**Preset:** TIPPING_ONLY | **Agents:** 9 of 16 | **Date:** 2026-03-24
**Pipeline Confidence:** 0.88 | **Rupture Window:** 2027–2028

---

## Key Conclusion

BEV will complete global incumbent displacement of ICE passenger vehicles in 2027–2028 (central 2028), with China already past the tipping point in 2024. Regional sequence: China 2024 → Europe 2027 → USA 2028. Binding constraint is co-binding: fleet-average TCO capability parity and USA highway corridor DCFC coverage, both resolving in 2028 from battery cost-curve dynamics at 16.81%/yr.

---

## Pipeline Execution Summary

| Agent | Confidence | Status | Duration (s) | Output File |
| --- | --- | --- | --- | --- |
| stdf-domain-disruption | 0.92 | OK | 629 | [agents/01-domain-disruption.md](agents/01-domain-disruption.md) |
| stdf-cost-researcher | 0.88 | OK | 510 | [agents/02a-cost-researcher.md](agents/02a-cost-researcher.md) |
| stdf-cost-fitter | 0.85 | OK | 381 | [agents/02b-cost-fitter.md](agents/02b-cost-fitter.md) |
| stdf-capability | 0.91 | OK | 434 | [agents/03-capability.md](agents/03-capability.md) |
| stdf-cost-parity-checker | 0.85 | OK | 177 | [agents/04a-cost-parity.md](agents/04a-cost-parity.md) |
| stdf-capability-parity-checker | 0.92 | OK | 245 | [agents/04b-cap-parity.md](agents/04b-cap-parity.md) |
| stdf-adoption-readiness-checker | 0.87 | OK | 865 | [agents/04c-adopt-readiness.md](agents/04c-adopt-readiness.md) |
| stdf-tipping-synthesizer | 0.88 | OK | 356 | [agents/04d-tipping-synthesizer.md](agents/04d-tipping-synthesizer.md) |
| stdf-synthesizer | 0.88 | OK | 744 | [agents/06-synthesizer.md](agents/06-synthesizer.md) |

## Guardrail Validation

**Result: PASS** — 0 critical violations, 32 warnings across 10 files. All files compliant.

## Agents Skipped (TIPPING_ONLY preset)

| Agent | Reason |
| --- | --- |
| stdf-scurve-fitter | Not in TIPPING_ONLY preset |
| stdf-regional-adopter | Not in TIPPING_ONLY preset |
| stdf-xcurve-analyst | Not in TIPPING_ONLY preset |
| stdf-demand-decomposer | Commodity chain — not triggered |
| stdf-stream-forecaster | Commodity chain — not triggered |
| stdf-fleet-modeler | Commodity chain — not triggered |
| stdf-regional-demand-analyst | Commodity chain — not triggered |

## Critical Path (Tier Structure)

```
Tier 1 (parallel):  domain-disruption + cost-researcher + capability
Tier 2 (sequential): cost-fitter ← cost-researcher
Tier 3 (parallel):  cost-parity-checker + cap-parity-checker + adopt-readiness-checker
Tier 4 (sequential): tipping-synthesizer ← all 3 checkers
Final:              synthesizer ← all outputs
```

## Output Files

- [Final Synthesis](00-final-synthesis.md)
- [Domain Disruption](agents/01-domain-disruption.md)
- [Cost Researcher](agents/02a-cost-researcher.md)
- [Cost Fitter](agents/02b-cost-fitter.md)
- [Capability](agents/03-capability.md)
- [Cost Parity](agents/04a-cost-parity.md)
- [Capability Parity](agents/04b-cap-parity.md)
- [Adoption Readiness](agents/04c-adopt-readiness.md)
- [Tipping Synthesizer](agents/04d-tipping-synthesizer.md)
- [Synthesizer](agents/06-synthesizer.md)
