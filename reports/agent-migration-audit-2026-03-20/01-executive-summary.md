# Executive Summary

## Overall Assessment
The migration from `old_prompts/` to `.claude/agents/` is only a partial business-logic migration.

The new agent set is better in five ways:
- It is more explicit, modular, and testable as a staged STDF-v2 pipeline.
- It has stronger evidence hygiene for observed data, especially around web-search recency and forecast rejection.
- It formalizes tipping into three conditions: cost parity, capability parity, and adoption readiness.
- It adds a more rigorous commodity-demand chain with explicit decomposition, stock-flow logic, and regional demand disaggregation.
- It improves compliance visibility through per-agent criteria, fit-quality expectations, and synthesis confidence logic.

The new agent set is weaker or incomplete in six ways:
- It does not yet reproduce the legacy product surface outside the core STDF pipeline.
- It removes or leaves implicit the calibrated sector skills that users actually depended on: artificial labor, lithium-ion/lead, energy SWB, and copper.
- It has no first-class investment workflow equivalent to `stellar_subagent_system` plus `value_investment_subagent_system` plus company/VCA support.
- It has no obvious equivalent for reformulation, clarification, evaluator enforcement, citation building, trace explanation, history recall, or meeting/standup retrieval.
- It does not fully preserve legacy anti-fabrication rules such as skill sovereignty, tiered derivation gating, and confirmation-only mode before assumption-heavy calculations.
- It lacks a report-lookup path for precomputed domain reports, which the old system used to answer recurring labor, energy, and lead questions deterministically.

## What Users Actually Needed
The chat exports show that users were not only asking for generic STDF analyses. They repeatedly needed:
- Reliable sector-specific answers for labor, batteries/lead, energy, and copper.
- Explicit source discipline and zero tolerance for invented assumptions.
- Investment translation: long/short framing, trade expression, company screening, ticker-aware analysis.
- Meta behaviors: traceability, continuity across sessions, history access, and correction-aware responses.
- Better handling of repeated asks on unresolved questions.

## Highest-Risk Business Gaps
### 1. Loss of specialized sector models
Legacy routing forced certain questions into calibrated domain skills. New agents are mostly generic STDF components. That creates a real risk of replacing validated domain logic with generic analysis.

Most exposed areas:
- Artificial labor / unemployment / labor-market disruption
- Lithium-ion and lead-acid demand / supply-demand / SLI / VRLA / TaaS interactions
- SWB energy-system displacement
- Copper demand tied to product-level disruption

### 2. Loss of investment product surface
The old system had three distinct investment behaviors:
- `stellar_subagent_system`: thesis -> instruments -> catalysts -> invalidation -> sizing
- `value_investment_subagent_system`: disruption -> value drivers -> long/short baskets
- company/VCA agents: company identification, ticker resolution, value-chain framing

The new system has no direct replacement. This matters because the chats include repeated asks about Bloom Energy, utility stocks, trade timing, rate implications, and other investment consequences.

### 3. Loss of orchestration and governance layers
The legacy product had explicit business logic for:
- reformulating user intent
- clarifying scope
- evaluating outputs for anti-patterns
- building citations and provenance
- handling history/meta/trace requests
- forcing web re-verification for disputed claims

The new agent set largely starts after those decisions should already have been made.

### 4. Weak migration of anti-fabrication controls
The old system encoded stronger commercial safeguards than the new one currently makes explicit:
- skill outputs were authoritative
- derived values had tiered permission rules
- confirmation was required before assumption-heavy conversion steps
- no shadow modeling when a skill existed
- no fabricated scope tables

This gap maps directly to user frustration in the chats.

## Chat-Derived Reality Check
The audit of `chat_exports/` shows four recurring failure classes:
- fabricated or weakly sourced numbers
- wrong scope or wrong metric
- business-logic mistakes in the model itself
- repeated user re-asks because prior answers were not production-grade

That means the migration risk is practical, not theoretical.

## Bottom Line
The new agent system is a stronger STDF-v2 engine than the legacy prompt stack.
It is not yet a stronger product.

To reach parity, the migration backlog should prioritize:
1. restoring domain-specialized business logic and deterministic routing,
2. restoring investment and company-analysis workflows,
3. restoring orchestration/evaluation/provenance layers,
4. restoring report-based deterministic retrieval for recurring domains,
5. hardening assumption governance to eliminate invented numbers and scope drift.
