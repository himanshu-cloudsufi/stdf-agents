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
