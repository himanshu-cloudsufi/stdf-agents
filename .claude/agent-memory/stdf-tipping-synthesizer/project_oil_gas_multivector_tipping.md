---
name: Oil/gas multi-vector tipping synthesis — key numbers and patterns
description: Key tipping years, binding constraints, regional sequences, and composite determination for the oil/gas demand disruption (3-vector: EV, Solar+BESS, ASHP) run 2026-03-20
type: project
---

## Tipping Point Determination (run 2026-03-20)

| Vector | Tipping Year | Binding Constraint | Status |
|--------|-------------|-------------------|--------|
| V1: EV vs ICE transport | 2027 | capability_parity | ACTIVE |
| V2: Solar+BESS vs NGCC | 2027–2028 | capability_parity | ACTIVE |
| V3: ASHP vs gas furnace (gross ducted) | CONTINGENT 2035–2043 | cost_parity (NOT_MET) | DEFERRED |
| Composite oil/gas demand | 2027–2028 | capability_parity | ACTIVE |

**Why:** capability_parity is the binding constraint in both active vectors because physical performance thresholds (fleet TCO, cold-weather range for V1; dispatchability index for V2) close slightly after economic thresholds. Cost parity resolved 3–7 years before tipping in both cases.

**How to apply:** For energy sector disruptions, always check if capability dimensions trail cost parity — the physical threshold closure is frequently what drives the S-curve inflection date.

## Condition Year Inputs (for downstream agents)

### V1
- Cost parity year: 2020.5 (midpoint 2020–2021, back-extrapolated, ±1–2yr uncertainty)
- Capability parity year: 2027.0 (model-derived)
- Adoption readiness year: 2026.0 (US highway corridor DCFC 70% coverage)

### V2
- Cost parity year: 2023.5 (midpoint 2023–2024, directly observed)
- Capability parity year: 2027.5 (midpoint 2027–2028, model-derived)
- Adoption readiness year: 2027.0 (US interconnection reform)

### V3 (CONTINGENT)
- Cost parity year: NOT_MET (no horizon; adverse cost direction)
- Capability parity year: 2036–2043 (upfront cost ratio 66.7% gap, decelerating)
- Adoption readiness year: 2029–2031 (installer workforce)

## Composite Demand Timing

- Oil demand structural peak: 2027 (V1-driven; transport ~80% of oil demand)
- Gas demand for power: enters structural decline 2027–2028 (V2-driven)
- Net gas demand structural peak: 2030–2032 (V2 power decline offset by V3 heating persistence)
- Gas heating demand: structurally intact past 2035 (V3 NOT tipped)

## Provisional S-Curve Parameters (for 05a scurve-fitter)

V1 (passenger car BEV): L=92, k=0.35, x0=2027.0 → 80% completion year 2032 (range 2031–2034)
V2 (solar+BESS new capacity): L=85, k=0.30, x0=2027.5 → 75% completion year 2034 (range 2033–2036)
Note: These are provisional. Scurve-fitter 05a should independently derive and supersede these.

## Confidence Scores

- cost-parity-checker: 0.69
- capability-parity-checker: 0.81
- adoption-readiness-checker: 0.75
- Aggregated: 0.75 (mean)

## Regional Tipping Sequences

V1 (EV): China 2025 → USA 2027, Europe 2027
V2 (Solar+BESS): China 2025 → Europe 2026 → USA 2027–2028
V3 (ASHP): All NOT_MET (Europe mini-split/subsidy pathway: 2026–2028 for <15% of market)

**Key pattern**: China leads by 2–3 years in both V1 and V2. In V2, Europe leads the USA by 1–2 years due to shorter grid interconnection timelines (1–3yr Europe vs 5yr US average).
