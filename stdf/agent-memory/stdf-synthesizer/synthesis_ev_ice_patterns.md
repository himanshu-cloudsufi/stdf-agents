---
name: EV-ICE synthesis patterns and conflict resolution
description: Synthesis patterns, conflict resolution decisions, and calibration insights from the BEV disruption of ICE passenger cars analysis (2026-03-13, updated 2026-03-24 TIPPING_ONLY run, updated 2026-03-27 CUSTOM capability-gap run)
type: project
---

## Key synthesis patterns observed in BEV-ICE CUSTOM capability-gap run (2026-03-27)

### CUSTOM 4-agent capability-gap run — confidence 0.875
CUSTOM runs with only capability-chain agents (domain-disruption, cost-researcher, capability, capability-parity-checker) produce confidence in the 0.87–0.89 range (mean 0.875). No penalties applied for the 7 intentionally skipped agents. The capability-parity-checker consistently yields the highest confidence (0.89) because all dimension data is observed with clear threshold crossings.

### 12-dimension BEV capability table — canonical structure
The per-dimension table (Dimension | BEV 2024 | ICE 2024 | Threshold | Status | Year Met) is the core analytical output for capability-gap queries. Always include the year-met column — it reveals the sequential convergence wave and is more informative than the static status alone. The 2022–2024 burst (range, TCO, purchase price, charge time, cold-weather retention all crossing in 3 years) is the headline finding.

### God Parity vs. competitive threshold — always distinguish
BEV will not achieve God Parity (superiority on ALL dimensions) because ICE retains a permanent refueling speed structural advantage (3–5 min vs. 15–22 min physics floor for DCFC). The competitive threshold for charge time is set at ≤30 min, not ≤5 min, because the decision gate is "acceptable travel delay," not "equals ICE refueling." This distinction must be explicit in the synthesis — without it, readers will incorrectly conclude charge time remains a major gap.

### Towing range as sole remaining niche blocker
As of 2026-03-27, towing range at maximum load (180 km vs. 200 km threshold) is the last APPROACHING dimension. Its 2026 closure date drives the "full capability parity" headline. The 10.0% gap is accurately characterized as a niche-segment blocker (heavy-duty towing users), not a wide-population blocker. Never frame it as a material adoption barrier for the general buyer.

### Cost-researcher vs. domain-disruption price data: minor scope boundary
Domain-disruption estimated "US BEV median ~$30k / ICE ~$29.5k (2025 model-derived)"; cost-researcher reported "$31k / $29k (2024 catalog observed)." Resolution: cost-researcher T2 catalog observed 2024 values are authoritative for current-year numbers. Domain-disruption's 2025 figure is used only as future-dated context. Both are directionally consistent — not a material conflict.

### Narrative structure for CUSTOM capability-gap queries
1. Per-dimension capability table (core answer to the query — lead with it)
2. Sequential convergence wave narrative (how/when dimensions closed — organize chronologically by crossing year)
3. Remaining APPROACHING dimensions with specific closure timing and physics constraints
4. Cost structure as the unified mechanism (all capability improvements trace back to battery learning rate)
5. Disruption landscape context (chimeras, convergence combinations, adoption position)
6. Key conclusion with parity window and binding constraint

## Key synthesis patterns observed in BEV-ICE TIPPING_ONLY run (2026-03-24)

### TIPPING_ONLY preset — scurve-fitter, regional-adopter, xcurve-analyst SKIPPED
These three agents are tagged MEDIUM/HIGH in the TIPPING_ONLY preset and carry zero confidence penalty when absent. The synthesis must note the scope limitation clearly in Phase 6, use provisional S-curve parameters from tipping-synthesizer (L=92%, k=0.30, x0=2028), and label them as indicative-only. Do not fabricate S-curve fit quality metrics.

### Co-binding convergence pattern
When two tipping conditions share the same underlying resolution driver (battery cost-curve dynamics in this case), they resolve simultaneously — producing a compressed tipping window rather than a staggered one. The co-binding lowers the uncertainty in the tipping year: if one condition resolves 2028, the other co-bound condition also resolves 2028 by definition. Report the lower bound (2027) as 1 year earlier than the central (2028) due to the shared cost-curve mechanism.

### "Regional Outlook" header trap — confirmed violation
The section header "Regional Outlook" was blocked by the stdf_validate.py hook (forecast language: "Outlook"). Use "Regional S-Curve Status" or "Regional Adoption Dynamics" instead. This is the same trap documented in the HDT and lead-demand memory files.

### TIPPING_ONLY confidence calibration
8-agent TIPPING_ONLY pipeline with high-quality data (R²=0.99 battery fit, 0.99 BEV USA fit, 0.97 fleet-TCO fit) produces agent confidence range 0.85–0.92, mean 0.885, final 0.88. The capability-parity-checker consistently produces the highest confidence (0.92) because all dimension data is observed with clear threshold crossings. The cost-parity-checker produces 0.85 due to the absence of observed 2025 data — the parity year is model-derived, not confirmed.

### Capability agent vs. capability-parity-checker scope conflict
The capability agent assessed 8 requested dimensions (all MET). The capability-parity-checker extended this to 10 dimensions (including 2 supplemental TCO dimensions), finding 9/10 MET and fleet-avg TCO NOT_MET. Resolution: the checker (specialist, downstream) takes precedence. The conflict is a scope expansion, not a factual contradiction — both are correct within their respective scope boundaries.

### China 4-year structural lead
China tipped in 2024 — 4 years ahead of the global date. This is the canonical model for how fast a single leading market can pull the global cost curve. China's LFP vertical integration ($85/kWh, 2025) is below the approximate ICE drivetrain cost per vehicle ($4,000–6,000), making BEV structurally cheaper to manufacture in China than ICE. The US 100% tariff delays but cannot reverse this cost-curve trajectory.

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
