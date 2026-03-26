# STDF Analysis: BEV Heavy Trucks Disrupt NG Trucks in China

**Preset:** FULL + COMMODITY | **Agents:** 16 (all) | **Date:** 2026-03-20
**Pipeline Confidence:** 0.794 | **Guardrail Validation:** 17/17 PASS

---

## Key Conclusion

BEV heavy trucks have already tipped in China's urban/regional freight market (2022) and are crossing the long-haul tipping threshold in **2025–2026**. The S-curve (L=90%, k=0.7227, x0=2026.59, R²=0.995) implies **80% market share by 2029.5** and the incumbent death spiral threshold in 2027. Cost parity was reached in 2019–2020 (BEV 1.32 CNY/km vs LNG 1.81 CNY/km, −27% advantage in 2024). The binding constraints — long-haul range and swap-network density — both resolve in 2026, driven by LFP battery cost-curve dynamics at 16.70%/yr learning rate.

### Rupture Window
- **Urban/regional:** 2022 (tipped — observed)
- **Captive fleets:** 2023–2024 (tipped — observed)
- **Long-haul full-network:** 2025–2026 (curve-fitted)
- **80% completion:** 2029.5 (conservative: 2030.3)

### Commodity Impact (P50, model-derived)
| Commodity | 2026 | 2031 (+5yr) | 2036 (+10yr) |
|-----------|-----:|------------:|-------------:|
| Lithium (kt LCE/yr) | 100.5 | 244.4 | 254.2 (336.6 with fleet replacement) |
| Copper (kt Cu/yr) | 48.0 | 81.3 | 83.6 |
| LNG displaced (Mt/yr) | 0.95 | 2.31 | 2.40 |
| Diesel displaced (Mbbl/yr) | 9.8 | 23.9 | 24.9 |

---

## Agent Results

| Agent | File | Confidence | Guardrail |
|-------|------|:----------:|:---------:|
| stdf-domain-disruption | `agents/01-domain-disruption.md` | 0.87 | PASS |
| stdf-cost-researcher | `agents/02a-cost-researcher.md` | 0.77 | PASS |
| stdf-cost-fitter | `agents/02b-cost-fitter.md` | 0.74 | PASS |
| stdf-capability | `agents/03-capability.md` | 0.78 | PASS |
| stdf-cost-parity-checker | `agents/04a-cost-parity.md` | 0.82 | PASS |
| stdf-capability-parity-checker | `agents/04b-cap-parity.md` | 0.72 | PASS |
| stdf-adoption-readiness-checker | `agents/04c-adopt-readiness.md` | 0.82 | PASS |
| stdf-tipping-synthesizer | `agents/04d-tipping-synthesizer.md` | 0.787 | PASS |
| stdf-scurve-fitter | `agents/05a-scurve-fitter.md` | 0.87 | PASS |
| stdf-regional-adopter | `agents/05b-regional-adopter.md` | 0.74 | PASS |
| stdf-xcurve-analyst | `agents/05c-xcurve-analyst.md` | 0.81 | PASS |
| stdf-synthesizer | `agents/06-synthesizer.md` | 0.794 | PASS |
| stdf-demand-decomposer | `agents/07a-demand-decomposer.md` | 0.84 | PASS |
| stdf-stream-forecaster | `agents/07b-stream-forecaster.md` | 0.82 | PASS |
| stdf-fleet-modeler | `agents/07c-fleet-modeler.md` | 0.81 | PASS |
| stdf-regional-demand-analyst | `agents/07d-regional-demand.md` | 0.72 | PASS |
| — (executive summary) | `00-final-synthesis.md` | — | PASS |

**Confidence range:** 0.72 (cap-parity, regional-demand) to 0.87 (domain-disruption, scurve-fitter)

---

## Guardrail Validation

**Status: ALL PASS** — 17 files scanned, 0 violations detected.

Checks performed:
- Banned vocabulary (transition, renewable energy, net zero, green, etc.)
- Banned source URLs (IEA, BNEF, EIA, OPEC — relaxed to allow historical data citations)
- Forecast language (forecast, projected, outlook, will reach, estimated to reach)
- Anti-pattern phrases (linear extrapolation, linear growth, green hydrogen, net zero target)

---

## Agents Skipped

**None** — all 16 agents in the STDF registry produced output.

---

## Critical Path (DAG Tiers)

| Tier | Agents | Parallelism |
|------|--------|-------------|
| 1 | domain-disruption, cost-researcher, capability | 3 parallel |
| 2 | cost-fitter | sequential |
| 3 | cost-parity, cap-parity, adopt-readiness | 3 parallel |
| 4 | tipping-synthesizer | sequential |
| 5a | scurve-fitter | sequential |
| 5b | regional-adopter, xcurve-analyst, demand-decomposer | 3 parallel |
| 6a | stream-forecaster | sequential |
| 6b | fleet-modeler, regional-demand-analyst | 2 parallel |
| Final | synthesizer | sequential |

---

## Files

```
output/bev-trucks-china/
├── README.md                          (this file)
├── 00-final-synthesis.md              (40 KB — 7-phase executive narrative)
└── agents/
    ├── 01-domain-disruption.md        (26 KB)
    ├── 02a-cost-researcher.md         (31 KB)
    ├── 02b-cost-fitter.md             (23 KB)
    ├── 03-capability.md               (24 KB)
    ├── 04a-cost-parity.md             (7 KB)
    ├── 04b-cap-parity.md              (8 KB)
    ├── 04c-adopt-readiness.md         (24 KB)
    ├── 04d-tipping-synthesizer.md     (23 KB)
    ├── 05a-scurve-fitter.md           (17 KB)
    ├── 05b-regional-adopter.md        (20 KB)
    ├── 05c-xcurve-analyst.md          (23 KB)
    ├── 06-synthesizer.md              (13 KB)
    ├── 07a-demand-decomposer.md       (23 KB)
    ├── 07b-stream-forecaster.md       (written)
    ├── 07c-fleet-modeler.md           (19 KB)
    └── 07d-regional-demand.md         (written)
```

Total output: ~360 KB across 17 markdown files.
