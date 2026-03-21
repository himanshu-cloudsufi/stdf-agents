# STDF v2 Analysis: Electric Vehicles vs ICE

**Generated:** 2026-03-13 | **Pipeline Confidence:** 0.857 (HIGH)

---

## Files

### Final Output
- [`00-final-synthesis.md`](./00-final-synthesis.md) — Full 7-phase STDF narrative with executive summary, regional outlook, and risk analysis

### Individual Agent Outputs (with reasoning + trace links)

| # | Agent | File | Confidence | Agent ID (Trace) |
|---|-------|------|-----------|------------------|
| 1 | Domain Disruption | [`agents/01-domain-disruption.md`](./agents/01-domain-disruption.md) | 0.87 | `a0ca485d5a786f311` |
| 2 | Cost Curve | [`agents/02-cost-curve.md`](./agents/02-cost-curve.md) | 0.88 | `a1a903b0efbab9b21` |
| 3 | Capability | [`agents/03-capability.md`](./agents/03-capability.md) | 0.87 | `a57735a87cab6ece3` |
| 4 | Tipping Point | [`agents/04-tipping-point.md`](./agents/04-tipping-point.md) | 0.86 | `a8be9d190317fb23a` |
| 5 | Adoption S-Curve | [`agents/05-adoption-scurve.md`](./agents/05-adoption-scurve.md) | 0.78 | `a11acd034ec2b7eec` |
| 6 | Synthesizer | [`agents/06-synthesizer.md`](./agents/06-synthesizer.md) | 0.857 (agg) | `a4ae6060fbd62f110` |

### Resuming Agents

Each agent can be resumed for follow-up work using its Agent ID:

```
# Example: resume the cost curve agent for deeper analysis
Agent(resume="a1a903b0efbab9b21", prompt="Drill deeper into solid-state battery cost projections")
```

## Pipeline Execution Summary

```
Phase 1 (parallel):
  ├── domain-disruption  ✅ 387s  confidence=0.87  (stdf-domain-disruption agent type)
  ├── cost-curve         ✅ 358s  confidence=0.88  (general-purpose — agent type not registered)
  └── capability         ✅ 412s  confidence=0.87  (general-purpose — agent type not registered)

Phase 2 (sequential):
  └── tipping-point      ✅ 310s  confidence=0.86  (general-purpose)

Phase 3 (sequential):
  └── adoption-scurve    ✅ 295s  confidence=0.78  (general-purpose)

Synthesis:
  └── synthesizer        ✅ 139s  confidence=0.857 (general-purpose)

Total pipeline time: ~32 minutes (wall clock, with Phase 1 parallelism)
Total tokens consumed: ~227,572
No CRITICAL failures. No confidence penalties applied.
```

## Key Conclusion

> The question is no longer whether EVs displace ICE, but at what regional pace and which incumbents survive the transition.

**Rupture Window:** 2026–2030 | **Global Tipping Point:** 2026 (base case)
