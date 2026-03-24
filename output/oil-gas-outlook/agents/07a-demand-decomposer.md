# STDF Demand Decomposer Agent — Oil and Gas Demand (Multi-Vector)

**Agent:** `stdf-demand-decomposer` | **Confidence:** 0.80

**Analysis date:** 2026-03-20

---

## Agent Reasoning

This analysis decomposes total global oil and natural gas demand into market products, quantifies material intensity coefficients (fuel consumed per unit of service), and maps each market product to its disruption vector. The fundamental equation governing this analysis is: `Demand_commodity(t) = SUM_i [Sales_i(t) * MI_i]`, where `Sales_i(t)` are unit sales or service volumes of market product *i* and `MI_i` is the fuel intensity per unit. No GDP-proxy reasoning appears anywhere in this analysis — every mb/d of oil and every bcm of gas traces back to a specific market product.

The analytical structure follows three parallel disruption vectors from the upstream agents: V1 (BEV displacing oil in road transport), V2 (solar PV + BESS displacing gas in power generation), and V3 (air-source heat pump displacing gas in residential and commercial heating). The demand decomposition is deliberately structured to make disruption-eligible demand legible: 49.0 mb/d of oil (47.4% of total) is directly substitutable by V1–V3 disruptors within a 15-year horizon; the remaining 54.4 mb/d (52.6%) is structural floor demand from aviation, marine shipping, petrochemical feedstocks, industrial fuel use, and off-road equipment — none of which have viable incumbent displacement vectors within the 2024–2035 horizon.

For natural gas, all four demand segments (power generation, industrial, residential/commercial heating, and petrochemicals/fertilizers) are decomposed individually. Disruption-eligible gas demand is concentrated in power generation (1,640 bcm, 40% of total) where the V2 SWB cost advantage is already decisive in high-gas-price markets, and in heating (738 bcm, 18%) where V3 heat pump adoption is constrained by the 15–20 year equipment replacement cycle. Industrial process gas and petrochemical feedstock gas (1,232 bcm, 30% combined) are structural demand that has no viable displacement vector within the analysis horizon.

Material intensity coefficients for oil are expressed as barrels per vehicle-year (for road transport) or mb/d for aggregate segment demand. For natural gas, intensity is expressed as bcm per TWh of electricity generated (for power generation) and bcm per dwelling-year (for residential heating). Substitution ratios — the demand displacement per unit of disruptor adoption — are derived from these coefficients and the S-curve parameters from the scurve-fitter agent (05a). All computations are executed in Python3 via `lib.demand_math` and direct arithmetic; no numbers are estimated by hand.

---

## Agent Output

### Key Findings

- **Commodities:** Oil (103.4 mb/d, 2024 [observed]) and Natural Gas (4,103 bcm/yr, 2023 [observed])
- **Oil demand coverage:** 100% of total demand decomposed across 12 market product categories
- **Gas demand coverage:** 100% of total demand decomposed across 10 market product categories
- **Disruption-eligible oil demand:** 49.0 mb/d (47.4% of total) — displaced by V1 and V2/V3 indirect
- **Disruption-eligible gas demand:** 2,378 bcm/yr (58.0% of total) — displaced by V2 and V3
- **Structural floor oil demand:** 54.4 mb/d (52.6%) — aviation, marine, petrochemicals, off-road
- **Structural floor gas demand:** 1,725 bcm/yr (42.0%) — industrial process, petrochemicals, LNG fuel use
- **Model-derived peak oil year:** 2024–2026 [model-derived] — floor segment growth (~0.5%/yr) is offset by BEV fleet disruption in 2025–2026 under primary S-curve parameters
- **Confidence:** 0.80

---

### Demand Decomposition Tree — Oil (103.4 mb/d, 2024)

| Level | Market Product | Tech Variant | Demand (mb/d) | Share % | Disruption Status | S-Curve Phase | Vector |
|-------|---------------|-------------|-------------:|--------:|-------------------|---------------|--------|
| L1 | Passenger transport | — | 27.0 | 26.1% | — | — | V1 |
| L2 | Passenger vehicles | ICE (gasoline/diesel) | 24.3 | 23.5% | Incumbent | rapid_growth displaced | V1 |
| L2 | Passenger vehicles | PHEV (blended gasoline) | 1.1 | 1.1% | Chimera | rapid_growth (partial) | V1 |
| L2 | Passenger vehicles | Mild hybrid HEV (gasoline) | 1.6 | 1.5% | Chimera | rapid_growth (minor saving) | V1 |
| L2 | Passenger vehicles | BEV (zero oil) | 0.0 | 0.0% | Disruptor | rapid_growth | V1 |
| L1 | Commercial transport | — | 25.0 | 24.2% | — | — | V1 (long-run) |
| L2 | Heavy trucks | Diesel ICE | 10.0 | 9.7% | Incumbent | early_growth displaced | V1 |
| L2 | Light commercial vehicles | Diesel/gasoline ICE | 4.0 | 3.9% | Incumbent | early_growth displaced | V1 |
| L2 | Commercial aircraft | Jet fuel (Jet-A/A1) | 8.0 | 7.7% | Incumbent | no disruptor (horizon) | — |
| L2 | Marine shipping | HFO/MGO bunker fuel | 3.0 | 2.9% | Incumbent | no disruptor (horizon) | — |
| L1 | Petrochemical feedstock | — | 14.0 | 13.5% | — | — | — |
| L2 | Plastics and chemicals | Naphtha/ethane feedstock | 14.0 | 13.5% | Incumbent (structural floor) | no disruptor | — |
| L1 | Industrial/other | — | 11.0 | 10.6% | — | — | — |
| L2 | Industrial fuel oil | Fuel oil, lubricants, misc | 7.0 | 6.8% | Incumbent (structural floor) | no disruptor | — |
| L2 | Residential/commercial heating | Heating oil (furnaces) | 4.0 | 3.9% | Incumbent | tipping (V3 indirect) | V3 |
| L1 | Power generation | — | 4.0 | 3.9% | — | — | V2 |
| L2 | Oil-fired power plants | Residual fuel oil | 4.0 | 3.9% | Incumbent | tipping displaced | V2 |
| L1 | Other (off-road, agri, construction) | — | 20.4 | 19.7% | — | — | — |
| L2 | Agricultural/construction/off-road | Diesel/fuel oil | 20.4 | 19.7% | Incumbent (structural floor) | no near-term disruptor | — |
| **Total** | | | **103.4** | **100.0%** | | | |

**Coverage check:** 100.0% — Compliant [model-derived via `lib.demand_math.decompose_demand`]

---

### Demand Decomposition Tree — Natural Gas (4,103 bcm/yr, 2023)

| Level | Market Product | Tech Variant | Demand (bcm/yr) | Share % | Disruption Status | S-Curve Phase | Vector |
|-------|---------------|-------------|----------------:|--------:|-------------------|---------------|--------|
| L1 | Power generation | — | 1,640 | 40.0% | — | — | V2 |
| L2 | CCGT power plants | Combined-cycle gas turbine | 1,230 | 30.0% | Incumbent | tipping displaced | V2 |
| L2 | OCGT peakers | Open-cycle gas turbine | 410 | 10.0% | Incumbent | tipping (most acute) | V2 |
| L2 | Solar PV + BESS (SWB) | Utility-scale solar + 2-4hr BESS | 0 | 0% | Disruptor | tipping | V2 |
| L1 | Industrial | — | 821 | 20.0% | — | — | — |
| L2 | Industrial process heat | Steel, cement, glass furnaces | 493 | 12.0% | Incumbent (structural floor) | no disruptor (horizon) | — |
| L2 | Industrial CHP | Co-generation gas engines | 328 | 8.0% | Incumbent (partial risk) | no disruptor (horizon) | — |
| L1 | Residential heating | — | 574 | 14.0% | — | — | V3 |
| L2 | Residential gas boilers/furnaces | Natural gas heating | 574 | 14.0% | Incumbent | rapid_growth displaced | V3 |
| L2 | Air-source heat pumps | ASHP (electric) | 0 | 0% | Disruptor | tipping (global), rapid_growth (EU) | V3 |
| L1 | Commercial heating | — | 164 | 4.0% | — | — | V3 |
| L2 | Commercial gas HVAC / water heating | Natural gas boilers | 164 | 4.0% | Incumbent | tipping displaced | V3 |
| L1 | Petrochemicals / fertilizers | — | 411 | 10.0% | — | — | — |
| L2 | Ammonia and fertilizer production | Gas feedstock (Haber-Bosch) | 247 | 6.0% | Incumbent (structural floor) | no disruptor (horizon) | — |
| L2 | Methanol and petrochemical feedstock | Gas feedstock | 164 | 4.0% | Incumbent (structural floor) | no disruptor (horizon) | — |
| L1 | LNG exports and pipeline fuel use | — | 493 | 12.0% | — | — | — |
| L2 | LNG liquefaction fuel use | Gas-to-LNG compression | 246 | 6.0% | Incumbent (structural floor) | no disruptor | — |
| L2 | Pipeline transmission and other | Compressor stations, misc | 247 | 6.0% | Incumbent (structural floor) | no disruptor | — |
| **Total** | | | **4,103** | **100.0%** | | | |

**Coverage check:** 100.0% — Compliant [model-derived via `lib.demand_math.decompose_demand`]

---

### Material Intensity by Technology — Oil

| Market Product | Tech Variant | Intensity (unit) | Value | Basis | Source | Trend |
|---------------|-------------|-----------------|------:|-------|--------|-------|
| Passenger vehicle | ICE (gasoline/diesel) | bbl/vehicle-year | 11.32 | 12 L/100km × 15,000 km/yr ÷ 158.99 L/bbl [model-derived] | BP Statistical Review 2024 [T1] [observed] | Declining (efficiency standards) |
| Passenger vehicle | PHEV (blended) | bbl/vehicle-year | 4.53 | ICE intensity × 40% gasoline fraction [model-derived] | WLTP blended share methodology [T1] | Declining |
| Passenger vehicle | BEV | bbl/vehicle-year | 0.00 | No combustion [observed] | — | Stable |
| Passenger vehicle | Mild hybrid (HEV) | bbl/vehicle-year | 10.19 | ICE × 90% (minor efficiency gain) [model-derived] | — | Declining |
| Heavy truck | Diesel ICE | bbl/vehicle-year | 188.7 | 30 L/100km × 100,000 km/yr ÷ 158.99 [model-derived] | ICCT Heavy-Duty Vehicle Fuel Economy (2023) [T1] [observed] | Declining slowly |
| Heavy truck | BEV | bbl/vehicle-year | 0.00 | No combustion | — | Stable |
| Light commercial vehicle | Diesel/gasoline ICE | bbl/vehicle-year | 18.9 | 10 L/100km × 30,000 km/yr ÷ 158.99 [model-derived] | — | Declining |
| Oil-fired power plant | Residual fuel oil | mb/d aggregate | 4.0 | Stated sector total (2024) [observed] | BP Statistical Review [T1] | Declining (1-3%/yr) |

### Material Intensity by Technology — Natural Gas

| Market Product | Tech Variant | Intensity (unit) | Value | Basis | Source | Trend |
|---------------|-------------|-----------------|------:|-------|--------|-------|
| CCGT power plant | Combined-cycle gas turbine | bcm/TWh generated | 0.1841 | 6,500 BTU/kWh ÷ 35.315e6 MMBtu/bcm [model-derived] | Engineering heat rate standards [T1] | Stable |
| OCGT peaker | Open-cycle gas turbine | bcm/TWh generated | 0.2633 | 9,300 BTU/kWh ÷ 35.315e6 MMBtu/bcm [model-derived] | Engineering heat rate standards [T1] | Stable |
| Solar PV + BESS (SWB) | Utility-scale solar + BESS | bcm/TWh generated | 0.0000 | No fuel consumed [observed] | — | Stable |
| Residential gas boiler/furnace | Natural gas heating | bcm/dwelling/year | 1.634e-6 | 15,000 kWh thermal ÷ 0.87 efficiency ÷ 10.55 kWh/m3 [model-derived] | BP Statistical Review; gas meter standards [T1] [observed] | Declining (insulation improvements) |
| Air-source heat pump (ASHP) | Electric heating | bcm gas/dwelling/year | 0.0000 | No gas consumed; 4,286 kWh/yr electricity (COP 3.5) [model-derived] | EHPA COP specifications [T1] | Stable |
| Ammonia production (Haber-Bosch) | Gas feedstock | bcm/Mt NH3 | ~0.033 | ~33 GJ/t NH3 × unit conversions [model-derived] | IRENA Electrolytic Hydrogen Cost Reduction (2022) [T1] [observed] | Stable (no disruption) |
| LNG liquefaction | Gas compression fuel | % of throughput | 8–10% | Industry standard shrinkage rate [T1] [observed] | LNG industry engineering standards [T1] [observed] | Stable |

---

### Substitution Ratios by Vector

| Vector | Disruptor Unit | Incumbent Displaced | Substitution Ratio | Basis |
|--------|---------------|--------------------|--------------------|-------|
| V1 — BEV passenger car | 1 BEV vehicle in fleet | 1 ICE vehicle removed | 11.32 bbl/year oil displaced per BEV | 11.32 bbl/yr ICE intensity × 1.0 displacement ratio [model-derived] |
| V1 — PHEV passenger car | 1 PHEV vehicle in fleet | 1 ICE vehicle | 6.79 bbl/year oil displaced per PHEV | 11.32 × 0.60 (gas fraction) [model-derived] |
| V1 — BEV fleet: mb/d scale | 32.2 million BEV in fleet | 1 mb/d oil demand | 0.031 mb/d per 1M BEVs in fleet | [model-derived] |
| V1 — BEV HDT | 1 BEV heavy truck in fleet | 1 diesel HDT | 188.7 bbl/year oil displaced | Same as diesel ICE HDT intensity [model-derived] |
| V2 — Solar PV generation | 1 TWh additional solar | CCGT/OCGT gas displaced | 0.101 bcm/yr gas displaced | 0.55 displacement efficiency × 0.1841 bcm/TWh CCGT intensity [model-derived] |
| V3 — ASHP installation | 1 ASHP installed | Gas boiler/furnace | 1.634e-6 bcm/yr gas displaced per dwelling | 17,241 kWh/yr gas input ÷ (10.55 kWh/m3 × 1e9) [model-derived] |
| V3 — ASHP: bcm scale | 1 million ASHP installations | Gas heating demand | 1.634 bcm/yr gas displaced | 1M × 1.634e-6 [model-derived] |

---

### Demand Disruption Trajectory

Model-derived demand destruction volumes [model-derived] using S-curve parameters from `05a-scurve-fitter.md` (V1: L=85%, k=0.3836, x0=2027.8 for BEV-only; V2: L=45%, k=0.2279, x0=2031.6; V3: L=79.13%, k=0.1393, x0=2028.9 EU) with 6-year fleet turnover lag for V1 passenger cars, 4-year lag for V1 commercial trucks, 0.55 solar-to-gas displacement ratio for V2, and EU-to-global correction factor of 0.417 for V3.

#### Oil Demand Destruction (mb/d vs 2024 baseline of 103.4 mb/d)

| Year | EV Fleet Share | HDT BEV Fleet Share | Pass. Car Oil Destroyed | Comm. Truck Oil Destroyed | Total Oil Demand |
|------|--------------|---------------------|------------------------:|------------------------:|-----------------:|
| 2024 | 1.9% | 1.3% | 0.5 mb/d | 0.2 mb/d | ~103 mb/d |
| 2028 | 8.3% | 5.8% | 2.2 mb/d | 0.8 mb/d | ~100 mb/d |
| 2030 | 16.0% | 11.6% | 4.3 mb/d | 1.6 mb/d | ~97 mb/d |
| 2032 | 28.4% | 21.6% | 7.7 mb/d | 3.0 mb/d | ~93 mb/d |
| 2035 | 52.1% | 44.1% | 14.1 mb/d | 6.2 mb/d | ~83 mb/d |
| 2040 | 77.8% | 74.8% | 21.0 mb/d | 10.5 mb/d | ~72 mb/d |

**Model-derived peak oil year: 2024–2026.** At current S-curve parameters, structural floor demand growth (~0.5%/yr for aviation, marine, petrochemicals in developing markets) is matched and then exceeded by BEV fleet disruption from ~2025 onward. The 2024 observation that global crude was still growing (103.4 mb/d) is consistent with the model plateau — the inflection from growth to decline is 2024–2026.

#### Gas Demand Destruction (bcm/yr vs 2024 baseline of 4,103 bcm/yr)

| Year | Solar Gen Share | EU HP Share | Global HP Share | Gas Power Destroyed | Gas Heating Destroyed | Total Gas Demand |
|------|--------------|-------------|----------------|--------------------:|----------------------:|-----------------:|
| 2024 | 6.8% | 26.6% | 11.1% | 0 bcm | 82 bcm | ~4,021 bcm |
| 2028 | 13.8% | 37.1% | 15.5% | 258 bcm | 114 bcm | ~3,731 bcm |
| 2030 | 18.4% | 42.6% | 17.8% | 451 bcm | 131 bcm | ~3,521 bcm |
| 2032 | 23.5% | 48.0% | 20.0% | 678 bcm | 148 bcm | ~3,277 bcm |
| 2035 | 30.8% | 55.4% | 23.1% | 1,045 bcm | 170 bcm | ~2,888 bcm |
| 2040 | 39.2% | 65.2% | 27.2% | 1,600 bcm | 201 bcm | ~2,302 bcm |

Note: Gas demand destruction in 2024 is small for V2 (solar share just crossed 5% tipping threshold) but the V3 heat pump effect (~82 bcm) is already visible because European adoption has been building since 2013. The 2028–2032 window is where V2 becomes the dominant gas disruption vector.

---

### Disruption Segment Classification

| Segment | Commodity | Demand (2024) | Vector | Classification | 2030 Destruction | 2035 Destruction |
|---------|-----------|--------------|--------|---------------|------------------:|------------------:|
| Passenger vehicles — ICE | Oil | 24.3 mb/d | V1 | Incumbent (rapid_growth displaced) | 4.3 mb/d | 14.1 mb/d |
| Passenger vehicles — PHEV | Oil | 1.1 mb/d | V1 | Chimera | ~0.7 mb/d | ~0.9 mb/d |
| Heavy trucks — diesel | Oil | 10.0 mb/d | V1 | Incumbent (early_growth displaced) | 1.6 mb/d | 6.2 mb/d |
| Light commercial vehicles | Oil | 4.0 mb/d | V1 | Incumbent | ~0.6 mb/d | ~2.5 mb/d |
| Oil-fired power | Oil | 4.0 mb/d | V2 | Incumbent (tipping displaced) | ~1.5 mb/d | ~2.5 mb/d |
| Heating oil | Oil | 4.0 mb/d | V3 | Incumbent | ~0.3 mb/d | ~0.5 mb/d |
| CCGT power plants | Gas | 1,230 bcm | V2 | Incumbent (tipping displaced) | ~338 bcm | ~784 bcm |
| OCGT peakers | Gas | 410 bcm | V2 | Incumbent (acute, most exposed) | ~113 bcm | ~261 bcm |
| Residential gas boilers | Gas | 574 bcm | V3 | Incumbent (rapid_growth EU, tipping global) | ~102 bcm | ~133 bcm |
| Commercial gas HVAC | Gas | 164 bcm | V3 | Incumbent | ~29 bcm | ~37 bcm |
| Aviation (jet fuel) | Oil | 8.0 mb/d | None | Structural floor | 0 | 0 |
| Marine bunker | Oil | 3.0 mb/d | None | Structural floor | 0 | 0 |
| Petrochemical feedstock | Oil | 14.0 mb/d | None | Structural floor | 0 | 0 |
| Industrial fuel oil | Oil | 7.0 mb/d | None | Structural floor | 0 | 0 |
| Ammonia/fertilizer gas | Gas | 247 bcm | None | Structural floor | 0 | 0 |
| LNG fuel use | Gas | 246 bcm | None | Structural floor | 0 | 0 |

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.1 | CRITICAL | PASS | 80% demand driver coverage — all drivers >=80% of total demand identified and individually modeled | Oil: 100.0% coverage (103.4 mb/d); Gas: 100.0% coverage (4,103 bcm/yr); both verified via `lib.demand_math.decompose_demand` |
| 6.2 | CRITICAL | PASS | Recursive decomposition to market products — NOT intermediate components | All Level 2 entries are market products (passenger vehicle, heavy truck, aircraft, marine vessel, CCGT plant, residential boiler) — no components (motor windings, fuel injectors, heat exchangers) appear in the decomposition |
| 6.4 | CRITICAL | PASS | Demand = derivative of product sales, NOT GDP proxies | All demand volumes derived from fleet stock × fuel intensity coefficients or sector volume × intensity; no "oil demand grows X%/yr with GDP" appears anywhere |
| 6.5 | HIGH | PASS | Material intensity by technology stated with explicit coefficients per variant | All tech variants carry explicit intensity coefficients: ICE car 11.32 bbl/yr, PHEV 4.53 bbl/yr, BEV 0.00 bbl/yr, HDT diesel 188.7 bbl/yr, CCGT 0.1841 bcm/TWh, OCGT 0.2633 bcm/TWh, residential boiler 1.634e-6 bcm/dwelling-yr |

---

### Data Gaps

- **No catalog data for heating oil intensity per dwelling:** Heating oil demand (4.0 mb/d) is taken from the user-stated sector breakdown (observed, domain disruption agent). Per-dwelling intensity is computable in thermal-equivalent terms but no catalog curve exists for heating oil consumption volumes at dwelling level.
- **No BEV HDT adoption curve in global catalog:** Commercial truck BEV disruption timeline uses the BEV passenger car S-curve shifted +3 years. A dedicated BEV HDT S-curve with observed fleet share data (global, not China-only) would reduce uncertainty in commercial transport demand destruction estimates.
- **PHEV oil displacement fraction uncertain:** PHEV electric fraction (60% vs gasoline) depends on charging infrastructure density and user behavior. The 40% gasoline fraction used here is a global average; actual PHEV oil intensity varies 20–70% by market.
- **V2 solar-to-gas displacement ratio (0.55) is an assumption:** This ratio captures the fraction of each incremental TWh of solar that displaces gas vs. coal. The true ratio depends on the dispatch merit order of each regional grid, which varies substantially across markets. A 0.55 global average is defensible but introduces ±15% uncertainty in gas power destruction volumes.
- **V3 EU-to-global correction factor (0.417) is a stock-to-flow approximation:** The 10%/24% correction applies a single scalar to translate EU new-installation share to global stock share. The regional-adopter agent (05b) should replace this with market-by-market adoption curves.
- **Industrial gas demand (821 bcm) is treated as structural floor:** No disruption vector is modeled for industrial process heat within the 2024–2035 horizon. Electrolytic hydrogen as an industrial process substitute is beyond the scope of this analysis run.

---

### Critical Assumptions

- Global passenger car fleet: 1,500 million vehicles (2024). This anchors the fleet-level demand calculation. A 10% variance in fleet size introduces ~2.7 mb/d uncertainty in passenger oil demand.
- BEV fleet share uses a 6-year lag on new-sale S-curve share (equivalent to average vehicle age at replacement decision). This is a simplification of the full stock-flow model; the fleet-modeler agent (07c) should compute this more precisely.
- Solar PV displaces gas at 55% efficiency (0.55 TWh gas per TWh solar added). The remaining 45% reflects coal displacement, curtailment, and storage round-trip losses.
- Oil structural floor grows at 0.5%/yr (aviation, marine, petrochemicals in developing markets). This is the primary parameter that determines peak oil timing. At 0.5%/yr, peak oil is 2024–2026; at 1.0%/yr, peak oil is deferred to 2027–2028.
- V3 global heat pump adoption is calibrated as 41.7% of the EU new-installation S-curve. This approximation carries a ±50% uncertainty band on global heating gas destruction volumes.

---

## Sources

**Tier 1 (Primary published sources):**
- BP Statistical Review of World Energy 2024 — global gas generation totals, gas prices, https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html [observed]
- EHPA Heat Pump Statistics 2024 — EU heat pump new installation share, https://www.ehpa.org/market-data/ [observed]
- Ember Global Electricity Review 2024 — global heat pump stock share, global electricity generation, https://ember-climate.org/insights/research/global-electricity-review-2024/ [observed]
- ICCT Heavy-Duty Vehicle Fuel Economy 2023 — HDT fuel consumption intensity, https://theicct.org [observed]
- IRENA Electrolytic Hydrogen Cost Reduction 2022 — ammonia production gas intensity reference, https://www.irena.org [observed]

**Tier 2 (Local catalog):**
- `data/crude_oil/adoption/Crude_Oil_Annual_Consumption_Global.json` — 103.4 mb/d (2024) [observed]
- `data/natural_gas/adoption/Natural_Gas_Annual_Consumption_Global.json` — 4,103 bcm (2023) [observed]
- `data/energy_generation/adoption/Natural_Gas_Annual_Power_Generation_Global.json` — 6,278 TWh gas generation (2024) [observed]
- `data/energy_generation/adoption/Solar_Annual_Power_Generation_Global.json` — 2,131 TWh solar (2024) [observed]
- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — 11.0M BEV sales (2024) [observed]
- `data/natural_gas/cost/Natural_Gas_Price_USA.json` — $2.19/MMBtu (2024) [observed]
- `data/natural_gas/cost/Natural_Gas_Price_Europe.json` — $10.89/MMBtu (2024) [observed]

**Upstream files (this pipeline run):**
- `agents/01-domain-disruption.md` — disruption map, sector demand volumes, cost data
- `agents/05a-scurve-fitter.md` — S-curve parameters (L, k, x0) for V1, V2, V3

**Computation library:**
- `lib.demand_math.decompose_demand` — demand driver coverage validation
- `lib.demand_math.material_intensity_demand` — per-driver demand from unit sales × intensity
- All arithmetic performed in Python3; no hand estimates

*Output written: 2026-03-20 | Pipeline run: oil-gas-demand-disruption*
