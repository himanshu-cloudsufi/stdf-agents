# Migration Analysis: LEAD / COMMODITIES Sector

**Source Systems:** Old Skills System (lead, lithium-ion, copper skills) + Old Agent Prompts
**Target System:** STDF v2 Pipeline (stdf-agents/stdf/)
**Compiled:** 2026-03-27
**Scope:** Lead (primary), Copper (secondary), Lithium-Ion Batteries (cross-commodity)

---

## 1. OLD SYSTEM ANALYSIS

### 1.1 Old Lead Report (family3-lead-report.txt)

The old lead report is a comprehensive, pre-computed analytical document containing 1,000+ lines of tabulated data spanning the full lead demand disruption thesis. It covers:

**Demand Model (12 Drivers, D01-D12):**
- D01: SLI Passenger Cars (4,202 kt, 39% of battery lead) -- the single largest driver
- D02: SLI Commercial Vehicles (2,955 kt, 27%)
- D03-D10: Minor battery drivers (EV auxiliary, 2W/3W starters, forklifts, datacenter/telecom VRLA)
- D11-D12: Residual buckets (other stationary 1,830 kt, other motive 731 kt) -- top-down from ILZSG, NOT bottom-up
- Non-battery uses (1,691 kt, 13%) held flat
- Calibrated total: 13,130 kt (ILZSG-aligned, including 660 kt residual gap)

**Supply-Demand Balance:**
- Table A (annual surplus only): surplus begins 2029
- Table B (cumulative stockpile with inventory carryover): surplus begins **2026**
- Primary supply + secondary supply (recycling at 99% rate)
- 10% surplus year: 2026 in both Base and TaaS scenarios
- Available surplus percentages projected through 2040 (reaching 70,000%+ cumulative)

**Cost Curves (Full Year-on-Year 2015-2040):**
- Li-ion SLI vs Lead-Acid AGM by region (China, USA, Europe, RoW) -- Section 3A
- Li-ion EV Aux vs Lead-Acid SLI by region -- Section 3B
- Two/Three-Wheeler pack costs -- Section 3C
- Generic pack-level Li-ion vs LAB ($/kWh) -- Section 3.0
- EV vs ICE vehicle cost parity curves for all regions (passenger cars, LCV, MCV, HCV) -- Appendix C

**Tipping Points:**
- ICE SLI: China 2025, USA/Europe/RoW 2029
- EV Auxiliary: China 2025, USA/Europe/RoW 2028
- 2W/3W Chemistry: China 2023, USA 2019, Europe 2018, RoW 2019
- Vehicle cost parity: China 2022, USA 2025, Europe 2024, RoW 2032

**Fleet Modeling:**
- OEM vs Replacement split for D01 and D02 (85% replacement, 15% OEM for passenger cars)
- Stock-flow formulas: IB(t+1) = IB(t) + Sales(t) - Scrappage(t)
- Explicit lead coefficients: 11.5 kg (passenger ICE), 22.0 kg (CV), 2.5 kg (2W), 7.0 kg (3W)
- Battery life 4.5 years, vehicle lifetimes 12-20 years by type

**TaaS Scenario:**
- Transport-as-a-Service overlay affecting D01 and D03
- Grand Total Base: 12,470 kt (2024) -> 3,734 kt (2040)
- Grand Total TaaS: 12,470 kt (2024) -> 3,538 kt (2040)

**Disruption Mechanisms (ranked):**
1. Vehicle electrification (ICE fleet shrinks)
2. Battery chemistry substitution (Li-ion replaces LAB in remaining ICE)
3. TaaS acceleration (compresses electrification timeline)

### 1.2 Old Lithium-Ion Skill (lithium_ion_subagent_system.txt + skills system)

The lithium-ion subagent is a demand forecasting engine covering:

**Capabilities:**
- Lithium-ion battery demand (GWh) by segment and region
- OEM vs replacement demand accounting
- EV adoption curves and tipping points
- Pack size evolution by vehicle segment
- Fleet stock-flow modeling
- Lead-acid to lithium-ion transition timelines
- Grid BESS, UPS, forklift, and auxiliary battery demand
- TaaS demand implications
- Lead-acid battery demand (kt) by 12 drivers (D01-D12)
- Li-ion vs LAB cost curves and tipping points by region

**Architecture (deployed skill):**
- Pre-computed report file: 1,800+ lines covering all segments
- Analysis scripts: 13 individual Python scripts (passenger_cars_analysis.py, two_wheeler_analysis.py, etc.)
- Shared library: analysis_utils.py for S-curve fitting, charting, data loading
- 11 data files (JSON): Battery_Pack, Commercial_Vehicle, Datacenter_UPS, Energy_Storage, Forklift, Lead, Passenger_Cars, Telecom_UPS, Three_Wheeler, Two_Wheeler, Variable_Cost
- Config: regions (China, USA, Europe, Rest_of_World), cutoff 2024, horizon 2040

**Methodology (5-Step Framework):**
1. Tipping Point Detection -- cost curve crossing
2. S-Curve Fitting -- Differential Evolution optimization on historical data
3. Demand Calculation -- OEM + Replacement
4. Fleet Tracking -- Stock-flow with scrappage
5. Regional Aggregation

**Operating Principles:**
- SKILL FIRST: always use canonical methodology
- Evidence grounded: every number from skill output or labeled as derived
- Segment granularity: EV (BEV/PHEV by class), grid BESS, UPS, forklifts, 12V auxiliary, lead-acid replacement, TaaS
- Stock-flow accounting: OEM vs replacement
- Pre-computed context: strict no-fabrication rule when using report data

### 1.3 Old Copper Skill (copper_forecast_subagent_system.txt + skills system)

The copper subagent is a demand forecasting engine covering:

**4-Category Model:**
1. Transportation -- bottom-up S-curve (EV 3-4x copper intensity vs ICE)
2. Grid Generation -- bottom-up capacity (solar 5.0 t/MW, onshore wind 4.0 t/MW, offshore wind 9.5 t/MW)
3. Grid T&D -- proportional to total capacity with dynamic SWB share
4. Legacy Residual -- total minus above (construction, industrial, electronics)

**Copper Intensity Coefficients (kg/vehicle):**
- ICE: 23 (passenger), 35 (commercial), 3 (2W), 4 (3W)
- BEV: 83 (passenger), 120 (commercial), 4 (2W), 5 (3W)
- PHEV: 60 (passenger) -- chimera modeled

**Full Python Codebase:**
- 13 source modules: tipping_point.py, scurve.py, stock_flow.py, chimera.py, transportation.py, grid_generation.py, grid_td.py, legacy_residual.py, reconciliation.py, data_loader.py, config.py, utils.py
- Complete dependency graph documented
- S-curve fitting with Differential Evolution (maxiter=1000, tol=1e-8)
- Chimera model for PHEV/NGV transitional shares
- Full data pipeline: tipping -> S-curve -> shares -> fleet -> copper per category
- Output: final forecast (CSV+JSON), intermediate step files, summary reports

### 1.4 Old Agent Prompt Methodology

Both the lithium-ion and copper subagents follow the same pattern:
- **SKILL FIRST:** Always use the skill's canonical methodology -- never mentally calculate
- **NO FABRICATION:** If data unavailable, say so
- **Tool Budget:** seba_research (up to 5), web_fetch (up to 5), code_execution
- **Pre-computed context:** When report data is provided, use it faithfully (NO_FABRICATION_BEYOND_REPORT_DATA)
- **Output format:** Structured analytical text with segment/regional breakdowns

### 1.5 Strengths of the Old System

1. **Deep domain knowledge in the lead report:** 12-driver decomposition with complete year-on-year data 2015-2040 for all cost curves, S-curve shares, and demand figures. The level of detail (every individual driver, every region, every year) is exceptional.

2. **Supply-side modeling:** The old lead report contains Table A (annual surplus) and Table B (cumulative stockpile) -- genuine supply-demand balance models with primary supply, secondary supply (recycling), and byproduct dynamics. This is the ONLY place in the entire system where supply is modeled.

3. **Recycling dynamics:** 99% battery recycling rate explicitly modeled. Recycling as secondary supply that persists even as demand drops, creating the recursive surplus loop.

4. **Byproduct supply recognition:** Lead as a byproduct of zinc mining -- primary supply cannot be shut off when demand drops. This is the core of the "recursive disruption" that Tony calls the canonical template.

5. **Cost curve granularity:** Pack-level and unit-level cost curves for 4 regions, 3 market segments (ICE SLI, EV Aux, 2W/3W), with separate Li-ion and LAB tracks.

6. **Copper code maturity:** A complete, executable Python forecasting system with 13 source modules, full dependency graph, Differential Evolution S-curve fitting, chimera modeling, and grid T&D calculation.

7. **Lithium-ion cross-commodity link:** The lithium-ion skill explicitly models lead-acid demand (D01-D12) as the inverse of Li-ion adoption -- cross-commodity validation built in.

8. **TaaS scenario separation:** Base vs TaaS consistently tracked as parallel scenarios.

### 1.6 Weaknesses of the Old System

1. **Static pre-computed reports:** The lead report is a snapshot. No mechanism for auto-refresh or real-time data updates. Tony demanded "auto-refresh data for lead model expected by next week" (Mar 26).

2. **Skill isolation:** Each skill (lead, lithium-ion, copper) operates independently. No cross-commodity pipeline. The lithium-ion skill's lead demand analysis is a separate code path, not integrated with the lead skill.

3. **No daily supply/demand tracking:** Tony specifically wants "tracking every day" for commodities. The old system produces annual projections only.

4. **No price collapse model:** The old system projects surplus percentages but does not model the price mechanism. Tony wants "when it falls off a cliff" and "when the price is gonna just go negative." There is no price model.

5. **No recycling decline modeling in supply:** Tony explicitly said "do NOT model recycling decline" -- but the old system doesn't model supply dynamics at all in a way that shows the recursive surplus acceleration. The supply model is rudimentary.

6. **Residual buckets (D11+D12) are opaque:** 2,561 kt (24% of battery lead) modeled top-down from ILZSG residuals, not bottom-up. No sub-application data.

7. **No recursive feedback loop formalization:** The old report describes the recursive loop qualitatively ("falling Li-ion costs -> EV adoption -> lead surplus -> can't cut supply -> price collapse -> further switch") but does not model it computationally as a feedback loop.

8. **No convergence between old prompts and skills:** The subagent system prompts reference skills but the actual skill methodology is separate from the prompts. Data hand-off is fragile.

---

## 2. NEW STDF PIPELINE ANALYSIS

### 2.1 Lead-Demand-Decline Output

The new STDF v2 pipeline ran a FULL+COMMODITY configuration (16 agents) on the lead disruption question, producing 16 agent outputs plus a final synthesis. Key outputs:

**Final Synthesis (00-final-synthesis.md):**
- Pipeline Confidence: 0.82
- Rupture Window: 2027-2028
- 2024 observed baseline: 12,259 kt
- 10% threshold (11,033 kt) crossed in 2027 (median)
- 7-phase narrative covering sector scoping, technology inventory, convergence, disruption pattern, business model shift, adoption/S-curve dynamics, and synthesis

**Agent Outputs (agents/ directory):**
- 01: Domain disruption -- 5 disruption vectors, 10 market products, 2024 baseline
- 02a: Cost researcher -- Li-ion and lead-acid cost histories (T1/T2)
- 02b: Cost fitter -- Exponential fit R^2=0.954, 16.81%/yr learning rate
- 03: Capability -- 13-dimension matrix, 11/13 MET
- 04a-d: Parity checkers + tipping synthesizer
- 05a: S-curve fitter -- 5-segment fits (BEV new-car, BEV fleet, telecom, datacenter, forklift)
- 05b: Regional adopter -- China 4.1yr ahead of USA in BEV
- 05c: X-curve analyst -- China smelter death spiral ACTIVE (22-35% utilization)
- 07a: Demand decomposer -- 10-product tree, 99.98% coverage, 12,256 of 12,259 kt
- 07b: Stream forecaster -- 3-stream projections (incumbent, disruptor=0, chimera PHEV hump)
- 07c: Fleet modeler -- 4 fleet models (ICE cars, forklifts, telecom, 2W), OEM/replacement split
- 07d: Regional demand analyst -- 5 regions (China, USA, Europe, India, RoW)

**Eval Audit (EVAL_AUDIT_REPORT.md):**
- 8/10 eval criteria PASS, 2 WARN (non-blocking)
- Addresses 3 prior failed attempts (T-25, T-26, T-27) where data was fabricated, 12V SLI disruption was missed, and banned vocabulary was used
- All numbers now trace to T1/T2 catalog files or model-derived computations via lib/ functions

### 2.2 The Commodity Demand Chain

The STDF v2 pipeline runs a 4-agent commodity chain (Tier 6):

**Agent 1: Demand Decomposer (stdf-demand-decomposer)**
- Decomposes total commodity demand into market products recursively
- Material intensity coefficients (kg/unit) per market product by technology variant
- Validates >= 80% demand coverage
- Core equation: `Demand_commodity(t) = SUM_i [Sales_i(t) * MI_i]`
- GDP-proxy reasoning is BANNED
- Uses empirical data catalog (956 curves)
- Compliance: 3 CRITICAL, 1 HIGH criteria

**Agent 2: Stream Forecaster (stdf-stream-forecaster)**
- Projects three parallel demand streams: incumbent declining, disruptor growing, chimera hump
- `I(t) = Total_market(t) * (1 - S_disruptor(t) - C(t)) * MI_incumbent`
- Pure math agent -- no web search
- S-curve integration from upstream fitter
- Confidence intervals via Monte Carlo (N=1,000 draws)
- Jevons Paradox classification (X-Flow vs Stellar)

**Agent 3: Fleet Modeler (stdf-fleet-modeler)**
- Stock-flow fleet models: `Fleet(t+1) = Fleet(t) + Sales(t) - Scrappage(t)`
- OEM vs replacement demand split with explicit lifetimes
- Stock-flow consistency verification
- Pure math agent

**Agent 4: Regional Demand Analyst (stdf-regional-demand-analyst)**
- Disaggregates global demand by region
- Region-specific S-curve parameters, material intensity, market sizes
- MAY use web search for region-specific data

### 2.3 demand_math.py Library

The `lib/demand_math.py` provides pre-built functions:

1. `decompose_demand()` -- validate >= 80% coverage
2. `material_intensity_demand()` -- units * intensity calculation
3. `stock_flow_fleet()` -- fleet evolution projection
4. `oem_replacement_split()` -- OEM vs replacement demand
5. `aggregate_demand_by_technology()` -- sum across incumbent/disruptor/chimera streams
6. `regional_demand_split()` -- global-to-regional disaggregation
7. `validate_stock_flow_consistency()` -- verify fleet accounting balances
8. `scurve_demand_projection()` -- S-curve-based demand projection

### 2.4 How the New Pipeline Handles Lead vs. the Old System

**What's better:**

1. **Systematic 15-agent pipeline:** The new system runs a rigorous 7-tier DAG with 15+ agents cross-checking each other. The old system was a monolithic pre-computed report with no pipeline verification.

2. **3-stream decomposition:** The new pipeline explicitly tracks incumbent (declining), disruptor (zero lead content), and chimera (PHEV hump) as separate streams. The old system mixed these implicitly.

3. **Formal tipping point analysis:** 3 separate condition checkers (cost parity, capability parity, adoption readiness) feed into a tipping synthesizer. The old system had tipping points as static table values without a systematic derivation chain.

4. **X-curve analysis:** The new pipeline includes incumbent decline dynamics with death spiral modeling. China smelter utilization at 22-35% is quantified. The old system had no equivalent.

5. **Confidence scores and Monte Carlo:** Every agent reports confidence; the stream forecaster runs 1,000 Monte Carlo simulations with P10/P25/P50/P75/P90 bands. The old system had point estimates only.

6. **Eval audit trail:** The new pipeline has a formal evaluator agent that checks all STDF guardrails. The eval audit documents 3 prior failed attempts and their resolution.

7. **STDF vocabulary and guardrails:** Banned vocabulary enforcement, no hedging, required declarative tone. The old system had no such governance.

8. **India as separate region:** The new pipeline models India as a 5th region (vs. "Rest of World" in the old system), recognizing India's structural difference (64% of demand in 2W/3W).

**What's missing:**

1. **SUPPLY-SIDE MODEL:** The new pipeline has ZERO supply-side modeling. No primary supply (byproduct of zinc mining), no secondary supply (recycling), no supply-demand balance, no cumulative stockpile projection. This is the single largest gap.

2. **No 12-driver granularity:** The old system had 12 named drivers (D01-D12) with consistent labeling and complete year-by-year data. The new system decomposes into 10 market products but uses different naming and grouping.

3. **No cost curve year-on-year data:** The old system had full 2015-2040 cost curves for every segment/region. The new system has cost-researcher observations and exponential fits but not the same granular year-on-year tables.

4. **No TaaS scenario:** The new pipeline does not model TaaS as a separate scenario. The old system explicitly ran Base vs TaaS comparisons.

5. **No price collapse timing:** Neither system models the price mechanism, but the old system at least had surplus percentages that implied timing. The new system focuses purely on demand decline.

6. **Different baselines:** Old system: 13,130 kt calibrated to ILZSG (including 660 kt unmodeled residual). New system: 12,259 kt from RethinkX catalog. The 871 kt gap is the calibration residual.

7. **No daily tracking framework:** The new pipeline runs as one-time analysis. No mechanism for the daily supply/demand tracking Tony demands.

---

## 3. STAKEHOLDER EXPECTATIONS (From Meetings)

### 3.1 Tony's Canonical Template

Tony selected lead as the canonical template for recursive disruption modeling because of its unique dynamics:

> "If we can get the lead disruption right, it's a good template to get other disruptions right. That's why I'm emphasizing lead -- because of the recursive nature of that disruption." (Mar 20)

The recursive loop: Falling lithium-ion battery costs -> EV adoption -> displacement of lead-acid batteries -> lead surplus -> lead cannot be cut (byproduct + recycling) -> surplus grows -> price collapse -> further acceleration of switch to lithium-ion.

### 3.2 Cumulative Stockpile View (Table B)

Tony confirmed: **use the cumulative stockpile view** (Table B), not annual-only (Table A).

- Table A (annual surplus only) shows surplus arriving in 2029
- Table B (cumulative stockpile with inventory carryover) shows surplus in **2026 (this year)**
- Tony: "Supply will increase as demand drops, and that's what makes this trade work."

### 3.3 Tipping Points

- China tipping point: **2026** (lithium-ion SLA batteries cheaper than lead-acid)
- Other countries tipping point: **~2029**
- These are cost parity tipping points for battery chemistry substitution

### 3.4 No Cost Floors on Battery Projections

Tony interrupted forcefully on this topic:

> "Wrong wrong. Do not do that, please." (Mar 20, on cost floors)
> "Cost curves are like gravity, and they will continue until of course they don't... it's not up to you or me to determine when that is the case." (Mar 20)

No raw-material-cost-based floors on lithium-ion projections. Let the cost curve run. The Moore's Law analogy: people at Intel in 1992 said the curve couldn't continue, and it's still going.

Bug fix noted: linear projection was driving lithium-ion SLA costs to $0 in USA 2040. Fixed to $12.

### 3.5 No Recycling Decline Modeling

Tony explicitly said: **do NOT model recycling decline.** The point is to see when the surplus overwhelms the market. Recycling continues at full capacity -- that is part of what makes the surplus accelerate.

### 3.6 "When Does It Fall Off a Cliff?" -- Price Collapse Timing

> "I want to understand when it's going to fall off a cliff. That's what I really want to understand. Because that's when the price is gonna just go negative." (Mar 26)

The surplus progression: 10% oversupply becomes 20%, then 80%, then 90%. "At some point folks are gonna be like, okay, take it at any cost."

### 3.7 Byproduct Dynamics

Lead is a byproduct of zinc mining. Primary supply **cannot be shut off** when lead demand drops -- miners produce lead whether they want to or not, because they are mining zinc. This means:
- Supply is structurally inelastic to demand
- Falling demand + constant supply = accelerating surplus
- Combined with 99% recycling rate = double supply inelasticity

### 3.8 Copper as Opposite Dynamic (Bottleneck)

> "In the case of copper, the supply will not scale as quickly as the demand will." (Mar 26)

Copper is the mirror image of lead:
- Lead: supply cannot shrink, demand collapses -> surplus -> price collapse
- Copper: demand grows (electrification), supply cannot scale (mining timelines, permitting) -> deficit -> price spike
- Daily tracking to identify when bottlenecks emerge before the market sees them

### 3.9 Lithium-Ion as the Disrupting Force

Lithium-ion batteries are the common disruptor across all three commodities:
- **Lead:** Li-ion displaces lead-acid batteries (the commodity itself becomes unnecessary)
- **Copper:** Li-ion enables EVs which use 3-4x more copper (increases demand)
- The cost curve (no floors, no intervention) is the driving force

---

## 4. GAP ANALYSIS

### Rating Key
- **COVERED:** Fully addressed by the new STDF pipeline with equivalent or better quality
- **PARTIAL:** Addressed but with material gaps compared to old system or stakeholder expectations
- **MISSING:** Not addressed at all in the new pipeline

| # | Capability | Rating | Notes |
|---|-----------|--------|-------|
| 1 | Lead demand decomposition (SLI vs EV auxiliary segments) | **PARTIAL** | New pipeline has 10 market products (99.98% coverage) but uses different naming than old D01-D12 system. Old system had SLA vs EV Aux cost curves explicitly separated; new system groups these differently. Old system had 12 drivers with consistent labels; new has 10 products with different labels. |
| 2 | Lead primary supply (byproduct of zinc mining) | **MISSING** | The new STDF pipeline has ZERO supply modeling. No zinc byproduct dynamics, no primary supply projection. The old system had a supply-demand balance table. Tony's canonical recursive disruption template REQUIRES supply modeling. |
| 3 | Lead secondary supply (recycling, 99% rate) | **MISSING** | No recycling supply model in the new pipeline. The old system modeled secondary supply from vehicle/battery retirements. Tony confirmed "do NOT model recycling decline" but expects recycling volume to be tracked as part of persistent supply. |
| 4 | Cumulative stockpile inventory model | **MISSING** | Tony confirmed Table B (cumulative) is required. Neither old nor new system has a proper cumulative inventory model in the pipeline -- the old report had static tables. The new pipeline does not attempt this at all. |
| 5 | Surplus progression -> price collapse prediction | **MISSING** | No price model exists in either system. But the old system had surplus percentages (10% -> 20% -> 80% -> 90%) that implied timing. The new pipeline has only demand decline, not surplus/price. Tony specifically wants "when it falls off a cliff." |
| 6 | Lead tipping point identification (China 2026) | **PARTIAL** | New pipeline identifies China as first to cross 10%-from-2026 threshold (~2028.1) but this is demand decline, not cost parity tipping. Old system had explicit China 2025 (SLI) and 2025 (EV Aux) cost parity years. The numbers differ because they measure different things. |
| 7 | Recursive disruption loop modeling | **MISSING** | The new pipeline describes the disruptor virtuous cycle and incumbent vicious cycle qualitatively (tipping-synthesizer), and the x-curve analyst documents China's smelter death spiral. But there is no computational feedback loop where surplus-driven price collapse accelerates switching. The recursive loop is identified but not modeled. |
| 8 | Lithium-ion battery cost curves (no floors) | **COVERED** | The new pipeline's cost-fitter produces exponential fits with 16.81%/yr learning rate. No cost floors imposed. The cost-researcher gathers T1/T2 data. Quality is equivalent or better than old system due to formal fitting methodology. |
| 9 | Copper demand from electrification (SWB, EVs) | **PARTIAL** | A partial copper-demand-electrification pipeline run exists (agents/ directory with 7 files through adoption-readiness). The old copper skill has a complete 4-category model with full Python codebase. The new pipeline covers the same ground in principle (demand-decomposer -> stream-forecaster) but the copper run is incomplete. |
| 10 | Copper supply constraints (mining timelines, permitting) | **MISSING** | Neither system models copper supply. The old copper skill was demand-only. Tony wants daily supply/demand tracking -- supply modeling is entirely absent. |
| 11 | Copper bottleneck timing | **MISSING** | Tony: "identify when bottlenecks may emerge before they emerge." No bottleneck prediction model exists in either system. Requires supply modeling plus demand projections. |
| 12 | Regional demand disaggregation (China, US, EU) | **COVERED** | The new pipeline's regional-demand-analyst provides 5-region breakdown (China, USA, Europe, India, RoW) with region-specific S-curve parameters. This is better than the old system's 4-region approach (China, USA, Europe, RoW) because India is separated. Confidence 0.74 due to T3-only segments. |
| 13 | Fleet modeling (vehicle stock-flow, OEM vs replacement) | **COVERED** | The new pipeline's fleet-modeler builds 4 fleet models with formal stock-flow consistency checks. The old system had the same formulas. Both use Fleet(t+1) = Fleet(t) + Sales(t) - Scrappage(t). New system adds consistency validation via lib.demand_math. |
| 14 | 3-stream demand (incumbent declining, disruptor growing, chimera hump) | **COVERED** | The new pipeline's stream-forecaster explicitly tracks 3 streams. The disruptor stream is identically 0 for lead (BEV/LFP contain no lead). Chimera (PHEV) hump peaks at 72 kt in 2031. This is structurally superior to the old system which mixed streams implicitly. |
| 15 | Daily supply/demand tracking for trading | **MISSING** | Neither system supports daily tracking. Tony: "We want to track every day." The old system produced annual forecasts. The new pipeline runs as one-time analysis. This requires a fundamentally different architecture (data feeds, monitoring, alerts). |
| 16 | Cross-commodity linkages (lithium -> EV -> lead, copper -> SWB) | **PARTIAL** | The new pipeline's domain-disruption agent identifies convergence vectors (Li-BEV, LFP-UPS, EV-FL) and the tipping-synthesizer notes cross-segment manufacturing subsidies. But there is no formal cross-commodity pipeline where the lithium-ion model feeds into lead and copper models simultaneously. The old lithium-ion skill had a lead_demand_analysis.py for cross-validation, but it was a separate code path, not an integrated pipeline. |

### Summary Scorecard

| Rating | Count | Items |
|--------|-------|-------|
| COVERED | 5 | Li-ion cost curves, regional disaggregation, fleet modeling, 3-stream demand, S-curve methodology |
| PARTIAL | 4 | Lead demand decomposition, tipping point identification, copper demand, cross-commodity links |
| MISSING | 7 | Primary supply (byproduct), secondary supply (recycling), cumulative stockpile, surplus/price collapse, recursive loop model, copper supply/bottleneck, daily tracking |

The MISSING items cluster around **supply-side dynamics** and **real-time tracking** -- precisely the features that Tony considers the core of the lead trade thesis and the Stellar Edge product vision.

---

## 5. MIGRATION PLAN

### 5.1 What Data and Methodology from the Old Lead Skill Should Migrate

**Must migrate (high value, not replicated in new pipeline):**

1. **Supply-Demand Balance Model (Tables A and B)**
   - Primary supply projection (zinc byproduct dynamics)
   - Secondary supply projection (recycling at 99% rate, tied to fleet retirement volumes)
   - Cumulative stockpile calculation with inventory carryover
   - Surplus percentage progression (10% -> 20% -> 80% -> 90%)
   - Source: family3-lead-report.txt Tables A and B, plus lead_demand_forecasting_instructions.md formulas

2. **12-Driver Naming Convention (D01-D12)**
   - Consistent driver labels that Tony's team is trained on
   - Mapping from new 10-product decomposition to old D01-D12 taxonomy
   - Source: lead_taxonomy_and_datasets.json

3. **Full Year-on-Year Cost Curves**
   - Li-ion SLI vs LAB AGM by region (2015-2040)
   - Li-ion EV Aux vs LAB SLI by region (2015-2040)
   - Vehicle cost parity curves (EV vs ICE) by region
   - These granular tables are valuable for visualization and validation
   - Source: family3-lead-report.txt Appendix C

4. **TaaS Scenario Framework**
   - Base vs TaaS side-by-side projections
   - TaaS impacts on D01 and D03
   - Source: family3-lead-report.txt Section 9

**Should migrate (moderate value, partially replicated):**

5. **Lead Coefficients (kg/unit)**
   - Old: 11.5 kg (passenger ICE), 22.0 kg (CV), 2.5 kg (2W), 7.0 kg (3W)
   - New: 13.0 kg (passenger), 17.9 kg (CV), 8.3 kg (2W), 7.8 kg (3W)
   - Different values due to different derivation methods. Reconciliation needed.

6. **Copper Code Modules**
   - 13 Python source modules from the copper forecast skill
   - Particularly: chimera.py, scurve.py, stock_flow.py, transportation.py, grid_generation.py, grid_td.py
   - Methodology is sound and could be adapted to new pipeline

### 5.2 What the New STDF Commodity Chain Already Provides

The new pipeline already delivers:

1. **Rigorous demand decomposition** with 99.98% coverage and formal compliance criteria
2. **3-stream forecasting** (incumbent/disruptor/chimera) with Monte Carlo confidence intervals
3. **Fleet stock-flow modeling** with formal consistency verification
4. **Regional disaggregation** (5 regions including India)
5. **Full disruption analysis pipeline** (15 agents, 7 tiers, formal DAG)
6. **Guardrails and vocabulary enforcement** (banned terms, data provenance)
7. **Eval audit** with documented resolution of prior failures
8. **S-curve fitting** with Differential Evolution and R-squared reporting
9. **X-curve analysis** (incumbent decline dynamics, death spiral identification)
10. **Tipping condition synthesis** (cost parity, capability parity, adoption readiness)

### 5.3 What Must Be Built

**Priority 1 -- Supply-Side Surplus Model (CRITICAL -- enables core trade thesis)**

Build a **lead supply model** that integrates with the demand-decomposer output:

```
Supply(t) = Primary_Supply(t) + Secondary_Supply(t)
Primary_Supply(t) = f(zinc_production(t))  -- byproduct, structurally inelastic
Secondary_Supply(t) = Recycled_Lead(t) = Retired_Batteries(t) * Recycling_Rate * Lead_Content
Retired_Batteries(t) = Fleet_Scrapped_Units(t) * Lead_per_Battery  -- from fleet-modeler
Annual_Surplus(t) = Supply(t) - Demand(t)
Cumulative_Stockpile(t) = Cumulative_Stockpile(t-1) + Annual_Surplus(t)
Surplus_Pct(t) = Cumulative_Stockpile(t) / Annual_Demand(t) * 100
```

Key parameters:
- Zinc production growth rate (historical CAGR from ILZSG)
- Lead-to-zinc ratio in primary production
- Recycling rate: 99% (per Tony's directive, do NOT model decline)
- Lead content per retired battery (from fleet-modeler's scrapped units)

Output: Surplus percentage progression with 10%/20%/50%/80%/90% threshold crossing years.

**Priority 2 -- Recursive Disruption Loop Model (HIGH -- Tony's canonical template)**

Build a feedback loop that connects:
1. Li-ion cost curve -> EV adoption S-curve -> Lead demand decline
2. Lead surplus -> Lead price decline (simple supply/demand to price mapping)
3. Lead price decline -> Li-ion cost advantage widened -> Accelerated switching
4. Accelerated switching -> Larger surplus -> Further price decline

This could be implemented as an iterative model where each cycle's output feeds the next cycle's input. Does not need to be a separate agent -- could be a post-processing step in the synthesizer or a new lib module.

**Priority 3 -- Copper Supply Constraint Model (MEDIUM -- separate commodity)**

For copper, build the mirror-image model:
- Demand projection (already exists in pipeline)
- Supply projection (mine production, project timelines, permitting delays)
- Deficit/surplus timing
- Bottleneck identification

**Priority 4 -- Cross-Commodity Pipeline Orchestration (MEDIUM)**

Enable running lead, copper, and lithium-ion analyses in a connected pipeline where:
- Lithium-ion cost projections feed into lead demand decline AND copper demand growth
- Lead surplus feeds back into Li-ion cost advantage
- Copper bottleneck feeds into EV production constraints

### 5.4 Recommended Architecture

**Option A (Recommended): Extend existing agents + new lead-specific agent**

1. Create `stdf-supply-modeler.md` agent in `.claude/agents/`:
   - Reads: demand-decomposer output (demand by segment), fleet-modeler output (fleet retirements)
   - Computes: primary supply (zinc byproduct), secondary supply (recycling), total supply
   - Outputs: annual surplus, cumulative stockpile, surplus percentage progression
   - Compliance criteria: supply-demand balance accuracy, cumulative accounting consistency

2. Add supply data to `data/` directory:
   - Zinc production by region (historical + forecast)
   - Lead primary production historical series
   - Lead recycling volumes historical series
   - ILZSG supply data

3. Add `supply_math.py` to `lib/`:
   - `byproduct_supply()` -- zinc-linked primary lead production
   - `recycling_supply()` -- battery retirement * recycling rate * lead content
   - `surplus_stockpile()` -- annual surplus + cumulative inventory
   - `surplus_threshold_years()` -- when surplus hits 10%, 20%, 50%, etc.

4. Extend `lib/demand_math.py` with:
   - `recursive_disruption_loop()` -- iterative feedback between surplus, price, and adoption acceleration

5. Update Agent Registry to include stdf-supply-modeler in the DAG:
   - Tier: After fleet-modeler (Tier 6.5)
   - Requires: 07a-demand-decomposer, 07c-fleet-modeler
   - Outputs: 08-supply-modeler.md

6. Extend synthesizer template to include supply-demand balance section in 00-final-synthesis.md

**Option B (Alternative): New lead-specific standalone agent**

Create a standalone lead disruption agent that combines demand, supply, and recursive dynamics in a single agent. Simpler but loses the modularity of the pipeline.

**Recommendation: Option A.** The supply model should be modular because it can be reused for other byproduct commodities and the opposite model (supply constraints) for copper.

### 5.5 Data Requirements

| Data Source | Type | Priority | Notes |
|-------------|------|----------|-------|
| ILZSG global refined lead supply (historical) | Time series | P1 | For supply model calibration |
| Global zinc mine production (historical) | Time series | P1 | For byproduct supply projection |
| Lead/zinc co-production ratio | Parameter | P1 | Typically ~0.3-0.4 tonnes lead per tonne zinc |
| Lead recycling volumes by source (historical) | Time series | P1 | For secondary supply calibration |
| Lead price history (LME) | Time series | P2 | For price collapse model |
| Copper mine production by project (historical + pipeline) | Time series | P3 | For copper supply model |
| Copper mine project timelines | Reference | P3 | For copper bottleneck prediction |

### 5.6 Effort Estimate

| Work Item | Complexity | Estimated Effort | Dependencies |
|-----------|-----------|-----------------|--------------|
| Supply-modeler agent definition | Medium | 2-3 days | Agent registry update |
| supply_math.py library | Medium | 2-3 days | demand_math.py patterns |
| Supply data ingestion (ILZSG, zinc production) | Medium | 2-3 days | Data sourcing |
| Recursive disruption loop model | High | 3-5 days | Supply model complete |
| D01-D12 mapping / reconciliation | Low | 1 day | Old report reference |
| TaaS scenario reintegration | Low | 1-2 days | Fleet-modeler extension |
| Pipeline integration + testing | Medium | 2-3 days | All above |
| Copper supply constraint model | High | 3-5 days | Separate data sourcing |
| Cross-commodity orchestration | High | 3-5 days | All commodity models |
| Daily tracking architecture design | Very High | 5-10 days | Separate architecture |

**Total estimated effort:**
- **Phase 1 (supply + recursive loop for lead): 10-15 days**
- **Phase 2 (copper supply + cross-commodity): 8-12 days**
- **Phase 3 (daily tracking): 10-15 days (architectural change)**

### 5.7 Migration Sequence

1. **Immediate:** Migrate old lead report's supply-demand balance data as reference data into `stdf/data/lead/supply/`
2. **Week 1-2:** Build supply-modeler agent + supply_math.py + integrate into DAG
3. **Week 2-3:** Build recursive disruption loop model, re-run lead pipeline with supply integration
4. **Week 3-4:** Reconcile D01-D12 naming, add TaaS scenario, validate against old report figures
5. **Week 4-5:** Copper supply model, cross-commodity linkages
6. **Week 5+:** Daily tracking architecture (separate workstream)

---

## APPENDIX: File Reference

### Old System Files
- `/archive/old_prompts/sector_reports/family3-lead-report.txt` -- Complete old lead report (1,000+ lines)
- `/archive/old_prompts/lithium_ion_subagent_system.txt` -- Lithium-ion agent prompt
- `/archive/old_prompts/copper_forecast_subagent_system.txt` -- Copper agent prompt

### Skills System Files
- `/skills/skill-instructions/Lead/lead_demand_forecasting_instructions.md` -- Lead demand formulas
- `/skills/skill-instructions/Lead/lead_taxonomy_and_datasets.json` -- D01-D12 taxonomy
- `/skills/skill-instructions/lithium-ion/` -- Full lithium-ion skill (config, docs, lib, data, scripts)
- `/skills/skill-instructions/Copper/copper_forecast/` -- Full copper forecast skill (src, data, config)
- `/skills/.claude/skills/copper-forecast/SKILL.md` -- Deployed copper skill definition
- `/skills/.claude/skills/lithium-ion-demand/SKILL.md` -- Deployed lithium-ion skill definition

### New STDF Pipeline Files
- `/stdf/output/lead-demand-decline/00-final-synthesis.md` -- Final lead analysis
- `/stdf/output/lead-demand-decline/agents/` -- All 16 agent outputs
- `/stdf/output/lead-demand-decline/EVAL_AUDIT_REPORT.md` -- Evaluation audit
- `/stdf/.claude/agents/stdf-demand-decomposer.md` -- Demand decomposer agent
- `/stdf/.claude/agents/stdf-stream-forecaster.md` -- Stream forecaster agent
- `/stdf/.claude/agents/stdf-fleet-modeler.md` -- Fleet modeler agent
- `/stdf/.claude/agents/stdf-regional-demand-analyst.md` -- Regional demand analyst agent
- `/stdf/lib/demand_math.py` -- Demand math library
- `/stdf/shared-rules.md` -- STDF vocabulary and guardrails

### Meeting Notes
- `/archive/meetings/consolidated_sector_commodity.md` -- Sections 1 (Lead), 2 (Copper), 3 (Lithium)
- `/archive/meetings/consolidated_tony_vs_robert.md` -- Tony's demands and priorities
