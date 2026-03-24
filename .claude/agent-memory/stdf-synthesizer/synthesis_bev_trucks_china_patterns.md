---
name: BEV heavy trucks China synthesis patterns
description: Synthesis patterns, conflict resolution, vocabulary violations, chimera tri-incumbent structure, fleet-model uplift gap, and confidence calibration from BEV HDT displacing LNG/NG trucks in China (2026-03-20)
type: project
---

## Analysis context

- **Slug:** `bev-trucks-china`
- **Pipeline preset:** FULL+COMMODITY (15 agents: 11 core + 4 commodity demand)
- **Final confidence:** 0.794 (mean of 15 agents; no penalty; no cap)
- **Tipping window:** 2025–2026 (long-haul full-network); 2022 (urban/regional — already tipped)
- **Binding constraint:** capability_parity and adoption_readiness (co-binding at 2026)

---

## Key synthesis patterns

### k parameter conflict between tipping-synthesizer provisional and scurve-fitter fitted

The tipping-synthesizer ran before the scurve-fitter and produced a provisional k=0.30 (calibrated top-down without H1 2025 data). The scurve-fitter subsequently fitted k=0.7227 on 6 observed data points including the H1 2025 annualized 22% data point (R²=0.9950). Discrepancy: 2.41× steeper.

**Resolution per STDF priority rule "granular specialist over generalist":** scurve-fitter's fitted k supersedes the tipping-synthesizer's provisional k. The material consequence: 80% completion year shifts from 2031.6 (provisional) to 2029.5 (fitted); death spiral threshold moves from ~2031 to 2027.

**Why this matters:** The H1 2025 data point was the critical anchor that the tipping-synthesizer lacked. When the scurve-fitter runs after a high-penetration data point arrives, expect its k to be materially higher than the tipping-synthesizer's provisional. This is the canonical pattern in a fast-growth disruption.

**How to apply:** In any synthesis, always check whether the most recent adoption data point arrived after the tipping-synthesizer ran. If yes, the scurve-fitter's k is authoritative. Flag and quantify the forward revision to 80% completion year.

---

### Chimera tri-incumbent structure (LNG-as-chimera)

This analysis features a complex incumbent structure: diesel (original dominant), LNG/CNG (prior disruptor-turned-chimera), BEV (current disruptor). The LNG S-curve peaked at model-derived 2023.3 at 25.8% share (ICCT-observed ~29% in 2024, 3.2 pp discrepancy). This is a canonical chimera hump-shape — LNG rose as a diesel disruptor, peaked as a chimera, and is now in accelerating decline as BEV disrupts the full incumbent-chimera stack simultaneously.

**Pattern:** Disruptions of disruptions create tri-incumbent arenas. The synthesis must track all three streams simultaneously, not just the primary BEV-vs-LNG framing. The chimera (LNG) acts as a transitional technology that captured market share before stalling due to its own unresolved TCO and capability disadvantages vs. BEV.

**How to apply:** Whenever domain-disruption identifies a "prior disruptor now stalling" designation, verify: (a) is it still gaining share (early chimera) or losing share (late chimera)? (b) Does the commodity demand model track the chimera stream separately? The 3-stream demand model (incumbent/disruptor/chimera) handles this correctly — ensure it is invoked in FULL+COMMODITY runs.

---

### Fleet-model mid-life battery replacement uplift is a systematic gap in stream-only projections

The stream-forecaster (flow-based) showed 2036 Li demand of 254.20 kt LCE. The fleet-modeler (stock-flow with mid-life battery replacement) showed 336.59 kt — a **+32.4% uplift** at +10 years. This gap is systematic: any flow-based model that treats batteries as non-consumable assets will understate Li demand by ~30% at peak fleet maturity (year +10 after tipping).

**Why:** Mid-life battery replacement (50% of pack at year 4–5) adds a third demand component (alongside OEM demand and full-replacement demand) that only materializes 4–5 years after BEV fleet deployment begins at scale. At tipping, this component is near-zero; by fleet maturity (+10yr), it can exceed OEM demand.

**How to apply:** In any FULL+COMMODITY synthesis, always compare stream-forecaster and fleet-modeler +10yr projections. If the fleet-modeler is ≥15% higher, flag the mid-life battery replacement component as a systematic uplift driver and use the fleet-model figure as primary for long-term demand projections (+10yr+). Use the stream-forecaster as primary for near-term (+5yr).

---

### Segmented tipping obscures aggregate market share readings

The 22% H1 2025 aggregate BEV market share reflects two very different sub-segments: urban/regional (already tipped 2022, likely 35–50% by 2025) and long-haul (<10% in 2025). Aggregate figures systematically understate disruption progress in the leading sub-segment and overstate it in the lagging one.

**How to apply:** When any domain-disruption or tipping-synthesizer output identifies multiple sub-segments with different tipping timelines, always report rupture windows per segment. The aggregate figure is useful for total market sizing; it is not a meaningful progress indicator for any single sub-segment.

---

### Vocabulary violations caught by pre-commit hook — patterns to avoid

The STDF validation hook blocked the first write of `00-final-synthesis.md` with 4 violations:
1. **"transition"** (2 occurrences): "OEM-to-replacement transition" → "OEM-to-replacement demand shift"; other instance also replaced with "shift" or "displacement"
2. **"Outlook"** (3 occurrences in section headers): renamed to "Commodity Demand Implications" (Phase 5 subsection), "Commodity Demand — Post-Tipping Implications" (Phase 7 subsection), "Regional Analysis" (top-level section)

**Pattern:** Section headers for commodity demand subsections are a recurring trap — "Outlook" is an intuitive label but banned. Use "Implications" or "Analysis" instead. The word "transition" appears naturally when describing fleet dynamics; replace with "shift," "displacement," or "demand change."

**How to apply:** Before writing any synthesis file, scan section headers for "Outlook," and scan fleet/market descriptions for "transition." These are the two highest-frequency accidental violations in synthesis outputs.

---

## Confidence calibration notes (15-agent FULL+COMMODITY run)

- **Mean confidence 0.794** — slightly lower than BEV-ICE (0.848). The primary drag is two agents at 0.72: capability-parity-checker (payload penalty data gap) and regional-demand-analyst (absence of sub-national HDT BEV registry data). In sectors where sub-national demand data is unavailable, the regional-demand-analyst consistently floors near 0.72–0.74.
- **Cost-fitter confidence (0.74)** was pulled down by a 3-point CNY tractor price series (low-N fit). When the primary purchase price series has N≤3 data points, the R² will appear artificially high (0.993) but the agent correctly self-reports low confidence. Always flag low-N fits regardless of R².
- **Scurve-fitter at 0.87** (ceiling) — consistent with BEV-ICE observation. When 5+ empirical data points produce R²>0.99 on a logistic fit, the agent confidence is high despite other pipeline uncertainties.
- **Demand-decomposer at 0.84** — the highest non-scurve-fitter confidence in this pipeline. When material intensities are well-characterized (BEV Li/Cu intensities are catalog-confirmed), the decomposer produces high-confidence outputs.

---

## Effective narrative structure for BEV HDT / China market sector

Phase 1 (Sector Scoping) → establish tri-incumbent arena (diesel-chimera-LNG + BEV) and the BSAF convergence driver up front; highlight segmented tipping (urban 2022 already done).
Phase 2 (Tech Inventory) → anchor on LFP cost trajectory (the primary driver); include the TCO comparison table (CNY/km).
Phase 3 (Convergence Analysis) → BSAF is the core narrative (Battery-Swap-Autonomous-Fleet); show how it compresses the three threshold crossings toward a single 2025–2026 window.
Phase 4 (Disruption Pattern) → the 11-dimension capability table; highlight the segmented pattern (urban MET vs. long-haul NOT_MET); co-binding constraint framing.
Phase 5 (Business Model Shift) → the three tipping conditions table (MET/NOT_MET/PARTIAL) is the decisive anchor; include fleet model OEM vs. replacement crossover for commodity demand subsection.
Phase 6 (Adoption + S-curve) → lead with scurve-fitter parameters (k=0.7227 vs. provisional 0.30 — flag the revision explicitly); regional comparison table; X-curve trauma mechanisms.
Phase 7 (Synthesis) → regional tipping sequence (Eastern 2022 → Western 2027); commodity demand post-tipping implications using fleet-model +10yr figure as primary; death spiral threshold 2027.

---

## Data gaps recurring in HDT / heavy transport analyses

- No sub-national heavy-truck registry data for China (sub-provincial granularity)
- No dedicated truck model purchase price time-series in catalog (requires T3 web scraping)
- Maintenance cost available as point estimate only, not as time series
- Battery swap throughput unverified (60/day/station is model-derived)
- Western China regional data quality consistently LOW-MEDIUM in all sub-national analyses
- LNG truck plant closure data absent (makes LNG stranded asset analysis model-derived only)
