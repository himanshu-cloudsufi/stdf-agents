# Plan 04: Subagent Frontmatter Enhancements

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| Agent files in `.claude/agents/` | VERIFIED | Correct location, Priority 2 discovery |
| `maxTurns` field (camelCase) | VERIFIED | Caps agentic turns; no range guidance in docs |
| `permissionMode` values | VERIFIED | Full enum: `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `mcpServers: []` suppresses inherited servers | UNVERIFIED | Docs show how to ADD servers, not suppress inherited ones |
| `skills` field injects content | VERIFIED | Full skill content injected at startup; agents don't inherit parent skills |
| Hooks in agent frontmatter | VERIFIED | All hook events supported; `Stop` auto-converts to `SubagentStop` |
| `memory: project` scope | VERIFIED | Stores at `.claude/agent-memory/<name>/`; 200-line MEMORY.md loaded |
| `model: sonnet` valid | VERIFIED | Also: `opus`, `haiku`, `default`, `sonnet[1m]`, `opus[1m]`, `opusplan`, `inherit`, full IDs |
| `tools` comma-separated string | VERIFIED | Frontmatter uses string; CLI `--agents` uses JSON array |
| Hook commands with relative paths | INCORRECT | Use absolute paths — cwd may reset between bash calls |
| `disallowedTools` field | NOT IN PLAN | Real field — denylist complement to `tools` |
| `background` field | NOT IN PLAN | Always run as background task |
| `isolation` field | NOT IN PLAN | Set to `worktree` for git worktree isolation |
| `description` field | NOT IN PLAN | Required field alongside `name` |

### Critical Findings

1. **`mcpServers: []` may not suppress inherited servers.** The docs document adding servers to subagents, not removing inherited ones. The field might simply mean "add nothing extra" while inherited servers remain. **Must test before relying on this.** Alternative: use `disallowedTools` to deny specific MCP tools by name (format: `mcp__<server>__<tool>`).

2. **Hook command paths must be absolute.** Shell cwd can reset between bash calls in agent threads. Use absolute paths like `/Users/himanshuchauhan/TONY/STDF/stdf-agents/scripts/hooks/validate_cost_curve.sh`.

3. **`permissionMode` caveat**: If the parent session uses `bypassPermissions`, it takes precedence and cannot be overridden by a more restrictive subagent mode.

## What We Get

- **No runaway agents** — `maxTurns` caps each agent at a fixed number of turns, preventing infinite research loops that burn tokens
- **Fully headless execution** — `permissionMode: bypassPermissions` eliminates all permission prompts for CI/CLI pipeline runs
- **Reduced context overhead** — removing irrelevant MCP tool descriptions frees ~2-4K tokens per agent
- **Pre-loaded compliance context** — `skills` field injects compliance rules directly into agent context at startup

## How We Do This

### Change 1: Add `maxTurns` to All Agents

Prevents agents from entering unbounded research loops. Recommended values based on agent complexity:

| Agent | maxTurns | Rationale |
|-------|----------|-----------|
| stdf-domain-disruption | 50 | Broad research, multiple sectors |
| stdf-cost-curve | 60 | Empirical data lookup + curve fitting computation |
| stdf-capability | 50 | Multi-dimensional comparison |
| stdf-tipping-point | 40 | Synthesis of existing data, less research needed |
| stdf-adoption-scurve | 50 | S-curve fitting + regional breakdown |
| stdf-synthesizer | 40 | Reads and merges, minimal new research |

### Change 2: Add `permissionMode` Per Agent

Full enum of valid values:

| Value | Behavior |
|-------|----------|
| `default` | Standard permission checking with prompts |
| `acceptEdits` | Auto-accept file edits |
| `dontAsk` | Auto-deny permission prompts (explicitly allowed tools still work) |
| `bypassPermissions` | Skip all permission checks |
| `plan` | Plan mode (read-only exploration) |

Assignment:
- **Research agents** (domain, cost-curve, capability): `permissionMode: bypassPermissions`
  - These need WebSearch, WebFetch, Bash (python3), Read, Write
- **Synthesis agents** (tipping-point, adoption, synthesizer): `permissionMode: acceptEdits`
  - These primarily read upstream files and write output — less risky

**Caveat**: If the parent session uses `bypassPermissions`, this takes precedence over any subagent mode.

### Change 3: Handle MCP Server Scoping

**Original approach (`mcpServers: []`) is unverified.** Two strategies:

**Strategy A — Test `mcpServers: []` first:**
```yaml
mcpServers: []
```
Run an agent and check if Figma/Gmail/Atlassian tools still appear. If they don't, this works.

**Strategy B — Use `disallowedTools` as fallback:**
```yaml
disallowedTools: mcp__claude_ai_Figma__get_design_context, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Atlassian__search, mcp__claude_ai_Atlassian__getJiraIssue
```
This is more verbose but documented to work — it explicitly denies specific MCP tools by name.

**Strategy C — Combine both:**
```yaml
mcpServers: []
disallowedTools: mcp__claude_ai_Figma__*, mcp__claude_ai_Atlassian__*
```
Belt and suspenders. Check if glob patterns work in `disallowedTools`.

### Change 4: Preload Skills into Agents

Create a shared compliance skill (note: must use subdirectory structure per Plan 03):

**Create** `.claude/skills/stdf-compliance-rules/SKILL.md`:
```markdown
---
name: stdf-compliance-rules
description: STDF compliance rules for all agents
user-invocable: false
---

## Banned Vocabulary
Never use: transition, renewable energy, net zero, green, sustainable,
hydrogen economy, Wright's Law, IEA, EIA, BNEF, OPEC, clean energy, decarbonization

## Required Vocabulary
Use: disruption, stellar energy, cost-curve dynamics, market-driven disruption,
incumbent displacement, S-curve adoption

## Output Format
Every output MUST include:
- `## Agent Reasoning` (2-4 paragraphs)
- `## Agent Output` (structured markdown with tables)
- `## Sources` (bulleted list, minimum 3 sources)
```

Note: `user-invocable: false` hides from `/` menu since this skill is only meant to be injected into agents, not invoked directly.

Then in each agent frontmatter:
```yaml
skills:
  - stdf-compliance-rules
```

**Important**: Subagents don't inherit skills from the parent conversation — you must list them explicitly in frontmatter.

### Change 5: Add `description` Field (Required)

The `description` field is required alongside `name`. Add a concise description to each agent that matches the agent type description used in the Agent tool.

### Complete Frontmatter Reference

All supported fields for agent `.md` files:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | Yes | string | Agent identifier |
| `description` | Yes | string | What the agent does (used for agent selection) |
| `model` | No | string | `sonnet`, `opus`, `haiku`, `default`, `sonnet[1m]`, `opus[1m]`, `opusplan`, `inherit`, or full model ID |
| `tools` | No | comma-separated string | Allowed tools |
| `disallowedTools` | No | comma-separated string | Denied tools (denylist) |
| `permissionMode` | No | enum | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | integer | Max agentic turns before stop |
| `skills` | No | YAML list | Skills whose content is injected at startup |
| `mcpServers` | No | YAML list | MCP servers (string refs or inline defs) |
| `hooks` | No | YAML map | Agent-scoped lifecycle hooks |
| `memory` | No | enum | `user`, `project`, `local` |
| `color` | No | string | UI cosmetic color |
| `background` | No | boolean | Always run as background task |
| `isolation` | No | `worktree` | Git worktree isolation |

### Example: Corrected stdf-cost-curve.md Frontmatter

Before:
```yaml
---
name: stdf-cost-curve
model: sonnet
memory: project
tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, NotebookEdit
---
```

After:
```yaml
---
name: stdf-cost-curve
description: "Analyze cost dynamics of disruptive vs incumbent technologies. Build historical cost trajectories, derive learning rates, identify competitive thresholds."
model: sonnet
color: orange
memory: project
maxTurns: 60
permissionMode: bypassPermissions
mcpServers: []
disallowedTools: mcp__claude_ai_Figma__get_design_context, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Atlassian__search
skills:
  - stdf-compliance-rules
tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, NotebookEdit
hooks:
  PostToolUse:
    - matcher: "Write"
      hooks:
        - type: command
          command: "/Users/himanshuchauhan/TONY/STDF/stdf-agents/scripts/hooks/validate_cost_curve.sh"
---
```

**Key corrections:**
1. Added `description` (required field)
2. Hook command uses **absolute path** (not relative `./scripts/...`)
3. Added `disallowedTools` as fallback for MCP scoping
4. Added `mcpServers: []` (needs testing)
5. `Stop` hooks in frontmatter auto-convert to `SubagentStop` — no need to add explicitly

### Implementation Steps

1. Create `.claude/skills/stdf-compliance-rules/SKILL.md` shared skill
2. **Test `mcpServers: []`** with one agent before rolling out — verify inherited MCP tools are actually suppressed
3. Update all 6 agent `.md` files with new frontmatter fields
4. Test with a single agent: `claude -p "Run stdf-cost-curve for energy storage"` — verify:
   - No permission prompts
   - maxTurns respected
   - MCP tools absent from context
   - Compliance skill content present
5. Run full pipeline in headless mode to verify end-to-end

## Files to Create

```
.claude/skills/stdf-compliance-rules/SKILL.md
```

## Files to Modify

```
.claude/agents/stdf-domain-disruption.md    — add description, maxTurns, permissionMode, mcpServers, disallowedTools, skills
.claude/agents/stdf-cost-curve.md           — add description, maxTurns, permissionMode, mcpServers, disallowedTools, skills, hooks
.claude/agents/stdf-capability.md           — add description, maxTurns, permissionMode, mcpServers, disallowedTools, skills
.claude/agents/stdf-tipping-point.md        — add description, maxTurns, permissionMode, mcpServers, disallowedTools, skills
.claude/agents/stdf-adoption-scurve.md      — add description, maxTurns, permissionMode, mcpServers, disallowedTools, skills
.claude/agents/stdf-synthesizer.md          — add description, maxTurns, permissionMode, skills (keep MCP access for potential Figma)
```

## Dependencies

- Plan 01 (Hooks) for agent-level hooks in frontmatter
- Plan 03 (Skills) for the shared compliance skill — must use subdirectory structure
