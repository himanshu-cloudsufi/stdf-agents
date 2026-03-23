# STDF Cost Researcher Agent — EV vs. ICE Passenger Vehicle Disruption

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.88

---

## Agent Reasoning

The disruption being analyzed is battery electric vehicles (BEVs) driving incumbent displacement of internal combustion engine (ICE) passenger cars — a market-driven disruption powered by cost-curve dynamics in the battery pack supply chain. This is a Stellar technology (zero marginal energy cost characteristic); Jevons Paradox does not apply. The service-level unit for this disruption is purchase price in $/vehicle for the consumer market (Market Type: Consumer), with operating cost presented as a disaggregated stack per cost-rules Rule 1. Battery pack cost in $/kWh is tracked separately as the primary hardware-level cost driver and must be converted to $/vehicle by the cost-fitter using pack size (~60–75 kWh for USA mid-range BEVs). S-curve adoption dynamics will govern the downstream disruption timing analysis once the cost-fitter establishes the parity crossover.

The local data catalog (T2) provided strong coverage: 15-point Li-ion battery pack global median series (2010–2024, Rethinkx), 6-point passenger BEV-specific pack cost series (2019–2024, Rethinkx), and 16-point EV/ICE purchase price series (2010–2025, Database). The catalog source labeled "Database" is unattributed and therefore classified T2. DOE Fact of the Week anchors (2008: $1,415/kWh; 2022: $153/kWh; 2023: $139/kWh — T1, usable-energy basis, Argonne BatPaC methodology) were layered in as T1 validation points. The battery pack series exhibits the clearest evidence of cost-curve dynamics: a ~92% cost reduction over 14 years (2010–2024), the foundational input for the tipping-point calculation.

For the incumbent (ICE), the catalog provides sedan median price series 2010–2024 (T2) and SUV series 2010–2024 (T2). These track segment-specific entry-level pricing, not the market-mix average transaction price (ATP). NADA annual data (T3, sourced from Wards Intelligence / Automotive News Data Center) fills the all-segment market-mix gap for 2017–2024 ($34,670–$47,652). Cox Automotive / Kelley Blue Book T3 data provides 2024 EV ATP ($55,544 in December 2024) and all-segment ATP ($49,740 December 2024). Pre-2017 market-mix ATP for all segments is not available from public T1/T3 sources — flagged as a data gap. The ICE incumbent shows a slow rising cost trend (not cost-curve dynamics), driven by vehicle weight gain, complexity increases, and inflation.

A critical unit conflict exists: catalog EV purchase prices track entry-level/economy segment vehicles only (2024: $31,000 USA), while KBB/Cox ATP reflects the market-mix inclusive of stellar energy-adjacent premium models such as Tesla (2024: ~$55,000). Both are included in the output with explicit labeling so the cost-fitter can select the appropriate series for the parity computation. The 2025 data points in the catalog are excluded from tables because they extend beyond the analysis date (2026-03-21) as the last reliable observed points — the 2025 entries are treated as preliminary observed data only through end-2024 (the 2025 field in the catalog may represent model-derived projection). Only data through year 2024 is used in the historical tables.

---

## Agent Output

### Key Findings
- **Disruptor:** Battery electric vehicle (BEV) passenger car
- **Incumbent:** Internal combustion engine (ICE) passenger car
- **Service unit:** $/vehicle (purchase price); $/kWh (battery pack hardware — requires cost-fitter conversion)
- **Data points (disruptor):** 15 battery pack points (2010–2024) + 15 EV purchase price points (2010–2024) + 6 BEV-specific pack points (2019–2024)
- **Data points (incumbent):** 15 ICE sedan price points (2010–2024) + 8 NADA market-mix points (2017–2024) + 15 ICE SUV points (2010–2024)
- **Confidence:** 0.88

---

### Disruptor Cost History — Battery Pack ($/kWh, Hardware Level)

**All values: [observed]** (T2 Rethinkx catalog 2010–2024; T1 DOE anchors noted separately)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2008 | 1,415 | $/kWh (usable energy) | DOE FOTW #1354, Argonne/National Academies [CAUTION: DOE source — historical data only] | T1 | [observed] |
| 2010 | 1,436 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2011 | 1,114 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2012 | 876 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2013 | 806 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2014 | 715 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2015 | 463 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2016 | 356 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2017 | 266 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2018 | 218 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2019 | 189 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2020 | 165 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2021 | 155 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2022 | 166 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2022 | 153 | $/kWh (usable energy) | DOE FOTW #1272, Argonne BatPaC [CAUTION: DOE source — historical data only] | T1 | [observed] |
| 2023 | 144 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2023 | 139 | $/kWh (usable energy) | DOE FOTW #1354, Argonne BatPaC [CAUTION: DOE source — historical data only] | T1 | [observed] |
| 2024 | 115 | $/kWh (rated) | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |

---

### Disruptor Cost History — Passenger BEV-Specific Pack Cost ($/kWh, most relevant to tipping analysis)

**All values: [observed]** (T2 Rethinkx, passenger BEV segment only)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2019 | 179 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2020 | 152 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2021 | 139 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2022 | 152 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2023 | 132 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2024 | 97 | $/kWh (rated) | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) | T2 | [observed] |

---

### Disruptor Cost History — EV Purchase Price ($/vehicle, USA — Entry-Level Segment)

**All values: [observed]** (T2 catalog, source "Database" — entry-level/economy segment only, NOT market-mix ATP)

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 52,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2012 | 50,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2014 | 47,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2016 | 43,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2018 | 39,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2020 | 35,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2021 | 34,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2022 | 33,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2023 | 32,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |
| 2024 | 31,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json | T2 | [observed] |

---

### Disruptor Cost History — EV Purchase Price ($/vehicle, China — Median Segment)

**All values: [observed]** (T2 catalog, source "Database")

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 39,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2013 | 33,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2016 | 26,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2019 | 21,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2021 | 18,500 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2022 | 17,300 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2023 | 16,500 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |
| 2024 | 16,200 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json | T2 | [observed] |

---

### Disruptor Cost History — EV Lowest-Cost Model ($/vehicle, USA, range <200 miles)

**All values: [observed]** (T2 catalog, source "Database" — represents cheapest available model in market each year)

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 109,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2013 | 80,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2017 | 37,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2019 | 36,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2021 | 31,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2022 | 26,595 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |
| 2024 | 29,000 | $/vehicle | data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json | T2 | [observed] |

---

### Disruptor Cost History — EV Market-Mix ATP ($/vehicle, USA — Full Market)

**All values: [observed]** (T3 Cox Automotive / Kelley Blue Book — market-mix inclusive of Tesla premium models)

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2021 | ~56,000 | $/vehicle | Cox Automotive / KBB ATP Report 2021 [T3] | T3 | [observed] |
| 2022 | ~65,108 | $/vehicle (peak) | Cox Automotive / KBB ATP Report 2022 [T3] | T3 | [observed] |
| 2023 Q3 | ~50,683 | $/vehicle | Cox Automotive / KBB ATP Report Sep 2023 [T3] | T3 | [observed] |
| 2024 Q1 | ~54,021 | $/vehicle | Cox Automotive / KBB ATP Report Mar 2024 [T3] | T3 | [observed] |
| 2024 Dec | 55,544 | $/vehicle | Cox Automotive / KBB ATP Report Dec 2024 [T3] | T3 | [observed] |

---

### Incumbent Cost History — ICE Purchase Price ($/vehicle, USA)

**All values: [observed]**

| Year | Cost ($/vehicle) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 22,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2012 | 23,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2014 | 24,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2016 | 25,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2018 | 26,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2020 | 27,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2022 | 28,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2024 | 29,000 | $/vehicle (mid-size sedan) | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json | T2 | [observed] |
| 2017 | 34,670 | $/vehicle (all-segment avg) | NADA Annual Data (Wards Intelligence / Automotive News) [T3] | T3 | [observed] |
| 2018 | 35,608 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2019 | 36,824 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2020 | 38,961 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2021 | 42,379 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2022 | 46,287 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2023 | 47,014 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |
| 2024 | 47,652 | $/vehicle (all-segment avg) | NADA Annual Data [T3] | T3 | [observed] |

---

### Incumbent Cost History — ICE Operating Costs (Supporting Data)

**All values: [observed]**

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2022 | 1.10 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) | T2 | [observed] |
| 2023 | 1.20 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) | T2 | [observed] |
| 2024 | 1.30 | $/mile (10k mi/yr) | data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) | T2 | [observed] |

---

### Fuel Cost Supporting Data — Gasoline (USA, computed annual median across states)

**All values: [observed]**

| Year | Median USD/L | USD/gal | Source | Tier | Data Type |
|------|-------------|---------|--------|------|-----------|
| 2015 | 0.510 | 1.93 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2016 | 0.570 | 2.16 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2017 | 0.610 | 2.31 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2018 | 0.715 | 2.71 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2019 | 0.660 | 2.50 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2020 | 0.550 | 2.08 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2021 | 0.790 | 2.99 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2022 | 0.985 | 3.73 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2023 | 0.910 | 3.44 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |
| 2024 | 0.845 | 3.20 | data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) | T2 | [observed] |

---

### Fuel Cost Supporting Data — Electricity, Residential USA

**All values: [observed]**

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 0.128 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2014 | 0.137 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2018 | 0.136 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2021 | 0.141 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2022 | 0.159 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2023 | 0.168 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |
| 2024 | 0.176 | $/kWh | data/electricity/cost/Electricity_Residential_Price_USA.json | T2 | [observed] |

---

### Current Costs

- **Disruptor current cost (battery pack):** $97/kWh (rated energy basis, 2024; Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json, Rethinkx T2 [observed])
- **Disruptor current cost (battery pack, T1 anchor):** $139/kWh (usable energy basis, 2023; DOE FOTW #1354, Argonne BatPaC [CAUTION: DOE source — historical data only] [observed])
- **Disruptor current cost (EV purchase price, entry-level USA):** $31,000/vehicle (2024; catalog T2 [observed])
- **Disruptor current cost (EV purchase price, market-mix USA):** $55,544/vehicle (December 2024; Cox/KBB T3 [observed])
- **Disruptor current cost (EV median China):** $16,200/vehicle (2024; catalog T2 [observed])
- **Incumbent current cost (ICE sedan USA):** $29,000/vehicle (2024; catalog T2 [observed])
- **Incumbent current cost (ICE all-segment avg USA):** $47,652/vehicle (2024; NADA T3 [observed])
- **Incumbent current cost (ICE all-segment avg, Cox/KBB):** $49,740/vehicle (December 2024; Cox/KBB T3 [observed])

---

### Unit Notes

- **Service-level unit:** $/vehicle (purchase price) — primary parity metric for consumer market (Market Type: Consumer per cost-rules Rule 3). Operating cost per mile is a secondary stack item per cost-rules Rule 1.
- **Hardware-to-service conversion needed:** YES — battery pack cost in $/kWh must be multiplied by pack capacity to yield $/vehicle battery component cost. The cost-fitter should use ~60–75 kWh as the representative USA passenger BEV pack size.
- **Conversion parameters available:**
  - USA pack size range: ~60–75 kWh (mid-range BEV; source: market knowledge, not catalog)
  - Electricity residential price available: $0.176/kWh (2024)
  - Gasoline price available: $0.845/L = $3.20/gal (2024)
  - ICE cost per mile (10k mi/yr): $1.30/mile (2024; AAA/Goldman Sachs, T2)
- **Rated vs. usable energy basis:** T2 Rethinkx values are on a rated/nameplate energy basis; T1 DOE values are on a usable-energy basis (typically 10–15% higher than rated basis in $/kWh terms for equivalent packs). The cost-fitter must apply a consistent basis when fitting the two series together.
- **Segment coverage warning:** Catalog EV and ICE purchase price curves track entry-level/economy segments. The KBB/Cox market-mix ATP series (T3) reflects the actual sales-weighted average including premium vehicles. The cost-fitter must choose which series to use for the parity computation and document that choice.

---

### Data Gaps

1. **EV market-mix ATP before 2021:** No T1/T3 source provides annual EV market-mix ATP for 2010–2020. The catalog entry-level series ($52,000 to $35,000, 2010–2020) is the only available proxy, and it underestimates the sales-weighted average.
2. **ICE all-segment market-mix ATP before 2017:** NADA data begins at 2017. Pre-2017 all-segment ATP is not available from T1/T3 public sources; catalog segments (sedan, SUV) are available individually.
3. **EV maintenance cost time series:** No catalog or web T1/T3 source provides annual BEV maintenance cost per mile or per year. This cost component must be dropped from the disaggregated stack per cost-rules Rule 1.
4. **ICE maintenance cost time series:** AAA publishes annual ICE maintenance estimates but not as a historical time series in available public form. No catalog curve exists. Dropped per cost-rules Rule 1.
5. **EV battery replacement cost:** No catalog or public T1/T3 time series available for battery mid-life replacement cost trajectory. Dropped per cost-rules Rule 1.
6. **BEV efficiency (kWh/mile) historical series:** Not in catalog; not found in T1/T3 web sources as a time series. The cost-fitter must use a fixed efficiency assumption (e.g., ~0.28 kWh/mile EPA average) to compute electricity cost per mile.
7. **2022 battery pack cost spike:** Both the T2 global median ($166/kWh) and T2 passenger BEV series ($152/kWh) show a 2022 uptick vs. 2021, consistent with the lithium carbonate price spike. The T1 DOE 2022 anchor ($153/kWh, usable basis) does not show this spike as dramatically. The cost-fitter should be aware that 2022 is an anomalous point that may affect learning-rate fits.
8. **China ICE price comparability:** The catalog China ICE sedan series uses USD values ($12,000–$19,000) that appear to be USD-converted RMB prices. Exchange rate assumptions underlying these USD values are not documented in the catalog metadata.

---

### Source Conflicts

1. **Battery pack 2022:** T2 global median shows $166/kWh (rated basis, Rethinkx); T1 DOE shows $153/kWh (usable basis, Argonne BatPaC). The T2 value is on a rated-energy basis (higher kWh denominator → lower $/kWh); the T1 is on a usable-energy basis (lower kWh denominator → higher $/kWh). After adjusting for the ~10–15% usable/rated difference, the values are directionally consistent. The T1 DOE value takes precedence as the primary T1 anchor but uses a different methodology. Both values are retained in the table with their basis noted.
2. **Battery pack 2023:** T2 global median shows $144/kWh (rated basis); T1 DOE shows $139/kWh (usable basis). Same basis difference as 2022. Both retained.
3. **ICE all-segment 2024:** NADA reports $47,652 (full-year 2024); Cox/KBB December 2024 reports $49,740. NADA is full-year average; KBB is a single month (December). The NADA annual figure ($47,652) is more representative of the full year and is used as the primary 2024 incumbent cost anchor.
4. **EV median USA catalog vs. market-mix KBB 2024:** Catalog entry-level median = $31,000; KBB market-mix ATP = $55,544. These are different populations (entry-level vs. market-mix). Both are valid and retained; the cost-fitter must explicitly choose which to use for parity analysis.

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | 15 battery pack data points 2010–2024 (T2) + 3 T1 DOE anchors (2008, 2022, 2023) — 16-year span |
| 2.2 | PASS | ICE sedan catalog 15 points 2010–2024 (T2) + NADA annual 8 points 2017–2024 (T3) |
| 2.3 | PASS | Li-ion passenger BEV pack: $97/kWh 2024 (T2 Rethinkx); EV ATP: $55,544 Dec 2024 (T3 Cox/KBB) |
| 2.4 | PASS | NADA all-segment avg: $47,652 full-year 2024 (T3); ICE sedan catalog: $29,000 2024 (T2) |

**Overall: COMPLIANT**

---

## Sources

- DOE FOTW #1354 (August 5, 2024): [https://www.energy.gov/eere/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty](https://www.energy.gov/eere/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty) [CAUTION: DOE source — historical data only]
- DOE FOTW #1272 (January 9, 2023): [https://www.energy.gov/eere/vehicles/articles/fotw-1272-january-9-2023-electric-vehicle-battery-pack-costs-2022-are-nearly](https://www.energy.gov/eere/vehicles/articles/fotw-1272-january-9-2023-electric-vehicle-battery-pack-costs-2022-are-nearly) [CAUTION: DOE source — historical data only]
- NADA Annual Financial Profile of Franchised New-Car Dealerships (2024): [https://www.nada.org/nada/nada-data](https://www.nada.org/nada/nada-data) [T3]
- Cox Automotive / Kelley Blue Book ATP Reports (2021–2024): [https://www.coxautoinc.com/learning-center/tag/average-transaction-price/](https://www.coxautoinc.com/learning-center/tag/average-transaction-price/) [T3]
- Cox Automotive December 2024 ATP Report: [https://www.coxautoinc.com/insights/december-2024-atp-report/](https://www.coxautoinc.com/insights/december-2024-atp-report/) [T3]
- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2]
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2]
- data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2]
- data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json (Database) [T2]
- data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json (Database) [T2]
- data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2]
- data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json (Database) [T2]
- data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json (AAA, Goldman Sachs Research) [T2]
- data/transport_fuel/cost/Gasoline_Average_Retail_Price_USA.json (WorldBank) [T2]
- data/electricity/cost/Electricity_Residential_Price_USA.json [T2]
