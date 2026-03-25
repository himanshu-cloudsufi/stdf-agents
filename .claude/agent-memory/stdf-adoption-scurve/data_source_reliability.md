---
name: Data source reliability notes for adoption analysis
description: Notes on which catalog data sources are reliable for market share computation and adoption curve fitting
type: reference
---

## Reliable Sources in Catalog

**Rethinkx (STDF catalog):** Highly reliable for annual BEV and total new car sales by region (Global, China, Europe, USA, Rest of World). Market share should be COMPUTED from the ratio of BEV sales / total sales — do NOT use secondary sources that report market share directly (they often mix BEV+PHEV).

- BEV-only series: `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_*.json`
- Total market: `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_*.json`
- ICE-only: `data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Annual_Sales_*.json`

**Important caveat:** China web sources often report "NEV" (BEV+PHEV) share (~50% in 2025), not BEV-only (~32% in 2025). Always disambiguate.

## Methodological Note
When fitting S-curves to early-growth data (<25% of L ceiling reached), free 3-parameter fitting is unreliable — L drifts to implausible values. Use fixed-L with domain-justified ceiling and fit only k and x0.

## Web Research Gaps Filled (2025 data only in catalog up to 2024)
- EVWire H1 2025 report: best source for H1 regional BEV unit volumes
- S&P Global Automotive: best for USA BEV market share percentages
- EVBoosters: China NEV/BEV split by H1 2025
- Visual Capitalist: country-level BEV market share rankings
