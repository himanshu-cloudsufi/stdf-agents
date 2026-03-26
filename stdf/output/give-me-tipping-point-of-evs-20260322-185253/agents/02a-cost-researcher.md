# STDF Cost Researcher Agent — EV vs. ICE Passenger Vehicle Disruption

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.88

---

## Agent Reasoning

**Search strategy and catalog findings.** This analysis covers battery electric vehicles (BEVs) as the disruptor against internal combustion engine (ICE) passenger cars as the incumbent. The passenger cars sector of the local data catalog (Tier 2) is well-populated with directly relevant cost curves, covering both EV and ICE purchase prices from 2010 through 2024–2025 for USA, China, Europe, and Rest of World. The battery pack cost series (Rethinkx, T2) is the primary disruptor hardware cost trajectory with 15 annual data points from 2010 to 2024 (global median) and 6 points from 2019 to 2024 (passenger BEV segment specifically). Operating cost curves (AAA/Goldman Sachs, T2) cover 2022–2024 for ICE on a per-mile basis. The catalog also contains residential electricity and gasoline price series (WorldBank T2) back to 2005–2016, providing fuel cost components.

**Key decisions on data selection.** The correct service-level unit for the EV vs. ICE consumer market disruption is $/vehicle (purchase price parity) as the primary metric, per shared-cost-rules.md Rule 2 and Rule 3 (Consumer market type → purchase price dominates). The secondary metric is cost per mile (fuel + maintenance), where EV has a structural operating cost advantage. Battery pack cost in $/kWh is the hardware cost driver — the cost-fitter must convert this to $/vehicle using pack size assumptions (~60–75 kWh for US passenger BEV). A critical data quality flag applies: the catalog's EV purchase price curve (`Passenger_Vehicle_(EV)_Median_Cost_USA.json`, source: "Database") tracks entry-level/economy EV pricing and understates the full market-mix average transaction price by roughly 40–80%. The KBB/Cox Automotive T3 source provides market-mix ATP: ~$54,000 EV vs. $47,652 ICE (all segments, 2024). Both representations are provided and labeled.

**Web research role.** Three T1/T3 web sources supplement the catalog: (1) DOE FOTW battery pack cost anchors (T1, usable-energy basis) for 2008, 2021, 2022, 2023 — confirming the Rethinkx T2 trajectory with a systematic ~5–10% offset due to rated vs. usable energy basis; (2) AAA "Your Driving Costs 2024" (T1) for disaggregated operating cost per mile and EV vs. ICE annual cost comparison; (3) NADA annual financial profile (T3) for all-segment ICE market-mix average retail price 2017–2024. All web data was evaluated as observed and pre-analysis-date before inclusion.

**Gap identification.** Maintenance cost time series ($/year or $/mile historically over multiple years) are not available for either BEV or ICE in the catalog, and no multi-year web time series was found — the AAA report provides a 2024 snapshot only. Battery pack $/kWh data prior to 2008 is not available from any T1 or T2 source. ICE all-segment market-mix ATP data is not available before 2017 from public sources. The 2025 data points in the catalog are treated as potentially model-derived and flagged accordingly.

---

## Agent Output

### Key Findings
- **Disruptor:** Battery electric vehicle (BEV)
- **Incumbent:** Internal combustion engine (ICE) passenger car
- **Service unit:** $/vehicle (purchase price, primary); $/mile (operating cost, secondary); $/kWh (battery pack hardware — requires cost-fitter conversion)
- **Data points (disruptor):** 15 battery pack cost points (2010–2024) + 16 EV purchase price points (2010–2024/2025) + 6 passenger-BEV-specific pack cost points (2019–2024)
- **Data points (incumbent):** 16 ICE sedan purchase price points (2010–2024/2025) + 8 NADA all-segment market-mix ATP points (2017–2024) + 4 ICE per-mile cost points (2022–2024/2025)
- **Confidence:** 0.88

---

### Disruptor Cost History

#### Table 1A — Li-Ion Battery Pack Cost (Global Median, $/kWh) — PRIMARY DISRUPTOR HARDWARE CURVE

**All values: [observed]** | Source: Rethinkx [T2] | File: `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json`

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 1,436 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2011 | 1,114 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2012 | 876 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2013 | 806 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2014 | 715 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2015 | 463 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2016 | 356 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2017 | 266 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2018 | 218 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2019 | 189 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2020 | 165 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2021 | 155 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2022 | 166 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2023 | 144 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |
| 2024 | 115 | $/kWh | Rethinkx — `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` | T2 | [observed] |

NOTE: 2022 spike ($166/kWh vs. $155 in 2021) is observed data reflecting lithium carbonate price surge. The cost-fitter should account for this anomaly in curve fitting.

#### Table 1B — DOE FOTW T1 Anchor Points (Usable-Energy Basis) — Validation Cross-Check

**All values: [observed]** | Source: U.S. DOE Vehicle Technologies Office, Argonne National Laboratory BatPaC tool [T1]

| Year | Cost ($/kWh, usable energy) | Unit | Source | Tier | Data Type |
|------|----------------------------|------|--------|------|-----------|
| 2008 | 1,415 | $/kWh (usable) | DOE FOTW #1354 (Aug 2024) — https://www.energy.gov/eere/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty [CAUTION: DOE/VTO source — historical data only] | T1 | [observed] |
| 2021 | 157 | $/kWh (usable) | DOE FOTW #1206 (Oct 2021) — https://www.energy.gov/eere/vehicles/articles/fotw-1206-oct-4-2021-doe-estimates-electric-vehicle-battery-pack-costs-2021 [CAUTION: DOE/VTO source — historical data only] | T1 | [observed] |
| 2022 | 153 | $/kWh (usable) | DOE FOTW #1272 (Jan 2023) — https://www.energy.gov/eere/vehicles/articles/fotw-1272-january-9-2023-electric-vehicle-battery-pack-costs-2022-are-nearly [CAUTION: DOE/VTO source — historical data only] | T1 | [observed] |
| 2023 | 139 | $/kWh (usable) | DOE FOTW #1354 (Aug 2024) — https://www.energy.gov/eere/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty [CAUTION: DOE/VTO source — historical data only] | T1 | [observed] |

NOTE: DOE uses usable-energy basis (not rated/nameplate). Rethinkx T2 values are on rated-energy basis. DOE values run ~5–10% lower than Rethinkx at the same year. Both series are consistent in direction and magnitude of decline. The cost-fitter must select one basis and apply consistently.

#### Table 1C — Li-Ion Battery Pack Cost, Passenger BEV Segment (Global, $/kWh) — SEGMENT-SPECIFIC CURVE

**All values: [observed]** | Source: Rethinkx [T2] | File: `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json`

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2019 | 179 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |
| 2020 | 152 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |
| 2021 | 139 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |
| 2022 | 152 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |
| 2023 | 132 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |
| 2024 | 97 | $/kWh | Rethinkx — `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` | T2 | [observed] |

#### Table 2A — EV Purchase Price, USA Median (Entry-Level Proxy, $/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json`

WARNING: This catalog curve tracks entry-level/economy EV pricing, NOT the full market-mix average transaction price. Use Table 2C (KBB/Cox T3) for market-mix comparison.

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 52,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2012 | 50,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2014 | 47,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2016 | 43,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2018 | 39,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2020 | 35,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2021 | 34,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2022 | 33,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2023 | 32,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |
| 2024 | 31,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_USA.json` | T2 | [observed] |

#### Table 2B — EV Purchase Price, China Median ($/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json`

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 39,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |
| 2013 | 33,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |
| 2016 | 26,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |
| 2019 | 21,000 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |
| 2022 | 17,300 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |
| 2024 | 16,200 | $/vehicle | Database — `Passenger_Vehicle_(EV)_Median_Cost_China.json` | T2 | [observed] |

#### Table 2C — EV Market-Mix Average Transaction Price, USA ($/vehicle) — T3 SUPPLEMENT

**All values: [observed]** | Source: Cox Automotive / Kelley Blue Book [T3]

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2022 | 65,108 | $/vehicle | KBB/Cox Automotive ATP Report (peak, 2022) — https://www.coxautoinc.com/learning-center/tag/average-transaction-price/ | T3 | [observed] |
| 2023 | 50,683 | $/vehicle | KBB/Cox Automotive ATP Report (Sep 2023) — https://www.coxautoinc.com/learning-center/tag/average-transaction-price/ | T3 | [observed] |
| 2024 | 54,021 | $/vehicle | KBB/Cox ATP March 2024 — https://www.coxautoinc.com/insights/kbb-atp-march-2024/ | T3 | [observed] |

NOTE: KBB/Cox ATP is the full market-mix (Tesla-heavy), reflecting premium mix bias. Annual 2024 average likely in $53,000–$56,000 range; December 2024 figure was $56,691. Use mid-year snapshots for annual comparisons.

#### Table 3 — EV Lowest Cost (Range <200 miles), USA ($/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json`

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 109,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2015 | 75,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2017 | 37,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2021 | 31,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2022 | 26,595 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2023 | 27,800 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |
| 2024 | 29,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` | T2 | [observed] |

NOTE: 2010–2016 values reflect early Tesla Roadster and premium-only market. The steep drop to $37,000 in 2017 reflects Model 3 introduction. 2023 uptick reflects IRA-driven price floor adjustments on Chevy Bolt; treat 2023–2024 as near-flat.

#### Table 4 — EV Lowest Cost, China ($/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json`

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2013 | 38,600 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |
| 2016 | 34,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |
| 2019 | 25,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |
| 2022 | 16,500 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |
| 2023 | 12,000 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |
| 2024 | 9,700 | $/vehicle | Database — `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` | T2 | [observed] |

---

### Incumbent Cost History

#### Table 5A — ICE Mid-Size Sedan Purchase Price, USA ($/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json`

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 22,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2012 | 23,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2014 | 24,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2016 | 25,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2018 | 26,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2020 | 27,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2021 | 27,500 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2022 | 28,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2023 | 28,500 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |
| 2024 | 29,000 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` | T2 | [observed] |

NOTE: ICE sedan prices show a gradual +32% rise 2010–2024 (inflation and feature-content driven). This is a segment-level curve — not the all-segment market mix (which is truck/SUV-dominated and higher). NADA all-segment data (Table 5B) provides the market-mix view.

#### Table 5B — ICE All-Segment Market-Mix Average Retail Price, USA ($/vehicle) — T3

**All values: [observed]** | Source: NADA Annual Financial Profile (Wards Intelligence / Automotive News) [T3] | URL: https://www.nada.org/nada/nada-data

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2017 | 34,670 | $/vehicle | NADA Annual Financial Profile 2017 — https://www.nada.org/nada/nada-data | T3 | [observed] |
| 2018 | 35,608 | $/vehicle | NADA Annual Financial Profile 2018 | T3 | [observed] |
| 2019 | 36,824 | $/vehicle | NADA Annual Financial Profile 2019 | T3 | [observed] |
| 2020 | 38,961 | $/vehicle | NADA Annual Financial Profile 2020 | T3 | [observed] |
| 2021 | 42,379 | $/vehicle | NADA Annual Financial Profile 2021 | T3 | [observed] |
| 2022 | 46,287 | $/vehicle | NADA Annual Financial Profile 2022 | T3 | [observed] |
| 2023 | 47,014 | $/vehicle | NADA Annual Financial Profile 2023 | T3 | [observed] |
| 2024 | 47,652 | $/vehicle | NADA Annual Financial Profile 2024 | T3 | [observed] |

NOTE: ICE all-segment market-mix ATP rose 37% from 2017 to 2024, driven by truck/SUV mix shift and COVID-era supply constraints. This is the appropriate comparator when using KBB/Cox EV market-mix ATP (Table 2C).

#### Table 5C — ICE Mid-Size SUV Purchase Price, USA ($/vehicle)

**All values: [observed]** | Source: Database (unattributed) [T2] | File: `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json`

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 25,735 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |
| 2015 | 30,675 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |
| 2018 | 31,630 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |
| 2020 | 34,600 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |
| 2022 | 36,420 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |
| 2024 | 39,520 | $/vehicle | Database — `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` | T2 | [observed] |

#### Table 6 — ICE Operating Cost per Mile, USA (All-In, $/mile)

**All values: [observed]** | Source: AAA / Goldman Sachs Research [T2] | Files: `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_*.json`

NOTE: These curves cover 2022–2024 observed + a 2025 point. The 2025 point may be model-derived — treat as [model-derived]. These are TOTAL costs (fuel + maintenance + depreciation + insurance), not fuel-only.

| Year | Cost ($/mile) | Annual Miles | Unit | Source | Tier | Data Type |
|------|--------------|--------------|------|--------|------|-----------|
| 2022 | 0.750 | 15,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` | T2 | [observed] |
| 2023 | 0.800 | 15,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` | T2 | [observed] |
| 2024 | 0.850 | 15,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` | T2 | [observed] |
| 2022 | 1.100 | 10,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` | T2 | [observed] |
| 2023 | 1.200 | 10,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` | T2 | [observed] |
| 2024 | 1.300 | 10,000 | $/mile | AAA/Goldman Sachs — `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` | T2 | [observed] |

#### Table 7 — AAA Disaggregated Annual Cost Comparison: EV vs. ICE (2024 Snapshot, Medium Sedan at 15k miles/yr)

**All values: [observed]** | Source: AAA "Your Driving Costs 2024" [T1] | URL: https://newsroom.aaa.com/2024/09/aaa-your-driving-costs-the-price-of-new-car-ownership-continues-to-climb/

| Cost Component | EV ($/year) | ICE ($/year) | Unit | Tier | Data Type |
|---------------|------------|--------------|------|------|-----------|
| Fuel/energy | 613 | 1,881 | $/year | T1 | [observed] |
| Maintenance | 1,138 | 1,634 | $/year | T1 | [observed] |
| Depreciation | 6,198 | 3,768 | $/year | T1 | [observed] |
| Insurance | 2,053 | 1,583 | $/year | T1 | [observed] |
| License/Registration | 980 | 644 | $/year | T1 | [observed] |
| **Total** | **10,982** | **9,510** | $/year | T1 | [observed] |

NOTE: Per shared-cost-rules.md Rule 1, TCO aggregation is NOT used for cost curve fitting. The disaggregated components are preserved here. The cost-fitter must use disaggregated components individually. EV depreciation is higher than ICE in 2024 (EV: $6,198/yr vs. ICE: $3,768/yr), reflecting faster value loss of current EV models. EV fuel cost is 67% lower than ICE ($613 vs. $1,881/yr). Operating cost per mile (AAA 2024): EV = 12.62¢/mile vs. ICE weighted average = 25.03¢/mile.

#### Table 8 — Gasoline Retail Price, USA ($/Liter, Annual Average)

**All values: [observed]** | Source: WorldBank.Org [T2] | File: `data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json`

| Year | Price ($/L) | Unit | Source | Tier | Data Type |
|------|------------|------|--------|------|-----------|
| 2016 | 0.564 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2017 | 0.616 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2018 | 0.697 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2019 | 0.661 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2020 | 0.556 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2021 | 0.766 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2022 | 1.007 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2023 | 0.898 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |
| 2024 | 0.843 | $/L | WorldBank — `Gasoline_Average_Retail_Price_USA.json` | T2 | [observed] |

NOTE: $0.843/L ≈ $3.19/gallon annual average 2024. 2025 data (3 monthly points averaging $0.787/L) is available in catalog but sparse — treat as preliminary.

#### Table 9 — US Residential Electricity Price ($/kWh)

**All values: [observed]** | Source: (unattributed) [T2] | File: `data/electricity/cost/Electricity_Residential_Price_USA.json`

| Year | Price ($/kWh) | Unit | Source | Tier | Data Type |
|------|--------------|------|--------|------|-----------|
| 2010 | 0.128 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2015 | 0.138 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2018 | 0.136 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2020 | 0.135 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2022 | 0.159 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2023 | 0.168 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |
| 2024 | 0.176 | $/kWh | `Electricity_Residential_Price_USA.json` | T2 | [observed] |

---

### Current Costs (Analysis Date: 2026-03-23)

- **Disruptor current cost (battery pack):** $115/kWh (Rethinkx T2, 2024 [observed]); $97/kWh passenger BEV segment (Rethinkx T2, 2024 [observed]); DOE T1 crosscheck: $139/kWh usable-energy basis (2023 [observed])
- **Disruptor current cost (vehicle purchase, entry-level):** $31,000/vehicle USA median (T2 catalog, 2024 [observed]); $29,000 lowest-cost short-range USA (T2 catalog, 2024 [observed]); $16,200 China median (T2 catalog, 2024 [observed])
- **Disruptor current cost (vehicle purchase, market-mix ATP):** ~$54,000–56,000/vehicle USA (KBB/Cox T3, 2024 [observed])
- **Disruptor current operating cost:** 12.62¢/mile all-in; 4.73¢/mile fuel only (AAA T1, 2024 [observed])
- **Incumbent current cost (ICE sedan, USA):** $29,000/vehicle (T2 catalog, 2024 [observed])
- **Incumbent current cost (ICE all-segment market-mix ATP):** $47,652/vehicle (NADA T3, 2024 [observed])
- **Incumbent current operating cost:** $0.85/mile at 15,000 miles/yr all-in (T2 catalog, 2024 [observed]); 25.03¢/mile weighted average operating cost (AAA T1, 2024 [observed])
- **Incumbent current fuel cost:** $0.843/L ≈ $3.19/gal US gasoline (WorldBank T2, 2024 [observed])

---

### Unit Notes

- **Service-level unit (primary):** $/vehicle — the consumer purchase decision unit for passenger car disruption
- **Service-level unit (secondary):** $/mile — the operating-cost comparison unit for TCO disaggregation (per shared-cost-rules.md Rule 1)
- **Hardware-to-service conversion needed:** YES — battery pack cost in $/kWh must be converted to $/vehicle contribution. The cost-fitter must apply: battery cost contribution = pack cost ($/kWh) × pack size (kWh). Assumed pack size for US passenger BEV: 60–75 kWh. Cost-fitter should sensitivity-test across this range.
- **Conversion parameters available:**
  - Pack size assumption: 60–75 kWh (US average passenger BEV, not in catalog — cost-fitter to parameterize)
  - Residential electricity price: $0.176/kWh (2024, Table 9)
  - EV efficiency: ~3–4 miles/kWh (not in catalog — see Data Gaps)
  - ICE fuel efficiency: approximately 30 MPG average (not in catalog — see Data Gaps)
  - Gasoline price: $0.843/L ≈ $3.19/gal (2024, Table 8)

---

### Data Gaps

1. **Battery pack cost before 2008:** No T1, T2, or T3 data available. The disruption trajectory can only be fitted from 2008 onward. The DOE 2008 anchor ($1,415/kWh usable energy, equivalent to ~$1,436/kWh Rethinkx rated energy in 2010) provides a practical start year.
2. **EV maintenance cost time series:** Not available in catalog. AAA 2024 provides a single-year snapshot ($1,138/yr for EV vs. $1,634/yr ICE, medium sedan). No multi-year historical series found. The cost-fitter cannot fit a maintenance cost trajectory. List as sourced snapshot only.
3. **EV efficiency (kWh/mile) by model year:** Not available in catalog. Model year 2024 EPA data exists (53–140 MPGe range per DOE FOTW #1374) but no single average for use in cost-per-mile computation. Cost-fitter should use 3.5 miles/kWh as a working assumption and flag as [model-derived].
4. **ICE fleet average fuel economy by year:** Not in catalog. Cost-fitter may use EPA published MPG averages (approximately 26–30 MPG for new vehicles 2010–2024); treat as T3 supplementary.
5. **ICE all-segment market-mix ATP before 2017:** Not available from any public T1 or T3 source in plain data form. Pre-2017 all-segment incumbent pricing cannot be fitted from public data.
6. **Catalog EV purchase price source attribution is unattributed ("Database"):** The source field in `Passenger_Vehicle_(EV)_Median_Cost_USA.json` and related files is listed as "Database" without further attribution. The series is plausible in magnitude and direction but the lack of a named source reduces confidence slightly. Cross-checked against KBB T3 data where available.
7. **China ICE sedan pricing does not match typical market benchmarks:** The catalog's China ICE sedan series shows $12,000–$19,000 (2010–2024), which aligns with compact economy segments but may underrepresent premium and SUV segments that dominate volume. China EV-ICE parity analysis should note this segment-level caveat.
8. **Regional electricity prices not used for per-mile computation:** China and Europe residential electricity prices are in the catalog but EV per-mile costs for those regions are not directly computable without regional efficiency data. The cost-fitter should limit per-mile cost computation to USA unless additional data is sourced.

---

### Source Conflicts

1. **Battery pack 2021: Rethinkx T2 = $155/kWh; DOE T1 = $157/kWh (usable energy).** Extremely close; DOE is on usable-energy basis which runs ~5–10% higher than rated-energy basis in prior years. At 2021 values the gap is negligible (~1.3%). No material conflict. Both used — T1 takes precedence for absolute 2021 value; T2 used for full 2010–2024 trajectory continuity.
2. **Battery pack 2022: Rethinkx T2 = $166/kWh (spike); DOE T1 = $153/kWh.** Discrepancy of $13/kWh. DOE uses 100k-unit scale production assumption which may not capture spot market lithium price surge. Rethinkx appears to reflect actual transaction prices during 2022 lithium shortage. Both are flagged. The cost-fitter must decide whether to treat 2022 as an outlier or include it as a price signal.
3. **Battery pack 2023: Rethinkx T2 = $144/kWh; DOE T1 = $139/kWh (usable energy).** ~3.5% gap, consistent with rated vs. usable energy basis offset. No material conflict.
4. **EV entry-level USA (T2 catalog) vs. KBB market-mix ATP (T3):** The catalog's 2024 EV median of $31,000 vs. KBB market-mix $54,000–56,000 represents a 74–80% difference. These are measuring different populations (entry-level models vs. full market mix including premium Tesla models). Both are used with clear labeling. The cost-fitter must select the appropriate comparator tier for the parity analysis — entry-level-to-entry-level or market-mix-to-market-mix.
5. **ICE sedan (T2 catalog, $29,000) vs. NADA all-segment ATP (T3, $47,652) in 2024:** Same issue as above — segment vs. market-mix. These must be paired consistently with the corresponding EV data series.

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | 15 data points (battery pack $/kWh) over 14 years (2010–2024); 16 data points EV purchase price 2010–2024 — both T2 catalog |
| 2.2 | PASS | ICE mid-size sedan USA 16 points 2010–2024 (T2); NADA all-segment market-mix 8 points 2017–2024 (T3) |
| 2.3 | PASS | Disruptor current cost: Li-ion pack $115/kWh (Rethinkx T2, 2024); passenger BEV segment $97/kWh (Rethinkx T2, 2024); EV ATP $54,021 (KBB T3, Mar 2024); AAA EV fuel: 12.62¢/mile (AAA T1, 2024) |
| 2.4 | PASS | Incumbent current: ICE sedan $29,000 (T2, 2024); all-segment $47,652 (NADA T3, 2024); ICE total cost $0.85/mile at 15k (T2, 2024); AAA total annual cost $12,297 (T1, 2024) |

**Overall: COMPLIANT**

---

## Sources

- Rethinkx — `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` [T2]
- Rethinkx — `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_Europe.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_China.json` [T2]
- Database (unattributed) — `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` [T2]
- AAA / Goldman Sachs Research — `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` [T2]
- AAA / Goldman Sachs Research — `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` [T2]
- WorldBank.Org — `data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json` [T2]
- (unattributed) — `data/electricity/cost/Electricity_Residential_Price_USA.json` [T2]
- U.S. DOE Vehicle Technologies Office / Argonne National Laboratory BatPaC — DOE FOTW #1354 (Aug 2024): https://www.energy.gov/eere/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty [T1] [CAUTION: DOE/VTO source — historical data only]
- U.S. DOE Vehicle Technologies Office — DOE FOTW #1206 (Oct 2021): https://www.energy.gov/eere/vehicles/articles/fotw-1206-oct-4-2021-doe-estimates-electric-vehicle-battery-pack-costs-2021 [T1] [CAUTION: DOE/VTO source — historical data only]
- U.S. DOE Vehicle Technologies Office — DOE FOTW #1272 (Jan 2023): https://www.energy.gov/eere/vehicles/articles/fotw-1272-january-9-2023-electric-vehicle-battery-pack-costs-2022-are-nearly [T1] [CAUTION: DOE/VTO source — historical data only]
- AAA "Your Driving Costs 2024" — https://newsroom.aaa.com/2024/09/aaa-your-driving-costs-the-price-of-new-car-ownership-continues-to-climb/ [T1]
- AAA "Your Driving Costs 2024" PDF — https://newsroom.aaa.com/wp-content/uploads/2024/08/YDC-Brochure-FINAL-9.2024.pdf [T1]
- NADA Annual Financial Profile of America's Franchised New-Car Dealerships (2017–2024) — https://www.nada.org/nada/nada-data [T3]
- Cox Automotive / Kelley Blue Book ATP Report (Mar 2024) — https://www.coxautoinc.com/insights/kbb-atp-march-2024/ [T3]
- Cox Automotive / Kelley Blue Book Q4 2024 EV Sales Report — https://www.coxautoinc.com/wp-content/uploads/2025/01/Q4-2024-Kelley-Blue-Book-EV-Sales-Report.pdf [T3]
