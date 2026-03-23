---
name: Capability Convergence Patterns by Sector
description: Observed dimension convergence patterns and timing dynamics across STDF capability parity evaluations
type: project
---

## BEV Heavy Trucks China (2026-03-20)

Convergence type: sequential with terminal simultaneous cluster.
- Cluster 1 (structural advantages): energy efficiency, noise, torque — MET at deployment (~2015), no trajectory needed
- Cluster 2 (LFP maturity): urban range, charging time, battery warranty — crossed 2022
- Cluster 3 (late blockers): long-haul range, payload penalty, swap infrastructure — crossing 2025–2026
- Cluster 4 (near-APPROACHING): lifecycle emissions — crossed 2024; cold weather — crossing 2026

Pattern insight: Market-driven disruption S-curve adoption inflects BEFORE full multi-dimensional parity. In this case urban segment (sub-set parity 2022) drove 13% BEV share by 2024 ahead of full parity crossing in 2026.

**How to apply:** When evaluating sectors with structural BEV physics advantages (efficiency, torque, noise), those dimensions will always be in Cluster 1 and should not be treated as indicators of capability trajectory progress — they are baseline from day 1. Range, infrastructure, and payload dimensions are the real trajectory metrics to watch.

## BEV vs ICE Passenger Car (2026-03-24) — dedicated capability parity pass

10-dimension evaluation: 9/10 MET → PARTIAL.
- Cluster 1 (structural, pre-2015): energy efficiency (3.77x primary energy advantage), maintenance cost, cargo space — MET at first purpose-built BEV platform deployment
- Cluster 2 (utility, 2017–2019): acceleration (2017), range (2018), charge time (2019) — threshold crossings aligned with Phase 1 S-curve inflection
- Cluster 3 (market completeness, 2021–2023): model variety (2021), cold weather retention (mid-2022), TCO SUV segment (2023)
- NOT_MET: tco_fleet_avg_usd_mile — 20.2% gap (exceeds 15% APPROACHING window), model-derived crossing 2028; economic, not performance
- Parity year (partial): 2023 | Full parity (all 10 dims): 2028 [model-derived]

Key insight: When the sole NOT_MET dimension is a fleet-average economic aggregate rather than a performance dimension, PARTIAL is the correct status even if the gap exceeds the 15% APPROACHING window. The physical capability disruption is complete; incumbent displacement is now gated by cost-curve dynamics on purchase price, not performance.

## Oil/Gas Multi-Vector Disruption — 3 Vector Pattern (2026-03-20)

V1 BEV vs ICE (passenger cars): sequential, 3 clusters spanning 2013–2027.
- Cluster 1 (structural): fuel cost, torque — MET ~2013–2017
- Cluster 2 (battery/range): range, charge time — MET 2019–2021
- Cluster 3 (market completeness): model count, towing — MET 2022; TCO/cold range model-derived 2026–2027
- 7/9 MET → PARTIAL; residual gaps (20.2%, 25.0%) non-blocking for mainstream

V2 Solar+BESS vs Natural Gas: sequential, 2 clusters spanning 2018–2028.
- Cluster 1 (physical advantages): ramp rate, volatility, build time — MET 2018–2020
- Cluster 2 (economics): installed cost, LCOE, BESS cost, scalability — MET 2020–2023
- 9/10 scoreable MET → PARTIAL; dispatchability 12.5% gap (within 15%)
- Standalone capacity factor correctly excluded: not a valid system-level metric for firmed solar+BESS

V3 ASHP vs Gas Furnace: divergent (genuine two-track split, not temporal sequential)
- Track A: all thermal performance + ductless install — MET 2010–2024
- Track B: gross upfront cost (66.7% gap, model-derived 2036–2043) + ducted install complexity (40.0% gap, no convergent trajectory) — hard blockers
- 8/10 MET → NOT_MET; segment bifurcation: ductless/subsidized path is effectively PARTIAL

Pattern insight for V3: divergent pattern in heating = performance parity achieved, capital access is the gate. This differs from BEV/solar where remaining gaps are trajectory-driven. For heating vectors, look specifically at upfront cost ratio and installer supply chain as the decisive dimensions — performance dims will nearly always be MET.

## Li-ion vs Lead-Acid Battery (2026-03-20) — lead-demand-decline pipeline

Convergence type: sequential, 3 clusters spanning pre-2010 to 2031.
- Cluster 1 (structural Li-ion physics): energy density, weight, efficiency, self-discharge — MET pre-2010 to 2014
- Cluster 2 (operational/economics): levelized cost/cycle, charge rate, cost/kWh, maintenance, calendar life — MET 2014–2020
- Cluster 3 (price/regulatory): SLI unit cost (USA 2027-2028, China 2030-2031), recycling rate (~2029)
- 11/13 MET → PARTIAL; blockers are segment-specific to automotive SLI, not blocking disruption in telecom/DC/forklift/stationary

Key pattern: S-curve adoption inflected in non-SLI segments (2018-2021) BEFORE full parity because Cluster 2 crossing was sufficient for commercial cycling applications. Automotive SLI is gated by unit cost economics — a cost-curve dynamics problem, not electrochemistry.

Per-segment differentiation: when the application has >100 cycles/year (forklift, stationary, telecom), levelized cost/cycle is the decisive crossing dimension, not upfront cost. When the application is infrequent-use (SLI cranking: ~30 cycles/year), upfront unit cost dominates decision-making and is the last blocker to fall.

## lib.capability_math.convergence_pattern behavior note

The function returns "divergent" when met_year values span more than ~5 years. For multi-cluster sequential patterns, this is technically correct but narratively imprecise. Always override library classification with manual narrative when the data shows distinct sequential clusters converging toward a simultaneous terminal phase.

For genuine two-track divergent (V3 ASHP case): library classification of "divergent" is correct AND narratively appropriate — the two tracks are not expected to converge on the same timeline.
