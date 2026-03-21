# Migration Gaps And Risks

## Gap 1: No first-class orchestrator above the new agents
### What was present before
The legacy stack had explicit orchestration roles for reformulation, clarification, planning, evaluation, citation building, and trace explanation.

### What exists now
The new agent set starts effectively at STDF analysis execution.

### Business risk
- Wrong domain path chosen for the question.
- Wrong scope due to missing clarification step.
- No system-level adjudication when outputs violate business rules.
- Harder recovery from user corrections, disputes, and history/meta asks.

### Why this matters in chats
- Tony repeatedly corrected scope and rules.
- Gibbins asked for revision after new evidence and for empirical corroboration.
- A no-response incident occurred in a pipeline context that clearly needed orchestration resilience.

## Gap 2: Specialized sector logic was replaced by generic STDF stages
### What was present before
Legacy routing forced battery, labor, copper, and energy questions into dedicated sector skills.

### What exists now
A generic STDF-v2 engine with optional commodity extensions.

### Business risk
- Loss of tuned business rules for recurring domains.
- More room for generic but wrong logic.
- Reduced determinism for repeated institutional asks.

### Highest-risk domains
- Artificial labor / unemployment
- Lithium-ion and lead / SLI / VRLA / TaaS
- Energy SWB displacement
- Copper demand

## Gap 3: Investment workflow is effectively absent
### What was present before
- `stellar_subagent_system`
- `value_investment_subagent_system`
- `company_analysis_subagent_system`
- `vca_company_subagent_system`

### What exists now
No clear investment, company, ticker, or trade-expression agents.

### Business risk
- The system can say disruption is happening, but cannot translate that into investable action.
- User queries around trades, short theses, utility equities, and company exposure lose their natural product path.

### Chat evidence it matters
- Bloom Energy trade/timing sessions
- Utility-stock/AI attribution sessions
- Gibbins’ repeated use of long/short framing

## Gap 4: Weak migration of assumption governance
### What was present before
The old system explicitly controlled derived outputs with:
- skill sovereignty,
- numeric grounding,
- derivation tiers,
- user confirmation for risky conversions,
- prohibition on fabricated scope tables.

### What exists now
Strong evidence rules exist, but the same pipeline-level commercial safeguards are not clearly reproduced.

### Business risk
- Assumption-heavy outputs can look rigorous while still being weakly governed.
- Users will continue to call out “made up” numbers even if the pipeline is technically more structured.

### Chat evidence it matters
- Tony labor unemployment conversions
- Tony biotech convenience-curve speculation
- Bloom backlog timing assumption for Gibbins

## Gap 5: Precomputed report mode is gone
### What was present before
Legacy sector workflows could answer directly from report artifacts and preserve exact labels, tables, provenance markers, and aggregation semantics.

### What exists now
No visible report-lookup or report-only answer path.

### Business risk
- Repeated questions in known sectors become slower and less deterministic.
- Exact business semantics such as lead driver labels and report-native aggregation can be lost.
- The system may regenerate analysis when it should retrieve canonical outputs.

## Gap 6: Meta/history/trace surfaces are gone
### What was present before
The old system had explicit handling for:
- `history_request`
- `trace_explain`
- `feedback_only`
- `meta_request`
- meeting/standup retrieval

### What exists now
No direct equivalent in `.claude/agents/`.

### Business risk
- Lower user trust when asking “why did you say that?” or “what did we conclude before?”
- Worse continuity in multi-session institutional work.
- Missing product behavior for non-analysis asks that still matter in research workflows.

## Gap 7: New design intentionally de-emphasizes policy/macro reaction modeling
### What exists now
The new system treats disruption primarily as cost-curve/market-driven and formalizes adoption readiness, but it does not include a dedicated feedback-loop / 5-actor model equivalent.

### Business risk
- Central-bank, government, consumer, and market response questions become second-class.
- This is especially relevant for labor-disruption and macro-rate questions.

### Chat evidence it matters
- Gibbins explicitly asked for central-bank policy-rate implications from labor disruption.
- Bloom and utility sessions frequently crossed into policy, market repricing, and timing-risk territory.

## Gap 8: Reliability and degraded-mode rules are under-specified at the product layer
### Observation
The new STDF agents define hard-fail and degraded behaviors inside the pipeline, but there is no visible top-level product policy for empty outputs, retries, or fallback answer modes.

### Business risk
- More user-visible dead ends.
- Harder recovery from upstream failures.
- Lower confidence in institutional use.

### Chat evidence it matters
- `chat_exports/rgibbins/2026-02-14_10-03-55_cc5f4e.md` shows a real no-response event.

## Net Risk Rating
| Risk area | Severity | Reason |
|---|---|---|
| Sector-specific forecast regression | Critical | Affects highest-frequency recurring asks |
| Investment workflow loss | Critical | Removes a major business use case |
| Orchestration/evaluation/meta loss | Critical | Reduces correctness, trust, and recoverability |
| Assumption/fabrication governance | High | Directly tied to user dissatisfaction |
| Report-mode loss | High | Degrades determinism and exactness in known domains |
| Macro/feedback-loop gap | High | Material for labor/macro/investment consequences |
| Reliability fallback gaps | High | Empty response is unacceptable in production workflows |
| Regional-global nuance limits in STDF-v2 | Medium | Important but not the most urgent migration blocker |
