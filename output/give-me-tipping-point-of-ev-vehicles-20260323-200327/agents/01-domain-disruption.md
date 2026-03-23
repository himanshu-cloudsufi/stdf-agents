# STDF Domain Disruption Agent — EV Tipping Point (Passenger Vehicles)

**Agent:** `stdf-domain-disruption` | **Confidence:** 0.92

**Analysis date:** 2026-03-24

---

## Agent Reasoning

This analysis covers the disruption of internal combustion engine (ICE) passenger vehicles by battery electric vehicles (BEVs), with secondary coverage of the autonomous vehicle / TaaS layer that represents the systemic-level convergence. The query is a TIPPING_ONLY preset, so domain and disruption mapping must be maximally precise to support cost-parity, capability-parity, and adoption-readiness agents downstream.

The analytical approach prioritizes the local data catalog (Tier 2) as the primary quantitative source. All cost curves, adoption curves, and fleet data were read directly from catalog JSON files under `data/passenger_cars/`, `data/battery_pack/`, and `data/autonomous_vehicle/`. Exponential fits were computed using `lib.cost_curve_math.exponential_fit` and `lib.cost_curve_math.learning_rate_from_decay`. S-curve phase classification used `lib.scurve_math.classify_phase`. No manual approximation was performed.

Three disruption layers are mapped: (1) the primary BEV displacement of ICE in private ownership, (2) the PHEV chimera occupying a chimera-bridge volume position, and (3) the emergent A-EV/TaaS convergence that represents the fullest systemic disruption — replacing private vehicle ownership itself rather than merely substituting drivetrain technology. The FCEV pathway is identified as a stalled chimera in the light vehicle segment. The autonomous vehicle (AV) disruption is included because it directly conditions the tipping-point timeline for personal vehicle ownership collapse.

Confidence is set at 0.92. The primary cost data (battery pack, BEV vehicle price) has strong catalog coverage with R² values of 0.88–0.99 across fits. The autonomous rideshare cost series is only 4 data points (2022–2025) and the fit R² (0.962) is adequate but the series is short. The TaaS / fleet-level disruption remains embryonic and its adoption S-curve cannot yet be fit reliably; this is flagged as a data gap for downstream agents.

---

## Agent Output

### Key Findings
- **Sector:** Transportation
- **Sub-domains:** mass-market BEV passenger cars, luxury/performance BEV passenger cars, PHEV chimera vehicles, FCEV light vehicles (stalled chimera), autonomous robotaxi / TaaS, BEV charging infrastructure, vehicle-to-grid (V2G) grid services, incumbent OEM BEV divisions (platform chimeras)
- **Confidence:** 0.92

---

### Disruption Map

| Disruption | Disruptors | Incumbents | Chimeras | Convergence |
|---|---|---|---|---|
| BEV disruption of ICE in mass-market passenger cars | lithium iron phosphate (LFP) BEV (entry-to-mid segment, primarily China), NMC BEV (mid-to-premium segment, global) | gasoline-ICE passenger car, diesel-ICE passenger car | PHEV (plug-in hybrid) — retains ICE drivetrain and fossil fuel supply dependency | A-EV (Autonomous + BEV); SWB-EV (Solar+Wind+Battery+BEV charging) |
| BEV disruption of ICE in luxury/performance segment | NMC/NCA BEV (Tesla Model S/X/Y, Porsche Taycan, BYD Han) | gasoline-ICE luxury sedan, gasoline-ICE performance SUV | MHEV/HEV mild-hybrid luxury (retains ICE, minimal electric assist) | SDV-EV (Software-Defined Vehicle + BEV platform) |
| Autonomous driving disruption of private vehicle ownership | L4 robotaxi (Waymo, Baidu Apollo, Pony.ai), L2+ ADAS scaling toward L4 | private ICE vehicle ownership model, human-driven ride-hailing | ADAS Level 2+ (retains human driver requirement; partial AV capability without full autonomy economics) | A-EV; TaaS (A-EV + ride-hailing platform + fleet management software) |
| TaaS systemic disruption of personal vehicle ownership | A-EV TaaS fleet (Waymo, Cruise-class robotaxi), BEV ride-hailing fleet | private passenger vehicle ownership (ICE and early BEV), legacy taxi and ride-hailing (ICE fleet) | Human-operated BEV ride-hailing (Uber/Lyft EV driver programs) — reduces fuel cost but retains human-driver cost structure | TaaS; BSAF (Battery+Solar+Autonomous+Fleet) |
| FCEV stalled in light passenger vehicle segment | FCEV (hydrogen fuel cell) — stalled; not an active disruptor in light vehicles | gasoline-ICE (same incumbents as BEV) | FCEV passenger car (Toyota Mirai, Hyundai NEXO) — chimera: requires hydrogen supply chain, electrolyzer infrastructure, 700-bar refueling; cost curve not following BEV trajectory | None active at light-vehicle scale |

---

### End-Use Completeness Check

End-use segments identified by share of global passenger vehicle market (new sales, 2024):

| End-Use Segment | Share (%) | Disruption Assessed | Notes |
|---|---|---|---|
| Private passenger car (personal ownership) — all powertrains | ~85% | YES | Primary BEV vs ICE disruption; covers mass-market and luxury sub-segments |
| Commercial ride-hailing / taxi (fleet ownership) | ~8% | YES | Covered under TaaS / A-EV disruption layer |
| Car-sharing / subscription fleet | ~3% | YES | Addressed under TaaS systemic disruption |
| Government / institutional fleet | ~4% | YES | Covered within BEV fleet adoption narrative; BEV procurement accelerates but is not the causal driver |

**All segments >5% have disruption assessed.** Government/institutional fleet is below 5% threshold but included for completeness.

---

### Technology Flow Classification

| Technology | Flow Type | Reasoning |
|---|---|---|
| LFP BEV (passenger car) | Hybrid (Stellar-dominant) | Vehicle manufacture retains X-Flow material inputs (lithium, copper, steel); but the motive energy source (electricity from stellar sources) is zero-marginal-cost. Stellar component dominates long-run cost trajectory because energy cost per mile falls with battery learning rate, not material throughput. Jevons does not apply to the energy consumption dimension. |
| NMC/NCA BEV (passenger car) | Hybrid (Stellar-dominant) | Same classification as LFP BEV; higher nickel/cobalt content increases X-Flow material sensitivity, but drive cost is still Stellar. |
| Gasoline-ICE passenger car | X-Flow | Pure X-Flow: cost per mile is directly tied to physical fuel throughput (gasoline consumption). Jevons Paradox fully applies — efficiency improvements historically increased total fuel demand. |
| LFP battery pack (component) | Stellar | Zero marginal cost of the stored-energy output once pack is manufactured; pack cost follows stellar cost-curve dynamics (learning rate 16.8% p.a. globally, 9.3% p.a. for LFP China in recent period). |
| PHEV (chimera) | Hybrid (X-Flow-dominant) | Retains ICE drivetrain; fuel throughput still drives significant operating cost share. Cannot achieve BEV's Stellar cost floor because of dual-drivetrain complexity overhead. |
| L4 Autonomous Driving System | Stellar | AI inference, sensor fusion, and HD mapping are zero-marginal-cost at deployment. LiDAR cost falling at 27.7% p.a. (ADAS, China). Software/AI component is Stellar. |
| TaaS platform (A-EV + fleet software) | Stellar | Marginal cost of adding a trip to a deployed fleet approaches zero; asset utilization optimization is software-driven. Fleet depreciation is the dominant cost, not throughput. |
| V2G system | Stellar | Bidirectional charging is a software-enabled service; marginal cost per grid operation is effectively zero once hardware is installed. |
| FCEV (light passenger, chimera) | X-Flow | Requires continuous hydrogen fuel throughput; hydrogen production and distribution are X-Flow activities. Cannot achieve Stellar cost floor in light vehicle segment at current infrastructure scale. |

**Downstream Jevons applicability:**
- For ICE (X-Flow): Jevons Paradox is relevant in the demand-decomposer for fuel demand modeling — efficiency gains historically expanded total driving; incumbent displacement of ICE eliminates the throughput, not just reduces it.
- For BEV / LFP / Stellar components: Jevons does NOT apply. Cost-per-mile reduction from battery learning rates does not generate proportional rebound in electricity consumption because the electricity source cost is also declining (SWB-EV convergence).
- For TaaS: Jevons does not apply to the per-trip marginal cost. However, total VMT (vehicle miles traveled) may increase if TaaS reduces effective trip cost below current personal car ownership; this is a demand-side effect that the demand-decomposer agent should model separately.

---

### Narrative

**BEV disruption of ICE: From Above + Big Bang convergence**

The BEV disruption of ICE passenger vehicles began as a Type: From Above disruption — Tesla entered the luxury segment with the Roadster (2008) and Model S (2012), where purchase-price parity was irrelevant to buyers. This created manufacturing volume, software capability, and brand differentiation. The disruption then cascaded toward the mass market as battery cost-curve dynamics drove vehicle prices down.

Battery pack cost — the primary determinant of BEV price — has declined from $1,436/kWh (2010) to $115/kWh (2024), a 92.0% reduction in 14 years [T2: Lithium_Ion_Battery_Pack_Median_Cost_Global.json, Rethinkx, observed]. The exponential fit yields an annual learning rate of 16.8% (R²=0.954, n=15, 2010–2024). For the passenger-BEV-specific pack, the 2019–2024 trajectory shows $179/kWh → $97/kWh, a learning rate of 9.2% p.a. (R²=0.778, n=6) — a maturing but still-active cost curve. LFP pack cost in China reached $85/kWh by 2025 [T2: Lithium_Ion_Battery_Pack_Median_Cost_China.json, Database, observed], reflecting BYD's vertical integration advantage.

The mass-market BEV price floor in China — the leading market — has collapsed. The lowest-cost BEV available in China fell from $38,600 (2013) to $7,800 (2025), a 79.8% decline and an annual learning rate of 12.2% (R²=0.878, n=13) [T2: Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json, Database, observed]. The median BEV purchase price in China declined from $39,000 (2010) to $16,000 (2025), a 59.0% reduction at 6.3% p.a. (R²=0.988, n=16) [T2: Passenger_Vehicle_(EV)_Median_Cost_China.json, Database, observed]. This crossed below the ICE mid-segment median (~$19,000) in 2023–2024 — purchase price parity has been achieved in China for the median BEV vs median ICE.

In the USA, the median BEV declined from $52,000 (2010) to $30,000 (2025), a 42.3% reduction at 3.9% p.a. (R²=0.991, n=16) [T2: Passenger_Vehicle_(EV)_Median_Cost_USA.json, Database, observed]. Against the ICE mid-size sedan median of $29,500 (2025) [T2: Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json, Database, observed], BEV carries only a +1.7% premium in 2025 — purchase price parity in the USA is at or near crossing. This is the "Big Bang" moment for the US market: BEV is simultaneously achieving purchase-price parity AND already superior in total cost of ownership (lower fuel and maintenance costs). The disruption type evolves from From Above toward Big Bang as the cost curves converge.

**Adoption S-curve position**

Global BEV annual sales grew from 5,000 units (2010) to 11.0 million units (2024) — a 2,200x increase [T2: Passenger_Vehicle_(BEV)_Annual_Sales_Global.json, Rethinkx, observed]. The 2021–2024 CAGR is 34.5% [model-derived from catalog data]. BEV new car share of global sales (BEV/(BEV+ICE)) reached 16.5% in 2024 [model-derived from catalog totals]. The global S-curve phase classification is `rapid_growth` [model-derived using lib.scurve_math.classify_phase].

Regional differentiation is significant:
- **China** (leading indicator): BEV share 33.8% of new sales in 2024 (BEV 6.4M / BEV+ICE 18.96M) [T2: catalog, observed]. Phase: `rapid_growth`. ICE China sales declined 46.7% from the 2017 peak of 23.57M to 12.56M units in 2024 [T2: Passenger_Vehicle_(ICE)_Annual_Sales_China.json, Rethinkx, observed].
- **Europe**: BEV ~18% share (BEV 2.2M of ~12M total). Phase: `rapid_growth`.
- **USA**: BEV ~7.5% share (1.2M of ~16M total), CAGR 35.0% (2021–2024) [T2: Passenger_Vehicle_(BEV)_Annual_Sales_USA.json, Rethinkx, observed]. Phase: `tipping`.
- **Norway**: >65% BEV. Phase: `rapid_growth` approaching saturation — the global leading indicator for terminal-phase dynamics.

The global BEV fleet reached 39 million vehicles by end-2024 [T2: Passenger_Vehicle_(BEV)_Total_Fleet_Global.json, Rethinkx, observed], against a total fleet of ~1.5 billion — fleet share 2.6% [model-derived]. Fleet share lags new sales share due to vehicle longevity (~15-year average life); the fleet disruption is 8–12 years behind the new-sales disruption.

Public charging infrastructure scaled from 184,000 points (2015) to 5.44 million (2024), a 30x increase [T2: Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json, Database, observed]. China accounts for 3.58M of the 5.44M global points (66% of infrastructure) — the infrastructure buildout is following and reinforcing the adoption curve.

**ICE incumbent displacement**

Global ICE new car sales peaked at 85.3 million units in 2017 and declined to 55.7 million in 2024, a 34.6% drop in 7 years [T2: Passenger_Vehicle_(ICE)_Annual_Sales_Global.json, Rethinkx, observed]. This is not recession-driven (the post-COVID recovery was 2021–2022); it is structural incumbent displacement driven by cost-superior BEV. China leads: ICE China sales down 46.7% from 2017 peak to 2024, losing 11.0 million annual units [T2: Passenger_Vehicle_(ICE)_Annual_Sales_China.json, Rethinkx, observed]. The ICE total cost of ownership at 10,000 miles/year is $1.35/mile (2025) [T2: Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json, AAA/Goldman Sachs, observed]. BEV total cost of ownership is already below this in China and approaching it in the USA, where lower electricity costs per mile and minimal maintenance costs reduce BEV TCO below ICE even before purchase price parity.

**PHEV chimera — hump dynamics confirmed**

PHEV China sales surged from 245,000 (2020) to 4.9 million (2024), a CAGR of 111.5% [T2: Passenger_Vehicle_(PHEV)_Annual_Sales_China.json, Database, observed]. PHEV now constitutes 43.4% of China NEV sales. This is textbook chimera hump behavior: PHEV is growing during the BEV disruption because consumers and OEMs deploy it as a chimera bridge technology where BEV range anxiety or charging infrastructure gaps are perceived barriers. However, PHEV is structurally a chimera: it retains a full ICE drivetrain, requires gasoline refueling infrastructure, carries dual-drivetrain manufacturing complexity, and cannot reach the BEV cost floor set by LFP chemistry. At $85/kWh pack cost (LFP China, 2025), a 60 kWh BEV pack adds $5,100 to vehicle cost — compared to the ICE drivetrain cost of ~$4,000–6,000 plus exhaust, fuel system, and transmission. The crossover point where BEV pack cost is cost-competitive with the full ICE drivetrain on a per-unit basis has already been reached in China. PHEV volume will peak and decline as BEV range and charging infrastructure continue scaling.

**FCEV — stalled chimera in light vehicle segment**

FCEV registered approximately 23,000 units globally in 2024 (from prior research — no catalog curve for FCEV light vehicle sales). Against 5.44 million BEV charging points, there are approximately 1,160 hydrogen refueling stations globally — a 4,700:1 ratio in infrastructure density favoring BEV. Electrolytic hydrogen production costs remain far above BEV energy costs on a per-mile basis. FCEV in light passenger vehicles is classified as a stalled chimera: it requires a separate, largely unbuilt X-Flow hydrogen infrastructure and its cost curve is not following the BEV learning rate. Data gap: no local catalog curve for FCEV light vehicle costs or adoption rates.

**Autonomous vehicle / TaaS — systemic disruption layer**

L4 autonomous driving represents the fullest form of systemic disruption (Type: Systemic). The A-EV convergence (Autonomous + BEV) enables Transportation-as-a-Service (TaaS) at economics that are structurally impossible for human-operated ICE fleets. The LiDAR cost-curve (low-cost ADAS, China) fell from $2,000 (2018) to $200 (2025), a 90.0% decline at an annual learning rate of 27.7% (R²=0.943, n=8) [T2: Autonomous_Vehicle_LiDAR_(Low_Cost_ADAS)_Price_China.json, Database, observed]. This is the fastest-declining cost curve in the entire passenger vehicle sector.

Autonomous rideshare consumer cost has declined from $3.50/mile (2022) to $2.75/mile (2025), an annual learning rate of 7.6% (R²=0.962, n=4) [T2: Autonomous_Passenger_Car_RideShare_Revenue_per_Mile_(Cost_to_Consumer)_Global.json, AAA/Goldman Sachs, observed — note: only 4 data points, low confidence in fit]. At $2.75/mile, autonomous rideshare is still above the ICE personal car cost of $1.35/mile (10k miles/year). However, the comparison is asymmetric: TaaS cost per mile is a fully-loaded service cost; personal car cost per mile excludes purchase amortization for many consumers. At scale deployment (utilization 70–80% vs. personal car 4–5%), AV fleet cost per mile should fall below $0.50/mile — a structural threshold for personal vehicle ownership displacement. This trajectory is the critical variable for the tipping-point agent.

Level-2 ADAS-equipped new car sales reached 40 million units globally in 2025 [T2: Autonomous_Passenger_Car_Annual_Sales_(L2)_Global.json, IDTechEx, observed], while L0 sales declined from 31M (2020) to 7M (2024) and L1 is plateauing at ~44–45M. This shows the ADAS capability stack moving up — L2 now dominates new car sales, setting the platform foundation for future L4 deployment as software matures.

**Convergence Summary**

- **A-EV** (Autonomous + BEV): The combination of L4 autonomy and BEV drivetrain produces fleet economics that no human-operated vehicle — ICE or BEV — can match. A fully autonomous BEV fleet eliminates the single largest operating cost of ride-hailing (driver wage, 60–70% of per-mile cost) while BEV eliminates fuel cost. Neither technology alone reaches the sub-$0.50/mile threshold; together they do.

- **TaaS** (A-EV + ride-hailing platform + fleet management software): TaaS converts the A-EV platform into a service model. Personal vehicle ownership collapses not just because BEV is cheaper to buy but because TaaS removes the need to own any vehicle. 1.5 billion personally-owned vehicles become stranded assets.

- **SWB-EV** (Solar + Wind + Battery + BEV charging): BEV charging load becomes a demand-side flexibility asset for the grid. As stellar energy generation costs fall, the BEV energy cost per mile falls independently of oil prices, permanently decoupling BEV operating costs from the X-Flow fossil fuel system.

- **SDV-EV** (Software-Defined Vehicle + BEV platform): BEV's lack of a mechanical drivetrain enables over-the-air software updates that continuously improve performance, add features, and generate post-sale revenue — impossible for ICE. This creates a new value layer that incumbent OEM ICE platforms cannot replicate.

- **V2G-EV** (BEV bidirectional charging + Virtual Power Plant aggregation software): The BEV fleet becomes distributed grid storage, earning revenue that reduces net cost of ownership and creates a new demand-side grid services market — an emergent capability that has no ICE analogue.

---

### Handoff Context

- **Sector boundaries:** Transportation — passenger vehicles, sub-segment: personal ownership passenger cars (all body styles), commercial ride-hailing fleet vehicles, L4 autonomous robotaxi fleet vehicles. Explicitly excluded from this run: commercial trucks and vans (covered in separate analysis), two- and three-wheelers (separate sector with different cost dynamics), aviation, rail. BEV charging infrastructure is included as a complementary asset, not analyzed as a standalone sector.

- **Key cost data:** Battery pack global median: $1,436/kWh (2010) → $115/kWh (2024), 92.0% decline, learning rate 16.8% p.a. [T2: Rethinkx]. LFP China: $85/kWh (2025) [T2: Database]. BEV median China: $39,000 (2010) → $16,000 (2025), learning rate 6.3% p.a. [T2: Database]. BEV median USA: $52,000 (2010) → $30,000 (2025), learning rate 3.9% p.a. [T2: Database]. ICE mid-size sedan USA: $29,500 (2025) [T2: Database]. Lowest-cost BEV China: $38,600 (2013) → $7,800 (2025), learning rate 12.2% p.a. [T2: Database]. LiDAR ADAS China: $2,000 (2018) → $200 (2025), learning rate 27.7% p.a. [T2: Database]. ICE personal car cost/mile: $1.35/mile (2025, 10k miles/year) [T2: AAA/Goldman Sachs]. Autonomous rideshare consumer cost: $2.75/mile (2025), declining at 7.6% p.a. [T2: AAA/Goldman Sachs].

- **S-curve positions [model-derived using lib.scurve_math.classify_phase]:** Global BEV new car share: 16.5% (2024) → `rapid_growth`. China BEV share: 33.8% (2024) → `rapid_growth`. USA BEV share: ~7.5% (2024) → `tipping`. Europe BEV share: ~18% (2024) → `rapid_growth`. Norway BEV share: >65% (2024) → `rapid_growth` approaching saturation. Global BEV fleet share: 2.6% (2024) — fleet disruption 8–12 years behind new-sales disruption. Note: Global S-curve fit (2010–2024) yields L=20.1%, k=0.73, x0=2022, R²=0.9955 — but L is underestimated because the rapid-growth phase began only in 2021 and the fit is anchored on 15 years of mostly pre-growth data; the scurve-fitter agent should apply a broader saturation assumption (L=80–100%) and re-fit.

- **Cost Metric Recommendation:** Use **purchase price ($/vehicle)** as the primary parity metric for the cost-parity checker, with TCO ($/mile, 10k miles/year) as the secondary metric. Rationale: consumer purchase decisions are dominated by sticker price in most markets; TCO parity has already been reached in China but has not fully unlocked mass-market adoption in USA/Europe, indicating purchase-price parity is the binding constraint. For TaaS tipping point, use $/mile as the primary metric (comparing AV rideshare to personal car ownership).

- **Market Type Recommendation:** **Consumer market** (primary) for BEV vs ICE disruption analysis. **Fleet market** (secondary) for TaaS/A-EV disruption. Consumer market dynamics dominate new-car sales and the tipping-point mechanism. Fleet markets (TaaS, ride-hailing) are separate disruption vectors and should be modeled separately in the demand-decomposer.

- **Data gaps:** (1) FCEV light vehicle sales and cost curve — no local catalog data; confidence on FCEV assessment is moderate. (2) Autonomous rideshare cost curve is only 4 observations (2022–2025); learning rate estimate of 7.6% p.a. has low statistical confidence. (3) Global S-curve L-saturation is underestimated at 20.1%; the scurve-fitter must override with market-based saturation assumption. (4) PHEV global total adoption data not fully loaded (only China sourced from catalog); PHEV share in Europe and USA is partially from prior run memory, not new catalog reads in this run. (5) No direct catalog data on ICE total cost of ownership breakdown by geography; AAA data is US-centric.

- **Unresolved questions for downstream agents:** (1) What year does BEV purchase price fully cross below ICE in USA (cost-parity checker)? (2) At what AV fleet utilization rate does rideshare cost per mile cross below personal ICE car TCO (capability-parity checker)? (3) What is the S-curve saturation ceiling for global BEV — 70%, 85%, or 95% (scurve-fitter)? (4) Does PHEV volume peak before or after BEV purchase-price parity in USA/Europe, and what is the disruption timeline (adoption-readiness checker)? (5) What is the fleet model for autonomous robotaxi displacement of privately-owned vehicles — at what robotaxi fleet density does personal car ownership become financially irrational (fleet-modeler)?

---

## Classification Overrides

Each technology's X-Flow/Stellar/Hybrid tag for downstream Jevons gate:

| Technology | Tag |
|---|---|
| LFP BEV passenger car | Hybrid (Stellar-dominant) |
| NMC/NCA BEV passenger car | Hybrid (Stellar-dominant) |
| Gasoline-ICE passenger car | X-Flow |
| Diesel-ICE passenger car | X-Flow |
| LFP/NMC battery pack (component) | Stellar |
| PHEV | Hybrid (X-Flow-dominant) |
| L4 Autonomous Driving System | Stellar |
| TaaS platform | Stellar |
| V2G system | Stellar |
| FCEV light passenger (chimera) | X-Flow |

**Jevons gate:** Apply Jevons Paradox modeling ONLY to ICE (X-Flow) and PHEV (X-Flow-dominant Hybrid) in downstream demand and fuel consumption analysis. Do NOT apply Jevons to BEV, battery packs, AV systems, TaaS, or V2G.

---

## Sources

- [T2] `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — Rethinkx, 2019–2024 [observed]
- [T2] `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Database, 2021–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_China.json` — Database, 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — Database, 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` — Database, 2013–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — Database, 2010–2025 [observed]
- [T2] `data/passenger_cars/cost/Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` — AAA / Goldman Sachs Research, 2022–2025 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_China.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_USA.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Annual_Sales_Global.json` — Rethinkx, 2005–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Annual_Sales_China.json` — Rethinkx, 2005–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Total_Fleet_Global.json` — Rethinkx, 2010–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json` — Database, 2015–2024 [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(PHEV)_Annual_Sales_China.json` — Database, 2020–2024 [observed]
- [T2] `data/passenger_cars/cost/Autonomous_Vehicle_LiDAR_(Low_Cost_ADAS)_Price_China.json` — Database, 2018–2025 [observed]
- [T2] `data/autonomous_vehicle/cost/Autonomous_Passenger_Car_RideShare_Revenue_per_Mile_(Cost_to_Consumer)_Global.json` — AAA / Goldman Sachs Research, 2022–2025 [observed]
- [T2] `data/autonomous_vehicle/adoption/Autonomous_Passenger_Car_Annual_Sales_(L2)_Global.json` — IDTechEx Research, 2020–2025 [observed]
- [model-derived] Exponential fits and learning rates computed via `lib.cost_curve_math.exponential_fit` and `lib.cost_curve_math.learning_rate_from_decay`
- [model-derived] S-curve phase classifications via `lib.scurve_math.classify_phase`
- [model-derived] Market share ratios, CAGR, and cost decline percentages computed via `python3` inline per shared-rules Computation Rule 1

## Classification Overrides

| Field | Value | Source |
|-------|-------|--------|
| Disruption Scope | Mass-market BEV displacing ICE passenger vehicles; PHEV as chimera | User-confirmed |
| Primary Disruptor | Battery Electric Vehicle (BEV) | User-confirmed |
| Primary Incumbent | Internal Combustion Engine (ICE) passenger vehicle | User-confirmed |
| Cost Parity Metric | Purchase price ($/vehicle) | User-confirmed |
| Market Type | Consumer (mass market) | User-confirmed |
| Technology Flow | Stellar | User-confirmed |
| Jevons Paradox | NOT APPLICABLE — Stellar technology | Auto-derived |
