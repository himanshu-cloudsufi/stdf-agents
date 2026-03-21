# STDF Cost Fitter Agent — BEV Heavy Trucks vs. Diesel (China)

**Agent:** `stdf-cost-fitter` | **Confidence:** 0.81

---

## Disruption Context

This analysis covers a market-driven disruption of diesel incumbent commercial vehicles in China by BEV heavy trucks. Cost-curve dynamics in LFP battery packs — the primary cost driver of BEV powertrains — are the gravitational force causing incumbent displacement of diesel in the heavy trucking segment. The BEV per-km energy cost crossed parity with diesel before 2019; purchase price parity for short-haul tractors (282 kWh) crossed in 2024. S-curve adoption patterns are already visible in market share data (1% in 2020 to 13% in 2024 to ~21% in December 2024). Note: this analysis uses stellar energy to mean solar/wind/battery as an energy conversion category; BEV trucks specifically are an electrification-of-transport technology, not a stellar energy generation technology.

---

## Agent Reasoning

The cost-researcher delivered four distinct cost data sets: (1) BEV HCV purchase price via T2 catalog in USD, 9 points spanning 2010–2024; (2) BEV 49t tractor T3 transaction prices in CNY, 4 points spanning 2021–2024; (3) LFP battery pack costs from two series — a long-run median China series (8 points, 2010–2024) and the Rethinkx E-Bus/Commercial series (7 points, 2018–2024); and (4) diesel ICE incumbent purchase price (9 points, 2010–2024) plus diesel retail fuel price (10 annual points, 2015–2024). The per-km operating cost comparison table was computed by the cost-researcher using literature consumption parameters (2.0 kWh/km BEV, 0.30 L/km diesel) and carried forward here as [model-derived] input.

No hardware-to-service conversion was required for the per-km energy cost analysis — the upstream researcher already derived CNY/km figures from catalog fuel prices and literature consumption rates. For the purchase price component, the unit is CNY/vehicle or USD/vehicle — a direct fleet-market cost-per-unit comparison (not a per-km conversion). This is appropriate for the fleet market type per shared-cost-rules.md Rule 3. Battery pack costs are reported in $/kWh (hardware component unit) separately and are NOT carried into the purchase price parity comparison directly; they serve as a structural explanation for the BEV cost decline trajectory.

Two exponential fits were computed for BEV purchase price. The T2 USD catalog fit (R²=0.992, 9 pts, 2010–2024) is the higher-confidence long-run series, yielding a conservative learning rate of 5.79%/yr and a model-derived crossover with the rising ICE price at 2029–2030 under the linear trend. The T3 CNY transaction fit (R²=0.753, 4 pts, 2021–2024) captures the aggressive recent price-war compression in the 440 kWh tractor segment, yielding a 9.65%/yr learning rate and a model-derived crossover at 2026–2027. The 282 kWh short-haul tractor is already below ICE diesel purchase price in 2024 (CNY 400k vs. CNY 486k). Per-km energy cost parity was crossed well before 2019 — BEV trucks have had a structural per-km operating cost advantage for the entire observable period, and that advantage is widening as diesel fuel prices continue their linear rise.

The T3 fit (R²=0.753) falls below the 0.80 flag threshold; this is flagged in Data Gaps. The 2022 lithium carbonate spike creates a visible outlier in the Rethinkx commercial battery series (R²=0.803, near minimum) — this is a real observed price event and is preserved in the series, not smoothed. The battery long-run fit (R²=0.976) is the highest-confidence series and anchors the structural learning rate interpretation for LFP chemistry.

---

## Agent Output

### Key Findings
- **Disruptor:** BEV heavy commercial vehicles (49t tractor-trailers, 282–440 kWh LFP, China)
- **Incumbent:** Diesel heavy commercial vehicles (ICE tractor-trailers, China)
- **Service unit:** CNY per vehicle (purchase price); CNY per km (fleet operating cost)
- **Confidence:** 0.81

---

### Disruptor Cost Trajectory — BEV HCV Purchase Price (T2 Catalog USD, 2010–2024)

**All values: [observed] from T2 catalog unless noted**

| Year | Cost (USD) | Cost (CNY est.) | Unit | Source | Data Type |
|------|-----------|----------------|------|--------|-----------|
| 2010 | 260,000 | 1,794,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2012 | 230,000 | 1,449,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2015 | 200,000 | 1,384,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2018 | 170,000 | 1,142,200 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2020 | 150,000 | 1,035,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2021 | 140,000 | 903,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2022 | 130,000 | 875,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2023 | 120,000 | 852,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |
| 2024 | 110,000 | 787,000 | USD/vehicle | HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json [T2] | [observed] |

### Disruptor Cost Trajectory — BEV 49t Tractor Transaction Prices (T3 CNY, 2021–2024)

**All values: [observed] from chinatruck.net fleet transactions**

| Year | Cost (CNY) | Cost (USD) | Battery Capacity | Unit | Source | Data Type |
|------|-----------|-----------|-----------------|------|--------|-----------|
| 2021 | 903,000 | 140,000 | 440 kWh | CNY/vehicle | Catalog T2 anchor [observed] | [observed] |
| 2022 | 875,000 | 130,000 | 440 kWh | CNY/vehicle | Catalog T2 anchor [observed] | [observed] |
| 2023 | 850,000 | 120,000 | 440 kWh | CNY/vehicle | chinatruck.net fleet transaction Sep 2023 [T3] | [observed] |
| 2024 | 650,000 | 91,000 | 400 kWh | CNY/vehicle | chinatruck.net fleet transaction Apr 2024 [T3] | [observed] |
| 2024 | 400,000 | 56,000 | 282 kWh | CNY/vehicle | chinatruck.net Shaanxi Auto M3000E late 2024 [T3] | [observed] |

---

### Disruptor Cost Trajectory — LFP Battery Pack ($/kWh, Component Only)

**Note: Battery pack cost is a component-level metric, reported here as structural context for the purchase price decline. It is NOT the cost-parity metric for the fleet comparison.**

**Long-run series (Li-Ion Median China): All values [observed] from T2 catalog**

| Year | Cost ($/kWh) | Source | Data Type |
|------|-------------|--------|-----------|
| 2010 | 1,100 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2013 | 600 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2015 | 400 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2017 | 226 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2019 | 156 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2021 | 127 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2023 | 94 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |
| 2024 | 94 | Lithium_Ion_Battery_Pack_Median_Cost_China.json [T2] | [observed] |

**Rethinkx E-Bus/Commercial series (primary for BEV trucks): All values [observed] from T2 catalog**

| Year | Cost ($/kWh) | Source | Data Type |
|------|-------------|--------|-----------|
| 2018 | 177 | Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_China.json [T2] (Rethinkx) | [observed] |
| 2019 | 170 | Rethinkx [T2] | [observed] |
| 2020 | 127 | Rethinkx [T2] | [observed] |
| 2021 | 119 | Rethinkx [T2] | [observed] |
| 2022 | 144 | Rethinkx [T2] — lithium carbonate price spike [observed] | [observed] |
| 2023 | 103 | Rethinkx [T2] | [observed] |
| 2024 | 90 | Rethinkx [T2] | [observed] |

---

### Incumbent Cost Trajectory — ICE Diesel Purchase Price (USD/vehicle)

**All values: [observed] from T2 catalog**

| Year | Cost (USD) | Cost (CNY est.) | Unit | Source | Data Type |
|------|-----------|----------------|------|--------|-----------|
| 2010 | 40,000 | 276,400 | USD/vehicle | Heavy_Duty_Commercial_Vehicle_(ICE)_Price_China.json [T2] | [observed] |
| 2013 | 46,000 | 289,800 | USD/vehicle | [T2] | [observed] |
| 2016 | 52,000 | 345,800 | USD/vehicle | [T2] | [observed] |
| 2018 | 56,000 | 376,320 | USD/vehicle | [T2] | [observed] |
| 2020 | 60,000 | 414,000 | USD/vehicle | [T2] | [observed] |
| 2021 | 62,000 | 399,900 | USD/vehicle | [T2] | [observed] |
| 2022 | 64,000 | 430,720 | USD/vehicle | [T2] | [observed] |
| 2023 | 66,000 | 468,600 | USD/vehicle | [T2] | [observed] |
| 2024 | 68,000 | 486,200 | USD/vehicle | [T2] | [observed] |

### Incumbent Cost Trajectory — Diesel Retail Fuel Price (USD/L)

**All values: [observed] T1, WorldBank multi-provincial series**

| Year | USD/L | Source | Data Type |
|------|-------|--------|-----------|
| 2015 | 0.820 | WorldBank via T2 catalog [T1] | [observed] |
| 2016 | 0.825 | WorldBank [T1] | [observed] |
| 2017 | 0.870 | WorldBank [T1] | [observed] |
| 2018 | 1.050 | WorldBank [T1] | [observed] |
| 2019 | 0.930 | WorldBank [T1] | [observed] |
| 2020 | 0.770 | WorldBank [T1] | [observed] |
| 2021 | 1.025 | WorldBank [T1] | [observed] |
| 2022 | 1.190 | WorldBank [T1] | [observed] |
| 2023 | 1.080 | WorldBank [T1] | [observed] |
| 2024 | 1.045 | WorldBank [T1] | [observed] |

---

### Disaggregated Cost Comparison (Service-Level)

Per shared-cost-rules.md Rule 1: three cost components presented separately; no TCO aggregate.

#### 1. Purchase Price Trajectory (CNY/vehicle or USD/vehicle)

The primary cost-parity metric per shared-cost-rules.md Rule 2 default hierarchy is purchase price, as this is the most directly observable and least assumption-laden metric for this fleet market.

| Year | BEV (T2, USD) | ICE Diesel (USD) | BEV Premium (USD) | Data Type |
|------|--------------|-----------------|-------------------|-----------|
| 2010 | 260,000 | 40,000 | +220,000 | [observed] |
| 2018 | 170,000 | 56,000 | +114,000 | [observed] |
| 2021 | 140,000 | 62,000 | +78,000 | [observed] |
| 2023 | 120,000 | 66,000 | +54,000 | [observed] |
| 2024 | 110,000 | 68,000 | +42,000 | [observed] |
| 2025 | 103,000 [model-derived] | 70,000 [model-derived] | +33,000 | [model-derived] |
| 2027 | 91,000 [model-derived] | 74,000 [model-derived] | +17,000 | [model-derived] |
| 2029 | 81,000 [model-derived] | 78,000 [model-derived] | +3,000 | [model-derived] |
| 2030 | 76,000 [model-derived] | 80,000 [model-derived] | −4,000 | [model-derived] |

**T3 transaction data (CNY, 440 kWh tractor):**

| Year | BEV CNY | ICE CNY | BEV Premium (CNY) | Data Type |
|------|---------|---------|-------------------|-----------|
| 2023 | 850,000 | 468,600 | +381,400 | [observed] |
| 2024 | 650,000 | 486,200 | +163,800 | [observed] |
| 2024 | 400,000 (282 kWh) | 486,200 | −86,200 | [observed] — already cheaper |
| 2025 | 588,000 [model-derived] | 500,500 | +87,500 | [model-derived] |
| 2026 | 531,000 [model-derived] | 514,800 | +16,200 | [model-derived] |
| 2027 | 480,000 [model-derived] | 529,100 | −49,100 | [model-derived] |

#### 2. Energy Cost Trajectory (CNY/km — fleet operating cost)

**All forward values: [model-derived] from upstream consumption parameters + diesel price trend**

| Year | BEV (CNY/km) | Diesel (CNY/km) | BEV % of Diesel | Data Type |
|------|-------------|----------------|----------------|-----------|
| 2019 | 1.20 | 1.93 | 62.2% | [model-derived] |
| 2020 | 1.24 | 1.59 | 78.0% | [model-derived] |
| 2021 | 1.30 | 1.98 | 65.7% | [model-derived] |
| 2022 | 1.34 | 2.40 | 55.8% | [model-derived] |
| 2023 | 1.40 | 2.30 | 60.9% | [model-derived] |
| 2024 | 1.44 | 2.24 | 64.3% | [model-derived] |
| 2025 | 1.46 | 2.31 | 63.2% | [model-derived] |
| 2026 | 1.48 | 2.38 | 62.2% | [model-derived] |
| 2027 | 1.50 | 2.44 | 61.5% | [model-derived] |
| 2028 | 1.52 | 2.51 | 60.6% | [model-derived] |
| 2029 | 1.54 | 2.58 | 59.7% | [model-derived] |

Per-km energy cost parity was crossed before 2019. BEV had a 35.7% per-km energy cost advantage as of 2024.

#### 3. Maintenance Cost

Not available as a sourced time series. Dropped from analysis per shared-cost-rules.md Rule 1. Noted in Data Gaps.

---

### Exponential Fit — BEV HCV Purchase Price (T2 Catalog USD)

- **Formula:** C(t) = 264,777.65 × exp(−0.0596 × (t − 2010))
- **C0:** 264,777.65 USD
- **r (decay rate):** 0.0596
- **Reference year:** 2010
- **R-squared:** 0.9921
- **Data points used:** 9
- **Year span:** 2010–2024 (14 years)
- **Validation (2024):** Model output = $114,949; observed = $110,000; deviation = 4.5% [PASS — within 15% threshold]

### Exponential Fit — BEV 49t Tractor Purchase Price (T3 CNY, 440 kWh)

- **Formula:** C(t) = 946,550.67 × exp(−0.1015 × (t − 2021))
- **C0:** 946,550.67 CNY
- **r (decay rate):** 0.1015
- **Reference year:** 2021
- **R-squared:** 0.7526
- **Data points used:** 4
- **Year span:** 2021–2024 (3 years)
- **Warning:** R²=0.753 < 0.80 — LOW CONFIDENCE FIT. Only 4 points; price compression is real but the rate may not persist. See Data Gaps.
- **Validation (2024):** Model output = CNY 698,074; observed = CNY 650,000; deviation = 7.4% [PASS]

### Exponential Fit — LFP Battery Pack, Long-Run Median China

- **Formula:** C(t) = 979.25 × exp(−0.1823 × (t − 2010))
- **C0:** 979.25 $/kWh
- **r (decay rate):** 0.1823
- **Reference year:** 2010
- **R-squared:** 0.9762
- **Data points used:** 8
- **Year span:** 2010–2024 (14 years)
- **Validation (2024):** Model output = $76.3/kWh; observed = $94/kWh; deviation = 18.8% — above 15% threshold, flagged in Data Gaps. The model underestimates recent cost (the curve is flattening as chemistry matures).

### Exponential Fit — LFP Battery Pack, Rethinkx E-Bus/Commercial

- **Formula:** C(t) = 176.64 × exp(−0.1038 × (t − 2018))
- **C0:** 176.64 $/kWh
- **r (decay rate):** 0.1038
- **Reference year:** 2018
- **R-squared:** 0.8034
- **Data points used:** 7
- **Year span:** 2018–2024 (6 years)
- **Note:** 2022 spike (lithium carbonate) depresses R². The spike is preserved as an observed event; it is not smoothed.

---

### Learning Rate

#### BEV HCV Purchase Price (T2 USD, long-run)
- **Value:** 5.79% per year
- **Basis:** per_year
- **Derived from:** 14-year exponential fit to T2 catalog USD series, r=0.0596, R²=0.992, 9 data points

#### BEV 49t Tractor Purchase Price (T3 CNY, recent price-war period)
- **Value:** 9.65% per year
- **Basis:** per_year
- **Derived from:** 4-point exponential fit to T3 CNY transaction series 2021–2024, r=0.1015, R²=0.753 (low confidence — flagged)

#### LFP Battery Pack — Long-Run (Median China)
- **Value:** 16.66% per year
- **Basis:** per_year
- **Derived from:** 14-year exponential fit to Li-Ion Median China catalog series, r=0.1823, R²=0.976, 8 data points — highest-confidence rate

#### LFP Battery Pack — E-Bus/Commercial (Rethinkx)
- **Value:** 9.86% per year
- **Basis:** per_year
- **Derived from:** 7-point exponential fit to Rethinkx commercial series 2018–2024, r=0.1038, R²=0.803; 2022 lithium spike depresses rate

---

### Incumbent Trend

#### ICE Diesel Purchase Price
- **Model:** linear_rising
- **Slope per year:** +2,000 USD/year (+14,300 CNY/year at 7.15)
- **R-squared:** 1.0000 (perfect fit on 9 catalog points — consistent steady-state pricing)
- **Structural drivers:** loss of scale economies as BEV share grows from 1% to 13%+ (2020–2024); stranded fixed costs in ICE powertrain manufacturing capacity; rising regulatory compliance costs (China VI emission standards since 2021)

#### Diesel Retail Fuel Price
- **Model:** linear_rising
- **Slope per year:** +0.031 USD/L/year (+0.22 CNY/L/year)
- **R-squared:** 0.4780 (low fit — significant commodity price volatility)
- **Mean:** 0.960 USD/L
- **Structural drivers:** fuel price exposure to Brent crude volatility; structurally rising extraction costs; domestic refining margin pressure; note that R²=0.478 reflects commodity price cycles, not a declining trend — the fuel price is not falling

---

### Competitive Threshold (Cost Parity)

#### Purchase Price — 282 kWh Short-Haul Tractor
- **Status:** Already crossed in 2024
- **Evidence:** CNY 400,000 BEV vs. CNY 486,200 diesel ICE (2024 observed [T3 + T2])
- **BEV advantage at crossover:** 17.7% cheaper than ICE purchase price [observed]

#### Purchase Price — 440 kWh Long-Haul Tractor (T3 CNY model)
- **Year range:** 2026–2027 [model-derived]
- **Cost at parity:** CNY ~515,000–530,000 per vehicle [model-derived]
- **Unit:** CNY/vehicle

#### Purchase Price — Broad HCV Fleet (T2 USD model, conservative)
- **Year range:** 2029–2030 [model-derived]
- **Cost at parity:** ~$78,000–$80,000 per vehicle [model-derived]
- **Unit:** USD/vehicle
- **Note:** T2 catalog represents a broad commercial EV fleet, not exclusively 49t tractors. This is the conservative bound.

#### Per-km Energy Operating Cost
- **Status:** Already crossed — BEV has been cheaper than diesel on a per-km energy cost basis throughout the entire 2019–2024 observable period
- **2024 BEV advantage:** 35.7% (CNY 1.44/km vs. CNY 2.24/km) [model-derived from T1 fuel data + literature consumption parameters]

---

### Inflection Threshold

#### Purchase Price — 440 kWh Tractor (50–70% of ICE price)
- **Year range:** 2029–2032 [model-derived]
- **BEV cost range at inflection:** CNY 310,000–380,000 per vehicle [model-derived]
- **Percent of incumbent:** 50–70% of ICE price (~CNY 572,000–600,000 at that time) [model-derived]
- **Interpretation:** This is the gravity threshold — when the 440 kWh tractor reaches 50–70% of ICE purchase price, the economics of retaining diesel become indefensible for all fleet operators, including those in geographies with premium electricity pricing.

#### Per-km Energy Cost Inflection
- **Status:** Already past — BEV per-km energy cost has been 60–78% of diesel per-km cost since 2019, and remained at 64% in 2024. The threshold was crossed before the observable data window.

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 2.5 | CRITICAL | PASS | Purchase price in CNY/vehicle; energy cost in CNY/km; battery in $/kWh — all service-level or component-level with named conversion params |
| 2.6 | HIGH | PASS | Direct CNY/vehicle and CNY/km comparison, no TCO aggregate |
| 2.7 | HIGH | PASS | T2 USD: 5.79%/yr from r=0.0596 (R²=0.992, 9 pts); LFP long-run: 16.66%/yr from r=0.1823 (R²=0.976, 8 pts) — none assumed |
| 2.8 | HIGH | PASS | Three exponential fits: T2 R²=0.992; T3 R²=0.753; LFP long-run R²=0.976; LFP Rethinkx R²=0.803 |
| 2.9 | HIGH | PASS | ICE diesel: linear_rising +2,000 USD/yr, R²=1.00; diesel fuel: linear_rising +0.031 USD/L/yr, R²=0.478 |
| 2.10 | HIGH | PASS | 282 kWh: already crossed 2024; 440 kWh: 2026–2027; per-km energy cost: crossed pre-2019 |
| 2.11 | MEDIUM | PASS | 440 kWh purchase price inflection (50–70% of ICE): 2029–2032; per-km inflection already passed |

**Overall: COMPLIANT**

---

### Data Gaps

1. **T3 CNY fit has R²=0.753** — below 0.80 threshold. Only 4 data points over 3 years; the recent price-war compression rate (9.65%/yr) may not persist beyond 2025–2026 as market consolidation proceeds. Use this as an upper bound, not a central estimate.
2. **LFP battery long-run fit: 18.8% deviation at 2024** — the exponential model overestimates cost decline speed; the actual battery cost curve is flattening as LFP chemistry matures toward a floor. The long-run learning rate (16.66%/yr) should be treated as historical, not forward-looking, for post-2024 battery cost analysis.
3. **No maintenance cost time series.** Maintenance differential (BEV lower than diesel) is not available as a sourced series. This cost component is excluded from all comparisons per shared-cost-rules.md Rule 1.
4. **No LNG truck purchase price time series.** LNG trucks hold ~29% China HCV market share in 2024. The LNG competitive dynamics are excluded from this analysis; a separate LNG/BEV vector should be analyzed if LNG displacement is the specific query.
5. **Electricity price regional variance is wide.** The CNY 0.72/kWh midpoint used in per-km calculations spans CNY 0.43–0.88/kWh across provinces. Inner Mongolia logistics corridors (CNY 0.43–0.54/kWh) are significantly more favorable for BEV operators than coastal urban rates.
6. **Battery swap vehicle pricing not captured.** Swap-capable trucks (29,569 units in 2024, +94% YoY) separate battery cost from vehicle frame cost. Upfront purchase price for swap models is substantially lower; this creates a second purchase price curve not modeled here.
7. **Pre-2021 T3 transaction data absent.** The T3 fit begins in 2021; there is no independent observed transaction data for 2010–2020 BEV tractor purchase prices.

---

### Critical Assumptions

1. **T2 BEV HCV catalog treated as 400km-range configuration.** The T2 series is labeled "Range-400KM_Lowest_Cost_China" — represents the most competitive BEV configuration available in each year, which trends toward the market-clearing price as competition intensifies.
2. **ICE diesel purchase price treated as linear_rising at +$2,000/yr.** The R²=1.000 fit on the T2 catalog data is mechanically smooth — this may reflect catalog smoothing rather than real market data. Applied as a structural lower bound for ICE pricing.
3. **T3 CNY 440 kWh series used for long-haul tractor crossover; T3 282 kWh treated as a single-year (2024) observed data point.** Two-point fits are not computed; the 282 kWh crossover is based on direct 2024 price comparison.
4. **Per-km energy cost computations carry forward the upstream researcher's conversion parameters** (2.0 kWh/km BEV, 0.30 L/km diesel, CNY 0.72/kWh electricity midpoint). These are literature-derived, not measured fleet data.
5. **CNY/USD exchange rate held at 7.15 (2024) for forward curve comparisons.** No currency forward model is applied.
6. **Diesel fuel forward trend applied at +0.031 USD/L/yr from 2024 base.** The R²=0.478 for the fuel price linear fit reflects commodity volatility; the trend direction is rising but the magnitude is uncertain. This is a structural assumption, not a commodity price model.

---

## Sources

- data/commercial_vehicle/cost/HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json — T2 catalog, HCV BEV China purchase price 2010–2025
- data/commercial_vehicle/cost/Heavy_Duty_Commercial_Vehicle_(ICE)_Price_China.json — T2 catalog, ICE diesel heavy truck China 2010–2024
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_China.json — T2 catalog, Rethinkx LFP commercial/e-bus battery China 2018–2024
- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json — T2 catalog, Li-Ion median China 2010–2025
- data/transport_fuel/cost/Diesel_Average_Retail_Price_China.json — T1/T2 catalog, WorldBank multi-provincial diesel price series China
- chinatruck.net — "Chinese electric heavy-duty trucks are caught up in a price war" — T3, retrieved 2026-03-20; BEV truck CNY transaction prices 2023–2024
- eu.36kr.com — "Chinese New Energy Heavy Trucks: On a Rampage in the Market!" — T3, retrieved 2026-03-20; battery CNY/Wh price and per-km savings
- ICCT — "Total Cost of Ownership for Heavy Trucks in China" (Nov 2021) — T1 [CAUTION: ICCT source — historical data only]; BEV consumption parameters context
- CEIC / NDRC — China industrial electricity price data — T1 (government source); electricity price ranges CNY/kWh by region
- Nature Energy (2024) — "Rapidly declining costs of truck batteries and fuel cells" — T1 peer-reviewed; battery cost decline meta-analysis context
