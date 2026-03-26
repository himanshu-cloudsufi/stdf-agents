---
name: oil-gas multi-vector regional adoption data
description: Regional adoption data and S-curve fits for the oil/gas demand disruption analysis (V1 EV, V2 solar PV, V3 heat pump) -- 4 regions per vector, 2024 data
type: project
---

Three-vector regional disruption analysis for oil/gas demand. Key findings:

**V1 EV (new car sales share, 2024):**
- China: 47.36% (catalog) vs 40.9% (CPCA broader base) -- rapid_growth; x0=2023.7
- Europe: 26.91% -- rapid_growth; x0=2025.9 (2.2 yrs behind China)
- USA: 11.59% -- tipping; x0=2029.2 (5.6 yrs behind China)
- Rest of World: 6.13% -- tipping; x0=2029.6

All fixed L=90 for consistency with global V1 ceiling. Europe R-squared=0.9207 (flagged, below 0.95 threshold) due to German incentive withdrawal kink in 2022-2024 data.

**V2 Solar generation share (2024):**
- Europe: 10.48% (confirmed by Ember EER 2025: 11%) -- tipping; x0=2030.5 (current leader)
- China: 9.03% -- tipping; x0=2029.5 (China overtakes Europe ~2027 due to steeper k=0.2649 vs Europe k=0.1852)
- USA: 6.07% -- tipping; x0=2033.0
- Rest of World: 5.90% -- tipping; x0=2032.2

All in tipping phase. All fixed L=45 consistent with global ceiling. V2 divergence is in growth rate, not phase.

**V3 Heat pump:**
- Europe: 24% new installs (EHPA) -- rapid_growth; x0=2028.9; only region with S-curve fit
- China: ~12% (T3 estimate, ±5pp) -- tipping; 4-6 yr lag; note China displaces coal-district-heating not gas boilers
- USA: ~10% (AHRI, heating/cooling installed base) -- tipping; 5-7 yr lag

**BESS regional (2024 cumulative MWh):**
- China: 167,401 MWh (45.2% global, +145% YoY)
- USA: 85,456 MWh (23.1% global, +67.6% YoY)
- Europe: 53,863 MWh (14.6% global, +62.2% YoY)
- Global: 370,112 MWh

**China denominator issue:** Rethinkx catalog uses passenger-car-only denominator (23.86M), CPCA uses broader vehicle base (27-31M). This produces 47.36% vs 40.9% -- both rapid_growth, but note when fitting global-consistent S-curves use catalog basis.

**Why:** Oil/gas disruption analysis pipeline run requiring multi-vector regional breakdown.
**How to apply:** For future oil/gas or energy disruption analyses, use these 2024 baseline figures as starting points and update when new annual data is available.
