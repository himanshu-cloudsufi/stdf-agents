# General Findings

## Executive verdict

The new `.claude` STDF system is the better platform, but it is not yet a full replacement for the old stack.

What the new system gets right:

- Strong STDF-first decomposition into cost, capability, parity, adoption, tipping, demand, and synthesis stages.
- Cleaner execution semantics through a DAG-oriented orchestrator.
- Better operational discipline through shared rules, shared cost rules, validation skills, and a write-blocking hook.
- Reusable code libraries for math, energy, demand, tipping, compliance, and vocabulary enforcement.

What the old system still has that matters:

- Canonical sector engines with deterministic business logic for copper, artificial labor, and lithium/lead.
- Better meta-orchestration: intent reformulation, clarification gating, evaluator-style semantic review, citation building, trace explanation, and report lookup.
- Better productization for certain business questions, especially lead/lithium report answering and investment-style follow-on analysis.

The practical conclusion is straightforward:

- Do not replace the old sector models with generic STDF prompts yet.
- Do use the new STDF system as the target architecture.
- Port or directly integrate the old sector model logic before retiring the old sector skills.

## High-level comparison

| Layer | Old sector skills | Old prompt system | New `.claude` STDF system | Assessment |
| --- | --- | --- | --- | --- |
| Core numerical modeling | Strong for copper, artificial labor, lithium/lead | Weak to moderate, mostly orchestration/reporting | Strong generic STDF math, weaker sector-specific logic | Mixed |
| Orchestration | Narrow, skill-specific | Strong router/planner chain | Strong DAG execution | New system better |
| Intent routing | Minimal inside skills | Strong reformulator/planner split | Limited | Old prompt system better |
| Clarification handling | Minimal | Explicit clarification agent | Limited | Old prompt system better |
| Validation | Skill discipline, limited final QA | Evaluator pass with semantic checks | Strong structural compliance and hook-based validation | Split: new stronger structurally, old stronger semantically |
| Provenance/citations | Skill-specific explanations | Citation builder + trace explainer | Partial, mostly file-based and rule-based | Old prompt system better |
| Report retrieval | Present for lithium/lead via precomputed reports | Explicit report lookup agent | Missing as first-class capability | Old prompt system better |
| Sector coverage | Deep in select sectors | Broad but prompt-centric | Broad STDF primitives, uneven sector depth | Mixed |
| Business-output extensions | Low | Stronger: feedback loops, company, VCA, investing | Minimal | Old prompt system better |

## What to preserve from the old system

### 1. Skill sovereignty

The old stack had a sound principle: if a canonical skill existed, the orchestrator had to use it instead of silently re-deriving the answer in prompt logic. That rule prevented numerical drift and shadow models.

The new STDF system should preserve this principle in updated form:

- If a domain has a validated sector engine, the orchestrator must call it.
- Generic STDF agents should frame, synthesize, and extend results, not replace a validated sector model with free-form reasoning.
- Agent memory must not become a substitute for an actual sector engine.

### 2. Sector-specific business logic

The old sector skills encode business rules that are not optional details. They define the actual model. Those rules should be migrated into code, data, and tests inside the new STDF tree.

The most important retained business logic is:

- Copper: four-bucket decomposition, transport coefficients, grid generation logic, T&D logic, residual balancing, region-aware vehicle mix.
- Artificial labor: task/subtask taxonomy, capability gating, cost-parity tipping, adoption ceilings, replacement/productivity split, scenario controls, FTE-centric outputs.
- Lithium/lead: report-first base case retrieval, base plus TaaS overlay for lead, segment-by-segment demand trees, OEM versus replacement splits, B2C versus B2B parity logic, explicit exclusions such as not using LCOE/SCOE for BESS.

### 3. Productized answer modes

The old system knew how to answer business questions, not just run models. That included:

- Precomputed report retrieval for standard cases.
- Investment-oriented synthesis.
- Company-specific extensions.
- Feedback-loop framing.
- Trace/provenance explanation.

The new STDF system should add these back as downstream modules after core modeling, not mix them into the numerical core.

## What the new system already does better

### 1. STDF execution discipline

The new `stdf` skill has a clearer execution model than the old prompt stack:

- Tiered parallelizable DAG.
- Named presets for common analysis shapes.
- Stronger output contracts between stages.
- Better separation between domain classification, cost work, parity checks, adoption, downstream demand translation, and synthesis.

This is the correct long-term shell for STDF analysis.

### 2. Reusable computation libraries

The new system is closer to a real modeling platform because it contains shared modules for:

- Demand math
- Energy math
- Cost curve math
- Capability math
- Tipping math
- Compliance
- Vocabulary

This is where migrated sector logic should live.

### 3. Guardrails and validation

The new system is stricter about:

- Historical-only web usage
- Future-number tagging
- Explicit `[observed]` versus `[model-derived]`
- Banned forecast language
- Banned source usage rules
- Computation through `python3` rather than estimated arithmetic

These are material improvements and should stay.

## What is missing in the new system

### 1. Missing meta-agents

The following old capabilities do not have clear first-class replacements:

- Intent reformulation and routing
- Clarification gating
- Semantic evaluator/reviewer
- Citation/provenance builder
- Trace explainer
- Precomputed report lookup
- Feedback-loop analysis
- Investment/company/VCA extensions

### 2. Missing canonical sector engines

The new STDF agents are good at generic disruption analysis, but they do not yet encode the full canonical sector logic for:

- Artificial labor
- Copper
- Lithium/lead

That creates a risk that future answers will look STDF-consistent while drifting away from validated domain-specific model behavior.

### 3. Business logic living in the wrong place

Some sector knowledge appears to exist in agent memory or scattered prompt instructions rather than in:

- Versioned code
- Versioned data files
- Versioned tests
- Explicit output contracts

That is not durable enough for production-grade sector analysis.

## Recommended target architecture

### Core principle

Use the new STDF system as the orchestration and compliance backbone, but move all durable business logic into code and data assets inside the new repository.

### Recommended layers

#### Layer 1: Request shaping

Responsibilities:

- Reformulate user intent
- Detect sector and requested output type
- Decide whether clarification is required
- Select canonical sector engine or pure-STDF path

Implementation:

- Add a first-class routing agent or fold the logic into the orchestrator with a strict structured schema

#### Layer 2: Canonical modeling engines

Responsibilities:

- Sector-specific coefficients
- Taxonomies
- Rules that define what the model means
- Deterministic calculations

Implementation:

- Create first-class sector packages inside `stdf-agents/lib/sector/`
- Until fully ported, directly invoke the existing legacy model scripts as transitional canonical engines

#### Layer 3: STDF orchestration

Responsibilities:

- Cost/capability/tipping/adoption analysis
- Demand and stream decomposition
- Cross-sector synthesis
- File production and audit trail

Implementation:

- Keep the existing `.claude/skills/stdf` and agent DAG as the control plane

#### Layer 4: Validation and provenance

Responsibilities:

- Structural validation
- Semantic review
- Citation compilation
- Trace explanation

Implementation:

- Keep the new compliance and hook system
- Add back evaluator-style semantic QA and a provenance builder

#### Layer 5: Business-output modules

Responsibilities:

- Investment framing
- Company implications
- VCA views
- Feedback-loop views
- Report retrieval for standard questions

Implementation:

- Add downstream optional agents after the core analysis is complete

## Where business logic should live

Business logic should not sit primarily in prompts.

Recommended placement:

- Prompts and agent definitions: routing, workflow, output contracts, quality gates
- `lib/`: formulas, transition logic, calibration utilities, decompositions, sector math
- `data/` or `references/`: canonical parameters, taxonomy files, regional calibration data, precomputed report assets
- Tests: regression fixtures for known scenarios and sector outputs
- Agent memory: supporting notes only, never the canonical rule source

## Migration roadmap

### Phase 1: Close correctness gaps first

Priority:

- Add intent routing, clarification, semantic review, provenance, and report lookup
- Wire the new orchestrator to canonical sector engines for copper, artificial labor, and lithium/lead
- Prevent generic STDF-only answers from bypassing canonical sector logic when that logic exists

### Phase 2: Consolidate sector engines into the new codebase

Priority:

- Port legacy model logic into `stdf-agents/lib/sector/`
- Normalize data assets and parameter files
- Add tests that prove parity between old outputs and new integrated outputs
- Remove duplicate or dead sector paths after parity is achieved

### Phase 3: Rebuild downstream business modules

Priority:

- Feedback-loop analysis
- Investment and company-specific views
- VCA output mode
- Research delta and web-gap modules where still useful

## Priority ranking by sector

| Sector | Migration status | Risk if left as-is | Recommended priority |
| --- | --- | --- | --- |
| Artificial labor | Weakly migrated | Very high | Highest |
| Copper | Partially represented generically | High | High |
| Lithium/lead | Partially migrated | High | High |
| Energy | Largely migrated at STDF layer | Moderate | Medium |

## Final recommendation

The correct migration path is not "replace old with new." It is:

1. Keep the new STDF shell.
2. Reinstall the missing old meta-layer.
3. Move legacy sector business logic into first-class sector engines.
4. Retire duplicated legacy paths only after output parity and regression coverage exist.
