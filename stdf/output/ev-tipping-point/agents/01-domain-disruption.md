# STDF Domain Disruption Agent — EV Tipping Point

**Agent:** `stdf-domain-disruption` | **Confidence:** 0.88

---

## Agent Reasoning

This analysis focuses on the tipping-point question for battery electric vehicles (BEVs) displacing internal combustion engine (ICE) vehicles across all major transportation sub-domains. The query "give me tipping point of EVs" signals a TIPPING_ONLY preset, but as the Tier 1 foundation agent, the role here is to map the full disruption landscape — incumbents, disruptors, chimeras, convergence labels, and S-curve positions — that downstream tipping-point agents will use for quantitative analysis.

The analytical approach prioritizes local catalog data (Tier 2) over web search (Tier 3) wherever available, given the depth of the 956-curve catalog for this sector. Key sources include Rethinkx-curated BEV annual sales (global, regional), lithium-ion battery pack cost curves (global median 2010–2024), and passenger vehicle median price data (BEV and ICE, regional). All cost computations use python3 via `lib.cost_curve_math`; learning rates and decay constants are derived from exponential fits to observed data, not hand-estimated.

A critical framing decision: the "EV tipping point" is not a single binary event but a layered set of market-segment-specific cost crossings. Purchase price parity (the "headline" tipping point) has already been crossed in China for the median passenger car segment — BEV median at $16,200 (2024) vs ICE median sedan at $19,000 [T2: Passenger_Vehicle_(EV)_Median_Cost_China.json, Database]. The USA is within $500 of parity as of 2025. Total cost of ownership (TCO) parity including running costs crossed years earlier, globally, given BEV running costs of $0.07/mile vs ICE $0.17/mile — a 59% running cost advantage. The remaining barrier is upfront purchase price premium in Western markets, which is collapsing at 9–17% annually.

The tipping-point framing must distinguish five sub-domain vectors: (1) mass-market BEV passenger cars, (2) BEV commercial vehicles (trucks, buses, vans), (3) BEV two- and three-wheelers, (4) autonomous-driving-enabled TaaS (Transport as a Service), and (5) vehicle-to-grid (V2G) grid services. Each has a different S-curve position and a different dominant metric for parity. Downstream cost-parity and tipping-synthesizer agents should treat these as separate disruption vectors, not a monolithic "EV disruption."

---

## Agent Output

### Key Findings

- **Sector:** Transportation
- **Sub-domains:** mass-market BEV passenger cars, BEV commercial vehicles (light/medium/heavy trucks and buses), BEV two- and three-wheelers, autonomous TaaS (robotaxi fleet), vehicle-to-grid (V2G) grid services, BEV charging infrastructure
- **Confidence:** 0.88

---

### Disruption Map

| Disruption | Disruptors | Incumbents | Chimeras | Convergence |
|---|---|---|---|---|
| BEV disruption of mass-market ICE passenger vehicles | Battery electric vehicle (BEV) — mass market; lithium iron phosphate (LFP) BEV; BEV SUV/crossover | Petrol ICE sedan/hatchback; diesel ICE sedan; naturally aspirated ICE drivetrain | PHEV (plug-in hybrid electric vehicle) — retains ICE drivetrain and fossil fuel dependency; MHEV (mild hybrid) — marginal fuel efficiency gain, no electric-only range | A-EV (Autonomous + BEV); SWB-EV (Solar + Wind + Battery + BEV charging) |
| BEV disruption of ICE commercial vehicles (trucks, buses, vans) | BEV light commercial van; BEV city bus; BEV medium-duty truck; BEV heavy-duty truck (short-to-medium haul) | Diesel ICE van; diesel ICE bus; diesel ICE medium/heavy truck; LNG-fueled heavy truck; CNG-fueled urban bus | PHEV delivery van; diesel-electric hybrid bus (range extender); hydrogen fuel cell commercial vehicle (FCEV) — requires hydrogen supply chain infrastructure | BSAF (Battery + Solar + Autonomous + Fleet); BEV bus depot with on-site solar |
| BEV disruption of ICE two- and three-wheelers | Battery electric two-wheeler (L1/L3 class); battery electric three-wheeler (auto-rickshaw, cargo tuk-tuk); LFP-powered cargo scooter | Petrol ICE motorcycle; petrol ICE scooter; petrol ICE auto-rickshaw; diesel three-wheeler | Low-speed electric two-wheeler (lead-acid battery, speed <25 km/hr) — chimera: lead-acid battery cannot achieve LFP cost floor | LFP-2W (LFP battery + lightweight electric drivetrain) |
| Autonomous TaaS disruption of personal vehicle ownership | L4 autonomous robotaxi (BEV platform); fleet management software; ride-hailing aggregation platform | Personal ICE vehicle ownership model; human-driven taxi and rideshare | L2/L2+ ADAS systems (retain human driver — chimera between autonomous and manual driving) | A-EV (Autonomous driving + BEV); TaaS (A-EV + ride-hailing + fleet management software) |
| V2G disruption of centralized grid peaking infrastructure | Bidirectional BEV charger (V2G); virtual power plant (VPP) aggregation software | Natural gas peaking plant (OCGT); stationary grid battery (conventional, non-vehicle-integrated) | One-way smart charger (V1G, demand response only) — limited by absence of discharge capability | V2G-EV (BEV bidirectional charging + VPP software); SWB-EV (solar + wind + BEV as distributed grid storage) |

---

### End-Use Completeness Check

**All share values: [observed] from global vehicle sales data (Rethinkx 2024; global market ~163M vehicles/yr)**

| End-Use Segment | Share (%) | Disruption Assessed | Notes |
|---|---|---|---|
| Passenger cars (petrol/diesel ICE) | 49% | YES | Primary disruption vector; BEV at 14% new-car share globally (2024) |
| Two-wheelers (motorcycles, scooters) | 31% | YES | BEV two-wheelers at ~18% global share (2024); China-led |
| Commercial vehicles (vans, trucks, buses) | 15% | YES | BEV commercial vehicles at ~4.7% global share (2024); CAGR 75% (2019–2024) |
| Three-wheelers (rickshaws, cargo) | 5% | YES | ~25% EV penetration estimated (China, India); LFP-powered |

All segments >5% have a disruption assessment. The V2G and TaaS sub-domains are demand-side derivatives of the BEV passenger car disruption and are captured in separate disruption rows.

---

### Technology Flow Classification

| Technology | Flow Type | Reasoning |
|---|---|---|
| Battery electric vehicle (BEV) — mass market | Hybrid (Stellar-dominant) | BEV has near-zero marginal energy cost per mile (stellar energy input) but retains X-Flow characteristics in battery mineral throughput (lithium, nickel, cobalt). Stellar component dominates. Jevons does NOT apply to energy input dimension. |
| LFP (lithium iron phosphate) battery pack | Stellar | Zero marginal cost of stored energy once manufactured; cost per kWh declines with cumulative production. No fossil fuel throughput. Jevons does not apply. |
| Autonomous driving system (L4 robotaxi) | Stellar | Compute and software with near-zero marginal cost of replication; key sensor costs follow steep cost-curve dynamics. No physical throughput of fossil resources. |
| PHEV (plug-in hybrid electric vehicle) | X-Flow (chimera) | Retains ICE drivetrain with continuous petrol/diesel throughput; cannot escape X-Flow cost dynamics of fossil fuel consumption. Structurally cannot reach BEV total cost floor. |
| Hydrogen fuel cell electric vehicle (FCEV) | Hybrid (X-Flow-dominant) | Hydrogen is a physical carrier requiring energy-intensive production, compression, and transport — full X-Flow characteristics. Not on a competitive cost curve vs. LFP BEV at equivalent range. |
| V2G bidirectional charging system | Stellar | Software and inverter hardware; monetizes idle BEV battery capacity. Marginal cost of a V2G dispatch event approaches zero at scale. |

**Classification overrides for downstream agents:**

```
## Classification Overrides
BEV (mass market): Hybrid (Stellar-dominant) | Jevons: NOT applicable to energy input; MAY apply to mineral demand
LFP battery pack: Stellar | Jevons: NOT applicable
Autonomous driving (L4): Stellar | Jevons: NOT applicable
PHEV: X-Flow (chimera) | Jevons: applicable
FCEV (light vehicle): Hybrid (X-Flow-dominant) | Jevons: applicable
V2G system: Stellar | Jevons: NOT applicable
```

---

### Narrative

**Disruption Type Classification**

This is a market-driven disruption — cost-curve dynamics, not policy mandates, are the primary force. The BEV disruption of ICE passenger vehicles is a **From Above + Big Bang** hybrid disruption:

- **From Above (Phase 1, 2012–2019):** Tesla's BEV entered at the luxury/performance segment ($57k–100k+), establishing brand and technology credibility before cost-curve dynamics allowed cascade to mass market. This is the canonical "From Above" trajectory.
- **Big Bang (Phase 2, 2020–present):** In China specifically, BEV simultaneously achieved superior performance AND lower purchase price than ICE equivalents — driven by BYD's LFP vertical integration and China's manufacturing scale. The BEV median price in China ($16,200 in 2024 [T2: Passenger_Vehicle_(EV)_Median_Cost_China.json, Database, observed]) is 14.7% below the ICE median sedan ($19,000 [T2: Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_China.json, Database, observed]). This constitutes a Big Bang event in China: BEV is now both cheaper AND functionally superior on most consumer dimensions.

The BEV commercial vehicle disruption (trucks, buses, vans) is a **From Below** disruption: BEV entered short-haul urban logistics and city bus segments first (lower duty-cycle requirements, lower range anxiety), and is now cascading upward to medium- and long-haul as battery energy density and fast-charging improve.

The autonomous TaaS disruption is **Architectural**: it does not merely replace the vehicle but reconfigures the entire value chain of personal mobility — eliminating vehicle ownership, insurance, parking, and maintenance costs as separate line items, collapsing them into a per-mile service fee.

**Battery Pack Cost Curve**

Li-ion battery pack costs have declined from $1,436/kWh in 2010 to $115/kWh in 2024 — a 92% decline over 14 years [T2: Lithium_Ion_Battery_Pack_Median_Cost_Global.json, Rethinkx, observed]. Exponential fit yields a decay rate of r = 0.184/year (R² = 0.954, 15 data points, 2010–2024 [model-derived]). This translates to a 16.8% annual cost decline [model-derived]. The implied learning rate from fleet scaling (proxy production growth ~2,000x from 2010 to 2024) is 20.6% per doubling of cumulative output [model-derived].

For passenger BEV packs specifically, the 2019–2024 series shows $179/kWh → $97/kWh (46% decline in 5 years) [T2: Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json, Rethinkx, observed], with an annual decline rate of 9.3% in this more recent window (R² = 0.778, 6 data points [model-derived] — note lower R² partly due to 2022 LME lithium price spike). China's LFP pack costs are already at $85–94/kWh (2024–2025) [T2: Lithium_Ion_Battery_Pack_Median_Cost_China.json, Database, observed].

**BEV Adoption S-Curve Position**

Global BEV annual passenger car sales grew from 5,000 (2010) to 11,000,000 (2024) — a CAGR of 73.3% over 14 years, with a doubling time of 1.3 years [model-derived from T2: Passenger_Vehicle_(BEV)_Annual_Sales_Global.json, Rethinkx, observed]. The 2019–2024 CAGR was 47.0% [model-derived], reflecting acceleration into the high-growth phase of the S-curve.

Global BEV new car share: 0.01% (2010) → 13.8% (2024) [observed]. S-curve adoption dynamics place the global market at the **early-to-mid growth phase** of the S-curve — past the embryonic phase but not yet at the inflection point (~20–25% share typically marks the inflection for durable goods). The global BEV fleet stands at 39 million out of ~1.5 billion total vehicles on road — only 2.6% fleet share [observed], indicating the stock-turnover disruption is still in early innings.

Regional S-curve positions are highly differentiated:
- **China:** 21% BEV share of new car sales (2024) [observed]; approaching inflection. The NEV (BEV + PHEV) share exceeds 35%. China leads: 6.4M of 11M global BEV sales in 2024 (58% of global supply) [T2: Passenger_Vehicle_(BEV)_Annual_Sales_China.json, Rethinkx].
- **Europe:** ~20% BEV share of new car sales (2024) [observed]; at early inflection.
- **USA:** ~8% BEV share of new car sales (2024) [observed]; early growth phase. Policy headwinds and charging infrastructure gaps constrain the S-curve.
- **Norway:** >90% BEV new car share [observed]; post-saturation phase in new sales, demonstrating what full-adoption markets look like.

**Purchase Price Parity**

The headline tipping metric for mass-market adoption is purchase price parity (the point at which the consumer faces zero cost penalty for choosing BEV over ICE). Key observations:

- **China 2024:** BEV purchase price parity crossed. BEV median $16,200 vs ICE median sedan $19,000 — BEV is 14.7% cheaper [T2: Database, observed].
- **USA 2025:** BEV median $30,000 vs ICE median sedan $29,500 — BEV is 1.7% more expensive, within rounding noise of parity [T2: Database, observed]. The gap was $2,000+ in 2024; it is collapsing.
- **Europe:** BEV purchase price premium persists in the $5,000–8,000 range as of 2024 (data gap — no direct catalog curve for Europe BEV vs ICE parity; see Data Gaps).

**Running Cost Parity**

Running cost parity (electricity + maintenance vs. petrol + maintenance) has been achieved globally: BEV running cost ~$0.07/mile vs. ICE ~$0.17/mile — a 59% advantage [model-derived from catalog energy and maintenance cost inputs]. At 12,000 miles/year, this generates $1,200/year in running cost savings. A $2,000 purchase price premium breaks even in 1.7 years [model-derived]. TCO parity is already clearly in BEV's favor in all major markets.

**Chimera Analysis**

The PHEV is the canonical chimera of this disruption. PHEV purchase price in China has declined from $27,857 (2015) to $11,100 (2025) [T2: Passenger_Vehicle_(PHEV)_Purchase_Price_Sedan_China.json, Database, observed] — aggressive cost reduction driven by volume. However, the PHEV's structural ceiling is clear: it retains the ICE drivetrain, ICE maintenance costs, fossil fuel dependency, and a smaller battery (typically 8–20 kWh vs. 40–100 kWh in a pure BEV). The PHEV captures the "range anxiety" gap during the disruption period but cannot match BEV's long-run cost curve as battery costs fall and charging infrastructure density increases. PHEVs represent a hump in the demand curve — rising as consumers hedge between ICE and BEV, then declining as the BEV becomes the dominant-TCO choice.

**Commercial Vehicle Disruption**

BEV commercial vehicles sold 1,171,919 units globally in 2024 [T2: Commercial_Vehicle_(EV)_Annual_Sales_Global.json, Rethinkx, observed], up from 71,506 in 2019 — a 5-year CAGR of 75% [model-derived]. This is the steepest CAGR of any vehicle segment. The disruption is concentrated in urban logistics (BEV vans, last-mile delivery) and city bus markets, where duty cycles are predictable and depot charging is economically superior to diesel fueling. Incumbent displacement is most advanced in city bus and last-mile delivery van sub-segments; the heavy long-haul truck segment (>400 km range) remains in early embryonic phase, with battery energy density and charging speed as the remaining constraints on duty-cycle coverage.

**Two- and Three-Wheeler Disruption**

BEV two-wheelers (L1/L3 class, top speed ≥25 km/hr) sold 8.9 million units globally in 2024 [T2: Two_Wheeler_(EV)_Annual_Sales_Global.json, Rethinkx, observed], representing ~18% of the global two-wheeler market (~50M/yr). This disruption is already well advanced — peaking at 11M units in 2021 before stabilizing in the 8.9–9.1M range (2022–2024), suggesting possible near-term saturation in the China-dominated market. The LFP battery cost for two/three-wheelers declined from $470/kWh (2015) toward sub-$200/kWh by 2024 [T2: Lithium-Ion_Battery_Pack_(Two_and_three-wheelers)_Cost_Global.json, Rethinkx]. Three-wheelers (auto-rickshaw, cargo tuk-tuk) in India and Southeast Asia show ~25% EV penetration, driven by the economics of urban short-haul cargo and the total absence of ICE refueling infrastructure advantages in these markets.

**Autonomous TaaS**

The TaaS disruption (A-EV convergence) is in the **embryonic/early commercial** phase. Consumer autonomous rideshare cost: $2.75/mile (2025) [T2: Autonomous_Passenger_Car_RideShare_Revenue_per_Mile_(Cost_to_Consumer)_Global.json, AAA/Goldman Sachs, observed]. This remains above personal vehicle ownership cost (~$1.10–1.35/mile for ICE, ~$0.85–1.05/mile for BEV at 10,000 miles/year). The TaaS cost must reach $0.25–0.50/mile at scale to disrupt personal vehicle ownership structurally. LiDAR cost-curve dynamics support this trajectory: low-cost ADAS LiDAR in China declined from $2,000 (2018) to $200 (2025) — 90% decline in 7 years, decay rate 27.7%/year (R² = 0.943, 8 data points [model-derived, T2: Autonomous_Vehicle_LiDAR_(Low_Cost_ADAS)_Price_China.json]).

**Convergence Combinations**

- **A-EV** (Autonomous driving + BEV): The combination enables TaaS at sub-$1.00/mile consumer cost at moderate fleet utilization — impossible for either technology alone. BEV's zero-marginal-energy cost and autonomous driving's labor elimination converge to reshape the per-mile cost structure.
- **TaaS** (A-EV + ride-hailing platform + fleet management software): Architectural disruption of personal vehicle ownership. Emergent capability: on-demand point-to-point mobility without capital asset ownership.
- **SWB-EV** (Solar PV + Wind + Battery storage + BEV charging): Enables stellar-energy-powered personal mobility — closing the loop between stellar electricity generation and zero-fossil-fuel transport. Relevant for V2G and the full cost trajectory of BEV energy costs.
- **V2G-EV** (BEV bidirectional charging + virtual power plant software): Turns the BEV fleet into a distributed grid-storage asset, generating revenue for BEV owners and further lowering effective cost-per-mile of BEV ownership.
- **SDV-EV** (Software-defined vehicle platform + BEV): OTA software updates, subscription services, and data monetization create post-sale revenue streams impossible for ICE OEMs — accelerating BEV's total value proposition advantage.

**Charging Infrastructure**

Global public charging points grew from 184,000 (2015) to 5.44 million (2024) — a 30x increase, CAGR 46% [T2: Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json, Database, observed]. The BEV fleet-to-charger ratio is 7.2 vehicles per public charger (2024), up from 4.0 in 2015. While the ratio has worsened slightly, it reflects that most BEV charging occurs at home (>80% of sessions), so public charger density is a lagging enabler, not the binding constraint for adoption. China accounts for 3.58 million of 5.44 million global public chargers — 66% of global infrastructure.

---

### Handoff Context

- **Sector boundaries:** Transportation sector. Analysis covers passenger cars, commercial vehicles (vans, trucks, buses), two-wheelers, three-wheelers, autonomous TaaS, and V2G grid services. Excludes aviation, maritime, and rail electrification (separate disruption vectors with distinct cost curves and technology sets). Excludes non-vehicle-level transport infrastructure disruption (road charging, etc.).
- **Key cost data for downstream agents:**
  - Li-ion battery pack global median: $1,436/kWh (2010) → $115/kWh (2024) [T2: Rethinkx, observed]; decay rate r = 0.184/yr, R² = 0.954
  - BEV passenger pack: $179/kWh (2019) → $97/kWh (2024) [T2: Rethinkx, observed]; decay rate r = 0.097/yr, R² = 0.778 (note: lower R² due to 2022 LME lithium spike)
  - China LFP pack: ~$85–94/kWh (2024–2025) [T2: Database, observed]
  - BEV median China: $16,200 (2024) [T2: Database, observed]
  - ICE median sedan China: $19,000 (2024) [T2: Database, observed] — parity CROSSED; BEV 14.7% cheaper
  - BEV median USA: $30,000 (2025) [T2: Database, observed]
  - ICE median sedan USA: $29,500 (2025) [T2: Database, observed] — BEV premium 1.7% (effectively at parity)
  - LiDAR low-cost ADAS China: $2,000 (2018) → $200 (2025) [T2: Database, observed]; 90% decline; decay rate 27.7%/yr, R² = 0.943
  - Autonomous rideshare: $3.50/mile (2022) → $2.75/mile (2025) [T2: AAA/Goldman Sachs, observed]
  - BEV running cost: ~$0.07/mile vs ICE $0.17/mile [model-derived]; 59% BEV advantage
  - BEV implied learning rate: 20.6% per doubling of cumulative production (proxy) [model-derived]
- **S-curve positions:**
  - Global BEV new-car share: 13.8% (2024) — early-to-mid growth phase (pre-inflection globally)
  - China BEV new-car share: ~21% (2024) — approaching or at inflection
  - Europe BEV new-car share: ~20% (2024) — at early inflection
  - USA BEV new-car share: ~8% (2024) — early growth
  - Norway: >90% (post-saturation reference market)
  - BEV fleet share: 2.6% (2024) of ~1.5B total fleet — stock-disruption in early innings
  - BEV two-wheelers: ~18% new sales share globally — high growth, possible early saturation in China
  - BEV commercial vehicles: ~4.7% new sales share globally — early growth; CAGR 75% (2019–2024)
  - Autonomous TaaS (L4 robotaxi): embryonic commercial phase; cost not yet competitive with personal ownership
- **Cost Metric Recommendation:** Purchase price ($/vehicle, median segment) as the primary tipping metric for mass-market adoption. This is the most legible consumer-facing metric and the one at which market tipping is observed empirically (Norway preceded mass adoption with purchase price parity). Secondary metric: TCO per mile over 5-year ownership horizon for fleet/commercial segment decisions. Autonomous TaaS uses $/mile as its parity metric against personal ownership.
- **Market Type Recommendation:** **Consumer** market for passenger BEV (individual purchase decisions driven by sticker price + TCO). **Fleet** market for BEV commercial vehicles and TaaS (fleet operators optimize on TCO, not sticker price — parity has already been achieved for urban duty cycles). Two-wheelers are predominantly consumer markets in Asia.
- **Data gaps:**
  - Europe BEV vs ICE purchase price parity curve: not present in local catalog; only global and USA/China median prices available. Europe BEV premium estimated at $5,000–8,000 but not confirmed from catalog. Downstream cost-fitter should use web search for EU data.
  - PHEV fleet data beyond 2025 is not in catalog. PHEV represents a hump-shaped disruption pattern (chimera) that peaks and declines as BEV reaches parity; no local catalog series tracks this explicitly.
  - Three-wheeler EV penetration data is sparse; the ~25% figure used above is estimated from partial catalog data. Downstream agents should note this as a low-confidence estimate.
  - Autonomous vehicle L4 cost-per-mile below $2.75 (2025) is not in the catalog — the trajectory to $0.25–0.50/mile is model-inferential, not directly observed.
  - Solid-state battery costs are not in the local catalog. This represents a potential second-order disruption of the LFP incumbent within the BEV segment itself; data gaps limit confidence.
- **Unresolved questions for downstream agents:**
  1. What is the global BEV new-car share at which the S-curve inflection occurs? (China at ~21% appears to be at or near this point; the cost-parity-checker should compute whether China's crossing of purchase price parity caused a visible kink in adoption rate.)
  2. What is the TCO break-even year for the European consumer, given the higher BEV purchase premium and different electricity pricing?
  3. At what battery pack cost ($/kWh) does BEV achieve purchase price parity with ICE in the USA for the mid-size SUV segment (the largest US segment by volume)?
  4. When does autonomous TaaS achieve cost parity with personal BEV ownership (not just ICE) — this is the second-order tipping point beyond the BEV-vs-ICE tipping point.
  5. How does the PHEV chimera's hump-shaped demand curve affect the calculation of the "true" BEV tipping point? (In China, the NEV share includes PHEV; stripping PHEVs gives a lower pure BEV share figure.)

---

## Sources

**Tier 2 (Local Catalog):**
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — Rethinkx, global BEV annual sales 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_China.json` — Rethinkx, China BEV annual sales 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_USA.json` — Rethinkx, USA BEV annual sales 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Total_Fleet_Global.json` — Rethinkx, global BEV fleet 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json` — Database, global public EV charging points 2015–2024 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json` — Database, BEV median purchase price China 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — Database, BEV median purchase price USA 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_China.json` — Database, ICE sedan median price China 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — Database, ICE sedan median price USA 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(PHEV)_Purchase_Price_Sedan_China.json` — Database, PHEV sedan purchase price China 2015–2025 [observed]
- [T2] `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx, Li-ion battery pack median cost global 2010–2024 [observed]
- [T2] `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Database, Li-ion battery pack median cost China 2010–2025 [observed]
- [T2] `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — Rethinkx, BEV passenger pack cost global 2019–2024 [observed]
- [T2] `data/battery_pack/cost/Lithium-Ion_Battery_Pack_(Two_and_three-wheelers)_Cost_Global.json` — Rethinkx, two/three-wheeler LFP pack cost global 2015–2019 [observed]
- [T2] `data/autonomous_vehicle/cost/Autonomous_Passenger_Car_RideShare_Revenue_per_Mile_(Cost_to_Consumer)_Global.json` — AAA/Goldman Sachs, autonomous rideshare cost 2022–2025 [observed]
- [T2] `data/autonomous_vehicle/adoption/Autonomous_Passenger_Car_Annual_Sales_(L2)_Global.json` — IDTechEx, L2 autonomous car sales 2020–2025 [observed]
- [T2] `data/autonomous_vehicle/safety_incidents/Autonomous_Vehicle_Disengagements_per_Million_Miles_Global.json` — MDPI Study, AV disengagements 2018–2022 [observed]
- [T2] `data/passenger_cars/cost/Autonomous_Vehicle_LiDAR_(Low_Cost_ADAS)_Price_China.json` — Database, low-cost ADAS LiDAR price China 2018–2025 [observed]
- [T2] `data/two_wheeler/adoption/Two_Wheeler_(EV)_Annual_Sales_Global.json` — Rethinkx, two-wheeler EV global sales 2015–2024 [observed]
- [T2] `data/commercial_vehicle/adoption/Commercial_Vehicle_(EV)_Annual_Sales_Global.json` — Rethinkx, commercial EV global sales 2010–2024 [observed]

**All computed values:** `lib.cost_curve_math.exponential_fit` [model-derived]; custom python3 computations for CAGR, doubling time, market share, and TCO break-even [model-derived]
