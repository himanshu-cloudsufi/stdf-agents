---
name: BEV Trucks China Regional Demand Run
description: Key findings and parameters from within-China sub-national disaggregation of BEV HDT commodity demand (bev-trucks-china pipeline run)
type: project
---

Sub-national China run disaggregated 900,000-unit HDT market into 5 regions. Output: `output/bev-trucks-china/agents/07d-regional-demand.md`.

**Reconciliation scalars (regional model → 07b totals):**
- Lithium: 1.05 at current, 1.02 at +20yr (weighted regional L=88.35% vs. national L=90%)
- Copper: 1.03 at current, 1.02 at +20yr

**Regional LNG displacement fractions used:**
- Eastern (YRD): 30%, Northern (BTH): 28%, PRD: 25%, Central: 25%, Western: 18%
- Eastern + Northern account for 58.7% of national LNG displacement in 2026

**Key demand finding:** Central China overtakes Eastern YRD as the largest lithium consumer at +5yr (60.3 vs. 65.1 kt LCE) due to larger market size (225k units each) but later inflection (x0=2027.09 vs. 2026.13). Eastern leads only in the near term by virtue of earlier S-curve inflection.

**Western China fastest CAGR:** Lithium 33.2%/yr (2026–2031); copper 15.0%/yr — reflects tipping-phase catch-up dynamics from lowest base.

**Why:** bev-trucks-china is a China-domestic analysis; cross-national breakdown is supplementary only.
**How to apply:** When this pipeline is re-run or extended, use these regional LNG fractions and reconciliation scalars as starting priors. They are calibrated, not guessed.
