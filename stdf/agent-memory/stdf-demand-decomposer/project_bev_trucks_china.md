---
name: BEV HDT China — material intensity and decomposition values
description: Confirmed material intensity coefficients and demand decomposition outputs for BEV heavy trucks displacing LNG/diesel in China; use for downstream agents and future runs
type: project
---

# BEV HDT China — Demand Decomposer Output Summary

Analysis date: 2026-03-20. Output: `output/bev-trucks-china/agents/07a-demand-decomposer.md`

## Market Structure (2025, observed/model-derived)
- Total China HDT: 900,000 units/yr
- BEV share: 22% = 198,000 units [observed, IEEFA Aug 2025]
- LNG share: ~25% = 225,000 units [model-derived, declining from 29% peak in 2024]
- Diesel share: ~53% = 477,000 units [model-derived]
- Segment split: urban/regional 45% (405k), captive 20% (180k), long-haul 35% (315k)

## Material Intensity Coefficients (per market product)

### Lithium (LCE)
- BEV heavy tractor-trailer 49t (350 kWh avg): **280 kg LCE/truck** (= 350 kWh × 0.8 kg LCE/kWh)
- BEV heavy tractor-trailer 49t (282 kWh): 226 kg LCE; (423 kWh): 338 kg LCE
- BEV heavy rigid >14t (200 kWh avg): **160 kg LCE/truck**
- CATL 75# swap block (282 kWh): **225.6 kg LCE/block**
- LNG HDT: 0 | Diesel HDT: 0

### Iron Phosphate (FePO4) — stoichiometric from LiFePO4
- BEV tractor-trailer 49t (350 kWh): **1,143 kg FePO4/truck** (= 423.2 kg Fe + 234.7 kg P + 485.1 kg O4)
- BEV heavy rigid >14t (200 kWh): **653 kg FePO4/truck**
- LCE-to-Fe conversion: 52.6 kg Li metal → 7,578 mol → 423.2 kg Fe (1:1 molar ratio)
- MW(LiFePO4) = 157.76; LCE factor = 5.323 (= MW(Li2CO3) / (2 × MW(Li)))

### Copper
- BEV tractor-trailer 49t: **100 kg Cu/truck** (range: 80–120)
- LNG tractor-trailer 49t: **27.5 kg Cu/truck** (range: 25–30)
- Diesel tractor-trailer 49t: **27.5 kg Cu/truck** (range: 25–30)
- Swap station: **10 kg Cu/station** (range: 8–12)
- Depot charger port: **20 kg Cu/port** (range: 15–25)
- Incremental Cu from BEV vs. incumbent: +72.5 kg/unit

### Natural Gas / Diesel (displacement per truck/year)
- BEV replacing LNG truck: 12,000 kg LNG/yr eliminated
- BEV replacing diesel truck: 6,500 L diesel/yr eliminated

## 2025 Annual Demand Totals (new vehicle flows)
- Lithium: **63.94 kt LCE/yr** (tractors 55.44, rigid 1.73, swap 6.77)
- Iron phosphate: **~252.6 kt FePO4/yr** (tractors 226.3, rigid 7.1, swap 10.1)
- Copper (HDT segment): **39.15 kt Cu/yr** (BEV 19.8, diesel 13.1, LNG 6.2, infra 0.05)
- Incremental copper from disruption: **+14.4 kt Cu/yr**
- LNG displaced: **0.59 Mt/yr = 0.82 BCM/yr** natural gas equivalent
- Diesel displaced: **6.11 million barrels/yr**

## BEV Units Replacing LNG vs. Diesel (2025 cohort, model-derived)
- Total BEV replacing LNG: 48,938 (long-haul 12,600, captive 14,400, urban 21,938)
- Total BEV replacing diesel: 149,062
- Displacement fractions: long-haul 80/20 LNG:diesel; captive 40/60; urban 15/85

**Why:** These are inputs needed by 07b-stream-forecaster and 07c-fleet-modeler.
**How to apply:** Use these coefficients directly for stream forecasting. Confirm battery size assumption (350 kWh avg) has not changed before applying.
