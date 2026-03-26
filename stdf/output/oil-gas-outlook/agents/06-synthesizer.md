# STDF Synthesizer Agent — Oil and Gas Demand (Multi-Vector)

**Agent:** `stdf-synthesizer` | **Confidence:** 0.383

---

## Agent Reasoning

This synthesis merges 13 upstream agent outputs covering a three-vector simultaneous disruption of oil and gas demand: V1 (BEV vs. ICE/petroleum), V2 (solar PV + BESS vs. CCGT/OCGT gas power), and V3 (ASHP vs. gas heating). Two conditional commodity demand agents were absent from this pipeline run — fleet-modeler (07c) and regional-demand-analyst (07d) — with respective MEDIUM and HIGH criticality, triggering Failure Matrix penalties of −0.10 and −0.30. The multi-vector structure required a more complex synthesis than single-vector analyses: three parallel tipping condition assessments, cross-vector amplification tracking, and simultaneous commodity demand impact assessment across both oil and gas.

The most significant conflict resolved in synthesis was the V2 S-curve parameter discrepancy between tipping-synthesizer (provisional L=85, k=0.30, x0=2027.5 based on capacity additions metric) and scurve-fitter (authoritative L=45, k=0.2279, x0=2031.6 based on generation share metric). Per the priority rule (granular specialist over generalist), the scurve-fitter's parameters are authoritative for all downstream demand projections. The tipping-synthesizer's 2027–2028 V2 tipping year remains valid because it is based on capability parity (dispatchability index reaching threshold), not the S-curve inflection year. This is the most consequential conflict type in multi-vector synthesis: metric mismatch between upstream and downstream agents where both are numerically correct but measuring different things. The resolution is to use the generation share metric for demand displacement and the capability parity timeline from the tipping-synthesizer.

V3 is the analytically distinct vector in this analysis. Unlike V1 and V2 — where cost parity has been achieved and the disruption is on a clear market-driven trajectory — V3 involves a cost structure that is NOT improving (heat pump capital costs rising) and operates in a market (USA) where incumbent operating costs (gas at $2.19/MMBtu) are structurally low. The V3 designation as CONTINGENT 2035–2043 is not a rounding error or data gap; it reflects a genuine structural barrier: US gas prices would need to rise substantially (above $0.088/kWh electricity break-even equivalent) or ASHP capital costs would need to fall dramatically for V3 to become a market-driven disruption rather than a policy-dependent niche. The synthesis explicitly preserves this distinction rather than averaging V3 into a composite "heating disruption" score.

Confidence calculation was driven primarily by the two missing agents. The base mean of 0.783 across 13 agents represents strong inter-agent agreement — the lowest individual agent confidence is cost-parity-checker at 0.69 (reflecting V3 NOT_MET complexity in a three-vector assessment), and the average of the remaining 12 core agents is 0.795. The −0.40 total penalty (−0.30 HIGH + −0.10 MEDIUM) reflects the analytical importance of regional demand quantification for a commodity-focused analysis — without market-by-market oil and gas demand projections, the analysis is incomplete for its primary use case of commodity market planning.

---

## Agent Output

### Confidence Breakdown

| Agent | Output File | Confidence | Criticality | Status | Notes |
|-------|------------|-----------|-------------|--------|-------|
| Domain Disruption | 01-domain-disruption.md | 0.82 | HIGH | OK | Three-vector disruption map; all sub-domains identified |
| Cost Researcher | 02a-cost-researcher.md | 0.84 | CRITICAL | OK | V1/V2/V3 cost data; TCO, LCOE, installed costs |
| Cost Fitter | 02b-cost-fitter.md | 0.78 | CRITICAL | OK | Learning rates, thresholds; V2 solar LCOE R²=0.756 flagged |
| Capability | 03-capability.md | 0.82 | HIGH | OK | 7/9 V1 dims, 9/10 V2 dims, 8/10 V3 dims |
| Cost Parity Checker | 04a-cost-parity.md | 0.69 | CRITICAL | OK | V1 MET, V2 MET, V3 NOT_MET; aggregate low due to V3 |
| Capability Parity Checker | 04b-cap-parity.md | 0.81 | HIGH | OK | V1 PARTIAL 2027, V2 PARTIAL 2027–2028, V3 NOT MET |
| Adoption Readiness Checker | 04c-adopt-readiness.md | 0.75 | HIGH | OK | V1 PARTIAL, V2 PARTIAL, V3 NOT_MET |
| Tipping Synthesizer | 04d-tipping-synthesizer.md | 0.75 | CRITICAL | OK | V1: 2027, V2: 2027–2028, V3: CONTINGENT 2035–2043 |
| S-Curve Fitter | 05a-scurve-fitter.md | 0.82 | HIGH | OK | V1 R²=0.9902; V2 R²=0.9965; V3 EU R²=0.9987 |
| Regional Adopter | 05b-regional-adopter.md | 0.78 | MEDIUM | OK | All 3 vectors, 4 regions; V3 China T3 data gap |
| X-Curve Analyst | 05c-xcurve-analyst.md | 0.75 | MEDIUM | OK | V1 China death spiral active; V2 pre-disruption |
| Demand Decomposer | 07a-demand-decomposer.md | 0.80 | CRITICAL* | OK | 100% demand coverage; substitution ratios |
| Stream Forecaster | 07b-stream-forecaster.md | 0.77 | HIGH* | OK | 3-stream demand; N=300 Monte Carlo CIs |
| Fleet Modeler | 07c-fleet-modeler.md | — | MEDIUM* | FAILED | Missing; rolling average approximation used instead |
| Regional Demand Analyst | 07d-regional-demand.md | — | HIGH* | FAILED | Missing; regional demand projections unavailable |

*Conditional commodity agents — CRITICAL/HIGH/MEDIUM as indicated above.

---

### Aggregated Confidence

- **Base (mean):** 0.783 (13 agents: domain_disruption=0.82, cost_researcher=0.84, cost_fitter=0.78, capability=0.82, cost_parity=0.69, cap_parity=0.81, adopt_readiness=0.75, tipping_synthesizer=0.75, scurve_fitter=0.82, regional_adopter=0.78, xcurve_analyst=0.75, demand_decomposer=0.80, stream_forecaster=0.77)
- **Degradation penalty:** −0.40 (fleet-modeler MEDIUM: −0.10; regional-demand-analyst HIGH: −0.30)
- **Weakest-link cap applied:** No (no CRITICAL compliance failures)
- **Final confidence:** 0.383
- **Calculation:** mean=0.783; −penalty 0.40 = 0.383; final=0.383 (verified via lib.tipping_math.confidence_aggregate)

---

### Key Conclusion

BEV will displace ICE oil demand and solar+BESS will displace gas power generation at the global composite tipping window of 2027–2028 (tipping-synthesizer, confidence 0.75). Cost parity: V1 MET 2020–2021 (cost-parity-checker, 0.65), V2 MET 2023–2024 (cost-parity-checker, 0.82), V3 NOT MET. Capability parity is the binding constraint for V1 and V2 — model parity 2027 and 2027–2028 respectively (capability-parity-checker, 0.81). Oil demand structural peak: 2024–2026; gas demand structural peak: 2030–2032. V3 CONTINGENT 2035–2043. Confidence: 0.383 (materially degraded by two missing commodity-demand agents: fleet-modeler −0.10, regional-demand-analyst −0.30).

---

### Handoff Context

- **Sector:** Oil and Gas
- **Sub-domains:** Road transport petroleum, electric power generation gas, residential and commercial space heating gas, structural floor demand (aviation, marine, petrochemicals, industrial)
- **Key disruptions:** V1: BEV vs. ICE passenger vehicles + diesel HDT; V2: Solar PV + BESS vs. CCGT/OCGT gas turbines; V3: ASHP vs. natural gas boilers/furnaces
- **Rupture window:** 2027–2028 (V1+V2 composite)
- **Tipping year:** 2027 (V1), 2027–2028 (V2), CONTINGENT (V3)
- **All conditions met:** No — V3 all three conditions NOT MET; V1 and V2 capability parity PARTIAL (resolving 2027–2028)
- **Cost parity year:** V1: 2020–2021 (MET); V2: 2023–2024 (MET); V3: NOT MET, lib parity 2043 ducted retrofit (cost-parity-checker)
- **Capability parity status:** V1: PARTIAL (2027); V2: PARTIAL (2027–2028); V3: NOT MET gross ducted (capability-parity-checker)
- **Adoption readiness status:** V1: PARTIAL (2026 US highway coverage); V2: PARTIAL (2027 US interconnection); V3: NOT MET (2029–2031 workforce; cost-parity-checker, adopt-readiness-checker)
- **Binding constraint:** V1: capability_parity; V2: capability_parity; V3: cost_parity (tipping-synthesizer)
- **Adoption phase:** V1: rapid_growth (23.89%, 2024); V2: tipping (6.92%, 2024); V3 EU: rapid_growth (24.0%, 2023); V3 global: tipping (~10%, 2024) (scurve-fitter)
- **Key cost data points:** BEV TCO $0.58/mile vs. ICE $0.85/mile (2024); battery 16.45%/yr learning rate; solar LCOE $43/MWh vs. NGCC $76/MWh (2024); NGCC rising +$4.40/MWh/yr; BESS 9.04%/yr learning rate; ASHP cost ratio 1.985× (cost-researcher + cost-fitter)
- **Key capability data points:** V1: 7/9 dims MET, fleet TCO parity 2026–2027, cold-weather range 2027; V2: 9/10 dims MET, dispatchability index 70% vs. 80% threshold, model parity 2027–2028; V3: upfront cost ratio 5.0× vs. <3.0×, ducted complexity 3.5/5 vs. ≤2.5/5 (capability)
- **Regional dynamics:** China leads V1 by 5.6 yr over USA (x0=2023.7 vs. 2029.2); China overtakes Europe V2 solar ~2027; Europe leads V3 at 24% new installations; all regions in V2 tipping phase simultaneously; China BESS 45.2% of global capacity (regional-adopter)
- **Incumbent decline stage:** V1 ICE global: Accelerating decline; V1 ICE China: Death spiral active (2025.8); V2 gas power: Pre-disruption/Early volume loss; V3 gas boiler EU: Accelerating decline, death spiral 2029.1; oil refinery sector: Structural stress (xcurve-analyst)
- **Data gaps:** Regional demand quantification absent (07d FAILED), fleet-model absent (07c FAILED), no BEV-HDT dedicated S-curve, V3 China T3 data only, EU V1 R²=0.9207 below threshold, solar-to-gas displacement ratio uncertain (0.55±10pp), industrial gas 821 bcm treated as structural floor with no disruption vector, V2 solar LCOE full-period R²=0.756
- **Critical assumptions:** BEV fleet stock share modeled via 6-year rolling average (not full stock-flow), structural floor grows 0.5%/yr (peak oil timing sensitive: at 1.0%/yr floor growth, peak deferred to 2027–2028), solar displaces gas at 55% efficiency globally, V3 global HP adoption = 41.7% of EU new-installation S-curve, PHEV electric fraction 40% gasoline globally

---

## Sources

Upstream agent output files (all from agents directory, this pipeline run):
- 01-domain-disruption.md (confidence 0.82)
- 02a-cost-researcher.md (confidence 0.84)
- 02b-cost-fitter.md (confidence 0.78)
- 03-capability.md (confidence 0.82)
- 04a-cost-parity.md (confidence 0.69)
- 04b-cap-parity.md (confidence 0.81)
- 04c-adopt-readiness.md (confidence 0.75)
- 04d-tipping-synthesizer.md (confidence 0.75)
- 05a-scurve-fitter.md (confidence 0.82)
- 05b-regional-adopter.md (confidence 0.78)
- 05c-xcurve-analyst.md (confidence 0.75)
- 07a-demand-decomposer.md (confidence 0.80)
- 07b-stream-forecaster.md (confidence 0.77)
- 07c-fleet-modeler.md (FAILED, MEDIUM, −0.10)
- 07d-regional-demand.md (FAILED, HIGH, −0.30)

Computation libraries used:
- lib.tipping_math.confidence_aggregate — confidence aggregation with Failure Matrix penalties
- lib.scurve_math — S-curve fitting and projection (all upstream agents)
- lib.demand_math — demand decomposition and substitution ratios (demand-decomposer)

*Output written: 2026-03-20 | Pipeline run: oil-gas-demand-disruption | Agent: stdf-synthesizer*
