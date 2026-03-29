# Comprehensive Gap Analysis: STDF System vs. Stakeholder Expectations

**Date:** 2026-03-27
**Sources:** 4 meeting transcriptions (Mar 6-26), full STDF codebase audit, server & frontend audit
**Scope:** What Tony & Robert expect vs. what exists, what migrating gains, what must be built fresh

---

## EXECUTIVE SUMMARY

The STDF system has **strong analytical DNA** — a well-architected 23-agent pipeline with 956 curated data curves, 15 Python math libraries (~4,000 lines), and 21 completed analysis runs. The server/frontend layer (FastAPI + React) is functional but early-stage.

However, what Tony and Robert actually want has **evolved far beyond what exists**. Across 4 meetings (Mar 6-26), their vision shifted from "better chat tool" to a **24/7 autonomous investment intelligence platform**. The current system covers roughly **35-40% of their stated requirements**, with the analytical pipeline being the strongest area (~70% coverage) and the product/operational layer being the weakest (~15% coverage).

| Category | Alignment | Gap |
|----------|-----------|-----|
| STDF analytical framework (cost curves, S-curves, tipping points) | **70%** | Convergence, bottlenecks, feedback loops, correlation breaks |
| AI/Employment (AL) model | **0%** | Entirely separate system; not in STDF pipeline |
| Lead disruption model | **0%** | Separate system; STDF has lead data (48 curves) but no supply-demand model |
| Data factory (1,108 curves, auto-refresh) | **~15%** | STDF has 956 static curves; no auto-refresh, no data factory dashboard |
| Proactive intelligence (Stellar Sense / 24-7 agent) | **0%** | Nothing exists — build from scratch |
| Portfolio monitoring | **0%** | Nothing exists — build from scratch |
| Speed / real-time response | **20%** | QUICK preset exists; no local LLM, no urgency toggle |
| Data provenance / references | **10%** | Data-type tags exist (`[observed]`/`[model-derived]`); no source URLs on responses |
| Back-testing framework | **5%** | S-curve fitting validates R²; no systematic back-testing against actual economic data |
| Newsletter / notifications | **0%** | No email, no WhatsApp, no push notifications |
| Multi-channel delivery | **0%** | Web chat only |
| Bloomberg integration | **0%** | Not present |

---

## PART 1: WHERE WE ALIGN

These are areas where the current STDF system directly serves what Tony and Robert demand.

### 1.1 SIBA/STDF Framework Implementation — STRONG

**What Tony demands:** "It's important to always do the SIBA framework... that's not optional." (Mar 11). Cost curves, S-curves, tipping points, scaling properties, market trauma — this is THE analytical lens.

**What we have:**
- 18 pipeline agents implementing the full STDF methodology
- Tier-by-tier execution: domain disruption → cost analysis → capability analysis → tipping synthesis → adoption S-curves → regional breakdown → X-curve decline → commodity demand → energy dispatch
- 15 Python math libraries (scipy-based curve fitting, merit order dispatch, fleet modeling, demand decomposition)
- 956 curated data curves across 25 sectors
- Compliance checklist (C1-C10) with structural validation
- Banned vocabulary system preventing mainstream economics framing
- `shared-rules.md` (399 lines) enforcing disruption-first analysis, no cost floors, no mainstream anchoring

**Alignment score: 70%**

**Remaining gaps within the framework:**
- **Convergence analysis** — Tony (Mar 20): "We haven't really done convergence." No dedicated convergence agent exists. The domain-disruption agent identifies convergence combinations but doesn't model them deeply.
- **Bottleneck detection** — Identified as essential SIBA element but not systematically modeled. Copper is the canonical example (demand outpaces supply) but no bottleneck-specific agent exists.
- **Feedback loops** — Referenced multiple times. The recursive dynamics (e.g., lead → battery → EV → lead surplus) are handled implicitly in the synthesizer but not as an explicit, traceable analytical step.
- **Correlation break detection** — Tony (Mar 20, 26): "Correlations breaking is a huge investment opportunity." No agent or module for this.

### 1.2 Cost Curve Analysis — STRONG

**What Tony demands:** "Cost curves are like gravity." No cost floors. No TCO. Service-level units ($/kWh, $/km). Regional costs, not PPP.

**What we have:**
- `stdf-cost-researcher` → `stdf-cost-fitter` two-stage pipeline
- `cost_curve_math.py` (532 lines): exponential fit, learning rate derivation, competitive threshold, inflection threshold, unit converters ($/Wp→$/kWh, $/vehicle→$/km, $/kWh-cap→$/kWh-delivered)
- `shared-cost-rules.md`: no TCO/DCF, service-level units mandatory, R² required, no scenario labels
- Banned vocabulary blocks "total cost of ownership", "levelized cost" aggregation
- `stdf_validate.py` PreToolUse hook blocks writes containing banned terms

**Alignment score: 85%**

**Remaining gaps:**
- No explicit "no cost floors" enforcement in the hook (Tony had to manually correct this on Mar 20). The banned vocabulary blocks "floor" in certain contexts but doesn't prevent agents from imposing implicit floors in their curve extrapolations.
- Regional cost differentiation depends on data availability per region in the catalog — some sectors have thin regional coverage.

### 1.3 S-Curve & Adoption Modeling — STRONG

**What Tony demands:** S-curves with rupture points at 5-10%. Differentiated by region. Know where we are on the curve.

**What we have:**
- `stdf-scurve-fitter`: logistic S-curve fit with scipy, L/k/x0 parameters, R², 5/10/20-year projections with confidence intervals
- `stdf-regional-adopter`: per-region breakdown (China/USA/Europe+), regional S-curve fits, year-behind-leader classification
- `scurve_math.py` (210 lines): fit, project, classify phase, completion year, X-curve decline mirror
- Phase classification (pre-tipping, early adoption, rapid growth, late majority, saturation)
- 503 adoption curves in the data catalog

**Alignment score: 75%**

**Remaining gaps:**
- Rupture point detection (5-10% threshold) is conceptual in the framework but not implemented as a proactive alert system
- No mechanism to determine "where we are on the curve" for active positions in real-time

### 1.4 Pipeline Architecture & Orchestration — STRONG

**What the team built (as described in Mar 6):** 21 active agents, compliance checklist, orchestration layer with reformulator, clarification agent, planning agent, STDF agent, plus micro-agents.

**What we have:**
- 23 agent definitions (18 pipeline + 4 utility + 1 evaluator)
- 8 pipeline presets (FULL, QUICK, TIPPING_ONLY, COST_FOCUS, ADOPTION_FOCUS, FULL+COMMODITY, ENERGY_FULL, ENERGY_GAS)
- Failure matrix (CRITICAL/HIGH/MEDIUM) with stop/continue/penalty rules
- Phase 1 hard gate (AskUserQuestion after Tier 1 for scope confirmation)
- File-based inter-agent communication (enforced by hooks)
- Compliance validation (`stdf-compliance`, `stdf-validate`, `stdf-evaluator`)

**Alignment score: 80%**

---

## PART 2: WHERE WE LAG (Partial Coverage)

### 2.1 Data Factory & Auto-Refresh

**What they have (their system):** 1,108 curves, 581 refreshed, 441 pending. Auto-refresh agent runs 5x/week. Data factory dashboard with color-coded status. Bloomberg access. Quality-gated ingestion ("highly guarded embassy").

**What STDF has:** 956 static curves in `data/`. `build_data.py` to construct the index. `query_curves.py` CLI for search. No auto-refresh. No data freshness tracking. No data factory dashboard. No Bloomberg integration.

**Gap:** The STDF data catalog is a **static snapshot**. It's high quality (curated, validated) but frozen. Their system has a living data factory with refresh scheduling, source tracking, and quality gates. We have the analytical consumption layer but not the data production layer.

**Migration gain:** The STDF catalog format (JSON with x/y arrays, index.json) is well-structured and could receive data from an auto-refresh pipeline. The `data_catalog.py` library already has search/query functions. **Adding an auto-refresh layer on top of the existing catalog structure is feasible.**

**What must be built fresh:**
- Auto-refresh scheduler (cron-based data fetcher)
- Per-curve source registry with freshness tracking
- Data quality validation pipeline
- Bloomberg API integration
- Paid data source API integrations (IRENA, IEA historical)
- Data factory health dashboard

### 2.2 Speed & Response Time

**What Tony demands:** Real-time answers in meetings. Urgency toggle. Estimated response times. Willing to pay for premium tokens. Local LLM exploration.

**What we have:**
- `QUICK` preset (3 agents instead of 12-18) — partial solution
- `DEV_MODEL` override (can switch to Haiku for speed) — but at cost of quality
- No urgency toggle in the UI
- No estimated response time
- No local LLM support
- Email notification for long queries exists in their product but **not in our server/frontend**

**Migration gain:** The QUICK preset is a genuine speed optimization. The pipeline preset system could be extended with an "URGENT" mode that runs fewer agents with a faster model.

**What must be built:**
- Urgency toggle in frontend → server → pipeline preset selection
- Response time estimation (based on preset complexity)
- Email notification system for long-running analyses
- Local LLM integration (research phase)

### 2.3 Data Provenance & Source References

**What Robert demands:** "Data reference links on every response." Per-source validation. Thumbs up/down per source.

**What STDF has:**
- Data-type tags: `[observed]` / `[model-derived]` — agents are trained to tag all data points
- Source hierarchy rules (Tier 1: government/peer-reviewed, Tier 2: local catalog, Tier 3: web)
- Banned organization policy (IEA/EIA/BNEF URLs banned; historical data only with `[CAUTION]` tags)
- Agent outputs cite source names but not always clickable links

**Gap:** The tagging system is good analytically but doesn't produce the UI-level source provenance Robert wants — clickable links, per-source feedback buttons, and source validation workflows.

**Migration gain:** The data-type tagging and source hierarchy are already embedded in agent behavior. Adding UI-level source display is a frontend feature, not a pipeline rebuild.

### 2.4 Observability & Compliance

**What they have:** Observability Hub (agent network view, compliance checklist dashboard, Stellar Sense cron view, data factory overview). ~73 planned micro-agents for compliance checking.

**What STDF has:**
- `stdf-compliance` agent (checks structural compliance criteria)
- `stdf-evaluator` (Haiku-based post-synthesis quality gate, 8 rule categories)
- `stdf-validate` (runs `validate_pipeline.py` on output files)
- `stdf_validate.py` PreToolUse hook (blocks banned vocabulary in writes)
- TodoPanel in frontend (pipeline progress tracking via TodoWrite intercept)

**Gap:** No visual observability hub. No agent network diagram in the UI. No compliance dashboard. The compliance tools exist as CLI/agent utilities, not as a product feature.

**Migration gain:** The compliance infrastructure exists — it just needs a UI layer.

---

## PART 3: WHAT WE DON'T HAVE AT ALL (Build from Scratch)

### 3.1 AI/Employment (AL) Disruption Model — CRITICAL GAP

**What they have:** A sophisticated bottom-up model: 341 BLS occupations → 12,000 tasks (O*NET) → 90,000 sub-tasks. K-Medoids clustering into 4 task categories. Per-cluster adoption parameters (ceiling, time-to-80%, base floor, replacement ratio). Capability parity + cost parity checks per task. S-curve adoption modeling. Aggregation from sub-task → task → job → job group → economy. Back-testing against actual unemployment data. US and UK reports live as of Mar 27.

**What STDF has:** The STDF pipeline handles technology disruption analysis (cost curves, S-curves, tipping points) but has **zero implementation of the AL model**. There is no:
- BLS occupation database
- O*NET task decomposition
- Task clustering (K-Medoids or otherwise)
- Unemployment prediction
- Back-testing against economic data
- Labor market modeling of any kind

The `agentic_ai` sector in the data catalog has some AI cost/adoption curves, but these are technology curves, not labor displacement curves.

**Why this matters:** AI/Employment is the **#1 analytical priority** for the fund. Tony and Robert spend the most meeting time on it. It's the core investment thesis.

**What must be built from scratch:**
- O*NET task database ingestion
- Task-level feature extraction (12 vectors per task from ONET + Anthropic Economic Index)
- Clustering algorithm (K-Medoids with labeled clusters)
- Per-cluster adoption parameter assignment
- Capability parity + cost parity checking per task
- S-curve adoption per cluster
- Hours-freed calculation per job
- Risk vs. productivity split
- Ceiling cap application
- Aggregation pipeline (sub-task → task → job → job group → economy)
- Back-testing framework against actual BLS/UK unemployment data
- In-product parameter tuning
- UK model (separate from US)
- Youth unemployment and college graduate unemployment tracking

**Effort estimate:** This is the largest single build item. It's an entirely parallel analytical system to the STDF commodity/energy pipeline.

### 3.2 Lead Disruption Model (Supply-Demand-Surplus) — SIGNIFICANT GAP

**What they have:** A detailed lead supply-demand model with: split cost curves (SLA vs. EV auxiliary), primary supply (byproduct of zinc mining) + secondary supply (recycling), cumulative stockpile inventory model, tipping point identification (China 2026, others 2029), surplus progression to price collapse.

**What STDF has:** The data catalog has 48 lead curves (cost, adoption, commodity intensity). The `stdf-demand-decomposer` + `stdf-stream-forecaster` + `stdf-fleet-modeler` chain can model commodity demand decomposition. But there is **no lead-specific supply-demand-surplus model** — no recycling dynamics, no byproduct supply constraints, no cumulative stockpile modeling, no price collapse prediction.

**What must be built:**
- Lead-specific supply model (primary from zinc + secondary from recycling)
- Cumulative stockpile inventory view
- Surplus → price collapse dynamics
- Integration with existing demand decomposition pipeline
- Template for other byproduct commodities

**Partial migration gain:** The STDF commodity demand chain (Tier 6) provides the demand-side infrastructure. The `demand_math.py` library has `stock_flow_fleet` and `oem_replacement_split`. The gap is the supply-side modeling and surplus dynamics.

### 3.3 Proactive Intelligence / 24-7 Autonomous Agent — THE BIGGEST GAP

**What Tony demands (Mar 26):** "Flip Stellar Edge from chat-based to around the clock, infinite loop kind of software. We don't prompt the software, it prompts us."

This includes:
- Software working 24/7: learning, gathering data, doing portfolio risk, looking for investment ideas, tracking positions, writing PTIPs
- Multi-channel alerts: email, WhatsApp, voice
- Correlation break detection across technology scaling properties
- Rupture point monitoring (5-10% market penetration thresholds)
- Supply/demand bottleneck early warning
- Portfolio position tracking (5-10 metrics per position, daily)
- Unprompted insights: "start with 5 things" (Mar 20)

**What STDF has:** Nothing. The system is entirely request-response. A user sends a query, the pipeline runs, it produces a report. There is no:
- Background processing loop
- Scheduled/cron-based analysis
- Multi-channel notification delivery
- Portfolio state management
- Correlation monitoring
- Real-time data tracking
- Proactive alert system

**What must be built entirely from scratch:**
- **Background agent scheduler** — cron-based system that triggers analyses on schedule
- **Portfolio module** — positions database, per-position metric tracking, daily data ingestion
- **Correlation engine** — tracks scaling properties across technologies, detects breaks
- **Rupture point monitor** — tracks market penetration %, flags approaching 5-10% thresholds
- **Bottleneck detector** — supply/demand balance tracking, early warning
- **Notification service** — email, WhatsApp, voice (probably via Twilio/SendGrid)
- **Intelligence synthesis** — daily/weekly digest of proactive findings
- **Human-in-the-loop workflow** — "WhatsApp me if you have a question, then keep going"

**This is not an enhancement of the existing system — it is a fundamentally different product architecture.**

### 3.4 Newsletter with Analytical Intelligence

**What Tony demands (Mar 11):** Not news — intelligence. Convergence signals, emerging bottlenecks, tipping points approaching, systemic implications, "things we're not paying attention to."

**What STDF has:** Nothing. No newsletter generation. No signal detection. No scheduled intelligence delivery.

**Overlap with 3.3:** The newsletter is a subset of the proactive intelligence system. If the 24/7 agent is built, the newsletter becomes a scheduled output format.

### 3.5 Morning Meeting Transcript Integration

**What Tony demands (Mar 20):** System should process morning meeting transcripts, derive insights from individual meetings and cumulatively over 6-9 months.

**What STDF has:** Nothing. No transcript ingestion, no NLP processing, no cumulative insight extraction.

**What must be built:** Transcript ingestion pipeline, entity extraction, insight extraction, cumulative analysis across meeting history. (Note: this is exactly what we just did manually with the 4 meeting transcriptions — but it needs to be automated and continuous.)

### 3.6 Bloomberg Terminal Integration

**What they want (Mar 26):** Plug Bloomberg data directly into the system for portfolio-related data.

**What STDF has:** Nothing. No Bloomberg API, no market data feeds.

**What must be built:** Bloomberg API integration (likely Bloomberg B-PIPE or Desktop API), data normalization layer, mapping to STDF data catalog format.

### 3.7 Time-Travel Analysis

**What Robert wants (Mar 11):** Ask the system to forget future knowledge and predict from a past vantage point.

**What STDF has:** Nothing. The pipeline always uses current data. No mechanism to constrain the model to a historical information set.

**What must be built:** Data versioning (time-stamped snapshots of the data catalog), temporal query scoping (restrict data to a given date), counterfactual analysis framework.

### 3.8 Predictive Power Warnings / Wealth Warnings

**What Robert demands (Mar 6):** Model should flag when it has no predictive applicability. "Put it aside and come back in three months." Model should self-learn from incoming data.

**What STDF has:** The `stdf-evaluator` checks output quality against structural criteria but does NOT check predictive accuracy against real-world data. No self-learning mechanism.

**What must be built:** Back-testing validation layer, predictive accuracy scoring, confidence warnings on outputs, self-refinement loop.

---

## PART 4: MIGRATION GAINS — OLD SYSTEM TO NEW

The "old system" is the Stellar Edge product (chat-based, with data factory, AL model, lead model, observability hub, newsletter, Stellar Sense cron jobs). The "new system" is the STDF v2 pipeline in this repo.

### What STDF v2 Brings That the Old System Lacks

| Capability | Old System | STDF v2 | Gain |
|---|---|---|---|
| **Pipeline architecture** | Monolithic prompt-based | 23 specialized agents, tiered DAG, file-based communication | Reproducibility, modularity, debuggability |
| **Analytical rigor** | Variable (agents sometimes returned Phillips curve instead of SIBA) | Enforced by shared-rules.md, banned vocabulary, PreToolUse hook, compliance checklist | Consistency with Tony's framework demands |
| **Cost curve math** | Unknown | 532-line scipy library with exponential fits, learning rates, thresholds, unit conversion | Mathematical precision |
| **Energy dispatch modeling** | Unknown | Full merit order dispatch, SWB generation, displacement scheduling, gas supply decomposition | Deep energy sector capability |
| **Commodity demand modeling** | Unknown | 4-agent chain: demand decomposition → stream forecasting → fleet modeling → regional disaggregation | Structured commodity analysis |
| **Quality gates** | None mentioned | Evaluator agent (Haiku), compliance agent, validation hook, guardrails library | Output quality assurance |
| **Framework enforcement** | Manual (Tony had to repeatedly correct violations) | Automated: banned vocabulary, mandatory SIBA-first routing, disruption dynamics guardrails (10 rules) | No more Phillips curve responses |
| **Output structure** | Chat responses | Structured markdown with agent attribution, data-type tags, confidence scores | Auditability |
| **Pipeline presets** | One-size-fits-all | 8 presets matched to query complexity | Right-sized analysis |
| **Server layer** | Unknown (likely separate) | FastAPI + WebSocket, Claude Agent SDK, streaming, plan approval, AskUserQuestion interception | Modern, extensible architecture |
| **Frontend** | Unknown (likely separate) | React 19 + TypeScript + streaming markdown + todo panel + tool visibility | Clean, purpose-built UI |

### What's Lost in Migration

| Capability | Old System | STDF v2 | Loss |
|---|---|---|---|
| **AL model** | Fully built (4 clusters, back-testing, US+UK) | Not present | **CRITICAL** — must be rebuilt |
| **Lead supply-demand model** | Built (cumulative stockpile, surplus timing) | Data exists but no model | **SIGNIFICANT** — needs supply-side build |
| **Data factory** | 1,108 curves, auto-refresh, quality gates, dashboard | 956 static curves, no refresh | **SIGNIFICANT** — needs refresh layer |
| **Observability Hub** | Built (agent view, compliance view, data factory view) | TodoPanel only | **MODERATE** — needs UI build |
| **Stellar Sense / Cron jobs** | Exists (daily/weekly/monthly automated queries) | Nothing | **SIGNIFICANT** — must be built |
| **Newsletter** | V1 built (news-based) | Nothing | **MODERATE** — lower priority per Tony |
| **Email notifications** | Built (for long-running queries) | Not present | **MODERATE** — needs notification service |
| **Data references** | In development (source links on responses) | Data-type tags only | **MODERATE** — needs UI layer |
| **Bloomberg access** | Connected via Guido's terminal | Nothing | **MODERATE** — API integration needed |
| **User data upload** | Planned (restricted access) | Nothing | **LOW** — build when needed |

---

## PART 5: PRIORITIZED BUILD PLAN

Based on Tony and Robert's stated priorities, ranked by urgency and impact.

### P0 — CRITICAL (Without these, the product doesn't serve the fund's core needs)

#### P0.1: AL Model Integration
**Why:** #1 analytical priority. Core investment thesis. Tony + Robert use it daily.
**Effort:** Large — 4-6 weeks for a team
**Approach:** Build as a parallel agent pipeline within STDF (new agents: `stdf-al-task-decomposer`, `stdf-al-clustering`, `stdf-al-adoption`, `stdf-al-aggregator`, `stdf-al-backtester`). Can reuse STDF's S-curve math, cost curve math, and pipeline orchestration. Needs O*NET data ingestion, BLS unemployment data, and back-testing framework.

#### P0.2: Framework Enforcement Fix — SIBA Routing
**Why:** Tony's biggest frustration (Mar 20): queries about UK unemployment or LNG returned mainstream economics instead of SIBA framework analysis.
**Effort:** Small — 1-2 days
**Approach:** Already largely solved in STDF v2 via shared-rules.md and banned vocabulary. The STDF system prompt explicitly routes everything through the SIBA framework. **This is a migration gain already realized.** Verify with test queries.

#### P0.3: No Cost Floors Enforcement
**Why:** Tony interrupted the team on Mar 20 to demand this. Critical to the disruption thesis.
**Effort:** Small — 1 day
**Approach:** Add explicit "no cost floor" rule to `shared-cost-rules.md` and add "cost floor" / "floor price" to banned vocabulary in `vocabulary.py`. Add guardrail check in `stdf_validate.py` hook. **Partially solved — needs tightening.**

### P1 — HIGH (Required for the product to be usable as an investment tool)

#### P1.1: Data Factory Auto-Refresh Layer
**Why:** Stale data = wrong answers. Tony: "Without precision we are gonna lose money."
**Effort:** Medium — 2-3 weeks
**Approach:** Build auto-refresh scheduler on top of existing data catalog. Per-curve source metadata, freshness tracking, API integrations (IRENA, Bloomberg, free sources). Quality gate before catalog update. Dashboard for monitoring.

#### P1.2: Lead Supply-Demand-Surplus Model
**Why:** Tony's canonical template for recursive disruption. Approaching tipping point (2026).
**Effort:** Medium — 1-2 weeks
**Approach:** Extend `demand_math.py` with supply-side functions (primary from zinc byproduct, secondary from recycling, cumulative stockpile). Build as STDF agent (`stdf-supply-surplus`) or extend `stdf-stream-forecaster`. Lead data already in catalog (48 curves).

#### P1.3: Back-Testing Framework
**Why:** Robert's #1 demand. "Back-testing is the ABC." Tony agrees it's non-negotiable.
**Effort:** Medium — 2-3 weeks
**Approach:** Build validation layer that compares STDF predictions against historical actuals. Requires time-stamped data (what we predicted vs. what happened). Start with lead tipping points and AI/unemployment model. Integrate with `stdf-evaluator` for automated accuracy scoring.

#### P1.4: Speed Improvements
**Why:** Tony needs answers in live meetings, not overnight.
**Effort:** Small-Medium — 1-2 weeks
**Approach:**
- Add URGENT preset to pipeline (domain-disruption + cost-researcher only, Haiku model)
- Wire urgency toggle in frontend → server → preset selection
- Add response time estimation based on preset
- Consider Sonnet for most agents, Opus only for synthesizer

### P2 — MEDIUM (Required for the full product vision)

#### P2.1: Proactive Intelligence / 24-7 Agent (Phase 1)
**Why:** Tony's central product vision as of Mar 26. But it's gated on precision improvements.
**Effort:** Large — 4-8 weeks
**Approach (phased):**
- Phase 1: Cron-based scheduled analyses (daily STDF runs on tracked sectors)
- Phase 2: Portfolio position tracking module
- Phase 3: Correlation break detection engine
- Phase 4: Multi-channel notification (email first, then WhatsApp)
- Phase 5: Full autonomous loop with human-in-the-loop

#### P2.2: Portfolio Monitoring Module
**Why:** Tony (Mar 26): "5 or 7 or 10 things we should be tracking every day for every position."
**Effort:** Medium — 2-3 weeks
**Approach:** Portfolio positions database (even a JSON file to start). Per-position metric definitions. Daily data fetcher. Pattern detection (using time series analysis). Alert thresholds. Integration with notification service.

#### P2.3: Convergence Analysis Agent
**Why:** Tony (Mar 20): "We haven't really done convergence." Essential SIBA element.
**Effort:** Small-Medium — 1 week
**Approach:** New agent `stdf-convergence-analyst` that reads domain-disruption output and identifies convergence points between technologies. Can use the existing capability comparison framework. Add to Tier 5b (parallel with regional-adopter and xcurve-analyst).

#### P2.4: Observability Dashboard
**Why:** Already exists in old system. Tony wants visibility into what agents are doing.
**Effort:** Medium — 2 weeks
**Approach:** Frontend feature using existing TodoWrite data, agent definitions from `agents.py`, compliance results from `stdf-evaluator`. No new backend needed — just UI.

### P3 — LOWER (Important but not blocking)

#### P3.1: Newsletter with Intelligence
**Why:** Tony wants intelligence, not news. Current version (old system) is news-based.
**Effort:** Medium — 2-3 weeks
**Approach:** Subset of the proactive intelligence system. Scheduled STDF runs → synthesized findings → email delivery. Start with weekly format.

#### P3.2: Data Source Provenance UI
**Why:** Robert wants clickable source links. Tony wants per-source feedback.
**Effort:** Small — 1 week
**Approach:** Parse `[observed]`/`[model-derived]` tags from agent outputs. Add source URLs to data catalog metadata. Render in frontend with feedback buttons.

#### P3.3: Meeting Transcript Integration
**Why:** Tony (Mar 20): process transcripts, derive cumulative insights.
**Effort:** Small-Medium — 1-2 weeks
**Approach:** Transcript ingestion agent, entity extraction, insight extraction, cumulative analysis. We just demonstrated this capability manually — automate it.

#### P3.4: Bloomberg Integration
**Why:** Real-time market data for portfolio monitoring.
**Effort:** Medium — 2-3 weeks (API complexity + data mapping)
**Approach:** Bloomberg API integration, data normalization, mapping to STDF catalog format.

#### P3.5: Time-Travel Analysis
**Why:** Robert's feature request for counterfactual analysis.
**Effort:** Medium — 2-3 weeks
**Approach:** Data versioning layer, temporal query scoping, counterfactual analysis framework.

#### P3.6: Predictive Power Warnings
**Why:** Robert: model should flag when it lacks applicability.
**Effort:** Small — 1 week (once back-testing framework exists)
**Approach:** Add accuracy scoring to `stdf-evaluator`. If prediction error > threshold, append "wealth warning" to output.

---

## PART 6: SERVER & FRONTEND SPECIFIC GAPS

### What the Server Has (Working)

- FastAPI + WebSocket real-time communication
- Claude Agent SDK integration (session management, streaming, resume)
- Agent definition loading from STDF agent files
- Tool permission interception (AskUserQuestion, PlanApproval, TodoWrite)
- Streaming text + thinking + tool events to frontend
- Multi-session per user
- Session persistence across reconnects
- Cost tracking per session ($20 budget cap)
- Nested subagent tool display (parent_tool_use_id threading)

### What the Server Lacks

| Gap | Priority | Effort |
|---|---|---|
| Thinking mode not forwarded to SDK | P2 | 1 day |
| Permission mode not forwarded to SDK | P2 | 1 day |
| `usage_update` never emitted (context usage indicator is wired but empty) | P2 | 1 day |
| No authentication / multi-user | P1 | 1-2 weeks |
| No persistent storage (all state in memory, lost on restart) | P1 | 1-2 weeks |
| No email/WhatsApp notification service | P2 | 2-3 weeks |
| No scheduled/cron task runner | P2 | 1-2 weeks |
| No portfolio state management | P2 | 2-3 weeks |
| Tool component registry not wired (exists but unused) | P3 | 1 day |
| Read coalescing not wired (exists but unused) | P3 | 1 day |
| Dark mode | P3 | 2-3 days |

### Frontend-Specific Gaps

| Feature | Requested By | Status | Effort |
|---|---|---|---|
| Urgency toggle | Tony | Not present | 2 days |
| Response time estimate | Team | Not present | 1 day |
| Data source links on responses | Robert | Not present | 1 week |
| Per-source thumbs up/down | Tony | Not present | 3 days |
| Observability hub | Tony | Not present (TodoPanel only) | 2 weeks |
| Data factory dashboard | Dr. Waleed | Not present | 2 weeks |
| Agent network visualization | Dr. Ali | Not present | 1 week |
| Compliance checklist view | Dr. Ali | Not present | 1 week |
| Parameter tuning dashboard | Jitin | Not present (chat only) | 2 weeks |
| Portfolio monitoring view | Tony | Not present | 3 weeks |
| Newsletter delivery config | Tony | Not present | 1 week |

---

## PART 7: STRATEGIC RECOMMENDATIONS

### 1. Migrate the Analytical Pipeline — It's Ready

The STDF v2 pipeline is **more rigorous** than the old system. The framework enforcement (shared-rules, banned vocabulary, compliance checks, validation hooks) directly solves Tony's biggest frustration — the system returning Phillips curve analysis instead of SIBA framework analysis. **This is the single biggest migration gain.**

### 2. Rebuild the AL Model Inside the STDF Architecture

Don't port the old AL model code. Rebuild it as STDF agents that follow the same file-based communication, compliance checking, and shared-rules enforcement. This ensures the AL model inherits all the quality gates. The clustering → adoption → aggregation pipeline maps naturally to the STDF tier architecture.

### 3. Build the Proactive Layer as a New System on Top

The 24/7 autonomous agent is a fundamentally different architecture than the request-response pipeline. Build it as a scheduler + monitor layer that sits above the STDF pipeline and triggers analyses when conditions are met. The pipeline remains the analytical engine; the proactive layer is the intelligence layer.

### 4. Fix the Quick Wins First

Before the big builds, capture immediate value:
- Wire up thinking mode forwarding (1 day)
- Wire up context usage indicator (1 day)
- Wire up tool component registry (1 day)
- Add "no cost floor" to banned vocabulary (1 day)
- Add URGENT pipeline preset (2 days)
- Fix stale reference to `orchestrator.md` in server/agents.py (1 hour)

### 5. Data Strategy Is the Long Pole

Nearly every gap trace back to data: stale data (no auto-refresh), missing data (no Bloomberg), wrong data (Robert's frustration), regional data (Chinese sources), field data (analyst trips). Build the data refresh layer early — it unblocks everything else.

---

## APPENDIX: SYSTEM INVENTORY SUMMARY

### STDF Pipeline
- **23 agent definitions** (18 pipeline + 4 utility + 1 evaluator)
- **8 pipeline presets** (FULL through ENERGY_GAS)
- **15 Python libraries** (~4,000 lines, scipy/numpy-based)
- **956 data curves** across 25 sectors
- **21 completed analysis runs** in output/
- **4 reference documents** for methodology

### Server
- **11 Python files** (FastAPI + Claude Agent SDK)
- **3 HTTP/WS endpoints** (health, sessions list, WebSocket)
- **15+ WS message types** (bidirectional streaming)
- **4 tool interception handlers** (AskUser, PlanApproval, TodoWrite, Plan capture)
- **In-memory state only** (no database)

### Frontend
- **React 19 + TypeScript + Vite + Tailwind CSS 4 + Zustand**
- **~20 components** (chat, tool cards, interactive cards, sidebar, settings)
- **LocalStorage persistence** (debounced, survives refresh)
- **Auto-reconnect WebSocket** with offline message queue
- **130ms buffered streaming** for performance

### Missing from Both
- Authentication / multi-user
- Persistent storage / database
- Email / WhatsApp / notification service
- Bloomberg / market data API
- Portfolio management module
- Background task scheduler
- AI/Employment (AL) analytical model
- Lead supply-demand-surplus model
- Auto-refresh data pipeline
