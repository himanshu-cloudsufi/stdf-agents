# Plan 10: Agent Memory System Best Practices

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `memory: project` works in agent frontmatter | VERIFIED | Three scopes: `user`, `project`, `local` |
| Path `.claude/agent-memory/<name>/` for project | VERIFIED | Correct for `project` scope |
| MEMORY.md loaded at session start, 200 lines | VERIFIED | Content beyond line 200 is literally not loaded |
| Topic files loaded on demand | VERIFIED | NOT auto-loaded — agent must actively Read them |
| Agents get Read/Write/Edit tools for memory | VERIFIED | Automatic when `memory:` is set — no manual tool config |
| Agents can create new memory files | VERIFIED | Write tool is auto-enabled |
| Memory persists across invocations | VERIFIED | Shared via filesystem, not context |
| `local` scope exists | NOT IN PLAN | Stores at `.claude/agent-memory-local/<name>/` (not committed to git) |
| Main session memory vs subagent memory | NOT IN PLAN | Different systems: `~/.claude/projects/` vs `.claude/agent-memory/` |
| Memory files have special frontmatter | NOT APPLICABLE | Memory files are plain markdown — no special frontmatter |

### Key Clarifications

1. **Topic files require active Read tool calls** — they are NOT injected at startup. Only the first 200 lines of MEMORY.md are auto-loaded. This makes the "Memory Protocol" instructions in agent definitions load-bearing.
2. **Three scopes exist**, not one: `user` (global across projects), `project` (project-specific, in git), `local` (project-specific, NOT in git). Plan uses `project` correctly.
3. **Each subagent invocation creates a fresh context window** — memory is shared via filesystem, not via a shared context. The agent must actively read topic files.
4. **Main session auto-memory** (`~/.claude/projects/<project>/memory/`) is a completely separate system from subagent memory (`.claude/agent-memory/<name>/`).

## What We Get

- **Institutional knowledge across runs** — agents remember reliable data sources, validated learning rates, sector-specific patterns
- **Faster subsequent runs** — agents skip failed data sources and go directly to ones that worked before
- **Calibrated confidence** — agents adjust confidence based on historical accuracy patterns
- **Cross-sector pattern recognition** — agents notice when disruption patterns in one sector mirror another
- **Reduced hallucination** — memory of validated data points prevents agents from inventing numbers

## How We Do This

### Step 1: Create MEMORY.md Index for Each Agent

Each agent gets a structured `MEMORY.md` that's auto-loaded at session start (first 200 lines only — keep it concise):

**`.claude/agent-memory/stdf-cost-curve/MEMORY.md`**
```markdown
# Cost Curve Agent Memory

## Validated Data Sources
- [cost_sources.md](./cost_sources.md) — Reliable data sources per sector with quality ratings

## Empirical Learning Rates
- [learning_rates.md](./learning_rates.md) — Learning rates derived from past analyses with data basis

## Conversion Factors
- [unit_conversions.md](./unit_conversions.md) — Hardware-to-service-level unit conversion factors

## Known Data Gaps
- [data_gaps.md](./data_gaps.md) — Sectors/technologies where catalog data is insufficient
```

**`.claude/agent-memory/stdf-domain-disruption/MEMORY.md`**
```markdown
# Domain Disruption Agent Memory

## Sector Knowledge
- [sector_patterns.md](./sector_patterns.md) — Disruption patterns observed across sectors

## Convergence Combinations
- [convergence.md](./convergence.md) — Validated convergence combinations from past analyses

## Disruptor Taxonomy
- [disruptors.md](./disruptors.md) — Named disruptor technologies with status and maturity
```

**`.claude/agent-memory/stdf-capability/MEMORY.md`**
```markdown
# Capability Agent Memory

## Performance Benchmarks
- [benchmarks.md](./benchmarks.md) — Validated performance data points per technology

## Dimension Templates
- [dimensions.md](./dimensions.md) — Commonly used capability dimensions per sector

## Threshold Patterns
- [thresholds.md](./thresholds.md) — Capability thresholds that indicate market readiness
```

**`.claude/agent-memory/stdf-adoption-scurve/MEMORY.md`**
```markdown
# Adoption S-Curve Agent Memory

## Fitted Parameters
- [scurve_params.md](./scurve_params.md) — S-curve parameters (L, k, x0) from past analyses

## Regional Dynamics
- [regional_patterns.md](./regional_patterns.md) — Region-specific adoption patterns and lead/lag

## Market Share Baselines
- [market_baselines.md](./market_baselines.md) — Current market share data points by sector/region
```

**`.claude/agent-memory/stdf-tipping-point/MEMORY.md`**
```markdown
# Tipping Point Agent Memory

## Binding Constraints
- [binding_constraints.md](./binding_constraints.md) — Which tipping condition is typically binding per sector

## Regional Sequences
- [regional_tipping.md](./regional_tipping.md) — Typical order of regional tipping (China first, etc.)

## Convergence Acceleration
- [convergence_effects.md](./convergence_effects.md) — How convergence affects tipping timeline
```

**`.claude/agent-memory/stdf-synthesizer/MEMORY.md`**
```markdown
# Synthesizer Agent Memory

## Narrative Structures
- [narrative_patterns.md](./narrative_patterns.md) — Effective 7-phase narrative structures by sector

## Confidence Calibration
- [confidence_calibration.md](./confidence_calibration.md) — Historical confidence vs actual accuracy

## Subagent Conflicts
- [conflict_patterns.md](./conflict_patterns.md) — Common disagreements between subagents and resolution
```

### Step 2: Update Agent Definitions with Memory Protocol (Corrected)

Add to each agent's prompt in `.claude/agents/stdf-*.md`:

```markdown
## Memory Protocol

**At session start (automatic):** The first 200 lines of your MEMORY.md are
pre-loaded into your context. Topic files are NOT loaded automatically.

**Before starting your analysis:**
1. Review the pre-loaded MEMORY.md index (already in your context)
2. Use the Read tool to read any topic files relevant to the current
   sector/technology (e.g., read `learning_rates.md` for cost-curve work)
3. Use remembered data sources, learning rates, and patterns as starting
   points — do not re-research what is already validated

**After completing your analysis:**
1. If you discovered a new reliable data source, update the relevant topic
   file (e.g., `cost_sources.md`)
2. If you computed a new learning rate or benchmark, append it to the
   appropriate topic file with date and source
3. If you encountered a data gap, log it in `data_gaps.md`
4. If MEMORY.md exceeds 200 lines, move detail into topic files and keep
   MEMORY.md as a concise index

**Memory update quality bar:**
- Good: "BloombergNEF 2025: Li-ion pack cost $92/kWh (2024 actual, USA)"
- Bad: "Battery costs are declining" (too vague, derivable from any source)
- Good: "China EV adoption S-curve fit: L=0.85, k=0.42, x0=2024.3 (R²=0.97)"
- Bad: "China has high EV adoption" (no parameters, not reusable)
```

**Critical**: The instruction to "Read any topic files" is load-bearing — without it, topic files are never loaded.

### Step 3: Seed Initial Memory

Pre-populate memory files with knowledge from existing pipeline runs:

For cost-curve agent, seed `learning_rates.md`:
```markdown
# Empirical Learning Rates

| Technology | Learning Rate | Data Basis | Source | Date Validated |
|-----------|--------------|------------|--------|----------------|
| Lithium-ion batteries | 18-20% | 1991-2024, curves_catalog | Multiple sources | 2026-03 |
| Solar PV modules | 23-24% | 1976-2024, curves_catalog | Farmer & Lafond | 2026-03 |
| Wind turbines | 12-15% | 2000-2024, curves_catalog | IRENA data | 2026-03 |
```

### Step 4: Memory Hygiene Rules

Add to CLAUDE.md:
```markdown
## Agent Memory Rules
- Agents MUST read their memory topic files before starting analysis
- Agents MUST update memory after completing analysis
- Memory files use structured markdown (tables preferred for data)
- Memory entries include date validated and source
- Stale entries (>6 months) should be re-validated or removed
- Never store raw analysis outputs in memory — only reusable facts
- MEMORY.md is an index only — keep it well under 200 lines
- Use `local` scope for data that should not be committed to git
```

### Step 5: Memory Scope Reference

| Scope | Storage Path | In Git? | Use When |
|-------|-------------|---------|----------|
| `project` | `.claude/agent-memory/<name>/` | Yes | Project-specific knowledge, shareable with team |
| `user` | `~/.claude/agent-memory/<name>/` | No | Cross-project knowledge (personal) |
| `local` | `.claude/agent-memory-local/<name>/` | No | Project-specific but private (API keys, draft notes) |

For STDF agents, `project` is correct — memory should be versioned and shared.

### Step 6: Distinguish from Main Session Memory

| System | What It Is | Storage |
|--------|-----------|---------|
| Main session auto-memory | Claude's own notes from conversations | `~/.claude/projects/<project>/memory/MEMORY.md` |
| Subagent persistent memory | Per-agent knowledge base | `.claude/agent-memory/<name>/` (project scope) |

These are entirely separate systems. This plan addresses only subagent memory.

## Files to Create

```
.claude/agent-memory/stdf-cost-curve/MEMORY.md
.claude/agent-memory/stdf-cost-curve/cost_sources.md (seed)
.claude/agent-memory/stdf-cost-curve/learning_rates.md (seed)
.claude/agent-memory/stdf-cost-curve/unit_conversions.md (seed)
.claude/agent-memory/stdf-cost-curve/data_gaps.md

.claude/agent-memory/stdf-domain-disruption/MEMORY.md
.claude/agent-memory/stdf-domain-disruption/sector_patterns.md
.claude/agent-memory/stdf-domain-disruption/convergence.md
.claude/agent-memory/stdf-domain-disruption/disruptors.md

.claude/agent-memory/stdf-capability/MEMORY.md
.claude/agent-memory/stdf-capability/benchmarks.md
.claude/agent-memory/stdf-capability/dimensions.md
.claude/agent-memory/stdf-capability/thresholds.md

.claude/agent-memory/stdf-adoption-scurve/MEMORY.md
.claude/agent-memory/stdf-adoption-scurve/scurve_params.md
.claude/agent-memory/stdf-adoption-scurve/regional_patterns.md
.claude/agent-memory/stdf-adoption-scurve/market_baselines.md

.claude/agent-memory/stdf-tipping-point/MEMORY.md
.claude/agent-memory/stdf-tipping-point/binding_constraints.md
.claude/agent-memory/stdf-tipping-point/regional_tipping.md
.claude/agent-memory/stdf-tipping-point/convergence_effects.md

.claude/agent-memory/stdf-synthesizer/MEMORY.md
.claude/agent-memory/stdf-synthesizer/narrative_patterns.md
.claude/agent-memory/stdf-synthesizer/confidence_calibration.md
.claude/agent-memory/stdf-synthesizer/conflict_patterns.md
```

## Files to Modify

```
.claude/agents/stdf-cost-curve.md           — add Memory Protocol section
.claude/agents/stdf-domain-disruption.md    — add Memory Protocol section
.claude/agents/stdf-capability.md           — add Memory Protocol section
.claude/agents/stdf-adoption-scurve.md      — add Memory Protocol section
.claude/agents/stdf-tipping-point.md        — add Memory Protocol section
.claude/agents/stdf-synthesizer.md          — add Memory Protocol section
CLAUDE.md                                    — add Agent Memory Rules section
```

## Dependencies

- `memory: project` already set in agent frontmatter (existing)
- Memory seeding benefits from having at least one completed pipeline run
- Read/Write/Edit tools are auto-enabled — no manual configuration needed
