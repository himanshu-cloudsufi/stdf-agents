# STDF Domain Disruption Agent — Solar Energy Disruption in Geopolitical Conflict Context (Iran War)

**Agent:** `stdf-domain-disruption` | **Confidence:** 0.82

**Analysis date:** 2026-03-24

---

## Agent Reasoning

This analysis addresses a dual-layer question: (1) the underlying disruption landscape of solar PV in global electricity generation, and (2) how an Iran war geopolitical scenario modifies that disruption dynamic. The framing is purely cost-curve and adoption-theoretic. All disruption classifications follow the five canonical STDF types. The Iran war context is treated as a geopolitical shock acting through four distinct channels, each with a quantified directional effect on the incumbent-vs-disruptor cost gap.

Data grounding is primarily Tier 2 (local catalog: Rethinkx-sourced solar PV installed cost and capacity curves, BESS cost curves, wind capacity curves) and Tier 1 (Ember Global Electricity Review 2025). The Iran geopolitical context is grounded in observed 2024 data on Hormuz transit volumes, Iran oil production, and the empirically observed 2022 Russia-Ukraine analogue for how oil-gas price shocks affect the relative cost position of solar vs. fossil-fuel generation. Confidence is 0.82 rather than 0.9+ because the Iran conflict is a scenario being evaluated against historical analogues, not observed data.

The core analytical insight is asymmetric sensitivity: solar LCOE is structurally insensitive to oil and gas price shocks (capital-cost-driven, zero fuel cost), while combined-cycle gas turbine (CCGT) and oil-fired generation LCOE scales directly with fuel price. An Iran war scenario that raises gas prices narrows the competitive space for CCGT incumbents and widens the LCOE advantage of solar PV in all markets outside the US cheap-gas exception. The 2022 Russia-Ukraine analogue produced a computed 5.9× solar LCOE advantage over CCGT at EU gas prices (gas at $37.52/MMBtu). A Hormuz closure scenario is structurally larger, removing a net 17.4 Mbpd from global supply vs. the Russia-Ukraine ~4 Mbpd reduction.

The analysis also identifies a critical geographic sub-domain: the Middle East itself, where 20% of electricity comes from oil-fired generation (~1.8 Mbpd). An Iran war directly threatens this sub-domain, creating an accelerant for market-driven disruption of oil-fired generation by utility-scale solar PV in the region. The geopolitical shock does not create the S-curve adoption disruption — cost-curve dynamics are already doing that — but it accelerates adoption timing by widening the cost gap between the disruptor and all fuel-dependent incumbents.

---

## Classification Overrides

| Technology | Flow Type | Reasoning |
|-----------|-----------|-----------|
| Utility-scale solar PV | Stellar | Zero fuel cost; cost-curve dynamics independent of resource consumption; Jevons MUST NOT apply |
| Onshore wind turbines | Stellar | Zero fuel cost; wind is free at point of use; Jevons MUST NOT apply |
| BESS (grid-scale lithium iron phosphate) | Stellar | Zero fuel cost; storage enables dispatchability without fuel throughput; Jevons MUST NOT apply |
| Coal-fired steam turbine | X-Flow | Physical coal throughput; fuel cost 40-60% of LCOE; demand elasticity via Jevons effect (X-Flow) |
| Combined-cycle gas turbine (CCGT) | X-Flow | Physical gas throughput; fuel cost 60-75% of LCOE; demand elasticity via Jevons effect (X-Flow) |
| Open-cycle gas turbine (OCGT) | X-Flow | Physical gas throughput; peak-load fuel cost 80%+ of LCOE; demand elasticity via Jevons effect (X-Flow) |
| Oil-fired steam turbine (Middle East) | X-Flow | Physical oil throughput; fuel cost dominant; demand elasticity via Jevons effect (X-Flow) |
| Gas-solar hybrid plant | Hybrid | Solar component is Stellar; gas backup component is X-Flow; gas component dominates in dispatch decisions at current solar/storage cost levels |
| Small modular reactor (SMR) | Hybrid | Capital-intensive like Stellar but with uranium fuel throughput (X-Flow component); cost trajectory diverging from solar PV |

---

## Agent Output

### Key Findings
- **Sector:** Energy
- **Sub-domains:** utility-scale solar PV electricity generation, CCGT gas-fired electricity generation, coal-fired electricity generation, oil-fired electricity generation (MENA sub-domain), grid-scale battery energy storage (BESS)
- **Confidence:** 0.82

---

### Disruption Map

| Disruption | Disruptors | Incumbents | Chimeras | Convergence |
|---|---|---|---|---|
| Solar PV + wind disruption of coal-fired electricity generation | Utility-scale solar PV, onshore wind turbines | Coal-fired steam turbine | Gas-solar hybrid plant (adds gas peaking without completing coal incumbent displacement); coal + CCS (retains coal infrastructure at higher cost) | SWB (Solar PV + Wind + BESS): enables dispatchable low-cost generation displacing baseload coal |
| Solar PV + BESS disruption of CCGT generation | Utility-scale solar PV + grid-scale BESS, onshore wind turbines | Combined-cycle gas turbine (CCGT), open-cycle gas turbine (OCGT) | Gas-solar hybrid plants (retains gas backup, cannot reach full solar cost floor); natural gas + CCS (cost-additive, retains gas supply chain) | SWB (Solar PV + Wind + BESS): 24/7 dispatchable electricity without gas; solar LCOE $44/MWh vs CCGT $86/MWh at EU gas prices [model-derived] |
| Solar PV incumbent displacement of oil-fired electricity generation (MENA) | Utility-scale solar PV, distributed rooftop solar PV | Oil-fired steam turbine, gas turbine (oil-capable) | Gas-solar hybrid (replaces oil with gas — retains fossil fuel infrastructure and Hormuz supply chain exposure) | SWB-Middle East: Solar PV + BESS in high-irradiance MENA region; capacity factors 25-30%, lowest achievable LCOE globally (~$25-35/MWh) |
| SWB systemic disruption of fossil fuel electricity generation | Utility-scale solar PV + onshore wind turbines + grid-scale BESS | Coal-fired steam turbine, CCGT, OCGT, oil-fired turbine | Small modular reactor (SMR): 10-20yr build time, $7,000-15,000/kW cost, diverging from solar PV cost trajectory; gas-solar hybrid plants | SWB: Solar + Wind + BESS systemic convergence; IRES (Intermittent Stellar Generation + Storage + Smart Grid) |
| Iran-war-accelerated disruption of gas/oil generation (geopolitical shock channel) | Utility-scale solar PV + BESS (zero fuel cost; structurally insensitive to oil/gas price shocks) | CCGT and OCGT (fuel-price-sensitive, LCOE scales with gas price); oil-fired turbines (fuel-price-sensitive, Hormuz-exposed) | Same chimeras as above — gas-solar hybrid; SMR | SWB geopolitical accelerant: solar LCOE advantage widens from 1.9× (EU 2024 baseline) to 3.3-5.9× at conflict-level gas prices [model-derived]; asymmetric insensitivity to fuel price shocks is the structural advantage |

---

### End-Use Completeness Check

**Global electricity generation 2024: 30,856 TWh [observed] — Ember Global Electricity Review 2025**

| End-Use Segment | Share (%) | Disruption Assessed | Notes |
|---|---|---|---|
| Coal-fired electricity generation | 34.4% | YES | Primary disruption entry: SWB disruption of coal incumbent |
| Natural gas CCGT/OCGT electricity generation | 22.0% | YES | Primary disruption entry: SWB + solar LCOE advantage over CCGT |
| Nuclear electricity generation | ~9% | NO | Out of scope for solar disruption; nuclear is displaced by SWB but on different cost dynamics; flagged for separate analysis |
| Hydroelectric generation | ~15% | NO | Hydro is a complementary dispatchable source, not disrupted by solar; included as flexibility asset in IRES convergence |
| Oil and other fossil fuel electricity generation | ~2.8% global; ~20% MENA | YES | Covered in MENA oil-fired incumbent displacement entry |
| Solar PV electricity generation | 6.9% | YES — as DISRUPTOR | Solar is the primary disruptor analyzed |
| Wind electricity generation | ~7% | YES — as DISRUPTOR | Wind is co-disruptor in SWB convergence |
| Other (geothermal, biomass, etc.) | ~2% | NO | Below 5% threshold; insufficient data for separate disruption assessment |

---

### Technology Flow Classification

| Technology | Flow Type | Reasoning |
|---|---|---|
| Utility-scale solar PV | Stellar | Zero marginal fuel cost; module cost-curve dynamics follow cumulative learning independent of energy throughput; Jevons MUST NOT apply |
| Onshore wind turbines | Stellar | Zero marginal fuel cost; wind resource is not consumed by generation; Jevons MUST NOT apply |
| Grid-scale BESS (LFP chemistry) | Stellar | Zero fuel cost in operation; cost-curve driven by manufacturing scale; Jevons MUST NOT apply |
| Coal-fired steam turbine | X-Flow | Coal consumed per MWh generated; fuel cost 40-60% of LCOE; demand elasticity via Jevons effect (X-Flow) |
| Combined-cycle gas turbine (CCGT) | X-Flow | Gas consumed per MWh generated; fuel cost 60-75% of LCOE at EU gas prices; demand elasticity via Jevons effect (X-Flow) |
| Open-cycle gas turbine (OCGT) | X-Flow | Gas consumed per MWh; higher heat rate than CCGT; fuel cost 75-85% of LCOE; demand elasticity via Jevons effect (X-Flow) |
| Oil-fired steam/gas turbine | X-Flow | Oil consumed per MWh; dominant in MENA; directly exposed to Hormuz supply shock; demand elasticity via Jevons effect (X-Flow) |
| Gas-solar hybrid plant | Hybrid | Solar component is Stellar; gas peaking component is X-Flow; gas dominates dispatch decisions in most markets at current solar penetration levels |
| Small modular reactor (SMR) | Hybrid | Uranium fuel throughput (X-Flow component); capital-intensive like Stellar; uranium cost small fraction of LCOE but supply chain dependency exists |

**Downstream Jevons implications:**
Solar PV, wind, and BESS: Jevons Paradox explicitly prohibited (Stellar classification). Lower electricity costs from solar PV do not generate rebound demand in a way that increases solar deployment above what cost-curve dynamics project independently.

CCGT, OCGT, coal, oil-fired generation: Jevons may apply (X-Flow classification). Lower fuel prices (e.g., US domestic gas at $2.19/MMBtu) increase CCGT competitiveness and may sustain X-Flow demand. In the Iran conflict scenario, the opposite applies: higher fuel prices suppress X-Flow demand for gas-fired generation, compressing incumbent utilization before physical incumbent displacement occurs.

**Cost Metric Recommendation:** LCOE ($/MWh) is the primary parity metric for this domain. Solar LCOE is capital-cost-dominated; CCGT LCOE is fuel-cost-dominated. The Iran war scenario acts directly on the CCGT fuel cost term, widening the LCOE gap. For project-level capital allocation analysis, additionally use installed cost ($/kW) for solar capex comparisons.

**Market Type Recommendation:** Utility (grid-scale, merchant and contracted power markets). Grid operators, utilities, and sovereign energy procurement bodies are the primary adoption decision-makers. The Iran conflict channel operates at the utility and sovereign energy-security level, not the consumer level.

---

### Narrative

#### Sector and Sub-Domain Definition

The primary sector is **Energy**, specifically the global electricity generation sub-domain. Sub-domains: (1) utility-scale solar PV electricity generation, currently the fastest-growing generation source globally; (2) CCGT and OCGT gas-fired electricity generation, the primary incumbent facing solar incumbent displacement in most markets; (3) coal-fired electricity generation, the largest single incumbent by generation share; (4) oil-fired electricity generation, a regionally concentrated incumbent critical to the MENA region; and (5) grid-scale BESS, the enabling convergence technology for 24/7 dispatchable solar power.

#### Baseline Solar Disruption Dynamics (Quantitative Grounding)

Solar PV belongs to the **stellar energy** category (zero marginal cost technologies) alongside wind and BESS. Utility-scale solar PV has followed a 30.8%-per-doubling cost-curve learning rate [model-derived], computed from catalog data: installed cost fell from $5,310/kW (2010) to $700/kW (2024), an 87% decline over 5.5 cumulative capacity doublings [T2: Solar_Photovoltaic_Installed_Cost_Global.json, Rethinkx, observed 2010-2024]. Annual decay rate is 14.6%/yr (R²=0.986, N=15 data points, 2010-2024). This is a market-driven disruption driven by cost-curve dynamics operating for 44 years at ~25.7% per doubling (Fraunhofer ISE, observed historical data).

Global installed solar PV capacity grew from 41 GW (2010) to 1,865 GW (2024) — a 45× increase at a CAGR of 31.3% [T2: Solar_Installed_Capacity_Global.json, Rethinkx, observed]. Annual solar generation reached 2,131 TWh (2024), representing 6.9% of global electricity — total global electricity was 30,856 TWh (2024) [T1: Ember Global Electricity Review 2025, observed]. Solar generation grew at 28%/yr over 2022-2024 [model-derived from catalog data].

Solar module prices are now $0.13/W globally (2024, Fraunhofer ISE, observed), having declined ~50% in 2022-2023 and a further ~25% in 2023-2024. China controls 93.2% of global polysilicon, 96.6% of wafers, 92.3% of cells, and 86.4% of modules [T3: China Photovoltaic Industry Association (CPIA), observed 2024]. Global manufacturing capacity reached ~800 GW/yr (2024) against ~600 GW of installations — a structural supply surplus that sustains price pressure independent of geopolitical events.

This places utility-scale solar PV firmly in the **Growth phase** of its S-curve adoption: above the 2.5% early-adopter threshold, below the ~15% inflection midpoint, with growth rates well above 20%/yr. The disruption is **Big Bang** in character where it has already crossed cost parity (most markets outside the US cheap-gas exception): simultaneously cheaper AND faster-deploying than any fossil fuel alternative.

Onshore wind capacity reached 1,053 GW globally (2024) at a CAGR of 13.5% over 2010-2024 [T2: Onshore_Wind_Installed_Capacity_Global.json, Rethinkx, observed]. Wind and solar together supply approximately 14% of global electricity (2024 [T1: Ember, observed]).

Grid-scale BESS grew from 193 MWh (2010) to 370,112 MWh (2024) at a CAGR of 72%/yr [T2: prior analysis, observed]. 2-hour turnkey BESS cost fell from $441/kWh (2019) to $269/kWh (2024) globally [T2: Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json, Rethinkx, observed]; China achieved $101/kWh by 2024 [T2: same series, China, observed]. BESS is in the **Early Adopter phase** — minimal penetration of total grid storage, but 72%/yr CAGR indicates clearance of the S-curve's initial threshold.

Gas-fired power generation peaked at 6,312 TWh (2022) and declined to 6,278 TWh (2024), a 0.5% decline from peak [T2: Natural_Gas_Annual_Power_Generation_Global.json, Rethinkx, observed]. This is the first confirmed post-peak signal for gas power generation globally — the onset of incumbent displacement.

Coal-fired generation continued growing globally (China-driven), reaching 10,018 TWh (2024) [T2: Coal_Annual_Power_Generation_Global.json, observed], but its market share fell from 40.8% (2007) to 34.4% (2024) [T1: Ember, observed] as total electricity demand grew faster than coal output. Coal incumbent displacement is structurally advanced in Europe and the US; still in early stages in developing Asia.

#### The Iran War Scenario: Four Disruption Channels

The Iran war scenario modifies the baseline solar disruption dynamics through four quantifiable channels. These are directional assessments grounded in the observed 2022 Russia-Ukraine analogue and structural geopolitical data; magnitudes are scenario-dependent.

**Channel 1: Fuel price shock widens the CCGT vs. solar LCOE gap (primary channel)**

Solar LCOE is structurally insensitive to oil and gas price shocks — it is capital-cost-dominated with zero fuel cost. CCGT LCOE scales directly with gas price at the rate of approximately $6.5/MWh per $1/MMBtu of gas price increase (CCGT heat rate ~6.5 MMBtu/MWh) [model-derived].

Solar LCOE computed at $700/kW capex, 20% CF, 7% WACC, 25yr life: **$44/MWh** [model-derived]. This value is independent of all fossil fuel price movements.

| Gas Price Scenario | CCGT LCOE (USD/MWh) | Solar LCOE (USD/MWh) | Solar Advantage |
|---|---|---|---|
| US baseline $2.19/MMBtu (2024) | 29 | 44 | CCGT cheaper (CCGT 0.7× solar) |
| EU baseline $10.89/MMBtu (2024) | 86 | 44 | Solar 1.9× cheaper |
| Moderate conflict $20/MMBtu | 145 | 44 | Solar 3.3× cheaper |
| Severe conflict $30/MMBtu | 210 | 44 | Solar 4.8× cheaper |
| 2022 peak (Russia-Ukraine) $37.52/MMBtu | 259 | 44 | Solar 5.9× cheaper |

**All CCGT values: [model-derived] from heat rate 6.5 MMBtu/MWh + $15/MWh fixed O&M. Solar LCOE: [model-derived].**

Iran exports approximately 1.6 Mbpd (2024) [T3: US Energy Information Administration Country Analysis Brief, October 2024, observed] [CAUTION: EIA source — historical data only]. The Strait of Hormuz carries ~20 Mbpd — 20% of global petroleum liquids consumption and 27% of seaborne oil trade (2024) [T3: US Energy Information Administration, 2024, observed] [CAUTION: EIA source — historical data only]. The only bypass capacity is approximately 2.6 Mbpd via Saudi and UAE pipelines [T3: same source] [CAUTION: EIA source — historical data only]. A full Hormuz closure would create a net supply shock of 17.4 Mbpd — 17% of global consumption, versus the ~4.4 Mbpd embargo of 1973 that caused a 4× oil price spike.

Gas-oil price correlations (particularly in LNG-linked markets) transmit oil shocks to gas prices globally, disproportionately raising CCGT operating costs and widening solar's LCOE advantage in all markets outside the US domestic gas basin. The key mechanism: this is market-driven disruption acceleration. Higher incumbent fuel costs make the LCOE crossover irreversible faster in more markets. Capital flows to solar and away from new CCGT builds because the economics widen in favor of solar PV — not because of policy.

**Channel 2: MENA oil-fired generation disruption (high-impact geographic sub-domain)**

The MENA region uses oil for 20% of its electricity generation, requiring ~1.8 Mbpd [T3: Future of Electricity in MENA report, observed] [CAUTION: IEA source — historical data only]. This is the sub-domain where an Iran war creates both a supply-side shock (disrupted oil routes) AND an energy security imperative to decouple domestic power from fossil fuel supply chains. Solar PV in MENA has the highest capacity factors globally (CF 25-30%, vs. 18-20% global average) — meaning solar LCOE in this region is structurally lower than the global computed $44/MWh, reaching approximately $25-35/MWh.

The MENA solar incumbent displacement of oil-fired generation is a **From Below** disruption: solar entered at the low end of the power stack (small-scale auctions), and is scaling to displace oil-fired baseload as costs fell to $25-44/MWh vs. oil-fired generation at $80-150/MWh. The Iran war creates an urgency premium that further accelerates capital allocation to utility-scale solar in affected countries.

**Channel 3: Solar supply chain disruption (transient headwind, not structural)**

China controls 80-97% of each stage of the solar PV supply chain [T3: CPIA, observed 2024]. The Iran war does not directly threaten Chinese manufacturing. Red Sea/Suez Canal shipping (already disrupted by Houthi-affiliated attacks as of 2024) would see further degradation, adding ~14 days to China-Europe module delivery. However: global manufacturing capacity (~800 GW/yr) exceeds installations (~600 GW/yr) — structural supply surplus means price is set by production cost, not shipping. The US-China Pacific route is unaffected. Conclusion: shipping disruption creates a transient 3-6 month delivery delay and minor cost increase, not a structural barrier to S-curve adoption progression.

**Channel 4: Energy security capital allocation signal**

The 2022 Russia-Ukraine analogue: the gas price spike accelerated solar deployment — solar installations approximately tripled in four years, and solar panel prices fell ~50% then ~25% in consecutive years [T3: Ember/CPIA, observed]. An Iran war involving Hormuz disruption would be structurally more severe than the Ukraine gas shock, given larger supply disruption volume and broader commodity exposure (both oil and gas via LNG price correlations). The capital allocation signal would be correspondingly stronger: energy security becomes a co-driver of sovereign energy investment decisions, compressing the S-curve adoption timeline for solar PV in affected and exposed markets.

#### Disruption Type Classification

- **SWB disruption of CCGT and coal:** **Systemic** — solar, wind, and BESS simultaneously attacking baseload (coal), mid-merit (CCGT), and peak (OCGT) positions in the dispatch stack. No single technology achieves this alone; the convergence produces system-level incumbent displacement.
- **Solar incumbent displacement of oil-fired generation (MENA):** **From Below** — solar entered MENA markets as small auction projects below oil-fired generation costs, is now scaling to displace oil-fired baseload. LCOE gap: solar $25-44/MWh vs. oil-fired $80-150/MWh.
- **Iran war channel effect:** **Architectural** — the geopolitical shock restructures the competitive cost landscape by raising the floor LCOE of all fuel-dependent incumbents simultaneously, making the SWB disruption structurally earlier and faster in more markets than cost-curve dynamics alone would produce.

#### Chimera Identification

**Gas-solar hybrid plants** are confirmed chimeras: they combine solar PV (Stellar) with gas backup (X-Flow), retaining infrastructure dependency on fossil fuel supply chains and Hormuz-exposed gas markets. When gas prices spike in a conflict scenario, the chimera's operating cost increases — it cannot achieve the full cost floor of pure solar + BESS. In MENA specifically, operators replacing oil-fired generation with gas turbines + solar substitute one incumbent with a different fossil fuel incumbent, remaining structurally exposed.

**Coal + CCS** is a chimera: adds capital cost ($3,000-5,000/kW) while retaining coal throughput dependency. Cost trajectory diverges further from SWB.

**Small modular reactors (SMR)** are an emerging chimera promoted as an energy security hedge. Their characteristics: build time 10-20 years, installed cost $7,000-15,000/kW — vs. solar at $700/kW in 2024 declining at 14.6%/yr. SMRs cannot achieve the cost floor of SWB in any realistic scenario. Their potential value (24/7 dispatchable baseload) is increasingly addressable by SWB as BESS costs continue declining via cost-curve dynamics.

#### Convergence Mapping

**SWB (Solar PV + Wind + BESS):** Primary convergence. Each technology compensates for the others' limitations: solar is intermittent at night; wind is geographically constrained; both intermittent — BESS enables 24/7 dispatch from combined generation. Combined: dispatchable electricity at $44-80/MWh range, declining continuously, zero fuel cost. CCGT at EU gas: $86/MWh and rising with any gas price shock.

**IRES (Intermittent Stellar Generation + Storage + Smart Grid):** SWB expanded to include smart grid management. Enables large-scale incumbent displacement of centralized baseload model with distributed, dispatchable generation.

**SWB-Middle East:** SWB applied to the MENA context. Highest global irradiance (CF 25-30%), lowest achievable solar LCOE (~$25-35/MWh). The Iran war accelerant makes this convergence more urgently capital-attractive, with both supply-side (oil-fired generation risk) and demand-side (energy security) pressures pointing to accelerated S-curve adoption.

---

### Handoff Context

- **Sector boundaries:** Energy sector, electricity generation sub-domain. Scope includes utility-scale solar PV, onshore wind, BESS, CCGT, OCGT, coal-fired, and oil-fired generation. Excluded: petroleum transportation (separate BEV disruption analysis), gas heating (ASHP disruption), industrial gas use. The Iran war geopolitical scenario is bounded to its effect on fuel prices, supply chain logistics, and capital allocation signals — not a geopolitical conflict timeline or military analysis.

- **Key cost data:**
  - Solar PV installed cost (Global): $700/kW (2024), annual decay 14.6%/yr, R²=0.986, 30.8%/doubling learning rate [T2: Rethinkx, observed 2010-2024]
  - Solar PV module price: $0.13/W (2024) [T3: Fraunhofer ISE/CPIA, observed]
  - Solar LCOE (computed): ~$44/MWh at $700/kW capex, 20% CF, 7% WACC, 25yr [model-derived]
  - CCGT LCOE sensitivity: ~$6.5/MWh per $1/MMBtu gas price increase [model-derived]
  - BESS 2-hr turnkey (Global): $269/kWh (2024); China: $101/kWh (2024) [T2: Rethinkx, observed]
  - Iran oil exports: ~1.6 Mbpd (2024) [T3: US Energy Information Administration, observed] [CAUTION: EIA source — historical data only]
  - Hormuz transit: ~20 Mbpd (2024), 20% global consumption [T3: US Energy Information Administration, observed] [CAUTION: EIA source — historical data only]
  - Hormuz bypass capacity: ~2.6 Mbpd [T3: US Energy Information Administration, observed] [CAUTION: EIA source — historical data only]
  - MENA oil-fired electricity: 20% of regional generation, ~1.8 Mbpd [T3: Future of Electricity in MENA study, observed] [CAUTION: IEA source — historical data only]

- **S-curve positions:**
  - Utility-scale solar PV: Growth phase — 6.9% of global electricity (2024), 28%/yr generation growth
  - Onshore wind: Growth phase — ~7% of global electricity (2024), 13.5%/yr capacity CAGR
  - Grid-scale BESS: Early Adopter phase — 72%/yr CAGR, minimal penetration of total storage market
  - SWB convergence: Early-to-growth junction — components in growth phase; combined dispatchability still assembling at scale
  - Oil-fired generation (MENA): Reverse S-curve beginning — peak expected before 2030 per operator signals

- **Data gaps:**
  - BESS cost fit is weak (R²=0.873) — 2021-2022 supply chain shock disrupted cost trend line
  - No catalog data for MENA-specific solar adoption curves or MENA oil-fired generation capacity; Tier 3 sources used
  - No catalog data for SMR installed cost trajectory
  - Gas price scenarios in Iran war are sensitivities from 2022 analogue — not model-derived projections
  - Nuclear generation (~9% of global electricity) not assessed — excluded from scope

- **Unresolved questions for downstream agents:**
  1. **Cost-fitter:** Does China's BESS trajectory ($101/kWh in 2024) justify a separate faster-decay curve from the global $269/kWh series?
  2. **Cost-parity checker:** At what year does solar + 4-hour BESS LCOE cross below CCGT LCOE at US domestic gas prices ($2.19/MMBtu)? This is the last major market where solar is not yet clearly dominant on raw LCOE.
  3. **Adoption-readiness checker:** What is the current grid integration capacity constraint for solar in key markets (Germany, China, US, India)? Curtailment rates may limit effective S-curve adoption even after cost parity is achieved.
  4. **Tipping-synthesizer:** Should the Iran war scenario be modeled as a permanent gas price shift (structural supply reduction) or a transient spike? Historical oil shocks suggest partial recovery, but infrastructure damage could produce structural long-term supply effects.
  5. **Regional-adopter:** MENA is the highest-impact region for oil-fired electricity incumbent displacement. Which countries have existing solar capacity and grid frameworks capable of absorbing rapid deployment acceleration?

---

## Sources

- [T2] Solar_Photovoltaic_Installed_Cost_Global.json — Rethinkx, observed 2010-2024 [observed]
- [T2] Solar_Installed_Capacity_Global.json — Rethinkx, observed 2000-2024 [observed]
- [T2] Solar_Annual_Power_Generation_Global.json — Rethinkx, observed 2006-2024 [observed]
- [T2] Solar_Photovoltaic_Installed_Cost_China.json — Rethinkx, 2010-2024 [observed]
- [T2] Onshore_Wind_Installed_Capacity_Global.json — Rethinkx, observed 2000-2024 [observed]
- [T2] Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json — Rethinkx, 2019-2024 [observed]
- [T2] Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_China.json — Rethinkx, 2019-2024 [observed]
- [T2] Natural_Gas_Annual_Power_Generation_Global.json — Rethinkx, 2006-2024 [observed]
- [T2] Coal_Annual_Power_Generation_Global.json — Rethinkx, 2006-2024 [observed]
- [T1] Ember Global Electricity Review 2025 — observed 2024 electricity generation data by source; 30,856 TWh total; ember-energy.org/latest-insights/global-electricity-review-2025/ [observed]
- [T3] US Energy Information Administration Country Analysis Brief: Iran (October 2024) — Iran oil production and export data [observed] [CAUTION: EIA source — historical data only]
- [T3] US Energy Information Administration — Strait of Hormuz critical oil chokepoint (2024) — 20 Mbpd transit volume, 2.6 Mbpd bypass capacity [observed] [CAUTION: EIA source — historical data only]
- [T3] The Future of Electricity in the Middle East and North Africa (study) — MENA electricity mix, 20% oil-fired, ~1.8 Mbpd [observed] [CAUTION: IEA source — historical data only]
- [T3] Fraunhofer ISE Photovoltaics Report — Solar PV module price $0.13/W (2024), 25.7%/doubling historical learning rate [observed]; fraunhofer.ise.de (retrieved 2026-03-24)
- [T3] China Photovoltaic Industry Association (CPIA) / Climate Energy Finance — China solar manufacturing dominance: 93.2% polysilicon, 96.6% wafers, 92.3% cells, 86.4% modules [observed 2024]; climateenergyfinance.org (retrieved 2026-03-24)
- [T3] Ember — Energy security analysis post-2022 Ukraine crisis: solar installations tripled, module prices halved [observed]; ember-energy.org (retrieved 2026-03-24)
- [T3] Worldometer / CEIC — Iran crude oil production 2024 (~3.75 Mbpd) [observed]; worldometers.info (retrieved 2026-03-24)
- [T3] Visual Capitalist / Speed Commerce — Hormuz transit volume by country, 2024 [observed]; visualcapitalist.com (retrieved 2026-03-24)
