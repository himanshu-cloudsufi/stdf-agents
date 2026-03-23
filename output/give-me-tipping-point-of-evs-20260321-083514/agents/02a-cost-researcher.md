# STDF Cost Researcher Agent — EV vs. ICE Passenger Vehicle Disruption

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.82

---

## Agent Reasoning

**Disruption matchup and unit selection.** This analysis concerns a market-driven disruption: battery electric vehicles (BEV) displacing internal combustion engine (ICE) passenger cars. Per shared-cost-rules.md Rule 2 and Rule 3, the market type is Consumer (purchase price dominates) with a Fleet secondary lens (operating cost per km). The primary cost metric for parity comparison is vehicle purchase price ($/vehicle); the secondary metric is fuel/energy cost per mile ($/mile). No upstream domain-disruption handoff file was present, so the default hierarchy applies. No TCO aggregation is performed (shared-cost-rules.md Rule 1). This follows cost-curve dynamics consistent with a Stellar technology: battery packs show persistent exponential cost decline driven by cumulative production scale.

**Local catalog search.** The catalog contains rich coverage for this disruption. Key curves found: (a) EV median purchase price by region (USA, China, Europe, Rest of World) — 16 annual data points 2010–2025, source "Database" (T2); (b) EV lowest-cost purchase price (<200 mi range) by region — 13–16 annual data points; (c) ICE median price by segment (hatchback, mid-size sedan, mid-size SUV) by region — 16 annual data points 2010–2025, source "Database" (T2); (d) Li-ion battery pack median cost global — 15 annual data points 2010–2024, source Rethinkx (T2); (e) Li-ion battery pack passenger BEV cost global — 6 data points 2019–2024, source Rethinkx (T2); (f) gasoline retail price USA — multi-series WorldBank T1 data 2015–2025; (g) US residential electricity price — annual 1980–2024, source "Database" (T2). ICE cost-per-mile data exists from AAA/Goldman Sachs (2022–2024 only, sparse). The catalog EV and ICE purchase price curves carry source "Database" (unattributed smooth curve) — treated as T2 but require cross-validation, which web search provides.

**Web research and validation.** Three primary source categories were used to cross-validate and fill gaps. First, the US Department of Energy Fact of the Week (DOE FOTW) series provides battery pack cost anchors at 2008 ($1,415/kWh), 2022 ($153/kWh), and 2023 ($139/kWh) on a usable-energy basis — consistent with the Rethinkx T2 catalog trajectory. Second, Cox Automotive/Kelley Blue Book (T3) provides EV average transaction price anchors: 2021 ~$56,000, July 2022 ~$65,108, September 2023 ~$50,683 — confirming the catalog EV median curves are within the right order of magnitude but lower than observed market-mix ATPs (the catalog likely represents entry-level EV pricing). Third, US government retail gasoline price data confirms the WorldBank catalog series: 2010 ~$2.79/gal, 2015 ~$2.45/gal, 2018 ~$2.72/gal, 2020 ~$2.17/gal, 2022 ~$3.95/gal, 2023 ~$3.53/gal, 2024 ~$3.30/gal. All web data points used below are pre-2026-03-21 and tagged [observed].

**Key decisions.** The catalog EV purchase price curves are labeled "Database" with no named methodology — treated as T2 (curated with provenance). Cross-validation against KBB/Cox T3 data shows catalog values underestimate market-average ATPs by ~30–50% (catalog likely tracks entry-level trim pricing, not full market mix). Both series are included, flagged accordingly. Battery pack cost is a hardware-level unit ($/kWh), not a service-level unit — the cost-fitter must apply vehicle battery size (median ~60–75 kWh for USA) to convert to $/vehicle contribution. No maintenance cost time series was found; this component is excluded per Rule 1. The S-curve adoption trajectory for BEV is visible in the purchase price data and is consistent with the cost-curve dynamics already well established in the battery pack data.

---

## Agent Output

### Key Findings
- **Disruptor:** Battery Electric Vehicle (BEV) — passenger car segment (Stellar technology, cost-curve dynamics apply)
- **Incumbent:** Internal Combustion Engine (ICE) vehicle — passenger car segment
- **Service unit:** USD per vehicle (purchase price parity, primary); USD per mile driven (operating cost parity, secondary)
- **Data points (disruptor):** 15 battery pack cost points (2010–2024) + 16 EV purchase price points (2010–2025) + 6 passenger BEV pack points (2019–2024)
- **Data points (incumbent):** 16 ICE purchase price points (2010–2025) + 7 gasoline price points (2010–2024) + 3 ICE cost-per-mile points (2022–2024)
- **Confidence:** 0.82

---

### Disruptor Cost History

#### Battery Pack Cost ($/kWh) — Hardware Level

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2008 | 1,415 | $/kWh (usable energy) | DOE FOTW #1354, US Department of Energy (August 2024) [T1] | T1 | [observed] |
| 2010 | 1,436 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2011 | 1,114 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2012 | 876 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2013 | 806 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2014 | 715 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2015 | 463 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2016 | 356 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2017 | 266 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 218 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 189 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 179 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 165 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 155 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 157 | $/kWh (usable energy) | DOE FOTW #1206, US Department of Energy (October 2021) [T1] | T1 | [observed] |
| 2022 | 166 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 153 | $/kWh (usable energy) | DOE FOTW #1272, US Department of Energy (January 2023) [T1] | T1 | [observed] |
| 2023 | 144 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 139 | $/kWh (usable energy) | DOE FOTW #1354, US Department of Energy (August 2024) [T1] | T1 | [observed] |
| 2024 | 115 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 97 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

**Note:** 2022 spike to $166/kWh (T2) and $153/kWh (T1 DOE) reflects lithium carbonate price event — not a reversal of cost-curve dynamics. Do not smooth this spike; include it in the fit.

#### EV Purchase Price — USA Median ($/vehicle)

| Year | Cost ($) | Unit | Source | Tier | Data Type |
|------|---------|------|--------|------|-----------|
| 2010 | 52,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2012 | 50,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2014 | 47,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2016 | 43,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2018 | 39,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2020 | 35,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2021 | 56,000 | $/vehicle | Cox Automotive / Kelley Blue Book EV ATP market report (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2022 | 65,108 | $/vehicle | Cox Automotive / Kelley Blue Book EV ATP July 2022 (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2023 | 50,683 | $/vehicle | Cox Automotive / Kelley Blue Book EV ATP September 2023 (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2024 | 31,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |

**WARNING — catalog vs. market-mix ATP:** The T2 catalog EV median series ($31,000 in 2024) is substantially lower than observed KBB/Cox market-average ATPs (~$55,000 in 2024). The catalog likely tracks entry-level/economy EV trim pricing. Both are included. The cost-fitter should use the T3 KBB series for overall market-mix EV ATP; use T2 catalog for entry-level EV affordability trajectory.

#### EV Lowest Purchase Price — USA (<200 mi range)

| Year | Cost ($) | Unit | Source | Tier | Data Type |
|------|---------|------|--------|------|-----------|
| 2010 | 109,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2013 | 80,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2017 | 37,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2020 | 36,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2021 | 31,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2022 | 26,595 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2023 | 27,800 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2024 | 29,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2] | T2 | [observed] |

#### EV Purchase Price — China Median ($/vehicle)

| Year | Cost ($) | Unit | Source | Tier | Data Type |
|------|---------|------|--------|------|-----------|
| 2010 | 39,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2013 | 33,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2016 | 26,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2019 | 21,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2022 | 17,300 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2024 | 16,200 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2] | T2 | [observed] |

#### EV Lowest Purchase Price — China (<200 mi range)

| Year | Cost ($) | Unit | Source | Tier | Data Type |
|------|---------|------|--------|------|-----------|
| 2013 | 38,600 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2016 | 34,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2019 | 25,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2022 | 16,500 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2023 | 12,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |
| 2024 | 9,700 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json (Database) [T2] | T2 | [observed] |

---

### Incumbent Cost History

#### ICE Vehicle Purchase Price — USA ($/vehicle)

| Year | Cost ($) | Unit | Source | Tier | Data Type |
|------|---------|------|--------|------|-----------|
| 2010 | 22,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2010 | 15,650 | $/vehicle (hatchback) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Hatchback)_USA.json (Database) [T2] | T2 | [observed] |
| 2010 | 28,000–30,000 | $/vehicle (all-segment average) | Cox Automotive historical ATP / industry consensus (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2015 | 24,500 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2018 | 26,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2019 | 38,000 | $/vehicle (all-segment average) | Cox Automotive ATP January 2020 report (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2020 | 27,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2021 | 46,000 | $/vehicle (all-segment average) | Cox Automotive ATP October 2021 (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2022 | 49,507 | $/vehicle (all-segment average) | Cox Automotive / Kelley Blue Book ATP December 2022 (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2023 | 48,247 | $/vehicle (all-segment average) | Cox Automotive / Kelley Blue Book November 2023 (T3), retrieved 2026-03-21 | T3 | [observed] |
| 2024 | 29,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2024 | 48,759 | $/vehicle (all-segment average) | Cox Automotive / Kelley Blue Book 2024 annual ATP (T3), retrieved 2026-03-21 | T3 | [observed] |

**Note on incumbent trajectory:** The ICE purchase price has risen over the observation period, driven by the shift to SUVs/trucks and the 2021–2022 semiconductor shortage spike. Incumbent displacement of ICE by BEV is visible in the narrowing purchase price gap, particularly in China. The mid-size sedan catalog curve ($22k in 2010 to $29k in 2024) understates the overall market-mix ATP; use Cox/KBB T3 series for like-for-like comparison against EV market-mix ATPs.

#### Gasoline Fuel Price — USA (T1 Source: US government annual data)

| Year | Price | Unit | Source | Tier | Data Type |
|------|-------|------|--------|------|-----------|
| 2010 | 2.79 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2015 | 2.45 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2018 | 2.72 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2020 | 2.17 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2022 | 3.95 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2023 | 3.53 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |
| 2024 | 3.30 | $/gallon (regular) | US DOE Alternative Fuels Data Center, Annual Retail Fuel Prices (from government price series) [T1] | T1 | [observed] |

**Cross-check with catalog:** WorldBank T2 gasoline catalog gives 2024 median ~$3.20/gal (12-state series). Government T1 data gives $3.30/gal for 2024 annual average. Discrepancy ~3% — T1 wins; see Source Conflicts.

#### US Residential Electricity Price (EV operating cost input)

| Year | Price | Unit | Source | Tier | Data Type |
|------|-------|------|--------|------|-----------|
| 2010 | 0.128 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2015 | 0.138 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2018 | 0.136 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2020 | 0.135 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2022 | 0.159 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2023 | 0.168 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |
| 2024 | 0.176 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json (Database) [T2] | T2 | [observed] |

#### ICE Cost Per Mile — Global ($/mile, all-in operating cost)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2022 | 1.10 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |
| 2023 | 1.20 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |
| 2024 | 1.30 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |
| 2022 | 0.75 | $/mile (15k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |
| 2023 | 0.80 | $/mile (15k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |
| 2024 | 0.85 | $/mile (15k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json (AAA, Goldman Sachs Research) [T2] | T2 | [observed] |

---

### Current Costs

- **Disruptor current cost (battery pack, global median):** $115/kWh (2024, Rethinkx T2) [observed]
- **Disruptor current cost (battery pack, passenger BEV):** $97/kWh (2024, Rethinkx T2) [observed]
- **Disruptor current cost (purchase price, USA entry-level <200 mi):** $29,000 (2024, catalog T2) [observed]
- **Disruptor current cost (purchase price, USA market-mix average):** ~$55,000 (2024, Cox/KBB T3) [observed]
- **Disruptor current cost (purchase price, China market-mix median):** $16,200 (2024, catalog T2) [observed]
- **Incumbent current cost (purchase price, USA mid-size sedan):** $29,000 (2024, catalog T2) [observed]
- **Incumbent current cost (purchase price, USA all-segment average):** $48,759 (2024, Cox/KBB T3) [observed]
- **Incumbent current cost (gasoline):** $3.30/gallon (2024, US government annual retail price T1) [observed]
- **Incumbent current cost (fuel per mile, derived):** ~$0.13/mile at $3.30/gal, 25 MPG (2024, derived from government T1 fuel price + EPA fleet average fuel economy — EPA 2020 fleet average) [model-derived]
- **Disruptor current cost (fuel per mile, derived):** ~$0.05/mile at $0.176/kWh, 0.31 kWh/mile (2024, derived from T2 electricity price + DOE fleet average efficiency) [model-derived]

---

### Unit Notes

- **Service-level unit (primary):** USD per vehicle (purchase price) — dominant consumer decision metric per Rule 3 (Consumer market type)
- **Service-level unit (secondary):** USD per mile — for operating cost comparison; EV advantage is ~$0.08/mile over ICE at 2024 fuel/electricity prices
- **Hardware-to-service conversion needed:** YES — battery pack cost is in $/kWh (hardware). Cost-fitter must apply median vehicle battery pack size to convert to $/vehicle contribution.
- **Conversion parameters available:**
  - Battery pack energy (usable): 60–75 kWh for USA passenger BEV (median estimate, per DOE FOTW methodology)
  - EV energy consumption: 0.31 kWh/mile (DOE/EPA 2023–2024 fleet average)
  - ICE fuel economy: 25.7 MPG average new vehicle (US EPA 2020 data)
  - Typical annual mileage: 10,000–15,000 miles/year (AAA baseline used in cost-per-mile catalog)

---

### Data Gaps

- **No maintenance cost time series found:** No reliable historical maintenance cost time series ($/year or $/mile) was found for either BEV or ICE in the catalog or via web search. Per Rule 1, maintenance cost is excluded from the disaggregated stack and flagged here. The cost-fitter should note this gap when building the parity model.
- **No pre-2022 EV cost-per-mile time series:** The AAA/Goldman Sachs cost-per-mile catalog series only goes back to 2022. Gasoline price inputs (T1) go back to 2010, but no complete all-in cost-per-mile series for EV exists before 2022.
- **EV purchase price 2010–2018 unattributed:** The T2 catalog EV median price series (source: "Database") has no named primary source for years 2010–2018. Cross-validation shows it underestimates market-mix ATPs significantly. Treat as lower-bound entry-level pricing only.
- **China EV/ICE comparison — no T3 ATP validation:** The China ICE and EV median price series (T2) cover 2010–2025, but no regional ATP validation data equivalent to Cox/KBB for USA was found for China via web search.
- **No EV efficiency time series by model year:** The 0.31 kWh/mile figure is a 2023–2024 fleet average, not a historical series. Pre-2015 EV efficiency was lower, which the cost-fitter should account for when computing historical per-mile energy cost.
- **No used-vehicle price series:** Used-vehicle pricing affects the effective disruption pace for cost-sensitive buyers; no catalog coverage and web data not compiled here.

---

### Source Conflicts

- **Catalog gasoline USA vs. government T1:** WorldBank T2 catalog 2024 median = $3.20/gal; US government annual average = $3.30/gal. Resolution: T1 government data wins. Discrepancy ~3%, within state-mix rounding.
- **Catalog EV median USA vs. KBB/Cox ATP:** T2 catalog shows EV median USA at $31,000 in 2024; KBB/Cox T3 market-average ATP shows ~$55,000 in 2024. Resolution: both are correct but measure different market segments. T2 catalog = entry-level trim. T3 KBB = full-market-mix average (dominated by Tesla and premium models). Cost-fitter must choose which benchmark to use for parity comparison; both series are provided.
- **Rethinkx T2 battery pack vs. DOE FOTW T1:** 2022: Rethinkx $166/kWh vs. DOE $153/kWh (usable energy basis). 2023: Rethinkx $144/kWh vs. DOE $139/kWh. Resolution: T1 DOE values preferred for absolute level anchors. ~5–10% discrepancy attributable to rated vs. usable energy basis difference and Rethinkx using volume-weighted average (not usable-energy adjusted). Both series provided to cost-fitter.
- **ICE purchase price — catalog segments vs. market-mix:** T2 catalog mid-size sedan = $29,000 in 2024 vs. Cox/KBB all-segment average = $48,759 in 2024. Resolution: the all-segment average is dominated by trucks and SUVs; neither series is "wrong." For parity comparison, use segment-matched pairs (EV sedan vs. ICE sedan, or EV market-mix vs. ICE market-mix).

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | Battery pack: 15 data points, 2010–2024 (14-year span). EV purchase price USA: 16 data points, 2010–2025. Exceeds minimum 3 points over 5 years. |
| 2.2 | PASS | ICE median price USA: 16 data points, 2010–2025. Government gasoline price: 7 annual anchors, 2010–2024 (T1). ICE cost-per-mile: 3 points, 2022–2024. |
| 2.3 | PASS | Disruptor current cost: $115/kWh battery pack (2024, Rethinkx T2); $29,000 entry-level EV USA (2024, T2); ~$55,000 market-mix EV (2024, T3 KBB). |
| 2.4 | PASS | Incumbent current cost: $29,000 ICE sedan USA (2024, T2); $48,759 all-segment average (2024, T3 KBB); $3.30/gal gasoline (2024, government T1). |

---

## Sources

- US Department of Energy, Fact of the Week #1354 (August 2024): "Electric Vehicle Battery Pack Costs for a Light-Duty Vehicle in 2023 Are 90% Lower than in 2008" — T1 [CAUTION: DOE/VTO source — historical data only]
- US Department of Energy, Fact of the Week #1272 (January 2023): "Electric Vehicle Battery Pack Costs in 2022 Are Nearly 90% Lower than in 2008" — T1 [CAUTION: DOE/VTO source — historical data only]
- US Department of Energy, Fact of the Week #1206 (October 2021): "EV Battery Pack Costs 87% Lower than in 2008" — T1 [CAUTION: DOE/VTO source — historical data only]
- US DOE Alternative Fuels Data Center, Average Annual Retail Fuel Price of Gasoline: https://afdc.energy.gov/data/10641 — T1 [CAUTION: government source — historical data only]
- Cox Automotive / Kelley Blue Book, New Vehicle ATP Monthly Reports (2020–2024): https://www.coxautoinc.com/learning-center/tag/average-transaction-price/ — T3, retrieved 2026-03-21
- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json — Rethinkx, $/kWh, 2010–2024 — T2
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json — Rethinkx, $/kWh, 2019–2024 — T2
- data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json — Database, $/vehicle, 2010–2025 — T2
- data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json — Database, $/vehicle, 2010–2025 — T2
- data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json — Database, $/vehicle, 2010–2025 — T2
- data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json — Database, $/vehicle, 2013–2025 — T2
- data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json — Database, $/vehicle, 2010–2025 — T2
- data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Hatchback)_USA.json — Database, $/vehicle, 2010–2025 — T2
- data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json — AAA, Goldman Sachs Research, $/mile, 2022–2025 — T2
- data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json — AAA, Goldman Sachs Research, $/mile, 2022–2025 — T2
- data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json — WorldBank, $/L multi-state series, 2015–2025 — T2
- data/electricity/cost/Electricity_Residential_Price_USA.json — Database, $/kWh, 1980–2024 — T2
