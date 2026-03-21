# STDF Chat UI — POC Implementation Spec

## Overview

A chat-based web UI powered by the Claude Agent SDK (Python). The user talks directly to a Claude session — Claude IS the orchestrator. It reads the STDF Agent Registry, resolves the DAG dynamically, spawns subagents via the Agent tool, handles failures, asks the user questions via AskUserQuestion, and answers follow-ups. No hardcoded Python pipeline manager.

---

## Core Architecture

```
┌──────────────────────────────────────────────────────┐
│                  React + Tailwind UI                  │
│  ┌────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Chat Panel │  │  DAG Sidebar │  │ Analysis Tabs│ │
│  │  (messages, │  │  (visual node│  │ (concurrent  │ │
│  │  streaming, │  │   graph,     │  │  analyses)   │ │
│  │  questions) │  │   status,    │  │              │ │
│  │             │  │   cost)      │  │              │ │
│  └──────┬─────┘  └──────┬───────┘  └──────┬───────┘ │
└─────────┼───────────────┼──────────────────┼─────────┘
          │               │                  │
          └───────────────┼──────────────────┘
                          │ WebSocket
                          ▼
┌──────────────────────────────────────────────────────┐
│                   FastAPI Server                      │
│                                                       │
│  ┌─────────────┐                    ┌─────────────┐  │
│  │ Session Mgr  │                    │  MCP Tools  │  │
│  │ (per-user    │                    │ (lib/ funcs │  │
│  │  sessions,   │                    │  as native  │  │
│  │  resume)     │                    │  tools)     │  │
│  └──────┬──────┘                    └──────┬──────┘  │
└─────────┼──────────────────────────────────┼─────────┘
          │                                  │
          ▼                                  ▼
┌──────────────────────────────────────────────────────┐
│              Claude Agent SDK (Python)                 │
│                                                       │
│  ClaudeSDKClient (one per user per analysis)          │
│    ┌──────────────────────────────────────────┐       │
│    │  ORCHESTRATOR CLAUDE SESSION              │       │
│    │                                           │       │
│    │  System prompt contains:                  │       │
│    │  - Agent Registry (DAG topology)          │       │
│    │  - Failure Matrix rules                   │       │
│    │  - Preset detection rules                 │       │
│    │  - Phase 1 hard gate instructions         │       │
│    │  - CLAUDE.md + shared-rules               │       │
│    │                                           │       │
│    │  Tools available:                         │       │
│    │  - Agent (spawns 16 STDF subagents)       │       │
│    │  - AskUserQuestion (UI interactions)      │       │
│    │  - Read, Write, Glob, Grep, Bash          │       │
│    │  - MCP tools (lib/ functions)             │       │
│    │                                           │       │
│    │  Claude dynamically:                      │       │
│    │  1. Detects preset from user query        │       │
│    │  2. Asks user to confirm (AskUserQuestion)│       │
│    │  3. Resolves DAG from Agent Registry      │       │
│    │  4. Spawns subagents in parallel tiers    │       │
│    │  5. Checks failures, applies penalties    │       │
│    │  6. Runs Phase 1 hard gate               │       │
│    │  7. Presents final synthesis              │       │
│    │  8. Answers follow-up questions           │       │
│    │  9. Re-runs agents if user requests       │       │
│    └──────────────────────────────────────────┘       │
│                                                       │
│  16 AgentDefinitions (loaded from .claude/agents/)    │
│  Custom MCP server (lib/ functions as tools)          │
│  Hooks (progress tracking, guardrails, audit)         │
│                                                       │
│  File I/O: output/<slug>/agents/*.md (unchanged)      │
└──────────────────────────────────────────────────────┘
```

### Key Insight: Claude IS the Pipeline Manager

There is **no Python DAG runner**. The orchestrator is a Claude session with:
- The Agent Registry table in its system prompt (same as CLAUDE.md)
- The failure matrix rules in its system prompt
- The `/stdf` skill's orchestration logic baked into its system prompt
- Access to the `Agent` tool to spawn any of the 16 STDF subagents
- Access to `AskUserQuestion` for all user interactions

This means:
- **Dynamic orchestration** — Claude decides execution order, not Python code
- **Natural conversation** — user talks to Claude, Claude talks back AND runs agents
- **Adaptive** — Claude can change plans mid-pipeline based on intermediate results
- **Follow-ups are free** — same session, Claude already has context
- **Re-runs are natural** — "re-run cost-fitter with 25%" is just a chat message
- **Error handling is intelligent** — Claude reads error messages, decides what to do

---

## Design Decisions (from interview)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Pipeline UX | Background + chat | User can keep chatting while agents run |
| Multi-user | Isolated per user | Each user owns their sessions and output |
| Output format | Raw markdown | Frontend renders with react-markdown. No structured JSON layer |
| Progress granularity | Agent-level | Show each agent start/complete with time and cost |
| Follow-up behavior | Default read-only, user can request re-runs | "Re-run with X" triggers selective re-execution |
| Auth | Basic username isolation | External auth system exists; just need username for isolation |
| All interactions | AskUserQuestion | Preset selection, gate approvals, re-run confirmations all render as UI components |
| Persistence | File-based | Output files persist on disk by slug. No DB. Session IDs stored alongside |
| Agent memory | Skip for POC | No per-agent persistent memory in SDK version |
| Cost display | Per-agent breakdown table | Shown after pipeline completion |
| Re-run scope | Ask the user | Show affected downstream agents, let user choose single vs cascade |
| DAG visualization | Visual node graph | Interactive sidebar showing agent dependencies, status, cost |
| Concurrent analyses | Multiple per user | Each analysis gets its own tab/panel |
| Validation | Internal only | Guardrails run silently; orchestrator fixes before presenting |
| Lib modules | MCP tools | Wrap lib/ functions as @tool decorators for native agent access |
| Frontend stack | React + Tailwind | Standard modern stack with react-markdown for rendering |
| Context strategy | Summary + lazy read | Load final synthesis upfront; lazy-read specific files on deep follow-ups |

---

## Backend Components

### 1. Agent Loader (`server/agents.py`)

Parses 16 `.claude/agents/*.md` files into `AgentDefinition` dicts.

```python
def load_agents() -> dict[str, AgentDefinition]:
    """
    Read each .claude/agents/stdf-*.md file.
    Extract YAML frontmatter (name, description, tools, model).
    Load the markdown body as the agent prompt.
    Prepend shared-rules.md content to each prompt.
    Return dict keyed by agent name.
    """
```

- Input: `.claude/agents/stdf-*.md` files
- Output: `dict[str, AgentDefinition]` with 16 entries
- Shared rules from `.claude/shared-rules.md` prepended to every agent prompt

### 2. MCP Tool Server (`server/mcp_tools.py`)

Wraps key `lib/` functions as native MCP tools via `@tool` decorator.

Tools to expose:

| Tool name | Wraps | Used by |
|-----------|-------|---------|
| `fit_exponential_cost_curve` | `lib.cost_curve_math.exponential_fit` | cost-fitter |
| `compute_learning_rate` | `lib.cost_curve_math.learning_rate` | cost-fitter |
| `compute_competitive_threshold` | `lib.cost_curve_math.competitive_threshold` | cost-fitter, cost-parity-checker |
| `fit_scurve` | `lib.scurve_math.fit_logistic` | scurve-fitter |
| `classify_adoption_phase` | `lib.scurve_math.phase_classification` | regional-adopter |
| `fit_capability_trajectory` | `lib.capability_math.fit_trajectory` | capability |
| `check_tipping_conditions` | `lib.tipping_math.check_conditions` | tipping-synthesizer |
| `query_data_catalog` | `lib.data_catalog.search_curves` | cost-researcher |
| `decompose_demand` | `lib.demand_math.decompose` | demand-decomposer |
| `project_streams` | `lib.demand_math.stream_projection` | stream-forecaster |
| `run_fleet_model` | `lib.demand_math.stock_flow` | fleet-modeler |
| `validate_vocabulary` | `lib.vocabulary.scan` | all agents (self-check) |

```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("fit_exponential_cost_curve", "Fit exponential curve to cost data points", {
    "years": list[int], "costs": list[float], "unit": str
})
async def fit_exponential_cost_curve(args):
    from lib.cost_curve_math import exponential_fit
    result = exponential_fit(args["years"], args["costs"], args["unit"])
    return {"content": [{"type": "text", "text": json.dumps(result)}]}

stdf_mcp_server = create_sdk_mcp_server(
    name="stdf-tools", version="1.0.0",
    tools=[fit_exponential_cost_curve, compute_learning_rate, ...]
)
```

### 3. Orchestrator System Prompt (`server/orchestrator.py`)

**There is no Python pipeline manager.** The orchestrator is a Claude session. This module builds the system prompt that teaches Claude how to be the STDF orchestrator.

```python
def build_orchestrator_prompt(slug: str, user_id: str) -> str:
    """
    Assembles the system prompt for the orchestrator Claude session.
    Includes:
    - Role: "You are the STDF pipeline orchestrator AND conversational assistant"
    - Agent Registry table (DAG topology) from CLAUDE.md
    - Failure Matrix (CRITICAL/HIGH/MEDIUM rules)
    - Preset detection rules (keyword → preset mapping)
    - Phase 1 hard gate instructions
    - AskUserQuestion usage patterns
    - Output directory: output/<slug>/agents/
    - Context strategy: load synthesis after pipeline, lazy-read on follow-ups
    """
    return f"""
You are the STDF disruption analysis assistant. You help users run analyses
and answer questions about results.

## Your Capabilities
- Run the full STDF 16-agent pipeline by spawning subagents via the Agent tool
- Answer follow-up questions about completed analyses
- Re-run specific agents with modified parameters when the user requests it
- Use AskUserQuestion for ALL user interactions (preset selection, approvals, etc.)

## Agent Registry (DAG Topology)
{AGENT_REGISTRY_TABLE}

## How to Run a Pipeline
1. When user requests an analysis, detect the preset from their query
2. Use AskUserQuestion to confirm preset selection with the user
3. Resolve which agents are needed (walk the "Requires" column recursively)
4. Group agents into parallel tiers (agents with no unmet deps run together)
5. Execute tier by tier — spawn parallel agents in a single message
6. After each tier, check results:
   - CRITICAL agent failed → STOP pipeline, tell user
   - HIGH agent failed → continue with -0.3 confidence penalty, warn user
   - MEDIUM agent failed → continue with -0.1 penalty, note it
7. After Phase 1 (domain-disruption, cost-researcher, capability):
   - Read 01-domain-disruption.md
   - Classify technologies as X-Flow/Stellar/Hybrid
   - Use AskUserQuestion to show classification and get user approval
   - Write approved classification to the domain-disruption file
8. After all agents complete, run validation (internal — don't show to user)
9. Read 00-final-synthesis.md and present key findings to user
10. Now you're in chat mode — answer follow-ups from the synthesis context

## Failure Matrix
| Criticality | On Failure | Action |
|-------------|-----------|--------|
| CRITICAL | Hard fail | Stop pipeline, report to user |
| HIGH | Soft fail | Continue, apply -0.3 confidence penalty |
| MEDIUM | Warning | Continue, apply -0.1 confidence penalty |

## Re-runs
When user asks to re-run an agent with modified parameters:
1. Identify which agent(s) are affected
2. Identify downstream agents that would need re-running for consistency
3. Use AskUserQuestion: "Re-run [agent] only, or cascade through [N downstream agents]?"
4. Execute based on user choice

## Context Strategy
- After pipeline: read the final synthesis into context
- For follow-up questions: lazy-read specific agent output files as needed
- For re-runs: re-read affected output files after re-execution

## Output Directory
All agent outputs go to: output/{slug}/agents/
"""
```

### What the orchestrator Claude does vs what Python does

| Responsibility | Who |
|---------------|-----|
| Detect preset from query | Claude (in conversation) |
| Ask user to confirm preset | Claude (via AskUserQuestion) |
| Resolve DAG topology | Claude (reads Agent Registry in system prompt) |
| Decide parallel vs sequential execution | Claude (spawns agents in single message for parallel) |
| Handle CRITICAL failures | Claude (reads agent result, decides to stop) |
| Phase 1 hard gate | Claude (reads output file, classifies, asks user) |
| Run guardrail validation | Claude (calls MCP tool) |
| Present synthesis | Claude (reads output file, streams to user) |
| Answer follow-ups | Claude (same session, reads files as needed) |
| Re-run agents | Claude (spawns specific subagents) |
| Create/manage sessions | Python (SessionManager) |
| Parse agent .md files → AgentDefinition | Python (agent loader) |
| Expose lib/ as MCP tools | Python (MCP server) |
| Track progress events for UI | Python (hooks) |
| Forward WebSocket messages | Python (FastAPI) |

### 4. Session Manager (`server/sessions.py`)

Manages per-user `ClaudeSDKClient` instances.

```python
class SessionManager:
    """
    Owns:
    - Creating new ClaudeSDKClient per user per analysis
    - Tracking active sessions: {user_id: {slug: client}}
    - Multiple concurrent analyses per user (one client per analysis)
    - Resuming sessions by slug (output files persist on disk)
    - Cleanup of idle sessions (timeout after 30 min)
    """

    async def get_or_create(self, user_id: str, slug: str) -> ClaudeSDKClient:
        key = f"{user_id}:{slug}"
        if key not in self.sessions:
            client = ClaudeSDKClient(options=ClaudeAgentOptions(
                cwd=REPO_ROOT,
                allowed_tools=[
                    "Read", "Write", "Bash", "Glob", "Grep",
                    "Agent",           # spawn subagents
                    "AskUserQuestion", # all user interactions
                ],
                agents=self.agent_defs,
                system_prompt=build_orchestrator_prompt(slug, user_id),
                mcp_servers={"stdf-tools": stdf_mcp_server},
                include_partial_messages=True,
                hooks=self.build_hooks(user_id, slug),
                model="claude-opus-4-6",
                setting_sources=["project"],  # loads CLAUDE.md, shared-rules
                permission_mode="acceptEdits",
            ))
            await client.__aenter__()
            self.sessions[key] = client
        return self.sessions[key]
```

### 5. Hooks (`server/hooks.py`)

Hooks are the **only** place Python intercepts the Claude session. They extract structured events for the frontend without interfering with Claude's orchestration.

```python
async def progress_hook(input_data, tool_use_id, context):
    """SubagentStop hook — emit agent completion event to frontend."""
    agent_name = input_data.get("agent_name", "unknown")
    event = {
        "type": "agent_completed",
        "agent": agent_name,
        "duration_s": input_data.get("duration_s"),
        "cost_usd": input_data.get("cost_usd"),
    }
    # Push to the WebSocket associated with this session
    await context["websocket"].send_json(event)
    return {}

async def guardrail_hook(input_data, tool_use_id, context):
    """PreToolUse hook — block writes with banned vocabulary."""
    content = input_data["tool_input"].get("content", "")
    from lib.vocabulary import scan
    violations = scan(content)
    if violations:
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": f"Banned vocabulary: {violations}",
            }
        }
    return {}

async def question_hook(input_data, tool_use_id, context):
    """PreToolUse hook for AskUserQuestion — forward to frontend as UI component."""
    if input_data.get("tool_name") == "AskUserQuestion":
        # Forward the question structure to the frontend
        await context["websocket"].send_json({
            "type": "question",
            "question_id": tool_use_id,
            "data": input_data["tool_input"],
        })
    return {}  # allow — the SDK handles the actual question flow

hooks = {
    "PreToolUse": [
        HookMatcher(matcher="Write|Edit", hooks=[guardrail_hook]),
        HookMatcher(matcher="AskUserQuestion", hooks=[question_hook]),
    ],
    "SubagentStop": [HookMatcher(hooks=[progress_hook])],
    "PostToolUse": [HookMatcher(hooks=[audit_hook])],
}
```

### 6. WebSocket API (`server/main.py`)

The server is thin — it just bridges WebSocket ↔ ClaudeSDKClient. No pipeline logic.

```python
@app.websocket("/ws/{user_id}")
async def chat(websocket: WebSocket, user_id: str):
    await websocket.accept()
    session_mgr = get_session_manager()

    while True:
        msg = await websocket.receive_json()

        match msg["type"]:
            case "new_analysis":
                # User wants a new analysis — create session, send query to Claude
                slug = generate_slug(msg["query"])
                client = await session_mgr.get_or_create(user_id, slug)
                # Claude receives the query, decides to run pipeline, spawns agents
                asyncio.create_task(
                    stream_response(client, msg["query"], websocket)
                )

            case "chat":
                # Follow-up question — same session, Claude already has context
                client = session_mgr.get(user_id, msg["slug"])
                asyncio.create_task(
                    stream_response(client, msg["text"], websocket)
                )

            case "answer":
                # User answered an AskUserQuestion rendered in the UI
                client = session_mgr.get(user_id, msg["slug"])
                asyncio.create_task(
                    stream_response(client, msg["answer_text"], websocket)
                )


async def stream_response(client: ClaudeSDKClient, text: str, ws: WebSocket):
    """Send a message to Claude and stream all responses to the frontend."""
    await client.query(text)
    async for event in client.receive_response():
        if isinstance(event, StreamEvent):
            await ws.send_json({"type": "stream", "data": format_stream(event)})
        elif isinstance(event, ResultMessage):
            await ws.send_json({
                "type": "done",
                "cost": event.total_cost_usd,
                "session_id": event.session_id,
            })
```

**Note how simple this is.** The server doesn't know about pipelines, agents, presets, or DAGs. It just forwards messages between the browser and Claude. All intelligence lives in the Claude session.

---

## Frontend Components

### Layout

```
┌─────────────────────────────────────────────────────────┐
│  STDF Analysis Platform                    [username]    │
├──────────┬──────────────────────────┬───────────────────┤
│          │                          │                    │
│ Analysis │     Chat Panel           │   DAG Sidebar      │
│  Tabs    │                          │                    │
│          │  ┌────────────────────┐  │  ┌──────────────┐ │
│ [Energy  │  │ User: Analyze the  │  │  │  ● domain    │ │
│  Storage]│  │ energy storage...  │  │  │  ↓           │ │
│          │  ├────────────────────┤  │  │  ● cost-res  │ │
│ [Auto-   │  │ System: Running    │  │  │  ↓           │ │
│  nomous] │  │ pipeline...        │  │  │  ▶ cost-fit  │ │
│          │  ├────────────────────┤  │  │  ↓           │ │
│ [+ New]  │  │ [AskUserQuestion]  │  │  │  ○ parity   │ │
│          │  │ ┌─────┐ ┌───────┐ │  │  │  ○ tipping   │ │
│          │  │ │FULL │ │QUICK  │ │  │  │              │ │
│          │  │ └─────┘ └───────┘ │  │  ├──────────────┤ │
│          │  ├────────────────────┤  │  │ Cost: $0.45  │ │
│          │  │ ▌Streaming response│  │  │ Time: 2m 14s │ │
│          │  │                    │  │  └──────────────┘ │
│          │  └────────────────────┘  │                    │
│          │  [Type a message...]     │                    │
├──────────┴──────────────────────────┴───────────────────┤
└──────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Purpose |
|-----------|---------|
| `AnalysisTabs` | Tab bar for concurrent analyses. Each tab = one pipeline run + chat session |
| `ChatPanel` | Message list with streaming support. Renders markdown via `react-markdown` |
| `AskUserQuestionRenderer` | Renders SDK `AskUserQuestion` tool calls as interactive forms/buttons |
| `DAGSidebar` | Visual node graph of the pipeline. Nodes show status (pending/running/done/failed) and cost |
| `CostBreakdown` | Post-completion table: agent name, duration, cost, status |
| `MessageInput` | Text input with send button. Disabled during AskUserQuestion (waiting for answer) |
| `ProgressIndicator` | Per-agent status updates in chat: "✓ cost-researcher (14s, $0.08)" |

### DAG Sidebar Node States

| State | Visual |
|-------|--------|
| Pending | Gray circle, dashed border |
| Running | Blue circle, pulsing animation |
| Completed | Green circle, checkmark |
| Failed (CRITICAL) | Red circle, X mark |
| Failed (HIGH) | Orange circle, warning icon |
| Skipped | Gray circle, slash |

### AskUserQuestion Rendering

When the backend emits a `question` event (from SDK's AskUserQuestion tool):

```tsx
// Rendered inline in chat as an interactive card
<QuestionCard>
  <QuestionText>{question}</QuestionText>
  <OptionGroup>
    {options.map(opt => (
      <OptionButton
        key={opt.label}
        onClick={() => sendAnswer(question_id, opt.label)}
        selected={selectedOption === opt.label}
      >
        <Label>{opt.label}</Label>
        <Description>{opt.description}</Description>
      </OptionButton>
    ))}
  </OptionGroup>
</QuestionCard>
```

Used for:
- Preset selection ("Which analysis depth?")
- Phase 1 hard gate ("I classified solar as Stellar. Approve?")
- Re-run scope ("Re-run cost-fitter only, or cascade through 4 downstream agents?")

---

## Context Strategy for Follow-ups

```
Pipeline completes
    → Load 00-final-synthesis.md into ClaudeSDKClient context (summary of everything)
    → User asks: "What's the tipping year?"
        → Answer from synthesis already in context ✓
    → User asks: "What specific data points drove the 18% learning rate?"
        → Orchestrator reads output/<slug>/agents/02b-cost-fitter.md (lazy)
        → Answers from that file
    → User asks: "Re-run with 25% learning rate"
        → AskUserQuestion: "Re-run cost-fitter only, or cascade through cost-parity → tipping-synth → scurve?"
        → User chooses → selective re-execution
```

---

## File Structure

```
stdf-agents/
├── server/                     # NEW — FastAPI backend (thin layer)
│   ├── __init__.py
│   ├── main.py                 # FastAPI app, WebSocket endpoint
│   ├── agents.py               # Agent loader (parse .md → AgentDefinition)
│   ├── orchestrator.py         # Builds orchestrator system prompt
│   ├── sessions.py             # Per-user ClaudeSDKClient management
│   ├── mcp_tools.py            # lib/ functions as @tool MCP tools
│   ├── hooks.py                # Progress tracking, guardrails, audit
│   └── config.py               # Settings, paths, constants
├── frontend/                   # NEW — React + Tailwind
│   ├── package.json
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── MessageList.tsx
│   │   │   ├── MessageInput.tsx
│   │   │   ├── DAGSidebar.tsx
│   │   │   ├── AnalysisTabs.tsx
│   │   │   ├── AskUserQuestionRenderer.tsx
│   │   │   ├── CostBreakdown.tsx
│   │   │   └── ProgressIndicator.tsx
│   │   ├── hooks/
│   │   │   ├── useWebSocket.ts
│   │   │   └── useAnalysis.ts
│   │   └── types/
│   │       └── events.ts
│   └── tailwind.config.js
├── .claude/agents/             # UNCHANGED — 16 agent definitions
├── .claude/shared-rules.md     # UNCHANGED
├── lib/                        # UNCHANGED — 14 Python modules
├── data/                       # UNCHANGED — 956 empirical curves
└── output/                     # UNCHANGED — pipeline output dir
```

**Note:** No `pipeline.py`, no `events.py`. Pipeline logic lives in the orchestrator Claude session, not in Python.

---

## SDK Features Used

| SDK Feature | STDF Use Case |
|-------------|---------------|
| `ClaudeSDKClient` | Multi-turn chat per user per analysis |
| `AgentDefinition` | 16 STDF subagents loaded from `.claude/agents/*.md` |
| `hooks.SubagentStop` | Pipeline progress → UI updates |
| `hooks.PreToolUse` | Guardrail enforcement on file writes |
| `hooks.PostToolUse` | Audit logging |
| `max_budget_usd` | Per-session cost cap |
| `ResultMessage.total_cost_usd` | Per-agent cost tracking → breakdown table |
| Model mixing (opus/sonnet/haiku) | Cost optimization per agent complexity |
| `resume` / `session_id` | Resume analysis by slug (file-based persistence) |
| Custom MCP tools (`@tool`) | Expose lib/ functions as native tools |
| `include_partial_messages` | Real-time streaming to chat UI |
| `setting_sources=["project"]` | Load CLAUDE.md + shared-rules automatically |
| `AskUserQuestion` | All user interactions (presets, gates, re-run scope) |

---

## What's NOT in the POC

- Agent memory (`.claude/agent-memory/`) — skip
- Database — file-based persistence only
- OAuth/SSO — basic username isolation (external auth exists)
- Structured JSON output — raw markdown rendering
- Validation surfaced to user — internal only
- Mobile/responsive UI — desktop only
- Export to PDF/PPT — future enhancement
- Extended thinking — add later if reasoning quality needs improvement

---

## Estimated Effort

| Component | Effort | Notes |
|-----------|--------|-------|
| Agent loader (`agents.py`) | 1 day | Parse .md frontmatter → AgentDefinition |
| MCP tool wrappers (`mcp_tools.py`) | 1.5 days | Wrap 12 lib/ functions as @tool |
| Orchestrator prompt (`orchestrator.py`) | 1 day | Bake STDF DAG + rules into system prompt |
| Session manager (`sessions.py`) | 1 day | Per-user per-analysis ClaudeSDKClient lifecycle |
| Hooks (`hooks.py`) | 1 day | Progress, guardrails, question forwarding |
| FastAPI WebSocket server (`main.py`) | 1 day | Thin bridge: WebSocket ↔ ClaudeSDKClient |
| React chat panel + streaming | 3 days | Message list, markdown rendering, streaming |
| DAG sidebar visualization | 2 days | Node graph from hook events |
| AskUserQuestion renderer | 1 day | Interactive cards inline in chat |
| Analysis tabs (concurrency) | 1 day | Tab per analysis, each with own session |
| Integration testing | 1.5 days | End-to-end: query → pipeline → follow-up |
| **Total** | **~15 days** | **3 days saved** by eliminating Python pipeline manager |

### Why it's less effort

The previous design had a `PipelineManager` class (~200-400 lines) that duplicated
orchestration logic already in the `/stdf` skill. By making Claude the orchestrator:
- No DAG resolver in Python (Claude reads the Agent Registry)
- No failure matrix in Python (Claude applies rules from system prompt)
- No preset detector in Python (Claude understands natural language)
- No event system in Python (hooks capture progress passively)
- No AskUserQuestion forwarding logic (SDK handles it natively)
