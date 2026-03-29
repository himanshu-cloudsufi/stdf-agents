# STDF Pipeline Gotchas

Common failure modes that are easy to miss during orchestration. Read this before your first pipeline run.

## CRITICAL agent failure MUST stop the pipeline

If a CRITICAL agent (cost-researcher, cost-fitter, tipping-synthesizer, demand-decomposer, synthesizer) fails, you MUST stop the entire pipeline. Do not try to work around it, do not substitute with a different agent, do not continue with "partial results." Report the failure to the user and stop.

## Date format must be YYYY-MM-DD

The analysis date MUST be formatted as `YYYY-MM-DD` (e.g., `2026-03-19`). Other formats (`March 19, 2026`, `03/19/2026`, `19-03-2026`) will cause guardrail false positives — the date consistency checker won't match them correctly, and the hooks may block writes.

## Upstream files must exist before launching dependent agents

Never assume an upstream file was written — verify it exists before launching a dependent agent. If Tier 1 completes but one agent's output file is missing (e.g., the agent wrote to the wrong path), Tier 2 will silently read nothing and produce garbage.

Quick check between tiers:
```bash
ls output/{SLUG}/agents/
```

## Synthesizer needs ALL produced files in UPSTREAM_FILES

The synthesizer's `UPSTREAM_FILES:` must list every output file that was actually produced — not just the "goal agents" but all intermediate outputs too. If you skip listing `02a-cost-researcher.md` because "it's just intermediate data," the synthesizer will have an incomplete picture.

## Commodity chain (Tier 6) is conditional

Only launch Tier 6 agents if the chosen preset is `FULL+COMMODITY`. If you launch `demand-decomposer` on a FULL preset, it will run but waste time and the synthesizer won't expect its output.

## Don't default to FULL — present the detected preset

When using AskUserQuestion, present the auto-detected preset as "(Recommended)." If the query says "quick overview," recommend QUICK — don't default to FULL because "more is better." Overrunning the user's intent wastes time and money.

## Agent subagent_type matches agent name

Every agent's `subagent_type` is identical to its name: `stdf-cost-fitter` → `subagent_type: "stdf-cost-fitter"`. No mapping table needed.

## Guardrail validation is a soft audit

The Step 4 validation script is informational — it runs AFTER all agents have written. The real enforcement happens via PreToolUse hooks that block writes containing banned vocabulary. If Step 4 reports violations, it means a hook was not active or was bypassed.

## Empty output files silently pass validation

An agent may create a file but write nothing to it. The guardrail checker won't flag an empty file as a violation. After each tier, check file sizes — not just file existence.

## Phase 1 hard gate is context-dependent

After Tier 1, the orchestrator decides whether to pause for user classification approval based on scope and risk:

**MANDATORY** for: FULL, ENERGY_FULL, ENERGY_GAS, FULL+COMMODITY, CUSTOM with 8+ agents, ambiguous sectors, or when domain-disruption lacks flow classification.

**OPTIONAL** for: QUICK, COST_FOCUS, CUSTOM with 5 or fewer agents where sector/flow/metric/market are all unambiguous from the query.

When skipping the gate, the orchestrator must state its reasoning (e.g., "Solar PV Stellar classification is unambiguous for a cost-only analysis").

**Risk of skipping:** Misclassification propagates through the pipeline. For FULL runs, wrong flow type (X-Flow vs Stellar) changes Jevons Paradox applicability in 5+ downstream agents. For QUICK runs, the blast radius is limited to cost-fitter and synthesizer.

## User Overrides propagate downstream

If 01-domain-disruption.md has a `## User Overrides` section, ALL downstream agents must check for it. The synthesizer MUST reference overrides in its narrative.

## Re-run scope on override

Only re-run cost-researcher and capability if the override changes the disruptor/incumbent definition. Flow type, cost metric, and market type changes do NOT require Phase 1 re-run.

## Jevons Paradox: never apply to Stellar technologies

Jevons Paradox (efficiency gains increasing total resource consumption) applies ONLY to X-Flow technologies (physical resource throughput like copper, lead, aluminium). For Stellar technologies (solar, wind, battery, AI/AL), efficiency gains do NOT rebound into increased resource consumption — the marginal cost of the resource approaches zero. If an agent references Jevons for a Stellar technology, the output is analytically incorrect. Check the `## Classification Overrides` section in `01-domain-disruption.md` for the tag.

## Banned Org Policy: IEA/BNEF needs CAUTION tag or hook blocks write

Inline mentions of IEA, BNEF, EIA, or OPEC in agent output are flagged as violations by `lib/vocabulary.py` UNLESS the same line contains a `[CAUTION: {org} ...]` tag. URLs (iea.org, bnef.com, etc.) are ALWAYS violations regardless of tagging. If you see a hook block on write due to "banned source," check whether the agent added the CAUTION tag.

## Data-type tags: check future-year tables have annotations

Every table containing future-year numbers (post-analysis-date) must have either:
- A header annotation: `**All values: [model-derived] from ...**` (for uniform tables)
- A `Data Type` column as the last column (for mixed observed/model-derived tables)

The `validate_data_type_tags()` guardrail catches untagged future-year numbers. If the Step 4 validation flags "untagged_projection" warnings, the agent needs to add data-type annotations.

## Energy agents (Tier 7) are conditional like commodity agents

Only launch energy-dispatch and gas-supply-decomposer if the preset is ENERGY_FULL or ENERGY_GAS. Their absence on non-energy queries is normal, not a degradation. Tier 6 (commodity) and Tier 7 (energy) can run in parallel when both triggered — no cross-dependencies.

## Marginal cost, not LCOE, for incumbent dispatch

The energy-dispatch agent uses marginal cost for fossil fuel dispatch ordering. LCOE includes sunk capital costs. If you see LCOE being used for merit order comparison, the analysis is structurally wrong — the tipping point will be incorrect by several years.

## China solar CF is 0.11, not 0.17

When converting solar $/Wp to $/kWh for China, use CF=0.11 (BNEF). The commonly cited 0.17 is a global average and produces a 55% underestimate of $/kWh service cost. This has been a recurring error in prior analyses.

## X-Flow/Stellar classification must propagate to downstream agents

The X-Flow/Stellar/Hybrid classification is set in `01-domain-disruption.md` `## Classification Overrides` during the Phase 1 hard gate. Every downstream agent that references Jevons Paradox (capability, xcurve-analyst, tipping-synthesizer, stream-forecaster, demand-decomposer) MUST read this tag before applying or excluding Jevons. If the tag is missing, agents should self-classify and emit a `[WARNING]`. A missing tag is a pipeline smell — check whether the Phase 1 hard gate was skipped.

## Research agent output must be included in synthesizer UPSTREAM_FILES

If the orchestrator injected `stdf-research` during the pipeline, its output files (`09-research-*.md`) must be listed in the synthesizer's UPSTREAM_FILES. The synthesizer will not find them on its own — it only reads files explicitly listed. After all research agents complete, verify their output files exist before launching the synthesizer and include them in the file list.

## Custom agent sets still need DAG resolution

When the orchestrator constructs a CUSTOM agent set (not matching any known configuration), it must still resolve the full dependency chain from the Agent Registry. Do not assume that listing goal agents is sufficient — walk the "Requires" column for every goal agent and add all transitive dependencies. Missing a dependency (e.g., forgetting cost-researcher when including cost-fitter) will cause the dependent agent to read a nonexistent upstream file.
