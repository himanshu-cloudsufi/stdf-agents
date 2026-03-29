# Energy Sector Migration Analysis: Old System -> Skills -> STDF v2 Pipeline

**Compiled:** 2026-03-27
**Scope:** SWB disruption modeling, merit order dispatch, gas supply decomposition, LNG displacement, oil demand, fossil fuel demand decline, correlation monitoring, portfolio tracking
**Files Reviewed:** 28 files across 4 systems (old agent prompt, old sector report, skills system, STDF v2 pipeline)

---

## 1. OLD SYSTEM ANALYSIS

### 1a. Old Energy Agent Prompt (`energy_sector_subagent_system.txt`)

The old agent prompt defines a single-agent SWB forecasting engine with 5 operating principles:

1. **SKILL FIRST** -- always use the energy-sector skill for generation and demand calculations
2. **EVIDENCE GROUNDED** -- every number from skill output or explicitly labeled as derived
3. **MERIT ORDER LOGIC** -- highest marginal cost displaced first
4. **DEMAND GROWTH DRIVERS** -- model EV, datacenter, heat pump demand growth
5. **YoY CAPACITY GROWTH** -- use historical CAGR, NOT S-curves for SWB capacity

The agent covers solar/wind/battery generation, electricity demand growth, generation mix evolution, coal/gas displacement sequencing, and renewable penetration trajectories.

**Workflow:** Read query -> run skill -> extract outputs -> supplement with web research if needed -> present results.

**Output requirements:** Generation in TWh, displacement sequencing, demand decomposition, penetration trajectories, all numbers labeled as SKILL OUTPUT or DERIVED.

**Tool budget:** 5 seba_research calls, 5 web_fetch calls, code execution for skill processing.

**Pre-computed context rules:** Strict no-fabrication policy when report data is provided. Two modes: format-only (no skill run) and supplement (skill fills gaps).

### 1b. Old Sector Report (`family2-energy-report.txt`)

The old report is a comprehensive 870-line document covering 10 sections:

| Section | Content |
|---------|---------|
| S00 | Full generation time series -- all regions, all years 2025-2040, all sources (SWB, Non-SWB, Coal, Gas) |
| S01 | Disruption map -- disruptor/incumbent identification, displacement sequence, demand drivers, chimeras |
| S02a | SWB cost curves -- solar LCOE 2010-2024, wind LCOE 2010-2024, battery pack cost 2010-2024, Wright's Law projections |
| S02b | Fossil fuel marginal costs by region -- merit order per region |
| S02c | Nuclear and hydrogen gap analysis |
| S03 | Installed capacity and capacity curves -- solar PV, onshore wind, offshore wind, battery storage, capacity factors |
| S04 | Adoption curves -- SWB generation TWh by year per region, curve phase identification |
| S05 | Tipping points -- absolute TWh milestones per region, fossil-free dates, SWB exceeds demand dates |
| S06 | Demand decomposition -- full time series (Baseline + EV + DC + HP) per region |
| S07 | Feedback loops -- 5 reinforcing (R1-R5), 5 balancing (B1-B5), net assessment |
| S08 | Confidence -- parameter sensitivity, external benchmarks |
| S09 | Provenance -- data sources, model parameters, methodology |
| S10 | Anti-patterns and compliance |

**Key data points produced:**
- Global SWB: 5,239 TWh (2025) -> 260,373 TWh (2040)
- Fossil-free dates: China 2031, Europe 2035, USA 2036, RoW 2037, Global 2037
- Gas exit: China already 0, Europe 2033, RoW 2034, USA 2036
- Coal exit: China 2031, USA 2032, Europe 2035, RoW 2037
- Demand growth: 28,221 TWh (2025) -> 54,849 TWh (2040), +94%
- Top demand driver: heat pumps (~6,800 TWh incremental by 2040)
- Regional marginal costs: Coal $35-50/MWh, Gas $35-70/MWh by region

### 1c. Skill Implementation (Skills System)

**Architecture:** Self-contained Python skill with 7 source modules, 3 config files, 5 data files, validation baseline.

**Source modules:**
- `generation.py` -- Steps 1-3: raw solar/wind generation from capacity x CF x 8760, battery energy from solar capacity x duration, total SWB = solar + wind + battery
- `displacement.py` -- Steps 6-11: non-SWB derivation from historical residuals, residual demand calculation, displacement weights, merit order allocation, market shares. Includes BOTH proportional allocation AND displacement-first logic.
- `forecast.py` -- blended CAGR (3yr/5yr/10yr equal weight 0.333)
- `load_data.py` -- JSON data loading from `data/` directory
- `output.py` -- JSON result output
- `calculate_ev_electricity_demand.py` -- EV fleet x kWh/vehicle/year
- `calculate_total_electricity_demand.py` -- baseline + EV + DC + HP

**Config:**
- `parameters.yaml` -- capacity factors (solar 0.11-0.15, wind onshore 0.21-0.32, wind offshore 0.38-0.42), marginal costs (coal $35-50, gas $35-70), battery duration (China 2h, others 4h), forecasting weights
- `regions.yaml` -- China, USA, Europe, Rest_of_World
- `entities.yaml` -- entity list

**Data files:** Electricity.json, Energy_Generation.json, Energy_Storage.json, EV_Electricity_Demand.json, Total_Electricity_Demand.json, plus fleet/ directory (4 vehicle type files).

**Validation:** Baseline comparison data in `validation/baseline/` (swb_results.json, EV_Electricity_Demand.json, Total_Electricity_Demand.json).

**Deployed skill (`.claude/skills/energy-sector/`):** Mirror of the skill instructions with identical lib/, data/, config/ structure. Entry point is `run_forecast.py` which wraps `scripts/analysis/run_analysis.py`.

**Spec (`SWB_ANALYSIS_SPEC.md`):**
- Step 0: Total_Demand = Baseline + DC + EV
- Steps 1-3: SWB generation from capacity x CF + battery energy
- Steps 4-5: Non-SWB derived from historical, forecasted via blended CAGR
- Steps 6-8: Residual = Total_Demand - SWB - Non_SWB; displacement-first merit order allocation
- Steps 9: Market shares

### 1d. Strengths and Weaknesses

**Strengths:**
- Deterministic, reproducible pipeline (`python3 run_forecast.py`)
- Self-contained data (no external API dependencies at runtime)
- Well-documented 9-step methodology with formal spec
- Proper displacement-first merit order logic
- Comprehensive demand decomposition (baseline + EV + DC + HP)
- Regional granularity (China, USA, Europe, RoW)
- Anti-double-count rule for incremental demand
- China solar CF = 0.11 correction explicitly enforced
- Validation baseline for regression testing

**Weaknesses:**
- **Single monolithic skill** -- no separation between dispatch modeling, gas supply decomposition, and cost analysis
- **No gas supply source decomposition** -- reports total gas displacement in GWh but does not decompose into domestic/pipeline/LNG
- **No LNG displacement cascade** -- critical gap for Tony's LNG portfolio positions
- **No oil demand modeling** -- energy sector skill covers electricity only, not petroleum
- **YoY CAGR only, no S-curve fitting** -- the old agent prompt explicitly says "use YoY capacity growth rates, NOT S-curves"
- **No cost parity analysis** -- reports LCOE history but does not compute parity dates
- **No tipping point framework** -- no SIBA-style three-condition analysis
- **No feedback loop quantification** -- qualitative only (S07)
- **No correlation monitoring** -- no oil/gas price tracking
- **No geopolitical modeling** -- Iran war, Ukraine, Trump/TTF correlation completely absent
- **No portfolio position tracking** -- not designed for daily monitoring
- **No SWB stack cost (SCOE)** -- battery cost curve tracked but SCOE not computed
- **Curtailment not modeled** -- SWB can exceed 100% of demand with no consequence in model
- **No non-power gas demand** -- skill covers only power generation gas, not heating/industrial/feedstock
- **No emerging market tracking** -- Pakistan zero-to-18GW example cannot be analyzed

---

## 2. NEW STDF PIPELINE ANALYSIS

### 2a. What the New System Produces for Energy

**Bloom Energy SOFC analysis (ENERGY_FULL pipeline, 14 agents):**

Produced 14 agent output files plus final synthesis. Energy-specific outputs:
- `08a-energy-dispatch.md` (confidence 0.71) -- adapted the 9-step pipeline to distributed on-site dispatch (site-level merit order: solar -> BESS -> Bloom SOFC -> grid -> diesel). Computed BESS duration pathway, SWB coverage fractions, LCOE crossover schedule, displacement timeline.
- `08b-gas-supply.md` (confidence 0.82) -- converted Bloom fleet gas consumption (1.756 BCM) using explicit GWh->BCM formula with Bloom-specific 0.58 SOFC efficiency (not default 0.45 CCGT). Decomposed US gas demand by sector. Covered China and Europe LNG displacement for macro context.
- Final synthesis computed: rupture window 2031-2032, pipeline confidence 0.702, 63-73% downside from current market cap.

**Oil-Gas Outlook analysis (FULL+COMMODITY pipeline, 16 agents):**

Produced 16 agent output files plus final synthesis. Key outputs:
- Multi-vector disruption (V1: BEV vs ICE, V2: Solar vs gas, V3: ASHP vs gas heating)
- Oil demand: 103.4 mb/d (2024) -> 87.7 (2031) -> 75.8 (2036) -> 73.0 (2046)
- Gas demand: 3,935 bcm (2026) -> 3,497 (2031) -> 2,920 (2036) -> 2,601 (2046)
- Disruption-eligible demand: 49.0 mb/d oil (47.4%), 2,378 bcm gas (58.0%)
- Structural floor: 54.4 mb/d oil, 1,725 bcm gas (petrochemicals, industrial, aviation, marine)
- Peak oil: 2024-2026, gas structural peak: 2030-2032
- OCGT peaker collapse: 410 bcm -> 9 bcm by 2046 (98% decline)
- Missing agents: fleet-modeler and regional-demand-analyst (HIGH degradation, -0.30 confidence penalty)

### 2b. The Energy Dispatch Pipeline

The `stdf-energy-dispatch` agent implements the canonical 9-step SWB merit order dispatch pipeline:

1. **Total Demand** = Baseline (blended CAGR) + incremental EV + incremental DC + incremental HP
2. **SWB Generation** = Total_Demand x SWB_Share (from upstream S-curve fitter, NOT CAGR)
3. **Non-SWB Baseline** = historical residual (hydro + nuclear + biomass), extrapolated via blended CAGR
4. **Residual Demand** = Total_Demand - SWB - Non_SWB
5. **Load Regional Marginal Costs** from `dispatch_parameters.json`
6. **Merit Order Dispatch** -- cheapest fuel fills residual first; expensive fuel displaced first
7. **Displacement Schedule** -- per-fuel displacement at +5/+10/+20yr horizons
8. **Reserve Floors** -- coal 10%, gas 15% of peak historical
9. **Energy Balance Validation** -- generation = demand within +/-2%

**Key improvement over old system:** SWB share comes from S-curve fitter (logistic L/k/x0), not blended CAGR extrapolation. This is a fundamental methodological upgrade.

The `stdf-gas-supply-decomposer` agent extends dispatch output:
- Converts gas GWh displaced -> BCM using explicit formula (GWh x 3.6 / (35.3 x efficiency))
- Decomposes gas supply by source per region (domestic -> pipeline -> LNG)
- Models LNG displacement cascade (most expensive displaced first)
- Includes non-power gas demand (heating, industrial, feedstock)
- Identifies structural gas floor (~15% as petrochemical feedstock)
- Assesses LNG exporter vulnerability (Venture Global, Woodside, NextDecade vs Cheniere)

### 2c. The energy_math.py Library

15 computational functions:

| Function | Purpose |
|----------|---------|
| `merit_order_dispatch()` | Cheapest-first residual allocation with reserve floors |
| `displacement_schedule()` | Per-fuel displacement from SWB growth (expensive first) |
| `swb_generation()` | SWB generation stack by component (solar/wind/battery fractions) |
| `energy_balance_check()` | Validate generation = demand within +/-2% |
| `scoe()` | Storage Cost of Energy calculation |
| `swb_stack_cost()` | MAX(Solar_LCOE, Wind_LCOE) + SCOE |
| `battery_sizing()` | Solar_Capacity_GW x Duration_hours |
| `blended_cagr()` | Equal-weight 3yr/5yr/10yr CAGR |
| `gwh_to_bcm()` | Gas generation to BCM conversion |
| `supply_source_ordering()` | Gas supply by displacement priority |
| `lng_displacement_cascade()` | LNG import reduction by source origin |
| `ev_charging_demand()` | Fleet x kWh/vehicle/year |
| `datacenter_demand()` | Base TWh x (1+CAGR)^years |
| `heat_pump_demand()` | COP-adjusted heat pump electricity |
| `full_energy_dispatch()` | Complete pipeline in one call |

### 2d. How It Differs from the Old System

| Dimension | Old System (Skill) | New System (STDF v2) |
|-----------|-------------------|---------------------|
| **Architecture** | Single monolithic Python script | 2 specialized agents (dispatch + gas supply) within 23-agent DAG |
| **SWB projection method** | Blended CAGR extrapolation of capacity | S-curve fitting (logistic L/k/x0 from scurve-fitter) |
| **Gas supply decomposition** | Not present | Full domestic/pipeline/LNG decomposition per region |
| **LNG displacement cascade** | Not present | Modeled per region with cost-based priority ordering |
| **Non-power gas demand** | Not present | Heating (24%), industrial (25%), feedstock (15%) included |
| **Oil demand modeling** | Not present | Full oil demand decomposition via commodity chain agents |
| **Cost parity analysis** | LCOE history reported | Formal parity date computation with three-condition framework |
| **Tipping point framework** | Not present | Three-condition SIBA: cost parity + capability parity + adoption readiness |
| **Energy balance** | Not explicitly validated | CRITICAL compliance criterion (8.1) -- pipeline stops if balance fails |
| **Reserve floors** | Not present | Coal 10%, gas 15% minimum of peak historical |
| **SCOE computation** | Not present | Full battery storage cost of energy |
| **SWB stack cost** | Not present | MAX(Solar_LCOE, Wind_LCOE) + SCOE |
| **Dispatch parameters** | parameters.yaml (4 regions) | dispatch_parameters.json (5 regions incl. India, plus LNG cascade, emission factors, demand growth vectors) |
| **Upstream integration** | Standalone skill | Reads S-curve parameters, cost curves, capability assessments from upstream agents |
| **Downstream integration** | Terminal output | Feeds gas-supply-decomposer, then synthesizer |
| **Compliance framework** | Anti-pattern checks (informal) | Formal compliance criteria with severity levels (CRITICAL/HIGH/MEDIUM) |
| **Vocabulary rules** | None | Enforced banned/required vocabulary (e.g., "stellar energy" not "renewable energy") |

### 2e. What's Better, What's Missing

**What's better in STDF v2:**
- S-curve-based SWB projections (methodologically superior to CAGR extrapolation)
- Gas supply source decomposition and LNG displacement cascade (critical for Tony's LNG positions)
- Formal energy balance validation as CRITICAL compliance criterion
- Multi-agent architecture allows each agent to focus on its domain
- Integration with full STDF pipeline (cost curves, capability, tipping points, adoption, X-curve)
- Oil demand modeling via commodity chain agents
- Reserve floors for grid stability realism
- SCOE and SWB stack cost computation
- Comprehensive dispatch_parameters.json with India, emission factors, LNG cascade config
- File-based I/O enables reproducibility and audit trail

**What's missing from STDF v2 (present in old system):**
- The old system's deterministic `python3 run_forecast.py` script produced a single reproducible JSON output. The new system's agents produce markdown reports with embedded tables -- less machine-parseable.
- The old system's full 16-year time series per region (every year 2025-2040) is extremely detailed. The new system's agents tend to report +5/+10/+20yr snapshots rather than year-by-year tables.
- The old system's self-contained data directory with fleet outputs allowed offline execution. The new system relies on 956 empirical curves in the data catalog but some agents still need web research for current data.
- Validation baseline (old system had `validation/baseline/swb_results.json` for regression testing). No equivalent in STDF v2 for energy agents yet.

---

## 3. STAKEHOLDER EXPECTATIONS (from meetings)

### 3a. Tony's Demands for LNG Analysis

Tony is emphatic that ANY LNG analysis MUST include SWB cost curves as the disrupting force:

> "To go off and do an analysis of LNG without doing cost curves of solar wind and battery and so on, doesn't add anything." (Mar 20)

This is the SIBA framework mandate -- every energy query must start from the disruption framework (solar/wind/battery cost curves -> merit order displacement -> gas demand decline -> LNG demand decline), not from supply/demand balances or price forecasting.

**Specific requirements:**
- Solar, wind, battery cost curves as the disruptive technologies in every fossil fuel analysis
- Merit order dispatch to determine which fuel is displaced first
- Gas supply source decomposition (domestic -> pipeline -> LNG) to show LNG is the marginal, most expensive source
- LNG displacement cascade showing which exporter is hit first (US LNG highest cost)

### 3b. Oil/Gas Price Correlation Tracking

> "Oil and gas price correlations broke simultaneously around beginning of the year, before the war started." (Mar 20)
> "If we had tracked just those three things [oil, EU gas, US gas], we would have detected that oil prices had been going up since January 1st to end of Feb, even before the war started." (Mar 26)
> "Correlations breaking is a huge investment opportunity for us." (Mar 26)

Tony wants:
- Daily tracking of oil prices, EU natural gas (TTF), US natural gas (Henry Hub)
- Correlation monitoring between oil and gas prices
- Alert when correlations break (leading indicator of geopolitical events)
- Trump social media / TTF price correlation mapping

### 3c. Pakistan Solar Example

> "In Pakistan it went from essentially zero to 18 gigawatts of solar in a 30 gigawatt grid. The stock exchange tripled." (Mar 26)

Tony uses Pakistan as the canonical example of exponential distributed scaling vs. incremental grid scaling. Requires:
- Country-level solar PV and battery importation/installation tracking
- Rupture point detection at 5-10% market penetration
- Stock market correlation with solar penetration milestones

### 3d. Rupture Point Monitoring

> "Rupture points at 5-10% market share when new is cheaper than old." (Mar 26)

Tony wants monitoring of when countries/regions hit the 5-10% SWB penetration threshold where disruption becomes self-reinforcing. This maps directly to the S-curve "tipping" phase identification in the STDF pipeline.

### 3e. Daily Portfolio Tracking for Energy Positions

> "For the LNG positions... we want to track oil prices every day. We want to track natural gas prices in Europe and natural gas prices in the US." (Mar 26)

This is the portfolio monitoring module requirement:
- Each energy position gets 5-10 daily tracking metrics
- LNG: oil prices, TTF, Henry Hub
- Correlation break detection as automated alerts
- Proactive, unprompted insights ("the software prompts us")

### 3f. SIBA Framework as Mandatory for Any Energy Query

> "It's important to always do the SIBA framework... that's not optional." (Mar 11)
> "That is our edge. And if we don't do it, then we're not doing anything." (Mar 20)

SIBA (Seba Investment and Business Architecture) = the STDF framework in different nomenclature. Every energy query must:
1. Start with cost curves (solar, wind, battery)
2. Identify the disruption flow (Stellar energy vs. X-Flow incumbents)
3. Compute tipping conditions (cost parity, capability parity, adoption readiness)
4. Model S-curve adoption
5. Project demand destruction via merit order displacement
6. Decompose supply-source impacts

---

## 4. GAP ANALYSIS

### Rating Scale
- **COVERED**: Fully functional in new STDF v2 pipeline with tested output
- **PARTIAL**: Capability exists but incomplete, degraded, or not yet validated against stakeholder needs
- **MISSING**: Not present in any system; must be built from scratch

| # | Capability | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 1 | SWB cost curve analysis (solar, wind, battery) | **COVERED** | `stdf-cost-researcher` + `stdf-cost-fitter` agents produce solar LCOE (-13.5%/yr), battery (-15.8%/yr), SCOE, SWB stack cost. `energy_math.py` has `scoe()` and `swb_stack_cost()` functions. Bloom analysis shows full cost crossing tables. |
| 2 | Merit order dispatch modeling | **COVERED** | 9-step pipeline fully implemented in `stdf-energy-dispatch` agent. `energy_math.py` has `merit_order_dispatch()`, `displacement_schedule()`, `full_energy_dispatch()`. Reserve floors applied. Energy balance validation as CRITICAL criterion. Tested in Bloom SOFC output (site-level dispatch) and referenced in oil-gas output. |
| 3 | Gas supply source decomposition (domestic/pipeline/LNG) | **COVERED** | `stdf-gas-supply-decomposer` agent implements full decomposition. `dispatch_parameters.json` has `gas_supply_source_ordering` for China (5 sources), Europe (4 sources), USA (3 sources). `energy_math.py` has `supply_source_ordering()`. Tested in Bloom output (China 107.64 BCM LNG, USA domestic shale). |
| 4 | LNG displacement cascade | **COVERED** | `stdf-gas-supply-decomposer` + `dispatch_parameters.json` `lng_displacement_priority` config. `energy_math.py` has `lng_displacement_cascade()`. Europe: US LNG first, Qatar second, Norwegian last. China: Spot LNG first, Australian second, Qatar third, pipeline last. Tested in Bloom output. |
| 5 | Oil disruption modeling | **PARTIAL** | Oil-gas-outlook analysis produced comprehensive oil demand decomposition (103.4 mb/d across 12 market products), stream forecasting (99.6 -> 73.0 mb/d by 2046), peak oil timing (2024-2026). However: fleet-modeler and regional-demand-analyst agents were MISSING in the run (-0.30 confidence), and there is no dedicated oil disruption agent. Oil analysis piggybacked on the commodity chain (demand-decomposer + stream-forecaster), not a purpose-built oil dispatch equivalent. |
| 6 | Fossil fuel demand decline (coal, gas, oil separately) | **PARTIAL** | Coal and gas tracked separately per region in the energy dispatch pipeline. Gas further decomposed by end-use (power gen 40%, industrial 20%, heating 14%, commercial 4%, petrochemicals 12%). Oil decomposed across 12 market product categories. However: coal demand decline is only in the electricity generation context -- no industrial coal, metallurgical coal, or coal-to-chemicals tracking. Gas decline covers all end-uses. Oil decline misses fleet-modeler precision. |
| 7 | Renewable scaling tracking (by country) | **PARTIAL** | Regional-adopter agent tracks V1 and V2 adoption S-curves for China, Europe, USA, Rest of World. Solar generation share per region computed (China 9.03%, Europe 10.48%, USA 6.07% in 2024). BUT: tracking is at the 4-region level, not country-level. Pakistan-style individual country tracking (Tony's explicit demand) is NOT supported. No country-level import/installation data pipeline. |
| 8 | Grid vs distributed scaling asymmetry | **PARTIAL** | Bloom analysis explicitly modeled distributed on-site dispatch separately from grid-scale dispatch. Tony's insight that "distributed and batteries can scale at a way faster pace than the existing grid" is acknowledged in the Bloom SOFC analysis (data center direct SWB adoption vs. grid interconnection queues). However: this is not formalized as a separate analytical module. No systematic tracking of distributed vs. centralized deployment rates by country. |
| 9 | Geopolitical impact modeling (Iran war, Ukraine) | **MISSING** | No geopolitical modeling capability in any system. The oil-gas-outlook analysis makes no mention of Iran, Ukraine, or geopolitical supply disruptions. The LNG meeting notes specifically reference the Iran war causing price spikes from ~20 to 50-60 (echoing Ukraine's ~20 to 200 pattern). No agent handles geopolitical supply shock scenarios. No Trump/TTF correlation analysis capability. |
| 10 | Real-time price tracking (oil, gas, TTF) | **MISSING** | No real-time data feed capability. The STDF pipeline uses historical observed data from JSON files and web research at analysis time. Tony demands daily tracking of oil prices, EU natural gas (TTF), US natural gas (Henry Hub). This requires a persistent data ingestion pipeline, not an on-demand analysis framework. The `dispatch_parameters.json` has static marginal costs, not live prices. |
| 11 | Correlation monitoring (oil/gas, Trump/TTF) | **MISSING** | No time-series correlation analysis capability. Tony specifically wants: (a) oil/gas price correlation tracking, (b) correlation break detection as alerts, (c) Trump social media / TTF price mapping. None of these exist in any system. This is the "Stellar Sense" product requirement -- autonomous, unprompted monitoring. |
| 12 | Pakistan/emerging market solar tracking | **MISSING** | No country-level emerging market solar penetration tracking. Tony's canonical example (Pakistan: zero to 18 GW in a 30 GW grid, stock exchange tripled) requires: country-level solar import data, installation tracking, grid capacity data, stock market correlation, rupture point detection. None of this exists. The regional-adopter agent works at 4-region granularity (China/USA/Europe/RoW). |
| 13 | Energy balance validation | **COVERED** | Formal CRITICAL compliance criterion (8.1) in the energy-dispatch agent. `energy_math.py` `energy_balance_check()` validates generation = demand within +/-2%. Pipeline STOPS if this fails. Fully tested in Bloom output. |
| 14 | Regional dispatch differences | **COVERED** | `dispatch_parameters.json` encodes different marginal costs per region (e.g., USA: gas $35 < coal $40, so gas runs as baseload; China: coal $35 < gas $70, so gas displaced first). The energy-dispatch agent requires minimum China, USA, Europe coverage. India added in dispatch_parameters.json. |
| 15 | Portfolio-level energy position monitoring | **MISSING** | No portfolio tracking module exists. Tony (Mar 26): "We need a module for portfolio -- each position and 5 or 7 or 10 things that we should be tracking every day." LNG positions require daily oil, TTF, Henry Hub tracking with correlation break alerts. This is entirely outside the current STDF pipeline architecture, which is designed for one-shot disruption analysis, not continuous monitoring. |

### Summary Counts

| Rating | Count | Items |
|--------|-------|-------|
| COVERED | 6 | SWB cost curves, merit order dispatch, gas supply decomposition, LNG cascade, energy balance, regional dispatch |
| PARTIAL | 4 | Oil disruption, fossil fuel demand decline, renewable scaling tracking, grid vs distributed asymmetry |
| MISSING | 5 | Geopolitical modeling, real-time price tracking, correlation monitoring, emerging market tracking, portfolio monitoring |

---

## 5. MIGRATION PLAN

### 5a. What Can Be Migrated from Old Skill -> New STDF Agents

The old skill's core computational pipeline has ALREADY been migrated and upgraded:

| Old Skill Component | STDF v2 Equivalent | Status |
|--------------------|--------------------|--------|
| `src/generation.py` (Steps 1-3) | `lib/energy_math.py: swb_generation(), battery_sizing()` | MIGRATED + UPGRADED (S-curve input instead of CAGR) |
| `src/displacement.py` (Steps 6-11) | `lib/energy_math.py: merit_order_dispatch(), displacement_schedule()` | MIGRATED + UPGRADED (reserve floors added) |
| `src/forecast.py` (blended CAGR) | `lib/energy_math.py: blended_cagr()` | MIGRATED (identical methodology) |
| `src/calculate_ev_electricity_demand.py` | `lib/energy_math.py: ev_charging_demand()` | MIGRATED |
| `src/calculate_total_electricity_demand.py` | `lib/energy_math.py: datacenter_demand(), heat_pump_demand()` | MIGRATED |
| `config/parameters.yaml` | `data/energy_sector/config/dispatch_parameters.json` | MIGRATED + EXPANDED (India added, LNG cascade, emission factors) |
| `data/*.json` (5 files) | `data/` catalog (956 empirical curves) | SUPERSEDED (10x more data) |
| `validation/baseline/` | No equivalent yet | NOT MIGRATED (gap) |

**Remaining migration items from old skill:**
1. **Validation baseline** -- the old `validation/baseline/swb_results.json` provides regression testing. The new system should have equivalent validation for the energy dispatch agent output.
2. **Year-by-year time series** -- the old system produced every-year tables (2025-2040) for all regions. The new agents tend to report snapshots (+5/+10/+20yr). Consider adding year-by-year output format to energy-dispatch agent.
3. **Deterministic execution** -- `python3 run_forecast.py` gave the same output every time. The new agent-based approach introduces LLM non-determinism. Consider adding a `scripts/run_energy_dispatch.py` deterministic wrapper that uses `energy_math.py` functions directly.

### 5b. What the New Energy Dispatch Chain Already Provides

The STDF v2 energy chain (Tier 7: energy-dispatch -> gas-supply-decomposer) already provides everything the old system did, plus substantial additions:

**Fully operational (tested with real pipeline runs):**
- 9-step merit order dispatch pipeline with S-curve integration
- Gas supply source decomposition (domestic/pipeline/LNG) per region
- LNG displacement cascade with cost-based priority ordering
- GWh-to-BCM conversion with explicit formula and configurable efficiency
- Non-power gas demand segmentation (heating, industrial, feedstock)
- LNG exporter vulnerability assessment
- Energy balance validation (CRITICAL compliance)
- Reserve floor enforcement
- SCOE and SWB stack cost computation
- Integration with upstream S-curve, cost, capability, and tipping agents
- File-based I/O for reproducibility

**Operational but needing refinement:**
- The Bloom SOFC analysis adapted the dispatch pipeline to site-level (distributed) dispatch -- this adaptation was ad hoc. A formal "distributed dispatch" variant could be templated.
- The oil-gas-outlook ran without fleet-modeler and regional-demand-analyst, causing significant confidence degradation (-0.30). These agents need to be validated for oil/energy analyses.

### 5c. What Must Be Built Fresh

Five capabilities are MISSING and must be built from scratch. These align directly with Tony's Mar 20 and Mar 26 demands:

#### 1. Geopolitical Impact Modeling
**What:** Scenario engine for supply disruption events (Iran war -> LNG price spike, Ukraine -> TTF spike, OPEC cuts).
**Why:** Tony: "What's relevant today is the Iran war." Robert uses the system to trade LNG positions during geopolitical events.
**Approach:** Create a `stdf-geopolitical-scenario` agent that models supply shock impacts on energy prices. Inputs: event type (war, sanctions, OPEC cut), affected supply volume (mb/d or bcm), duration estimate. Output: price impact range, portfolio position implication.
**Data requirements:** Historical geopolitical event impacts (Ukraine 2022 TTF spike data, Iran 2026 LNG spike data, OPEC production cut history).
**Effort:** Medium (2-3 weeks). Mostly prompt engineering + reference document creation. No new math library needed.

#### 2. Real-Time Price Tracking
**What:** Daily ingestion of oil (Brent, WTI), gas (Henry Hub, TTF, JKM), and solar/battery spot prices.
**Why:** Tony (Mar 26): "We want to track oil prices every day. We want to track natural gas prices in Europe and natural gas prices in the US."
**Approach:** This is a data infrastructure requirement, not an agent requirement. Options:
  - Bloomberg API (Tony confirmed credentials available, Mar 11)
  - Free alternatives: EIA API (US gas/oil), ENTSOG (EU gas), Ember (solar capacity)
  - Store in `data/prices/` as daily time series JSON
  - Create `scripts/fetch_energy_prices.py` cron job
**Data requirements:** Bloomberg or equivalent API credentials. Daily price feeds for 5-8 instruments.
**Effort:** Medium (2-3 weeks for infrastructure). Ongoing maintenance.

#### 3. Correlation Monitoring and Break Detection
**What:** Automated detection of correlation breaks between energy price pairs (oil/gas, Trump/TTF).
**Why:** Tony (Mar 20): "Oil and gas price correlations broke simultaneously around beginning of the year, before the war started." Tony (Mar 26): "Correlations breaking is a huge investment opportunity for us."
**Approach:** Create `lib/correlation_monitor.py` with:
  - Rolling correlation computation (30-day, 90-day windows)
  - Break detection (correlation drops below 2-sigma threshold)
  - Alert generation when breaks detected
  - Historical correlation chart generation
**Data requirements:** Depends on real-time price tracking (item 2 above). Minimum 2 years of daily price history for baseline correlation.
**Effort:** Small (1 week for math library). Depends on real-time price tracking being built first.

#### 4. Emerging Market Solar Penetration Tracking
**What:** Country-level solar import/installation data tracking with rupture point detection.
**Why:** Tony (Mar 26): "In Pakistan it went from essentially zero to 18 gigawatts of solar in a 30 gigawatt grid." Tony wants to track this pattern replicating in other emerging markets.
**Approach:**
  - Add country-level data to `data/` catalog (IRENA publishes country-level capacity data annually)
  - Create `scripts/emerging_market_scanner.py` that computes solar penetration % per country
  - Flag countries approaching 5-10% penetration threshold (Tony's "rupture point")
  - Track import data from customs/trade databases where available
**Data requirements:** IRENA country-level capacity data (publicly available). Trade data for solar panel imports by country (potentially paywalled).
**Effort:** Medium (2-3 weeks). Data sourcing is the bottleneck.

#### 5. Portfolio Position Monitoring Module
**What:** Per-position daily tracking dashboard with configurable metrics and alerts.
**Why:** Tony (Mar 26): "We need a module for portfolio -- each position and 5 or 7 or 10 things that we should be tracking every day." This is the "Stellar Sense" vision -- "the software prompts us."
**Approach:** This is a product module, not an agent. Architecture:
  - Position registry (JSON config: position name, direction, entry date, key metrics to track)
  - Daily metric fetcher (depends on real-time price tracking)
  - Alert engine (threshold crossings, correlation breaks, STDF model deviations from observed)
  - Output: daily digest file or push notification
**Data requirements:** Depends on items 2 and 3 above. Also needs position data from Tony/Robert.
**Effort:** Large (4-6 weeks). This is a new product module, not a pipeline enhancement.

### 5d. Data Requirements and Sources

| Capability | Data Source | Access | Priority |
|-----------|-----------|--------|----------|
| Energy dispatch (existing) | 956 empirical curves in `data/` catalog | In-repo | Already available |
| Dispatch parameters (existing) | `dispatch_parameters.json` | In-repo | Already available |
| Real-time oil prices | Bloomberg API or EIA API | Bloomberg credentials available (Mar 11) | HIGH -- Tony demands daily tracking |
| Real-time gas prices (TTF, Henry Hub) | Bloomberg or ICE/NYMEX public feeds | Bloomberg credentials or API signup | HIGH -- core LNG position monitoring |
| Country-level solar capacity | IRENA Renewable Capacity Statistics | Public download | MEDIUM -- emerging market tracking |
| Solar panel trade/import data | UN Comtrade or national customs databases | Potentially paywalled | MEDIUM -- Pakistan-style tracking |
| Geopolitical event database | Custom compilation from historical events | Manual initially | LOW -- can start with 5-10 canonical events |
| Trump social media feed | Twitter/Truth Social API | Public/API | LOW -- novel correlation, may not persist |
| Stock market data by country | Bloomberg or Yahoo Finance | Bloomberg or free API | LOW -- for Pakistan stock exchange correlation |

### 5e. Effort Estimate

| Item | Effort | Dependencies | Priority |
|------|--------|-------------|----------|
| Validation baseline migration | 1 week | None | MEDIUM |
| Year-by-year output format | 3 days | None | LOW |
| Deterministic dispatch wrapper script | 3 days | None | LOW |
| Distributed dispatch template | 1 week | None | LOW |
| Geopolitical scenario agent | 2-3 weeks | Reference doc creation | MEDIUM |
| Real-time price tracking | 2-3 weeks | Bloomberg API access | HIGH |
| Correlation monitoring library | 1 week | Real-time price tracking | HIGH |
| Emerging market solar scanner | 2-3 weeks | IRENA data pipeline | MEDIUM |
| Portfolio monitoring module | 4-6 weeks | Real-time prices + correlation | HIGH |
| Fleet-modeler validation (oil) | 1-2 weeks | None | MEDIUM |
| Regional-demand-analyst validation | 1-2 weeks | None | MEDIUM |

**Total estimated effort:** 16-24 weeks for all items. Critical path: real-time price tracking -> correlation monitoring -> portfolio module (8-10 weeks sequential).

**Recommended phasing:**
1. **Phase 1 (Weeks 1-3):** Real-time price tracking infrastructure + validation baseline migration
2. **Phase 2 (Weeks 3-5):** Correlation monitoring library + fleet-modeler/regional-demand validation
3. **Phase 3 (Weeks 5-8):** Portfolio monitoring module (MVP: LNG position with 3 daily metrics)
4. **Phase 4 (Weeks 8-12):** Emerging market scanner + geopolitical scenario agent
5. **Phase 5 (Weeks 12-16):** Distributed dispatch template + year-by-year output + deterministic wrapper

---

## Appendix: Key File Paths

### Old System
- Agent prompt: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/old_prompts/energy_sector_subagent_system.txt`
- Sector report: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/old_prompts/sector_reports/family2-energy-report.txt`

### Skills System
- Skill instructions: `/Users/himanshuchauhan/TONY/STDF/skills/skill-instructions/energy_sector/`
- Deployed skill: `/Users/himanshuchauhan/TONY/STDF/skills/.claude/skills/energy-sector/`
- Spec: `/Users/himanshuchauhan/TONY/STDF/skills/.claude/skills/energy-sector/references/SWB_ANALYSIS_SPEC.md`

### STDF v2 Pipeline
- Energy dispatch agent: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/.claude/agents/stdf-energy-dispatch.md`
- Gas supply agent: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/.claude/agents/stdf-gas-supply-decomposer.md`
- Energy math library: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/lib/energy_math.py`
- Dispatch parameters: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/data/energy_sector/config/dispatch_parameters.json`
- Dispatch methodology: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/references/energy-dispatch-methodology.md`
- Gas supply ordering: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/references/gas-supply-ordering.md`

### Pipeline Outputs
- Bloom Energy SOFC: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/output/bloom-energy-sofc-disruption/`
- Oil-Gas Outlook: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/output/oil-gas-outlook/`

### Meeting Notes
- Sector/commodity breakdown: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/meetings/consolidated_sector_commodity.md`
- Tony vs Robert: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/meetings/consolidated_tony_vs_robert.md`
