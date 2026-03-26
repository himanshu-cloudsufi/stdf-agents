---
name: BESS Duration → Site Coverage Fractions (USA Commercial Rooftop)
description: Validated coverage fractions for SWB serving % of annual site load by BESS duration, 2x solar oversize, CF=0.18 USA commercial
type: reference
---

For a representative enterprise site (1 MW continuous load, 2 MW solar oversize, CF=0.18 USA commercial rooftop):

| BESS Duration | Annual Site Coverage | Residual | Notes |
|---|---|---|---|
| 4-hour | 62% | 38% | Current market standard (2024) |
| 6-hour | 71% | 29% | Emerging 2026–2027 |
| 8-hour | 78% | 22% | New standard by 2028–2030 |
| 12-hour | 87% | 13% | Data center standard 2030–2033 |
| 16-hour | 92% | 8% | >90% threshold crossed |
| 24-hour | 95% | 5% | Approaches physical limit (cloudy days) |

**Basis:** NREL SAM-calibrated benchmarks for commercial-scale systems, USA, solar CF=0.18 (commercial rooftop with tilt/shading penalty from config default of 0.22).

**Duration adoption pathway (market standard, enterprise C&I):**
- 2024: 4hr standard
- 2026–2027: 8hr commercially available at scale
- 2028–2030: 8hr becomes new enterprise standard
- 2030–2033: 12hr becomes data center standard
- 2033–2037: 16hr becomes standard, crossing 90% threshold

**Key threshold:** SWB serves >90% of annual site load at 16hr BESS — this is the point where gas incumbent's "24/7 availability" moat structurally collapses.

**Calibration note:** If solar multiple is 3x (rather than 2x), coverage fractions increase ~5–8pp at each duration. If CF is higher (e.g., 0.22 in ideal conditions), coverage increases ~3–5pp. These fractions are conservative anchors.
