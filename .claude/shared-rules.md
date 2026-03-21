# STDF Shared Agent Rules

**All STDF agents must read this file at the start of every run.** These rules apply uniformly across all agents in the pipeline.

## Companion Files
- `.claude/shared-glossary.md` — STDF concept definitions (read by all agents)
- `.claude/shared-cost-rules.md` — Cost analysis rules (read by cost-chain agents)

---

## Banned Vocabulary

Never use these terms anywhere in your output:

| Banned Term | Use Instead |
|---|---|
| transition | "disruption" |
| renewable energy | "stellar energy" or name the specific technology (solar PV, wind) |
| net zero | Omit; frame in terms of cost-curve superiority |
| green | Omit |
| sustainable / sustainability | Omit |
| hydrogen economy | Specify production method and its cost curve |
| Wright's Law | "cost-curve dynamics" or "learning rate" with specific percentage |
| IEA / EIA / BNEF / OPEC | Permitted ONLY for historical observed data with [CAUTION: {org} source] tag — see Banned Organization Policy below |
| clean energy | Name the specific technology |
| decarbonization | "displacement of fossil-fuel incumbents" or name the specific disruption |
| base case / bull case / bear case | Parameter value label (e.g., L=85%) |
| optimistic scenario / pessimistic scenario | Parameter sensitivity range |
| best case / worst case | Parameter value label |
| AI capability growth | "AI capability improvement" |

## Required Vocabulary

Use these terms consistently:
- **disruption** (not "transition")
- **stellar energy** (not "renewable energy") when referring to the category
- **cost-curve dynamics** (not "Wright's Law")
- **market-driven disruption** (not policy-driven narratives)
- **incumbent displacement** (not "phase-out" or "retirement")
- **S-curve adoption** (not "linear growth" or "gradual adoption")

## Date Awareness

Your prompt includes an **Analysis date: YYYY-MM-DD**. This is your temporal anchor:
- Data BEFORE this date = historical (observed, citable)
- Data AFTER this date = projected/forecast (NOT citable from web sources)
- When citing data, tag as [observed] or [model-derived]
- NEVER present projected web data as observed fact

## Web Search Guardrails

### Historical-Only Rule (STRICT)
Web search gathers ONLY observed, historical data from primary sources.
After EVERY WebSearch/WebFetch, evaluate BEFORE using any data:
1. Is the data point OBSERVED or FORECASTED?
2. Is the timestamp BEFORE the analysis date?
3. Is the source a primary data publisher (government, peer-reviewed, official registry)?
If ANY check fails → DISCARD the data point and note it in Data Gaps.

### Forecast Ban (CRITICAL GUARDRAIL)
REJECT web results containing: "forecast", "projected", "outlook", "expected to
reach", "will reach", "estimated to reach" when paired with future-dated claims.
Your OWN model-derived projections (exponential decay, S-curve fits) from
historical data are permitted — third-party forecasts are NOT.

## Data Source Hierarchy (STRICT)

For cost, adoption, and capability data:

**Tier 1 (HIGHEST): Published Reports** — government statistical agencies,
peer-reviewed publications, official industry body reports with named methodology.
**Tier 2: Local Data Catalog** (data/ directory) — curated, validated, with provenance.
**Tier 3 (LOWEST): Web Search** — historical only, gap-filling, NO forecasts.

Tag every data point: [T1: source], [T2: catalog-file.json], [T3: url, retrieved YYYY-MM-DD]
If tiers conflict: higher tier wins; note discrepancy in Data Gaps.

## Citation Standards

Every numerical data point MUST include:
- **Source name** (organization or publication)
- **Year of data** (year described, not publication year)
- **Data type tag:** [observed] or [model-derived]
- **URL** + retrieval date (for web sources)

In-table: `Source Name (year) [observed] | url`
In-text: "value (Source, year [observed])"

## Core Analytical Guardrails

- **NO linear extrapolation.** Disruption follows S-curves, not straight lines.
- **NO narrative without numbers.** Every analytical claim must be grounded in quantitative evidence.
- **NO ESG framing.** Disruptions succeed because of cost superiority, not environmental goals.
- **NO policy-driven narratives.** Cost-curve dynamics drive adoption, not mandates.

## Context-Dependent Rules

### Jevons Paradox
- **X-Flow technologies** (physical resource throughput): Jevons Paradox MAY be referenced. Tag: "demand elasticity via Jevons effect (X-Flow)".
- **Stellar technologies** (solar, wind, battery, AI/AL): Jevons Paradox MUST NOT be used.
- **Gate:** The /stdf skill classification step assigns each technology an X-Flow/Stellar/Hybrid tag. Downstream agents check this tag.

**Where to find the tag:** Read `01-domain-disruption.md` section `## Classification Overrides`. Each technology is tagged with `X-Flow`, `Stellar`, or `Hybrid`.

**Fallback behavior:** If the `## Classification Overrides` section is missing (e.g., Phase 1 hard gate was skipped), the agent MUST self-classify based on the technology's characteristics — X-Flow if it has physical resource throughput, Stellar if it has zero marginal cost characteristics — and emit `[WARNING: Jevons classification not found in upstream — self-classified as {tag}]` in the output.

**Propagation rule:** Every downstream agent that may reference Jevons (capability, xcurve-analyst, tipping-synthesizer, stream-forecaster, demand-decomposer) MUST read the classification tag before applying or excluding Jevons. Never assume the classification — always check.

### Banned Organization Policy (IEA, EIA, BNEF, OPEC)
Permitted ONLY under ALL conditions:
1. Data is OBSERVED and HISTORICAL (not a forecast/scenario)
2. Tagged with `[CAUTION: {org} source — historical data only]`
3. Primary government source was searched first and not found
4. Data point is NOT used as basis for forward projections
If ANY condition fails → DISCARD the data point.

## Data-Type Tagging (MANDATORY)

Every numerical value must be tagged `[observed]` or `[model-derived]`.

**By format:**
- **Prose/narrative:** Tag inline: "86.4% [model-derived]"
- **Tables — ALL values same type:** Header annotation: `**All values: [model-derived] from upstream S-curve parameters**`
- **Tables — mixed types:** Add a `Data Type` column as last column

Self-check: before writing output, verify no tables or prose with future-year numbers lack data-type tags.

---

## Computation Rules (MANDATORY)

### Rule 1: Never Estimate by Hand
**ALL numerical computation MUST use `Bash` with `python3`.** Never estimate, approximate, or "eyeball" a number. If you need a number, compute it. If you catch yourself writing "approximately" or "roughly" for a derived value, stop and write python3 code instead.

### Rule 2: Use `lib/` Functions First
Before writing inline python3, check if a pre-built function exists in `lib/`. These are tested, validated, and produce consistent outputs across agents.

**Discovery**: Run this to see available functions for your task:
```bash
python3 -c "import lib.<module>; help(lib.<module>)"
```

**Library map — which agent uses which lib:**

| Agent | Primary Library | Key Functions |
|-------|----------------|---------------|
| cost-researcher | `lib.data_catalog` | `search_curves`, `find_cost_curves`, `get_xy_data` |
| cost-fitter | `lib.cost_curve_math` | `exponential_fit`, `learning_rate_from_decay`, `competitive_threshold`, `inflection_threshold`, `convert_*` |
| capability | `lib.capability_math` | `fit_trajectory`, `threshold_check`, `parity_year_estimate`, `convergence_pattern` |
| capability-parity-checker | `lib.capability_math` | `threshold_check`, `parity_year_estimate` |
| cost-parity-checker | `lib.tipping_math` | `check_tipping_conditions` |
| tipping-synthesizer | `lib.tipping_math` | `check_tipping_conditions`, `completion_timeline_from_scurve`, `confidence_aggregate`, `regional_tipping_assessment` |
| scurve-fitter | `lib.scurve_math` | `fit_scurve`, `project_scurve`, `classify_phase`, `completion_year` |
| regional-adopter | `lib.scurve_math` | `fit_scurve`, `classify_phase` |
| xcurve-analyst | `lib.scurve_math` | `xcurve_decline` |
| demand-decomposer | `lib.demand_math` | `decompose_demand`, `material_intensity_demand` |
| stream-forecaster | `lib.demand_math` | `project_demand_from_scurve`, `aggregate_demand_by_technology` |
| fleet-modeler | `lib.demand_math` | `stock_flow_fleet`, `oem_replacement_split`, `validate_stock_flow_consistency` |
| regional-demand-analyst | `lib.demand_math` | `regional_demand_split` |
| ALL downstream agents | `lib.upstream_reader` | `read_upstream`, `get_cost_trajectory`, `get_scurve_parameters`, `get_capability_dimensions` |
| ALL agents | `lib.compliance` | `create_checklist`, `checklist_to_markdown`, `has_critical_failure` |
| ALL agents | `lib.output_writer` | `build_agent_output`, `table_to_markdown` |

### Rule 3: When to Write Inline python3

Write inline `python3 -c "..."` via Bash ONLY when:
- No `lib/` function covers your specific calculation
- You need a one-off computation (e.g., unit conversion not in `lib.cost_curve_math`)
- You're combining outputs from multiple lib functions in a custom way

Always import from `lib/` first, then add custom logic on top:
```bash
python3 -c "
from lib.cost_curve_math import exponential_fit, competitive_threshold
from lib.scurve_math import fit_scurve
# ... your custom computation using lib functions
"
```

### Rule 4: Always Report Fit Quality
Any curve fitting (exponential, logistic, linear) MUST report:
- **R-squared** (or equivalent goodness-of-fit metric)
- **Number of data points** used
- **Year span** of the data
- If R² < 0.8, flag in Data Gaps as low-confidence fit

---

## Pre-Output Self-Check (MANDATORY)

Before writing your output file, run this validation:
```bash
python3 -c "
from lib.vocabulary import scan_banned, vocabulary_report
text = open('<your-output-file>').read()
report = vocabulary_report(text)
print(report)
"
```
Fix ALL violations before writing. A Claude Code hook will BLOCK your write
if banned terms, banned source URLs, or forecast language are detected.

---

## Persistent Agent Memory

You have a persistent, file-based memory system. **Your memory directory path is specified in your agent definition file** — look for the `**Agent memory directory**` line. Write to it directly with the Write tool (do not run mkdir or check for its existence).

You should build up this memory system over time so that future conversations can have a complete picture of who the user is, how they'd like to collaborate with you, what behaviors to avoid or repeat, and the context behind the work the user gives you.

If the user explicitly asks you to remember something, save it immediately as whichever type fits best. If they ask you to forget something, find and remove the relevant entry.

### Types of memory

There are several discrete types of memory that you can store in your memory system:

<types>
<type>
    <name>user</name>
    <description>Contain information about the user's role, goals, responsibilities, and knowledge. Great user memories help you tailor your future behavior to the user's preferences and perspective. Your goal in reading and writing these memories is to build up an understanding of who the user is and how you can be most helpful to them specifically. For example, you should collaborate with a senior software engineer differently than a student who is coding for the very first time. Keep in mind, that the aim here is to be helpful to the user. Avoid writing memories about the user that could be viewed as a negative judgement or that are not relevant to the work you're trying to accomplish together.</description>
    <when_to_save>When you learn any details about the user's role, preferences, responsibilities, or knowledge</when_to_save>
    <how_to_use>When your work should be informed by the user's profile or perspective. For example, if the user is asking you to explain a part of the code, you should answer that question in a way that is tailored to the specific details that they will find most valuable or that helps them build their mental model in relation to domain knowledge they already have.</how_to_use>
    <examples>
    user: I'm a data scientist investigating what logging we have in place
    assistant: [saves user memory: user is a data scientist, currently focused on observability/logging]

    user: I've been writing Go for ten years but this is my first time touching the React side of this repo
    assistant: [saves user memory: deep Go expertise, new to React and this project's frontend — frame frontend explanations in terms of backend analogues]
    </examples>
</type>
<type>
    <name>feedback</name>
    <description>Guidance or correction the user has given you. These are a very important type of memory to read and write as they allow you to remain coherent and responsive to the way you should approach work in the project. Without these memories, you will repeat the same mistakes and the user will have to correct you over and over.</description>
    <when_to_save>Any time the user corrects or asks for changes to your approach in a way that could be applicable to future conversations – especially if this feedback is surprising or not obvious from the code. These often take the form of "no not that, instead do...", "lets not...", "don't...". when possible, make sure these memories include why the user gave you this feedback so that you know when to apply it later.</when_to_save>
    <how_to_use>Let these memories guide your behavior so that the user does not need to offer the same guidance twice.</how_to_use>
    <body_structure>Lead with the rule itself, then a **Why:** line (the reason the user gave — often a past incident or strong preference) and a **How to apply:** line (when/where this guidance kicks in). Knowing *why* lets you judge edge cases instead of blindly following the rule.</body_structure>
    <examples>
    user: don't mock the database in these tests — we got burned last quarter when mocked tests passed but the prod migration failed
    assistant: [saves feedback memory: integration tests must hit a real database, not mocks. Reason: prior incident where mock/prod divergence masked a broken migration]

    user: stop summarizing what you just did at the end of every response, I can read the diff
    assistant: [saves feedback memory: this user wants terse responses with no trailing summaries]
    </examples>
</type>
<type>
    <name>project</name>
    <description>Information that you learn about ongoing work, goals, initiatives, bugs, or incidents within the project that is not otherwise derivable from the code or git history. Project memories help you understand the broader context and motivation behind the work the user is doing within this working directory.</description>
    <when_to_save>When you learn who is doing what, why, or by when. These states change relatively quickly so try to keep your understanding of this up to date. Always convert relative dates in user messages to absolute dates when saving (e.g., "Thursday" → "2026-03-05"), so the memory remains interpretable after time passes.</when_to_save>
    <how_to_use>Use these memories to more fully understand the details and nuance behind the user's request and make better informed suggestions.</how_to_use>
    <body_structure>Lead with the fact or decision, then a **Why:** line (the motivation — often a constraint, deadline, or stakeholder ask) and a **How to apply:** line (how this should shape your suggestions). Project memories decay fast, so the why helps future-you judge whether the memory is still load-bearing.</body_structure>
    <examples>
    user: we're freezing all non-critical merges after Thursday — mobile team is cutting a release branch
    assistant: [saves project memory: merge freeze begins 2026-03-05 for mobile release cut. Flag any non-critical PR work scheduled after that date]

    user: the reason we're ripping out the old auth middleware is that legal flagged it for storing session tokens in a way that doesn't meet the new compliance requirements
    assistant: [saves project memory: auth middleware rewrite is driven by legal/compliance requirements around session token storage, not tech-debt cleanup — scope decisions should favor compliance over ergonomics]
    </examples>
</type>
<type>
    <name>reference</name>
    <description>Stores pointers to where information can be found in external systems. These memories allow you to remember where to look to find up-to-date information outside of the project directory.</description>
    <when_to_save>When you learn about resources in external systems and their purpose. For example, that bugs are tracked in a specific project in Linear or that feedback can be found in a specific Slack channel.</when_to_save>
    <how_to_use>When the user references an external system or information that may be in an external system.</how_to_use>
    <examples>
    user: check the Linear project "INGEST" if you want context on these tickets, that's where we track all pipeline bugs
    assistant: [saves reference memory: pipeline bugs are tracked in Linear project "INGEST"]

    user: the Grafana board at grafana.internal/d/api-latency is what oncall watches — if you're touching request handling, that's the thing that'll page someone
    assistant: [saves reference memory: grafana.internal/d/api-latency is the oncall latency dashboard — check it when editing request-path code]
    </examples>
</type>
</types>

### What NOT to save in memory

- Code patterns, conventions, architecture, file paths, or project structure — these can be derived by reading the current project state.
- Git history, recent changes, or who-changed-what — `git log` / `git blame` are authoritative.
- Debugging solutions or fix recipes — the fix is in the code; the commit message has the context.
- Anything already documented in CLAUDE.md files.
- Ephemeral task details: in-progress work, temporary state, current conversation context.

### How to save memories

Saving a memory is a two-step process:

**Step 1** — write the memory to its own file (e.g., `user_role.md`, `feedback_testing.md`) using this frontmatter format:

```markdown
---
name: {{memory name}}
description: {{one-line description — used to decide relevance in future conversations, so be specific}}
type: {{user, feedback, project, reference}}
---

{{memory content — for feedback/project types, structure as: rule/fact, then **Why:** and **How to apply:** lines}}
```

**Step 2** — add a pointer to that file in `MEMORY.md`. `MEMORY.md` is an index, not a memory — it should contain only links to memory files with brief descriptions. It has no frontmatter. Never write memory content directly into `MEMORY.md`.

- `MEMORY.md` is always loaded into your conversation context — lines after 200 will be truncated, so keep the index concise
- Keep the name, description, and type fields in memory files up-to-date with the content
- Organize memory semantically by topic, not chronologically
- Update or remove memories that turn out to be wrong or outdated
- Do not write duplicate memories. First check if there is an existing memory you can update before writing a new one.

### When to access memories
- When specific known memories seem relevant to the task at hand.
- When the user seems to be referring to work you may have done in a prior conversation.
- You MUST access memory when the user explicitly asks you to check your memory, recall, or remember.

### Memory and other forms of persistence
Memory is one of several persistence mechanisms available to you as you assist the user in a given conversation. The distinction is often that memory can be recalled in future conversations and should not be used for persisting information that is only useful within the scope of the current conversation.
- When to use or update a plan instead of memory: If you are about to start a non-trivial implementation task and would like to reach alignment with the user on your approach you should use a Plan rather than saving this information to memory. Similarly, if you already have a plan within the conversation and you have changed your approach persist that change by updating the plan rather than saving a memory.
- When to use or update tasks instead of memory: When you need to break your work in current conversation into discrete steps or keep track of your progress use tasks instead of saving to memory. Tasks are great for persisting information about the work that needs to be done in the current conversation, but memory should be reserved for information that will be useful in future conversations.

- Since this memory is project-scope and shared with your team via version control, tailor your memories to this project

### MEMORY.md

Your MEMORY.md is currently empty. When you save new memories, they will appear here.
