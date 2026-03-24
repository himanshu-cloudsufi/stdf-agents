---
name: Oil market multi-sector synthesis patterns
description: Synthesis patterns, conflict resolution, confidence calibration, and analytical structures from the oil market disruption analysis (2026-03-16)
type: project
---

## Key synthesis patterns from the oil market analysis (2026-03-16)

### Multi-incumbent disruption requires sector-decomposed tipping conditions
Oil is not disrupted by a single technology. Three simultaneous disruption fronts (transport BEV, power SWB, heating ASHP) each have distinct cost parity years, capability status, and adoption phases. The synthesizer must run three independent tipping condition tables rather than a single table. The binding constraint for the composite oil demand peak is NOT the most-disrupted sector (power: already tipped) nor the least-disrupted (heating: structural barriers unresolved before 2030) — it is the middle sector (transport) via fleet turnover dynamics.

**How to apply:** For any multi-incumbent disruption, map tipping conditions independently per sector and then identify which sector's adoption readiness governs the composite demand peak timing.

### Ratchet mechanism as the core answer to supply-constraint questions
When the user asks "will supply constraints accelerate disruption?" the analytical answer is the ratchet mechanism: oil price spikes above $80–90/bbl compress disruptor payback periods and permanently advance adoption decisions, while normalization does not reverse already-installed disruptors. This is quantified: +$10/bbl WTI → ICE +$0.003/km (transport), +$7/MWh thermal (heating). Evidence: USA transportation oil demand peaked 2007, still 9.6% below peak despite 17 years of growth — permanent demand destruction via historical price shocks.

**Why:** Users asking about supply constraints are often conflating the incumbent's ability to manage price with the disruptor's cost trajectory. The ratchet resolves this — they operate on different mechanisms.

### Atypical cost curve for heat pumps — rising installed cost exception
ASHP installed costs in the USA rose 29% from 2015 to 2024 due to labor costs and regulatory efficiency standard changes. This is a documented exception to the standard STDF exponential decay model. The Cost Curve agent correctly used a linear rising model for HP full cost (C_HP rising +$3.58/MWh/yr) and noted that HP disruption operates through running cost advantage (COP 2.8 = 2.8x thermal per unit electricity), not installed cost decline. Synthesizer should flag this as a structural exception and differentiate running-cost parity (achieved ~2010) from full-cost parity (requires WTI > $120/bbl).

**How to apply:** If a disruptor has a rising installed cost, separate running-cost parity from full-cost parity in Phase 5 and provide a WTI/price sensitivity table for the full-cost parity threshold. This is the canonical treatment for energy-service substitutes where efficiency amplification is the mechanism.

### Confidence calibration for multi-sector oil analysis
Five-agent pipeline on a data-mixed sector (transport: heavy catalog; heating: sparse web data; petrochemicals: no catalog) produces confidence range 0.74–0.83, mean 0.784. The tipping point agent is typically the lowest-confidence agent in multi-sector oil analysis because it must integrate three S-curves with an unquantified demand offset (petrochemicals). The cost curve agent is second-lowest because of the HP rising-cost exception and the component-model EV service cost derivation.

### S-curve parameter conflict resolution — confirmed again
Tipping point agent estimated x0=2030 (L=0.95, top-down) for global BEV; Adoption agent fitted x0=2028.6 (L=0.88, scipy, 11 pts, R²=0.972). Resolution per canonical pattern in memory: Adoption agent for S-curve computation, Tipping agent for rupture window. This pattern held in the BEV-ICE analysis and holds again here. L=88 vs. L=95 is a material but not contradictory divergence (~6–7pp in 20-year computations).

### Fleet turnover as the binding constraint pattern
In any vehicle fleet disruption, the binding constraint for physical commodity demand destruction is fleet turnover rate (~6%/yr globally), not new-sale share crossing. New-sale share crossing is the leading signal; fleet-level demand destruction is the lagging confirmation. The lag is 8–12 years. This means cost parity and capability parity can be met for 10+ years before aggregate oil demand responds — which is the case for oil transport (parity met 2015–2016; demand peak 2027–2030).

**How to apply:** Always compute fleet-level displacement in addition to new-sale share for any fuel displacement analysis. The fleet displacement table (year, BEV fleet M, oil displaced Mbpd, % of transport demand) is a required output for oil market synthesis.

### China as structural leading indicator
China leads the global BEV S-curve by 4–5 years over Europe and 6–8 years over the USA. China's oil consumption plateau (2023–2024: 16.86 → 16.72 Mbpd, −0.8%) is the most significant leading indicator for the global demand peak — China represents 16.2% of global demand. When China's structural demand peak is confirmed by 2–3 additional data years, the global composite peak range will compress from a 3-year window to a 1–2 year window.

### USA policy shock handling (federal EV tax credit expiry)
USA BEV market share declined from 9.2% (2024) to 7.5% (2025) due to the federal EV tax credit expiry in September 2025. This is a policy shock, not a structural reversal. The Adoption agent correctly included the 2025 data point in the S-curve fit (which widened the CI and shifted inflection to x0=2032.6) rather than excluding it. The synthesizer should provide the specific policy event as context and note the structural dynamics remain intact.

---

## Effective narrative structure for oil market multi-sector analysis

Phase 1 — Establish the four-sub-domain structure immediately; identify petrochemicals as resilient to set the demand offset context.
Phase 2 — Three matchup tables (transport $/km, power $/MWh, heating $/MWh thermal); highlight the HP rising-cost exception.
Phase 3 — SWB convergence (power) and SWB-EV convergence (transport) are the two most important convergences; ASHP-SWB is third and has a building-system-replacement-cycle permanence argument.
Phase 4 — Dual-vector disruption label is essential for BEV (Tesla From Above + BYD From Below simultaneously); power generation is Systemic; heating is From Below with sequential convergence.
Phase 5 — Lead with the transport cost parity year (2015–2016) because it is the most counterintuitive finding (parity was 10 years ago yet oil demand still grew). The ratchet mechanism belongs here.
Phase 6 — The fleet displacement table is the most important quantitative output; show it prominently. The regional BEV share table (China 32%, Europe 19%, USA 7.5%) anchors the regional divergence narrative.
Phase 7 — The composite tipping conditions table (9 rows, 3 sectors × 3 conditions) is the full analytical summary; the ratchet and post-tipping death spiral mechanism are the closing argument.
