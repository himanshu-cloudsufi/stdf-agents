# Legacy-to-New Agent Migration Audit

Date: 2026-03-24

Scope reviewed:

- `skills/.claude/skills/copper-forecast/`
- `skills/.claude/skills/artificial-labor/`
- `skills/.claude/skills/lithium-ion-demand/`
- `stdf-agents/.claude/`
- `stdf-agents/old_prompts/`

Files in this audit:

- `general-findings.md`
- `agent-system-findings.md`
- `migration-blueprint.md`
- `sector-artificial-labor-findings.md`
- `sector-copper-findings.md`
- `sector-lithium-lead-findings.md`
- `sector-energy-findings.md`

Bottom line:

- The new STDF `.claude` system is materially stronger as an execution shell. Its DAG, file contracts, shared rules, validation hooks, and reusable math libraries are the right long-term foundation.
- The old system still contains important capabilities that are not yet first-class in the new one. The biggest gaps are canonical sector modeling, intent/routing discipline, semantic QA, provenance/report lookup, and downstream business-output agents.
- Energy is the most successfully migrated area.
- Lithium and lead are partially migrated, but much of their business logic is still fragmented rather than encoded as a canonical sector engine.
- Copper has only generic commodity/STDF support in the new system; the old canonical four-bucket copper model is not yet represented directly.
- Artificial labor is the weakest migrated area. The old bottom-up simulation is far richer than anything presently encoded in the new STDF agents.

Recommended direction:

- Keep the new STDF orchestration and compliance stack.
- Promote legacy sector model logic into first-class sector engines inside the new STDF codebase.
- Restore the missing meta-layer from the old prompt system: intent routing, clarification, semantic review, provenance, and report retrieval.
- Treat agent memory as support material only, never as the system of record for business logic.
