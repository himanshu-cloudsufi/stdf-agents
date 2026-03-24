---
name: EV-ICE synthesis patterns and conflict resolution
description: Synthesis patterns, conflict resolution decisions, and calibration insights from the BEV disruption of ICE passenger cars analysis (March 2026)
type: project
---

## Key synthesis patterns observed in BEV-ICE analysis (2026-03-13)

### Tipping Point vs. Adoption Agent S-curve conflict — canonical pattern
The tipping point agent (running before the adoption agent) uses top-down estimated S-curve parameters; the adoption agent subsequently fits empirical parameters. In the BEV analysis:
- Tipping point agent: x0=2027 (L=0.95, top-down)
- Adoption agent: x0=2028.6 (L=0.88, scipy fit, R²=0.978, 16 pts)
- Resolution: defer to adoption agent for S-curve projections; retain tipping point's rupture window as threshold-crossing assessment (these are complementary, not contradictory)

**Why:** Tipping point precedes S-curve inflection in canonical STDF analysis. The rupture window and the inflection year serve different analytical purposes. Always clarify this distinction in the synthesis narrative.

**How to apply:** In any synthesis where tipping point and adoption agents produce different x0 values, check if the discrepancy is within ±1σ parameter uncertainty from the adoption agent's pcov. If yes, it is not a material conflict — defer to empirical fit for projections, preserve tipping range for threshold analysis.

### Dual-vector disruption typing requires both "From Above" and "From Below" labels
BEV disruption operates simultaneously from the luxury segment (Tesla) and the entry segment (BYD/Chinese OEMs). Single disruption type labels miss this. The synthesis correctly labels it as "dual-vector (From Above + From Below), progressing to Systemic via convergence."

**How to apply:** For any transportation or consumer hardware disruption, check whether both a premium cascade and an entry-segment attack are occurring simultaneously before applying a single disruption type.

### Simultaneous capability convergence (2016–2021) is the key narrative anchor
When 7 of 9 capability dimensions cross their thresholds within a 5-year window, this simultaneous convergence is the strongest signal of approaching adoption inflection. The 5-year window (rather than sequential dimension-by-dimension parity) is what distinguishes a disruption approaching tipping from one still in pre-commercial phase.

### Market share baseline conflict: domain agent estimate vs. adoption agent computed
Domain agent cited "14–16% global BEV share" for 2025 (estimated). Adoption agent computed 15.0% (2024) and 18.7% (2025) from catalog ratio of BEV sales to total sales series. Always use the adoption agent's catalog-derived computation as authoritative — the domain agent estimates from narrative context, not direct series computation.

### USA policy shock handling
The USA's 2025 BEV market share declined (9.2% → 7.5%) due to federal EV tax credit expiry. This non-structural reversal caused the USA's fitted S-curve inflection to shift to 2032.5 (conservative). The correct handling is: (1) note it as a policy shock, not a structural reversal; (2) fit the S-curve through the shock data point (widens CI, pushes inflection later); (3) provide a sensitivity note that excluding the shock shifts inflection ~2 years earlier. Do not exclude the shock from the fit — it is real data that the model should capture.

---

## Confidence calibration notes

- Five-agent pipeline on a high-data-density sector (136 Passenger Cars + 49 Battery Pack catalog curves) produces confidence range 0.82–0.88 across agents; mean 0.848, final 0.85.
- The cost curve agent consistently has slightly lower confidence (~0.82) because its primary data gap is the absence of a direct EV $/mile catalog series — this must be computed from components, introducing assumption risk.
- The adoption agent consistently has higher confidence (~0.87) when working with 15+ data points from catalog series with clear S-curve shape — the empirical fit quality is high.
- In early-growth disruptions (data covering only 10–20% of the S-curve), the adoption agent correctly uses fixed-L fitting rather than free 3-parameter fitting to avoid underestimated ceilings. This is the correct methodology.

---

## Effective narrative structure for this sector

Phase 1 (Sector Scoping) → establish dual-vector disruption and chimera classification up front.
Phase 2 (Tech Inventory) → anchor on the battery pack cost trajectory as the primary driver; include the cost table.
Phase 3 (Convergence) → SDV-EV (already embedded, widening gap), SWB-EV (cost floor compression), A-EV (future accelerator) in that order of immediacy.
Phase 4 (Disruption Pattern) → the 9-dimension capability table is the core evidence here; highlight the simultaneous 2016–2021 convergence window.
Phase 5 (Business Model Shift) → the $/mile parity crossing (2023) is the decisive narrative anchor; include the 4-year cost comparison table.
Phase 6 (S-Curve) → lead with the regional comparison table; highlight the 4–5 year China lead on the S-curve.
Phase 7 (Tipping Point) → the three conditions table (MET/MET/APPROACHING), post-tipping dual-cycle dynamics, and regional completion timeline.
