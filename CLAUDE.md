# STDF v2 -- Server & Frontend

This repo contains two concerns:

1. **`stdf/`** -- Self-contained STDF analysis system. Run `cd stdf && claude` to work on pipeline analyses. Has its own `.claude/`, `CLAUDE.md` (which includes the full orchestrator), agents, lib, data, scripts, and output.

2. **`server/`** -- Claude Agent SDK server that exposes STDF via WebSocket/HTTP. The server loads agent definitions from `stdf/.claude/agents/` and runs sessions with `cwd=stdf/`.

## Key Directories

| Path | Purpose |
|------|---------|
| `stdf/` | Self-contained STDF analysis system (run Claude Code from here) |
| `stdf/CLAUDE.md` | Pipeline orchestrator -- presets, DAG, tiers, execution steps, evaluation |
| `server/` | Claude Agent SDK server (FastAPI + WebSocket) |
| `scripts/` | Legacy CLI wrapper (`stdf_v2_cc.py`) |

## Server Development

Server code is in `server/`. Key files:
- `server/main.py` -- FastAPI app, WebSocket handler
- `server/session_manager.py` -- SDK client creation, `cwd=stdf/`
- `server/agents.py` -- Agent definition loader, system prompt
- `server/config.py` -- `REPO_ROOT`, `STDF_DIR`, `DEV_MODEL`
- `server/tool_permissions.py` -- Interactive tool interception (AskUser, PlanMode)

## Conventions
- Always use python3
