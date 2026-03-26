# Plan 01: Hooks — Automated Compliance & Observability

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| PreToolUse, PostToolUse, SubagentStart/Stop, Stop, TaskCompleted events | VERIFIED | All real events |
| JSON schema format (3-level nesting) | VERIFIED | event → matcher groups → hooks array |
| Hook scripts receive stdin JSON | VERIFIED | Includes `tool_name`, `tool_input`, `session_id`, `cwd` |
| Exit code 0 = allow, 2 = block | PARTIALLY CORRECT | PreToolUse: exit 2 blocks. PostToolUse: exit 2 sends feedback (doesn't undo write) |
| `"background": true` async option | INCORRECT | Correct field is `"async": true` |
| Hooks in agent frontmatter | VERIFIED | All events supported; `Stop` auto-converts to `SubagentStop` |
| "prompt" type hooks | VERIFIED | Not in original plan; LLM-based validation is real |
| Matcher on TaskCompleted, Stop | SILENTLY IGNORED | Matcher is ignored for these events |
| Relative command paths | RISKY | Use `$CLAUDE_PROJECT_DIR/scripts/...` instead |
| Missing events: SessionStart, PostToolUseFailure, PreCompact, Notification | NOT IN PLAN | All real and useful |

### Critical Corrections

1. **`"background": true` does not exist** — the correct field is `"async": true`
2. **PostToolUse exit 2 does NOT prevent the write** — the tool already ran; exit 2 sends feedback to Claude asking it to fix and re-write
3. **PreToolUse exit 2 DOES block** — this is where you prevent bad writes from ever hitting disk
4. **Use `$CLAUDE_PROJECT_DIR`** in command paths, not relative `./scripts/...`
5. **Stdout must be clean JSON on exit 0** — shell profile output (`.bashrc`) will corrupt parsing

## What We Get

- **Zero banned vocabulary in agent outputs** — PreToolUse blocks writes containing forbidden terms before they hit disk
- **Structural validation** — PostToolUse checks output structure and sends feedback to Claude if sections are missing (Claude then rewrites)
- **CRITICAL compliance gates** — cost-curve agent gets feedback if criteria 2.1/2.5 aren't PASS
- **Per-agent timing data** — SubagentStart/Stop hooks record wall-clock duration to `timing.json`
- **Desktop notification** when pipeline finishes
- **Complete audit trail** — every tool call logged with timestamp, agent name, file path

## How We Do This

### Phase A: Create Hook Scripts

**1. Banned Vocabulary Enforcer** (`scripts/hooks/check_banned_vocab.sh`)
- Reads stdin JSON from PreToolUse event
- Extracts `tool_input.content` and `tool_input.file_path` from JSON
- Scans content against banned word list
- **Exit 0** = clean (stdout must be valid JSON or empty)
- **Exit 2** = blocked — stderr message is sent back to the agent with the specific violation
- Only fires on `Write` tool (via matcher)

**2. Output Structure Validator** (`scripts/hooks/validate_output_structure.sh`)
- Fires on PostToolUse (after write completes)
- Reads the written file path from stdin JSON
- Checks file contains required sections: `## Agent Reasoning`, `## Agent Output`, `## Sources`
- **Exit 0** = valid
- **Exit 2** = sends feedback to Claude (does NOT undo the write — Claude will re-write the file)
- Must be **synchronous** (no `async: true`) to provide feedback

**3. Cost-Curve Compliance Gate** (`scripts/hooks/validate_cost_curve.sh`)
- Agent-level PostToolUse hook (in stdf-cost-curve.md frontmatter)
- Parses `02-cost-curve.md` specifically
- Checks CRITICAL criteria 2.1 and 2.5
- Exit 2 sends feedback asking Claude to fix compliance issues

**4. Pipeline Timer** (`scripts/hooks/record_timing.py`)
- On SubagentStart: reads `agent_type` and `agent_id` from stdin JSON, writes start time
- On SubagentStop: reads `agent_type`, updates entry with end time and duration
- Uses file locking for parallel Phase 1 agents
- stdin includes `agent_type` field (e.g., `"stdf-cost-curve"`) for identification

**5. Completion Notifier** (`scripts/hooks/notify_complete.sh`)
- On Stop event: sends macOS notification via `osascript`
- Runs as `"async": true` (fire-and-forget, doesn't block)
- Must check `stop_hook_active` flag in stdin to prevent infinite loops

### Phase B: Configure Hooks in Settings

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash $CLAUDE_PROJECT_DIR/scripts/hooks/check_banned_vocab.sh",
            "timeout": 30,
            "statusMessage": "Checking for banned vocabulary..."
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash $CLAUDE_PROJECT_DIR/scripts/hooks/validate_output_structure.sh",
            "timeout": 30,
            "statusMessage": "Validating output structure..."
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/scripts/hooks/record_timing.py start"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/scripts/hooks/record_timing.py stop"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash $CLAUDE_PROJECT_DIR/scripts/hooks/notify_complete.sh",
            "async": true
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/scripts/hooks/check_task_output.py"
          }
        ]
      }
    ]
  }
}
```

### Hook Field Reference (Official Schema)

```json
{
  "type": "command",           // Required: "command", "prompt", or "agent"
  "command": "/path/to/script", // Required for type "command"
  "timeout": 30,               // Optional: seconds (default varies by event)
  "async": false,              // Optional: fire-and-forget (default false)
  "statusMessage": "..."       // Optional: shown in UI while running
}
```

### Exit Code Reference

| Context | Exit 0 | Exit 2 | Other non-zero |
|---------|--------|--------|----------------|
| **PreToolUse** | Allow (read stdout JSON) | **Block tool execution**, stderr sent to Claude | Non-blocking error, stderr in verbose only |
| **PostToolUse** | Success (read stdout JSON) | **Send feedback to Claude** (tool already ran, write NOT undone) | Non-blocking error |
| **TaskCompleted** | Allow task completion | **Block completion**, stderr sent to agent | Non-blocking error |
| **SubagentStart** | Allow | Block agent start | Non-blocking error |

**Critical rule**: On exit 2, all stdout JSON is ignored. Choose one signaling method — exit codes OR exit 0 + JSON, never both.

### Phase C: Add Agent-Level Hooks in Frontmatter

Add to `.claude/agents/stdf-cost-curve.md` frontmatter:
```yaml
hooks:
  PostToolUse:
    - matcher: "Write"
      hooks:
        - type: command
          command: "bash $CLAUDE_PROJECT_DIR/scripts/hooks/validate_cost_curve.sh"
          timeout: 30
          statusMessage: "Validating cost-curve compliance..."
```

**Architectural note**: Since PostToolUse fires after the write, exit 2 here does NOT undo the write — it sends the error back to Claude so it can correct and re-write. This is the right behavior for compliance validation. If you need to prevent bad writes from ever hitting disk, use PreToolUse instead.

### Phase D: TaskCompleted Quality Gate

```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/scripts/hooks/check_task_output.py"
          }
        ]
      }
    ]
  }
}
```

**Note**: Matcher is silently ignored for TaskCompleted — hooks fire for ALL task completions. Filter by task metadata inside the script.

### Phase E: Optional — Prompt-Type Hooks for Nuanced Validation

For validation that's hard to encode in shell scripts (e.g., "does the reasoning section contain substantive analysis?"):

```json
{
  "type": "prompt",
  "prompt": "Evaluate if this output meets quality criteria. Check: 1) Agent Reasoning has 2+ substantive paragraphs 2) Sources list has 3+ entries 3) No banned vocabulary. Respond with ok:true or ok:false with reason.",
  "model": "claude-haiku-4-5",
  "timeout": 30
}
```

Supported for: PreToolUse, PostToolUse, PostToolUseFailure, Stop, SubagentStop, TaskCompleted, UserPromptSubmit.
**NOT** supported for: SubagentStart.

### Additional Useful Events (Not in Original Plan)

| Event | Use Case | Example |
|-------|----------|---------|
| `SessionStart` | Initialize timing.json and output directory | Pre-create `output/<slug>/` structure |
| `PostToolUseFailure` | Log when a Write fails | Alert on disk errors or permission issues |
| `PreCompact` | Snapshot pipeline state before context compaction | Save progress to a state file |
| `Notification` with `idle_prompt` matcher | Alternative desktop notification trigger | Fires when Claude goes idle |

## Important Gotchas (from docs)

1. **Stdout must be clean JSON** on exit 0 — shell `.bashrc`/`.zshrc` output will corrupt parsing. Redirect all non-JSON to stderr.
2. **Hooks snapshot at session startup** — changes to `.claude/settings.json` during a running session don't take effect. Use `/hooks` to review and reload.
3. **`stop_hook_active` flag** — check this in Stop hook input to prevent infinite loops.
4. **Async hooks cannot block** — decision fields are ignored for `async: true`.
5. **Agent-type hooks** (`type: "agent"`) have 50-turn limit and only Read, Grep, Glob tools.
6. **Identical command hooks are deduplicated** — same command string from multiple settings files runs once.
7. **SessionEnd hooks** have 1.5s default timeout. Override with `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS=5000`.

## Files to Create

```
scripts/hooks/
  check_banned_vocab.sh
  validate_output_structure.sh
  validate_cost_curve.sh
  validate_capability.sh
  validate_tipping_point.sh
  record_timing.py
  notify_complete.sh
  check_task_output.py
```

## Dependencies

- `jq` for JSON parsing in shell scripts (available on macOS via Homebrew)
- `$CLAUDE_PROJECT_DIR` environment variable (set automatically by Claude Code)
- No external packages needed
