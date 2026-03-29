---
name: BEV ICE capability gap analysis
description: Key parameters and data from the bev-ice-capability pipeline run — battery costs, S-curve fit, disruption classification
type: project
---

Analysis slug: bev-ice-capability
Analysis date: 2026-03-27

Key data anchors:
- Li-Ion battery pack global median: $1,436/kWh (2010) → $115/kWh (2024), 18.4%/yr decay, R²=0.954 [Rethinkx]
- BEV-specific passenger pack: $179/kWh (2019) → $97/kWh (2024), 9.7%/yr decay, R²=0.778 [Rethinkx]
- BEV new sales S-curve: L=100%, k=0.3687, x0=2029.1, R²=0.973 (15 data points, 2010-2024)
- BEV new sales share 2024: 12.2% globally — past tipping point, acceleration phase
- China BEV median $16,200 vs ICE mid-sedan $19,000 — BEV 14.7% cheaper (2024, observed)
- US BEV median $31,000 vs ICE mid-sedan $29,500 — at parity (2025, observed)

Disruption classification:
- Type: From Above (2012-2022) + Big Bang (2022-present, China)
- BEV flow type: Hybrid (Stellar-dominant)
- ICE flow type: X-Flow
- PHEV: Chimera (Hybrid, X-Flow-dominant)

**Why:** This is the foundation run for a CUSTOM 5-agent pipeline (domain-disruption, cost-researcher, capability, capability-parity-checker, synthesizer).

**How to apply:** If asked about BEV/ICE disruption again, these data anchors are validated and can be cited directly from the catalog files listed in the agent output.
