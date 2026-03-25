# Agent-System Findings

## Executive summary

The new `.claude` agent system is a better execution engine than the old prompt stack, but it is a thinner product system. It is optimized for running STDF analyses, not yet for governing the full lifecycle of user intent, canonical sector routing, semantic QA, provenance, and downstream business deliverables.

That means the migration problem is not only about adding sector math. It is also about restoring the missing operating system around the math.

## What the new agent system does well

The new system has strong first-class STDF agents for:

- domain disruption framing
- cost research and cost fitting
- capability analysis and capability parity
- adoption readiness
- tipping synthesis
- S-curve fitting
- regional adoption
- X-curve analysis
- demand decomposition
- stream forecasting
- fleet modeling
- regional demand analysis
- energy dispatch
- gas-supply decomposition
- final synthesis

This agent family is coherent and maps cleanly to a staged disruption-analysis DAG. It is much more maintainable than the old prompt-only orchestration pattern.

## Missing agent families

The new system does not clearly replace several important old prompt roles.

### 1. Intent and request shaping

Old system coverage:

- `reformulator_system.txt`
- `clarification_system.txt`
- parts of `planner_system.txt`

What those old prompts contributed:

- intent normalization
- anti-sycophancy framing
- terminology preservation
- sector hints
- structured routing to the right specialist
- explicit clarification boundaries

Current gap:

- The new `stdf` orchestrator classifies work at a high level, but it does not appear to provide the same explicit request-shaping layer or deterministic routing semantics.

Recommendation:

- Add `stdf-intent-router`
- Add `stdf-clarifier`
- Define a structured routing schema with fields such as `sector`, `query_type`, `needs_report_lookup`, `needs_company_mode`, `needs_canonical_sector_engine`, and `confidence`

### 2. Semantic review

Old system coverage:

- `evaluator_system.txt`

What it contributed:

- final-pass semantic QA
- tool-grounding checks
- skill-sovereignty checks
- citation completeness
- temporal consistency
- sycophancy checks
- corrected-response generation when needed

Current gap:

- The new system is stronger on structural validation and banned-pattern enforcement, but weaker on reviewing whether the final answer is semantically faithful to upstream evidence and policy.

Recommendation:

- Add `stdf-semantic-reviewer`
- Make it run after synthesis and before user-facing finalization
- Give it authority to fail the run if the final write-up drifts from upstream files

### 3. Provenance and report retrieval

Old system coverage:

- `citation_builder_system.txt`
- `trace_explain_system.txt`
- `report_knowledge_lookup_system.txt`

What it contributed:

- structured citation assembly
- user-facing provenance traces
- direct retrieval from precomputed reports for standard cases

Current gap:

- The new system has output files and source rules, but it does not expose the same first-class provenance builder or report retrieval layer.

Recommendation:

- Add `stdf-provenance-builder`
- Add `stdf-trace-explainer`
- Add `stdf-report-lookup`
- Store retrievable report assets in a versioned, queryable format rather than burying them in free-text prompt files

### 4. Business-output extensions

Old system coverage:

- `feedback_loop_subagent_system.txt`
- `value_investment_subagent_system.txt`
- `company_analysis_subagent_system.txt`
- `vca_company_subagent_system.txt`
- `stellar_subagent_system.txt`

What it contributed:

- scenario framing beyond raw sector modeling
- investment implications
- company-specific implications
- value-chain analysis

Current gap:

- The new STDF system largely stops at disruption synthesis.

Recommendation:

- Add these as optional downstream agent families, not as changes inside the core STDF modeling DAG

## Old-to-new component mapping

| Old component | New equivalent | Status | What should happen |
| --- | --- | --- | --- |
| `main_agent_system.txt` | `stdf` skill orchestrator | Partially replaced | Keep new orchestrator, restore missing routing and product modules |
| `planner_system.txt` | `stdf` DAG plan logic | Partially replaced | Keep new DAG planner, re-add skill-sovereignty rules and richer route policy |
| `reformulator_system.txt` | None obvious | Missing | Add request-shaping layer |
| `clarification_system.txt` | None obvious | Missing | Add clarification gate |
| `evaluator_system.txt` | `stdf-validate` plus hook, partially | Partially replaced | Add semantic reviewer |
| `citation_builder_system.txt` | None obvious | Missing | Add provenance builder |
| `trace_explain_system.txt` | None obvious | Missing | Add trace explainer |
| `report_knowledge_lookup_system.txt` | None obvious | Missing | Add report lookup service |
| `stdf_subagent_system.txt` | Many STDF execution agents | Replaced and improved | Keep new system |
| `energy_sector_subagent_system.txt` | `stdf-energy-dispatch`, `stdf-gas-supply-decomposer` | Largely replaced | Fill retrieval and scenario gaps only |
| `copper_forecast_subagent_system.txt` | Generic STDF agents only | Weak replacement | Add canonical copper engine |
| `artificial_labor_subagent_system.txt` | Generic STDF pieces only | Weak replacement | Add canonical labor engine |
| `lithium_ion_subagent_system.txt` | Generic STDF pieces plus memory | Partial replacement | Add canonical battery demand engine and report lookup |
| `web_search_subagent_system.txt` | Shared web-search rules inside STDF | Partially replaced | Keep new rules; add research-delta mode if needed |
| `feedback_loop_subagent_system.txt` | None obvious | Missing | Add optional downstream module |
| `value_investment_subagent_system.txt` | None obvious | Missing | Add optional downstream module |
| `company_analysis_subagent_system.txt` | None obvious | Missing | Add optional downstream module |
| `vca_company_subagent_system.txt` | None obvious | Missing | Add optional downstream module |

## What should become code, not prompt text

The old stack used prompts to carry a lot of policy. The new migration should not repeat that pattern when the rule is actually deterministic.

Put the following into code and tests:

- sector coefficients
- calibration parameters
- taxonomy mappings
- parity rules
- stream decomposition rules
- report retrieval indexes
- citation assembly schemas
- semantic validation checks that can be made deterministic

Keep the following in prompts:

- workflow instructions
- agent role boundaries
- escalation criteria
- output style contracts
- explanation standards

## Recommended new agents and services

### Critical additions

- `stdf-intent-router`
- `stdf-clarifier`
- `stdf-semantic-reviewer`
- `stdf-provenance-builder`
- `stdf-trace-explainer`
- `stdf-report-lookup`
- sector engines for artificial labor, copper, and lithium/lead

### Important but secondary additions

- `stdf-feedback-loop-analyst`
- `stdf-investment-synthesizer`
- `stdf-company-impact-analyst`
- `stdf-vca-analyst`
- `stdf-research-delta-finder`

## Recommended operating rules

The new system should adopt these explicit rules from the old stack:

- If a canonical sector engine exists, use it.
- If the request is ambiguous on scope, ask a clarification question before modeling.
- If the user asks for a standard base-case sector answer and a precomputed canonical report exists, retrieve it instead of re-running an equivalent analysis.
- Every final answer should pass both structural validation and semantic review.
- Every user-facing report should be able to produce a trace/provenance summary from the underlying files.
- Agent memory may inform search or setup, but it must not override versioned code or versioned reference data.

## Business logic ownership model

Recommended ownership:

- Orchestrator owns sequencing and route selection.
- Sector engines own sector math and domain rules.
- Shared STDF agents own generic disruption abstractions.
- Validation layer owns guardrails and review.
- Business-output agents own investor/company/feedback presentations.

This separation is necessary if the new system is meant to scale cleanly across sectors.

## Final recommendation

Treat the migration as two parallel workstreams:

1. Restore the missing operating system around STDF.
2. Port the missing sector engines into first-class code.

If only the second happens, the system will still be weak on routing, review, and productized outputs.
If only the first happens, the system will still drift on sector correctness.
