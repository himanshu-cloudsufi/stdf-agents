# Plan 03: Custom Skills (`/stdf-run`, `/stdf-validate`, `/stdf-resume`)

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| Skill file at `.claude/skills/stdf-run.md` | INCORRECT | Must be `.claude/skills/stdf-run/SKILL.md` (subdirectory + SKILL.md) |
| `name`, `description` frontmatter | VERIFIED | |
| `disable-model-invocation: true` | VERIFIED | Also hides skill description from Claude's context entirely |
| `argument-hint` field | VERIFIED | Shown during autocomplete |
| `$ARGUMENTS` substitution | VERIFIED | Also supports `$0`, `$1` positional and `$ARGUMENTS[N]` indexed |
| `` !`command` `` dynamic injection | VERIFIED | Preprocessing — Claude only sees the output |
| `context: fork` | VERIFIED | Runs in isolated subagent with no conversation history |
| Multiple arguments via awk hack | WORKS but unnecessary | Use `$0`/`$1` positional syntax instead |
| `allowed-tools` field | NOT IN PLAN | Real field — restricts tools available to the skill |
| `model` field | NOT IN PLAN | Override model for a specific skill |
| `agent` field | NOT IN PLAN | Specify subagent type when `context: fork` is set |
| `user-invocable` field | NOT IN PLAN | Set `false` to hide from `/` menu |
| `${CLAUDE_SKILL_DIR}` variable | NOT IN PLAN | Resolves to skill's own directory |
| `hooks` field | NOT IN PLAN | Skill-scoped lifecycle hooks |

### Critical Structural Fix

Skills in `.claude/skills/` must use a **subdirectory structure**:
```
.claude/skills/stdf-run/SKILL.md      # CORRECT
.claude/skills/stdf-run.md            # INCORRECT
```

The flat-file convention (`.md` directly in directory) only works in `.claude/commands/`. The `.claude/skills/` directory requires each skill to be a folder containing `SKILL.md`.

## What We Get

- **One-command pipeline launch** — `/stdf-run electric vehicles` kicks off the full 6-agent pipeline
- **Post-run compliance audit** — `/stdf-validate energy-storage` scans all output files and produces a VALIDATION.md report
- **Mid-pipeline recovery** — `/stdf-resume energy-storage tipping-point` picks up from a specific phase using existing output files
- **Dynamic data injection** — skills pre-query the curves catalog so agents start with relevant empirical data
- **Consistent invocation** — no need to remember the full pipeline prompt; skills encapsulate the orchestration logic

## How We Do This

### Skill 1: `/stdf-run`

**File:** `.claude/skills/stdf-run/SKILL.md`

```markdown
---
name: stdf-run
description: Run a complete STDF disruption analysis pipeline. Use when asked to analyze a sector disruption.
disable-model-invocation: true
argument-hint: [sector or technology to analyze]
---

Execute the full STDF v2 pipeline for: $ARGUMENTS

Available empirical data for this sector:
!`./scripts/lookup_curves --query "$ARGUMENTS" --detail 2>/dev/null | head -50`

Follow the pipeline steps in CLAUDE.md exactly:
1. Derive analysis slug from the query (lowercase, hyphens)
2. Create output directory: `output/<slug>/agents/`
3. Launch Phase 1 agents in parallel (domain-disruption, cost-curve, capability)
4. Verify Phase 1 outputs, check for failures
5. Launch Phase 2: tipping-point (reads Phase 1 files)
6. Launch Phase 3: adoption-scurve (reads Phase 1 + Phase 2 files)
7. Launch synthesizer (reads all 5 files)
8. Write README.md index
9. Present results to user
```

Key features:
- `disable-model-invocation: true` — only runs when user types `/stdf-run`; skill description is also hidden from Claude's context entirely (saves tokens)
- `` !`command` `` syntax is preprocessing — Claude only sees the output, not the command
- `$ARGUMENTS` passes the user's full input after `/stdf-run`

### Skill 2: `/stdf-validate`

**File:** `.claude/skills/stdf-validate/SKILL.md`

```markdown
---
name: stdf-validate
description: Validate a completed STDF pipeline run for compliance violations and structural issues.
disable-model-invocation: true
argument-hint: [analysis-slug, e.g., energy-storage]
context: fork
allowed-tools: Read, Grep, Glob, Write
---

Validate the STDF pipeline run at `output/$ARGUMENTS/`.

Read each agent output file in `output/$ARGUMENTS/agents/` and check:

1. **Structural completeness**: All 6 agent files exist (01 through 06)
2. **Required sections**: Each file has `## Agent Reasoning`, `## Agent Output`, `## Sources`
3. **Metadata present**: Each file has `**Agent:**` and `**Confidence:**` fields
4. **Banned vocabulary**: Scan all files for forbidden terms
5. **Cost-curve CRITICAL criteria**: 2.1 (3+ data points, 5+ years) and 2.5 (service-level units) marked PASS
6. **Capability CRITICAL criteria**: 3.1 (3+ dimensions) and 3.2 (historical trajectories) present
7. **Tipping-point CRITICAL criteria**: 5.1 (explicit year/range) and 5.2 (3 conditions checked)
8. **Adoption CRITICAL criteria**: 4.1 (S-curve model, no linear extrapolation)
9. **Cross-agent consistency**: Tipping year in 04 aligns with cost parity year in 02
10. **Source coverage**: Each agent cites at least 3 sources

Write results to `output/$ARGUMENTS/VALIDATION.md` with:
- Overall PASS/FAIL status
- Per-agent compliance table
- List of specific violations with file path and line reference
- Recommendations for re-running failed agents
```

Key features:
- `context: fork` — runs in isolated subagent with no conversation history; verbose output stays contained
- `allowed-tools: Read, Grep, Glob, Write` — restricts forked subagent to only these tools (no web, no bash)
- **Important**: `context: fork` requires explicit task instructions — guidelines alone without a task produce empty output

### Skill 3: `/stdf-resume`

**File:** `.claude/skills/stdf-resume/SKILL.md`

```markdown
---
name: stdf-resume
description: Resume an STDF pipeline from a specific phase using existing output files.
disable-model-invocation: true
argument-hint: [analysis-slug] [phase: domain|cost-curve|capability|tipping-point|adoption|synthesizer]
---

Resume the STDF pipeline for slug `$0`, starting from phase `$1`.

Check which output files already exist in `output/$0/agents/`:
!`ls -la output/$0/agents/ 2>/dev/null`

Resume rules:
- If resuming from `tipping-point`: Phase 1 files (01, 02, 03) must exist. Run Phase 2 onward.
- If resuming from `adoption`: Files 01-04 must exist. Run Phase 3 onward.
- If resuming from `synthesizer`: Files 01-05 must exist. Run synthesizer only.
- If resuming from `domain`, `cost-curve`, or `capability`: Re-run that specific Phase 1 agent, then continue from Phase 2 onward.

Follow the same pipeline logic as CLAUDE.md but skip completed phases.
```

Key features:
- Uses `$0` and `$1` positional argument syntax (official documented approach) instead of fragile `awk` parsing
- `` !`ls` `` pre-injects existing file listing so Claude knows what's already complete

### Skill 4: `/stdf-catalog`

**File:** `.claude/skills/stdf-catalog/SKILL.md`

```markdown
---
name: stdf-catalog
description: Query the STDF curves catalog for available empirical data on a sector or technology.
disable-model-invocation: true
argument-hint: [sector, type, or search query]
context: fork
allowed-tools: Bash(./scripts/lookup_curves *)
---

Query the curves catalog for: $ARGUMENTS

!`./scripts/lookup_curves --query "$ARGUMENTS" --detail 2>/dev/null`

Available sectors:
!`./scripts/lookup_curves --list-sectors 2>/dev/null`

Summarize what data is available, covering:
- Number of matching curves by type (cost, adoption, capability, etc.)
- Time ranges covered
- Regions available
- Key data gaps that would require web research
```

Key features:
- `allowed-tools: Bash(./scripts/lookup_curves *)` — scopes Bash permission to only the lookup script
- `context: fork` — isolates verbose catalog output from main conversation

## Additional Frontmatter Fields Available

These verified fields can enhance skills further:

| Field | Type | Use Case |
|-------|------|----------|
| `allowed-tools` | comma-separated string | Restrict tool access for forked skills |
| `model` | string | Override model (e.g., `haiku` for lightweight catalog queries) |
| `agent` | string | Specify subagent type with `context: fork` (can reference custom agents from `.claude/agents/`) |
| `user-invocable: false` | boolean | Hide from `/` menu; still loadable by Claude automatically |
| `hooks` | YAML map | Skill-scoped lifecycle hooks |

### Built-in Variables

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | Full argument string after skill name |
| `$0`, `$1`, `$2`... | Positional arguments (0-indexed) |
| `$ARGUMENTS[N]` | Indexed access (equivalent to `$N`) |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing this SKILL.md file |

## Directory Structure (Corrected)

```
.claude/skills/
  stdf-run/
    SKILL.md
  stdf-validate/
    SKILL.md
  stdf-resume/
    SKILL.md
  stdf-catalog/
    SKILL.md
```

**NOT** flat files like `.claude/skills/stdf-run.md`.

## Implementation Steps

1. Create subdirectories: `mkdir -p .claude/skills/{stdf-run,stdf-validate,stdf-resume,stdf-catalog}`
2. Write `SKILL.md` in each subdirectory
3. Test each skill:
   - `/stdf-run lab-grown meat` — verify full pipeline launches
   - `/stdf-validate energy-storage` — verify against an existing run
   - `/stdf-resume energy-storage synthesizer` — verify partial re-run
   - `/stdf-catalog "Energy Storage"` — verify catalog query
4. Verify `$ARGUMENTS` expands correctly inside `` !`...` `` commands (may need testing)

## Dependencies

- `./scripts/lookup_curves` must be executable (already exists)
- Existing pipeline orchestration logic in CLAUDE.md (already exists)
