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

## Phase 1 hard gate is MANDATORY

After Tier 1, pause for user classification approval. Never skip this step. If domain-disruption lacks flow classification, the /stdf skill provides it. The gate presents disruption scope, cost parity metric, and market type for user confirmation before Tier 2 proceeds.

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

## X-Flow/Stellar classification must propagate to downstream agents

The X-Flow/Stellar/Hybrid classification is set in `01-domain-disruption.md` `## Classification Overrides` during the Phase 1 hard gate. Every downstream agent that references Jevons Paradox (capability, xcurve-analyst, tipping-synthesizer, stream-forecaster, demand-decomposer) MUST read this tag before applying or excluding Jevons. If the tag is missing, agents should self-classify and emit a `[WARNING]`. A missing tag is a pipeline smell — check whether the Phase 1 hard gate was skipped.
