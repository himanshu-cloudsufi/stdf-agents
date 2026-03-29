# STDF Synthesizer Agent — BEV vs. ICE Capability Gap

**Agent:** `stdf-synthesizer` | **Confidence:** 0.875

---

## Agent Reasoning

This synthesis merged 4 upstream agent outputs from a CUSTOM capability-gap analysis pipeline. The configuration was selected because the user's query focused specifically on capability dimensions and their closure timing — not on full tipping point determination, S-curve adoption projections, or incumbent X-curve decline. The 7 skipped agents (cost-fitter, cost-parity-checker, adoption-readiness-checker, tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst) are intentional design choices for this configuration, not degradations. No confidence penalty was applied for their absence.

The synthesis narrative was organized around the user's question directly: first a per-dimension capability table (the core analytical output), then the historical convergence sequence that explains how and when each dimension closed, then the 2 remaining APPROACHING dimensions with specific closure timing, then cost context that makes the capability trajectory legible as a unified process rather than a collection of independent improvements, then disruption landscape context, and finally the key conclusion with explicit uncertainty bounds. Cost, capability, and adoption evidence were integrated within sections rather than siloed into separate phase blocks.

One minor scope boundary was managed: the domain-disruption agent estimated "US BEV median ~$30k / ICE ~$29.5k (2025 model-derived)" while the cost-researcher reported "$31k BEV / $29k ICE (2024 catalog observed)." These are consistent — the cost-researcher's 2024 T2 catalog observed values were used as the authoritative current-year number; the domain-disruption's 2025 figure was used only where explicitly future-dated context was needed. No material contradiction.

Confidence aggregation used `lib.tipping_math.confidence_aggregate` with 4 active agent scores (mean 0.875). No degradation penalties were applied. No weakest-link cap was triggered — all 4 agents passed their CRITICAL compliance criteria. The final score of 0.875 reflects high-quality empirical data (15+ data points per cost series, R²=0.954–0.998 across trajectory fits) and strong inter-agent agreement on dimension status.

---

## Agent Output

### Confidence Breakdown

| Agent | Output File | Confidence | Criticality | Status | Notes |
|-------|------------|-----------|-------------|--------|-------|
| Domain Disruption | 01-domain-disruption.md | 0.87 | HIGH | OK | Dual-vector disruption (From Above + Big Bang China); BEV Hybrid (Stellar-dominant) |
| Cost Researcher | 02a-cost-researcher.md | 0.87 | CRITICAL | OK | 15 battery pack data pts (2010–2024), 16 BEV/ICE price pts per region; R²=0.778 for BEV-specific pack (commodity spike noted) |
| Cost Fitter | 02b-cost-fitter.md | — | CRITICAL | SKIPPED | Not needed for capability gap analysis; cost context sourced from domain-disruption + cost-researcher |
| Capability | 03-capability.md | 0.87 | HIGH | OK | 12 dimensions assessed; 10 MET, 2 APPROACHING; R²=0.983–0.998 across trajectories |
| Cost Parity Checker | 04a-cost-parity.md | — | CRITICAL | SKIPPED | Not needed — cost parity condition not in scope for this CUSTOM capability-gap run |
| Capability Parity Checker | 04b-cap-parity.md | 0.89 | HIGH | OK | PARTIAL status confirmed; all compliance criteria PASS; parity year 2026 |
| Adoption Readiness Checker | 04c-adopt-readiness.md | — | HIGH | SKIPPED | Not needed for capability gap analysis |
| Tipping Synthesizer | 04d-tipping-synthesizer.md | — | CRITICAL | SKIPPED | Not needed — tipping point determination out of scope for CUSTOM run |
| S-Curve Fitter | 05a-scurve-fitter.md | — | HIGH | SKIPPED | Not needed — adoption modeling out of scope for CUSTOM run |
| Regional Adopter | 05b-regional-adopter.md | — | MEDIUM | SKIPPED | Not needed — regional adoption modeling out of scope for CUSTOM run |
| X-Curve Analyst | 05c-xcurve-analyst.md | — | MEDIUM | SKIPPED | Not needed — incumbent decline modeling out of scope for CUSTOM run |
| Demand Decomposer | 07a-demand-decomposer.md | — | CRITICAL* | SKIPPED | Conditional — not triggered (no commodity demand question) |
| Stream Forecaster | 07b-stream-forecaster.md | — | HIGH* | SKIPPED | Conditional — not triggered |
| Fleet Modeler | 07c-fleet-modeler.md | — | MEDIUM* | SKIPPED | Conditional — not triggered |
| Regional Demand Analyst | 07d-regional-demand.md | — | HIGH* | SKIPPED | Conditional — not triggered |
| Energy Dispatch | 08a-energy-dispatch.md | — | HIGH** | SKIPPED | Conditional — not triggered (no energy sector dispatch question) |
| Gas Supply Decomposer | 08b-gas-supply.md | — | MEDIUM** | SKIPPED | Conditional — not triggered |

*Commodity agents are conditional — SKIPPED status is normal when the query does not involve commodity demand.
**Energy agents are conditional — SKIPPED status is normal when the query does not involve energy sector dispatch.

### Aggregated Confidence

- **Base (mean):** 0.875 — mean of 4 active agent scores (0.87, 0.87, 0.87, 0.89)
- **Degradation penalty:** 0.0 — no failed agents; all skips are intentional CUSTOM configuration design choices
- **Weakest-link cap applied:** No — all 4 agents passed CRITICAL compliance criteria
- **Final confidence:** 0.875
- **Calculation:** mean(domain_disruption=0.87, cost_researcher=0.87, capability=0.87, cap_parity=0.89) = 0.875; penalty=0.0; cap=not applied; final=0.875

### Key Conclusion

BEV capability parity with ICE is substantially complete as of 2024 (10 of 12 dimensions MET) and will be fully achieved in 2026 when towing range under maximum load crosses its 200 km threshold (linear trajectory, R²=0.995 [model-derived]). The 2022–2024 multi-dimensional parity burst — when range, TCO, purchase price premium, charge time, and cold-weather retention all crossed threshold within 3 years — constitutes the wide-population capability inflection. The binding remaining constraint is towing range at maximum load (10.0% gap, est. 2026 [model-derived]). God Parity is not expected: ICE retains a permanent refueling speed advantage (3–5 min vs. 22 min best-case DCFC). Confidence: 0.875 (high inter-agent agreement; high-quality empirical data; 4-agent CUSTOM run with no degraded agents).

### Handoff Context

- **Sector:** Transportation — passenger vehicle
- **Sub-domains:** passenger vehicle individual ownership (IO), fleet/corporate leasing, ride-hail/TaaS, compact/hatchback segment, mid-size sedan segment, SUV/crossover segment, premium/luxury segment
- **Key disruptions:** BEV disruption of ICE in passenger vehicles (all segments); TaaS disruption of IO model; A-EV convergence with BSAF
- **Rupture window:** 2022–2024 (multi-dimensional capability parity); full parity 2026
- **Tipping year:** unknown — out of scope for CUSTOM run (use TIPPING_ONLY pipeline)
- **All conditions met:** PARTIAL — capability parity PARTIAL (2 dimensions APPROACHING); cost parity and adoption readiness not assessed in this run
- **Cost parity year:** unknown — cost-parity-checker not run in this CUSTOM configuration
- **Capability parity status:** PARTIAL — 10 MET, 2 APPROACHING (battery energy density ~2025, towing range ~2026)
- **Adoption readiness status:** unknown — adoption-readiness-checker not run in this CUSTOM configuration
- **Binding constraint:** capability_parity (towing_range_km — final APPROACHING dimension, est. 2026 [model-derived])
- **Adoption phase:** S-curve acceleration (12.2% global new sales share 2024, past 10% tipping point threshold) — qualitative from domain-disruption; no scurve-fitter parameters available for this run
- **Key cost data points:** Battery pack $115/kWh global median (2024 [T2: Rethinkx, observed]); BEV-specific pack $97/kWh (2024 [T2: Rethinkx, observed]); 18.4%/yr global learning rate (R²=0.954, n=15); USA BEV median $31,000 / ICE $29,000 (2024 [T2: catalog, observed]); China BEV median $16,200 / ICE $19,000 (2024 [T2: catalog, observed])
- **Key capability data points:** 12 dimensions assessed; 10 MET as of 2024; battery energy density 195/200 Wh/kg (APPROACHING, ~2025); towing range 180/200 km at max load (APPROACHING, ~2026); BEV 5-yr TCO $36,325 vs. ICE $42,575 (0.85x ratio [model-derived])
- **Regional dynamics:** China — purchase price parity achieved (BEV 14.7% cheaper, 2024); USA — at parity (1.07x ratio); Europe — 20% premium persists in compact-mid segment, expected to close 2026–2028 [model-derived]
- **Incumbent decline stage:** unknown — xcurve-analyst not run in this CUSTOM configuration
- **Data gaps:** No dedicated BEV $/km operating cost series; BEV-specific pack cost R²=0.778 (commodity spike); no emerging market charging data; no ICE fuel consumption series pre-2022; sub-$35k BEV model scarcity in USA; solid-state battery timeline unquantified; PHEV chimera hump peak timing not in catalog
- **Critical assumptions:** ≤30-min DCFC threshold framing (acceptable travel delay, not refueling speed parity); 200 km towing threshold based on contractor/recreational use patterns; 80%+ home-charging rate is US/Europe-centric; battery cost-curve continuation assumed from 14-year empirical trajectory

---

## Sources

- `output/bev-ice-capability/agents/01-domain-disruption.md` (confidence 0.87)
- `output/bev-ice-capability/agents/02a-cost-researcher.md` (confidence 0.87)
- `output/bev-ice-capability/agents/03-capability.md` (confidence 0.87)
- `output/bev-ice-capability/agents/04b-cap-parity.md` (confidence 0.89)
- `lib.tipping_math.confidence_aggregate` — confidence calculation
