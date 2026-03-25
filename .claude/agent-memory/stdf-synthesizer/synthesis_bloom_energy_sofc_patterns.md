---
name: Bloom Energy SOFC disruption synthesis patterns
description: Synthesis patterns from ENERGY_FULL preset — counter-disruption growth phase, dual threshold structure, inverted China-leads pattern, enterprise BTM S-curve proxy construction, EIA inline tag format
type: project
---

## Analysis context

- **Slug:** `bloom-energy-sofc-disruption`
- **Pipeline preset:** ENERGY_FULL (13 agents: 11 core + 2 energy)
- **Final confidence:** 0.702
- **Rupture window:** 2028–2032
- **Short entry window:** 2028–2030 (not the tipping year)
- **Binding constraint:** cost_parity (LCOE parity 2031–2032)
- **Tipping year:** 2031

---

## Key synthesis patterns

### Counter-disruption growth phase masking structural decline

When the incumbent is in an AI-driven demand surge (Bloom revenue +37.3% in 2025, observed), the tipping year and the short entry date are structurally separated:
- Revenue peak: 2027–2028 (2–3 years AFTER S-curve crosses 10%)
- Short entry: 2028–2030 (when revenue decelerates and LCOE gap closes within enterprise procurement horizon)
- Tipping year: 2031–2032 (when new orders collapse)

The gap between 10% S-curve threshold (2025.6) and revenue peak (2027–2028) is created by the TAM expansion outrunning the share loss — analogous to chimera behavior at the company level.

**How to apply:** Any future synthesis where an incumbent has a non-disruption TAM driver (AI, grid interconnection delays, etc.) should explicitly model the revenue peak separately from the tipping year, and place the short entry at revenue peak, not at tipping year.

---

### Dual threshold structure (user override: marginal cost primary)

When the user overrides to MARGINAL COST as the primary metric, report two thresholds:
1. LCOE parity (new-vs-new procurement comparison) — commercial displacement signal, used for tipping condition
2. Marginal cost kill (build new SWB vs. pay fuel on existing box) — existential endpoint, not the tipping condition

For Bloom: LCOE parity at 2031–2032; marginal cost kill at 2038–2042. The tipping-synthesizer correctly binds to Threshold 1 (LCOE parity) per user override for the tipping year calculation.

**How to apply:** Always report both thresholds when user override is marginal cost framing. State explicitly which threshold drives the tipping condition.

---

### SWB LCOE basis conflict: capacity vs. delivered MWh

Energy-dispatch ($76.6/MWh for 4hr BESS, "already below Bloom") conflicts with cost-parity-checker ($162.6/MWh, parity at 2031–2032). Resolution:
- Energy-dispatch uses per-MWh-DELIVERED basis with 2x solar oversize factor (CF=0.18 + 2x sizing)
- Cost-parity-checker uses capacity-basis amortization (no oversizing)
Both are correct for their respective frames. Prefer energy-dispatch for dispatch economics; prefer cost-parity-checker for procurement-level tipping condition (downstream-over-upstream rule).

**How to apply:** In energy sector analyses with behind-the-meter configurations, always check whether LCOE is expressed per-kW-rated or per-MWh-delivered. Different agents may use different bases legitimately.

---

### Inverted China-leads adoption pattern

In this disruption, China leads SWB adoption by volume (~16% BTM enterprise share) but has zero Bloom revenue exposure. The relevant competitive threat comes from Europe (leading the enterprise BTM reliability-grade segment at 13% share) and USA (65% of Bloom revenue). The regional-adopter correctly documented this inversion; synthesis must explicitly state it to avoid misinterpreting China data as relevant to the short thesis.

**How to apply:** Always check whether the incumbent has material China revenue before applying STDF standard China-leads prior. If no China revenue exists, document the inversion pattern explicitly.

---

### EIA inline tag format — "observed, CAUTION: EIA" fails validation

The combined format `[observed, CAUTION: EIA source]` fails the stdf_validate.py hook because `[CAUTION: EIA` does not appear at line start. The validator looks for the exact string `[CAUTION: EIA` at the beginning of a bracket — not inside a combined bracket like `[observed, CAUTION: EIA...]`.

**Correct format:** Write as two separate tags on the same line:
```
[observed] [CAUTION: EIA source — historical data only]
```
This passes the validator because `[CAUTION: EIA` appears on the same line as the `EIA` match.

**How to apply:** Always separate `[observed]` and `[CAUTION: EIA source]` tags. Never combine them in a single bracket.

---

### x0 conflict: tipping year vs. S-curve inflection

For enterprise B2B disruptions with 3–7 year procurement cycles, the scurve-fitter x0 (actual market share inflection) lags the tipping-synthesizer x0 (cost parity crossing) by approximately 3 years. This is economically coherent and not a true conflict — they measure different events. Document as "resolved: different events" and use both:
- Tipping-synthesizer x0 for the tipping year (procurement trigger)
- Scurve-fitter x0 for the S-curve inflection (market share flow inflection)

**How to apply:** For enterprise B2B markets, expect a 2–4 year lag between cost parity crossing and S-curve inflection. Flag and resolve in synthesis as measuring different events.

---

### Permanent footprint moat (25–35% TAM)

Stellar technologies (SWB) cannot overcome physical density constraints in high-density urban deployments. The ~0.56 m²/kW SOFC footprint vs. ~10 m²/kW SWB system creates a permanent 25–35% TAM niche that defines L<100% for the S-curve. This pattern appears consistently in energy disruptions where physical space constraints apply (data centers, urban hospitals). L=70% (not 100%) is the correct saturation ceiling.

**How to apply:** For any energy technology with a footprint dimension, check whether physical density constraints create a structural permanent niche. If yes, L<100% and document the niche size explicitly.

---

### "Outlook" section header trap — confirmed still active

Section headers named "Outlook" (e.g., "Energy Dispatch Outlook", "Energy Supply Outlook") trigger the forecast language validator. Use alternative headers:
- "Energy Dispatch Analysis" (not "Energy Dispatch Outlook")
- "Gas Supply and Displacement Analysis" (not "Energy Supply Outlook")
- "Regional Assessment" (not "Regional Outlook")

This trap was caught twice in this analysis. It was previously documented in synthesis_bev_trucks_china_patterns.md and synthesis_lead_demand_patterns.md but remains a recurring error.

**How to apply:** Never use "Outlook" in any section header in output files.
