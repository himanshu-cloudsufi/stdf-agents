---
name: Data source reliability patterns by sector
description: Which T1 web sources work for which technologies, and unit conversion flags for cost-fitter
type: feedback
---

## BEV / Battery Sector

**Reliable T1 web sources:**
- U.S. DOE Vehicle Technologies Office FOTW series (energy.gov) — battery pack $/kWh, 2008–2023, model-derived via Argonne BatPaC. Anchor points confirmed at 2008=1415, 2021=157, 2022=153, 2023=139 $/kWh.
- FuelEconomy.Gov — BEV energy consumption (kWh/100km), historical, reliable
- World Bank — gasoline retail prices, historical, confirmed reliable

**Unit confusion patterns:**
- Catalog battery pack cost uses rated-energy basis; DOE uses usable-energy basis → ~5-10% difference is normal, NOT a conflict
- BEV median purchase price in catalog (~$31-52k USA) is MUCH lower than market-average transaction price (~$56-67k USA) because catalog reflects production cost trend, market data reflects luxury-mix
- ICE all-in $/mile series (AAA) bundles depreciation, fuel, insurance, maintenance — DO NOT present as fuel cost; flag as bundled for cost-fitter

**Gasoline price multi-series issue:**
- WorldBank.Org gasoline files contain multiple sub-series per region (10-12 series), each with overlapping years
- Must compute per-year median from all sub-series to get clean annual value
- Use: `from collections import defaultdict; statistics.median(by_year[yr])`

## Common Cross-Source Conflicts

1. Battery pack cost ~2022: catalog T2 = $166/kWh, DOE T1 = $153/kWh. Resolution: measurement basis difference (market median vs production-optimized). Both retain.
2. BEV ATP web vs catalog: $67k (Cox Automotive) vs $33k (catalog). Resolution: catalog = cost-trend proxy; web = market-mix reality. Both have uses.

**Why:** Knowing these conflicts in advance avoids re-running the validation logic from scratch.
**How to apply:** When the cost-fitter or downstream agent questions the BEV price discrepancy, cite this pattern.
