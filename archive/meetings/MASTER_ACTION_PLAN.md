# STDF v2 Migration: Master Action Plan

**Date:** 2026-03-27
**Sources:** 4 meeting transcriptions (Mar 6-26), 23 old system prompts, 13 deployed skills, full STDF v2 codebase audit, server & frontend audit
**Purpose:** Single consolidated, deduplicated, prioritized action plan for migrating from old Stellar Edge system to STDF v2

---

## STATUS OVERVIEW

### What We Have (STDF v2 Pipeline)
- 23 agents in a tiered DAG (18 pipeline + 4 utility + 1 evaluator)
- 15 Python math libraries (~4,000 lines, scipy/numpy)
- 956 curated data curves across 25 sectors
- 8 pipeline presets (FULL → ENERGY_GAS)
- 6-layer quality enforcement (hooks, vocabulary, guardrails, compliance, evaluator, validation)
- FastAPI + WebSocket server with Claude Agent SDK
- React 19 frontend with streaming, tool visibility, plan approval, todo panel
- 21 completed analysis runs

### What Tony & Robert Want (from 4 meetings, Mar 6-26)
- SIBA/STDF framework enforced on EVERY query — non-negotiable
- AI/Employment model with K-Medoids clustering, back-testing against actual unemployment
- Lead supply-demand-surplus model (cumulative stockpile, price collapse timing)
- 24/7 autonomous agent that prompts THEM (not the other way around)
- Daily portfolio position tracking with correlation break alerts
- Precision over speed (but speed matters in live meetings)
- No cost floors, no mainstream economics first, no TCO

### Alignment Score: ~35-40%
- Analytical framework: **70%** (strong)
- AI/Employment model: **0%** (not in STDF)
- Lead supply model: **0%** (demand side only)
- Data factory / auto-refresh: **15%** (static curves)
- Proactive intelligence: **0%** (nothing exists)
- Portfolio monitoring: **0%** (nothing exists)

---

## PRIORITY 0 — CRITICAL (Do Immediately)

These items address fundamental gaps that block the product from serving the fund's core needs. Without them, STDF v2 cannot replace the old system.

### P0.1 Create `shared-philosophy.md` — Port Tony's Intellectual Framework
**Source:** `archive/old_prompts/tony_core.txt` (343 lines)
**Problem:** The new system encodes RULES but not WHY. Agents follow rules mechanically without understanding the epistemological reasoning behind them. This makes them brittle when facing edge cases.
**Action:** Create `/stdf/shared-philosophy.md` containing:
- Core Axioms (Convergence, 10x Factor, Phase Change, Metamorphosis Principle)
- "Cost curves are like gravity" argument with Moore's Law parable
- Historical Precedents table (cars, digital cameras, smartphones, Blockbuster, coal plants)
- RethinkX Prediction Track Record (99.2% accuracy on EV cost)
- 9 Principles of Disruption (Disruption Compass)
- Incumbent Response Pattern (7 stages: Denial → Collapse)
- Boulder Analogy for system dynamics
**Effort:** 1 day
**Owner:** Framework team

### P0.2 Update `shared-rules.md` — Add Missing Guardrails
**Problem:** Three enforcement gaps identified from old system comparison.
**Action:**
1. Add "Cost Curve Gravity" section explaining WHY no cost floors (not just "don't clip")
2. Add "Lag Exclusion Protocol" — exclude regulatory/adoption lags unless specifically requested
3. Add "Scope Assumption Fabrication Check" — agents must not present invented numbers as stated assumptions
4. Add "cost floor" / "floor price" / "minimum cost" to banned vocabulary in `vocabulary.py`
**Effort:** 0.5 days
**Owner:** Framework team

### P0.3 Update `CLAUDE.md` — SIBA-First Routing
**Problem:** Tony erupted (Mar 20) when UK unemployment and LNG queries returned Phillips curve analysis instead of SIBA. The orchestrator doesn't explicitly enforce SIBA-first routing for "mainstream economics" queries.
**Action:**
1. Add "SIBA First" orchestration rule: when ANY query could be analyzed through mainstream economics, route through SIBA disruption lens first
2. Add explicit convergence detection in Phase 1a
3. Add Philosophy Reference pointing to `shared-philosophy.md`
**Effort:** 0.5 days
**Owner:** Framework team
---

## PRIORITY 1 — HIGH (Required for Investment Use)

These items are required for the product to serve as an actual investment tool, not just an analytical demo.

### P1.1 Build Feedback Loop Agent
**Source:** Old `feedback_loop_subagent_system.txt` had a sophisticated 5-actor model (Government, Central Banks, Consumers, Corporations, Markets) with competing Reinforcing/Balancing loops and 3-scenario forecasts.
**Problem:** Tony (Mar 20): "Feedback loops are essential to SIBA." The new system has NO feedback loop agent. This is the single biggest IP loss from the old system.
**Action:** Create `stdf-feedback-loop.md` (Flex agent, injectable after Tier 4 or 5b) + `lib/feedback_math.py`
- Port: 5-Actor Model with reaction templates
- Port: Competing R/B loop architecture
- Port: 3-Scenario adjusted forecast methodology
- Port: Actor Reference Matrix (6 shock types × 5 actors)
- Add: Monitoring indicators for each loop
**Effort:** 3-4 days
**Owner:** Agent team

### P1.2 Build Convergence Agent
**Problem:** Tony (Mar 20): "We haven't really done convergence... we really haven't done it." The domain-disruption agent MAPS convergence but doesn't MODEL interaction dynamics.
**Action:** Create `stdf-convergence.md` (Tier 5c, parallel with regional-adopter) + `lib/convergence_math.py`
- Reads: domain-disruption convergence map, tipping-synthesizer, scurve-fitter
- Models: cross-sector feedback loops (Energy→Transport, Energy→AI, Energy+AI→Food)
- Produces: convergence acceleration estimates, emergent capability assessment
**Effort:** 2-3 days
**Owner:** Agent team

### P1.3 Build Bottleneck Detection Agent
**Problem:** Tony (Mar 20): "essential to SIBA." Neither old nor new system has dedicated bottleneck detection. Copper is the canonical example (demand outpaces supply).
**Action:** Create `stdf-bottleneck.md` (Flex agent, injectable when upstream agents flag constraints)
- Reads: domain-disruption, cost-researcher, capability, demand-decomposer
- Produces: bottleneck inventory with severity, timeline, mitigation pathways
- Uses: WebSearch + data catalog (no new math library needed)
**Effort:** 1-2 days
**Owner:** Agent team

### P1.4 Build Lead Supply-Demand-Surplus Model
**Problem:** Tony's canonical template for recursive disruption. STDF v2 has strong demand-side modeling (15 agents) but ZERO supply-side modeling. Lead trade thesis requires: zinc byproduct dynamics, recycling supply, cumulative stockpile, surplus → price collapse.
**Action:**
1. Create `stdf-supply-modeler.md` agent (Tier 6.5, after fleet-modeler)
2. Create `lib/supply_math.py`:
   - `byproduct_supply()` — zinc-linked primary lead production
   - `recycling_supply()` — battery retirement × recycling rate × lead content
   - `surplus_stockpile()` — annual surplus + cumulative inventory
   - `surplus_threshold_years()` — when surplus hits 10%/20%/50%/80%/90%
3. Build recursive disruption loop model in `lib/demand_math.py`:
   - Li-ion cost curve → EV adoption → lead demand decline → surplus → price decline → faster switching → larger surplus
4. Ingest supply reference data into `data/lead/supply/`
5. Update synthesizer template to include supply-demand balance section
**Data needed:** ILZSG lead supply data, zinc production by region, lead recycling volumes
**Effort:** 10-15 days (Phase 1)
**Owner:** Commodities team

### P1.5 Migrate AI/Labor Simulation Engine into STDF
**Problem:** AI/Employment is the #1 analytical priority. The old skill has a genuine bottom-up simulation (341 occupations, 89,040 subtasks). STDF v2 has strong analytical framing but no computation engine. Neither system has what Tony's team finalized on Mar 26 (K-Medoids clustering, back-testing).
**Action (phased):**

**Phase A — Data & Engine Migration (10-14 days):**
1. Migrate subtask dataset (34 gzip JSON parts + job-to-group mapping) to `stdf/data/labor/`
2. Adapt simulation engine (`lib/simulator.py`, `models.py`, `aggregator.py`) to `stdf/lib/labor_math.py`
3. Create `stdf-al-simulator` agent that wraps the adapted engine
4. Integrate with existing STDF synthesizer

**Phase B — K-Medoids Clustering (3-4 days):**
5. Extract 12 feature vectors per task from O*NET data
6. Build K-Medoids clustering module (4 clusters: manual, admin/tech, cognitive high-exposure, cognitive already-penetrated)
7. Assign per-cluster adoption parameters (ceiling, time-to-80%, base floor, replacement ratio)

**Phase C — Back-Testing (4-7 days):**
8. Integrate actual BLS unemployment data (monthly, last 36 months)
9. Create `stdf-al-backtester` agent — compare predictions vs actuals, compute R²/RMSE
10. Build `stdf-al-calibrator` agent — adjust parameters to improve fit
11. Add youth unemployment + college graduate unemployment tracking

**Phase D — UK Model (2-3 days):**
12. Source UK ONS employment/wage data
13. Extend regional-adopter for UK as standalone region

**Total effort:** P0 core: 10-14 days, full completion: 23-28 days
**Owner:** Labor team

## PRIORITY 2 — MEDIUM (Required for Full Product Vision)

### P2.1 Investment Translation Layer
**Problem:** Old system had STDF → Stellar → Value Investment chain. Stellar sub-agent had Hype Delta framework (HYPE_DELTA = Market-Implied Narrative - Operational Reality), Fragile/Robust/Antifragile classification, trade expression methodology, no-trade protocol. New system has none of this.
**Action:** Either port Stellar sub-agent into `stdf-investment-thesis.md` or wire the value-driven-investment skill from the Skills system.
**Effort:** 2-3 days
**Owner:** Framework team

### P2.2 Anti-Sycophancy Reformulation
**Problem:** Old system's reformulator extracted hypotheses, neutralized framing, preserved STDF terminology. New orchestrator handles interpretation but doesn't actively prevent sycophantic responses.
**Action:** Integrate anti-sycophancy rules into orchestrator (CLAUDE.md) or create a lightweight reformulator step.
**Effort:** 1-2 days
**Owner:** Framework team

### P2.3 Predictive Power Warnings
**Problem:** Robert (Mar 6): "The model should say 'Hey, just so you know, this model does not appear to have applicability.'" No mechanism exists in either system.
**Action:**
1. After evaluation, compare model predictions against recent actual data (if available in data catalog)
2. Flag when predictions diverge significantly (R² below threshold)
3. Append "wealth warning" to output when applicable
**Depends on:** Back-testing infrastructure (P1.5 Phase C)
**Effort:** 1-2 days
**Owner:** Agent team

### P2.4 Copper Supply Constraint Model (Migrate from COpper SKill)
**Problem:** Tony: "In the case of copper, the supply will not scale as quickly as demand." No supply model exists for any commodity.
**Action:** Extend `stdf-supply-modeler` (built in P1.4) with copper supply parameters:
- Mine production projections by region
- Project pipeline timelines and permitting delays
- Deficit/surplus timing and bottleneck identification
**Effort:** 3-5 days (after P1.4 complete)
**Owner:** Commodities team

### P2.5 Real-Time Energy Price Tracking
**Problem:** Tony (Mar 26): "Track oil prices, EU natural gas, US natural gas daily." No real-time data feed capability exists.
**Action:**
1. Build `scripts/fetch_energy_prices.py` cron job
2. Bloomberg API or EIA/ENTSOG free alternatives
3. Store as daily time series in `data/prices/`
4. Create `lib/correlation_monitor.py` (rolling correlation, break detection, alert generation)
**Effort:** 2-3 weeks for infrastructure
**Owner:** Data team

### P2.6 Cross-Commodity Pipeline Orchestration
**Problem:** No mechanism to run lead, copper, and lithium-ion analyses in a connected pipeline where lithium-ion cost → lead surplus AND copper demand.
**Action:** Add cross-commodity preset to CLAUDE.md that chains multiple commodity runs with shared upstream outputs.
**Effort:** 3-5 days
**Owner:** Framework team

### P2.7 Update `stdf-evaluator` — Port Missing Checks
**Problem:** Old evaluator had two checks not in the new evaluator: lag handling rule and scope assumption fabrication check.
**Action:** Add both checks to `stdf-evaluator.md` criteria.
**Effort:** 0.5 days
**Owner:** Agent team

---

## PRIORITY 3 — FUTURE (Product Roadmap, 1-3 Months)

### P3.1 Proactive Intelligence / 24-7 Autonomous Agent (Stellar Sense)
Tony's central product vision (Mar 26): "We don't prompt the software, it prompts us."

**Phase 1 — Signal Detection Layer (5-7 days):**
- Scheduled data refresh checks against data catalog
- Correlation monitoring across tracked asset pairs
- Rupture point proximity detection (5-10% market penetration)
- Cost parity threshold monitoring (new region crossings)

**Phase 2 — Portfolio Monitor Module (3-5 days):**
- Per-position metric tracking (5-10 metrics per position, JSON config)
- Daily/hourly data collection from Bloomberg
- Pattern detection against SIBA hypotheses
- Alert generation when thresholds crossed

**Phase 3 — Autonomous Analysis Loop (3-5 days):**
- Signal detected → auto-trigger appropriate pipeline preset
- Cost parity crossed → TIPPING_ONLY
- Correlation break → domain-disruption + research
- Rupture point proximity → FULL preset

**Phase 4 — Multi-Channel Notification (3-5 days):**
- Email digest (configurable: daily/weekly/on-signal)
- WhatsApp integration for urgent alerts (SendGrid/Twilio)
- Voice synthesis for audio briefings
- Alert triage: Critical/High/Medium priority levels

**Phase 5 — Human-in-the-Loop (2-3 days):**
- System asks humans questions via notification channels
- Responses feed back into analysis loop
- "WhatsApp me if you have a question, then keep going" workflow

**Total effort:** 16-25 days
**Owner:** Product + infrastructure team

### P3.2 Newsletter with Analytical Intelligence
Tony (Mar 11): "Not news — intelligence. Convergence signals, bottlenecks, tipping points, things not being paid attention to."
**Depends on:** Convergence agent (P1.2), feedback loop agent (P1.1), Stellar Sense (P3.1)
**Action:** Scheduled STDF runs → synthesized findings → email delivery. Weekly format.
**Effort:** 2-3 weeks
**Owner:** Product team

### P3.3 Emerging Market Solar Penetration Tracker
Tony (Mar 26): Pakistan went from zero to 18GW solar in a 30GW grid; stock exchange tripled.
**Action:**
1. Country-level solar capacity data from IRENA
2. `scripts/emerging_market_scanner.py` computing penetration % per country
3. Flag countries approaching 5-10% rupture point
**Effort:** 2-3 weeks
**Owner:** Data team

### P3.4 Geopolitical Scenario Agent
Tony's LNG position was impacted by Iran war. No geopolitical modeling exists.
**Action:** Create `stdf-geopolitical-scenario` agent for supply disruption impact modeling.
**Effort:** 2-3 weeks
**Owner:** Agent team

### P3.5 Meeting Transcript Integration
Tony (Mar 20): Process morning meeting transcripts, derive insights cumulatively.
**Action:** Automate what we just did manually — transcript ingestion, entity extraction, insight extraction, cumulative analysis.
**Effort:** 1-2 weeks
**Owner:** Product team

### P3.6 Time-Travel Analysis
Robert's request: ask the system to forget future knowledge and predict from a past vantage point.
**Action:** Data versioning layer, temporal query scoping, counterfactual analysis framework.
**Effort:** 2-3 weeks
**Owner:** Framework team

### P3.7 Bloomberg Terminal Integration
**Action:** Bloomberg API integration for real-time portfolio data.
**Effort:** 2-3 weeks
**Owner:** Data team

### P3.8 China / UK Data Pipeline
Tony: "China is definitely one of the top disruptors." Field teams (Peter, Guido) collecting data.
**Action:**
1. Ingest PowerPoints from China trips
2. Source Chinese data (NBS employment, battery costs)
3. UK ONS labor/wage data
4. Jane's macro economics data
**Effort:** 3-5 weeks
**Owner:** Data team

### P3.9 In-Product Parameter Tuning Dashboard
Tony (Mar 26): Tweak cluster parameters and regenerate numbers live.
**Action:** Frontend dashboard for adjusting AL model parameters, lead model parameters. Backend must support fast re-runs.
**Effort:** 2-3 weeks
**Owner:** Frontend + agent team

### P3.10 Self-Learning / Self-Refining Model
Robert's request: model should refine its own assumptions from incoming data.
**Action:** Automated calibration loop that ingests new data, re-runs back-tests, adjusts parameters.
**Effort:** 3-5 weeks
**Owner:** Agent team

---

## EFFORT SUMMARY

| Priority | Item Count | Effort Range | Cumulative |
|----------|-----------|-------------|-----------|
| **P0 — Critical** | 4 items | 4-5 days | 4-5 days |
| **P1 — High** | 7 items | 35-55 days | 39-60 days |
| **P2 — Medium** | 9 items | 15-25 days | 54-85 days |
| **P3 — Future** | 10 items | 35-60 days | 89-145 days |

**Recommended sprint plan:**
- **Week 1:** P0 (all 4 items) — philosophy doc, shared-rules, CLAUDE.md, server quick wins
- **Weeks 2-3:** P1.1-P1.3 (feedback loop, convergence, bottleneck agents)
- **Weeks 3-5:** P1.4 (lead supply model) + P1.7 (URGENT preset)
- **Weeks 3-7:** P1.5 (AL model migration — longest single item)
- **Weeks 5-8:** P1.6 (data factory auto-refresh)
- **Weeks 8-12:** P2 items in priority order
- **Months 3-5:** P3 items (Stellar Sense, portfolio monitoring, multi-channel)

---

## KEY ARCHITECTURAL DECISIONS

### 1. Merger, Not Replacement
The migration is a MERGER of old system IP into new STDF v2 architecture. The new pipeline provides the engineering skeleton (DAG, quality gates, math libraries). The old system provides domain-specific intelligence (feedback loops, Tony's philosophy, AL simulation engine, lead supply model).

### 2. File-Based Communication is Non-Negotiable
All agents communicate via markdown files in `output/{slug}/agents/`. This is enforced by hooks and is the foundation of reproducibility and auditability. New agents (feedback loop, convergence, supply-modeler, AL simulator) must follow this pattern.

### 3. Proactive Layer Sits ABOVE the Pipeline
The 24/7 autonomous agent (Stellar Sense) is NOT a modification of the pipeline — it's a scheduler/monitor/notifier that sits above it and TRIGGERS pipeline runs when conditions are met. The pipeline remains the analytical engine.

### 4. Quality Gates Are the Competitive Advantage
6 layers of enforcement (hooks, vocabulary, guardrails, compliance, evaluator, validation) prevent the system from producing mainstream economics responses. This directly addresses Tony's #1 frustration and is the biggest migration gain.

### 5. Tony's Philosophy Must Be Encoded as Context, Not Just Rules
`shared-philosophy.md` gives agents the WHY behind rules. Without it, agents follow rules mechanically and break at edge cases. With it, they can reason about novel situations using Tony's framework.

---

## FILES PRODUCED BY THIS ANALYSIS

| File | Lines | Purpose |
|------|-------|---------|
| `2026-03-06_insights.md` | 185 | Per-meeting extraction |
| `2026-03-11_insights.md` | 191 | Per-meeting extraction |
| `2026-03-20_insights.md` | 291 | Per-meeting extraction |
| `2026-03-26_insights.md` | 262 | Per-meeting extraction |
| `consolidated_tony_vs_robert.md` | 202 | Tony vs Robert wants, shared ground, tensions |
| `consolidated_product_vs_analysis.md` | 318 | 27 product features + 19 analysis features |
| `consolidated_philosophy_thinking.md` | 258 | Investment philosophy, key metaphors, "flip" evolution |
| `consolidated_sector_commodity.md` | 468 | 11 sectors with data points, thresholds, actions |
| `comprehensive_gap_analysis.md` | 620 | System capabilities vs expectations |
| `migration_labor_sector.md` | 516 | Old AL skill → STDF v2 migration |
| `migration_energy_sector.md` | 503 | Old energy skill → STDF v2 migration |
| `migration_lead_commodities_sector.md` | 605 | Old lead/copper/lithium skills → STDF v2 migration |
| `migration_framework_core.md` | 710 | Old orchestration/prompts → STDF v2 migration |
| **MASTER_ACTION_PLAN.md** | **this file** | **Consolidated, deduplicated, prioritized action plan** |
| **Total** | **~5,100+** | |

All files in `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/meetings/`.
