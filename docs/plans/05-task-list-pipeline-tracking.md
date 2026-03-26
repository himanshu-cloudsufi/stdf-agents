# Plan 05: Task List for Pipeline Progress Tracking

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `CLAUDE_CODE_ENABLE_TASKS: "true"` enables tasks | INCORRECT | Tasks enabled by default since v2.1.19; `"false"` opts out |
| TaskCreate, TaskUpdate, TaskList, TaskGet tools | VERIFIED | All exist with documented schemas |
| Task statuses: pending, in-progress, completed, failed, blocked | INCORRECT | `in_progress` (underscore); no `blocked` status — use `blockedBy` array |
| `Ctrl+T` shows task list | VERIFIED | Also `/tasks` command and "show me all tasks" |
| `CLAUDE_CODE_TASK_LIST_ID` for cross-session sharing | VERIFIED | Stored at `~/.claude/tasks/<id>/` |
| TaskCompleted hooks gate transitions | VERIFIED | Exit code 2 blocks completion; no matcher support |
| `claude task list --id` CLI command | INCORRECT | No such subcommand — read `~/.claude/tasks/<id>/` directly |
| Subagents share parent task list | INCORRECT | Agent tool subagents do NOT auto-share; only agent teams do |
| Checklist, parentId, owner, category, metadata fields | MISSING from plan | All real features |

### Critical Corrections

1. **Tasks are enabled by default** — no config needed. Remove the `CLAUDE_CODE_ENABLE_TASKS` setting.
2. **`in-progress` → `in_progress`** (underscore, not hyphen).
3. **No `blocked` status** — use `addBlockedBy` to set dependencies; task stays `pending` until blockers resolve.
4. **`claude task list --id` doesn't exist** — read task files from `~/.claude/tasks/<id>/` directly.
5. **Subagents (Agent tool) don't share the parent task list** — they run in separate sessions. Only agent teams share natively. The orchestrator (main session) must own the task list.
6. **TaskCompleted hook has no matcher** — filter by `task_subject`/`task_id` inside the script.

## What We Get

- **Visual pipeline progress** — see which agents are running, completed, or pending at a glance
- **Quality gates on task transitions** — tasks can't be marked complete until output validation passes
- **Dependency tracking** — Phase 2 tasks auto-blocked until Phase 1 completes
- **Cross-session continuity** — shared task list IDs let you monitor from another terminal
- **Survives `/compact` and `/clear`** — tasks stored on disk, persist through context management

## How We Do This

### Step 1: No Config Needed (Tasks Enabled by Default)

Tasks are enabled by default since v2.1.19. To use a shared task list across sessions:

```bash
CLAUDE_CODE_TASK_LIST_ID="stdf-$(date +%Y%m%d-%H%M)" claude -p "Run STDF analysis on energy storage"
```

Tasks are stored at `~/.claude/tasks/<CLAUDE_CODE_TASK_LIST_ID>/`.

To **disable** tasks (revert to legacy TodoWrite): `CLAUDE_CODE_ENABLE_TASKS=false`.

### Step 2: Update Pipeline Orchestration in CLAUDE.md

Modify pipeline Step 0 to create tasks with correct schema:

```markdown
### Step 0: Initialize Pipeline
1. Create output directory: `mkdir -p output/<slug>/agents`
2. Create pipeline tasks:
```

**TaskCreate schema:**
```
TaskCreate(
  subject: string,        // REQUIRED — imperative title
  description: string,    // REQUIRED — detailed context + acceptance criteria
  activeForm: string      // OPTIONAL — present-continuous spinner text
)
```

**Pipeline initialization:**
```
TaskCreate(subject="Phase 1: Domain Disruption",
           description="Cat 1 analysis. Output: output/<slug>/agents/01-domain-disruption.md",
           activeForm="Running domain disruption analysis...")

TaskCreate(subject="Phase 1: Cost Curve",
           description="Cat 2 analysis. Output: output/<slug>/agents/02-cost-curve.md",
           activeForm="Running cost curve analysis...")

TaskCreate(subject="Phase 1: Capability",
           description="Cat 3 analysis. Output: output/<slug>/agents/03-capability.md",
           activeForm="Running capability analysis...")

TaskCreate(subject="Phase 2: Tipping Point",
           description="Cat 5 synthesis — requires Phase 1. Output: output/<slug>/agents/04-tipping-point.md",
           activeForm="Running tipping point synthesis...")

TaskCreate(subject="Phase 3: Adoption S-Curve",
           description="Cat 4 analysis. Output: output/<slug>/agents/05-adoption-scurve.md",
           activeForm="Running adoption S-curve analysis...")

TaskCreate(subject="Phase 4: Synthesizer",
           description="Final 7-phase narrative. Output: output/<slug>/00-final-synthesis.md",
           activeForm="Running final synthesis...")

TaskCreate(subject="Write README Index",
           description="Pipeline summary and links to all outputs.",
           activeForm="Writing README index...")
```

**Set dependencies (after creation):**
```
# Phase 2 blocked by all Phase 1 tasks
TaskUpdate(taskId="<tipping-id>", addBlockedBy=["<domain-id>", "<cost-id>", "<capability-id>"])

# Phase 3 blocked by Phase 2
TaskUpdate(taskId="<adoption-id>", addBlockedBy=["<tipping-id>"])

# Synthesizer blocked by Phase 3
TaskUpdate(taskId="<synth-id>", addBlockedBy=["<adoption-id>"])

# README blocked by Synthesizer
TaskUpdate(taskId="<readme-id>", addBlockedBy=["<synth-id>"])
```

### Step 3: Task State Machine (Corrected)

**Valid statuses:** `pending`, `in_progress`, `completed`, `failed`

There is **no `blocked` status**. A task with `blockedBy: ["upstream-id"]` and `status: "pending"` is implicitly blocked — it auto-unblocks when the blocker completes.

```
pending  ─────────────────→  in_progress  →  completed
  │                                        ↘
  │  (with addBlockedBy=["upstream-id"])     failed
  └── implicitly blocked while blockers pending
```

Pipeline orchestration logic:
- When launching an agent: `TaskUpdate(taskId, status: "in_progress")`
- When agent returns successfully: `TaskUpdate(taskId, status: "completed")`
- When agent fails:
  - If CRITICAL (cost-curve, tipping-point): `TaskUpdate(taskId, status: "failed")` → downstream tasks remain blocked → HARD FAIL
  - If non-critical: `TaskUpdate(taskId, status: "failed")` → apply confidence penalty → continue

### Step 4: Interactive Progress View

Press `Ctrl+T` (or `/tasks`) to see task list:
```
STDF Pipeline: energy-storage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[x] Phase 1: Domain Disruption      (completed, 48s)
[x] Phase 1: Cost Curve             (completed, 62s)
[~] Phase 1: Capability             (in_progress, 34s...)
[ ] Phase 2: Tipping Point          (pending, blocked by 1,2,3)
[ ] Phase 3: Adoption S-Curve       (pending, blocked by 4)
[ ] Phase 4: Synthesizer            (pending, blocked by 5)
[ ] Write README Index              (pending, blocked by 6)
```

Shows up to 10 tasks. You can also say "show me all tasks" or "clear all tasks".

### Step 5: Headless Task Monitoring (Corrected)

**`claude task list` does not exist as a CLI command.** Query tasks from the filesystem:

```bash
# Set shared task list ID
CLAUDE_CODE_TASK_LIST_ID="stdf-20260314-0900" claude -p "Run STDF analysis..."

# From another terminal, read task state directly:
ls ~/.claude/tasks/stdf-20260314-0900/

# Parse task JSON:
python3 -c "
import json, glob
for f in sorted(glob.glob('$HOME/.claude/tasks/stdf-20260314-0900/*.json')):
    t = json.load(open(f))
    status = t.get('status', 'unknown')
    print(f\"[{status:12s}] {t['subject']}\")
"
```

Or open a new interactive session with the same ID to inspect via `Ctrl+T`:
```bash
CLAUDE_CODE_TASK_LIST_ID="stdf-20260314-0900" claude
# Then press Ctrl+T
```

### Step 6: TaskCompleted Hook Integration (Corrected)

**Note**: TaskCompleted does NOT support matchers — hooks fire for ALL task completions. The script must filter by `task_subject` or `task_id`.

Correct hook config (flat structure, not nested):
```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "type": "command",
        "command": "python3 $CLAUDE_PROJECT_DIR/scripts/hooks/check_task_output.py"
      }
    ]
  }
}
```

**Hook input (stdin JSON):**
```json
{
  "hook_event_name": "TaskCompleted",
  "task_id": "string",
  "task_subject": "string",
  "task_description": "string",
  "teammate_name": "string (optional)",
  "team_name": "string (optional)"
}
```

The `check_task_output.py` script:
1. Reads stdin JSON, extracts `task_subject`
2. Maps subject to expected output file (e.g., "Phase 1: Cost Curve" → `output/<slug>/agents/02-cost-curve.md`)
3. Validates the file: required sections, compliance criteria, banned vocab
4. Exit 0 = allow completion; Exit 2 = block + stderr feedback to agent

### Important Architectural Note

**Subagents (Agent tool) do NOT share the parent's task list.** The main orchestrator session owns the task list and updates it. Subagent invocations run in separate sessions. This means:

- The **orchestrator** creates tasks and updates them based on subagent return values
- **Subagents** themselves don't see or update the task list
- If you need shared task visibility, use **agent teams** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) which share task lists natively

### Additional Task Features (Not in Original Plan)

| Feature | Description | Use Case |
|---------|-------------|----------|
| `checklist` | Sub-items within a task | Track per-agent compliance criteria as sub-tasks |
| `parentId` | Parent-child task hierarchy | Group Phase 1 tasks under a parent |
| `owner` | Assign to specific teammate | Attribute tasks to specific agents |
| `category` | Categorize tasks | Group by pipeline phase |
| `metadata` | Arbitrary key-value store | Store agent confidence scores, timing data |
| `addBlocks` in TaskUpdate | Reverse of `addBlockedBy` | Add this task as a blocker to another |

**Full TaskUpdate schema:**
```
TaskUpdate(
  taskId: string,          // REQUIRED
  status: "pending" | "in_progress" | "completed" | "failed",
  subject: string,         // rename
  description: string,     // update description
  addBlockedBy: string[],  // add dependency IDs
  addBlocks: string[],     // add this as blocker to other tasks
  delete: true             // delete the task
)
```

## Files to Create

```
scripts/hooks/check_task_output.py  — TaskCompleted validation gate
```

## Files to Modify

```
CLAUDE.md  — add task creation/update to pipeline steps
```

## Dependencies

- Tasks are built-in, no config needed
- Plan 01 (Hooks) for TaskCompleted quality gate
- Uses `$CLAUDE_PROJECT_DIR` in hook paths (from Plan 01)
