# STDF Framework/Core Orchestration Migration Report

**Compiled:** 2026-03-27
**Scope:** Old system (multi-agent chat pipeline) -> Skills system (Stellar Core) -> New STDF v2 pipeline (Claude Code agents)
**Sources:** 13 old prompts, Stellar Core skill instructions, Skills SYSTEM_PROMPT, 24 new agent definitions, 4 shared rule files, 4 lib modules, 3 meeting consolidation reports

---

## 1. OLD SYSTEM ANALYSIS

### 1.1 Main Agent Orchestration

The old system's `main_agent_system.txt` (~550 lines) is a monolithic prompt that serves as the central router, analyst, and presentation layer. It receives a reformulated query from the reformulator, routes to 8 specialized subagent tools, synthesizes outputs, and produces a JSON response with chart data, company mentions, VCA suggestions, and plan updates.

**Routing mechanism:** The reformulator classifies intent (new_question, feedback_only, revise_previous, meta_request, history_request, trace_explain, vca_company_analysis, company_analysis) and populates `sector_hints` and a `[SUBAGENT ROUTING]` block. The main agent reads these and deterministically invokes the matching subagent tools. Sector hints map to four validated skill domains (lithium-ion-demand, artificial-labor, copper-forecast, energy-sector). A STDF exclusion rule prevents redundant STDF analysis when sector agents already cover the domain.

**Chaining patterns:**
- STDF -> Stellar: handoff_context as stdf_context
- STDF -> Feedback Loop: handoff_context as stdf_context
- STDF -> Value Investment: output as skill_outputs (Mode A)
- Skill -> Value Investment: skill output as skill_outputs (Mode A)

**Key architectural features:**
- Plan lifecycle ownership (main agent owns the active plan)
- Skill Sovereignty doctrine (5 rules: use skill, trust outputs, no shadow modeling, no methodology mixing, preserve exact outputs)
- 3-tier post-processing hierarchy (TIER 1 automatic, TIER 2 requires user confirmation, TIER 3 forbidden)
- Derived Calculation Gating (must present assumptions, wait for confirmation)
- Scenario Gating (no scenarios unless explicitly requested)
- Internal validation checklist (6 anti-pattern checks before output)
- Citation hard rules ([C#] markers, downstream citation builder)
- Company mention markers ([[COMPANY:CO#]])
- JSON-only output contract with chart_data, plan_update, company_mentions

**Strengths:** The main agent encodes deep institutional knowledge about Seba methodology in a single prompt. Skill Sovereignty doctrine prevents hallucination. The routing system handles complex multi-step chains (STDF->Feedback->Value Investment). The confirmation-based flow for derived calculations prevents fabricated assumptions.

**Weaknesses:** The monolithic prompt is ~550 lines and growing. Every capability addition requires editing this single file. No file-based communication -- everything passes through prompt context. No DAG resolution -- routing is keyword-based. The main agent is simultaneously router, synthesizer, and evaluator, creating a single point of failure.

### 1.2 STDF Sub-Agent Methodology

The STDF sub-agent (`stdf_subagent_system.txt`, 182 lines) implements a 7-phase disruption analysis:

1. Sector scoping
2. Technology inventory
3. Convergence analysis
4. Disruption pattern classification (From Below / From Above / Big Bang / Architectural / Systemic)
5. Business-model shift
6. Adoption/S-curve
7. Synthesis

**Quantitative method expectations:**
- Cost trajectory: C(t) = C0 * exp(-r * delta_t)
- Convergence and threshold timing in service-unit terms
- Rupture window logic tied to threshold crossings + feedback loop shifts + incumbent economic weakening
- S-curve position classification (pre-tipping, tipping, acceleration, saturation)
- Confidence calibration: 0.80-1.00 (strong), 0.60-0.79 (plausible), 0.40-0.59 (ambiguous), <0.40 (insufficient)

**Output:** Structured JSON with phases, confidence scores, assumptions, data_gaps, and handoff_context containing cost_curves, adoption_curve_signals, and critical_uncertainties.

**Assessment:** Rigorous analytical skeleton, but entirely dependent on the LLM following instructions without hard enforcement. No library functions, no compliance checks, no file-based output. Handoff context is a JSON blob passed through prompt, not a persistent file.

### 1.3 Feedback Loop Analyzer

The feedback loop sub-agent (`feedback_loop_subagent_system.txt`, 153 lines) is one of the old system's most sophisticated components. It implements a 6-step workflow:

1. Identify domain, disruptions, and value drivers
2. Define falsifiable, time-bound shock statement
3. Map 5-actor reactions (Government, Central Bank, Consumers, Corporations, Markets) with strength scores, time lags, and evidence
4. Build competing feedback loops (R = accelerator, B = brake) with causal chains and competing_with fields
5. Generate 3-scenario adjusted forecast (No Reaction, Moderate Reaction, Strong Reaction)
6. Derive strategic implications with monitoring indicators, timing windows, and invalidation conditions

**Unique features:**
- Actor Reference Matrix with shock-type-specific reaction templates
- Timing framework with explicit lag ranges per actor type (Market: 0-3mo, Consumer: 0-6mo, Corporate: 3-12mo, Regulatory: 6-18mo, Infrastructure: 3-5yr)
- Mandatory competing_with field linking opposing loops
- Second-order effects from loop interactions
- Tipping points defined as conditions where one loop overtakes another
- Integration with STDF context (uses rupture windows, confidence levels as quantitative anchors)
- STDF skill recommendation when domain matches

**Assessment:** This is the most intellectually complete agent in the old system. The 5-actor model with competing feedback loops and 3-scenario framework is analytically powerful. The tool budget management (Steps 1-3: web search; Step 4: pure synthesis; Step 5: no new searches) is well-designed.

### 1.4 Stellar Sub-Agent (Investment Thesis)

The Stellar sub-agent (`stellar_subagent_system.txt`, 161 lines) converts disruption economics into actionable trade frameworks via 4 stages:

1. Economics and thesis decomposition (behaves like fundamentals researcher)
2. Trade expression and instrument mapping (behaves like trader)
3. Stress test and risk framing (Fragile/Robust/Antifragile classification)
4. Execution plan (entry triggers, invalidation, position sizing)

**Unique features:**
- Hype Delta framework: HYPE_DELTA = Market-Implied Narrative - Operational Reality
- Transition quality checks between stages (won't proceed if edge doesn't exist)
- No-trade output when edge is weak
- Recommendation quality rubric (testable thesis, observable triggers, explicit falsifiers, conviction-based sizing)

**Assessment:** This is the investment-specific layer that translates STDF analysis into trading decisions. The Hype Delta concept is original and powerful. The explicit no-trade output prevents forced trades.

### 1.5 Evaluator, Planner, Reformulator, Citation Builder

**Evaluator** (`evaluator_system.txt`, 115 lines): Post-hoc quality gate checking factual grounding, temporal consistency, methodology compliance (SEBA method checklist), Skill Sovereignty, numeric rules. Outputs PASS/MINOR_ISSUES/MAJOR_ISSUES. Key checklist items: service unit defined, incumbent vs. disruptor compared on cost per service unit, S-curve + X-curve (not linear), Jevons Paradox applied only where applicable, long tail prohibited, market trauma awareness, chimera recognition, feedback loop verification (disruptor virtuous, incumbent vicious), data confidence tiers. Also enforces Disruption Dynamics Engine guardrails (no mainstream anchoring, no constraint invention, no clipping, no incumbent protection).

**Planner** (`planner_system.txt`, 673 lines): Creates execution plans with tier routing (DIRECT/LIGHTWEIGHT/FULL). Encodes Skill Sovereignty doctrine, SEBA framework, S-curve methodology, and tipping point definitions. Handles 5 follow-up query types (explainability, scenario, derivative, parameter change, scope extension) with gating rules and decision tree. Outputs structured JSON with steps, data_requirements, retrieval_type, fallback, quality_gates.

**Reformulator** (`reformulator_system.txt`, 326 lines): Neutralizes user framing (anti-sycophancy), extracts hypotheses, assigns complexity confidence, routes to sectors, preserves STDF terminology (84+ terms in preservation table), classifies intent (8 types), appends [SUBAGENT ROUTING] blocks with chaining instructions. Detailed sector_routing_rules for 6 sector agents.

**Citation Builder** (`citation_builder_system.txt`, 35 lines): Creates structured citations for [C#] markers using only provided tool evidence. Maps provenance pointers (G#/D#/W#/S#/R#). Extracts URLs from web search evidence.

**Report Knowledge Lookup** (`report_knowledge_lookup_system.txt`, 48 lines): Pure data extraction agent that searches pre-computed sector reports. Reproduces ALL columns verbatim. Assesses coverage (fully_covered/partially_covered/not_covered). Never fabricates.

**Trace Explain** (`trace_explain_system.txt`, 136 lines): Explains system's reasoning using stored trace context. Translates internal terms to user-facing language (GraphRAG -> "SEBA corpus", skill.md -> "the relevant skill"). Attributes every claim to its source.

### 1.6 Tony Core Prompt

The `tony_core.txt` (343 lines) is the STDF reference knowledge base embedded in the system. It encodes:

- **Core Axioms:** Convergence, 10x Factor, Phase Change, Metamorphosis Principle
- **S-Curve Dynamics:** Thresholds (2-5% rupture, ~10% tipping, >80% saturation), left-skewed adoption, tipping point definition (ALL THREE: cost parity + capability + adoption readiness)
- **System Dynamics:** Virtuous/vicious cycles, Boulder Analogy, self-organization, cross-sector feedback loops (Energy->Transport, Energy->AI, Energy+AI->Food)
- **Market Trauma & Stranded Assets:** Financial collapse precedes physical obsolescence
- **Incumbent Response Pattern:** 7 stages (Denial->Dismissal->Doubt-sowing->Lobbying->Chimeras->Protectionism->Collapse)
- **Sector analyses:** Energy (SWB, God Parity, Clean Energy U-Curve, Superpower), Transportation (TaaS at $0.05-0.10/mile vs ICE $0.80/mile), Food (Precision Fermentation), Labor (AI+Robotics convergence)
- **Stellar Framework:** X-Flow vs Seed-Flow, Ignition Point, Radiance
- **Historical precedents:** Cars 2%->95% in 20 years, digital cameras 2%->98% in 15 years
- **RethinkX prediction track record:** 99.2% accuracy on 2014 EV cost prediction

**Assessment:** This is the intellectual core of the system. It is a remarkably complete encoding of Tony Seba's framework. However, it is a static reference document, not a dynamic analytical system. The new system needs to preserve every concept here while making them enforceable rather than advisory.

### 1.7 Terminology Guardrails

The `terminology_guardrails.txt` (147 lines) enforces Seba-aligned language:

- **Banned terms:** 27 terms including "transition", "evolution", "renewable energy", "net zero", "hydrogen economy", "Wright's Law", "IEA/EIA/BNEF/OPEC", "mainstream", "conservative"
- **Banned hedging phrases:** 14 phrases including "time will tell", "to be conservative", "in the real world"
- **Required tone:** Analytical, confident, mathematical, unapologetic
- **Tone violations:** Hedging supported conclusions, using "might/could", softening exponential projections
- **Replacement guidance:** 15 banned->preferred mappings with reasoning
- **Role-specific rules:** Different enforcement per agent (Reformulator rewrites, Evaluator flags MAJOR_ISSUES, etc.)

### 1.8 Web Search Agent

The `web_search_subagent_system.txt` (154 lines) is a temporal gap-filler that sits at Priority 4 (lowest) in the evidence hierarchy:

1. Internal curves & DB tables
2. Seba GraphRAG corpus
3. Sector skills
4. Web search (you)

**Key constraints:** Only searches for deltas since last data update. Rejects forecasts. Reports values in STDF service units. Tags chimeras with [CHIMERA: incumbent-aligned]. Flags disruption signal markers ([SIGNAL: cost-parity], [SIGNAL: incumbent-distress]). Source quality hierarchy (Primary: government, Secondary: financial press, Tertiary: blogs). Applies STDF anti-pattern guardrails to its own output.

### 1.9 Strengths of the Old Architecture

1. **Comprehensive framework encoding:** Tony's philosophy is deeply embedded across all prompts
2. **Multi-agent specialization:** Each agent has a clear, bounded role
3. **Skill Sovereignty doctrine:** Prevents LLM hallucination in quantitative domains
4. **Anti-sycophancy at the gate:** Reformulator neutralizes leading questions before analysis
5. **Evidence hierarchy:** Clear priority ordering (internal > corpus > skills > web)
6. **Feedback loop analyzer:** The most intellectually sophisticated component
7. **Investment translation:** STDF -> Stellar -> Value Investment chain is complete
8. **Terminology enforcement:** Comprehensive banned/required vocabulary across all agents

### 1.10 Weaknesses / What Breaks

1. **No file-based communication:** All data passes through prompt context, creating context window pressure and information loss
2. **No hard enforcement:** Vocabulary rules, compliance criteria, and guardrails are advisory (prompt-based), not enforced programmatically
3. **Monolithic main agent:** ~550-line prompt that grows with every feature
4. **No DAG resolution:** Routing is keyword-matched from reformulator hints, not dynamically resolved from dependency graphs
5. **No persistent evaluation:** Evaluator runs inline, not as a separate auditable step
6. **No computational libraries:** All math is done ad-hoc by the LLM, with no validated functions
7. **No empirical data catalog:** Web search is the primary data source; no curated time-series curves
8. **No compliance framework:** Quality is assessed subjectively, not against numbered criteria with severity levels
9. **No hooks for real-time enforcement:** Banned vocabulary can still leak through since there's no PreToolUse interception
10. **Single evaluator pass:** If the evaluator misses a violation, there's no safety net

---

## 2. NEW STDF PIPELINE ANALYSIS

### 2.1 Orchestrator Architecture (CLAUDE.md)

The new orchestrator (`stdf/CLAUDE.md`, ~394 lines) operates on 4 foundational principles:

1. **Reason from the question to the agents** -- agent selection emerges from analytical reasoning, not keyword matching
2. **The DAG is the only hard sequencing constraint** -- dependencies are non-negotiable, everything else is flexible
3. **Exercise judgment on process gates** -- complex scope always confirms; simple scope may auto-approve
4. **Fill gaps proactively** -- inject research agents when data gaps threaten downstream quality

**Phases:**
- Phase 0: Setup (create output directory, derive slug, store variables)
- Phase 1: Analyze Query & Select Agents (reason about needed outputs, resolve DAG backward, confirm with user if 6+ agents)
- Phase 1c: Classification Approval (X-Flow/Stellar/Hybrid classification after Tier 1 completes)
- Phase 2: Plan (resolve DAG, group into parallel tiers, identify research injection points)
- Phase 3: Execute (tier-by-tier with parallel agent launches, failure handling, research injection)
- Phase 4: Evaluate (stdf-evaluator agent on Haiku)
- Phase 5: Write Index & Present

**Key architectural features:**
- Dynamic DAG resolution from Agent Registry (never hardcoded)
- File-based communication only (agents write files, downstream agents read files)
- Progress checklist tracking
- Agent re-run permitted for weak outputs
- Research injection between tiers
- Evaluator always runs last

### 2.2 The 23-Agent Pipeline with File-Based Communication

The pipeline has 24 agent definitions (18 pipeline + 1 research + 1 evaluator + 4 utility):

**Core pipeline (Tiers 1-5b, 12 agents):**
- Tier 1 (parallel): domain-disruption, cost-researcher, capability
- Tier 2: cost-fitter
- Tier 3 (parallel): cost-parity-checker, capability-parity-checker, adoption-readiness-checker
- Tier 4: tipping-synthesizer
- Tier 5a: scurve-fitter
- Tier 5b (parallel): regional-adopter, xcurve-analyst
- Final: synthesizer
- Eval: evaluator (Haiku)

**Conditional commodity chain (Tier 6, 4 agents):**
- demand-decomposer -> stream-forecaster -> fleet-modeler + regional-demand-analyst

**Conditional energy chain (Tier 7, 2 agents):**
- energy-dispatch -> gas-supply-decomposer

**Flex:** stdf-research (injected anywhere)

**File-based communication protocol:**
- Each agent writes to `output/<slug>/agents/<nn>-<agent-name>.md`
- Downstream agents read upstream files via `UPSTREAM_FILES:` paths
- Synthesizer reads ALL produced files and produces `output/<slug>/00-final-synthesis.md`
- Every agent output follows a standardized markdown template: Agent Reasoning -> Agent Output -> Sources

**Agent prompt template (every agent gets):**
```
Analysis date: {DATE}
QUERY: {full user query}
OUTPUT_FILE: output/{SLUG}/agents/{filename}
UPSTREAM_FILES: [list of dependency files]
```

### 2.3 Shared Rules Enforcement

`shared-rules.md` (~400 lines) is read by ALL agents and enforces:

**Banned Vocabulary:** 39 banned terms with replacements (expanded from old system's 27), including new additions: "decarbonization", "base case/bull case/bear case", "optimistic/pessimistic scenario", "AI capability growth" -> "AI capability improvement"

**Banned Hedging Phrases:** Same 14 phrases as old system

**Required Vocabulary:** 10 mandatory terms (disruption, stellar energy, cost-curve dynamics, market-driven disruption, incumbent displacement, S-curve adoption, etc.)

**Required Tone:** Analytical, confident, mathematical, unapologetic (same as old system but now enforced programmatically via vocabulary.py)

**Date Awareness:** Strict temporal anchoring -- data before analysis date is [observed], after is [model-derived]

**Web Search Guardrails:** Historical-only rule, forecast ban (CRITICAL GUARDRAIL), source hierarchy (Published Reports > Local Data Catalog > Web Search)

**Core Analytical Guardrails:** No linear extrapolation, no narrative without numbers, no ESG framing, no policy-driven narratives

**Disruption Dynamics Guardrails (10 rules):**
1. No Mainstream Anchoring
2. No Constraint Invention
3. No Clipping
4. No Incumbent Protection
5. No Long Tail
6. S-Curve Threshold Values (2-5% rupture, ~10% tipping, >80% saturation)
7. Market Trauma Awareness
8. Chimera Recognition
9. Feedback Loop Consistency
10. Data Confidence Tiers (Tier 1 Energy/Transport, Tier 2 Labor/Materials, Tier 3 Food)

**Jevons Paradox rules:** X-Flow technologies only. Must check classification tag in `01-domain-disruption.md`. Propagation rule for 5 downstream agents.

**Banned Organization Policy:** IEA/EIA/BNEF/OPEC permitted ONLY for historical observed data with `[CAUTION: {org} source]` tag

**Data-Type Tagging:** Every numerical value must be tagged [observed] or [model-derived]

**Computation Rules (4 rules):**
1. Never estimate by hand -- ALL computation via python3
2. Use lib/ functions first (15 library modules mapped to agents)
3. Write inline python3 only when no lib function exists
4. Always report fit quality (R-squared, data points, year span)

### 2.4 Compliance Framework (C1-C10)

`lib/compliance.py` implements a generic checklist system with CRITICAL/HIGH/MEDIUM severity levels:

**Pre-defined criteria sets:**
- COST_CURVE_CRITERIA (2.1-2.11): 11 criteria including min 3 historical data points, service-level units, learning rate from data
- CAPABILITY_CRITERIA (3.1-3.6): 6 criteria including min 3 dimensions, historical trajectory
- ADOPTION_CRITERIA (4.1-4.6): 6 criteria including S-curve model required, regional breakdown
- TIPPING_CRITERIA (5.1-5.5): 5 criteria including all 3 conditions checked simultaneously
- SYNTHESIZER_CRITERIA (6.1-6.7): 7 criteria including zero banned vocabulary
- COMMODITY_DEMAND_CRITERIA (7.1-7.9): 9 criteria including 80% demand driver coverage, recursive decomposition, stock-flow fleet model
- PIPELINE_CRITERIA (P.1-P.6): 6 pipeline-level criteria

**Functions:**
- `create_checklist()`, `update_criterion()`, `has_critical_failure()`, `is_compliant()`, `overall_status()`, `checklist_to_markdown()`

**Status outcomes:** COMPLIANT / DEGRADED / NON-COMPLIANT

### 2.5 Pipeline Presets

8 named configurations plus CUSTOM:

| Preset | Agents | Typical Trigger |
|--------|--------|----------------|
| FULL | 12 | Comprehensive disruption analysis |
| QUICK | 3 | Cost overview, brief assessment |
| TIPPING_ONLY | 9 | Tipping point timing |
| COST_FOCUS | 4 | Cost trajectory, learning rates |
| ADOPTION_FOCUS | 12 | Market share, adoption curves |
| FULL+COMMODITY | 16 | Commodity demand impact |
| ENERGY_FULL | 14 | Energy sector dispatch |
| ENERGY_GAS | 14 | LNG/gas supply displacement |
| CUSTOM | Varies | Query-specific agent set |

### 2.6 Failure Matrix

| Criticality | On Failure | Penalty |
|-------------|-----------|---------|
| CRITICAL | STOP pipeline | -- |
| HIGH | Continue with warning | -0.3 |
| MEDIUM | Continue silently | -0.1 |

CRITICAL agents: cost-researcher, cost-fitter, cost-parity-checker, tipping-synthesizer, demand-decomposer (conditional)
HIGH agents: domain-disruption, capability, capability-parity-checker, adoption-readiness-checker, scurve-fitter
MEDIUM agents: regional-adopter, xcurve-analyst, fleet-modeler

### 2.7 Quality Gates at Every Level

**Level 1 -- PreToolUse Hook** (`hooks/stdf_validate.py`): Hard enforcement on file writes. Validates banned vocabulary, banned source URLs, forecast language, and anti-pattern phrases BEFORE the file is written. Exit code 2 blocks the write.

**Level 2 -- Per-Agent Compliance Checklists**: Each agent has numbered criteria (e.g., 2.1-2.11 for cost-fitter) with CRITICAL/HIGH/MEDIUM severity. Agents self-check and report in their output file.

**Level 3 -- Vocabulary Module** (`lib/vocabulary.py`): `scan_banned()`, `scan_banned_hedging()`, `scan_banned_sources()`, `check_required()`, `vocabulary_report()`. Programmatic enforcement, not prompt-based.

**Level 4 -- Guardrails Module** (`lib/guardrails.py`): `full_guardrail_check()` running 6 validation functions: banned vocabulary, banned sources, forecast language, anti-patterns, scenario labels, date consistency, citation provenance, data-type tags.

**Level 5 -- Evaluator Agent** (`stdf-evaluator.md`): Runs on Haiku model after synthesis. Checks A (banned vocabulary), B (hedging), C (tone), D (terminology preservation), E (disruption dynamics -- 10 sub-rules), F (analytical integrity -- 5 rules), G (banned sources), H (data-type tagging). Writes report to `07-evaluation.md` with PASS/FAIL verdict.

**Level 6 -- Pipeline Validation Script** (`scripts/validate_pipeline.py`): Post-hoc audit of all agent outputs.

### 2.8 What Is Fundamentally Better About the New Architecture

1. **File-based communication eliminates context window pressure.** Each agent reads exactly what it needs from disk, not from an ever-growing prompt. This is critical for FULL pipeline runs with 12+ agents.

2. **Programmatic enforcement replaces advisory prompts.** `lib/vocabulary.py` catches banned terms with regex, `hooks/stdf_validate.py` blocks writes in real-time. The old system relied on LLM compliance.

3. **DAG resolution from a single source of truth.** Agent Registry defines dependencies; the orchestrator resolves them dynamically. No hardcoded routing tables.

4. **Decomposed tipping point analysis.** Old system: one agent checks all 3 tipping conditions. New system: 3 separate checker agents (cost-parity, capability-parity, adoption-readiness) feed into a tipping-synthesizer. This prevents single-agent blind spots and makes each condition independently auditable.

5. **15 validated Python library modules.** `lib/cost_curve_math`, `lib/scurve_math`, `lib/tipping_math`, `lib/demand_math`, `lib/energy_math`, `lib/capability_math`, etc. Every calculation is reproducible and testable, not ad-hoc LLM math.

6. **956 curated empirical time-series curves.** Agents have direct access to validated data in `data/`, eliminating dependence on web search for core cost/adoption data.

7. **Auditable pipeline execution.** Every agent writes its reasoning, output, compliance checklist, and sources to disk. The entire analysis is reconstructable from files.

8. **Conditional pipeline configurations.** QUICK (3 agents) for simple queries vs FULL+COMMODITY (16 agents) for comprehensive analysis. The old system ran the same pipeline for everything.

9. **Research injection capability.** The orchestrator can insert `stdf-research` between any tiers when data gaps are identified, without restarting the pipeline.

10. **Persistent agent memory.** Each agent builds institutional knowledge across conversations -- synthesis patterns, common conflicts, data gaps, calibration insights.

### 2.9 What Is Lost from the Old System

1. **Feedback Loop Analysis.** The old system's feedback-loop-subagent with 5-actor model, competing R/B loops, and 3-scenario framework has no equivalent in the new pipeline. No agent produces actor reactions, competing loop dynamics, or adjusted forecasts.

2. **Stellar Investment Thesis.** The Hype Delta framework, Fragile/Robust/Antifragile classification, trade expression, entry/exit triggers, and position sizing logic have no equivalent. The new pipeline stops at disruption analysis.

3. **Value-Driven Investment Screening.** The 3-gate qualification (technology layer L1-L4, improvement rate, scalability), vulnerability scoring, and basket construction are in the Skills system but not wired into the new pipeline.

4. **Convergence Analysis.** The old STDF sub-agent had an explicit Phase 3 (convergence analysis). The new domain-disruption agent maps convergence in its disruption map, but there is no dedicated convergence agent that models multi-technology interaction dynamics.

5. **Bottleneck Identification.** Tony explicitly identified this as a gap: "convergence, bottlenecks, and feedback loops are essential to the SIBA framework." The new system has no bottleneck detection agent.

6. **Anti-Sycophancy Reformulation.** The old reformulator actively extracted user claims as hypotheses, neutralized leading language, and classified 8 intent types with nuanced routing. The new system has no reformulator -- the orchestrator handles query interpretation directly.

7. **Citation Builder.** The old system had a dedicated agent that created structured citations with provenance pointers (G#/D#/W#/S#/R#). The new pipeline's synthesizer handles citations inline, which is less rigorous.

8. **Trace Explainability.** The old trace-explain agent could reconstruct what the system did and why. The new system relies on agent output files for traceability, but has no dedicated explanation agent.

9. **Meeting Knowledge Graph.** The old main agent had access to `meeting_kg_query` for querying team meeting data. The new pipeline has no meeting integration.

10. **Conversational context.** The old system maintained conversation state across turns (plan lifecycle, prior approved responses). The new pipeline is single-run -- each analysis is independent.

---

## 3. STAKEHOLDER EXPECTATIONS (from Meetings)

### 3.1 SIBA Framework as Non-Negotiable

Tony's most repeated demand across all 4 meetings. The SIBA framework (Second-order Implications, Bottlenecks, Accelerators) must be the starting point for EVERY analysis.

- Mar 11: "It's important to always do the SIBA framework... that's not optional."
- Mar 20: Erupted when UK unemployment analysis used Phillips curve instead of SIBA: "that's mainstream economics. To me, it really adds no value."
- Mar 20: "That is our edge. And if we don't do it, then we're not doing anything."
- Mar 26: SIBA is the foundation for Stellar Sense autonomous agent.

**Implication for migration:** Every query entering the pipeline must be routed through the SIBA lens first. The orchestrator's Phase 1 (domain-disruption) partially addresses this but does not explicitly enforce SIBA routing for queries that might seem to be "mainstream economics" questions (e.g., unemployment forecasting).

### 3.2 "Cost Curves Are Like Gravity"

Tony's core axiom: cost curves will continue until physics or biology stops them. The system must NOT impose cost floors.

- Mar 20: Interrupted the team on battery cost floors: "Wrong wrong. Do not do that, please."
- Mar 20: Moore's Law parable -- everyone said the cost curve would stop; it's still going and accelerating.
- Mar 26: Confirmed for lead model -- no declining recycling rates, no cost floors.

**Implication for migration:** `shared-rules.md` enforces this via "No Clipping" guardrail. But the old system's `tony_core.txt` explanation (the Moore's Law story, the epistemological argument) is not encoded in the new system's rules. The new system says "don't clip" but doesn't explain WHY, which makes agents less likely to internalize the principle.

### 3.3 Framework Must Route EVERY Query Through SIBA First

- Mar 20: An LNG analysis was done without cost curves of solar/wind/battery: "To go off and do an analysis of LNG without doing cost curves of solar wind and battery and so on, doesn't add anything."

**Implication for migration:** The new system's preset logic (ENERGY_FULL, ENERGY_GAS) would handle this specific case. But the general principle -- "always start with disruption economics, even for seemingly non-disruption queries" -- needs to be encoded in the orchestrator.

### 3.4 Convergence Analysis (Not Yet Done -- Identified Gap)

- Mar 20: "We haven't really done convergence... we have as a group threatened to come back to do convergence but we really haven't done it."
- Convergence, bottlenecks, and feedback loops are "essential to the SIBA framework."

**Implication for migration:** The new system's domain-disruption agent maps convergence in its disruption map, and the Stellar Core skill has a `layer2_sectors/convergence/feedback_loops.md` file. But there is no dedicated convergence agent that models how multiple disruptions interact to produce emergent capabilities. This is a critical gap.

### 3.5 Feedback Loops (Essential but Not Explicit)

The old system had a dedicated feedback loop analyzer with 5-actor model. The new system has no equivalent.

Tony considers feedback loops essential to SIBA. The old system could analyze how governments, central banks, consumers, corporations, and markets would react to a disruption -- producing competing accelerator/brake loops and scenario forecasts.

**Implication for migration:** A dedicated feedback loop agent should be added to the new pipeline, either as a Tier 6 conditional agent or as a flex agent that the orchestrator can inject.

### 3.6 Predictive Power Warnings (Robert's Demand)

- Mar 6: "The model should say, 'Hey, just so you know, looking at the last recent data, this model does not appear to have applicability.'"
- Model should flag when disruption IS starting to show up in data.
- Model should self-learn and self-refine.

**Implication for migration:** The new system has no "predictive power warning" mechanism. The evaluator checks compliance with STDF rules but does not assess whether the analysis has predictive applicability based on recent empirical data.

### 3.7 Back-Testing as Mandatory

Both Tony and Robert demand back-testing. Robert discovered zero fit to actual unemployment data (Mar 6). Tony: "if we don't test it on actual data, what are we gonna test it on?"

**Implication for migration:** Neither the old nor the new system has a built-in back-testing framework. This is a feature gap in both systems.

### 3.8 The "Flip" from Chat to 24/7 Autonomous Agent

Mar 26 paradigm shift: "We need to flip Stellar Edge from essentially a chat-based kind of exercise to around the clock, infinite loop kind of software. Basically, we don't prompt the software, it prompts us."

The vision:
- Software works 24/7: learning, gathering data, doing portfolio risk, looking for investment ideas
- Multi-channel alerts: email, WhatsApp, voice
- "If it has a question, then WhatsApp me or Robert"
- Portfolio position tracking with 5-10 metrics per position
- Correlation break detection
- Rupture point detection

**Implication for migration:** The new STDF pipeline is designed as a single-run analysis tool. The autonomous agent layer requires a wrapping scheduler/monitor that continuously runs the pipeline on new signals. The server architecture (`server/`) is the foundation for this, but the autonomous loop, signal detection, and multi-channel notification are not yet built.

### 3.9 Newsletter with Intelligence, Not News

- Mar 11: "News is super abundant and not that interesting anymore." Wants convergence signals, emerging bottlenecks, tipping points, systemic implications, "things not being paid attention to."

**Implication for migration:** The new pipeline could generate newsletter content via QUICK or TIPPING_ONLY presets on a schedule, but the "intelligence layer" (what signals matter, what's being missed) requires the convergence and feedback loop capabilities that are currently missing.

### 3.10 Speed vs. Precision Tradeoff

Tony consistently subordinates speed to precision: "I don't want bad results quickly" (Mar 20). But he also wants real-time answers in meetings with Robert.

**Implication for migration:** The preset system (QUICK at 3 agents vs FULL at 12 agents) addresses this. QUICK can answer in minutes; FULL takes longer but is comprehensive. The key is accurate preset detection from the query.

---

## 4. GAP ANALYSIS -- Old vs New

| Capability | Rating | Assessment |
|---|---|---|
| **SIBA framework enforcement** | NEW BETTER | New system has programmatic enforcement via vocabulary.py, guardrails.py, and hooks. Old system relied on prompt-based compliance. But old system has deeper WHY encoding (tony_core.txt). |
| **Cost curve analysis rigor** | NEW BETTER | New system has lib/cost_curve_math.py with validated exponential_fit, learning_rate_from_decay, competitive_threshold. Old system relied on LLM ad-hoc math. |
| **S-curve fitting (mathematical vs heuristic)** | NEW BETTER | New system has lib/scurve_math.py with fit_scurve, project_scurve, classify_phase, completion_year. Requires R-squared reporting. Old system described S-curve methodology but had no enforced math. |
| **Tipping point synthesis** | NEW BETTER | New system decomposes into 3 separate checker agents + synthesizer. Uses lib/tipping_math.py for check_tipping_conditions, regional_tipping_assessment. Old system checked all 3 conditions in one agent with no formal logic. |
| **Convergence analysis** | OLD BETTER | Old STDF sub-agent had explicit Phase 3 convergence analysis. Old feedback loop analyzer modeled cross-sector interactions. New system's domain-disruption agent maps convergence in a table but has no dedicated convergence modeling. |
| **Feedback loop detection** | OLD BETTER | Old system had a dedicated 6-step feedback loop analyzer with 5-actor model, competing R/B loops, 3-scenario forecasts, and monitoring indicators. New system has NO feedback loop agent. |
| **Bottleneck identification** | NEITHER HAS IT | Tony explicitly identified this as a gap (Mar 20). Neither system has a dedicated bottleneck detection agent. The old feedback loop analyzer partially addressed it through brake loops. |
| **Terminology guardrails** | NEW BETTER | New system: programmatic regex scanning (vocabulary.py) + PreToolUse hook blocking writes + evaluator check + required terms verification. Old system: prompt-based rules that leaked. |
| **Source validation** | NEW BETTER | New system: 3-tier data source hierarchy (Published > Local Catalog > Web), data-type tagging ([observed]/[model-derived]), banned source URL detection, date consistency checks. Old system had an evidence hierarchy but no enforcement. |
| **Data provenance** | NEW BETTER | New system: every data point tagged with [T1: source], [T2: catalog], [T3: url+date]. Citation provenance validation in guardrails.py. Old system had [C#] citations but provenance was generated downstream by citation builder. |
| **Evaluation/quality gates** | NEW BETTER | New system: 6 layers of enforcement (hook, per-agent checklist, vocabulary module, guardrails module, evaluator agent, pipeline validation). Old system: single evaluator pass. |
| **Pipeline orchestration** | NEW BETTER | New system: dynamic DAG resolution, parallel tier execution, conditional chains, research injection, failure matrix with graduated penalties. Old system: keyword-based routing from reformulator. |
| **Error handling / failure modes** | NEW BETTER | New system: CRITICAL/HIGH/MEDIUM failure matrix, pipeline stop on CRITICAL, confidence degradation on HIGH/MEDIUM, structural guarantee (tipping-synthesizer fails if checkers missing). Old system had no formal failure handling. |
| **Tony's philosophy encoding** | OLD BETTER | Old system: tony_core.txt (343 lines) + terminology_guardrails.txt (147 lines) with epistemological reasoning, historical precedents, RethinkX track record, Moore's Law parable, disruption compass. New system encodes the RULES but not the WHY. shared-glossary.md defines terms; shared-rules.md enforces them; but the intellectual foundation (why cost curves are like gravity, why human intuition systematically fails) is absent. |
| **Mainstream economics suppression** | EQUIVALENT | Both systems ban IEA/EIA/BNEF/OPEC. Both enforce "market-driven disruption" over "policy-driven transition." New system adds programmatic enforcement; old system had deeper reasoning. |
| **Regional analysis** | NEW BETTER | New system: dedicated regional-adopter agent with per-region S-curve fits. Tipping-synthesizer requires minimum 3 regional assessments. Old system had no dedicated regional agent. |
| **Cross-sector analysis** | OLD BETTER | Old system: cross-sector feedback loops explicitly modeled (Energy->Transport, Energy->AI, Energy+AI->Food). Old feedback loop analyzer could trace second-order effects. New system: domain-disruption maps convergence but does not model cross-sector dynamics. |
| **Proactive intelligence** | NEITHER HAS IT | Tony's Mar 26 vision of autonomous agent with correlation break detection, rupture point alerts, and portfolio monitoring exists in neither system. Both are query-driven, single-run tools. |
| **Back-testing** | NEITHER HAS IT | Robert's #1 demand. Neither system has a built-in back-testing framework. The old system could run predictions and compare to actuals manually; the new system has no mechanism. |
| **Self-learning capability** | NEW BETTER (partial) | New system has persistent agent memory (agent-memory/ directory) where agents record patterns, conflicts, and calibration insights. Old system had no memory across sessions. But neither system has automated model refinement. |
| **Multi-channel delivery** | NEITHER HAS IT | Tony wants email, WhatsApp, and voice alerts. The server/ directory has WebSocket/HTTP foundations, but multi-channel notification is not built. |

---

## 5. MIGRATION PLAN

### 5.1 Intellectual Property from Old Prompts to Absorb into New shared-rules

The following content from old prompts contains IP that should be migrated into the new system's shared files:

**From `tony_core.txt` -> create `stdf/shared-philosophy.md`:**
- Core Axioms section (Convergence, 10x Factor, Phase Change, Metamorphosis Principle) -- these go beyond glossary definitions and encode the reasoning framework
- System Dynamics section (Boulder Analogy, self-organization, cross-sector feedback loops)
- Historical Precedents table (cars, digital cameras, smartphones, Blockbuster, coal plants) -- critical for calibration
- RethinkX Prediction Track Record (99.2% accuracy on EV cost) -- justifies confident projections
- Disruption Compass (9 Principles of Disruption)
- Levels of Change hierarchy (Organizing System > Sectors > Technology)
- Incumbent Response Pattern (7 stages: Denial -> Collapse)
- "Cost curves are like gravity" epistemological argument with Moore's Law parable

**From `stdf_subagent_system.txt` -> verify coverage in agent definitions:**
- Disruption-model classification rubric (From Below, From Above, Big Bang, Architectural, Systemic) -- already in stdf-domain-disruption.md, verified
- Quantitative method expectations (C(t) formula, convergence threshold timing, rupture window logic) -- partially covered by lib/ functions, but the explicit formulas should be in agent definitions

**From `feedback_loop_subagent_system.txt` -> create new agent (see 5.4):**
- 5-Actor Model with reaction templates
- Timing framework with lag ranges
- Competing loop architecture (R/B with competing_with)
- 3-Scenario adjusted forecast methodology
- Actor Reference Matrix (6 shock types x 5 actors)

**From `stellar_subagent_system.txt` -> consider new agent or integration:**
- Hype Delta framework (HYPE_DELTA = Market-Implied Narrative - Operational Reality)
- Fragile/Robust/Antifragile classification
- Trade expression methodology
- No-trade output protocol

**From `reformulator_system.txt` -> integrate into orchestrator:**
- STDF terminology preservation table (84+ terms) -- already in shared-glossary.md, verified
- Anti-sycophancy protocol (hypothesis extraction, neutral reformulation)
- Intent classification logic (8 types)
- Sector routing rules with chaining patterns

**From `evaluator_system.txt` -> verify coverage in stdf-evaluator.md:**
- Evaluator SEBA method checklist -- largely covered but verify:
  - Lag handling rule (lags excluded unless requested) -- NOT in new evaluator
  - Linear projection detection rule -- covered
  - Market trauma awareness -- covered
  - Chimera recognition -- covered
  - Feedback loop verification -- covered
  - Jevons Paradox verification -- covered
  - Long tail prohibition -- covered
  - Scope assumption fabrication check -- NOT explicitly in new evaluator

### 5.2 What the Old System Does That the New System Should Add

**Priority 1 (CRITICAL -- addresses Tony's #1 demand):**

1. **Feedback Loop Agent** -- Port the old `feedback_loop_subagent_system.txt` into a new `stdf-feedback-loop.md` agent. This is Tony's "feedback loops are essential to SIBA" demand. Design as a Flex agent that can be injected after Tier 4 (tipping-synthesizer) or after Tier 5b, depending on the query. Include: 5-actor model, competing R/B loops, 3-scenario forecasts, monitoring indicators. Add `lib/feedback_math.py` for loop strength calculations and scenario probability normalization.

2. **Convergence Agent** -- Create `stdf-convergence.md` to explicitly model multi-technology interaction dynamics beyond simple mapping. This should trace cross-sector feedback loops (Energy->Transport, Energy->AI, Energy+AI->Food) and model emergent capabilities. Design as a Tier 5c agent (parallel with regional-adopter and xcurve-analyst) that reads tipping-synthesizer, domain-disruption, and scurve-fitter outputs.

3. **Bottleneck Detection Agent** -- Create `stdf-bottleneck.md` to identify supply chain, infrastructure, and resource constraints that could delay disruption timelines. Tony identified bottleneck analysis as essential but missing. Design as a Flex agent (like research) that can be injected when upstream agents flag potential bottlenecks.

**Priority 2 (HIGH -- addresses investment use case):**

4. **Investment Translation Layer** -- The old STDF->Stellar->Value Investment chain has no equivalent. Either port the Stellar sub-agent's Hype Delta framework into a new `stdf-investment-thesis.md` or wire the value-driven-investment skill from the Skills system into the pipeline.

5. **Anti-Sycophancy Reformulator** -- The new pipeline has no query reformulation step. While the orchestrator handles interpretation, it does not actively neutralize user framing, extract hypotheses, or rewrite leading questions. Either encode anti-sycophancy rules in the orchestrator or create a lightweight reformulator step.

6. **Predictive Power Warning** -- Implement Robert's "wealth warning" mechanism. After evaluation, a check should compare model predictions against recent actual data (if available in the data catalog) and flag when predictions have diverged significantly.

**Priority 3 (MEDIUM -- improves quality):**

7. **Philosophy Document** -- Create `stdf/shared-philosophy.md` containing the intellectual foundation from `tony_core.txt`: why cost curves are like gravity, the Moore's Law parable, historical precedents, RethinkX track record, 9 Principles of Disruption. Agents should read this for context, not just rules.

8. **Citation Rigor** -- The old citation builder was a dedicated agent. The new synthesizer handles citations inline. Consider adding a post-synthesis citation verification step (could be part of the evaluator).

9. **Meeting Intelligence Integration** -- Tony wants meeting transcripts processed and derived insights ingested. Add a data source in the pipeline for meeting context.

### 5.3 What the New System Already Does Better (No Migration Needed)

- Programmatic vocabulary enforcement (vocabulary.py + hooks)
- File-based inter-agent communication
- DAG-based orchestration with parallel tiers
- Validated computation libraries (15 lib modules)
- 956 curated empirical data curves
- Per-agent compliance checklists with severity levels
- Multi-layer quality gates (6 levels)
- Conditional pipeline configurations (8 presets)
- Failure matrix with graduated penalties
- Persistent agent memory
- Decomposed tipping point analysis (3 checkers + synthesizer)
- Regional analysis (dedicated regional-adopter agent)
- Energy dispatch modeling (merit order, displacement schedule)
- Commodity demand decomposition (4-agent chain)

### 5.4 Specific Recommendations for Improving CLAUDE.md, shared-rules.md, Agent Definitions

**CLAUDE.md improvements:**
1. Add a "SIBA First" rule in Orchestration Principles: "When any query arrives that could be analyzed through mainstream economics (GDP, unemployment, inflation, Phillips curve), the orchestrator MUST route through the SIBA lens first. Mainstream economics may provide secondary context for understanding policymaker reactions, but SIBA disruption dynamics always take priority."
2. Add explicit convergence detection in Phase 1a: "If the query involves multiple sectors or technologies that interact, add the convergence agent to the goal set."
3. Add a "Philosophy Reference" section pointing to shared-philosophy.md for agents that need to understand WHY the rules exist, not just WHAT they are.

**shared-rules.md improvements:**
1. Add a "Cost Curve Gravity" section explaining WHY no cost floors are permitted -- include the Moore's Law parable and epistemological argument from tony_core.txt. Rules without reasoning are brittle.
2. Add "Lag Exclusion Protocol" from old evaluator: "Do NOT include regulatory, policy, or adoption lag analysis in the main response. State explicitly: 'Analysis reflects cost-curve dynamics; regulatory/adoption lags excluded unless specifically requested.'"
3. Add "Scope Assumption Fabrication Check": agents must not present numbers as "stated assumptions" if they don't appear in upstream data.

**Agent definition improvements:**
1. `stdf-domain-disruption.md`: Add explicit SIBA routing check -- if the query could be analyzed through mainstream economics, the agent must identify the disruption-theoretic framing FIRST and note that mainstream analysis is secondary context.
2. `stdf-synthesizer.md`: Add consistency audit for all entities described as "benefiting" or "growing" -- cross-check against X-curve analyst output. (Already present but should be made a CRITICAL check.)
3. `stdf-evaluator.md`: Add "Lag Handling" check and "Scope Assumption Fabrication" check from old evaluator.

### 5.5 New Agents to Create

1. **stdf-feedback-loop** (Flex agent)
   - Purpose: Model system reactions to disruptions using 5-actor framework and competing feedback loops
   - Reads: domain-disruption, tipping-synthesizer, and optionally cost-fitter/scurve-fitter
   - Produces: Actor reactions, R/B loops, 3-scenario forecast, monitoring indicators
   - Library: `lib/feedback_math.py` (new)
   - Criticality: HIGH

2. **stdf-convergence** (Tier 5c, parallel with regional-adopter)
   - Purpose: Model multi-technology interaction dynamics and emergent capabilities
   - Reads: domain-disruption (convergence map), tipping-synthesizer, scurve-fitter
   - Produces: Cross-sector feedback loop analysis, convergence acceleration estimates, emergent capability assessment
   - Library: `lib/convergence_math.py` (new)
   - Criticality: HIGH

3. **stdf-bottleneck** (Flex agent, like research)
   - Purpose: Identify supply chain, infrastructure, and resource constraints
   - Reads: domain-disruption, cost-researcher, capability, and optionally demand-decomposer
   - Produces: Bottleneck inventory with severity, timeline, and mitigation pathways
   - Library: None needed (uses WebSearch and data catalog)
   - Criticality: MEDIUM

### 5.6 Architecture Recommendations for 24/7 Autonomous Agent Layer

Tony's Mar 26 vision requires a wrapping layer around the STDF pipeline:

**1. Signal Detection Layer (Stellar Sense)**
- Scheduled data refresh checks against 956 curves in data/
- Correlation monitoring across tracked asset pairs
- Rupture point proximity detection (is any market approaching 5-10% penetration?)
- Cost parity threshold monitoring (has any disruptor crossed parity in a new region?)

**2. Portfolio Monitor**
- Per-position metric tracking (5-10 metrics per position)
- Daily/hourly data collection from Bloomberg and other premium sources
- Pattern detection against SIBA hypotheses
- Alert generation when monitored metrics cross thresholds

**3. Autonomous Analysis Loop**
- When a signal is detected, automatically run the appropriate pipeline preset:
  - Cost parity crossed -> TIPPING_ONLY preset for the affected sector
  - Correlation break -> CUSTOM preset with domain-disruption + research
  - Rupture point proximity -> FULL preset
- Store results in persistent output directory
- Generate alerts from synthesizer conclusions

**4. Multi-Channel Notification**
- Email digest (configurable frequency: daily, weekly, on-signal)
- WhatsApp integration for urgent alerts (rupture points, correlation breaks)
- Voice synthesis for audio briefings
- In-app dashboard for continuous monitoring

**5. Human-in-the-Loop**
- System can ask humans questions via notification channels
- Responses feed back into the analysis loop
- Alert triage: Critical (immediate notification), High (next digest), Medium (weekly report)

### 5.7 Effort Estimate

| Item | Effort | Priority |
|------|--------|----------|
| Create shared-philosophy.md (port tony_core.txt IP) | 1 day | P1 |
| Create stdf-feedback-loop agent + lib/feedback_math.py | 3-4 days | P1 |
| Create stdf-convergence agent + lib/convergence_math.py | 2-3 days | P1 |
| Create stdf-bottleneck agent | 1-2 days | P2 |
| Update shared-rules.md (gravity section, lag protocol, scope fabrication check) | 0.5 days | P1 |
| Update CLAUDE.md (SIBA-first rule, convergence detection, philosophy reference) | 0.5 days | P1 |
| Update stdf-evaluator (lag handling, scope fabrication checks) | 0.5 days | P2 |
| Anti-sycophancy reformulation (integrate into orchestrator or create agent) | 1-2 days | P2 |
| Investment translation layer (port Hype Delta or wire value-driven-investment) | 2-3 days | P2 |
| Predictive power warning mechanism | 1-2 days | P2 |
| Signal detection layer (Stellar Sense foundation) | 5-7 days | P3 |
| Portfolio monitor module | 3-5 days | P3 |
| Autonomous analysis loop | 3-5 days | P3 |
| Multi-channel notification system | 3-5 days | P3 |

**Total P1 (Critical):** ~8-10 days
**Total P2 (High):** ~5-8 days
**Total P3 (24/7 Autonomous Agent):** ~14-22 days

**Grand total:** ~27-40 days

---

## Summary

The new STDF v2 pipeline is architecturally superior to the old system in nearly every engineering dimension: file-based communication, programmatic enforcement, validated computation, DAG orchestration, and multi-layer quality gates. However, the old system contains irreplaceable intellectual property -- particularly the feedback loop analyzer, the investment thesis layer, Tony's philosophical encoding, and the anti-sycophancy reformulator -- that must be ported to maintain analytical completeness.

The most critical gaps relative to stakeholder expectations are:
1. **Feedback loops** (Tony: "essential to SIBA" -- no agent exists)
2. **Convergence modeling** (Tony: "we really haven't done it" -- mapping exists but not modeling)
3. **Bottleneck detection** (Tony: "essential to SIBA" -- neither system has it)
4. **Tony's philosophy encoding** (rules exist but the WHY is absent)
5. **Proactive intelligence** (the "flip" from chat to 24/7 agent is the vision, not yet architecture)

The P1 migration items (shared-philosophy.md, feedback loop agent, convergence agent, shared-rules updates) should be completed before any production deployment of the new pipeline. The P3 items (autonomous agent layer) represent the product roadmap for the next 1-2 months.
