# STDF Chat UI — Feature Implementation Spec

Comprehensive feature list derived from researching 3 open-source Claude Agent SDK projects:
- **Official Demos**: `anthropics/claude-agent-sdk-demos` (cloned at `/tmp/stdf-research/claude-agent-sdk-demos/`)
- **Agentrove**: `Mng-dev-ai/agentrove` (cloned at `/tmp/stdf-research/agentrove/`)
- **Claude Agent Kit**: `JimLiu/claude-agent-kit` (cloned at `/tmp/stdf-research/claude-agent-kit/`)

Each feature includes: what to build, source reference files, current state, dependencies, and effort estimate.

---

## TIER 1 — DROP-IN COPIES (< 30 min each)

### F01: Tool Metadata Registry
**What:** A mapping of every Claude Code tool name to icon (emoji), hex color, category, and description. Used by tool cards for consistent visual treatment.
**Current state:** No tool metadata — `ToolCallCard.tsx` just shows raw tool name.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/excel-demo/src/renderer/components/utils/toolMetadata.ts`
**What to copy:** The entire `TOOL_METADATA` record (18 tools), `getToolMetadata()`, `formatToolInput()`, `getFriendlyParameterName()`.
**Output:** New file `frontend/src/utils/toolMetadata.ts`
**Effort:** 10 min

### F02: Scroll-to-Bottom Button
**What:** A floating button that appears when the user scrolls up, allowing one-click scroll back to the latest message.
**Current state:** Auto-scroll via `useAutoScroll` hook exists, but no manual scroll-to-bottom button.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/chat-window/ScrollButton.tsx`
**Dependencies:** lucide-react (`ArrowDown` icon)
**Output:** New file `frontend/src/components/ScrollButton.tsx`, integrate into `ChatPanel.tsx`
**Effort:** 15 min

### F03: Improved ThinkingBlock with Active Animation
**What:** Replace current plain ThinkingBlock with animated version — bouncing dots during active thinking, Brain icon, preview text (first 60 chars) when collapsed, smooth CSS transition for expand/collapse.
**Current state:** Basic collapsible div with isExpanded toggle in `ThinkingBlock.tsx`.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/ThinkingBlock.tsx`
**Dependencies:** lucide-react (`Brain`, `ChevronRight` icons)
**Output:** Replace `frontend/src/components/ThinkingBlock.tsx`
**Effort:** 20 min

### F04: Connection Status Indicator
**What:** Green/red dot with "Connected"/"Disconnected" text in the header area.
**Current state:** `isConnected` state exists in store but is not displayed anywhere in the UI.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/simple-chatapp/client/components/ChatWindow.tsx` (lines 129-133)
**Output:** Modify `frontend/src/components/Header.tsx`
**Effort:** 10 min

---

## TIER 2 — COMPONENT UPGRADES (30 min – 2h each)

### F05: Universal ToolCard Component
**What:** A reusable tool card shell with: left icon (from F01 metadata), status indicator (green check = done, red X = failed, pulsing circle = running), dynamic title, expandable/collapsible content, optional action buttons slot. Replaces current `ToolCallCard`.
**Current state:** `ToolCallCard.tsx` — basic card with name, stringified input, running/done badge.
**Source files:**
- Shell: `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/common/ToolCard.tsx`
- Status icons: Same file, `statusIndicator` record
**Dependencies:** F01 (tool metadata), lucide-react (`Check`, `X`, `Circle`, `ChevronRight`)
**Output:** Replace `frontend/src/components/ToolCallCard.tsx` with new `ToolCard.tsx`
**Effort:** 45 min

### F06: Per-Tool Summary Line (Collapsed View)
**What:** When a tool card is collapsed, show a one-line summary instead of nothing. E.g., `Read → src/types.ts`, `Bash → npm install...`, `Grep → "pattern" in src/`, `WebSearch → query text`.
**Current state:** Tool input shown as raw JSON string.
**Source files:**
- Summary logic: `/tmp/stdf-research/claude-agent-sdk-demos/simple-chatapp/client/components/ChatWindow.tsx` (getToolSummary function, lines 23-43)
- Parameter formatting: `/tmp/stdf-research/claude-agent-sdk-demos/excel-demo/src/renderer/components/utils/toolMetadata.ts` (formatToolInput, getFriendlyParameterName)
**Dependencies:** F01, F05
**Output:** Integrate into the new ToolCard component
**Effort:** 30 min

### F07: Lazy-Loaded Tool Component Registry
**What:** A registry that maps tool names to lazy-loaded React components. Each tool type gets its own dedicated renderer (BashTool, FileOperationTool, GrepTool, etc.) loaded on demand. Unknown tools fall back to a generic renderer.
**Current state:** Single `ToolCallCard` handles all tools identically.
**Source files:**
- Registry pattern: `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/registry.tsx`
- Tool components (reference): `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/BashTool.tsx`, `FileOperationTool.tsx`, `GrepTool.tsx`, `GlobTool.tsx`, `WebSearch.tsx`, `AgentTool.tsx`
- Alternative (OOP factory): `/tmp/stdf-research/claude-agent-kit/examples/claude-code-web/src/client/components/messages/tool-use/tool-renderer-factory.tsx`
**Dependencies:** F05 (ToolCard shell)
**Output:** New files `frontend/src/components/tools/registry.tsx` + individual tool components
**Effort:** 2-3h (registry + 6-8 tool renderers)

**Individual tool renderers to create:**

#### F07a: BashTool Renderer
**What:** Shows `$ command` with monospace font, collapsible output in pre block.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/BashTool.tsx`
**Effort:** 20 min

#### F07b: FileOperationTool Renderer (Read/Write/Edit)
**What:** Read shows file path + line count. Edit shows inline diff (red old_string, green new_string). Write shows file path + line count.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/FileOperationTool.tsx`
**Effort:** 45 min

#### F07c: GrepTool Renderer
**What:** Shows pattern highlighted, path, glob filter, output mode as pills, results as file list or content.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/GrepTool.tsx`
**Effort:** 20 min

#### F07d: GlobTool Renderer
**What:** Shows glob pattern + matched file list.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/GlobTool.tsx`
**Effort:** 15 min

#### F07e: WebSearchTool Renderer
**What:** Shows search query, results as titled links.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/WebSearch.tsx`
**Effort:** 20 min

#### F07f: AgentTool Renderer
**What:** Nested agent card with expandable prompt/result/child-tools sections. Recursively renders child tool events.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/AgentTool.tsx`
**Dependencies:** F08 (segment builder for tool hierarchy)
**Effort:** 45 min

#### F07g: TodoWriteTool Renderer
**What:** Renders todo items with status icons (pending/in_progress/completed), priority colors.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/excel-demo/src/renderer/components/TodoListDisplay.tsx`
**Effort:** 20 min

#### F07h: WebFetchTool Renderer
**What:** Shows URL + prompt, collapsible result.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/WebFetchTool.tsx`
**Effort:** 15 min

### F08: Segment Builder (Event Stream → Structured UI Segments)
**What:** A pure function that converts a flat array of stream events into structured `MessageSegment[]` with types: `TextSegment`, `ThinkingSegment`, `ToolSegment` (with nested children), `SuggestionsSegment`. Handles:
- Text batching (consecutive text events → single segment)
- Thinking batching
- Tool parent-child hierarchy (Agent spawning subagents)
- Out-of-order events (child tool arriving before parent)
- Prompt suggestion extraction
**Current state:** Flat `blocks` array built incrementally via store actions (appendChunk, startToolCall, etc.). No tool hierarchy, no segment concept.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/segmentBuilder.ts` (~405 lines)
**Impact:** This is the most architecturally significant change. It replaces the current block-by-block store update pattern with a derived-state model: store raw events, build segments on render.
**Dependencies:** New types for `MessageSegment`, `ToolAggregate`
**Output:** New file `frontend/src/utils/segmentBuilder.ts`, new types in `types.ts`
**Effort:** 2-3h (adapt types and integrate with existing store)

### F09: Improved AskUserQuestion Component
**What:** Letter-keyed options (A, B, C...), multi-question pagination (prev/next with counter), "Other" free-text input option, auto-advance on single-select, answered state display with Q&A summary, Skip button.
**Current state:** Basic `AskUserQuestionCard.tsx` — functional but plain.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/AskUserQuestion.tsx` (~376 lines)
**Dependencies:** lucide-react (`HelpCircle`, `ChevronUp`, `ChevronDown`, `AlertCircle`)
**Output:** Replace `frontend/src/components/AskUserQuestionCard.tsx`
**Effort:** 1.5h

### F10: Token Usage / Cost Display Enhancement
**What:** Expandable metadata panel on assistant messages showing `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, cost in USD. Currently only shows total cost in `CostBadge`.
**Current state:** `CostBadge.tsx` shows aggregate cost per analysis. No per-message token breakdown.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/components/message/AssistantMessage.tsx` (metadata section)
**Dependencies:** Server must send token usage data per message (check current WS protocol)
**Output:** New component `frontend/src/components/MessageMetadata.tsx`, integrate into `ChatMessage.tsx`
**Effort:** 1h

### F11: TodoPanel Upgrade with Priority Colors and Interactive Checkboxes
**What:** Priority-colored todos (high=red, medium=yellow, low=green), interactive cross-off toggling, status icons, summary footer with counts.
**Current state:** `TodoPanel.tsx` exists with basic status badges.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/excel-demo/src/renderer/components/TodoListDisplay.tsx`
**Output:** Upgrade `frontend/src/components/TodoPanel.tsx`
**Effort:** 30 min

---

## TIER 3 — NEW FEATURES (1-3h each)

### F12: Tool Permission Inline Card
**What:** When the server requests permission for a tool call, show an inline card with: tool name in code badge, parameter display (each param with label + value), approve/reject buttons, optional feedback textarea for rejections.
**Current state:** No permission handling in the UI. Server runs in bypass mode.
**Source files:**
- Card: `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/ToolPermissionInline.tsx`
- Approval footer: `/tmp/stdf-research/agentrove/frontend/src/components/ui/shared/ApprovalFooter.tsx`
- Hook: `/tmp/stdf-research/agentrove/frontend/src/hooks/useApprovalState.ts`
**Dependencies:** New WS message type `permission_request`, new store actions
**Output:** New component `frontend/src/components/ToolPermissionCard.tsx`, new store actions, WS handler case
**Effort:** 2h

### F13: Prompt Suggestions (Clickable Follow-ups)
**What:** After an assistant message completes, show clickable suggestion chips that the user can tap to send as their next message. The agent provides these via `<prompt_suggestions>` tags.
**Current state:** Not implemented.
**Source files:**
- Component: `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/PromptSuggestions.tsx`
- Segment type: `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/segmentBuilder.ts` (SuggestionsSegment)
- Parsing: `/tmp/stdf-research/agentrove/frontend/src/utils/stream.ts` (PROMPT_SUGGESTIONS_RE)
**Dependencies:** F08 (segment builder) or standalone parsing
**Output:** New component `frontend/src/components/PromptSuggestions.tsx`, integrate into ChatMessage
**Effort:** 1h

### F14: Context Usage Indicator (Circular Progress)
**What:** SVG circular progress showing context window usage percentage. Color coding: normal (< 75%), warning (75-95% yellow), error (> 95% red). Tooltip shows "142k/200k" format. Positioned in the input area.
**Current state:** Not implemented.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-input/ContextUsageIndicator.tsx`
**Dependencies:** Server must send context usage data (could piggyback on existing `done` message)
**Output:** New component `frontend/src/components/ContextUsageIndicator.tsx`, integrate into MessageInput area
**Effort:** 1.5h

### F15: Message Actions (Copy, Retry)
**What:** On hover over a message, show action buttons: Copy (copies markdown to clipboard), Retry (re-sends the previous user message). Appears as a floating toolbar above/below the message bubble.
**Current state:** Not implemented.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/MessageActions.tsx`
**Dependencies:** lucide-react icons, clipboard API
**Output:** New component `frontend/src/components/MessageActions.tsx`, integrate into ChatMessage
**Effort:** 1h

### F16: Offline Message Queue
**What:** Messages sent while WebSocket is disconnected are queued locally and flushed when connection is restored. Prevents message loss during brief disconnections.
**Current state:** `useWebSocket` has auto-reconnect but no message queue — messages sent while disconnected are silently dropped.
**Source files:**
- Queue pattern: `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/hooks/useWebSocket.ts`
- Also: `/tmp/stdf-research/claude-agent-kit/examples/claude-code-web/src/client/hooks/use-web-socket.ts`
**Output:** Modify `frontend/src/hooks/useWebSocket.ts` to add queue
**Effort:** 45 min

### F17: Read Tool Coalescing
**What:** When the agent reads multiple files consecutively, instead of showing N separate Read tool cards, show a single "Read N files" card with an expandable file list. Reduces visual noise for file-heavy operations.
**Current state:** Each Read shows as a separate ToolCallCard.
**Source:** `/tmp/stdf-research/claude-agent-kit/packages/messages/src/messages/messages.ts` (coalesceReadMessages function)
**Output:** New utility `frontend/src/utils/coalesceTools.ts`, integrate into message rendering
**Effort:** 1.5h

### F18: Thinking Mode Selector
**What:** Dropdown in the input area to control extended thinking: Off / Low (4k) / Medium (10k) / High (15k) / Ultra (32k). Sends the preference to the server.
**Current state:** Not implemented — server controls thinking mode.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/thinking-mode-selector/ThinkingModeSelector.tsx`
**Dependencies:** Server must accept thinking mode preference, WS protocol extension
**Output:** New component `frontend/src/components/ThinkingModeSelector.tsx`, integrate into MessageInput controls area
**Effort:** 1h

### F19: Permission Mode Selector
**What:** Dropdown to switch between permission modes: Auto (bypass), Ask (per-action approval), Plan (review steps before execution).
**Current state:** Not implemented — server decides.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/permission-mode-selector/PermissionModeSelector.tsx`
**Dependencies:** F12 (permission card), server support
**Output:** New component `frontend/src/components/PermissionModeSelector.tsx`
**Effort:** 1h

### F20: Enhanced PlanApprovalCard with Streamdown
**What:** Upgrade the plan approval card: show the plan using Streamdown (already integrated), add a "Reject with feedback" flow where the user can type why they're rejecting, show allowed permissions as a checklist.
**Current state:** Basic card with Streamdown rendering (from our earlier change), approve/reject buttons.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/tools/PlanModeTool.tsx`
**Output:** Upgrade `frontend/src/components/PlanApprovalCard.tsx`
**Effort:** 45 min

---

## TIER 4 — ARCHITECTURAL IMPROVEMENTS (2-4h each)

### F21: Stream Flush Timer (Batched Re-renders)
**What:** Instead of updating React state on every WS message, batch updates with a 130ms flush timer. Accumulate events in a mutable buffer, then flush to state on timer tick. Prevents excessive re-renders during fast streaming.
**Current state:** Every WS message triggers a Zustand state update → React re-render. During fast streaming, this can cause hundreds of re-renders per second.
**Source files:**
- Flush pattern: `/tmp/stdf-research/agentrove/frontend/src/hooks/useStreamCallbacks.ts` (scheduleProjection with STREAM_FLUSH_INTERVAL_MS = 130)
- Accumulator: `/tmp/stdf-research/agentrove/frontend/src/utils/stream.ts` (StreamingContentAccumulator class)
**Impact:** Major performance improvement for long-running agent sessions.
**Output:** New `frontend/src/utils/StreamAccumulator.ts`, modify `useWebSocket.ts` to batch updates
**Effort:** 2-3h

### F22: Event-Based Store (Raw Events + Derived Segments)
**What:** Instead of the current approach where each WS message type has its own store action that mutates the messages/blocks array, store raw events and derive the UI segment tree on render. This is a more robust architecture:
- Store appends raw `AssistantStreamEvent[]` per message
- `buildSegments(events)` (F08) is called during render (or memoized)
- Tool hierarchy, text batching, etc. are all derived, not manually maintained
**Current state:** ~15 store actions manually build the blocks array (appendChunk, startToolCall, appendToolInput, endToolCall, addSubToolCall, etc.)
**Impact:** Eliminates an entire class of bugs around block ordering and tool hierarchy. Makes it trivial to add new event types.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-bubble/segmentBuilder.ts` + `/tmp/stdf-research/agentrove/frontend/src/types/stream.types.ts`
**Dependencies:** F08 (segment builder)
**Output:** Refactor `useAnalysisStore.ts` to store events, add derived segments
**Effort:** 3-4h (significant refactor)

### F23: Stream Reconnection / Resumability
**What:** Track sequence numbers for each active stream. On page reload or reconnect, pass `after_seq` to the server to resume from the last received event. No data loss across disconnections.
**Current state:** On reconnect, server sends a `sync` message with active session statuses, but no event replay.
**Source files:**
- Seq tracking: `/tmp/stdf-research/agentrove/frontend/src/types/stream.types.ts` (StreamEnvelope.seq)
- Reconnection hook: `/tmp/stdf-research/agentrove/frontend/src/hooks/useStreamRestoration.ts`
- Reconnect mid-session: `/tmp/stdf-research/agentrove/frontend/src/hooks/useStreamReconnect.ts`
**Dependencies:** Server must support seq-based event replay
**Output:** Modify `useWebSocket.ts` to track seq, new reconnection logic
**Effort:** 2-3h (frontend) + server changes

### F24: Session Manager Pattern (Multi-Session Server)
**What:** Server-side session management with: session pool, subscribe/unsubscribe per client, fan-out to multiple clients, SDK options composition, session resume via JSONL files.
**Current state:** Server handles sessions but the exact pattern isn't documented here.
**Source files:**
- Session manager: `/tmp/stdf-research/claude-agent-kit/packages/server/src/server/session-manager.ts`
- Session: `/tmp/stdf-research/claude-agent-kit/packages/server/src/server/session.ts`
- Client interface: `/tmp/stdf-research/claude-agent-kit/packages/server/src/types/client.ts`
- WS handler: `/tmp/stdf-research/claude-agent-kit/packages/websocket/src/websocket-handler.ts`
**Impact:** Production-grade session management for the backend.
**Output:** Server-side implementation (not frontend)
**Effort:** 3-4h

---

## TIER 5 — ADVANCED FEATURES (3h+ each)

### F25: Slash Command Input Panel
**What:** Typing `/` in the message input triggers an autocomplete panel showing available slash commands with descriptions. Selecting a command inserts it into the input.
**Current state:** Not implemented.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-input/SlashCommandsPanel.tsx`
**Dependencies:** Command list from server or static config
**Output:** New component, modify `MessageInput.tsx` to detect `/` prefix
**Effort:** 2h

### F26: @Mention File Suggestions
**What:** Typing `@` in the message input triggers a fuzzy-search file picker. Selected files are attached as context to the message.
**Current state:** Not implemented.
**Source files:**
- Panel: `/tmp/stdf-research/agentrove/frontend/src/components/chat/message-input/MentionSuggestionsPanel.tsx`
- Hook: `/tmp/stdf-research/agentrove/frontend/src/hooks/useMentionSuggestions.ts`
- Parser: `/tmp/stdf-research/agentrove/frontend/src/utils/mentionParser.ts`
**Dependencies:** File list API from server, fuzzy search (fuzzysort lib)
**Output:** New components, modify MessageInput
**Effort:** 3-4h

### F27: Split/Mosaic View
**What:** Tiled window manager allowing chat + output viewer + todo panel to be arranged as resizable panes. Shift+click to add a tile.
**Current state:** Fixed layout: sidebar | chat + todo panel.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/components/ui/MosaicSplitView.tsx`
**Dependencies:** `react-mosaic-component` library
**Output:** New layout system
**Effort:** 4-6h

### F28: Dark Mode
**What:** Full dark mode support with system preference detection and manual toggle. CSS custom properties already partially set up (from Streamdown integration in `index.css`).
**Current state:** Light mode only. `.dark` CSS variables exist but no toggle.
**Source:** `/tmp/stdf-research/agentrove/frontend/src/store/uiStore.ts` (theme: 'light' | 'dark' | 'system')
**Dependencies:** Tailwind dark mode classes throughout all components
**Output:** Theme toggle in Header, `useMediaQuery` for system pref, Tailwind `dark:` classes
**Effort:** 3-4h (touching many files)

### F29: Dynamic Component Rendering in Chat
**What:** Allow the agent to embed custom React components inline in the chat (e.g., data tables, charts, dashboards). Components are registered in a registry and rendered by name.
**Current state:** Not implemented.
**Source files:**
- Renderer: `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/components/message/ComponentRenderer.tsx`
- Registry: `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/components/custom/ComponentRegistry.ts`
- Task board example: `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/components/custom/TaskBoard.tsx`
**Impact:** Enables rich interactive output from STDF analyses (cost curve charts, adoption curves, etc.)
**Output:** New component system
**Effort:** 4-6h

### F30: Action Buttons on Messages
**What:** Executable action buttons attached to assistant messages. E.g., "Open output folder", "Download report", "Run validation". Server attaches action metadata to messages.
**Current state:** Not implemented.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/client/components/ActionButton.tsx`
**Dependencies:** Server must send action metadata with messages
**Output:** New component, WS protocol extension
**Effort:** 2-3h

### F31: V2 Session API Integration
**What:** Migrate from the V1 `query()` generator to V2 Session API (`unstable_v2_createSession`, `session.send()`, `session.stream()`). Cleaner multi-turn conversation support with explicit session lifecycle.
**Current state:** Server uses V1 query() pattern.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/hello-world-v2/v2-examples.ts`
**Impact:** Server-side change. Enables cleaner session resume, explicit session cleanup.
**Output:** Server modification
**Effort:** 3-4h

---

## IMPLEMENTATION ORDER (Recommended)

### Phase 1 — Quick Visual Wins (Day 1, ~3h)
1. F01: Tool Metadata Registry (10 min)
2. F03: ThinkingBlock with Animation (20 min)
3. F04: Connection Status Indicator (10 min)
4. F02: Scroll-to-Bottom Button (15 min)
5. F05: Universal ToolCard Component (45 min)
6. F06: Per-Tool Summary Line (30 min)
7. F11: TodoPanel Upgrade (30 min)

### Phase 2 — Tool Rendering System (Day 2, ~4h)
8. F07: Lazy Tool Registry + Tool Renderers (F07a-F07h) (3h)
9. F17: Read Tool Coalescing (1h)

### Phase 3 — Streaming & Architecture (Day 3, ~5h)
10. F08: Segment Builder (2-3h)
11. F21: Stream Flush Timer (2h)

### Phase 4 — Interactive Features (Day 4, ~5h)
12. F09: AskUserQuestion Upgrade (1.5h)
13. F13: Prompt Suggestions (1h)
14. F15: Message Actions (Copy, Retry) (1h)
15. F16: Offline Message Queue (45 min)
16. F20: PlanApprovalCard Upgrade (45 min)

### Phase 5 — Input Enhancements (Day 5, ~4h)
17. F18: Thinking Mode Selector (1h)
18. F19: Permission Mode Selector (1h)
19. F14: Context Usage Indicator (1.5h)
20. F10: Token Usage Display (1h)

### Phase 6 — Advanced (Future)
21. F12: Tool Permission Card (2h)
22. F22: Event-Based Store Refactor (3-4h)
23. F23: Stream Reconnection (2-3h)
24. F25: Slash Commands (2h)
25. F26: @Mention Files (3-4h)
26. F28: Dark Mode (3-4h)
27. F29: Dynamic Components (4-6h)
28. F30: Action Buttons (2-3h)

---

## REFERENCE: Current STDF Frontend Files

| File | Purpose | Features Using It |
|------|---------|-------------------|
| `src/types.ts` | Type definitions (blocks, messages, analysis) | F05, F07, F08, F09, F12, F22 |
| `src/stores/useAnalysisStore.ts` | Zustand store (messages, blocks, state) | F08, F16, F21, F22 |
| `src/hooks/useWebSocket.ts` | WebSocket connection + message dispatch | F16, F21, F23 |
| `src/hooks/useAutoScroll.ts` | Auto-scroll on new messages | F02 |
| `src/components/ChatMessage.tsx` | Message rendering (Streamdown) | F05, F07, F08, F10, F13, F15 |
| `src/components/ToolCallCard.tsx` | Tool call display | F05, F06, F07 (replaced) |
| `src/components/ThinkingBlock.tsx` | Thinking block display | F03 (replaced) |
| `src/components/AskUserQuestionCard.tsx` | Ask user question UI | F09 (replaced) |
| `src/components/PlanApprovalCard.tsx` | Plan approval UI | F20 (upgraded) |
| `src/components/TodoPanel.tsx` | Todo list sidebar | F11 (upgraded) |
| `src/components/CostBadge.tsx` | Cost display | F10, F14 |
| `src/components/MessageInput.tsx` | Chat input | F14, F18, F19, F25, F26 |
| `src/components/Header.tsx` | Top header bar | F04, F28 |
| `src/components/ChatPanel.tsx` | Chat message list container | F02, F13 |
| `src/components/StreamingIndicator.tsx` | Streaming status indicator | F21 |
| `src/components/AnalysisTabs.tsx` | Analysis tab sidebar | — |
| `src/App.tsx` | Root app component | F27 |
| `src/index.css` | Global styles + Streamdown CSS vars | F28 |
| `src/constants.ts` | WS_URL constant | F16, F23 |

---

## REFERENCE: Source Repo Locations

All repos cloned at `/tmp/stdf-research/`:

```
/tmp/stdf-research/claude-agent-sdk-demos/     # Official Anthropic demos
/tmp/stdf-research/agentrove/                  # Agentrove (claudex)
/tmp/stdf-research/claude-agent-kit/           # Claude Agent Kit
```

These clones are shallow (`--depth 1`). They may be cleared on reboot — re-clone if needed.

---

## APPENDIX: Server-Side Patterns (from Solo IDE + Agent Kit)

These patterns apply to the STDF WebSocket server, not the frontend. Include them when agents work on server features.

### S01: MessageQueue Async Iterator
**What:** Instead of calling `query()` per user message, create a persistent async iterator (MessageQueue) that the SDK consumes across multiple turns. New user messages are pushed into the queue.
**Source:** Solo IDE blog post — `MessageQueue` class with push/pull resolver pattern.
**Also:** `/tmp/stdf-research/claude-agent-sdk-demos/simple-chatapp/server/ai-client.ts` (same pattern)
**Why:** Enables true multi-turn conversations within a single `query()` call. No need for session resume.

### S02: includePartialMessages: true
**What:** Pass `includePartialMessages: true` in SDK `query()` options. Without this, the SDK only yields complete messages — no streaming deltas.
**Source:** Solo IDE blog post.
**Impact:** Required for any streaming UI. Enables text_delta and thinking_delta events.

### S03: Permission Gate via canUseTool Callback
**What:** Implement `canUseTool(toolName, toolInput)` that creates a dangling Promise, sends a permission request to the client via WS, and resolves only when the client responds.
**Source:** Solo IDE blog post (9-step flow) + `/tmp/stdf-research/claude-agent-sdk-demos/ask-user-question-previews/server.ts`
**Also set:** `CLAUDE_CODE_STREAM_CLOSE_TIMEOUT=86400000` to prevent stream timeout during long waits.
**Dependencies:** F12 (frontend permission card), F19 (permission mode selector)

### S04: Session Resume via session_id
**What:** Capture `session_id` from the first `system/init` SDK message. On subsequent messages, pass `{ resume: sessionId }` to maintain context.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/email-agent/ccsdk/session.ts`
**Also:** `/tmp/stdf-research/claude-agent-kit/packages/server/src/server/session.ts`
**Current state:** STDF server already captures sessionId and passes it back on follow-up messages.

### S05: V2 Session API
**What:** Migrate from `query()` generator to `unstable_v2_createSession()` + `session.send()` / `session.stream()`. Cleaner lifecycle, supports `await using` for cleanup.
**Source:** `/tmp/stdf-research/claude-agent-sdk-demos/hello-world-v2/v2-examples.ts`
**Impact:** Future improvement when V2 API stabilizes.

### S06: Session Fan-Out (Multi-Client)
**What:** `Session` maintains a `Set<ISessionClient>` and broadcasts events via `notifyClients()`. Multiple browser tabs can observe the same session.
**Source:** `/tmp/stdf-research/claude-agent-kit/packages/server/src/server/session.ts`

### S07: JSONL Session Persistence
**What:** Sessions persisted as JSONL files at `~/.claude/projects/{project-id}/{session-id}.jsonl`. Utility scans project dirs to find session files by ID. Messages parsed line-by-line with lenient error handling.
**Source:** `/tmp/stdf-research/claude-agent-kit/packages/server/src/utils/session-files.ts`
