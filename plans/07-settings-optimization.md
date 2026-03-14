# Plan 07: Settings & Configuration Optimization

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` env var | VERIFIED | Default 95%, set lower to compact earlier |
| `BASH_DEFAULT_TIMEOUT_MS` env var | UNVERIFIED | Not found in official docs — may not exist |
| `BASH_MAX_TIMEOUT_MS` env var | UNVERIFIED | Not found in official docs — may not exist |
| `permissions.allow` block in settings.json | VERIFIED | Schema: `deny` → `ask` → `allow` evaluation order |
| `Bash(python3 *)` permission pattern | VERIFIED | Prefix matching with space before `*` |
| `Write(output/**)` permission | INCORRECT | `Write` is not a valid permission tool — use `Edit` |
| `cleanupPeriodDays` setting | VERIFIED | Top-level key, default 30 days, 0 = disable persistence |
| `plansDirectory` setting | VERIFIED | Top-level key, path relative to project root |
| Settings at `.claude/settings.json` | VERIFIED | Project scope, shared via git |
| Settings precedence hierarchy | VERIFIED | managed > CLI > local > project > user |
| `CLAUDE_CODE_SUBAGENT_MODEL` env var | VERIFIED | Pins model for all subagents |
| `CLAUDE_CODE_ENABLE_TASKS` env var | UNVERIFIED | Not found in official docs |

### Critical Corrections

1. **`Write(output/**)` is invalid** — `Write` is not a recognized tool in the permission system. Use `Edit(output/**)` for file edits. The `Edit` permission rule covers all built-in file-editing tools.
2. **`BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` are unverified** — removed from the corrected settings. For long-running scripts, use `--dangerously-skip-permissions` in headless mode or structure scripts to run faster.
3. **`CLAUDE_CODE_ENABLE_TASKS` is unverified** — removed from corrected settings.
4. **Array settings merge across scopes** — project `permissions.allow` entries are concatenated with user-level entries, not replacing them.

## What We Get

- **No mid-analysis context compaction** — agents compact at 75% instead of 95%, preventing loss of upstream context
- **Pre-approved permissions** — headless pipeline runs proceed without interactive prompts
- **Consistent environment** — all pipeline configuration centralized in project settings
- **Longer session retention** — pipeline run history available for 90 days for audit and replay
- **Plans directory** — pipeline plans stored in project `./plans` folder

## How We Do This

### Change 1: Context Compaction Threshold

**Problem**: Agents hitting 95% context capacity trigger compaction mid-analysis, losing important upstream context.

**Fix**: Set earlier compaction trigger:
```json
{
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75"
  }
}
```

### Change 2: Pre-Approved Permissions

**Problem**: Interactive permission prompts block headless pipeline execution.

**Fix**: Add specific permission allowances. Evaluation order is `deny` → `ask` → `allow` (first match wins):
```json
{
  "permissions": {
    "allow": [
      "Bash(python3 *)",
      "Bash(./scripts/lookup_curves *)",
      "Bash(mkdir *)",
      "Bash(ls *)",
      "Edit(output/**)",
      "Read(output/**)",
      "Read(curves_catalog.json)",
      "Read(.claude/**)",
      "WebSearch",
      "WebFetch"
    ]
  }
}
```

**Permission pattern reference:**
| Pattern | Matches |
|---------|---------|
| `Bash(python3 *)` | Any bash command starting with `python3 ` |
| `Edit(output/**)` | Edit any file recursively under `output/` |
| `Read(.claude/**)` | Read any file under `.claude/` |
| `WebSearch` | All web search calls (no parens = match all) |

**Note**: `Write` is NOT a valid permission tool name. Use `Edit` which covers all file-editing tools.

### Change 3: Session Retention

Keep pipeline session history longer for audit:
```json
{
  "cleanupPeriodDays": 90
}
```
Default is 30. Setting to `0` deletes all transcripts at startup and disables persistence entirely.

### Change 4: Plans Directory

Point plan files to the project plans folder:
```json
{
  "plansDirectory": "./plans"
}
```
Path is relative to project root. Default is `~/.claude/plans`.

### Change 5: Pipeline Environment Variables

```json
{
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75",
    "STDF_OUTPUT_DIR": "./output",
    "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
  }
}
```

`CLAUDE_CODE_SUBAGENT_MODEL` pins all STDF subagents to Sonnet explicitly, matching agent definitions.

### Combined Settings Update

Final `.claude/settings.json` additions (merged with existing settings):

```json
{
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75",
    "STDF_OUTPUT_DIR": "./output",
    "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
  },
  "permissions": {
    "allow": [
      "Bash(python3 *)",
      "Bash(./scripts/lookup_curves *)",
      "Bash(mkdir *)",
      "Bash(ls *)",
      "Edit(output/**)",
      "Read(output/**)",
      "Read(curves_catalog.json)",
      "Read(.claude/**)",
      "WebSearch",
      "WebFetch"
    ]
  },
  "cleanupPeriodDays": 90,
  "plansDirectory": "./plans"
}
```

### Settings File Locations (Precedence)

| File | Scope | Priority |
|------|-------|----------|
| `managed-settings.json` (system) | Managed — cannot be overridden | Highest |
| CLI flags | Session overrides | |
| `.claude/settings.local.json` | Local project — personal, gitignored | |
| `.claude/settings.json` | **Project — shared via git** (target) | |
| `~/.claude/settings.json` | User — personal global | Lowest |

**Important**: Array settings (like `permissions.allow`) **merge across scopes** — project entries concatenate with user-level entries, they don't replace them.

### Handling Long-Running Bash Commands

Since `BASH_DEFAULT_TIMEOUT_MS` is unverified, alternatives for long-running python3 scripts:

1. **`--dangerously-skip-permissions` in headless mode** — bypasses all timeouts/prompts (isolated environments only)
2. **Structure scripts to run faster** — break curve fitting into smaller chunks, cache intermediate results
3. **Use `timeout` parameter in Bash tool calls** — individual calls can set timeout up to 600000ms (10 min)
4. **Background execution** — use `run_in_background: true` in Bash tool calls for non-blocking execution

### Implementation Steps

1. Read current `.claude/settings.json` to understand existing config
2. Merge new settings without overwriting existing values
3. Test headless run: `claude -p "Run stdf-cost-curve for energy storage"` — verify no permission prompts
4. Test long-running script: run a python3 curve fitting script — verify it completes within tool timeout

## Files to Modify

```
.claude/settings.json  — merge new env vars, permissions, and config
```

## Dependencies

- None — standalone configuration changes
- Benefits all other plans (hooks, skills, subagent enhancements)
