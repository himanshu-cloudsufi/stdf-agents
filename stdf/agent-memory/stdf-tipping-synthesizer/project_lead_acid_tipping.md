---
name: Lead-acid vs. Li-ion tipping synthesis — key numbers and patterns
description: Key tipping years, segment decomposition, demand-decline milestone, binding constraints, provisional S-curve params for lead demand decline pipeline run 2026-03-20
type: project
---

## Tipping Point Determination (run 2026-03-20)

| Segment | Tipping Year | Binding Constraint | Status |
|---------|-------------|-------------------|--------|
| Non-SLI (UPS, forklift, stationary) | 2021–2024 | adoption_readiness | All conditions MET — ALREADY TIPPED |
| SLI automotive — Europe | 2026–2027 | adoption_readiness | All conditions MET in Europe |
| SLI automotive — USA/Europe | 2027–2028 | adoption_readiness | co-binding with cost_parity IMMINENT |
| SLI automotive — China | 2031–2032 | cost_parity | adoption_readiness MET; cost 4x gap |

**Why:** SLI automotive is 62.5% of global lead demand. Its tipping is gated by SLI unit cost parity (NOT yet met in either region) and USA EV corridor coverage (59.1% at Q4 2024, needs 80%, model-derived 2028). China SLI binds on cost_parity ($100/unit vs. $25 threshold, 4x gap, 14.84%/yr learning rate, model-derived 2031–2032).

**How to apply:** For commodity demand questions, always decompose by segment; the dominant volume segment (62.5% SLI) determines the primary demand tipping timeline.

## 10% Lead Demand Decline Milestone

- **Question:** When does lead demand drop 10% vs. 2026 baseline?
- **Answer:** 2027–2028 [model-derived interpolated crossing: 2027.5]
- **Mechanism:** Non-SLI displacement (~40% at 2027) + early SLI substitution (~30% at 2027) on weighted S-curves crosses the 10% decline threshold before SLI fully tips globally
- **Key insight:** The milestone does not require SLI global tipping — non-SLI displacement (already underway) contributes the first ~7% of demand reduction by 2027

## Condition Year Inputs (for downstream agents)

### Non-SLI (all MET)
- Cost parity year: 2020.0 (midpoint 2019–2021)
- Capability parity year: 2021.0 (all 4 non-SLI segments MET by 2021)
- Adoption readiness year: 2022.0 (manufacturing 3:1 surplus, no EV charging dependency)

### SLI USA/Europe (binding = adoption_readiness co-binding with cost_parity)
- Cost parity year: 2027.5 (IMMINENT; midpoint 2027–2028)
- Capability parity year: 2027.5 (PARTIAL approaching; midpoint 2027–2028)
- Adoption readiness year: 2028.0 (USA EV corridor model-derived)
- Tipping year: 2028.0

### SLI China (binding = cost_parity)
- Cost parity year: 2031.5 (NOT_MET; midpoint 2031–2032)
- Capability parity year: 2030.5 (PARTIAL; midpoint 2030–2031)
- Adoption readiness year: 2024.0 (MET — NEV mandate 47.9%, 98% EV corridor)
- Tipping year: 2031.5

## Provisional S-Curve Parameters (for 05a scurve-fitter)

- Non-SLI: L=90, k=0.22, x0=2028 → 80% completion ~2036–2040
- SLI USA/Europe: L=80, k=0.25, x0=2029 → 75% completion ~2038–2042
- SLI China: L=80, k=0.22, x0=2032 → 75% completion ~2042–2047

Note: L<100 in all cases because residual ICE/specialist lead-acid applications persist; China SLI ceiling lower due to extreme low domestic lead-acid cost ($25/unit).

## Confidence Scores

- cost-parity-checker: 0.87
- capability-parity-checker: 0.84
- adoption-readiness-checker: 0.82
- Aggregated: 0.82 (mean 0.843 − 0.02 multi-segment penalty)

## China Paradox Pattern

China is FIRST to tip on non-SLI (manufacturing scale advantage, NEV mandate) but LAST to tip on SLI because China is the LOWEST COST lead-acid producer globally ($25/unit vs. $55 USA). The incumbent's own low-cost position becomes the binding constraint on disruptor tipping. Pattern: in markets where the incumbent has a structural manufacturing cost advantage, cost_parity (not adoption_readiness) is the binding constraint regardless of demand-side readiness.

## Key Post-Tipping Mechanics for Lead-Acid

- Lead-acid SLI plant fixed costs: ~40% of total, ~$20/unit at 80% utilization; rises to $32/unit (+60%) at 50% utilization — the breakeven collapse mechanism
- Learning trajectory: Li-ion SLI $135/unit (2024 USA) → ~$71/unit (2028) → ~$51/unit (2030) at 14.84%/yr
- Cross-segment subsidy: LFP manufacturing for non-SLI applications (including stellar energy BESS) subsidizes SLI learning — shared factory-floor economics contribute ~2–3 pp/yr to SLI learning rate
- Recycling flywheel: EU Battery Regulation recycling mandates (65% by Dec 2025, 70% by Dec 2030) create closed-loop cost advantage for Li-ion that is non-replicable by lead-acid incumbents
