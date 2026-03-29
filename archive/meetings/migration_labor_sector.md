# Migration Analysis: AI/Labor Sector -- Old System to STDF v2

**Date:** 2026-03-27
**Scope:** AI/Employment (Artificial Labor) disruption analysis
**Systems compared:** Old skill-based system, Skills v2 system, New STDF v2 multi-agent pipeline

---

## 1. OLD SYSTEM ANALYSIS

### 1.1 Old Agent Prompt (`artificial_labor_subagent_system.txt`)

The old agent is defined as an "artificial labor forecasting engine" with a strict directive to use the artificial-labor skill for all calculations. Key instructions:

- **SKILL FIRST**: The skill's methodology is canonical -- the agent must never calculate displacement independently.
- **EVIDENCE GROUNDED**: Every number must come from skill output or be explicitly labeled as derived.
- **OCCUPATION GRANULARITY**: Break displacement into occupational categories and task types (cognitive, physical, routine, non-routine).
- **COST TRAJECTORY**: Track artificial labor cost per hour over time against human labor costs.
- **DOUBLE-EXPONENTIAL**: AI improves on both hardware AND software curves simultaneously.
- **Tool budget**: 5 `seba_research` calls, 5 `web_fetch` calls, plus code execution for skill data processing.
- **Pre-computed context**: When provided `<pre_computed_report_context>` tags, the agent formats that data into a polished response without re-running the skill. Strict anti-fabrication rules enforce that no number can be invented beyond the report data.
- **Output format**: Well-structured analytical text (not JSON), with FTE displacement, automation timelines, cost trajectories, and provenance markers `[R1]` flowing through to the citation builder.

**Strengths of the old agent prompt:**
- Strong anti-hallucination guardrails (NO FABRICATION BEYOND REPORT DATA)
- Clear delineation between SKILL OUTPUT and DERIVED data
- Forces occupational granularity
- Pre-computed context mode allows fast query responses without re-running the full simulation

**Weaknesses of the old agent prompt:**
- Single-agent architecture -- one agent does everything (skill invocation, supplementation, formatting)
- No multi-agent validation or cross-checking
- No compliance framework, no evaluator, no banned vocabulary enforcement
- No file-based communication -- data passes through prompt context
- Web search limited to 5 calls, no tiered data source hierarchy
- No S-curve fitting, no regional breakdown, no X-curve incumbent decline analysis
- No explicit STDF framework enforcement (no tipping point formalism, no rupture window)

### 1.2 Old Sector Report (`family1-labor-report.txt`)

The old report covers US AI labor disruption (2022-2035) and contains 10 structured sections:

| Section | Content |
|---------|---------|
| Executive Summary | Headline: 49M FTE (34.4%) displaced by 2030, plateau by 2028-2029 |
| S01 Disruption Map | 12 demand drivers (D01-D12) across occupation groups, each with employment, S-curve phase, tipping window |
| S02a Cost Curve AI | Exponential decline: $5.00/M tokens (2025) at 70%/yr to $0.01 floor by 2030 |
| S02b Cost Curve US Labor | BLS wages by 24 occupation groups, 3.5%/yr growth |
| S02c Physical Robotics | GAP -- cognitive only, physical excluded |
| S03 AI Capability | METR-based: 1560s baseline, 7-month doubling, subtask coverage from 5% (2022) to 99% (2030) |
| S04 S-Curve Adoption | Two-phase: floor 10%, ceiling 80%, 4 years to ceiling, tipping at AI < 50% human cost |
| S05 Tipping Points | 4 waves of occupation groups hitting 10%/25%/30% thresholds (2023-2029) |
| S06 Quantitative Forecast | Year-by-year displacement by occupation group, top 10 jobs by absolute and rate |
| S07 Feedback Loops | 4 reinforcing (R1-R4) + 5 balancing (B1-B5) loops with strength ratings |
| S08 Confidence | Medium overall, range 20-37%, sensitivity to doubling time, ceiling, years-to-ceiling |
| S09 Data Provenance | 5 data sources (BLS, O*NET, METR, AI API pricing, BLS wages), 7 model parameters |
| S10 Anti-Patterns | STDF compliance scorecard: 7/9 PASS, 2 PARTIAL (robotics gap, no multi-scenario) |

**Strengths of the old report:**
- Extremely detailed occupational breakdown (24 groups, top 10 jobs)
- Well-structured tipping point analysis with specific dates per occupation group
- Parameter sensitivity analysis
- Feedback loop analysis (reinforcing + balancing)
- Data provenance tracking
- STDF compliance self-assessment
- Query-time usage guide mapping common questions to sections

**Weaknesses of the old report:**
- Uniform parameters across all subtasks (no clustering, no per-cluster adoption)
- No back-testing against actual unemployment data
- No regional analysis (US only)
- No convergence analysis (domain-disruption mapping, chimera recognition)
- No X-curve incumbent decline modeling
- FTE displaced only -- does not model unemployment, new job creation, or reabsorption
- Static employment baseline
- No observed/model-derived tagging on data points
- No enterprise adoption readiness assessment
- Cost metric is $/M tokens -- no CTE (cognitive task equivalent) normalization
- Limited external benchmark comparison (Goldman, McKinsey, IMF cited but not integrated)

### 1.3 Skill Implementation (`.claude/skills/artificial-labor/`)

The deployed skill is a self-contained Python simulation with the following architecture:

**Data:**
- 341 occupations, 12,996 tasks, 89,040 subtasks (expanded from initial 186 jobs)
- 143,066,500 total US employment covered
- Data stored in 34 gzip-compressed JSON parts + job-to-group mapping CSV
- Hierarchical: Job > Task > Subtask, each subtask with time_per_iteration, tokens_required, cognitive/physical flag, importance, relevance, hourly_pay

**Core Models (6):**
1. **Capability Model**: C(t) = 1560 * 2^(months/7) -- METR-based 7-month doubling
2. **Cost Model**: cost(t) = $5.00 * 0.30^years -- 70%/yr decline, $0.01 floor
3. **Tipping Point**: AI cost < 50% of human cost triggers adoption acceleration
4. **Adoption Model**: S-curve from 10% floor to 80% ceiling over 4 years post-tipping
5. **Split Model**: 50/50 replacement vs. productivity (configurable per year)
6. **Ceiling Model**: 80% max replacement per job, overflow redirected to productivity

**Calculation Pipeline:**
For each month, for each of 341 jobs, for each subtask: capability check > cost comparison > tipping determination > S-curve adoption > hours freed > replacement/productivity split > ceiling application. Aggregation: subtask > job > group > economy.

**Configuration:**
All parameters in `simulation_config.json` + CLI overrides. Supports scenario runs (`--scenario conservative`, `--adoption-lag 24`, etc.).

**Output:**
JSON + CSV at job, group, and economy levels, monthly and yearly granularity.

**Strengths:**
- Genuine bottom-up simulation at subtask granularity
- Deterministic, reproducible (stdlib-only Python)
- Comprehensive occupational coverage (341 jobs)
- Configurable parameters via JSON + CLI
- Multi-level aggregation
- The actual computational engine that produces numbers

**Weaknesses:**
- Uniform parameters -- no clustering, no per-cluster adoption schedules
- No back-testing capability built in
- US only -- no regional models
- Static employment (no demographic shifts)
- No wage dynamics
- No regulation modeling
- Outputs displacement, NOT unemployment -- critical gap for Tony/Robert
- No self-learning or self-refining capability
- No integration with real-time data feeds
- Token-based cost metric not aligned with CTE normalization used by new pipeline

### 1.4 Existing Research (skill-instructions/artificial-labor/existing research/)

The skill-instructions directory contains extensive research documentation:

- **AL_Methodology_Framework.md** (v1.4): 14-part framework covering core model architecture, job displacement, productivity, cost decline, secondary effects (monetary/fiscal, consumer spending, investment flows, regulation), feedback loops, government response, backtesting mechanism, investment signals. Far more ambitious than what was actually implemented.
- **AL_Gap_Analysis_Tony_Requirements.md**: Identified 7 gaps and 6 new requirements from Tony's Jan 20, 2026 meeting. Key gaps: multiple S-curve layers not implemented (task, job, industry, output), productivity/replacement split needed per-task calibration, temporal granularity needed monthly interpolation, aggregation needed employment weighting.
- **AL_Scope_Framework.md**, **AL_External_Data_Report.md**, **AL_Data_Feasibility_Analysis.md**: Data requirements and feasibility assessments.
- **AL_Academic_Research_Review.md**, **AL_SME_Review_Document.md**: Literature review and expert validation plans.
- **AL_Research_Consolidated.md**: Unified research synthesis.

**Key finding**: The methodology framework document described a system far more sophisticated than what was actually built. Parts 8-14 (secondary effects, feedback loops, government response, backtesting, investment signals) were designed but not implemented in the simulation code.

---

## 2. NEW STDF PIPELINE ANALYSIS

### 2.1 What the New System Produces

The new STDF v2 pipeline ran a FULL configuration (11 agents) producing `ai-cognitive-labor/` output:

| Agent | Output | Confidence |
|-------|--------|------------|
| Domain Disruption | 5 sub-domains mapped, Big Bang classification, Stellar technology flow, chimera analysis, convergence architecture | 0.82 |
| Cost Researcher | 15 data points 2020-2025, BLS OEWS T1 incumbent data, CTE normalization ($0.002/CTE vs $17.50/CTE) | 0.87 |
| Cost Fitter | Exponential fit R^2=0.983, 69.5%/yr decline, competitive/inflection/enterprise integration thresholds | 0.91 |
| Capability | 10 dimensions assessed, 9 MET, HCAST R^2=0.999, agentic blocker mid-2026 | 0.82 |
| Cost Parity Checker | MET 2020-2021, 8,944x advantage | 0.88 |
| Capability Parity Checker | PARTIAL 9/10, mid-2026 threshold crossing | 0.88 |
| Adoption Readiness Checker | PARTIAL -- infrastructure READY, skills gap + EU regulatory PARTIAL | 0.84 |
| Tipping Synthesizer | 2026-2028, central 2027, adoption_readiness binding | 0.87 |
| S-Curve Fitter | L=88%, k=0.5903, x0=2028.6, R^2=0.9910 | 0.84 |
| Regional Adopter | USA leads (21.9%), China (15.1%), EU (3.6%) -- 4.8-yr gap | 0.71 |
| X-Curve Analyst | Early volume loss, 5 market trauma mechanisms, $3-6T/yr wage compression | 0.81 |

**Final synthesis** (`00-final-synthesis.md`): 7-phase narrative (Sector Scoping, Technology Inventory, Convergence, Disruption Pattern, Business Model Shift, Adoption & S-Curve, Synthesis & Tipping Point), plus Key Conclusion, Rupture Window, Confidence Score, Risk Factors, Regional Dynamics.

**Pipeline confidence: 0.841**

### 2.2 How It Differs from the Old System

| Dimension | Old System | New STDF v2 Pipeline |
|-----------|------------|---------------------|
| **Architecture** | Single skill + single agent | 11 specialized agents in DAG |
| **Cost metric** | $/M tokens raw | CTE (cognitive task equivalent) -- $0.002/CTE normalized |
| **Cost parity** | "All groups crossed already" (assertion) | Formal parity check with year (2020-2021), 8,944x ratio, enterprise integration threshold analysis |
| **Capability** | Single METR-based exponential | 10-dimension capability matrix, 9/10 MET, agentic blocker tracked |
| **S-curve** | Uniform: 10%->80% in 4 years per subtask | Empirical fit: L=88%, k=0.5903, x0=2028.6, R^2=0.9910 |
| **Regional** | US only | 5 regions with fitted S-curves (USA, China, EU, India, RoW) |
| **X-curve** | Not modeled | Full incumbent decline stages: early volume loss > accelerating decline > death spiral > advanced collapse |
| **Convergence** | Not modeled | 6 convergence architectures (AL+SA, AL+RAG, AL+DB, AL+CE, AL+MM, AL+MA) |
| **Chimera** | Not recognized | Explicitly modeled as hump-shaped dynamic |
| **Market trauma** | Not modeled | 5 mechanisms tracked (wage deflation, entry-level collapse, credential erosion, BPO disruption, social/political) |
| **Data tagging** | [R1] provenance markers | [observed] vs [model-derived], T1/T2/T3 source hierarchy |
| **Compliance** | Self-assessed scorecard | Automated evaluator agent (Haiku), banned vocabulary, guardrails |
| **Disruption framing** | Sector report with 10 sections | 7-phase STDF narrative with rupture window |
| **Feedback loops** | 4R + 5B loops named | Disruptor virtuous cycle + incumbent vicious cycle formally modeled |
| **Deflationary thesis** | Not addressed | Central analytical question: $3-6T/yr wage bill compression |
| **Confidence** | Medium (qualitative) | 0.841 (quantitative, per-agent, aggregated with penalty/cap rules) |

### 2.3 What the New Pipeline Does Better

1. **Multi-agent validation**: 11 agents cross-check each other; upstream conflicts are resolved explicitly (k=0.35 vs k=0.5903 documented and resolved).
2. **Formal parity framework**: Cost parity, capability parity, and adoption readiness are separate formal checks, each with year-of-crossing and confidence.
3. **Regional analysis**: 5 regions with independent S-curve fits -- critical for Tony's priority ordering (US > UK > China > EU).
4. **Empirical S-curve fitting**: Actual logistic fit to 7 observed data points (R^2=0.9910) rather than assumed adoption schedule.
5. **X-curve incumbent decline**: Maps the "death spiral" trajectory Tony wants to see -- when does the labor market hit each stage.
6. **CTE normalization**: Converts raw token costs to task-equivalent units, making the 8,944x ratio directly comparable to human labor costs.
7. **Convergence analysis**: Maps how AI combines with other technologies (agents, RAG, code execution) to create capabilities neither achieves alone.
8. **Market trauma mechanisms**: Tracks observable signals (entry-level tech postings -67%, India IT -42K headcount) that validate the disruption thesis.
9. **Guardrails enforcement**: Banned vocabulary, no mainstream anchoring, no constraint invention, no clipping, no incumbent protection -- enforced by evaluator.
10. **File-based communication**: Agents write files, downstream agents read files -- auditable, reproducible pipeline.

### 2.4 What the New Pipeline Does Worse or Doesn't Cover

1. **NO bottom-up subtask simulation**: The new pipeline does NOT run the 341-occupation, 89,040-subtask simulation. It fits an aggregate S-curve to proxy data. The old skill's granular "for each subtask, check capability, check cost, adopt" loop is entirely absent.
2. **NO per-occupation forecasts**: The new pipeline produces aggregate economy-wide and regional forecasts but not per-occupation-group displacement rates, tipping dates, or FTE counts.
3. **NO per-occupation tipping windows**: The old report had specific tipping dates for each of 24 occupation groups in 4 waves. The new pipeline does not produce this.
4. **NO hours-freed calculation**: The old skill calculated actual hours freed per employee, mapped to FTE replacement. The new pipeline works in "cognitive task share %" -- a different metric entirely.
5. **NO configurable parameter sweeps**: The old skill supported `--ceiling 0.90 --split 0.60 --scenario conservative` via CLI. The new pipeline has no scenario configuration mechanism for parameter sensitivity.
6. **NO back-testing against actual unemployment**: Both systems lack this, but it was more explicitly demanded of the old system.
7. **Proxy-based S-curve**: The S-curve's dependent variable is a "constructed proxy" from enterprise adoption surveys -- not directly measured cognitive task substitution. The old system at least used the direct simulation output.
8. **No UK model**: Despite UK being priority #2 geography, neither system has a UK-specific model.
9. **No youth unemployment tracking**: A specific stakeholder demand not addressed by either system.

---

## 3. STAKEHOLDER EXPECTATIONS (from meetings)

### 3.1 The AL Model Architecture Tony and Robert Have Been Iterating

Across 4 meetings (Mar 6, 11, 20, 26), the AI/Employment model has evolved:

**Mar 6 (Foundation):**
- Bottom-up: 341 US occupations from BLS, 12,000 tasks (O*NET), 90,000 sub-tasks
- Per sub-task: token estimate, cognitive classification, time estimate
- Tipping point: AI cost < 50% of human cost
- Parameters: capability doubling 7 months, cost decline 70%/yr, adoption 10-80% in 4 years, ceiling 80%, split 50/50
- **CRITICAL FINDING**: Model predicted ~18-20% unemployment but had ZERO FIT to recent actual data (Robert's discovery)

**Mar 11 (Clustering & Calibration):**
- Tony: unemployment > GDP growth. Priority: US > UK > China > EU
- Youth unemployment and college graduate unemployment as specific targets
- Two clustering approaches: rule-based (Anthropic E0/E1/E2) and unsupervised (K-means, hierarchical)
- Parameters per cluster: time to 80% adoption, adoption lag, replacement ratio, ceiling
- Calibration against youth unemployment as target signal
- Back-testing against 3 years since ChatGPT launch

**Mar 20 (ML Clustering & UK Model):**
- ML-based clustering into 4 clusters: (1) manual tasks, (2) admin/tech tasks, (3) cognitive high-exposure, (4) cognitive already AI-penetrated
- Different adoption parameters and S-curves per cluster
- Aggregation at task level from 90,000 subtasks
- Back-testing against historical unemployment (overall, youth, by education level)
- UK model being finalized
- METR data available but not updated fast enough

**Mar 26 (K-Medoids & Live Reports):**
- 12 feature vectors per task from O*NET job-task pairs
- K-Medoids clustering into 4 clusters with labeled adoption parameters (ceiling, time to 80%, base floor adoption %)
- Full pipeline: capability parity > cost parity > S-curve adoption > hours freed > risk vs productivity split > ceiling cap
- Aggregation: subtask > task > job > job group > economy
- Back-tested against 5 months actual unemployment data
- Model currently UNDER-PREDICTS unemployment -- needs calibration
- **In-product parameter tuning**: Can tweak cluster parameters and regenerate numbers live
- Capacity factor concept proposed but not yet implemented

### 3.2 Specific Data Demands

| Data Source | Purpose | Status |
|-------------|---------|--------|
| O*NET | Task/subtask decomposition for 341 occupations | Available in skill data |
| BLS OEWS | Employment counts, wage data by occupation | Available in skill data |
| Anthropic Economic Index | E0/E1/E2 task exposure categories, conversation penetration % | Referenced but not integrated |
| METR/HCAST | AI capability benchmarks, doubling time | Used in both old and new systems |
| Youth unemployment | Specific tracking metric for calibration | NOT tracked by either system |
| College graduate unemployment | Specific tracking metric | NOT tracked by either system |
| UK unemployment data | UK model | NOT built |
| China field intelligence | PowerPoints from Peter/Guido trips | NOT integrated |
| Jane's macro data | Macro context | NOT integrated |

### 3.3 Tony's Analysis Methodology Requirements

1. **No cost floors**: Cost curves run until physics says otherwise. Tony's Moore's Law story -- people at Intel in 1992 said the curve couldn't continue.
2. **Unemployment over GDP**: Focus on unemployment impact, not GDP growth.
3. **Regional costs, not PPP**: Use actual market costs, not purchasing power parity.
4. **Back-testing is mandatory**: "If we don't test it on actual data, what are we gonna test it on?"
5. **SIBA/STDF framework is non-negotiable**: Cost curves, S-curves, tipping points, convergence, feedback loops.
6. **Predictive or don't add complexity**: "It has to be predictive. If it's not predictive, we don't want to introduce complexity just to introduce complexity."
7. **Self-learning model**: Model should self-refine from incoming data.

### 3.4 Robert's Requirements

1. **Back-testing with zero tolerance**: "Why are we pretending that this is insightful and predictive when it actually today has no predictive power?"
2. **Model self-awareness / wealth warnings**: Model should flag when it has no predictive power and suggest shelving itself.
3. **Non-linear disruption thresholds**: "At 16 minutes [between hallucinations], maybe it doesn't show up. At 4 hours, it's a beast. At 64 hours, I'm gone."
4. **Time-travel analysis**: Go back in time and predict forward to validate.
5. **Nine hypotheses for model failure**: Economic upswing, wrong thesis, non-linear thresholds, GPU supply lag, regulatory barriers, install time, startup growth time, labor regulations, capacity sufficient only for augmentation.

### 3.5 Priority Ordering

- **US > UK > China > EU** for unemployment analysis
- AI/Employment is #1 sector priority (most meeting time, core investment thesis)
- US and UK reports were expected live in product by Mar 27

---

## 4. GAP ANALYSIS

### Rating: COVERED = fully implemented | PARTIAL = exists but incomplete | MISSING = not present

| # | Capability | Old Skill System | New STDF v2 Pipeline | Meeting Expectation | Gap Rating |
|---|-----------|-----------------|---------------------|---------------------|------------|
| 1 | Bottom-up task decomposition (BLS > O*NET > sub-tasks) | COVERED (341 jobs, 89K subtasks) | MISSING (aggregate S-curve, no subtask loop) | REQUIRED | **MISSING in new** |
| 2 | Task clustering (K-Medoids, 4 clusters) | MISSING (uniform parameters) | MISSING | REQUIRED (Mar 26 final methodology) | **MISSING in both** |
| 3 | Per-cluster adoption parameters | MISSING (uniform) | MISSING | REQUIRED (ceiling, time to 80%, base floor per cluster) | **MISSING in both** |
| 4 | Capability parity + cost parity per task | COVERED (per-subtask check) | PARTIAL (aggregate parity checks, 10-dim capability, but not per-task) | REQUIRED | **PARTIAL** |
| 5 | S-curve adoption per cluster | MISSING (single S-curve) | PARTIAL (empirical aggregate S-curve, not per-cluster) | REQUIRED | **PARTIAL** |
| 6 | Hours freed calculation | COVERED (per subtask per month) | MISSING (works in % task share, not hours) | REQUIRED | **MISSING in new** |
| 7 | Risk vs. productivity split | COVERED (50/50 configurable) | MISSING (not modeled in new pipeline) | REQUIRED | **MISSING in new** |
| 8 | Aggregation (sub-task > task > job > economy) | COVERED (full pipeline) | MISSING (no bottom-up aggregation) | REQUIRED | **MISSING in new** |
| 9 | Back-testing against actual unemployment | MISSING | MISSING | CRITICAL (Robert's #1, Tony's mandatory) | **MISSING in both** |
| 10 | Youth unemployment tracking | MISSING | MISSING | HIGH PRIORITY (Mar 11) | **MISSING in both** |
| 11 | UK model | MISSING | PARTIAL (UK in regional-adopter but no UK-specific analysis) | HIGH PRIORITY (US > UK > China > EU) | **PARTIAL** |
| 12 | Capacity factor concept | MISSING | MISSING | PROPOSED (Mar 26, contingent on predictive value) | **MISSING in both** |
| 13 | In-product parameter tuning | PARTIAL (CLI overrides) | MISSING (no parameter tuning in pipeline) | REQUIRED (Mar 26: tweak and regenerate live) | **PARTIAL in old** |
| 14 | Self-learning / self-refining model | MISSING | MISSING | DESIRED (Robert's requirement) | **MISSING in both** |
| 15 | Predictive power warnings | MISSING | PARTIAL (confidence scores per agent, but no "this model has no predictive power" warning) | REQUIRED (Robert's "wealth warnings") | **PARTIAL in new** |
| 16 | Regional cost analysis (not PPP) | PARTIAL (US only, actual wages) | COVERED (5 regions with actual cost data) | REQUIRED | **COVERED in new** |
| 17 | Cost-curve dynamics (no floors) | COVERED ($0.01 floor exists but configurable) | COVERED (exponential fit, no artificial floor) | REQUIRED | **COVERED** |
| 18 | SIBA/STDF compliance framework | PARTIAL (self-assessed scorecard) | COVERED (evaluator agent, banned vocabulary, guardrails) | NON-NEGOTIABLE | **COVERED in new** |
| 19 | Feedback loop modeling | PARTIAL (named loops, no quantification) | PARTIAL (virtuous/vicious cycles documented, not quantified) | REQUIRED | **PARTIAL** |
| 20 | X-curve incumbent decline | MISSING | COVERED (death spiral stages, market trauma) | IMPLIED (Tony wants to see "when it falls off a cliff") | **COVERED in new** |
| 21 | Convergence analysis | MISSING | COVERED (6 convergence architectures) | IMPLIED (STDF framework) | **COVERED in new** |
| 22 | Chimera recognition | MISSING | COVERED (AI copilots as chimera, hump-shaped dynamic) | IMPLIED (STDF framework) | **COVERED in new** |
| 23 | Data provenance / source hierarchy | PARTIAL ([R1] markers) | COVERED (T1/T2/T3, [observed]/[model-derived]) | REQUIRED | **COVERED in new** |
| 24 | Deflationary thesis framing | MISSING | COVERED ($3-6T/yr wage compression, universal input disruption) | CORE THESIS | **COVERED in new** |

### Summary

| Rating | Count | Details |
|--------|-------|---------|
| COVERED (in new or both) | 8 | Regional costs, cost curves, STDF compliance, X-curve, convergence, chimera, data provenance, deflationary thesis |
| PARTIAL | 5 | Capability/cost parity per task, S-curve per cluster, UK model, predictive warnings, feedback loops |
| MISSING in new pipeline | 4 | Bottom-up subtask sim, hours freed, risk/productivity split, aggregation chain |
| MISSING in both | 5 | K-Medoids clustering, per-cluster adoption, back-testing, youth unemployment, capacity factor, self-learning |

---

## 5. MIGRATION PLAN

### 5.1 What Can Be Migrated from Old Skill to New STDF Agents

**Directly reusable:**
1. **The subtask dataset** (341 jobs, 12,996 tasks, 89,040 subtasks) -- this is the foundation. The compressed JSON parts in `.claude/skills/artificial-labor/data/` are the most valuable asset.
2. **The simulation engine** (`lib/simulator.py`, `lib/models.py`, `lib/aggregator.py`, `lib/data_loader.py`) -- the monthly simulation loop that processes capability > cost > tipping > adoption > hours freed > split > ceiling per subtask.
3. **The job-to-group mapping** (`job_to_group_mapping.csv`) -- maps 341 jobs to 24 BLS occupation groups.
4. **Configuration schema** (`simulation_config.json`) -- the parameter structure is well-designed and supports scenario runs.
5. **The methodology documentation** -- `AL_Methodology_Framework.md` describes the full architecture including parts (8-14) not yet implemented.

**Reusable with adaptation:**
6. **The AL Gap Analysis** -- identifies specific gaps against Tony's requirements that remain relevant.
7. **The existing research corpus** -- academic review, data feasibility, SME review documents provide context.

### 5.2 What Must Be Rebuilt from Scratch

1. **K-Medoids clustering engine**: The skill has no clustering. A new module must take 12 feature vectors per task from O*NET job-task pairs, run K-Medoids into 4 clusters, and assign per-cluster adoption parameters (ceiling, time to 80%, adoption lag, base floor).
2. **Back-testing module**: Compare model predictions against actual BLS unemployment data (overall, youth, by education, by occupation group). Generate fit metrics (R^2, RMSE, directional accuracy).
3. **Parameter calibration loop**: When back-testing shows under-prediction (as it does per Mar 26), the system needs a calibration process to adjust cluster parameters.
4. **UK and China models**: New data pipelines for UK (ONS data) and China (NBS data) labor markets, with region-specific occupation structures, wages, and regulatory environments.
5. **Youth unemployment tracker**: Specific data feed and model output tracking youth (16-24) and college graduate unemployment against AI displacement.
6. **Predictive power warnings**: A validation module that runs automatically, checks model predictions against recent actuals, and generates confidence/warning flags if R^2 drops below threshold.
7. **In-product parameter tuning interface**: The ability to tweak cluster parameters and regenerate displacement numbers live (this is a product/frontend concern but the backend simulation must support fast re-runs).

### 5.3 What the New STDF Framework Provides That the Old System Lacks (and Vice Versa)

**New STDF provides, old lacks:**
- Multi-agent DAG with cross-validation and evaluator
- Regional S-curve fitting (USA, China, EU, India, RoW)
- X-curve incumbent decline modeling with market trauma detection
- Convergence and chimera analysis
- Formal tipping window with binding constraint identification
- CTE-normalized cost comparison
- [observed]/[model-derived] data tagging with T1/T2/T3 hierarchy
- Banned vocabulary and guardrail enforcement
- File-based agent communication (auditable, reproducible)
- Confidence scoring (per-agent and pipeline aggregate)
- Deflationary shock framing as analytical thesis

**Old system provides, new lacks:**
- Bottom-up subtask-level simulation (89,040 subtasks)
- Per-occupation displacement forecasts with specific tipping dates
- Hours-freed and FTE-replaced calculations
- Replacement vs. productivity split modeling
- Configurable scenario runs via CLI
- Ceiling application at job level with overflow to productivity
- The actual computational engine that produces granular numbers

### 5.4 Recommended New Agent Architecture

The ideal migration creates a HYBRID that combines the new STDF pipeline's analytical framework with the old skill's computational engine. Recommended agent set:

#### Tier 0 (Pre-pipeline): Data & Clustering

**Agent: `stdf-al-data-loader`** (NEW)
- Reads the 341-job subtask dataset
- Extracts 12 feature vectors per task from O*NET data
- Runs K-Medoids clustering into 4 clusters
- Assigns per-cluster adoption parameters based on cluster characteristics
- Outputs: `agents/00a-data-clusters.md` (cluster definitions, parameter assignments)
- **Criticality**: CRITICAL

**Agent: `stdf-al-backtester`** (NEW)
- Reads the simulation output + actual BLS unemployment data
- Computes fit metrics (R^2, RMSE, directional accuracy) at economy, group, and age levels
- Generates predictive power warnings if fit is poor
- Outputs: `agents/00b-backtest-results.md`
- **Criticality**: HIGH

#### Tier 1 (Foundation): Existing STDF Agents + AL Simulation

Existing agents run as-is:
- `stdf-domain-disruption` -- maps the labor sector, identifies sub-domains
- `stdf-cost-researcher` -- gathers cost data (AI inference + human labor)
- `stdf-capability` -- 10-dimension capability assessment

**Agent: `stdf-al-simulator`** (NEW -- wraps old skill)
- Runs the adapted simulation engine with K-Medoids cluster parameters
- Per-cluster S-curves instead of uniform adoption
- Full subtask > task > job > group > economy aggregation
- Outputs: `agents/01b-al-simulation.md` (occupation-level results, economy totals, hours freed, FTE displaced, replacement/productivity split)
- **Criticality**: CRITICAL

#### Tier 2-5: Existing STDF Pipeline

Run exactly as today:
- Cost Fitter, Cost Parity Checker, Capability Parity Checker, Adoption Readiness Checker
- Tipping Synthesizer
- S-Curve Fitter (now calibrated against both proxy data AND simulation output)
- Regional Adopter (extended to include UK as standalone region)
- X-Curve Analyst

#### Tier 6 (New): Validation & Calibration

**Agent: `stdf-al-calibrator`** (NEW)
- Reads backtest results + simulation output
- Proposes parameter adjustments to improve fit
- Re-runs simulation with adjusted parameters
- Outputs: `agents/06b-calibration.md` (parameter changes, fit improvement)
- **Criticality**: HIGH

#### Final: Synthesizer + Evaluator (existing)

The synthesizer must integrate BOTH the aggregate STDF pipeline outputs AND the granular AL simulation results into a single 7-phase narrative.

### 5.5 Data Requirements

| Data | Source | Status | Priority |
|------|--------|--------|----------|
| 341-job subtask dataset (US) | Existing skill data | AVAILABLE | P0 |
| O*NET feature vectors (12 per task) | O*NET database | PARTIALLY AVAILABLE | P0 |
| BLS OEWS employment + wages | BLS | AVAILABLE in skill data | P0 |
| Actual US unemployment (monthly, last 36 months) | BLS CPS | NEEDS INTEGRATION | P0 |
| Youth unemployment (16-24, monthly) | BLS CPS | NEEDS INTEGRATION | P1 |
| College graduate unemployment | BLS CPS / NCES | NEEDS INTEGRATION | P1 |
| UK employment by occupation | ONS | NEEDS SOURCING | P1 |
| UK wages by occupation | ONS ASHE | NEEDS SOURCING | P1 |
| Anthropic Economic Index (E0/E1/E2 categories) | Anthropic | NEEDS INTEGRATION | P2 |
| China employment by sector | NBS China | NEEDS SOURCING | P2 |
| METR/HCAST latest benchmarks | METR | PARTIALLY AVAILABLE (needs auto-refresh) | P1 |
| AI inference cost time series (real-time) | API pricing aggregators | AVAILABLE in STDF data catalog | P0 |

### 5.6 Effort Estimate

| Component | Effort | Dependencies | Priority |
|-----------|--------|-------------|----------|
| **Migrate skill data to STDF data catalog** | 1-2 days | None | P0 |
| **Adapt simulation engine to STDF lib/** | 3-5 days | Data migration | P0 |
| **Build K-Medoids clustering module** | 3-4 days | Feature vector extraction from O*NET | P0 |
| **Build per-cluster S-curve adoption** | 2-3 days | Clustering module | P0 |
| **Create stdf-al-simulator agent definition** | 1-2 days | Adapted engine | P0 |
| **Integrate actual unemployment data for back-testing** | 2-3 days | BLS CPS data pipeline | P1 |
| **Build stdf-al-backtester agent** | 2-3 days | Actual data + simulation output | P1 |
| **Build stdf-al-calibrator agent** | 2-3 days | Backtester | P1 |
| **Extend regional-adopter for UK** | 2-3 days | UK ONS data | P1 |
| **Youth + college graduate unemployment tracking** | 1-2 days | BLS CPS age breakdown | P1 |
| **Predictive power warning system** | 1-2 days | Backtester | P2 |
| **In-product parameter tuning** | 3-5 days | Server/frontend integration | P2 |
| **China model** | 5-7 days | NBS data, field intelligence | P3 |
| **Self-learning/self-refining loop** | 5-7 days | Full calibration infrastructure | P3 |

**Total estimated effort:**
- **P0 (core migration)**: 10-16 days
- **P1 (back-testing + UK + calibration)**: 9-14 days
- **P2 (warnings + tuning)**: 4-7 days
- **P3 (China + self-learning)**: 10-14 days

**Critical path**: Data migration > simulation adaptation > clustering > per-cluster S-curves > simulator agent > synthesizer integration. This path is approximately 10-14 days to produce a first working run.

### 5.7 Migration Strategy Summary

The migration is NOT a replacement of old with new -- it is a MERGER:

1. **Keep the new STDF v2 pipeline** as the analytical framework (domain-disruption, cost-fitter, capability, parity checkers, tipping synthesizer, S-curve, regional, X-curve, evaluator).
2. **Port the old skill's simulation engine** into a new STDF agent (`stdf-al-simulator`) that produces the granular occupation-level numbers Tony and Robert need.
3. **Add the K-Medoids clustering** that Tony's team finalized on Mar 26 -- this is the key methodological advance neither old nor new system has.
4. **Build back-testing** as a new agent that runs automatically and generates predictive power assessments.
5. **The synthesizer integrates both**: the STDF framework's tipping/S-curve/X-curve analysis AND the simulation's per-occupation FTE displacement numbers.

This produces a system that answers Tony's question ("when does unemployment hit 9-16%?") with both the macro disruption framework AND the granular bottom-up numbers, validated against actual data.

---

## Appendix: File Reference

| File | Path |
|------|------|
| Old agent prompt | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/old_prompts/artificial_labor_subagent_system.txt` |
| Old sector report | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/old_prompts/sector_reports/family1-labor-report.txt` |
| Skill README | `/Users/himanshuchauhan/TONY/STDF/skills/skill-instructions/artificial-labor/README.md` |
| Deployed skill | `/Users/himanshuchauhan/TONY/STDF/skills/.claude/skills/artificial-labor/SKILL.md` |
| Skill methodology | `/Users/himanshuchauhan/TONY/STDF/skills/.claude/skills/artificial-labor/references/methodology.md` |
| Skill config | `/Users/himanshuchauhan/TONY/STDF/skills/.claude/skills/artificial-labor/config/simulation_config.json` |
| Gap analysis | `/Users/himanshuchauhan/TONY/STDF/skills/skill-instructions/artificial-labor/existing research/AL_Gap_Analysis_Tony_Requirements.md` |
| Methodology framework | `/Users/himanshuchauhan/TONY/STDF/skills/skill-instructions/artificial-labor/existing research/AL_Methodology_Framework.md` |
| New final synthesis | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/output/ai-cognitive-labor/00-final-synthesis.md` |
| New synthesizer metadata | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/output/ai-cognitive-labor/agents/06-synthesizer.md` |
| STDF pipeline CLAUDE.md | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/CLAUDE.md` |
| STDF shared rules | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/stdf/shared-rules.md` |
| Meeting: sector/commodity | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/meetings/consolidated_sector_commodity.md` |
| Meeting: Tony vs Robert | `/Users/himanshuchauhan/TONY/STDF/stdf-agents/archive/meetings/consolidated_tony_vs_robert.md` |
