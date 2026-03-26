# STDF v2 Agent Pipeline — Eval Gap Analysis

**Generated:** 2026-03-20
**Source:** `evals_from_chat_exports.md` (202 sessions: Tony ~42, Robert ~160)
**Cross-referenced against:** 16 agents, 5 skills, 14 lib modules, 956 empirical curves

---

## How to Read This Document

Each eval entry contains:
- **Chat Question** — the original user query
- **Topic / Issues** — what went wrong or what was being tested
- **Expected Behavior** — what the system should do
- **Current STDF Agent Coverage** — what the v2 pipeline handles today
- **Gaps & Recommendations** — what's missing and how to close the gap

---

## Table of Contents

1. [P0 — Fabricating Data](#p0-fabricating-data)
2. [P0 — Framework Compliance (Seba Framework)](#p0-framework-compliance)
3. [P0 — Opinion vs Process-Driven Analysis](#p0-opinion-vs-process)
4. [P1 — Terminology Precision](#p1-terminology-precision)
5. [P1 — No Scenario Ranges](#p1-no-scenario-ranges)
6. [P1 — Internal Consistency](#p1-internal-consistency)
7. [P1 — Correct Baselines](#p1-correct-baselines)
8. [P2 — Excessive Clarification](#p2-excessive-clarification)
9. [P2 — Internal Data First](#p2-internal-data-first)
10. [P2 — Wrong Financial Terminology](#p2-wrong-financial-terminology)
11. [P3 — Web Data Access](#p3-web-data-access)
12. [P3 — Multi-Session Consistency](#p3-multi-session-consistency)
13. [Query-Type Coverage Gap Analysis](#query-type-coverage)
14. [Agent-Level Gap Summary](#agent-level-gaps)
15. [Recommended New Agents / Capabilities](#new-capabilities)

---

## P0 — Fabricating Data {#p0-fabricating-data}

**Priority:** P0 (8+ incidents, destroys trust)
**Key Quote:** "Stop making stuff up" / "Never make up stuff"

### Eval T-23: GLP-1 Half-Life Theoretical Limits

| Field | Detail |
|-------|--------|
| **Chat Question** | "Are we seeing a disruption in GLP-1?" |
| **Topic / Issues** | System fabricated molecular half-life theoretical limits. User said: "you're making up the theoretical limit of half-life", "Stop making stuff up", "If you don't know, then ask me." |
| **Expected Behavior** | Never fabricate scientific data. If data unavailable, state gap explicitly and ask user for input. |
| **Current STDF Coverage** | `shared-rules.md` Rule 1: "Never Estimate by Hand — ALL numerical computation MUST use Bash with python3." Data Source Hierarchy enforces Tier 1 > Tier 2 > Tier 3 sourcing. `lib.guardrails.validate_citation_provenance()` checks for empty source columns. Vocabulary hook blocks banned terms at write time. |
| **Gaps** | **No pharmaceutical/biotech data in the 956-curve catalog.** The data catalog covers energy, transport, compute, materials — zero GLP-1/pharma curves. No agent is specialized for pharma disruption analysis. The guardrail system catches *vocabulary* violations but cannot detect *fabricated numerical claims* — there's no provenance validator that flags numbers without source tags. |
| **Recommendations** | (1) Add a **fabrication detection guardrail** in `lib/guardrails.py`: scan for numerical claims (percentages, dollar amounts, physical constants) that lack `[observed]` or `[model-derived]` tags. (2) Expand `data/` catalog to include pharma cost/adoption curves (GLP-1 pricing, patent cliffs, biosimilar adoption). (3) Add explicit "I don't have data for this" behavior to `shared-rules.md` — agents must state data gaps rather than fill them with plausible-sounding numbers. |

### Eval T-28: AI Compute Growth Rates

| Field | Detail |
|-------|--------|
| **Chat Question** | "What is the growth rate of AI data center compute?" |
| **Topic / Issues** | System fabricated cost-per-token projections and learning rate parameters. User: "you're making up a lot of stuff", "the cost per token projections seem to be made up", "Never make up stuff." |
| **Expected Behavior** | Use only observed data. Cost curve parameters must be derived from actual data via `lib.cost_curve_math.exponential_fit()`, never assumed. |
| **Current STDF Coverage** | `stdf-cost-fitter` is computation-only (no web access), derives learning rates exclusively from upstream `02a-cost-researcher.md` data. `stdf-cost-researcher` has minimum 3 data points over 5+ years gate (criterion 2.1 — CRITICAL). `lib.cost_curve_math.exponential_fit()` requires min 3 actual data points. |
| **Gaps** | **AI compute/inference cost data is sparse in the catalog.** The `data/` catalog has energy and transport cost curves but limited AI inference cost data. If the cost-researcher can't find 3+ data points, criterion 2.1 fails — but this is a *hard stop*, not a graceful degradation. Users expect analysis even with limited data. The pipeline has no mechanism for "best-effort with explicit uncertainty" when data is thin. |
| **Recommendations** | (1) Add AI compute cost curves to `data/` catalog: GPU $/FLOP, inference $/token (by model tier), training $/parameter. (2) Add a **thin-data mode** to cost-fitter: when data points are 2-3, fit with explicit wide confidence intervals and flag as LOW_CONFIDENCE rather than hard-failing. (3) Add `lib.cost_curve_math` function for token-cost learning rates specifically. |

### Eval T-25: Lead Supply-Demand Fabrication

| Field | Detail |
|-------|--------|
| **Chat Question** | "When will demand for lead drop by 10% relative to today?" |
| **Topic / Issues** | System fabricated historical figures. User: "I don't believe you", "This is all wrong", "You're making stuff up." Also missed the 12V starter battery disruption vector entirely. |
| **Expected Behavior** | Use only sourced data. Include ALL disruption vectors — especially obvious ones like 12V starter battery displacement by LFP. |
| **Current STDF Coverage** | `stdf-domain-disruption` is designed to map ALL disruption vectors for a sector. `stdf-cost-researcher` sources from catalog + web. Commodity chain (demand-decomposer → stream-forecaster) decomposes demand into market products. |
| **Gaps** | **No completeness check for disruption vectors.** The domain-disruption agent identifies disruption vectors but has no mechanism to validate it hasn't missed an obvious one. Lead-acid battery data may be thin in the catalog. The demand-decomposer validates 80% coverage of total demand but doesn't validate that all *disruption pathways* are captured. |
| **Recommendations** | (1) Add a **disruption vector completeness heuristic** to `stdf-domain-disruption`: for commodity analyses, cross-reference the commodity's end-use breakdown (from web/catalog) against identified disruption vectors — flag if any end-use >10% of demand lacks a disruption assessment. (2) Add lead-acid, 12V automotive battery, and industrial lead demand data to catalog. (3) Add a self-check prompt in domain-disruption: "Have I covered the largest end-use segment for this commodity?" |

### Eval T-38: BEV Cost Decline Rates

| Field | Detail |
|-------|--------|
| **Chat Question** | "When will BEV trucks disrupt natural gas trucks in China?" |
| **Topic / Issues** | BEV costs "can't possibly be declining 5.5% annually" — fabricated decline rate. User: "a lot of your arguments are made up, totally linear or extractive", "Just use the Seba Framework and just use our data factory data." |
| **Expected Behavior** | Derive cost decline rates from actual data using `exponential_fit()`. Never assume decline rates. |
| **Current STDF Coverage** | `stdf-cost-fitter` enforces: "No assumed ~20% learning rates." All computation via `lib.cost_curve_math` with python3. Criterion 2.3 requires empirically derived learning rate, not assumed. |
| **Gaps** | **China-specific BEV truck cost data may be missing from catalog.** The enforcement is strong at the agent level but depends on the cost-researcher finding the right data. If the catalog lacks China BEV truck data, the cost-researcher falls back to web search, where quality is harder to control. No mechanism to flag when a derived learning rate seems implausible vs. historical norms for the technology class. |
| **Recommendations** | (1) Add China BEV truck cost data to catalog. (2) Add a **learning rate plausibility check** to `lib.cost_curve_math`: flag if derived learning rate is outside historical bounds for the technology class (e.g., batteries typically 15-25%, solar 20-28%). (3) Add BEV truck-specific conversion functions ($/ton-km) to `lib.cost_curve_math`. |

---

## P0 — Framework Compliance (Seba Framework) {#p0-framework-compliance}

**Priority:** P0 (5+ incidents, wrong methodology = wrong answers)
**Key Quote:** "Use the Seba Framework not garbage mainstream projections"

### Eval T-26: Lead Supply-Demand (Seba Framework)

| Field | Detail |
|-------|--------|
| **Chat Question** | "When will lead supply exceed lead demand by more than 10% globally?" |
| **Topic / Issues** | System used IEA/mainstream projections instead of Seba Framework. User: "This is garbage.", "You need to use the Seba Framework not garbage mainstream projections.", "Don't give me three garbage scenarios.", "I shouldn't have to tell you this every time." |
| **Expected Behavior** | ALWAYS use Seba Framework S-curves for disruption analysis. Never cite IEA/EIA/BNEF/OPEC forecasts. |
| **Current STDF Coverage** | **Strong coverage.** `shared-rules.md` bans IEA/EIA/BNEF/OPEC citations. `lib.guardrails.validate_banned_vocabulary()` enforces at runtime. `lib.vocabulary.BANNED_TERMS` includes these organizations. PreToolUse hooks hard-block banned sources at write time. The entire pipeline is structurally designed around S-curves: `stdf-scurve-fitter` uses `lib.scurve_math.fit_scurve()`, never linear extrapolation. Criterion 4.1 makes linear extrapolation an instant non-compliance. |
| **Gaps** | **The banned-source enforcement is incomplete.** `lib/vocabulary.py` currently has `BANNED_SOURCE_PATTERNS = []` (empty list). The shared-rules say to ban IEA/EIA/BNEF/OPEC, but the code doesn't enforce it. The guardrail catches the *term* "IEA" in banned vocab but doesn't catch IEA *URLs* or citation patterns like "(IEA, 2025)". |
| **Recommendations** | (1) **Populate `BANNED_SOURCE_PATTERNS`** in `lib/vocabulary.py` with: `iea.org`, `eia.gov`, `bnef.com`, `opec.org`, and citation patterns like `(IEA,`, `(EIA,`, `(BNEF,`, `(OPEC,`. (2) Add a compliance criterion specifically for source provenance: "No Tier 3 web data from banned organizations." |

### Eval T-03: Unemployment Modeling (S-Curves)

| Field | Detail |
|-------|--------|
| **Chat Question** | "When will artificial labor increase US unemployment to 6%?" |
| **Topic / Issues** | Used linear extrapolation instead of S-curves. Used yearly instead of monthly granularity. Provided base/bull/bear scenarios. |
| **Expected Behavior** | S-curve per sector. Monthly granularity. Single best estimate. Cognitive + digitizable tasks only. |
| **Current STDF Coverage** | `stdf-scurve-fitter` fits logistic S-curves with `lib.scurve_math`. `project_scurve()` supports arbitrary time horizons. `classify_phase()` maps current adoption position. |
| **Gaps** | **No labor/unemployment-specific agent.** The pipeline models technology adoption (market share of disruptor vs. incumbent technology), not labor market displacement. There's no mechanism to convert technology adoption S-curves into sector-by-sector unemployment impacts. No monthly granularity support — `project_scurve()` works at annual resolution. No cognitive/digitizable task filter exists anywhere. |
| **Recommendations** | (1) **New agent: `stdf-labor-impact`** — converts technology adoption S-curves to labor displacement estimates by sector, with cognitive/digitizable task filtering. (2) Add monthly resolution to `lib.scurve_math.project_scurve()`. (3) Add a labor market data category to `data/` catalog: sector employment counts, task digitizability scores, automation exposure indices. (4) Add `lib/labor_math.py` with functions: `displacement_from_adoption()`, `sector_unemployment_projection()`, `task_filter(cognitive=True, digitizable=True)`. |

### Eval R-12: AI Productivity (Challenge Goldman)

| Field | Detail |
|-------|--------|
| **Chat Question** | "How should I think about the impact on productivity of AI? Run a disruption process." |
| **Topic / Issues** | User asked: "Goldman have productivity going from 2% to 4% growth. What are they missing?" System should use disruption framework to challenge mainstream consensus. |
| **Expected Behavior** | Run full disruption process with cost curves. Identify what consensus gets wrong by applying S-curve dynamics. Lead with quantitative evidence, not narrative. |
| **Current STDF Coverage** | The full pipeline produces cost curves, capability analysis, tipping points, and S-curves. The synthesizer produces a 7-phase narrative. `shared-rules.md` enforces "NO narrative without numbers." |
| **Gaps** | **No "consensus challenge" capability.** The pipeline analyzes a disruption in isolation — it doesn't compare its output against mainstream consensus forecasts to highlight divergences. No mechanism to say "Goldman assumes X, but our S-curve shows Y, the delta is Z." The productivity-specific framing (GDP growth from AI) isn't a natural output of the disruption pipeline, which focuses on market share of disruptor vs. incumbent. |
| **Recommendations** | (1) Add a **consensus comparison section** to `stdf-synthesizer`: optionally include mainstream consensus numbers (sourced from the query) and quantify the divergence. (2) Add productivity multiplier modeling to the labor impact agent (recommendation above). (3) The synthesizer should have a "Non-Consensus Insights" section in its Phase 7 output. |

---

## P0 — Opinion vs Process-Driven Analysis {#p0-opinion-vs-process}

**Priority:** P0 (5+ incidents, undermines credibility)
**Key Quote:** "always always run the process and avoid opinion"

### Eval R-42: Nuclear Long Recommendation Error

| Field | Detail |
|-------|--------|
| **Chat Question** | "Which things are most surprising to conventional opinion?" |
| **Topic / Issues** | System recommended going long nuclear while its own analysis showed battery disruption making nuclear uncompetitive. User: "Why would you be long nuclear with battery install into grid systems starting to be significant?" |
| **Expected Behavior** | Investment recommendations must be consistent with the system's own disruption framework output. |
| **Current STDF Coverage** | `stdf-synthesizer` traces every claim to upstream agent output. Criterion 6.2: "Every claim traceable to a specific subagent output file." `shared-rules.md`: "NO narrative without numbers." |
| **Gaps** | **No internal consistency checker.** The synthesizer merges outputs but doesn't validate that conclusions are consistent with each other. If the cost analysis shows batteries disrupting gas peakers, and the domain analysis identifies nuclear as a convergence victim, the synthesizer should NOT recommend nuclear — but there's no automated cross-check. Investment recommendation is outside pipeline scope entirely. |
| **Recommendations** | (1) Add a **consistency validation step** to `stdf-synthesizer`: before writing Phase 7, cross-check that all conclusions align with cost parity and tipping point findings. (2) Add `lib/consistency_math.py` with `check_recommendation_alignment(disruption_map, cost_parity, recommendations)`. (3) If the system generates investment implications, they MUST pass through the disruption framework filter: "Is this position consistent with the cost curves and tipping analysis?" |

### Eval R-20: Oil & Gas → Russia Financial Impact

| Field | Detail |
|-------|--------|
| **Chat Question** | "Using the disruption process for oil and gas, run a full analysis... Then look at financial consequences for Russia." |
| **Topic / Issues** | Some conclusions marked "wrong" — opinion mixed with process. |
| **Expected Behavior** | Run disruption process first (cost curves, S-curves), then derive geopolitical/financial consequences from quantitative findings. |
| **Current STDF Coverage** | Pipeline produces cost curves, tipping points, and S-curves. `stdf-xcurve-analyst` models incumbent decline and market trauma mechanisms (fixed-cost spread, investment drought, talent flight, panic pricing, policy lobbying). |
| **Gaps** | **No geopolitical/financial cascading agent.** The X-curve analyst models market trauma for the incumbent *technology* (e.g., coal plants) but not for *nation-states* whose economies depend on that technology. Russia-as-petro-state is a second-order effect not captured by any agent. No sovereign fiscal analysis capability. |
| **Recommendations** | (1) **New agent: `stdf-macro-impact`** — takes X-curve decline data and maps it to sovereign/macroeconomic impacts for countries with high incumbent exposure (Russia/oil, Australia/coal, Saudi/oil, etc.). (2) Add country-level fossil fuel dependency data to catalog (% GDP, % exports, % fiscal revenue from fossil fuels). (3) This agent would own the "financial consequences for Country X" query pattern. |

---

## P1 — Terminology Precision {#p1-terminology-precision}

**Priority:** P1 (10+ incidents)
**Key Quote:** "Cost is not price" / "No Jevons for AL"

### Eval T-21: Cost vs Price (GLP-1)

| Field | Detail |
|-------|--------|
| **Chat Question** | "Tell me about GLP-1 / What are the capability curves that drive GLP-1 adoption?" |
| **Topic / Issues** | System conflated cost and price. User: "Cost is not price." |
| **Expected Behavior** | Always distinguish manufacturing cost from market price. Use "cost" for production economics, "price" for what buyers pay. |
| **Current STDF Coverage** | `shared-rules.md` defines banned vocabulary and required vocabulary. `lib/vocabulary.py` has 10 banned terms and 6 required terms. |
| **Gaps** | **Cost/price distinction is not in the vocabulary rules.** The banned terms list handles "transition" → "disruption" etc., but doesn't enforce cost vs. price precision. This is a semantic distinction that regex-based guardrails can't easily catch. |
| **Recommendations** | (1) Add "cost vs price" guidance to `shared-rules.md` under a new "Semantic Precision" section. (2) Add a **context-aware term check** in `lib/guardrails.py`: flag instances where "price" appears in a cost-curve analysis context (near "learning rate", "$/kWh", "curve"). (3) Add to agent prompts: "Distinguish manufacturing cost (production economics) from market price (what buyers pay). Never conflate." |

### Eval T-31: Jevons Paradox for AL Technologies

| Field | Detail |
|-------|--------|
| **Chat Question** | "What is the cheapest cost per inference token today?" |
| **Topic / Issues** | System invoked Jevons Paradox for AI/Artificial Labor. User: "There's no Jevons Paradox in digital markets. Jevons paradox applies to X-Flow not Stellar technologies.", "Stop using Jevons paradox for AL." |
| **Expected Behavior** | Jevons Paradox applies ONLY to X-Flow technologies (physical resource throughput), NEVER to Stellar/AL technologies (digital, zero marginal cost). |
| **Current STDF Coverage** | Not covered. "Jevons Paradox" is not in the banned vocabulary list. No rule distinguishes X-Flow vs. Stellar technology behavior. |
| **Gaps** | **No X-Flow vs. Stellar classification system.** This is a core STDF concept: technologies behave differently based on whether they involve physical resource flows (X-Flow: oil, gas, coal) vs. information/digital flows (Stellar: solar, AI, software). The pipeline has no mechanism to classify a technology and apply different analytical rules accordingly. |
| **Recommendations** | (1) **Add "Jevons Paradox" to banned vocabulary** with replacement: "demand elasticity (X-Flow only)" or similar — or add a conditional rule: banned when used with Stellar/AL technologies. (2) Add X-Flow vs. Stellar classification to `stdf-domain-disruption` output. (3) Add to `shared-rules.md`: "Jevons Paradox is valid ONLY for X-Flow (physical resource) technologies. Never apply to Stellar (solar, wind, battery) or AL (artificial labor, AI) technologies." (4) Add `lib/vocabulary.py` context-sensitive rule for Jevons. |

### Eval T-24: Terminology Corrections (Copper)

| Field | Detail |
|-------|--------|
| **Chat Question** | "What are the demand drivers for copper?" |
| **Topic / Issues** | System used "green copper" (should be "EV + SWB Copper"), "total green" (imprecise), T&D demand growth underestimated. |
| **Expected Behavior** | Use precise STDF labels: "EV + SWB Copper" not "green copper". Include T&D in system totals. |
| **Current STDF Coverage** | `lib/vocabulary.py` bans "green" as a standalone term. `shared-rules.md` bans "green" and "clean energy." |
| **Gaps** | **Compound terms like "green copper" may slip through.** The banned term "green" is matched as a whole word — "green copper" might be caught, but the replacement guidance doesn't specify "EV + SWB Copper" as the correct label. Domain-specific terminology corrections aren't in the vocabulary system. |
| **Recommendations** | (1) Add domain-specific term mappings to `lib/vocabulary.py`: "green copper" → "EV + SWB copper", "green hydrogen" → specify production method. (2) Add a **domain terminology reference** section to agent prompts for commodity analyses. (3) Ensure T&D is always included in energy system analyses — add to domain-disruption agent's completeness heuristic. |

### Eval T-18: Wright's Law / God Parity

| Field | Detail |
|-------|--------|
| **Chat Question** | "Download solar cost curve... explain God Parity, calculate COE" |
| **Topic / Issues** | System used "Wright's Law" (banned). Misunderstood God Parity concept. User: "Please don't say 'Wright's Law'", "Do you really understand what God parity is?" |
| **Expected Behavior** | Use "cost-curve dynamics" or "learning rate" instead of "Wright's Law". Correctly define God Parity. |
| **Current STDF Coverage** | **"Wright's Law" IS banned** in `lib/vocabulary.py` with replacement "cost-curve dynamics." This would be caught and blocked by PreToolUse hooks. |
| **Gaps** | **God Parity concept not defined anywhere in the system.** God Parity (when rooftop solar < T&D costs alone, making centralized utilities structurally uncompetitive) is a core STDF concept with no definition in shared-rules, vocabulary, or any agent prompt. Agents may misdefine it. |
| **Recommendations** | (1) Add **STDF glossary** to `shared-rules.md` or a new `glossary.md` file defining key concepts: God Parity, Seba Framework, X-Flow, Stellar, SWB, convergence, etc. (2) The domain-disruption and capability agents should reference this glossary. (3) Add God Parity threshold computation to `lib/cost_curve_math.py`: `god_parity_check(rooftop_solar_lcoe, td_cost_per_kwh)`. |

### Eval T-32: AI Capability Improvement (not Growth)

| Field | Detail |
|-------|--------|
| **Chat Question** | "How many digital workers could be deployed today?" |
| **Topic / Issues** | System used "AI Capability Growth" instead of "AI Capability Improvement". Misunderstood "digital worker" concept. User: "It's 'AI Capability Improvement' not 'AI Capability Growth'." |
| **Expected Behavior** | Use precise terminology. "Digital worker" = token supply equivalent (Epoch AI concept), not displacement. |
| **Current STDF Coverage** | Not covered in vocabulary. No "growth" → "improvement" mapping exists. |
| **Gaps** | **AI/AL-specific terminology not in vocabulary rules.** The vocabulary system covers energy/disruption terms but not AI/labor terminology. |
| **Recommendations** | (1) Add to `lib/vocabulary.py` or `shared-rules.md`: "AI Capability Improvement" (not "Growth"), "Artificial Labor" (not "AI replacing workers"), "digital worker" = token supply equivalent. (2) Add these as context-sensitive rules rather than blanket bans (since "growth" is valid in other contexts). |

---

## P1 — No Scenario Ranges {#p1-no-scenario-ranges}

**Priority:** P1 (3+ incidents)
**Key Quote:** "Please do not ever do 'base case', 'optimistic' and 'pessimistic' timing scenarios. Ever."

### Eval T-03 / T-26: Scenario Ranges

| Field | Detail |
|-------|--------|
| **Chat Question** | Multiple — unemployment forecasts, lead demand forecasts |
| **Topic / Issues** | System provided base/optimistic/pessimistic scenarios. User explicitly prohibited this. |
| **Expected Behavior** | Single best estimate. Sensitivity analysis ONLY if requested. No base/bull/bear. |
| **Current STDF Coverage** | `stdf-scurve-fitter` produces a single S-curve with confidence intervals (k ± 15%), which is sensitivity analysis, not scenarios. `stdf-tipping-synthesizer` produces a single tipping year. |
| **Gaps** | **No explicit anti-scenario guardrail.** The agents structurally produce single estimates (good), but there's no vocabulary or guardrail rule that catches "base case", "optimistic scenario", "pessimistic scenario", "bull case", "bear case" in output text. An agent could write narrative using these terms. |
| **Recommendations** | (1) Add **anti-scenario terms** to `lib/vocabulary.py` or `lib/guardrails.py` anti-patterns: "base case", "bull case", "bear case", "optimistic scenario", "pessimistic scenario", "best case", "worst case". (2) Add to `shared-rules.md`: "NEVER provide base/optimistic/pessimistic scenarios. Provide single best estimate with confidence intervals. Sensitivity analysis only if explicitly requested." (3) Add to `lib.guardrails.validate_anti_patterns()`. |

---

## P1 — Internal Consistency {#p1-internal-consistency}

**Priority:** P1 (3+ incidents)
**Key Quote:** "long nuclear" while showing battery disruption

### Eval R-42: Nuclear vs Battery Contradiction

(Covered in P0 — Opinion vs Process section above)

### Eval T-05 vs T-06: Same Question, Different Answers

| Field | Detail |
|-------|--------|
| **Chat Question** | "What will unemployment be in the USA by June 2027?" (asked twice, same day) |
| **Topic / Issues** | Got 19.5% in one session and 8.3% in another for the same question. |
| **Expected Behavior** | Consistent answers for the same query with the same input assumptions. If assumptions differ, explicitly state which changed. |
| **Current STDF Coverage** | Pipeline is deterministic given the same data inputs. Each run produces a new output directory. No mechanism to compare across runs. |
| **Gaps** | **No cross-run consistency validation.** Each pipeline run is independent. If the same query produces different results, there's no mechanism to detect or explain the divergence. No run comparison tool. |
| **Recommendations** | (1) Add a **run comparison skill** (`/stdf-compare`): given two output directories, compare key metrics (tipping year, S-curve parameters, confidence scores) and flag divergences > threshold. (2) Store key parameters in a structured format (JSON sidecar to each output) to enable programmatic comparison. (3) Add `lib/consistency.py` with `compare_runs(dir1, dir2)` → divergence report. |

---

## P1 — Correct Baselines {#p1-correct-baselines}

**Priority:** P1 (3+ incidents)
**Key Quote:** "You can't change the past. You can't change 2025. Start in Feb 2026."

### Eval T-08: Baseline Date Handling

| Field | Detail |
|-------|--------|
| **Chat Question** | "What will USA unemployment be by December 2028 based on the AL disruption?" |
| **Topic / Issues** | System tried to modify historical data. User: "You can't change the past. You can't change 2025. Start in Feb 2026." |
| **Expected Behavior** | Use current date as baseline. Historical data is immutable. Projections start from today. |
| **Current STDF Coverage** | **Strong coverage.** `shared-rules.md` Date Awareness section: "Data BEFORE analysis date = historical (observed, citable). Data AFTER analysis date = projected/forecast (NOT citable)." `lib.guardrails.validate_date_consistency()` flags future-dated years near `[observed]` tags. Every agent prompt includes analysis date (YYYY-MM-DD). |
| **Gaps** | **Baseline value validation is missing.** The date awareness rules handle temporal direction (past vs. future) but don't validate that the *starting values* are correct. If an agent uses "4.2% unemployment" as the baseline but the actual current rate is 5.4%, there's no check. |
| **Recommendations** | (1) Add a **baseline validation step** to agents that project from current values: verify the starting value against a known source (web fetch or catalog) before projecting. (2) Add to `shared-rules.md`: "Baseline values must be sourced from the most recent observed data point. Never use a historical baseline when a current one is available." (3) The labor impact agent (proposed) should always fetch current unemployment rate before projecting. |

### Eval T-11: UK Baseline Unemployment

| Field | Detail |
|-------|--------|
| **Chat Question** | "What is UK unemployment going to be December 2026?" |
| **Topic / Issues** | User had to manually provide baseline: "UK baseline unemployment today (February 2026) is 5.4%." |
| **Expected Behavior** | System should fetch current baseline data from web or catalog before projecting. |
| **Current STDF Coverage** | `stdf-scurve-fitter` and `stdf-regional-adopter` have web access and can fetch current market share data. |
| **Gaps** | **No labor baseline data sourcing.** The pipeline fetches technology adoption baselines but has no mechanism for labor market baselines. (Same gap as T-08.) |
| **Recommendations** | Same as T-08. The proposed `stdf-labor-impact` agent must include a baseline data fetch step. |

---

## P2 — Excessive Clarification {#p2-excessive-clarification}

**Priority:** P2 (5+ incidents)
**Key Quote:** "Ask no clarifying questions"

### Eval T-12: Over-Clarification Before Analysis

| Field | Detail |
|-------|--------|
| **Chat Question** | "When will USA unemployment hit 7%?" |
| **Topic / Issues** | Too many clarifying questions before running analysis. |
| **Expected Behavior** | Run analysis with reasonable defaults first. Ask for corrections after if needed. |
| **Current STDF Coverage** | The `/stdf` skill Step 1 does ask user for preset confirmation via `AskUserQuestion`. Otherwise, agents run autonomously once launched. |
| **Gaps** | **The `/stdf` skill asks ONE question (preset confirmation) which is appropriate.** However, if the user's query is ambiguous, there's no "reasonable defaults" fallback. The skill could default to FULL preset and skip confirmation for straightforward queries. |
| **Recommendations** | (1) Add **auto-detect confidence** to preset selection: if keyword matching is strong (e.g., query clearly says "disruption analysis of X"), skip the confirmation step and auto-select. Only ask when ambiguous. (2) Add to `shared-rules.md`: "When in doubt, run the analysis with reasonable defaults. Present results with stated assumptions. Let the user correct assumptions after seeing output." (3) Add a `--no-confirm` flag to `/stdf` for power users. |

---

## P2 — Internal Data First {#p2-internal-data-first}

**Priority:** P2 (3+ incidents)
**Key Quote:** "Just use our data factory data"

### Eval T-09: UK Labour Market Internal Data

| Field | Detail |
|-------|--------|
| **Chat Question** | UK labour market composition analysis |
| **Topic / Issues** | User asked: "what did you get from our internal data on uk labour if anything?" — implying system didn't use internal data. |
| **Expected Behavior** | Check internal data catalog FIRST before web search. |
| **Current STDF Coverage** | **Strong coverage by design.** Data Source Hierarchy in `shared-rules.md`: Tier 1 (published reports) > Tier 2 (local data catalog) > Tier 3 (web search). `stdf-cost-researcher` searches `data/` catalog first via `lib.data_catalog.search_curves()`. Every data point must be tagged with tier. |
| **Gaps** | **The hierarchy is well-defined but enforcement is soft.** There's no guardrail that detects when an agent used web data for something available in the catalog. The compliance criteria don't check for "could have used Tier 2 but used Tier 3 instead." UK labor data likely isn't in the catalog anyway (it covers energy/transport/compute/materials). |
| **Recommendations** | (1) Add a **catalog coverage pre-check** to cost-researcher and capability agents: before web search, run `search_curves(query)` and log hits. If catalog has relevant data, use it; log the decision. (2) Expand catalog to include labor market data if AI/labor disruption is a core use case. (3) Add a compliance criterion: "Tier 2 data used when available" — check if any Tier 3 data point has a matching Tier 2 curve. |

---

## P2 — Wrong Financial Terminology {#p2-wrong-financial-terminology}

**Priority:** P2 (3+ incidents)
**Key Quote:** "steepener is the opposite"

### Eval R-35: Bond Market Terminology Error

| Field | Detail |
|-------|--------|
| **Chat Question** | UK employment forecast with bond market implications |
| **Topic / Issues** | System reversed the definition of curve steepener/flattener. User corrected: "A curve steepener is the opposite where the front end rates go down and back end rates go up. You have it reversed." |
| **Expected Behavior** | Correct financial terminology: steepener = spread widens (long rates up, short rates down); flattener = spread narrows. |
| **Current STDF Coverage** | **No financial terminology rules exist.** The vocabulary system covers disruption/energy terminology but not fixed income, equity, or macro terminology. |
| **Gaps** | **No financial domain glossary or guardrails.** The pipeline was built for technology disruption analysis, not financial markets. When results cross into investment implications (which they frequently do for both users), there's no terminology enforcement. |
| **Recommendations** | (1) Add a **financial terminology reference** to `shared-rules.md` or a separate `financial-glossary.md`: curve steepener/flattener, LCOE limitations, basis points, contango/backwardation, etc. (2) Since the system is used for investment analysis, this is higher priority than P2 suggests. (3) The synthesizer should reference the glossary when generating investment implications. |

### Eval R-35 (continued): LCOE Misuse

| Field | Detail |
|-------|--------|
| **Chat Question** | Various energy analyses |
| **Topic / Issues** | Robert: "LCOE is a very poor measure" — used when inappropriate. |
| **Expected Behavior** | Recognize LCOE limitations. Use system-level cost comparisons (including storage, T&D, capacity factor) not just LCOE. |
| **Current STDF Coverage** | `stdf-cost-fitter` converts to service-level units (criterion 2.5). `lib.cost_curve_math` has `convert_solar_wp_to_kwh()` and `convert_storage_cap_to_delivered()` which go beyond simple LCOE. |
| **Gaps** | **No explicit anti-LCOE guidance.** While the cost-fitter converts to service-level units, there's no rule saying "Don't rely on LCOE alone — include system-level costs (storage, T&D, reliability)." |
| **Recommendations** | (1) Add to `shared-rules.md`: "LCOE is an incomplete metric. For energy analyses, always compute system-level cost including storage, T&D, and reliability costs. Flag LCOE as partial when used." (2) Add a system-level cost function to `lib/cost_curve_math.py`. |

---

## P3 — Web Data Access {#p3-web-data-access}

**Priority:** P3 (8+ incidents, platform capability)

### Eval T-17: Residential Solar Cost Data

| Field | Detail |
|-------|--------|
| **Chat Question** | "What is the cost per watt of installed residential solar in Australia, Germany, and Netherlands?" |
| **Topic / Issues** | Could not provide data — no internal data, no web access. User: "yes go get web data and show it to me before you use it." |
| **Expected Behavior** | When web access is available, use it to fill data gaps. When not, clearly state limitation. |
| **Current STDF Coverage** | **Web access IS available** for Phase 1 agents (cost-researcher, capability, domain-disruption), adoption agents (scurve-fitter, regional-adopter, xcurve-analyst), and the adoption-readiness-checker. `stdf-cost-researcher` has full WebSearch + WebFetch tools. |
| **Gaps** | **Coverage is good at the pipeline level.** The old system (pre-v2) lacked web access; the v2 pipeline has it for research agents. However: (1) residential solar cost data by country may not be in the catalog, and (2) the cost-researcher's web search quality depends on search queries — country-specific solar installation costs require specific search strategies. |
| **Recommendations** | (1) Add residential solar installation cost data (by country) to `data/` catalog. (2) Add **country-specific cost search templates** to cost-researcher guidance: for solar, search "installed cost per watt [country] [year]". (3) Test that WebFetch can actually retrieve data from common solar cost databases (solarchoice.net.au, IRENA, etc.). |

### Eval T-19: UK Power Generation (Wrong Scope)

| Field | Detail |
|-------|--------|
| **Chat Question** | "What is the UK annual power generation in TWh since 2000?" |
| **Topic / Issues** | System returned European aggregate data instead of UK-specific. User: "I did not ask for European generation data. I asked for UK generation data." |
| **Expected Behavior** | Answer the specific geographic scope asked. UK means UK, not Europe. |
| **Current STDF Coverage** | `stdf-regional-adopter` does per-region analysis (China, USA, Europe minimum). `stdf-cost-researcher` can search by region. |
| **Gaps** | **Region filtering in web search needs improvement.** This is a search quality issue, not an architectural gap. The agents can search the web but may return broader geographic data than requested. No validation that search results match the requested geographic scope. |
| **Recommendations** | (1) Add a **geographic scope validation** to agents: if the user specified "UK", verify that data returned is UK-specific, not UK+Europe or Europe aggregate. (2) Add UK-specific energy generation data to catalog. (3) Add to agent prompts: "If the query specifies a country/region, verify ALL data points are for that specific geography. Never substitute aggregates." |

---

## P3 — Multi-Session Consistency {#p3-multi-session-consistency}

**Priority:** P3 (3+ incidents)
**Key Quote:** "Will you learn from this interaction?"

### Eval T-05 vs T-06 / R-14 / T-25-T-27

| Field | Detail |
|-------|--------|
| **Chat Question** | Same questions across sessions producing different answers |
| **Topic / Issues** | 19.5% vs 8.3% for same unemployment question. Lead analysis required 3 attempts. Robert asked "Will you learn from this?" |
| **Expected Behavior** | Consistent results for same inputs. Learning from corrections persists across sessions. |
| **Current STDF Coverage** | `.claude/agent-memory/` provides persistent per-agent memory. `shared-rules.md` includes memory system instructions. Each run produces a new output directory, preserving history. |
| **Gaps** | **Agent memory is available but underutilized.** The memory system exists but there's no mechanism to: (1) automatically store key parameters from each run for comparison, (2) recall previous run results when processing a similar query, (3) apply user corrections from past sessions. The memory is reactive (save when told) not proactive (save results for future reference). |
| **Recommendations** | (1) Add **auto-archival** to `/stdf` skill: after each run, save key parameters (tipping year, S-curve params, confidence) to agent memory with the query as key. (2) Add a **previous run recall** step to `/stdf` skill Step 1: before starting, check if a similar query was run before and note previous results. (3) Add a **correction persistence** mechanism: when users correct model parameters, save to agent memory for reuse. |

---

## Query-Type Coverage Gap Analysis {#query-type-coverage}

This section maps user query *types* (not specific queries) to pipeline coverage.

| Query Type | Example Queries | Current Pipeline Coverage | Gap Level |
|------------|----------------|--------------------------|-----------|
| **Technology disruption** (core) | "Analyze energy storage disruption", "When will BEV disrupt ICE?" | **FULL** — entire 16-agent pipeline built for this | None |
| **Commodity demand** | "What happens to copper demand?" "When will lead demand drop 10%?" | **FULL** — commodity chain (07a-d) handles this | Minor (catalog gaps) |
| **Labor/unemployment forecasting** | "What will US unemployment be in Dec 2026?" (16+ Tony sessions, 45+ Robert sessions) | **NOT COVERED** — no labor-specific agent, no task digitizability model, no sector employment data | **CRITICAL GAP** |
| **Investment/trading ideas** | "Best contrarian trade?", "Short Bloom Energy?" | **PARTIAL** — disruption analysis provides the foundation, but no investment thesis agent | Significant |
| **Macroeconomic impact** | "Is AI deflationary?", "Impact on GDP growth?" | **NOT COVERED** — no macro modeling capability | **CRITICAL GAP** |
| **Geopolitical cascading** | "Financial consequences for Russia from oil disruption" | **NOT COVERED** — X-curve models technology decline, not nation-state impact | Significant |
| **Country-specific data lookup** | "UK power generation since 2000", "Cost of solar in Australia" | **PARTIAL** — agents have web access, but no country-data-lookup specialization | Minor |
| **Pharmaceutical disruption** | "GLP-1 disruption analysis" | **PARTIAL** — pipeline framework works, but zero pharma data in catalog | Significant |
| **Credit/financial stress** | "Top 4 areas of credit stress from disruption" | **NOT COVERED** — no credit/financial modeling agent | Significant |
| **Policy analysis** | "If US gives right to generate/store power, what happens?" | **PARTIAL** — adoption-readiness-checker assesses regulatory environment, but no policy impact modeling | Minor |
| **Real-time economic data** | "What about today's nonfarm payroll?" | **NOT COVERED** — pipeline runs on historical data, no real-time event analysis | Moderate |

### Most-Requested Query Types vs Coverage

| Query Type | % of All Sessions | Pipeline Coverage |
|------------|-------------------|-------------------|
| AI/Labor Disruption | **33%** (67/202 sessions) | **NOT COVERED** |
| Energy Disruption | **18%** (36/202) | **FULL** |
| Investment/Trading | **16%** (32/202) | **PARTIAL** |
| Macro/Inflation/Rates | **8%** (16/202) | **NOT COVERED** |
| Commodity Markets | **7%** (14/202) | **FULL** |
| Geopolitics | **5%** (10/202) | **NOT COVERED** |
| AI Infrastructure | **5%** (10/202) | **PARTIAL** |
| Pharma/GLP-1 | **3%** (6/202) | **PARTIAL** |

**The pipeline's strongest coverage (energy, commodities) represents ~25% of actual queries. The most frequent query type (AI/labor, 33%) has zero dedicated coverage.**

---

## Agent-Level Gap Summary {#agent-level-gaps}

| Agent | Works Well For | Missing Capability | Priority |
|-------|---------------|-------------------|----------|
| `stdf-domain-disruption` | Technology disruption mapping | Disruption vector completeness validation; X-Flow vs Stellar classification | P1 |
| `stdf-cost-researcher` | Energy/transport cost data | AI compute, pharma, labor market data; country-specific search strategies | P0 |
| `stdf-cost-fitter` | Exponential fitting, thresholds | Learning rate plausibility bounds; thin-data mode (2-3 points) | P1 |
| `stdf-capability` | Multi-dimensional comparison | Pharma-specific dimensions; AI capability dimensions | P1 |
| `stdf-cost-parity-checker` | Binary parity assessment | No gaps for its scope | — |
| `stdf-capability-parity-checker` | Aggregate parity assessment | No gaps for its scope | — |
| `stdf-adoption-readiness-checker` | Infrastructure/regulatory assessment | Labor market readiness dimensions | P2 |
| `stdf-tipping-synthesizer` | Tipping year integration | Post-tipping labor market dynamics | P2 |
| `stdf-scurve-fitter` | Logistic S-curve fitting | Monthly resolution; technology-to-labor conversion | P1 |
| `stdf-regional-adopter` | Per-region adoption breakdown | More granular country coverage (beyond China/USA/Europe) | P2 |
| `stdf-xcurve-analyst` | Incumbent decline modeling | Nation-state impact; financial cascading | P1 |
| `stdf-demand-decomposer` | Commodity demand decomposition | No gaps for its scope | — |
| `stdf-stream-forecaster` | 3-stream projection | No gaps for its scope | — |
| `stdf-fleet-modeler` | Stock-flow fleet modeling | No gaps for its scope | — |
| `stdf-regional-demand-analyst` | Regional demand breakdown | No gaps for its scope | — |
| `stdf-synthesizer` | 7-phase narrative merge | Consistency checker; consensus comparison; investment implications filter | P0 |

---

## Recommended New Agents / Capabilities {#new-capabilities}

### 1. `stdf-labor-impact` (NEW AGENT) — **CRITICAL PRIORITY**

**Justification:** 33% of all sessions (67/202) involve AI/labor disruption queries. Zero dedicated coverage today.

| Field | Detail |
|-------|--------|
| **Produces** | `08a-labor-impact.md` |
| **Requires** | `05a-scurve-fitter.md` (adoption S-curves), `01-domain-disruption.md` (disruption map) |
| **Criticality** | HIGH |
| **Key Functions** | Convert technology adoption → sector employment displacement. Task-level filtering (cognitive + digitizable). Monthly granularity. Baseline validation (current unemployment rate). Displacement-to-unemployment conversion with explicit assumptions. |
| **Lib Support** | New `lib/labor_math.py`: `displacement_from_adoption()`, `sector_unemployment_projection()`, `task_filter()`, `monthly_projection()` |
| **Data Needs** | Sector employment counts by country, task digitizability indices, current unemployment rates |
| **Addresses Evals** | T-01 through T-12, R-12 through R-19, R-21, R-22 |

### 2. `stdf-macro-impact` (NEW AGENT) — HIGH PRIORITY

**Justification:** 8% of sessions involve macro/inflation/rates. Geopolitical cascading (5%) also routes here.

| Field | Detail |
|-------|--------|
| **Produces** | `08b-macro-impact.md` |
| **Requires** | `05c-xcurve-analyst.md` (incumbent decline), `08a-labor-impact.md` (labor displacement) |
| **Criticality** | MEDIUM |
| **Key Functions** | GDP impact from technology disruption. Deflationary/inflationary assessment. Sovereign fiscal impact for petro-states. Credit stress assessment from stranded assets. |
| **Addresses Evals** | R-16, R-20, R-23, T-36, T-37 |

### 3. `stdf-investment-analyst` (NEW AGENT) — MEDIUM PRIORITY

**Justification:** 16% of sessions involve investment/trading analysis. Both users heavily use disruption analysis for investment decisions.

| Field | Detail |
|-------|--------|
| **Produces** | `08c-investment-thesis.md` |
| **Requires** | `06-synthesizer.md` (full synthesis), optionally `08b-macro-impact.md` |
| **Criticality** | MEDIUM |
| **Key Functions** | Translate disruption findings into investment implications. Consistency check: all positions must align with cost curves and tipping analysis. Contrarian insight identification (what does consensus miss?). Individual company disruption exposure scoring. |
| **Addresses Evals** | R-24, R-25, R-27, R-28, R-33, R-42, T-14, T-35, T-36 |

### 4. Vocabulary / Guardrail Enhancements (EXISTING MODULES)

| Enhancement | Module | Priority | Addresses |
|-------------|--------|----------|-----------|
| Populate `BANNED_SOURCE_PATTERNS` | `lib/vocabulary.py` | P0 | T-26, T-38 |
| Add anti-scenario terms | `lib/guardrails.py` | P1 | T-03, T-26 |
| Add fabrication detection (untagged numbers) | `lib/guardrails.py` | P0 | T-23, T-28, T-25 |
| Add Jevons Paradox rule (X-Flow only) | `lib/vocabulary.py` | P1 | T-31 |
| Add cost/price semantic check | `lib/guardrails.py` | P1 | T-21 |
| Add STDF glossary (God Parity, X-Flow, Stellar, SWB) | `shared-rules.md` | P1 | T-18, T-31 |
| Add financial terminology reference | `shared-rules.md` | P2 | R-35 |
| Add "AI Capability Improvement" not "Growth" | `lib/vocabulary.py` | P1 | T-32 |

### 5. Data Catalog Expansion (EXISTING INFRASTRUCTURE)

| Data Category | Priority | Addresses | Estimated Curves |
|---------------|----------|-----------|-----------------|
| AI compute costs (GPU $/FLOP, inference $/token) | P0 | T-28, T-31 | 10-15 |
| Labor market (sector employment, digitizability) | P0 | T-01 to T-12, R-12 to R-19 | 20-30 |
| Pharmaceutical (GLP-1 costs, adoption, efficacy) | P1 | T-21 to T-23 | 10-15 |
| Residential solar by country | P1 | T-17, T-18, T-20 | 15-20 |
| Lead-acid battery / lead demand | P1 | T-25 to T-27 | 5-10 |
| Bond/rates macro data | P2 | R-35, R-23 | 10-15 |
| Sovereign fossil fuel dependency | P2 | R-20 | 5-10 |

### 6. Skill Enhancements

| Skill | Enhancement | Priority | Addresses |
|-------|------------|----------|-----------|
| `/stdf` | Auto-detect preset without confirmation for clear queries | P2 | T-12 (excessive clarification) |
| `/stdf` | Auto-archival of key params to agent memory | P2 | Multi-session consistency |
| `/stdf` | Previous run recall before starting | P3 | T-05 vs T-06 divergence |
| NEW: `/stdf-compare` | Cross-run comparison tool | P3 | Multi-session consistency |
| `/stdf-validate` | Untagged number detection | P0 | Fabrication prevention |
| `/stdf-validate` | Anti-scenario term detection | P1 | T-03, T-26 |

---

## Summary: Coverage Scorecard

| Eval Category | # Evals | Current Coverage | After Recommendations |
|---------------|---------|-----------------|----------------------|
| Fabricating Data (P0) | 8+ | **Partial** — guardrails catch vocab but not fabricated numbers | **Strong** — number provenance + plausibility checks |
| Framework Compliance (P0) | 5+ | **Strong** — S-curves structural, banned sources enforced | **Complete** — populated BANNED_SOURCE_PATTERNS |
| Opinion vs Process (P0) | 5+ | **Partial** — agents are process-driven, but no consistency checker | **Strong** — cross-check in synthesizer |
| Terminology (P1) | 10+ | **Moderate** — 10 banned terms, but gaps in AI/financial/STDF-specific terms | **Strong** — expanded vocabulary + glossary |
| No Scenarios (P1) | 3+ | **Moderate** — structural single-estimate, but no anti-scenario guardrail | **Complete** — anti-scenario terms in guardrails |
| Internal Consistency (P1) | 3+ | **Weak** — no cross-check mechanism | **Strong** — consistency validation in synthesizer |
| Correct Baselines (P1) | 3+ | **Strong** — date awareness rules | **Complete** — baseline value validation |
| Excessive Clarification (P2) | 5+ | **Good** — one confirmation step only | **Complete** — auto-detect for clear queries |
| Internal Data First (P2) | 3+ | **Strong** — tier hierarchy enforced | **Complete** — catalog coverage pre-check |
| Financial Terms (P2) | 3+ | **None** — no financial glossary | **Moderate** — reference added |
| Web Data Access (P3) | 8+ | **Strong** — agents have WebSearch/WebFetch | **Complete** — catalog + search improvements |
| Multi-Session (P3) | 3+ | **Weak** — memory exists but underutilized | **Moderate** — auto-archival + recall |

### Critical Insight

**The #1 gap is not a bug — it's a missing domain.** The pipeline excels at technology disruption analysis (energy, transport, materials) but 33% of user queries are about AI/labor disruption, which requires a fundamentally different output type (unemployment forecasts, not market share S-curves). Adding `stdf-labor-impact` would address the single largest category of user queries and the most frequent source of frustration.
