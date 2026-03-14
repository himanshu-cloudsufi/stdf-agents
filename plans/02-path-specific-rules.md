# Plan 02: Path-Specific Rules (`.claude/rules/`)

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `.claude/rules/` is a real feature | VERIFIED | Fully documented, files discovered recursively |
| `paths:` frontmatter field | VERIFIED | Exact YAML list syntax correct |
| Glob pattern matching for paths | VERIFIED | Glob only, no regex. Brace expansion supported (`*.{ts,tsx}`) |
| Rules load when **editing** matching files | INCORRECT | Trigger is **reading** a matching file, not writing/editing |
| `description:` frontmatter field | NOT SUPPORTED | Not documented; only `paths:` is a recognized key — remove it |
| Always-loaded vs path-scoped distinction | VERIFIED | Rules without `paths:` load unconditionally at session start |
| Rules supplement CLAUDE.md (additive) | VERIFIED | No override mechanism; additive system |
| Symlink support | VERIFIED (not in original plan) | `.claude/rules/` supports symlinks for cross-project sharing |
| User-level rules at `~/.claude/rules/` | VERIFIED (not in original plan) | Personal rules apply to all projects on machine |

### CRITICAL Design Issue Found

**Path-scoped rules trigger when Claude READS a matching file, NOT when it writes/edits.** The original plan assumed rules would fire when agents write output files like `output/*/agents/02-cost-curve.md`. Since STDF agents write these files but don't read them in the same session, **the path-scoped compliance rules would never trigger automatically**.

## Corrected Strategy

Given the read-trigger behavior, we use a **hybrid approach**:

1. **Always-loaded rules** for universal compliance (banned vocab, output format) — reliable, always in context
2. **Agent-definition-scoped rules** for per-agent compliance — scope rules to `.claude/agents/stdf-*.md` paths, which agents DO read at startup
3. **Reserve path-scoped rules** for downstream validation scenarios (e.g., tipping-point reads cost-curve output, triggering cost-curve validation rules)

## What We Get

- **Reduced token overhead** — compliance criteria split across focused rule files instead of one giant CLAUDE.md
- **Cleaner CLAUDE.md** — move ~40% of compliance detail into dedicated rule files
- **Automatic enforcement** — always-loaded rules ensure banned vocab and output format are always in context
- **Cross-project sharing** — symlink support lets us share STDF rules across multiple analysis projects
- **Downstream validation** — when tipping-point agent reads cost-curve output, cost-curve compliance rules load automatically

## How We Do This

### Step 1: Create the Rules Directory

```
.claude/rules/
├── pipeline-conventions.md          # Always loaded — banned vocab, required vocab, output format
├── compliance-cost-curve.md         # Loaded when READING output/*/agents/02-cost-curve.md
├── compliance-capability.md         # Loaded when READING output/*/agents/03-capability.md
├── compliance-tipping-point.md      # Loaded when READING output/*/agents/04-tipping-point.md
├── compliance-adoption.md           # Loaded when READING output/*/agents/05-adoption-scurve.md
├── compliance-domain-disruption.md  # Loaded when READING output/*/agents/01-domain-disruption.md
└── compliance-synthesizer.md        # Loaded when READING output/*/agents/06-synthesizer.md
```

**Subdirectories supported** — you can organize as `.claude/rules/stdf/compliance-cost-curve.md` etc.

### Step 2: Write Always-Loaded Rules (No `paths:` frontmatter)

**`pipeline-conventions.md`** — no frontmatter needed, loads unconditionally:
```markdown
## Banned Vocabulary
Never use: transition, renewable energy, net zero, green, sustainable,
hydrogen economy, Wright's Law, IEA, EIA, BNEF, OPEC, clean energy, decarbonization

## Required Vocabulary
Use instead: disruption, stellar energy, cost-curve dynamics, market-driven disruption,
incumbent displacement, S-curve adoption

## Output Format
Every agent output file MUST contain:
- `# STDF [Agent Name] Agent — [Topic]`
- `**Agent:** [name] | **Confidence:** [score]`
- `## Agent Reasoning` (2-4 paragraphs)
- `## Agent Output` (structured markdown)
- `## Sources` (bulleted list)
```

**Note:** Do NOT include `description:` in frontmatter — it is not a documented field for rules files.

### Step 3: Write Path-Scoped Rules

These trigger when **downstream agents read** the matching output files. For example, when tipping-point reads `02-cost-curve.md`, cost-curve compliance rules load into context — enabling the downstream agent to validate upstream data quality.

**`compliance-cost-curve.md`**:
```markdown
---
paths:
  - "output/*/agents/02-cost-curve.md"
---

## Cost Curve Compliance Criteria

### CRITICAL (hard-fail if violated)
- 2.1: Historical disruptor cost trajectory with minimum 3 data points spanning 5+ years
- 2.5: All costs in service-level units ($/kWh, $/km, $/lumen-hour) — NEVER hardware units

### HIGH
- 2.2: Incumbent cost trajectory with minimum 2 data points
- 2.3: Exponential/power-law fit with R² reported
- 2.4: Learning rate derived from empirical data (not assumed)
- 2.6: Competitive threshold year identified

### Compliance Checklist
Output MUST include a `### Compliance Checklist` table with PASS/FAIL for each criterion.
```

Similar files for each agent. The path-scoped rules serve **double duty**:
- Downstream agents reading upstream output get compliance context for validating what they're reading
- The `/stdf-validate` skill (Plan 03) reads all output files, triggering ALL compliance rules

### Step 4: Embed Per-Agent Compliance in Agent Definitions

Since path-scoped rules won't trigger for the writing agent itself, embed CRITICAL compliance criteria directly in each agent's `.claude/agents/stdf-*.md` definition file. This is where agents get their own compliance rules — from their own definition, not from path-scoped rules.

This means compliance criteria exist in **two places**:
1. **Agent definition** (`.claude/agents/stdf-cost-curve.md`) — enforced during writing
2. **Path-scoped rule** (`.claude/rules/compliance-cost-curve.md`) — enforced during downstream reading/validation

### Step 5: Slim Down CLAUDE.md

Remove detailed per-agent compliance criteria from CLAUDE.md. Replace with:
```markdown
## Agent Compliance System
- Universal rules (banned vocab, output format): `.claude/rules/pipeline-conventions.md` (always loaded)
- Per-agent CRITICAL criteria: embedded in `.claude/agents/stdf-*.md` definitions
- Downstream validation rules: `.claude/rules/compliance-*.md` (path-scoped, trigger on read)
```

### Step 6: Optional — Cross-Project Sharing via Symlinks

If you create multiple STDF analysis projects:
```bash
# Share rules across projects
ln -s ~/shared-stdf-rules .claude/rules/shared
```

### Step 7: Debug Rule Loading

Use the `InstructionsLoaded` hook (from Plan 01) to verify which rules loaded:
```json
{
  "hooks": {
    "InstructionsLoaded": [
      {
        "hooks": [
          { "type": "command", "command": "echo \"Rules loaded at $(date)\" >> /tmp/stdf-rules-debug.log" }
        ]
      }
    ]
  }
}
```

### Step 8: Test

- Run a single agent and verify always-loaded rules (banned vocab) appear in context
- Run tipping-point agent — when it reads `02-cost-curve.md`, verify cost-curve compliance rules load
- Run `/stdf-validate` — verify ALL path-scoped rules trigger as it reads each output file
- Confirm `description:` field is NOT used in any frontmatter

## Additional Features Discovered

### User-Level Rules (`~/.claude/rules/`)
Personal rules that apply to every project. Useful for user-specific conventions:
```
~/.claude/rules/
└── personal-conventions.md   # Your personal style/approach rules
```

### Excluding Rules (`claudeMdExcludes`)
In `settings.local.json`, exclude specific rules:
```json
{
  "claudeMdExcludes": ["compliance-synthesizer.md"]
}
```

### Glob Pattern Reference
| Pattern | Matches |
|---------|---------|
| `**/*.ts` | All TypeScript files in any directory |
| `src/**/*` | All files under `src/` |
| `output/*/agents/02-cost-curve.md` | Cost curve output in any analysis run |
| `*.{md,txt}` | Markdown and text files (brace expansion) |

## Files to Create

```
.claude/rules/
  pipeline-conventions.md             # Always loaded (no frontmatter)
  compliance-cost-curve.md            # Path-scoped to output/*/agents/02-cost-curve.md
  compliance-capability.md            # Path-scoped to output/*/agents/03-capability.md
  compliance-tipping-point.md         # Path-scoped to output/*/agents/04-tipping-point.md
  compliance-adoption.md              # Path-scoped to output/*/agents/05-adoption-scurve.md
  compliance-domain-disruption.md     # Path-scoped to output/*/agents/01-domain-disruption.md
  compliance-synthesizer.md           # Path-scoped to output/*/agents/06-synthesizer.md
```

## Files to Modify

- `CLAUDE.md` — slim down compliance section, point to rules directory
- `.claude/agents/stdf-*.md` — ensure CRITICAL compliance criteria are embedded in each agent definition

## Dependencies

- None — `.claude/rules/` is a built-in Claude Code feature
- Plan 01 (Hooks) for `InstructionsLoaded` debug hook (optional)
- Plan 03 (Skills) for `/stdf-validate` which triggers path-scoped rules via reads
