# STDF Synthesizer Agent — BEV Truck Costs in China (QUICK Preset)

**Agent:** `stdf-synthesizer` | **Confidence:** 0.815 (cost data quality only)

---

## Agent Reasoning

**Preset scope.** This pipeline ran under the QUICK preset, which executes only the cost chain: stdf-cost-researcher and stdf-cost-fitter. The tipping-synthesizer, capability chain, adoption chain, and commodity demand chain were not invoked. Their absence is by design — QUICK preset skips them intentionally, not due to failure. Confidence is therefore scoped to the quality of the cost data and fitting, not to a complete disruption assessment. The rupture window and tipping year are unavailable from this pipeline run; producing them would require the FULL preset.

**Data quality and conflict resolution.** The cost-researcher identified a meaningful source conflict for the 2024 BEV HCV purchase price: the T2 catalog shows USD 110,000 (CNY ~787,000 at 7.15) for a generic 400km-range configuration, while direct T3 fleet transactions (chinatruck.net) show CNY 400,000–650,000 depending on battery capacity (282–400 kWh). Per STDF conflict resolution priority rule "granular specialist over generalist" and "more data points," the T3 observed fleet transaction prices are used as the market-clearing price anchors for 2023–2024, with the T2 catalog carried as the broad-fleet conservative bound. This resolution was also made by the cost-fitter, which ran two separate exponential fits: one on the T2 catalog USD series (long-run, R²=0.992, 9 pts) and one on the T3 CNY transaction series (recent price-war period, R²=0.753, 4 pts). The T3 fit is flagged below the 0.80 quality threshold.

**Confidence calculation.** Only the two cost-chain agents ran. QUICK preset exclusions of domain-disruption, capability, tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, and commodity demand agents are not failures — no degradation penalty applies. Both agents passed their compliance checklists with no CRITICAL criterion failures, so no weakest-link cap is applied. The resulting confidence of 0.815 accurately reflects the internal quality of the cost data; it does NOT represent confidence in a complete disruption assessment, which would require the FULL preset.

**Scope limitation.** The absence of tipping-synthesizer, capability-parity-checker, and adoption-readiness-checker means that three of the four tipping conditions required for a full STDF tipping point assessment are unverified in this pipeline run. The cost-fitter has established that: (a) per-km energy cost parity was crossed before 2019; (b) 282 kWh short-haul tractors achieved purchase price parity in 2024; and (c) 440 kWh long-haul tractors are on track for parity in 2026–2027 [model-derived]. These findings are cost parity signals, not confirmed tipping point determinations. A prior FULL+COMMODITY pipeline run on the same sector (slug: `bev-trucks-china`) established a tipping window of 2025–2026 with a binding constraint of capability_parity and adoption_readiness (co-binding). The current QUICK run is consistent with and does not contradict those prior findings.

---

## Agent Output

### Confidence Breakdown

**All values: [observed] from agent output files**

| Agent | Output File | Confidence | Criticality | Status | Notes |
|-------|------------|-----------|-------------|--------|-------|
| Cost Researcher | 02a-cost-researcher.md | 0.82 | CRITICAL | OK | 21 purchase price data points (9 T2 + 5 T3 + anchors), 10 fuel price T1 points |
| Cost Fitter | 02b-cost-fitter.md | 0.81 | CRITICAL | OK | 4 fits computed; T3 CNY fit R²=0.753 flagged; T2 USD R²=0.992; LFP long-run R²=0.976 |
| Domain Disruption | 01-domain-disruption.md | — | HIGH | SKIPPED | Not invoked by QUICK preset |
| Capability | 03-capability.md | — | HIGH | SKIPPED | Not invoked by QUICK preset |
| Cost Parity Checker | 04a-cost-parity.md | — | CRITICAL | SKIPPED | Not invoked by QUICK preset |
| Capability Parity Checker | 04b-cap-parity.md | — | HIGH | SKIPPED | Not invoked by QUICK preset |
| Adoption Readiness Checker | 04c-adopt-readiness.md | — | HIGH | SKIPPED | Not invoked by QUICK preset |
| Tipping Synthesizer | 04d-tipping-synthesizer.md | — | CRITICAL | SKIPPED | Not invoked by QUICK preset — rupture window UNAVAILABLE |
| S-Curve Fitter | 05a-scurve-fitter.md | — | HIGH | SKIPPED | Not invoked by QUICK preset |
| Regional Adopter | 05b-regional-adopter.md | — | MEDIUM | SKIPPED | Not invoked by QUICK preset |
| X-Curve Analyst | 05c-xcurve-analyst.md | — | MEDIUM | SKIPPED | Not invoked by QUICK preset |
| Demand Decomposer | 07a-demand-decomposer.md | — | CRITICAL* | SKIPPED | Not invoked by QUICK preset |
| Stream Forecaster | 07b-stream-forecaster.md | — | HIGH* | SKIPPED | Not invoked by QUICK preset |
| Fleet Modeler | 07c-fleet-modeler.md | — | MEDIUM* | SKIPPED | Not invoked by QUICK preset |
| Regional Demand Analyst | 07d-regional-demand.md | — | HIGH* | SKIPPED | Not invoked by QUICK preset |

*SKIPPED by preset design — not a pipeline failure. No confidence penalty applied.

### Aggregated Confidence

- **Base (mean of agents that ran):** (0.82 + 0.81) / 2 = **0.815**
- **Degradation penalty:** 0.00 — QUICK preset exclusions are not failures; all skipped agents were omitted by design
- **Weakest-link cap applied:** No — no CRITICAL criterion failures in either compliance checklist
- **Final confidence:** **0.815**
- **Calculation (from `confidence_aggregate`):** `mean(cost_researcher=0.82, cost_fitter=0.81) = 0.815; final = 0.815`
- **Important caveat:** This confidence applies to the quality of the cost data and fitted trajectories only. A comprehensive disruption tipping assessment is outside the scope of this QUICK run.

### Key Conclusion

BEV heavy trucks are driving market-driven disruption and incumbent displacement of diesel commercial vehicles in China through cost-curve dynamics alone. Purchase price parity was crossed in 2024 for 282 kWh short-haul tractors (CNY 400,000 [observed] vs. CNY 486,200 [observed] ICE, a 17.7% BEV cost advantage), with 440 kWh long-haul tractors on track for parity at 2026–2027 [model-derived] per the T3 CNY exponential fit (r=0.1015, R²=0.753). Per-km energy cost parity was crossed before 2019 and the BEV advantage is now 35.7% (CNY 1.44/km vs. CNY 2.24/km in 2024 [model-derived]). Broader-fleet purchase price parity (T2 conservative bound) arrives at 2029–2030 [model-derived]. S-curve adoption evidence is visible in market share data (1% in 2020 to 13% in 2024 to ~21% in December 2024) but no formal scurve-fitter analysis was performed. Tipping point determination, capability assessment, and adoption curve analysis require the FULL preset. Confidence: 0.815 (cost data quality; 2 agents; QUICK preset scope).

### Handoff Context

- **Sector:** Heavy commercial vehicles, China
- **Sub-domains:** BEV heavy-duty tractors (282–440 kWh LFP); Diesel heavy-duty ICE tractors
- **Key disruptions:** BEV heavy trucks displacing diesel ICE via LFP cost-curve dynamics; secondary LNG chimera displacement (not modeled in this QUICK run)
- **Rupture window:** UNAVAILABLE — tipping-synthesizer not invoked in QUICK preset
- **Tipping year:** UNAVAILABLE — tipping-synthesizer not invoked in QUICK preset
- **All conditions met:** UNAVAILABLE — tipping condition checkers not invoked
- **Cost parity year:** 2024 (282 kWh short-haul, observed); 2026–2027 (440 kWh long-haul, model-derived from cost-fitter T3 CNY fit) — not formally confirmed by cost-parity-checker agent
- **Capability parity status:** UNAVAILABLE — capability and capability-parity-checker not invoked
- **Adoption readiness status:** UNAVAILABLE — adoption-readiness-checker not invoked
- **Binding constraint:** UNAVAILABLE — tipping-synthesizer not invoked
- **Adoption phase:** UNAVAILABLE — scurve-fitter not invoked (contextual note: 1% to 13% market share 2020–2024 is consistent with early fast-growth; December 2024 ~21% flash reading cited by cost-researcher)
- **Key cost data points:** BEV HCV purchase price declined 57.7% from $260,000 (2010) to $110,000 (2024, T2 catalog); T3 market-clearing price CNY 400,000–650,000 (2024); LFP battery cost declined 91.5% from $1,100/kWh (2010) to $94/kWh (2024); learning rate 5.79%/yr (T2 long-run), 9.65%/yr (T3 recent price-war, low confidence), 16.66%/yr (LFP long-run); ICE diesel rising linearly at +$2,000/yr
- **Key capability data points:** UNAVAILABLE — capability agent not invoked
- **Regional dynamics:** UNAVAILABLE — regional-adopter not invoked; cost-researcher notes wide electricity price variance (CNY 0.43–0.88/kWh across provinces) relevant to per-km cost comparisons
- **Incumbent decline stage:** UNAVAILABLE — xcurve-analyst not invoked
- **Data gaps:** No T1 time series for BEV tractor purchase prices pre-2020; no LNG truck purchase price time series; no maintenance cost time series; electricity price regional variance wide (CNY 0.43–0.88/kWh); battery swap vehicle pricing not captured; T3 CNY fit R²=0.753 (low confidence); LFP battery long-run model deviation 18.8% at 2024 (curve flattening)
- **Critical assumptions:** T2 BEV HCV catalog treated as 400km-range lowest-cost configuration; ICE diesel price linear_rising at +$2,000/yr (catalog-smoothed, may understate actual pricing pressure); per-km energy cost parameters literature-derived (2.0 kWh/km BEV, 0.30 L/km diesel, CNY 0.72/kWh electricity midpoint); CNY/USD held at 7.15 for forward comparisons; diesel fuel forward trend +0.031 USD/L/yr from R²=0.478 base (low precision)

---

## Sources

- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/bev-trucks-china-2/agents/02a-cost-researcher.md` — cost-researcher agent output, confidence 0.82
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/bev-trucks-china-2/agents/02b-cost-fitter.md` — cost-fitter agent output, confidence 0.81
