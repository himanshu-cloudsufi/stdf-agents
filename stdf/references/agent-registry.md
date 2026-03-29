# Agent Registry — Dependency Graph & Tier Template

This file provides detailed dependency resolution information for the STDF pipeline orchestrator. The canonical Agent Registry table lives in CLAUDE.md — this file supplements it with execution details.

## Dependency Graph (Visual)

```
                    ┌─────────────────┐
                    │   User Query    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     domain-disruption  cost-researcher  capability
              │              │              │
              │              ▼              │
              │          cost-fitter        │
              │         ╱    │    ╲         │
              ▼        ▼     │     ▼        ▼
    adoption-readiness  cost-parity  capability-parity
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    tipping-synthesizer
                             │
                             ▼
                       scurve-fitter
                        ╱         ╲
                       ▼           ▼
             regional-adopter   xcurve-analyst
                    │
   ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─  (Tier 6 — conditional)
                    │
                    ▼
           demand-decomposer ←── scurve-fitter + domain-disruption
                    │
                    ▼
           stream-forecaster
                ╱         ╲
               ▼           ▼
        fleet-modeler   regional-demand-analyst ←── regional-adopter
                ╲         ╱
   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  (Tier 7 — conditional energy)
              energy-dispatch ←── cost-fitter + scurve-fitter + domain-disruption
                    │
                    ▼
        gas-supply-decomposer ←── domain-disruption
   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  (Flex — injected anywhere)
              research (no fixed tier — orchestrator inserts when data gaps are flagged)
   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
                    │
                    ▼
              synthesizer (always second-to-last)
                    │
                    ▼
              evaluator (Haiku — always last)
```

## Tier Execution Template

When building the execution plan, use this template. Delete tiers not needed by the chosen preset.

| Tier | Agents | Parallel? | Depends On |
|------|--------|-----------|------------|
| 1 | domain-disruption, cost-researcher, capability | Yes | — |
| 2 | cost-fitter | No | cost-researcher |
| 3 | cost-parity-checker, capability-parity-checker, adoption-readiness-checker | Yes | cost-fitter, capability, domain-disruption |
| 4 | tipping-synthesizer | No | all 3 checkers |
| 5a | scurve-fitter | No | tipping-synthesizer + cost-fitter |
| 5b | regional-adopter, xcurve-analyst | Yes | scurve-fitter |
| 6a | demand-decomposer | No | scurve-fitter + domain-disruption |
| 6b | stream-forecaster | No | demand-decomposer |
| 6c | fleet-modeler, regional-demand-analyst | Yes | stream-forecaster (+ regional-adopter for regional-demand) |
| 7a | energy-dispatch | No | cost-fitter + scurve-fitter + domain-disruption |
| 7b | gas-supply-decomposer | No | energy-dispatch + domain-disruption |
| Flex | research | No | varies (injected by orchestrator) |
| Final | synthesizer | No | all selected outputs |
| Eval | evaluator | No | synthesizer |

## Example Configurations

These configurations document agent sets that commonly result from reasoning about different query types. They are reference material, not the canonical selection mechanism. The orchestrator determines agent sets by reasoning from the query (see Orchestration Principles in CLAUDE.md), and the result may match one of these known configurations or may be a custom set.

**FULL** resolves to 12 agents (Tiers 1–5b + Final):
domain-disruption, cost-researcher, capability, cost-fitter, cost-parity-checker, capability-parity-checker, adoption-readiness-checker, tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, synthesizer

**QUICK** resolves to 3 agents (Tier 1 partial + Tier 2 + Final):
cost-researcher, cost-fitter, synthesizer

**TIPPING_ONLY** resolves to 9 agents (Tiers 1–4 + Final):
domain-disruption, cost-researcher, capability, cost-fitter, cost-parity-checker, capability-parity-checker, adoption-readiness-checker, tipping-synthesizer, synthesizer

**COST_FOCUS** resolves to 4 agents:
cost-researcher, capability, cost-fitter, synthesizer

**ADOPTION_FOCUS** resolves to 12 agents (same as FULL — adoption needs tipping first):
domain-disruption, cost-researcher, capability, cost-fitter, cost-parity-checker, capability-parity-checker, adoption-readiness-checker, tipping-synthesizer, scurve-fitter, regional-adopter, xcurve-analyst, synthesizer

**FULL+COMMODITY** adds 4 agents to FULL (16 total):
FULL agents + demand-decomposer, stream-forecaster, fleet-modeler, regional-demand-analyst

**ENERGY_FULL** adds 2 agents to FULL (14 total):
FULL agents + energy-dispatch, gas-supply-decomposer

**ENERGY_GAS** adds 2 agents to FULL (14 total):
FULL agents + energy-dispatch, gas-supply-decomposer

**CUSTOM** — queries that do not match any known configuration produce a custom agent set. The orchestrator labels these "CUSTOM" and lists the goal agents explicitly. Examples:
- Capability-only analysis: domain-disruption, cost-researcher, capability, capability-parity-checker, synthesizer (5 agents)
- Cost + tipping without adoption: domain-disruption, cost-researcher, capability, cost-fitter, cost-parity-checker, capability-parity-checker, adoption-readiness-checker, tipping-synthesizer, synthesizer (9 agents)

**Note:** Tier 6 (commodity) and Tier 7 (energy) can run in parallel when both triggered — no cross-dependencies.

---

## Flex Agent: stdf-research

The research agent has no fixed tier position. It is injected by the orchestrator between tiers when:
- A specialist agent flags a data gap the orchestrator considers important for downstream quality
- The query needs context outside any specialist's coverage (regulatory, geopolitical, supply chain)
- The user requests additional research on a specific topic

**Output:** `output/{slug}/agents/09-research-{topic-slug}.md`

**Dependencies:** Reads any upstream files as context. No agent depends on it by default, but its output is included in the synthesizer's UPSTREAM_FILES when present.

**Criticality:** MEDIUM (its absence is always acceptable — it is supplementary)
