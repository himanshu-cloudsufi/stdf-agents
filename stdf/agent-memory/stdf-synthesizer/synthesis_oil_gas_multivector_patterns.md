---
name: synthesis_oil_gas_multivector_patterns
description: Multi-vector synthesis patterns from oil and gas demand disruption (V1+V2+V3 simultaneous): metric mismatch resolution, CONTINGENT tipping logic, vocabulary trap in pipeline slug path, confidence penalty mechanics, and structural floor dynamics
type: project
---

## Multi-Vector Synthesis Patterns (Oil and Gas Demand, 2026-03-20)

### V2 S-curve metric mismatch — highest-priority conflict resolution pattern

The tipping-synthesizer used V2 S-curve parameters derived from solar share of *new capacity additions* (provisional: L=85, k=0.30, x0=2027.5). The scurve-fitter used solar share of *electricity generation* (authoritative: L=45, k=0.2279, x0=2031.6). These are numerically consistent — 2024 capacity share was ~76%, generation share was ~6.92% — but describe completely different phenomena.

**Resolution:** Always use generation share (not capacity additions share) for V2 demand displacement calculations. Capacity additions share overstates displacement because: (1) solar capacity factors are below 100%; (2) the existing gas fleet is not immediately retired. The tipping year from the tipping-synthesizer (2027–2028) is NOT invalidated — it is based on capability parity (dispatchability index), not the S-curve inflection. Only downstream demand volume estimates must use scurve-fitter generation share parameters.

**Why:** This is a common pattern when provisional S-curve parameters (used by tipping-synthesizer before scurve-fitter runs) differ from authoritative fitted parameters. The fix is always: keep the tipping year, replace the demand volume projection parameters.

### CONTINGENT tipping — V3 is structurally different from V1/V2

V3 (ASHP vs. gas heating) has a fundamentally different cost structure than V1 and V2: ASHP capital costs are RISING (no learning curve), while US gas prices ($2.19/MMBtu) are structurally low. This means V3 is CONTINGENT — not just slower but conditionally gated on either (a) gas price increases or (b) HP capital cost decline.

**Synthesis rule:** When one vector in a multi-vector analysis is CONTINGENT, do NOT average it into a composite tipping score or blend it with the MET vectors. Report it separately with explicit CONTINGENT designation. The composite tipping year covers only the MET/PARTIAL vectors (V1: 2027, V2: 2027–2028).

**Why:** Averaging a CONTINGENT vector with MET vectors misleads downstream users. A composite tipping of "2027–2040" is analytically useless.

### Vocabulary trap — pipeline slug path contains "outlook"

The pipeline slug for this analysis is `oil-gas-outlook`. Any reference to the agents directory path as `output/oil-gas-outlook/agents/` in the final synthesis document triggers the STDF validation hook's `\boutlook\b` regex (because hyphens are word boundaries in Python regex).

**Fix:** In the Sources section and anywhere else the full directory path would appear, write "agents directory" or "this pipeline run" instead of the literal path. The hook scans the *content* being written, not just section headers.

**Why:** The previous BEV HDT China session identified "Outlook" in section headers as a trap; this session revealed the trap extends to *path strings* embedded in the document. Both are blocked by the same regex.

### Confidence penalty mechanics — HIGH failure dominates

In this analysis, base mean confidence = 0.783. Two missing agents:
- fleet-modeler (MEDIUM): −0.10 → manageable
- regional-demand-analyst (HIGH): −0.30 → dominant penalty

Final confidence = 0.383. The −0.30 HIGH failure for regional-demand-analyst is the single largest factor — it reduces confidence by 38% of the base mean. For commodity-demand queries, regional-demand-analyst is the HIGH-criticality agent that almost always causes the biggest degradation when absent.

**Calibration insight:** When running FULL+COMMODITY pipeline, regional-demand-analyst absence will produce a final confidence roughly 0.30 below the base agent mean. At base mean 0.78, final = 0.48. At base mean 0.75, final = 0.45. This is the expected confidence floor for commodity analyses with missing regional demand.

### Structural floor dynamics — oil vs. gas have different floor shares

Oil: 54.4 mb/d structural floor = 52.6% of 2024 total. By 2046, floor grows to ~60.7 mb/d = 74% of the 73.0 mb/d total. The floor grows in absolute terms and dominates at long horizons because disruption-eligible demand has been largely displaced.

Gas: 1,725 bcm structural floor = 42.0% of 2024 total. By 2046, floor grows to ~1,928 bcm = 74% of 2,601 bcm total. Same pattern.

**Why this matters for synthesis:** At +20yr, the dominant uncertainty is NOT S-curve parameter uncertainty — it is structural floor growth rate uncertainty (±0.3%/yr sensitivity). The oil structural floor (aviation, marine, petrochemicals, off-road) is less likely to be disrupted within 20 years than the gas structural floor (industrial process heat could be disrupted by electrolytic hydrogen post-2035). Gas demand tail uncertainty is therefore larger than oil.

### Regional asymmetry — V3 displacement is structurally coal, not gas in China

China's primary heating incumbent in northern China is coal-fired district heating, NOT gas boilers. This means V3 demand destruction in China does NOT reduce gas demand — it reduces coal demand (a different commodity). This structural asymmetry means cross-region V3 comparisons should be explicit about what incumbent is being displaced, not just that "heat pumps are growing."

**How to apply:** In Phase 6 regional analysis, always note that China V3 = coal displacement story; Europe and USA V3 = gas displacement story. Do not conflate them in gas demand projections.

### Cross-vector amplification — V1 battery supply chain accelerates V2 BESS by 1–2 years

This is a structural interaction that the tipping-synthesizer explicitly quantified: V1 BEV mass production drives battery cost decline (16.45%/yr), which reduces BESS costs (9.04%/yr on its own) by an additional estimated 1–2 years. The mechanism is shared manufacturing, supply chain, and chemistry between EV batteries and stationary BESS.

**Why this matters:** Multi-vector analyses should always check for cross-vector supply chain amplification. When V1 and V2 share the same key material (lithium-ion batteries), V1 adoption subsidizes V2 cost decline. This asymmetric amplification creates a stronger combined disruption than two independent S-curves would suggest.

### Section header anti-patterns — confirmed blocked list

Confirmed blocked by STDF validation hook as of 2026-03-20:
- "Commodity Demand Outlook" → use "Commodity Demand Impact"
- "Regional Outlook" → use "Regional Analysis"
- Any path string containing `oil-gas-outlook` or any directory slug with "outlook" as a word-boundary-delimited substring

**Why:** .claude/hooks/stdf_validate.py uses `\boutlook\b` IGNORECASE regex. This matches the word "outlook" whether it appears in section headers, body text, inline code, or path strings where the surrounding characters are non-word characters (hyphens, slashes, backticks).
