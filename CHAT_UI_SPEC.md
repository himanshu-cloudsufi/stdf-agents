# STDF Chat UI — POC Implementation Spec

## Architecture

```
┌──────────────────────────────────────────────┐
│  React + Tailwind UI                          │
│  [Analysis Tabs]  [Chat Panel + Streaming]    │
└────────────────────┬─────────────────────────┘
                     │ WebSocket
                     ▼
┌──────────────────────────────────────────────┐
│  FastAPI — server/main.py (~80 lines)        │
│  Session dict + WebSocket ↔ SDK bridge       │
└────────────────────┬─────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────┐
│  ClaudeSDKClient (one per user per analysis)  │
│                                               │
│  setting_sources=["user", "project"] loads:   │
│    .claude/agents/*.md   → 16 subagent defs  │
│    CLAUDE.md             → DAG, presets       │
│    .claude/settings.json → hooks, permissions │
│                                               │
│  Claude streams its orchestration as text:    │
│    "Launching Phase 1: domain-disruption,     │
│     cost-researcher, capability..."           │
│    "✓ cost-researcher complete (14s)"         │
│    "Phase 2: cost-fitter..."                  │
│    "Pipeline complete. Key findings: ..."     │
│                                               │
│  File I/O: output/<slug>/agents/*.md          │
└──────────────────────────────────────────────┘
```

Progress is just Claude's text streaming into the chat. No separate DAG UI, no progress hooks, no stream event parsing for tool calls.

---

## Decisions

| Decision | Choice |
|----------|--------|
| Pipeline progress | Claude's streamed text (no separate UI) |
| Multi-user | Isolated per user (basic username) |
| Output format | Raw markdown via react-markdown |
| Follow-ups | Read-only by default, user says "re-run" for re-execution |
| Interactions | AskUserQuestion → rendered as inline buttons |
| Persistence | File-based (output files + session IDs on disk) |
| Concurrent analyses | Multiple per user, one tab each |
| Lib modules | Agents call via Bash (unchanged) |
| Validation | Internal only (existing shell hooks) |
| Frontend | React + Tailwind |

---

## Backend — `server/main.py`

### What the SDK handles

| Thing | Custom Python? |
|-------|---------------|
| 16 agent definitions | No — `setting_sources` loads `.claude/agents/*.md` |
| CLAUDE.md (DAG, presets, rules) | No — injected as system context |
| Guardrail hooks | No — shell hooks from `settings.json` fire automatically |
| Permission rules | No — loaded from `settings.json` |
| lib/ computation | No — agents call via Bash as today |

### What Python does

1. **Create sessions** (one `ClaudeSDKClient` per user per analysis)
2. **Bridge WebSocket ↔ SDK** (forward text stream + cost)

### Code

```python
import asyncio
import os
import re
from datetime import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, ResultMessage
from claude_agent_sdk.types import StreamEvent

app = FastAPI()
sessions: dict[str, dict[str, ClaudeSDKClient]] = {}
REPO_ROOT = os.environ.get("STDF_ROOT", os.getcwd())


async def get_or_create_session(user_id: str, slug: str) -> ClaudeSDKClient:
    user_sessions = sessions.setdefault(user_id, {})
    if slug not in user_sessions:
        client = ClaudeSDKClient(options=ClaudeAgentOptions(
            model="claude-opus-4-6",
            system_prompt={
                "type": "preset",
                "preset": "claude_code",
                "append": (
                    f"You are the STDF analysis assistant in a chat UI.\n"
                    f"Output directory: output/{slug}/agents/\n"
                    f"User: {user_id} | Date: {datetime.now():%Y-%m-%d}\n\n"
                    f"Use AskUserQuestion for ALL user interactions.\n"
                    f"After pipeline completes, read 00-final-synthesis.md "
                    f"and present key findings. Then answer follow-ups."
                ),
            },
            setting_sources=["user", "project"],
            allowed_tools=[
                "Read", "Write", "Edit", "Bash", "Glob", "Grep",
                "Agent", "AskUserQuestion", "WebSearch", "WebFetch",
            ],
            permission_mode="bypassPermissions",
            include_partial_messages=True,
            cwd=REPO_ROOT,
            max_budget_usd=5.00,
        ))
        await client.__aenter__()
        user_sessions[slug] = client
    return user_sessions[slug]


@app.websocket("/ws/{user_id}")
async def chat(websocket: WebSocket, user_id: str):
    await websocket.accept()
    try:
        while True:
            msg = await websocket.receive_json()
            slug = msg.get("slug") or generate_slug(msg.get("query", ""))
            text = msg.get("text") or msg.get("query") or msg.get("answer", "")
            client = await get_or_create_session(user_id, slug)
            asyncio.create_task(stream_to_ws(client, text, slug, websocket))
    except WebSocketDisconnect:
        pass


async def stream_to_ws(client: ClaudeSDKClient, text: str, slug: str, ws: WebSocket):
    await client.query(text)
    async for event in client.receive_response():
        if isinstance(event, StreamEvent):
            raw = event.event
            if raw.get("type") == "content_block_delta":
                delta = raw.get("delta", {})
                if delta.get("type") == "text_delta":
                    await ws.send_json({
                        "type": "text", "slug": slug,
                        "chunk": delta.get("text", ""),
                    })
        elif isinstance(event, ResultMessage):
            await ws.send_json({
                "type": "done", "slug": slug,
                "cost": event.total_cost_usd,
                "session_id": event.session_id,
            })


def generate_slug(query: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', query.lower())[:50].strip('-')
    return f"{slug}-{datetime.now():%Y%m%d-%H%M%S}"
```

That's it. ~80 lines. The only stream event we forward is `text_delta` — Claude's words appearing in the chat.

---

## Frontend

### Layout

```
┌─────────────────────────────────────────────┐
│  STDF Analysis Platform          [username]  │
├──────────┬──────────────────────────────────┤
│          │                                   │
│ Analysis │  ┌─────────────────────────────┐  │
│  Tabs    │  │ User: Analyze the energy    │  │
│          │  │ storage disruption          │  │
│ [Energy  │  ├─────────────────────────────┤  │
│  Storage]│  │ Assistant: Running pipeline │  │
│          │  │ Phase 1: domain-disruption, │  │
│ [Auto-   │  │ cost-researcher, capability │  │
│  nomous] │  │ ✓ cost-researcher (14s)     │  │
│          │  │ ✓ domain-disruption (18s)   │  │
│ [+ New]  │  │ ...                         │  │
│          │  ├─────────────────────────────┤  │
│          │  │ [AskUserQuestion card]      │  │
│          │  │ ┌──────┐ ┌───────┐         │  │
│          │  │ │ FULL │ │ QUICK │         │  │
│          │  │ └──────┘ └───────┘         │  │
│          │  ├─────────────────────────────┤  │
│          │  │ ▌Streaming text...          │  │
│          │  └─────────────────────────────┘  │
│          │  [Type a message...]              │
├──────────┴──────────────────────────────────┤
│                              Cost: $0.45     │
└─────────────────────────────────────────────┘
```

### Components

| Component | Purpose |
|-----------|---------|
| `App.tsx` | Layout, tab state, WebSocket provider |
| `AnalysisTabs` | Tab bar — one tab per analysis. `[+ New]` creates new session |
| `ChatPanel` | Message list + streaming text. Renders markdown via `react-markdown` |
| `MessageInput` | Text input + send button |
| `AskUserQuestionCard` | Renders AskUserQuestion tool calls as inline button groups |
| `CostBadge` | Shows `$0.45` from `ResultMessage.total_cost_usd` after completion |

### WebSocket Hook

```ts
// frontend/src/hooks/useWebSocket.ts
function useWebSocket(userId: string) {
  const ws = useRef<WebSocket>();
  const [analyses, setAnalyses] = useState<Map<string, Analysis>>();

  useEffect(() => {
    ws.current = new WebSocket(`ws://localhost:8000/ws/${userId}`);
    ws.current.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      switch (msg.type) {
        case "text":
          // Append chunk to current message for this analysis
          appendToMessage(msg.slug, msg.chunk);
          break;
        case "done":
          // Mark analysis complete, show cost
          markComplete(msg.slug, msg.cost);
          break;
      }
    };
  }, [userId]);

  const send = (slug: string, text: string) =>
    ws.current?.send(JSON.stringify({ slug, text }));

  const newAnalysis = (query: string) =>
    ws.current?.send(JSON.stringify({ query }));

  return { analyses, send, newAnalysis };
}
```

### AskUserQuestion Detection

Claude's AskUserQuestion tool calls appear in the stream as tool_use blocks. The frontend detects them from the text pattern (Claude writes the question text before the tool call) or by checking for `tool_start` events in the stream. For POC, simplest approach: Claude's text naturally includes the question — user just types their answer in the chat input.

If richer rendering is needed later, detect `content_block_start` with `name: "AskUserQuestion"` in the stream and render a button card.

---

## File Structure

```
stdf-agents/
├── server/
│   └── main.py                 # Entire backend (~80 lines)
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── MessageInput.tsx
│   │   │   ├── AnalysisTabs.tsx
│   │   │   └── CostBadge.tsx
│   │   ├── hooks/
│   │   │   └── useWebSocket.ts
│   │   └── types.ts
│   └── tailwind.config.js
├── .claude/                    # UNCHANGED (SDK loads automatically)
├── CLAUDE.md                   # UNCHANGED (SDK loads automatically)
├── lib/                        # UNCHANGED
├── data/                       # UNCHANGED
└── output/                     # UNCHANGED
```

---

## Effort

| Component | Days |
|-----------|------|
| `server/main.py` | 1 |
| Chat panel + streaming | 2 |
| Analysis tabs | 1 |
| AskUserQuestion card (optional) | 0.5 |
| Integration testing | 0.5 |
| **Total** | **~5 days** |
