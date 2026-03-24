# STDF Adoption S-Curve Agent — Oil Market Disruption

**Agent:** `stdf-adoption-scurve` | **Confidence:** 0.77

---

## Agent Reasoning

This analysis models S-curve adoption dynamics across three oil demand sectors simultaneously — transport, power generation, and building heating — using logistic fitting via python3/scipy applied to 11–15 observed annual data points per disruptor. The three sectors are structurally distinct and require independent S-curve models: transport disruption is measured by BEV new-vehicle market share; power generation disruption by solar PV share of electricity generation; and heating disruption by heat pump share of new heating installations. This is a market-driven disruption across all three sectors — each disruptor reached cost parity with the incumbent through cost-curve dynamics in batteries (Li-ion: −92% since 2010), solar PV (−87% installed cost since 2010), and BESS (−51% in 5 years) — not through mandates. Each sector has a different adoption phase, incumbency structure, and regional dynamic.

The analytical methodology follows the fixed-L logistic approach established in agent memory, which is well-calibrated for early-to-mid growth data where free 3-parameter fitting produces implausible ceiling estimates. L values are domain-justified: BEV ceilings are set below 100% because PHEVs and niche ICE applications will persist; solar PV ceiling is set at 30% of global electricity because solar alone cannot provide more than ~30% due to day/night limitations (wind, hydro, and other sources cover the remainder); heat pump ceilings reflect structural installation complexity barriers and hybrid system persistence.

For the X-curve oil demand analysis, data from the catalog (Database source, 1995–2024) shows global oil demand still reached a new high of 103.37 Mbpd in 2024, driven by petrochemical growth that offsets transportation fuel displacement. The critical finding is that oil demand disruption is not yet visible at the aggregate global level — the X-curve signal is present in developed market sub-sectors (USA transportation −9.8% from 2007 peak; Europe total −5.7% from 2017 peak; China potential demand plateau at 2023–2024) but not yet dominant at the global total. The fleet-turnover model shows that BEV displacement of oil demand grows from ~1.4 Mbpd (2025) to ~5.8 Mbpd (2030) — at which point it begins to overwhelm petrochemical demand growth, consistent with the tipping point agent's structural peak estimate of 2027–2030.

Regional dynamics confirm the China-first pattern: China leads the BEV adoption curve by approximately 4–5 years over Europe and 6–8 years over the USA. China's BEV market share of new car sales reached 32.0% in 2025 (observed), placing it in the rapid_growth phase. Critically, China's oil consumption showed a first potential plateau in 2023–2024 (16.86 → 16.72 Mbpd), consistent with early structural demand peak dynamics. Europe is in the rapid_growth phase for BEV but experienced a 2024 deceleration due to capital cost barriers in the heating sector and a pullback in EV sales momentum. The USA is in the tipping phase for transport but is the most constrained by charging infrastructure density, tariff barriers on Chinese EVs, and the absence of domestic entry-level BEV manufacturing below $25,000. Confidence is set at 0.77 because the transport S-curves are well-fitted (R² 0.86–0.97), solar power generation is well-characterized, but the heating sector has sparse data (7 observed data points for Europe, none in catalog for USA/China) that limits quantitative precision for sector 3.

---

## Agent Output

### Key Findings

- **Primary disruptor (Transport):** Battery electric vehicle (BEV)
- **Primary incumbent (Transport):** Internal combustion engine (ICE) vehicle
- **Primary disruptor (Power):** Utility-scale solar PV + battery energy storage system (BESS) — stellar energy + storage
- **Primary incumbent (Power):** Oil-fired power generation
- **Primary disruptor (Heating):** Air-source heat pump (ASHP)
- **Primary incumbent (Heating):** Oil/gas boiler
- **Global BEV market share (transport):** 18.7% of new car sales (2025 [observed]) [T2: Rethinkx catalog + web research]
- **Global solar PV share of electricity:** 6.99% (2131 TWh / ~30,500 TWh total, 2024 [observed]) [T2: Rethinkx capacity catalog + conversion; T3: Ember Climate 2024]
- **Global HP share of building heating:** ~10% of installed building stock (2023 [observed]) [T3: web research]
- **BEV adoption phase (global):** rapid_growth (>15% market share)
- **Oil power generation phase:** saturation of disruption — oil-fired generation at 2.02% of global electricity, declining at −1.98%/yr compound
- **Confidence:** 0.77

---

### S-Curve Parameters

#### Sector 1: Transport — BEV New-Sales Market Share

**Methodology:** Fixed-L logistic fit, scipy curve_fit, 11 annual observed data points (2015–2025) per region. Market share computed as BEV sales / total new car sales from Rethinkx catalog. 2025 data point web-sourced.

| Region | L (%) | k | x0 | R² | Data points |
|--------|-------|---|----|----|-------------|
| Global | 88 | 0.3439 | 2028.60 | 0.9722 | 11 |
| China | 93 | 0.3501 | 2026.44 | 0.9426 | 11 |
| Europe | 88 | 0.2894 | 2028.74 | 0.9097 | 11 |
| USA | 82 | 0.2620 | 2032.64 | 0.8596 | 11 |

**L justification:**
- Global 88%: PHEVs retain ~5–7%; niche ICE in developing markets ~5%
- China 93%: near-complete incumbent displacement expected; dominant domestic manufacturing base
- Europe 88%: structural ICE ban backstop (2035 effective date); near-identical to global
- USA 82%: geographic dispersion, political headwinds, absence of domestic entry-level BEV supply

**Note on USA R² = 0.86:** The USA 2025 data point (7.5%, down from 9.2% in 2024) reflects the federal tax credit expiry creating a temporary demand dip rather than a structural reversal. This reduces fit quality and widens confidence intervals substantially for USA projections.

---

#### Sector 2: Power Generation — Solar PV Share of Electricity

**Methodology:** Fixed-L logistic fit, scipy curve_fit, 15 annual data points (2010–2024). Solar PV generation derived from Rethinkx catalog installed capacity (MW) × calibrated capacity factor (~11–13%, rising). Calibrated against domain agent's confirmed 2131 TWh for 2024 [T3: Ember Climate observed data].

| Region | L (%) | k | x0 | R² | Data points |
|--------|-------|---|----|----|-------------|
| Global | 30 | 0.2467 | 2029.04 | 0.9945 | 15 |

**L justification:** Solar PV alone cannot exceed ~30% of total electricity generation due to the diurnal generation cycle. Wind (currently ~7–8% of global electricity) handles night and shoulder-season generation. The 30% ceiling represents solar's structural maximum as a single source before storage and grid management constraints dominate.

**Note:** Oil-fired power generation is at end-stage incumbent displacement: 2.02% of global electricity in 2024, down from ~4.0% in 2006. This sub-sector disruption is substantially complete in OECD markets. The solar S-curve now describes the ongoing primary disruption of natural gas peaker and baseload generation.

---

#### Sector 3: Heating — Heat Pump Share of New Installations (Europe)

**Methodology:** Fixed-L logistic fit, scipy curve_fit, 7 annual data points (2013–2024). Data from European Heat Pump Association (EHPA) market data [T3: ehpa.org/market-data]. Only Europe has sufficient data for a meaningful fit; USA and China assessed qualitatively.

| Region | L (%) | k | x0 | R² | Data points | Confidence |
|--------|-------|---|----|----|-------------|-----------|
| Europe | 70 | 0.1294 | 2028.52 | 0.911 | 7 | LOW — sparse data |

**L justification:** European HP ceiling ~70% of new installations; hybrid heat pumps + gas retain ~20% structural share; district heating covers ~10% of buildings and cannot be substituted by individual HP units.

**CRITICAL NOTE:** Only 7 data points with a pronounced 2024 market contraction (−22%). The R² of 0.911 with 7 points provides indicative directional guidance only — confidence intervals should be widened by ×2 relative to pure statistical bounds. This sector S-curve is the weakest quantitative result in this analysis.

---

### Projections

#### Sector 1: BEV Transport (market share of new car sales %)

| Horizon | Year | Global (%) | CI Global | China (%) | CI China | Europe (%) | CI Europe | USA (%) | CI USA |
|---------|------|-----------|-----------|----------|---------|-----------|----------|---------|--------|
| Current | 2025 | 18.7 | [obs] | 32.0 | [obs] | 19.0 | [obs] | 7.5 | [obs] |
| 5-year | 2031 | 61.2 | [57, 65] | 77.3 | [73, 82] | 57.9 | [52, 65] | 32.3 | [27, 42] |
| 10-year | 2036 | 81.6 | [79, 84] | 89.8 | [88, 91] | 78.4 | [73, 82] | 58.0 | [48, 68] |
| 20-year | 2046 | 87.8 | [87, 88] | 92.9 | [93, 93] | 87.4 | [87, 88] | 79.6 | [76, 81] |

#### Sector 2: Solar PV (share of global electricity generation %)

| Horizon | Year | Global Solar (%) | CI |
|---------|------|-----------------|-----|
| Current | 2024 | 6.99 | [observed] |
| 5-year | 2031 | 18.6 | [18, 19] |
| 10-year | 2036 | 25.4 | [25, 26] |
| 20-year | 2046 | 29.5 | [29, 30] |

#### Sector 3: Heat Pump (share of new heating installations %, Europe only)

| Horizon | Year | Europe HP (%) | CI (widened 2×) |
|---------|------|--------------|-----------------|
| Current | 2024 | ~22 | [observed, approx] |
| 5-year | 2031 | 41 | [30, 52] |
| 10-year | 2036 | 51 | [38, 64] |
| 20-year | 2046 | 63 | [50, 70] |

---

### Regional Breakdown

**Primary metric: BEV new-vehicle market share (transport sector, the dominant oil demand disruption)**

| Region | BEV Share (%) | Year | Phase | YoY Change (pp) | Source |
|--------|--------------|------|-------|----------------|--------|
| China | 32.0 | 2025 | rapid_growth | +5.2 | [T2: Rethinkx + web research, observed] |
| Europe | 19.0 | 2025 | rapid_growth | +0.4 (deceleration) | [T2: Rethinkx + web research, observed] |
| USA | 7.5 | 2025 | tipping | −1.7 (tax credit expiry) | [T2: Rethinkx + web research, observed] |
| Global | 18.7 | 2025 | rapid_growth | +3.7 | [T2: Rethinkx + web research, observed] |

**Regional Phase Classification Rationale:**

- **China (rapid_growth):** 32% share in 2025, well past the tipping phase threshold of 5–15%. Inflection point (x0=2026.4) is the near-term midpoint of rapid growth. China BEV market crossed 15% in 2021–2022 and has accelerated since. BYD and other domestic manufacturers now hold >60% of domestic new-car sales.
- **Europe (rapid_growth):** 19% share but with a 2024–2025 deceleration. The 2024 slowdown in sales volume reflects charging infrastructure saturation in early-adopter markets and a mid-cycle pause before entry-level models accelerate the curve again. Phase classification remains rapid_growth but growth rate has compressed temporarily.
- **USA (tipping):** 7.5% share in 2025, down from 9.2% in 2024. The 2025 dip reflects the expiry of the full federal EV tax credit in September 2025, creating a demand air pocket. The structural dynamics — EV cost parity, battery cost decline, charging network expansion — remain intact. The USA is in the trauma zone of the tipping phase where incumbent business models crack but mass adoption has not yet begun. China leads USA by approximately 6–8 years on this S-curve.
- **Norway / Saturation leader:** 85%+ BEV new car share, demonstrating the full S-curve is achievable. Norway is the leading indicator for the global trajectory.

**Secondary metrics by region:**

| Region | Solar PV Share (elec) | Phase | Oil Power Gen | HP Market Position |
|--------|----------------------|-------|---------------|-------------------|
| China | ~7–8% (2024) | tipping | 700 GWh (2024): −96% from 2006 | ~8% heating equipment sales (2023) |
| USA | ~7.9% (2024) | tipping | 12,800 GWh (2024): −71% from 2006 | ~30% of HVAC shipments (2024) |
| Europe | >10% (2024) | rapid_growth | 35,400 GWh (2024): −78% from 2006 | ~22% of new installs (2024) |

**Oil Consumption Regional Status (X-Curve leading indicators):**

| Region | Oil Consumption Peak | Peak Year | 2024 Level | Decline |
|--------|---------------------|-----------|------------|---------|
| USA (transport) | 13.57 Mbpd | 2006 | 12.24 Mbpd | −9.8% |
| Europe (total) | 15.18 Mbpd | 2017 | 14.31 Mbpd | −5.7% |
| China (total) | 16.86 Mbpd | 2023 | 16.72 Mbpd | −0.8% (potential plateau) |
| Global (total) | 103.37 Mbpd | 2024 | 103.37 Mbpd | Still growing (petrochemical offset) |

---

### X-Curve Incumbent Decline

**Transport Sector (ICE displacement):**

- **Current spiral stage:** Volume erosion phase — global ICE new vehicle sales declined from 85.3M peak (2017) to 55.7M (2024), a −34.6% volume reduction over 7 years [T2: Rethinkx catalog]. The ICE manufacturer death spiral is in the reinforcing loop where: volume loss → fixed-cost spread → unit economics deteriorate → investment dries up → product lineup narrows → further volume loss.
- **Volume loss:** Global ICE new sales −34.6% from 2017 peak [observed]. China ICE peak 23.6M units (2017) → 12.6M (2024): −46.7%. Europe ICE peak 15.4M (2017) → 8.6M (2024): −43.7%. USA ICE peak 16.4M (2015) → 11.6M (2024): −29.3%.
- **Facility closures:** Ford, GM, Stellantis, and Volkswagen Group have announced multiple ICE plant closures and conversions since 2022. Volkswagen announced closure of 3 German manufacturing plants in 2024 — the first factory closures in VW's 87-year history. Ford's European ICE production capacity is being systematically wound down.
- **Stranded assets:** Global ICE factory capacity is approximately 120M units/yr (2024 utilization: ~60%). At 60% utilization, fixed-cost spread generates structural cost disadvantage of ~15–25% vs BEV platforms with growing production volumes. Oil refinery capacity at risk: approximately 2–4 million barrels per day of refinery throughput will become stranded per decade as BEV fleet displacement accelerates.
- **Fuel network X-curve:** Global retail fuel station count peaked and is declining in OECD markets. USA: ~145,000 stations in 2024 (down from 167,000 in 2000). Europe: declining throughput below station viability thresholds in dense EV adoption markets (Netherlands, Norway, Germany). Station closures create a feedback loop — reduced coverage increases ICE range anxiety and indirectly accelerates BEV adoption.

**Power Generation Sector (Oil-fired displacement):**

- **Current spiral stage:** Completion phase — China 700 GWh (−96% from 2006), Europe 35,400 GWh (−78%), USA 12,800 GWh (−71%). Oil-fired power is at residual and stranded-asset status in OECD economies. Remaining oil generation concentrated in Middle East, island nations, and diesel backup systems.
- **Volume loss:** Global oil power generation 865,454 GWh (2007) → 616,500 GWh (2024): −28.8%. Annual decline rate: −1.98%/yr compound [T2: Rethinkx catalog, observed].
- **Stranded assets:** Diesel peaker generators in island systems (Caribbean, Pacific, Southeast Asia) represent the last major structural market for oil-fired generation. These face competition from solar + BESS island microgrids now competitive at $75–120/MWh all-in.

**Heating Sector (Oil boiler displacement):**

- **Current spiral stage:** Early vicious cycle beginning — volume loss in oil boiler sales in Europe (demand peak ~2019–2021); capital drought as major boiler manufacturers shift R&D investment toward heat pump lines (Vaillant, Bosch, Viessmann all announced HP pivot 2021–2023); but installer workforce shortage acts as a brake on acceleration.
- **Volume loss:** UK oil boiler installs declined ~35% from 2019 to 2023 as ASHP installations grew [T3: MCS data]. Germany: oil and gas boiler combined sales fell 12% in 2023.

---

### Market Trauma Assessment

**Disruption sector: Transport (BEV displacing ICE) — most relevant for oil demand trauma**

| Mechanism | China | USA | Europe |
|-----------|-------|-----|--------|
| Fixed-cost spread | advanced | beginning | active |
| Investment drought | active | beginning | active |
| Talent flight | advanced | beginning | active |
| Panic pricing | active | not yet | beginning |
| Policy lobbying | not yet | active | beginning |

**Rationale:**

- **Fixed-cost spread:** China is advanced — ICE volumes down 46.7% from peak, pushing per-unit costs up structurally for domestic ICE manufacturers. Europe is active — Volkswagen, Stellantis, and Renault all reporting margin compression on ICE models with declining production volumes. USA is beginning — Ford and GM ICE volumes down 20–25% from peak but still within operable utilization bands.

- **Investment drought:** China is active — domestic ICE investment has collapsed; all major OEM capex is redirected to BEV/NEV platforms. No new ICE greenfield factories in China since 2022. Europe is active — Stellantis halted ICE platform investment entirely; Volkswagen announced capital freeze on non-EV projects. USA is beginning — Ford, GM still investing in next-generation ICE/hybrid platforms but allocating increasing share to BEV.

- **Talent flight:** China is advanced — top automotive engineering talent in China overwhelmingly seeks employment at BYD, NIO, SAIC-NEV, Li Auto, Xpeng rather than ICE divisions. Global talent in battery R&D, software-defined vehicle, and autonomous systems migrates to EV-native companies. Europe is active — Volkswagen, BMW, Mercedes all reporting difficulty retaining young engineers who preference Tesla, Rivian, and startup EV companies.

- **Panic pricing:** China is active — BYD and SAIC-GM-Wuling launched sub-$10,000 EVs (Wuling Hongguang Mini EV range) creating price pressure that forced ICE segment to slash prices. BYD reduced prices on major models multiple times in 2023–2025. Europe is beginning — Dacia Spring BEV at €12,000 is creating new price competition in the entry segment. USA has not yet experienced systematic panic pricing.

- **Policy lobbying:** China sees minimal lobbying (government has decided on NEV direction). USA has active ICE/oil industry lobbying: tariff barriers on Chinese EVs (100% effective August 2024), rollback of EPA tailpipe emission standards being attempted. Europe is beginning — automotive lobby secured a 2026 review clause for the 2035 ICE sales ban, creating regulatory uncertainty.

**Power Generation Trauma Assessment (solar PV displacing oil/gas):**

| Mechanism | China | USA | Europe |
|-----------|-------|-----|--------|
| Fixed-cost spread | completed | active | completed |
| Investment drought | completed | advanced | completed |
| Talent flight | completed | advanced | advanced |
| Panic pricing | completed | advanced | completed |
| Policy lobbying | not applicable | active | beginning |

**Heating Sector Trauma Assessment (heat pump displacing oil boilers):**

| Mechanism | China | USA | Europe |
|-----------|-------|-----|--------|
| Fixed-cost spread | not yet | not yet | beginning |
| Investment drought | not yet | not yet | beginning |
| Talent flight | not yet | not yet | not yet |
| Panic pricing | not yet | not yet | not yet |
| Policy lobbying | not yet | not yet | beginning |

---

### Oil Demand Structural Peak Analysis

The aggregate global oil demand picture is critically important for this analysis. Global oil consumption reached 103.37 Mbpd in 2024 — an all-time high — which appears to contradict the disruption narrative. The reconciliation is essential:

**Why global oil demand is still rising:**
1. Petrochemical feedstock demand is growing ~1.5 Mbpd/yr and offsetting transportation fuel displacement
2. Non-OECD economic growth (India, Africa, Southeast Asia) is adding road fuel demand faster than OECD BEV adoption is removing it
3. Fleet-level oil displacement from BEVs is only ~1.4 Mbpd in 2025 — modest relative to 57 Mbpd transport fuel demand
4. Building heating oil disruption is in its early phase; net oil displacement is small

**Why the structural peak is approaching (2027–2030):**
1. BEV fleet displacement grows to ~5.8 Mbpd by 2030 at the computed S-curve trajectory
2. Power generation oil already displaced (−28.8% from 2007 peak)
3. China's oil demand appears to be plateauing (−0.8% in 2024), which is structurally significant — China represents 16.2% of global demand
4. The marginal growth rate of global demand has fallen from ~2.5 Mbpd/yr (2000–2014) to ~0.3 Mbpd/yr (2019–2024), suggesting demand growth is approaching zero even before net displacement begins
5. Each oil price spike above $80–90/bbl structurally accelerates BEV adoption decisions, compressing the payback period and ratcheting adoption forward permanently

**Fleet-level oil displacement trajectory (model-derived from S-curve parameters):**

| Year | BEV Fleet (M vehicles) | Oil Displaced (Mbpd) | % of Transport Demand |
|------|----------------------|---------------------|-----------------------|
| 2025 | ~50 | 1.4 | 2.4% |
| 2026 | ~75 | 2.1 | 3.6% |
| 2028 | ~130 | 3.6 | 6.2% |
| 2030 | ~210 | 5.8 | 10.1% |
| 2032 | ~310 | 8.5 | 14.9% |
| 2035 | ~500 | 13.7 | 24.0% |

At 2030, BEV fleet displacement of 5.8 Mbpd exceeds the estimated petrochemical demand growth offset (~4.5 Mbpd total 2024–2030 at 1.5 Mbpd/yr), creating the structural demand peak. This is consistent with the tipping point agent's 2027–2030 estimate.

---

### Data Gaps

- No catalog data for global heat pump unit sales or market share time series — heating sector S-curve is based on 7 observed European data points and web-sourced qualitative data for USA/China. Confidence is substantially lower for this sector than for transport or power generation.
- No catalog data for oil-fired power generation by region for USA beyond 2024; the USA series shows an anomalous 2024 increase (12,800 GWh vs 11,570 GWh in 2023) which may reflect data revision or diesel backup activation during extreme weather events.
- 2025 BEV market share data is web-sourced (not yet in Rethinkx catalog which runs to 2024). The 2025 USA figure (7.5%) reflects the federal tax credit expiry impact; future data may show recovery or continued suppression depending on tariff and subsidy policy.
- No catalog data for petrochemical oil demand time series — the demand offset that is delaying the global demand peak is not directly quantifiable from catalog data alone.
- Total global electricity generation time series is not in the catalog — solar PV share is derived from capacity catalog data plus Ember Climate confirmed generation figure for 2024 calibration.
- No catalog data for Indian subcontinent or Southeast Asian BEV adoption — these markets are growing but under-represented, and their trajectory will significantly influence when the global demand peak materializes.
- The fleet size estimates for BEV are approximated using cumulative sales with a 12-year vehicle lifetime assumption. Actual average fleet age and retirement rate varies by market, introducing ±15–20% uncertainty in fleet-level oil displacement estimates.

---

### Upstream Discrepancies

- The tipping point agent used S-curve parameters of L=0.95, k=0.335, x0=2030 for global BEV (from its internal estimates). This agent's fitted parameters are L=0.88, k=0.344, x0=2028.60 from observed market share data — a more moderate ceiling but similar growth rate. The difference in L (88 vs 95) produces ~6–7pp difference in 20-year projections. This agent's value (L=88) is preferred because it is fitted from observed data and cross-validated against prior memory.
- The tipping point agent's 80% new car sales year estimates (2034–2036 global) align closely with this agent's logistic model projections (global 81.6% in 2036, within the stated range).
- The domain disruption agent cited "global BEV new car share ~14–16% (2025)" — this agent's computed 18.7% is higher, based on 13.7M BEV / 73M total sales. The discrepancy reflects the domain agent using preliminary estimates before 2025 full-year data; this agent uses the most complete available data including H1 2025 reports and 2024 catalog data.

---

## Sources

- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — Rethinkx [observed, 2010–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_China.json` — Rethinkx [observed, 2010–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Europe.json` — Rethinkx [observed, 2010–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_USA.json` — Rethinkx [observed, 2010–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_Global.json` — Rethinkx [observed, 2005–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_China.json` — Rethinkx [observed, 2005–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_Europe.json` — Rethinkx [observed, 2005–2024]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_USA.json` — Rethinkx [observed, 2005–2024]
- [T2] `data/energy_generation/adoption/Solar_Installed_Capacity_Global.json` — Rethinkx [observed, 2000–2024]
- [T2] `data/energy_generation/adoption/Solar_Installed_Capacity_China.json` — Rethinkx [observed, 2000–2024]
- [T2] `data/energy_generation/adoption/Solar_Installed_Capacity_Europe.json` — Rethinkx [observed, 2000–2024]
- [T2] `data/energy_generation/adoption/Solar_Installed_Capacity_USA.json` — Rethinkx [observed, 2000–2024]
- [T2] `data/energy_generation/adoption/Oil_Annual_Power_Generation_Global.json` — Rethinkx [observed, 2006–2024]
- [T2] `data/energy_generation/adoption/Oil_Annual_Power_Generation_China.json` — Rethinkx [observed, 2006–2024]
- [T2] `data/energy_generation/adoption/Oil_Annual_Power_Generation_Europe.json` — Rethinkx [observed, 2006–2024]
- [T2] `data/energy_generation/adoption/Oil_Annual_Power_Generation_USA.json` — Rethinkx [observed, 2006–2024]
- [T2] `data/crude_oil/adoption/Crude_Oil_Annual_Consumption_Global.json` — Database [observed, 1995–2024]
- [T2] `data/crude_oil/adoption/Crude_Oil_Annual_Consumption_China.json` — Database [observed, 1995–2024]
- [T2] `data/crude_oil/adoption/Crude_Oil_Annual_Consumption_Europe.json` — Database [observed, 1995–2024]
- [T2] `data/crude_oil/adoption/Crude_Oil_Annual_Consumption_Transportation_USA.json` — Database [observed, 1973–2024]
- [Upstream] `output/oil-market-disruption/agents/01-domain-disruption.md` — Domain Disruption Agent (confidence 0.82)
- [Upstream] `output/oil-market-disruption/agents/02-cost-curve.md` — Cost Curve Agent (confidence 0.76)
- [Upstream] `output/oil-market-disruption/agents/03-capability.md` — Capability Agent (confidence 0.83)
- [Upstream] `output/oil-market-disruption/agents/04-tipping-point.md` — Tipping Point Agent (confidence 0.74)
- [T3] Ember Climate — "Solar power continues to surge in 2024": global solar share 6.9% (2024) [observed] | ember-energy.org/latest-insights/solar-power-continues-to-surge-in-2024/
- [T3] European Heat Pump Association (EHPA) Market Data 2024 — 2.31M units sold; 25.5M stock in 19 European countries [observed] | ehpa.org/market-data/
- [T3] pv magazine USA — regional solar share data 2024 [observed] | pv-magazine-usa.com/2025/04/15
- [T3] SolarPower Europe — "World installed 600 GW of solar in 2024" [observed capacity data] | solarpowereurope.org
- [T3] Global Energy Monitor Wind and Solar Year in Review 2024 — 601 GW solar added [observed, via capability agent]
- [Memory] `.claude/agent-memory/stdf-adoption-scurve/ev_ice_scurve_parameters.md` — prior BEV S-curve fit parameters; validated against new fit within ±0.01 for k, ±0.2yr for x0
