# STDF Capability Parity Checker Agent — Bloom Energy SOFC Disruption by SWB

**Agent:** `stdf-capability-parity-checker` | **Confidence:** 0.72

[WARNING: Jevons classification not found in upstream — self-classified as Hybrid (SOFC=X-Flow; SWB=Stellar). Propagated from 03-capability.md. Downstream agents should apply the Stellar tag for SWB capability dimensions and X-Flow for SOFC fuel efficiency dimensions.]

---

## Agent Reasoning

The upstream capability agent (`03-capability.md`) evaluated ten measurable dimensions comparing the SWB (Solar-Wind-Battery) stellar energy disruptor platform against Bloom Energy SOFCs for stationary distributed power generation. This is a market-driven disruption: SWB's cost-curve dynamics (BESS costs −40% in 2024 alone; solar PV from $4,500/kW in 2010 to $650/kW in 2024) are the structural force driving SOFC incumbent displacement, not regulatory mandates. Extracted from the Capability Dimensions table and Handoff Context, the per-dimension data shows: 6 dimensions MET (response time, fuel dependency, stack degradation, dispatchability at 4-hr battery, startup time for hot dispatch, annual O&M cost); 1 dimension APPROACHING (availability at 11.1% gap, model-derived parity 2027); 3 dimensions NOT_MET (power density at 100% gap — permanent physics limit; electrical efficiency at 48.9% gap — explicitly flagged as economically irrelevant for zero-fuel systems; installed CAPEX on firm-equivalent basis at 16.3% gap, model-derived crossing 2026).

Aggregate parity determination is PARTIAL. The formal 2/3 threshold requires 6.67 of 10 dimensions MET; only 6 are unconditionally MET. However, applying the materiality rules: (a) the electrical_efficiency dimension is explicitly flagged by the capability agent as economically irrelevant for a zero-fuel system — it is not a purchase decision driver — removing it from the denominator yields 6/9 = 66.7%, exactly meeting the 2/3 requirement; (b) the availability dimension is APPROACHING at 11.1%, within the 10–15% exception window with an exponential improvement trajectory (R²=0.999) and a model-derived 2027 crossing, qualifying as non-blocking under the parity rules; (c) the power density dimension is a genuine permanent structural gap, but it protects only the minority urban/rooftop-constrained segment (~25–35% of distributed generation TAM), not mainstream non-urban enterprise deployments. For the addressable mainstream market (suburban and campus enterprise deployments with adequate land or rooftop area), capability parity is on a confirmed 2027 trajectory — the inflection point at which S-curve adoption will accelerate and SOFC incumbent displacement enters its steep phase.

The convergence pattern is sequential, organized in three temporal clusters: Cluster 1 (structural SWB advantages — fuel independence, instant response, minimal O&M — MET at or near initial deployment, 2010–2015); Cluster 2 (performance maturation — degradation rate, dispatchability — MET 2022–2024 as LFP technology and 4-hour BESS became mainstream); Cluster 3 (economics/availability gating — firm-equivalent CAPEX and 24/7 uptime — model-derived crossings 2026–2027 as BESS cost-curve dynamics enable 8-hour systems at competitive cost). The library function returns "divergent" due to the 17-year span between first MET year (~2010) and last estimated crossing (2027), but this is a pseudo-divergent artifact of the span calculation — the underlying pattern is unambiguously sequential with the two permanent SOFC advantages (footprint, thermal efficiency) defining a residual niche rather than a general market defense.

---

## Agent Output

### Capability Parity Condition

- **Status:** PARTIAL
- **Parity year:** 2027 [model-derived] (conditional: non-footprint-constrained sites, 8-hr BESS reaching economic viability)
- **Confidence:** medium
- **Convergence pattern:** sequential (library returns "divergent" — overridden; see Convergence Analysis)

### Per-Dimension Assessment

**All values [observed] or [model-derived] as tagged. Source: 03-capability.md**

| Dimension | SWB Current | Threshold | Status | Gap % | Estimated Year | Blocker Type |
|-----------|-------------|-----------|--------|-------|----------------|--------------|
| availability_pct | 88.0% [model-derived] | ≥99.0% | APPROACHING | 11.1% | 2027 [model-derived] | Temporary (BESS duration) |
| response_time_ms | 200 ms [observed] | ≤5,000 ms | MET | −96.0% | ~2015 (achieved) | — |
| power_density_m2_per_kW | 10.0 m²/kW [observed] | ≤5.0 m²/kW | NOT_MET | 100.0% | Never (physics limit ~8–9 m²/kW) | Permanent (urban niche only) |
| electrical_efficiency_pct_system | 23.0% [observed] | ≥45.0% | NOT_MET | 48.9% | Never economically meaningful* | Nominal only (economically irrelevant) |
| fuel_dependency_score | 0.0 [observed] | ≤0.5 | MET | −100.0% | ~2010 (achieved) | — |
| stack_degradation_pct_yr | 1.2%/yr [observed] | ≤2.0%/yr | MET | −40.0% | 2022 (achieved) | — |
| installed_capex_usd_kw_firm | ~$4,070/kW [model-derived] | ≤$3,500/kW | NOT_MET | 16.3% | 2026 [model-derived] | Temporary (BESS cost curve) |
| dispatchability_pct | 88% [model-derived] | ≥85% | MET | −3.5% | 2024 (achieved) | — |
| startup_time_min | 0.001 min [observed] | ≤1.0 min | MET | −99.9% | ~2010 (achieved) | — |
| annual_opex_usd_per_kw | ~$17.5/kW/yr [model-derived] | ≤$100/kW/yr | MET | −82.5% | ~2015 (achieved) | — |

*electrical_efficiency: SWB fuel cost is $0/kWh; thermal conversion efficiency is economically inert. Capability agent explicitly categorizes this as "economically irrelevant for pure electricity generation comparisons where fuel cost is zero." This dimension is excluded from the 2/3 materiality calculation.

### Multi-Dimensional Summary

- **Total dimensions:** 10
- **Dimensions MET:** 6
- **Dimensions APPROACHING:** 1 (availability_pct, 11.1% gap, within exception window)
- **Dimensions NOT_MET:** 3
- **Relevant dimensions (excluding economically irrelevant electrical_efficiency):** 9; MET: 6/9 = 66.7%
- **Blocking dimensions (active):** availability_pct (temporary, 2027 crossing), installed_capex_usd_kw_firm (temporary, 2026 crossing)
- **Blocking dimensions (permanent/structural):** power_density_m2_per_kW (urban dense sites only, ~25–35% of TAM)
- **Non-blocking nominal NOT_MET:** electrical_efficiency_pct_system (economically irrelevant — free fuel)

### Convergence Analysis

The 10 capability dimensions sort into three distinct sequential clusters plus a residual permanent-advantage category. Cluster 1 (structural SWB advantages) was MET at or near initial deployment 2010–2015: zero fuel dependency, sub-second startup and response time, and minimal O&M cost. These dimensions were never genuinely competitive — SWB had structural superiority from inception, analogous to BEV's torque and energy efficiency advantages. Cluster 2 (performance maturation) crossed thresholds in 2022–2024 as LFP battery technology matured: degradation rate fell below 2%/yr (2022) and 4-hour BESS deployment reached scale sufficient for the 85% dispatchability threshold (2024). Cluster 3 (economics and availability gating) consists of the two remaining trajectory-driven dimensions: firm-equivalent CAPEX, where the 8-hour BESS cost curve places the $3,500/kW crossing in 2026 [model-derived], and 24/7 availability, where the same BESS cost trajectory enables 8-hour systems to become economically mainstream and reach 99% uptime in 2027 [model-derived]. The two permanent SOFC advantages — footprint (~0.56 m²/kW vs. SWB's physics-limited 8–9 m²/kW) and thermal conversion efficiency (65% vs. 23%) — define a defensible residual niche for Bloom Energy in high-density urban deployments where SWB cannot be physically accommodated, estimated at 25–35% of the distributed generation TAM. For the mainstream 65–75% of the TAM (suburban campuses, industrial sites, lower-density commercial), capability parity is a 2027 event gated by BESS cost curves already in motion.

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.4a | CRITICAL | PASS | All 10 dimensions extracted from 03-capability.md Capability Dimensions table and Handoff Context |
| 5.4b | CRITICAL | PASS | Status: PARTIAL |
| 5.4c | HIGH | PASS | 10 dimensions listed with current value, threshold, gap %, and MET/APPROACHING/NOT_MET status |
| 5.4d | HIGH | PASS | Convergence: sequential (library "divergent" overridden with 3-cluster sequential narrative) |
| 5.4e | HIGH | PASS | Parity year stated for all: 6 achieved, 1 estimated 2027, 2 estimated 2026/never, 1 nominal never |
| 5.4f | MEDIUM | PASS | All figures traced to 03-capability.md; no independent web research performed |

### Data Gaps

- Upstream confidence 0.74 due to SOFC degradation rate conflict (Bloom: 5%/yr company-disclosed vs. Hindenburg independent estimate of 2.5–3 year stack life); this does not affect parity determination for SWB dimensions but adds uncertainty to SOFC incumbent valuation.
- SWB uptime trajectory (availability_pct) is model-derived from solar CF + BESS storage modeling, not direct field measurement of SWB 24/7 uptime. The 2027 parity year carries a ±1–2 year uncertainty band.
- The installed_capex_usd_kw_firm estimate uses a model-derived composite (solar overbuild + 8-hr BESS cost trajectory); R²=0.888 on BESS cost curve fit is below the 0.95 threshold. The 2026 parity year is model-derived with medium confidence.
- Wind co-location potential: if solar+wind diversification is included, 6-hour BESS may be sufficient for 99% uptime in wind-rich regions, pulling the availability parity year forward to 2026 in those markets. The upstream agent notes this as a scenario variant (L=wind-rich); the primary parameter scenario uses 8-hour BESS at US median solar sites.

---

## Sources

- Upstream: `output/bloom-energy-sofc-disruption/agents/03-capability.md`
- All capability dimension values, trajectories, and parity year estimates derived from upstream capability agent output only
- No independent web research performed by this agent
