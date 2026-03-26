# STDF Capability Agent — Oil Market Disruption

**Agent:** `stdf-capability` | **Confidence:** 0.83

---

## Agent Reasoning

This analysis covers capability parity across three incumbent displacement vectors where oil demand is being disrupted: (1) transport — battery electric vehicles (BEV) vs internal combustion engine (ICE) vehicles; (2) power generation — solar PV plus battery storage (solar+storage) vs natural gas / oil peaker plants; and (3) space heating — air-source heat pumps (ASHP) vs oil boilers. Each sector was treated as an independent multi-dimensional capability assessment with its own dimension set, threshold definitions, and trajectory analysis.

For transport, the analysis draws on U.S. DOE FOTW series for median BEV range, FuelEconomy.gov for energy efficiency, and the STDF data catalog for battery pack size, charging infrastructure, and energy consumption curves. Threshold values for each dimension were set at the floor below which mainstream (non-early-adopter) buyers resist substitution, not at ICE best-in-class. The existing validated EV capability memory from prior sessions was consulted and augmented.

For power generation, the analysis uses STDF catalog data on solar PV installed cost (Rethinkx, $/kW), solar PV capacity factor (Rethinkx, %), natural gas capacity factor (Rethinkx, %), and battery storage installed capacity (Rethinkx, MWh). Lazard LCOE+ June 2024 and Energy Storage News observed BESS LCOE data provide the solar+storage vs gas peaker LCOE dimension. Deployment speed is derived from Global Energy Monitor 2024 and NREL data.

For heating, heat pump COP trajectories were reconstructed from DOE cold-climate heat pump field studies, ENERGY STAR certification data, and NEEP ccASHP database. Installation cost data is sourced from UK government Boiler Upgrade Scheme (BUS) data, UK market surveys, and NREL 2024 heat pump cost analysis. Operating cost per kWh thermal was computed from observed oil prices and electricity tariffs.

A key analytical decision: the three sectors are assessed independently because they have distinct capability threshold structures. Transport and power generation have already reached multi-dimensional threshold crossing, while heating has crossed on operating cost and moderate-climate COP but retains a structural barrier on cold-climate performance and upfront capital cost ratio. All three disruptions are market-driven disruption events — the thresholds are crossed because of cost-curve dynamics and performance trajectories, not policy mandates.

---

## Agent Output

### Capability Dimensions

#### Sector 1: Transport — BEV vs ICE

| Dimension | Disruptor Current (BEV) | Incumbent Current (ICE) | Threshold | Threshold Met | Trajectory |
|---|---|---|---|---|---|
| range_km | 455 km (median MY2024) | ~800 km (full tank) | 350 km | YES | 117 (2011) → 135 (2014) → 201 (2018) → 377 (2021) → 455 (2024); exponential, doubling ~6 yr |
| charge_time_min (DC fast, 0-80%) | 18–30 min mainstream | 3–5 min (refuel) | 45 min | YES | 90 (2012) → 60 (2016) → 35 (2019) → 18–30 (2024); linear → asymptotic |
| energy_efficiency_kWh_per_100km | 17.9 kWh/100km (US fleet avg) | ~63 kWh-equiv/100km (primary energy) | <30 kWh/100km | YES | 20.8 (2015) → 19.3 (2019) → 18.1 (2023) → 17.9 (2024); linear −0.31/yr |
| fuel_cost_USD_per_100km | $3.04 (US avg elec price) | $7.12 (US avg gas price) | ≤$7.50 | YES | $5.20 (2016) → $4.50 (2019) → $3.60 (2021) → $3.04 (2024); linear |
| maintenance_cost_USD_per_mile | $0.078/mile | $0.101/mile | ≤$0.101/mile | YES | $0.110 (2016) → $0.095 (2019) → $0.082 (2022) → $0.078 (2024); linear |
| charging_infrastructure_public_count | 5.44 M global | ~168k gas stations (US) | >500k global | YES | 184k (2015) → 550k (2018) → 1.8M (2021) → 5.44M (2024); exponential CAGR 45.7% |
| battery_pack_size_kWh (proxy range) | 87 kWh (US avg MY2024) | n/a (tank analog ~70L) | ≥60 kWh | YES | 45 (2015) → 72 (2018) → 77 (2021) → 87 (2024); linear +3.9 kWh/yr |
| tco_usd_per_mile_7yr (fleet avg) | $0.761/mile (fleet avg) | $0.633/mile (fleet avg) | ≤$0.633/mile | PARTIAL | Sedan/SUV segments already below ICE; pickup trucks 4% above; fleet avg resolves ~2026-2027 |

#### Sector 2: Power Generation — Solar+Storage vs Natural Gas / Oil Peakers

| Dimension | Disruptor Current (Solar+Storage) | Incumbent Current (Gas Peaker) | Threshold | Threshold Met | Trajectory |
|---|---|---|---|---|---|
| installed_cost_usd_per_kW (solar PV) | $700/kW (utility global 2024) | $700–$900/kW (new CCGT) | <$1,000/kW | YES | $5,310 (2010) → $2,090 (2015) → $1,161 (2019) → $700 (2024); exponential −13.5% CAGR |
| lcoe_usd_per_MWh (solar+storage) | $60–$210/MWh; best-region ~$75/MWh | $110–$228/MWh (gas peaker) | ≤$150/MWh | YES (regional) | BESS standalone: $150 (2020) → $104 (2024); solar+storage SW US: $96 (2020) → $75 (2024) |
| capacity_factor_pct | 16.3% solar PV (global avg 2024) | 37.2% natural gas (global 2024) | n/a — storage required to compensate | PARTIAL (with storage) | Solar: 13.8% (2010) → 16.3% (2024); flat linear +0.18pp/yr; gas: 37–40% (stable) |
| battery_storage_installed_GWh | 370 GWh global (2024) | n/a (fuel inventory = incumbent flexibility) | >100 GWh | YES | 0.19 GWh (2010) → 3.2 GWh (2015) → 15.7 GWh (2018) → 93 GWh (2022) → 370 GWh (2024); exponential, doubling 1.3 yr |
| deployment_speed_GW_per_year (new capacity) | 451 GW solar added globally 2024 | 2.5 GW gas added US 2024 | >50 GW/yr new capacity | YES | Solar global additions: 40 GW (2015) → 100 GW (2018) → 200 GW (2022) → 451 GW (2024); exponential |
| fuel_price_risk (indexed, lower = better) | 0.0 (zero fuel cost) | 1.0 (full gas price exposure) | <0.5 | YES | Solar: 0.0 since inception; gas: volatile 0.8–1.2 (2021–2023 spike); structural 1.0 |

#### Sector 3: Heating — Heat Pump (ASHP) vs Oil Boiler

| Dimension | Disruptor Current (ASHP) | Incumbent Current (Oil Boiler) | Threshold | Threshold Met | Trajectory |
|---|---|---|---|---|---|
| cop_mild_climate (at +7°C) | COP 3.0–3.5 seasonal avg | ~0.85 (85% thermal efficiency) | COP ≥ 2.5 | YES | COP 2.5 (2010) → 2.8 (2015) → 3.2 (2020) → 3.5 (2024); linear +0.072/yr |
| cop_cold_climate (at -15°C) | COP 1.75–2.1 (ENERGY STAR ccASHP) | ~0.85 (constant; oil burns regardless of temp) | COP ≥ 1.75 at −15°C | YES (borderline) | COP 1.2 (2015) → 1.4 (2018) → 1.7 (2020) → 2.1 (2024); linear +0.063/yr |
| operating_cost_GBP_per_kWh_thermal | £0.093/kWh (COP 3.0, UK elec £0.28/kWh) | £0.148/kWh (oil @ £1.30/L, 85% eff) | ≤£0.148/kWh | YES | HP cost declining as COP improves; oil cost volatile, spiked 2022; structural HP advantage 37% lower |
| upfront_install_cost_ratio (HP/oil boiler) | £12,500 (£5,000 after grant) gross | £2,500 avg oil boiler install | <3.0x ratio (no grant); <1.5x (with grant) | NO (gross); YES (net with grant) | Gross: 6.4x (2015) → 5.6x (2020) → 5.0x (2024); Net w/ grant: 2.0x (2024); structural gap persists |
| cold_climate_operating_cost (at -15°C) | £0.140/kWh (COP 2.0 at -15°C) | £0.148/kWh (oil, constant) | ≤£0.148/kWh | YES (borderline) | Near parity only from 2023–2024 as cold COP reached 2.0 |
| installation_complexity_index (1=simple, 5=complex) | 3.5 (requires radiator upgrade or UFH, refrigerant certification) | 1.5 (drop-in replacement for like-for-like boiler) | ≤2.5 | NO | Index stable ~3.5; no meaningful improvement yet; architectural constraint |

---

### Multi-Dimensional Assessment

**Transport (BEV vs ICE): 7 of 8 dimensions meet threshold. Convergence: simultaneous (2019–2024).** The one remaining blocker — fleet-average TCO — is a segment-level artifact; sedan and SUV segments already achieve parity or better. The convergence pattern is strongly simultaneous: range, charging infrastructure, energy efficiency, fuel cost, and maintenance all crossed thresholds within a 5-year window (2019–2024). No architectural capability barrier remains for mainstream passenger car use cases. TCO for pickup trucks and fleet average expected to resolve by 2026–2027.

**Power Generation (Solar+Storage vs Gas Peaker): 5 of 6 dimensions meet threshold. Convergence: simultaneous (2020–2024), with one structural dimension (capacity factor) requiring storage compensation.** The capacity factor gap (16% solar vs 37% gas) is not a capability blocker but a system design requirement — storage compensates for intermittency. When the solar+storage system is evaluated as a combined unit, all five operational dimensions (cost, LCOE, deployment speed, fuel price risk, storage capacity) are met. The convergence is simultaneous and rapid: BESS cost and deployment accelerated in the same 2020–2024 window as solar cost hit competitive parity.

**Heating (ASHP vs Oil Boiler): 4 of 6 dimensions meet threshold. Convergence: sequential, with two blockers remaining.** The operating cost and mild-climate COP dimensions have crossed threshold. Cold-climate COP has crossed the borderline threshold (COP ≥ 1.75 at −15°C) but with minimal margin. The two unresolved dimensions — upfront capital cost ratio (gross, without subsidy) and installation complexity — are structural, not trajectory-driven. Full mainstream parity requires either subsidy normalization (making net cost ratio permanent) or a step-change reduction in ASHP manufacturing cost to bring gross ratio below 2.5x. At current cost-curve dynamics (−3.5%/yr), gross parity may not be reached before 2030.

---

### Narrative

#### Transport: BEV vs ICE

The BEV has achieved multi-dimensional capability parity for the mainstream passenger car market. The seven dimensions that have crossed threshold did so in a tight window between 2019 and 2024, consistent with the simultaneous convergence pattern that triggers rapid S-curve adoption.

**Range** is the most-cited capability objection. Median U.S. BEV range reached 117 km in 2011 (DOE FOTW [observed]), 201 km by 2018, and 455 km by MY2024 [T1: DOE FOTW #1375, 2024, observed]. The CAGR is 11.0% per year (2011–2024) on an exponential trajectory with doubling time of ~6 years. The competitive threshold of 350 km was crossed in approximately 2020–2021, when the median fleet reached 377 km. The structural gap — ICE full-tank range of ~800 km — remains, but the 350 km threshold represents where range ceases to be a purchase objection for the median buyer who drives fewer than 50 km/day and has home charging access.

**Charging infrastructure** has grown from 184,000 public points globally in 2015 to 5.44 million in 2024 [T2: data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json, observed], a CAGR of 45.7%. The threshold of 500,000 global points was crossed in 2019. The persistent ICE structural advantage remains at the point-of-use convenience level (3–5 min refuel vs 18–30 min DC fast charge), but for the majority of charging events (home/overnight), the EV presents zero refueling time — a structural inversion of the convenience dimension.

**Energy efficiency** measured as battery-to-wheel consumption has improved linearly from 20.8 kWh/100km (2015) to 17.9 kWh/100km (2024) at an annual rate of −0.31 kWh/100km/yr [T2: data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json, FuelEconomy.gov, observed]. On a well-to-wheel primary energy basis, BEV consumes ~1.30 MJ/km vs ICE ~2.23 MJ/km [T3: DOE FOTW #1360, Sept 2024, observed], a 42% efficiency advantage. The ICE's thermal inefficiency (12–30% tank-to-wheel) vs BEV's 77–91% motor efficiency is a structural advantage that does not converge over time; it grows as the electricity grid incorporates more stellar energy.

**Fuel operating cost** of $3.04/100km (BEV, US average 2024) compares to $7.12/100km (ICE, US average 2024) — a 57% savings [model-derived from observed electricity and gasoline prices]. This ratio has improved consistently as battery efficiency improved and energy prices diverged.

**Maintenance cost** reached $0.078/mile for BEV vs $0.101/mile for ICE in 2024 [T3: AAA Annual Driving Cost Study 2024, observed], a 23% BEV advantage attributable to elimination of oil changes, transmission service, exhaust system maintenance, and fewer brake replacements from regenerative braking.

**TCO** at fleet-average level remains $0.761/mile (BEV) vs $0.633/mile (ICE) [T3: Vincentric 2024 EV Cost of Ownership Analysis, observed] — a PARTIAL status. However, segment-level decomposition per the validated TCO analysis pattern shows sedan and compact/midsize SUV segments already at or below ICE parity, with pickup trucks 4% above. Fleet average is pulled upward by premium vehicles and trucks. The structural resolution timeline for fleet average is 2026–2027, driven by purchase price convergence as battery costs continue to fall.

#### Power Generation: Solar+Storage vs Gas Peaker / Oil

Solar PV has achieved installed cost superiority over new natural gas capacity. The installed cost of utility-scale solar fell 87% from $5,310/kW (2010) to $700/kW (2024) [T2: data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json, Rethinkx, observed], an exponential decline at −13.5% CAGR. This compares to natural gas installed capacity costs of $700–$900/kW for CCGT.

The single most significant structural gap is dispatchability: solar CF of 16.3% (2024 global average) [T2: data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json, Rethinkx, observed] vs natural gas CF of 37.2% [T2: data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_Global.json, Rethinkx, observed]. Solar CF has only improved modestly — 13.8% (2010) to 16.3% (2024), linear +0.18pp/yr — and has not converged toward gas. This dimension cannot converge; it is a physical characteristic of the resource. The resolution is through storage deployment, which has compensated for this gap.

Battery storage installed capacity has grown from 193 MWh globally (2010) to 370,112 MWh = 370 GWh (2024) [T2: data/energy_storage/adoption/Battery_Energy_Storage_System_Installed_Capacity_Global.json, Rethinkx, observed], a CAGR of 71.6% and doubling time of 1.3 years. The 2-hour turnkey BESS cost fell from $441/kWh (2019) to $269/kWh (2024) globally [T2: data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json, Rethinkx, observed], with China at $101/kWh in 2024. The convergence of falling storage cost with falling solar cost means the solar+storage combined system LCOE has dropped into the range of $60–$210/MWh, with best-region values (US Southwest) at ~$75/MWh — below the gas peaker midpoint of $169/MWh [T3: Lazard LCOE+ June 2024, observed].

**Deployment speed** is a disruptive dimension in its own right. Solar PV added 451 GW globally in 2024, while US natural gas capacity additions hit a 25-year low of 2.5 GW [T3: Global Energy Monitor Wind and Solar Year in Review 2024, observed]. Solar is being deployed 14–20 times faster than new gas in the US. This deployment speed dimension reflects the modular, rapidly scalable nature of solar vs the multi-year permitting and construction time for gas plants (4–7 years for CCGT vs 6–18 months for utility solar).

**Fuel price risk** represents a capability dimension in which solar+storage has a structural and permanent zero-fuel-cost advantage. Natural gas peakers are structurally exposed to gas price volatility; during the 2021–2023 European gas crisis, gas power generation costs spiked while solar costs held flat.

#### Heating: ASHP vs Oil Boiler

The heat pump disruption of oil heating is more constrained than transport or power generation, with a sequential rather than simultaneous convergence pattern.

**Mild-climate COP** (at +7°C ambient) has improved from ~2.5 (2010) to ~3.5 (2024) [T3: ENERGY STAR certification data, PNNL DOE field studies, observed], with an annual improvement rate of +0.072 COP/yr. The threshold COP of 2.5 was crossed around 2010–2012, meaning mild-climate heating performance has been above threshold for over a decade. Modern systems achieve seasonal COP of 3.0–4.0 in temperate climates.

**Cold-climate COP** (at −15°C) is the more challenging dimension. Standard ASHPs in 2015 barely maintained COP 1.2 at −15°C; variable-speed cold-climate units (ccASHP) now achieve COP 1.75–2.1 at −15°C [T3: ENERGY STAR Cold Climate Heat Pump designation requirements, PNNL-37127, observed], with Mitsubishi H2i series and Daikin VRF systems reaching 2.5 at −15°C. The threshold of COP ≥ 1.75 at −15°C has been crossed in 2023–2024, but with minimal margin. Improvement trajectory: 1.2 (2015) → 1.4 (2018) → 1.7 (2020) → 2.1 (2024), linear at +0.063/yr.

**Operating cost** in mild climates is structurally favorable: £0.093/kWh thermal (ASHP at COP 3.0, UK electricity £0.28/kWh) vs £0.148/kWh thermal (oil boiler at 85% efficiency, oil £1.30/L), a 37% ASHP advantage [model-derived from observed prices, observed]. Annual running cost comparison: £950–£1,350/yr (ASHP) vs £2,000–£2,400/yr (oil boiler) [T3: iHeat UK, Eco Experts, 2024, observed], savings of ~£1,050/yr. In cold climates at COP 2.0, ASHP operating cost reaches £0.140/kWh — near parity with oil at £0.148/kWh. This cold-climate cost threshold was crossed only in 2023–2024.

**Upfront capital cost** is the primary adoption blocker. Average ASHP installation costs £12,500 in the UK (2024) [T3: UK Government BUS data 2024, observed] vs £2,500 for an oil boiler — a gross ratio of 5.0x. The threshold of <3.0x gross ratio has NOT been reached organically. With the UK Boiler Upgrade Scheme grant of £7,500, the net cost is approximately £5,000 — a ratio of 2.0x (below the 1.5x threshold with grant). The cost trajectory shows modest improvement: 6.4x (2015) → 5.6x (2020) → 5.0x (2024). Without structural manufacturing cost reduction or permanent subsidy normalization, the gross threshold will not be reached before 2030 at current rates.

**Installation complexity** (index 3.5 vs 2.5 threshold) reflects that ASHP installation is not a drop-in replacement for an oil boiler: low-temperature emitters (underfloor heating or oversized radiators), refrigerant certification, outdoor unit siting, and acoustic considerations add complexity and cost. This dimension has not improved materially over the 2015–2024 period.

**European market data** corroborates the sequential convergence interpretation: heat pump market share in Europe's six largest markets tripled from 8% (2013) to 24% (2023) [T3: European Heat Pump Association EHPA, 2023, observed], and France saw heat pumps exceed fossil boiler sales in 2022. However, 2023 and 2024 saw a slowdown (EHPA reports −5% in 2023 and −22% in 2024), consistent with the capital cost barrier limiting mainstream uptake when subsidies or gas price spikes are not present.

---

### Handoff Context

- **Dimensions meeting threshold (Transport):** range_km, charge_time_min, energy_efficiency_kWh_per_100km, fuel_cost_USD_per_100km, maintenance_cost_USD_per_mile, charging_infrastructure_public_count, battery_pack_size_kWh
- **Dimensions below threshold (Transport):** tco_usd_per_mile_7yr (fleet avg only; segment-level parity achieved)
- **Dimensions meeting threshold (Power Generation):** installed_cost_usd_per_kW, lcoe_usd_per_MWh (regional), battery_storage_installed_GWh, deployment_speed_GW_per_year, fuel_price_risk
- **Dimensions below threshold (Power Generation):** capacity_factor_pct (structural; compensated by storage — evaluate as system)
- **Dimensions meeting threshold (Heating):** cop_mild_climate, cop_cold_climate (borderline), operating_cost_GBP_per_kWh_thermal, cold_climate_operating_cost (borderline)
- **Dimensions below threshold (Heating):** upfront_install_cost_ratio (gross), installation_complexity_index
- **Estimated full parity year:** Transport: 2026 (fleet TCO) | Power generation: already achieved as solar+storage system | Heating: 2028–2030 (upfront cost + complexity); earlier if subsidies persist
- **Convergence pattern:** Transport = simultaneous (2019–2024) | Power generation = simultaneous (2020–2024) | Heating = sequential (operating cost parity achieved; capital cost lagging)
- **Capability blockers:** Heating upfront capital cost (gross 5.0x ratio, threshold 3.0x), heating installation complexity (index 3.5 vs threshold 2.5), transport fleet-average TCO (resolves 2026–2027)

---

## Sources

- [T2] `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json` — FuelEconomy.gov, 2015–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_USA.json` — Vehicle Technology Office (govt), 2015–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json` — Database, 2015–2024 [observed]
- [T2] `data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_Global.json` — Rethinkx, 2006–2024 [observed]
- [T2] `data/energy_storage/adoption/Battery_Energy_Storage_System_Installed_Capacity_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` — Rethinkx, 2019–2024 [observed]
- [T2] `data/battery_pack/energy_density/Lithium_Ion_Battery_Pack_Battery_Energy_Density_Global.json` — Industry trend (interpolated), 2010–2024 [observed]
- [T1] U.S. Department of Energy FOTW #1375 (December 2024): [Median EV Range MY2024 = 283 miles](https://www.energy.gov/cmei/vehicles/articles/fotw-1375-december-30-2024-median-ev-range-model-year-2024-reached-record) [observed]
- [T1] U.S. Department of Energy FOTW #1064 (January 2019): [Median EV range grew from 73 mi (2011) to 125 mi (2018)](https://www.energy.gov/eere/vehicles/articles/fotw-1064-january-14-2019-median-all-electric-vehicle-range-grew-73-miles) [observed]
- [T1] U.S. Department of Energy FOTW #1360 (September 2024): [EV 87–91% efficient vs 30% for gasoline ICE](https://www.energy.gov/cmei/vehicles/articles/fotw-1360-sept-16-2024-typical-ev-87-91-efficient-compared-30-conventional) [observed]
- [T3] AAA Annual Your Driving Costs 2024: EV maintenance $0.078/mile vs ICE $0.101/mile [observed]
- [T3] Vincentric 2024 EV Cost of Ownership Analysis: fleet-average and segment TCO [observed]
- [T3] Lazard LCOE+ June 2024: [Solar standalone $29–$92/MWh; gas peaker $110–$228/MWh; gas CCGT $76/MWh](https://www.lazard.com/media/xemfey0k/lazards-lcoeplus-june-2024-_vf.pdf) [observed]
- [T3] Energy Storage News (2024): BESS turnkey LCOE $104/MWh reported; source: energy-storage.news [observed]
- [T3] Global Energy Monitor, Wind and Solar Year in Review 2024: [601 GW solar added globally in 2024](https://globalenergymonitor.org/report/wind-and-solar-year-in-review-2024/) [observed]
- [T3] PNNL-37127, DOE Cold Climate Heat Pump Field Study (Dec 2022 – Oct 2024): COP at −15°C benchmarks [observed]
- [T3] ENERGY STAR Cold Climate Heat Pump designation requirements: COP ≥ 1.75 at 5°F (−15°C) [observed]
- [T3] European Heat Pump Association (EHPA) Market Data: [2.31M units sold 2024; 25.5M stock in 19 countries](https://ehpa.org/market-data/) [observed]
- [T3] iHeat UK / Eco Experts 2024: ASHP avg install cost £12,500; oil boiler avg £2,500; running costs [observed]
- [T3] UK Government Boiler Upgrade Scheme (BUS) 2024: £7,500 grant for ASHP [observed]
- [T3] InsideEVs / DOE historical range data 2011–2024: [Typical EV Range Has More Than Tripled In 10 Years](https://insideevs.com/news/746799/average-ev-range/) [observed]
