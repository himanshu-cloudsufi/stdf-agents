# Plan 08: Session Management & Telemetry

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `--continue` / `-c` flag | VERIFIED | Loads most recent conversation in current directory |
| `--resume` / `-r` flag | VERIFIED | Accepts session name or ID; no-arg opens interactive picker |
| `/rename` command | VERIFIED | Works mid-session; for headless use `--name` / `-n` instead |
| `--session-id` for human-readable names | INCORRECT | Requires valid UUID — use `--name` / `-n` for readable names |
| `CLAUDE_CODE_ENABLE_TELEMETRY` env var | VERIFIED | Set to `1` to enable |
| `cost_counter` metric name | INCORRECT | Actual: `claude_code.cost.usage` |
| `token_counter` metric name | INCORRECT | Actual: `claude_code.token.usage` |
| `tool_decision_counter` metric name | INCORRECT | Actual: `claude_code.code_edit_tool.decision` |
| `session_duration` metric name | INCORRECT | Actual: `claude_code.active_time.total` |
| OTEL endpoint port 4318 | INCORRECT | gRPC default is 4317; 4318 is HTTP/protobuf |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | MISSING | Required — must be set alongside endpoint |
| `OTEL_LOGS_EXPORTER` | MISSING | Required for per-request cost/token events |
| `/rewind` command | VERIFIED | Opens checkpoint picker (per-prompt, not per-file-write) |
| `--from-pr` flag | VERIFIED but MISSING from plan | Links sessions to PRs |
| `--fork-session` flag | MISSING from plan | Branch a session without overwriting original |
| `--name` / `-n` flag | MISSING from plan | Name session at startup (headless equivalent of `/rename`) |

### Critical Corrections

1. **`--session-id` requires a valid UUID**, not human-readable names. Use `--name` / `-n` instead.
2. **All 4 metric names were wrong** — corrected to official `claude_code.*` naming.
3. **OTEL port is 4317** (gRPC), not 4318 (HTTP/protobuf).
4. **`OTEL_LOGS_EXPORTER` is required** for per-request cost events (the data the tracking script needs).
5. **Checkpoints are per-prompt**, not per-file-write.

## What We Get

- **Named pipeline sessions** — resume any STDF analysis by name across days or weeks
- **`--continue` support** — pick up mid-pipeline after interruption without re-running completed agents
- **Per-agent token and cost tracking** — know exactly which agent is most expensive and optimize
- **Pipeline cost budgeting** — track total cost per analysis run, compare across sectors
- **Session branching** — fork a failed pipeline run without overwriting the original

## How We Do This

### Part A: Session Management (Corrected)

**Starting a named pipeline session:**
```bash
# Interactive — name mid-session
/rename stdf-energy-storage-20260314

# Headless — use --name / -n (NOT --session-id)
claude -n stdf-energy-storage-20260314 -p "Run STDF analysis on energy storage"
```

**Session naming convention:**
```
stdf-<analysis-slug>-<YYYYMMDD>
```

**Resuming interrupted pipelines:**
```bash
# Resume most recent session in current directory
claude --continue
# or
claude -c

# Resume specific named session
claude --resume stdf-energy-storage-20260314
# or
claude -r stdf-energy-storage-20260314

# Resume session linked to a PR
claude --from-pr 123

# Resume and branch (don't overwrite original)
claude --resume stdf-energy-storage-20260314 --fork-session

# Resume without arguments — opens interactive session picker
claude --resume
```

**Session picker keyboard shortcuts:**
| Key | Action |
|-----|--------|
| `R` | Rename session |
| `P` | Preview session |
| `B` | Filter by git branch |
| `A` | Toggle all projects |

**Update CLAUDE.md** Step 0:
```markdown
### Step 0: Initialize Pipeline
1. Derive analysis slug from query
2. Name session: `claude -n stdf-<slug>-<date>` at startup or `/rename stdf-<slug>-<date>` mid-session
3. Create output directory
4. Initialize task list
```

### Part B: OpenTelemetry Integration (Corrected)

**Corrected settings:**
```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4317",
    "OTEL_LOG_TOOL_DETAILS": "1"
  }
}
```

Key settings:
- `OTEL_LOGS_EXPORTER`: Required for per-request events with cost/token data
- `OTEL_EXPORTER_OTLP_PROTOCOL`: Required — `grpc` for port 4317
- `OTEL_LOG_TOOL_DETAILS`: Enables per-tool attribution (MCP server/tool names)

**Corrected metrics (official names):**
| Metric Name | Unit | STDF Application |
|-------------|------|------------------|
| `claude_code.cost.usage` | USD | Total pipeline cost per analysis |
| `claude_code.token.usage` | tokens | Per-agent token consumption |
| `claude_code.code_edit_tool.decision` | count | File write accept/reject rate |
| `claude_code.active_time.total` | seconds | Pipeline execution time |
| `claude_code.session.count` | count | Pipeline run count |
| `claude_code.lines_of_code.count` | count | Lines modified per run |
| `claude_code.commit.count` | count | Commits created |

**Key events (via `OTEL_LOGS_EXPORTER`):**

The `claude_code.api_request` event is what `track_pipeline_cost.py` needs — it includes:
- `cost_usd` per API call
- `input_tokens`, `output_tokens`, `cache_read_tokens`
- `duration_ms`
- `model`
- `prompt.id` — UUID linking all events from a single prompt turn (use to group by agent)

Other events: `claude_code.user_prompt`, `claude_code.tool_result`, `claude_code.api_error`.

**Corrected local collector setup:**
```bash
# gRPC port is 4317 (NOT 4318)
docker run -p 4317:4317 -p 16686:16686 jaegertracing/all-in-one:latest
```

View traces at `http://localhost:16686`.

### Part C: Pipeline Cost Tracking Script

**Create `scripts/track_pipeline_cost.py`:**
- Reads OTEL events after each pipeline run
- Groups `claude_code.api_request` events by `prompt.id` to attribute costs per agent
- Writes cost summary to `output/<slug>/cost_report.json`:
```json
{
  "analysis": "energy-storage",
  "date": "2026-03-14",
  "total_cost_usd": 2.47,
  "total_tokens": 485000,
  "agents": {
    "domain-disruption": {"cost": 0.38, "input_tokens": 42000, "output_tokens": 18000, "duration_s": 48},
    "cost-curve": {"cost": 0.52, "input_tokens": 58000, "output_tokens": 24000, "duration_s": 62},
    "capability": {"cost": 0.41, "input_tokens": 45000, "output_tokens": 19000, "duration_s": 51},
    "tipping-point": {"cost": 0.35, "input_tokens": 38000, "output_tokens": 16000, "duration_s": 35},
    "adoption-scurve": {"cost": 0.44, "input_tokens": 48000, "output_tokens": 21000, "duration_s": 47},
    "synthesizer": {"cost": 0.37, "input_tokens": 55000, "output_tokens": 15000, "duration_s": 40}
  }
}
```

### Part D: Benchmarking Dashboard

**Create `scripts/benchmark_runs.py`:**
- Aggregates `cost_report.json` across all runs in `output/`
- Produces `output/BENCHMARK.md` comparing average cost, most expensive agent, token trends

### Part E: Checkpointing (Corrected)

**Checkpoints are created per user prompt turn**, not per file write. In the STDF pipeline, each agent invocation happens within a prompt turn — so checkpoint granularity is at the agent invocation level.

```markdown
### Recovery
- Press `Esc+Esc` or use `/rewind` to open the checkpoint picker — select any prior prompt to restore
- Checkpoints are per-prompt (not per-file-write)
- Name sessions with `claude -n <name>` at startup or `/rename <name>` mid-session
- Use `claude --resume <name> --fork-session` to branch without overwriting the original
- Use `claude --from-pr <number>` to resume any session linked to a PR
- Use `--no-session-persistence` for ephemeral CI/test runs that shouldn't be saved
```

## CLI Flag Quick Reference

| Flag | Short | Description |
|------|-------|-------------|
| `--continue` | `-c` | Resume most recent session in current dir |
| `--resume <name>` | `-r` | Resume specific named session |
| `--name <name>` | `-n` | Name the session at startup |
| `--session-id <uuid>` | | Use specific UUID (must be valid UUID) |
| `--fork-session` | | Branch session on resume (don't overwrite) |
| `--from-pr <num>` | | Resume session linked to PR |
| `--no-session-persistence` | | Don't save session (ephemeral) |

## Files to Create

```
scripts/
  track_pipeline_cost.py
  benchmark_runs.py
```

## Files to Modify

```
.claude/settings.json  — add telemetry env vars
CLAUDE.md              — add session naming to Step 0, add recovery section
```

## Dependencies

- Docker (optional — for local Jaeger OTEL collector)
- Session management and checkpointing work without telemetry
