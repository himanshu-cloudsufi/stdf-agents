---
name: BEV Heavy Trucks China — Capability Parity Findings
description: Key findings from capability parity evaluation for BEV vs LNG/NG heavy trucks in China (2026-03-20)
type: project
---

Capability parity condition: NOT_MET as of 2026-03-20. Status applies to full multi-dimensional long-haul parity. Urban/regional sub-segment (<300 km/day) achieved full parity in 2022.

**Why:** 7 of 11 dimensions MET, but met count (7) falls below 2/3 threshold (7.33), and all 3 NOT_MET dimensions carry gaps exceeding 15% (range_km_longhaul 20%, payload_penalty_t 33.3%, infrastructure_swap_per_50km 23.0%) — both aggregate conditions independently trigger NOT_MET.

**Curve-fitted full parity year:** 2026 (last blockers: range_km_longhaul and payload_penalty_t).

**Blocker cluster:** range_km_longhaul (crossing 2026), payload_penalty_t (crossing 2026), infrastructure_swap_per_50km (crossing 2025). All three driven by same LFP cost-curve dynamics.

**Convergence pattern:** lib returns "divergent" due to wide met_year spread (2015–2026); narrative is more precisely "sequential with terminal simultaneous cluster." Note this discrepancy when interpreting lib output in similar multi-cluster sectors.

**Segment bifurcation:** A critical output for downstream agents — capability parity is segment-dependent. Urban parity (2022) is already driving S-curve disruption adoption ahead of full-dimensional long-haul parity. Always carry segment qualification to tipping synthesizer.

**How to apply:** For future BEV-vs-incumbent evaluations with segment splits, always evaluate urban and long-haul conditions separately, and report both. NOT_MET at aggregate level does not mean disruption is not underway.
