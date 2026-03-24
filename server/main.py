"""STDF Chat UI — FastAPI backend.

Bridges WebSocket connections from the React frontend to Claude Agent SDK.
Each user gets an isolated ClaudeSDKClient per analysis session.
Sessions survive page reloads — WS disconnect does NOT kill running processes.
"""

from __future__ import annotations

import asyncio
import logging
import os
import re
import time
from datetime import datetime, timezone
from typing import Any

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    StreamEvent,
)
from claude_agent_sdk.types import (
    PermissionResultAllow,
    ToolPermissionContext,
)
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="STDF Chat UI", version="0.1.0")
logger = logging.getLogger("stdf-server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://del-c4x772g7hx.tail99fe31.ts.net",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# WsHolder — mutable WebSocket reference that survives reconnections
# ---------------------------------------------------------------------------
class WsHolder:
    """Closures in make_can_use_tool and stream_to_ws capture a WsHolder
    instead of a raw WebSocket. On disconnect the ws is nulled; on reconnect
    it is swapped to the new WebSocket."""

    def __init__(self, ws: WebSocket | None = None):
        self._ws: WebSocket | None = ws

    @property
    def ws(self) -> WebSocket | None:
        return self._ws

    def set_ws(self, ws: WebSocket | None) -> None:
        self._ws = ws

    async def safe_send(self, data: dict) -> bool:
        """Send JSON, swallowing errors if WS is disconnected. Returns True if sent."""
        ws = self._ws
        if ws is None:
            return False
        try:
            await ws.send_json(data)
            return True
        except Exception:
            self._ws = None
            return False


# ---------------------------------------------------------------------------
# Global state
# ---------------------------------------------------------------------------
# Sessions: user_id -> slug -> ClaudeSDKClient
sessions: dict[str, dict[str, ClaudeSDKClient]] = {}
# WsHolder per user: user_id -> WsHolder
ws_holders: dict[str, WsHolder] = {}
# Per-slug locks to prevent concurrent queries on the same client
slug_locks: dict[str, asyncio.Lock] = {}
# Pending interactive prompts: slug -> {future, type, payload}
pending_prompts: dict[str, dict[str, Any]] = {}
# Cached plan content: slug -> plan markdown (captured from Write tool)
plan_content_cache: dict[str, str] = {}
# Session metadata: slug -> {query, created_at, session_id}
session_meta: dict[str, dict[str, Any]] = {}
# Active streaming tasks: slug -> asyncio.Task
active_tasks: dict[str, asyncio.Task] = {}
# Session last-activity timestamp: slug -> float
session_last_active: dict[str, float] = {}

REPO_ROOT = os.environ.get(
    "STDF_ROOT",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

ABANDON_TIMEOUT_SEC = 1800  # 30 minutes


def generate_slug(query: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", query.lower())[:50].strip("-")
    return f"{slug}-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}"


# ---------------------------------------------------------------------------
# can_use_tool callback — uses WsHolder for resilient sends
# ---------------------------------------------------------------------------
def make_can_use_tool(slug: str, ws_holder: WsHolder):
    """Create a can_use_tool callback that intercepts AskUserQuestion."""

    async def can_use_tool(
        tool_name: str,
        tool_input: dict[str, Any],
        context: ToolPermissionContext,
    ):
        # Capture plan file content when Write tool targets a plans path
        if tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            if "plans/" in file_path and file_path.endswith(".md"):
                content = tool_input.get("content", "")
                if content:
                    plan_content_cache[slug] = content
                    logger.info(
                        "Captured plan content for slug=%s from %s (%d chars)",
                        slug,
                        file_path,
                        len(content),
                    )
            return PermissionResultAllow()

        # Intercept TodoWrite and forward to frontend
        if tool_name == "TodoWrite":
            todos = tool_input.get("todos", [])
            await ws_holder.safe_send(
                {"type": "todo_update", "slug": slug, "todos": todos}
            )
            logger.info(
                "TodoWrite intercepted for slug=%s, %d todos", slug, len(todos)
            )
            return PermissionResultAllow()

        if tool_name == "AskUserQuestion":
            logger.info("AskUserQuestion intercepted for slug=%s", slug)
            payload = {"questions": tool_input.get("questions", [])}
            await ws_holder.safe_send(
                {"type": "ask_user", "slug": slug, **payload}
            )
            future: asyncio.Future = asyncio.get_event_loop().create_future()
            pending_prompts[slug] = {
                "future": future,
                "type": "ask_user",
                "payload": payload,
            }
            try:
                answers = await asyncio.wait_for(future, timeout=300)
            except asyncio.TimeoutError:
                answers = {}
            finally:
                pending_prompts.pop(slug, None)
            return PermissionResultAllow(
                updated_input={
                    "questions": tool_input.get("questions", []),
                    "answers": answers,
                },
            )

        if tool_name == "ExitPlanMode":
            logger.info("ExitPlanMode intercepted for slug=%s", slug)
            # Use cached plan content (captured from Write tool), fall back to disk
            plan_content = plan_content_cache.pop(slug, "")
            if plan_content:
                logger.info(
                    "Using cached plan content for slug=%s (%d chars)",
                    slug,
                    len(plan_content),
                )
            else:
                # Fallback: search .claude/plans dirs for recently written files only
                import glob

                now = time.time()
                for plans_dir in [
                    os.path.join(REPO_ROOT, ".claude", "plans"),
                    os.path.join(os.path.expanduser("~"), ".claude", "plans"),
                ]:
                    try:
                        plan_files = sorted(
                            glob.glob(os.path.join(plans_dir, "*.md")),
                            key=os.path.getmtime,
                            reverse=True,
                        )
                        for pf in plan_files:
                            if now - os.path.getmtime(pf) < 120:
                                with open(pf) as f:
                                    plan_content = f.read()
                                logger.info("Read plan from %s", pf)
                                break
                        if plan_content:
                            break
                    except Exception:
                        continue
                if not plan_content:
                    logger.warning("No plan content found for slug=%s", slug)

            payload = {
                "plan": plan_content,
                "allowedPrompts": tool_input.get("allowedPrompts", []),
            }
            await ws_holder.safe_send(
                {"type": "plan_approval", "slug": slug, **payload}
            )
            future = asyncio.get_event_loop().create_future()
            pending_prompts[slug] = {
                "future": future,
                "type": "plan_approval",
                "payload": payload,
            }
            try:
                result = await asyncio.wait_for(future, timeout=300)
            except asyncio.TimeoutError:
                result = {"approved": True}
            finally:
                pending_prompts.pop(slug, None)

            if result.get("approved", True):
                return PermissionResultAllow(
                    updated_input={"plan": "User approved", "isAgent": False},
                )
            else:
                from claude_agent_sdk.types import PermissionResultDeny

                return PermissionResultDeny(
                    message=result.get("feedback", "User rejected the plan"),
                )

        # Log all tool calls for debugging
        logger.info("Tool allowed: %s for slug=%s", tool_name, slug)
        return PermissionResultAllow()

    return can_use_tool


# ---------------------------------------------------------------------------
# Session lifecycle
# ---------------------------------------------------------------------------
async def get_or_create_session(
    user_id: str,
    slug: str,
    ws_holder: WsHolder,
    session_id: str | None = None,
) -> ClaudeSDKClient:
    user_sessions = sessions.setdefault(user_id, {})
    if slug not in user_sessions:
        opts: dict[str, Any] = {
            "model": "claude-opus-4-6",
            "system_prompt": {
                "type": "preset",
                "preset": "claude_code",
                "append": (
                    f"You are the STDF analysis assistant in a chat UI.\n"
                    f"Output directory: output/{slug}/agents/\n"
                    f"User: {user_id} | Date: {datetime.now(timezone.utc):%Y-%m-%d}\n\n"
                    f"Use AskUserQuestion for ALL user interactions.\n"
                    f"After pipeline completes, read 00-final-synthesis.md "
                    f"and present key findings. Then answer follow-ups."
                ),
            },
            "setting_sources": ["user", "project"],
            "allowed_tools": [
                "Read",
                "Write",
                "Edit",
                "Bash",
                "Glob",
                "Grep",
                "Agent",
                "AskUserQuestion",
                "WebSearch",
                "WebFetch",
            ],
            "can_use_tool": make_can_use_tool(slug, ws_holder),
            "include_partial_messages": True,
            "cwd": REPO_ROOT,
            "max_budget_usd": 20.00,
        }
        # Resume previous session if session_id provided
        if session_id:
            opts["resume"] = session_id
            logger.info(
                "Resuming session slug=%s with session_id=%s", slug, session_id
            )

        client = ClaudeSDKClient(options=ClaudeAgentOptions(**opts))
        await client.__aenter__()
        user_sessions[slug] = client
    return user_sessions[slug]


# ---------------------------------------------------------------------------
# Resilient streaming — keeps consuming SDK events even if WS is disconnected
# ---------------------------------------------------------------------------
async def stream_to_ws(
    client: ClaudeSDKClient,
    text: str,
    slug: str,
    ws_holder: WsHolder,
) -> None:
    lock = slug_locks.setdefault(slug, asyncio.Lock())
    session_last_active[slug] = time.time()
    async with lock:
        try:
            logger.info("Query sent for slug=%s", slug)
            await client.query(text)

            current_block_type = None
            current_tool_id = None
            current_tool_name = None

            async for event in client.receive_response():
                if isinstance(event, StreamEvent):
                    raw = event.event
                    evt_type = raw.get("type")
                    parent_id = getattr(event, "parent_tool_use_id", None)

                    if evt_type == "content_block_start":
                        block = raw.get("content_block", {})
                        current_block_type = block.get("type")

                        if current_block_type == "tool_use":
                            current_tool_id = block.get("id", "")
                            current_tool_name = block.get("name", "")
                            logger.info(
                                "Tool start: %s (parent=%s)",
                                current_tool_name,
                                parent_id,
                            )
                            msg: dict[str, Any] = {
                                "type": "tool_start",
                                "slug": slug,
                                "toolId": current_tool_id,
                                "name": current_tool_name,
                            }
                            if parent_id:
                                msg["parentToolId"] = parent_id
                            await ws_holder.safe_send(msg)

                    elif evt_type == "content_block_delta":
                        delta = raw.get("delta", {})
                        delta_type = delta.get("type")

                        if delta_type == "text_delta":
                            if current_block_type != "tool_use":
                                msg = {
                                    "type": "text",
                                    "slug": slug,
                                    "chunk": delta.get("text", ""),
                                }
                                if parent_id:
                                    msg["parentToolId"] = parent_id
                                await ws_holder.safe_send(msg)
                        elif delta_type == "thinking_delta":
                            msg = {
                                "type": "thinking",
                                "slug": slug,
                                "chunk": delta.get("thinking", ""),
                            }
                            if parent_id:
                                msg["parentToolId"] = parent_id
                            await ws_holder.safe_send(msg)
                        elif delta_type == "input_json_delta" and current_tool_id:
                            msg = {
                                "type": "tool_input",
                                "slug": slug,
                                "toolId": current_tool_id,
                                "json": delta.get("partial_json", ""),
                            }
                            if parent_id:
                                msg["parentToolId"] = parent_id
                            await ws_holder.safe_send(msg)

                    elif evt_type == "content_block_stop":
                        if current_block_type == "tool_use" and current_tool_id:
                            logger.info(
                                "Tool end: %s (parent=%s)",
                                current_tool_name,
                                parent_id,
                            )
                            msg = {
                                "type": "tool_end",
                                "slug": slug,
                                "toolId": current_tool_id,
                            }
                            if parent_id:
                                msg["parentToolId"] = parent_id
                            await ws_holder.safe_send(msg)
                        current_block_type = None
                        current_tool_id = None
                        current_tool_name = None

                elif isinstance(event, ResultMessage):
                    logger.info(
                        "Result for slug=%s cost=%s", slug, event.total_cost_usd
                    )
                    # Always capture session_id — even without WS
                    if slug in session_meta:
                        session_meta[slug]["session_id"] = event.session_id
                        session_meta[slug]["cost"] = event.total_cost_usd

                    # Extract token usage from ResultMessage if available
                    usage = getattr(event, "usage", None)
                    input_tokens = None
                    output_tokens = None
                    if isinstance(usage, dict):
                        input_tokens = usage.get("input_tokens")
                        output_tokens = usage.get("output_tokens")
                    elif usage is not None:
                        input_tokens = getattr(usage, "input_tokens", None)
                        output_tokens = getattr(usage, "output_tokens", None)

                    await ws_holder.safe_send(
                        {
                            "type": "done",
                            "slug": slug,
                            "cost": event.total_cost_usd,
                            "session_id": event.session_id,
                            "duration_ms": getattr(event, "duration_ms", None),
                            "input_tokens": input_tokens,
                            "output_tokens": output_tokens,
                        }
                    )
            logger.info("Stream complete for slug=%s", slug)
        except Exception:
            logger.exception("Stream error for slug=%s", slug)
            await ws_holder.safe_send(
                {"type": "error", "slug": slug, "error": "Stream processing failed"}
            )
        finally:
            session_last_active[slug] = time.time()


# ---------------------------------------------------------------------------
# Sync message on reconnect
# ---------------------------------------------------------------------------
async def _send_sync(user_id: str, ws: WebSocket) -> None:
    """Send sync message to reconnected client with current session states."""
    user_sessions = sessions.get(user_id, {})
    sync_data: dict[str, Any] = {}

    for slug in user_sessions:
        meta = session_meta.get(slug, {})
        task = active_tasks.get(slug)
        is_streaming = task is not None and not task.done()

        entry: dict[str, Any] = {
            "status": "streaming" if is_streaming else "complete",
            "sessionId": meta.get("session_id"),
            "query": meta.get("query"),
        }

        # Re-send pending interactive prompts
        prompt_info = pending_prompts.get(slug)
        if prompt_info and not prompt_info["future"].done():
            entry["pendingPrompt"] = {
                "type": prompt_info["type"],
                **prompt_info["payload"],
            }

        sync_data[slug] = entry

    if sync_data:
        try:
            await ws.send_json({"type": "sync", "sessions": sync_data})
            logger.info(
                "Sent sync to user=%s: %d sessions (%s streaming)",
                user_id,
                len(sync_data),
                sum(1 for v in sync_data.values() if v["status"] == "streaming"),
            )
        except Exception:
            logger.warning("Failed to send sync to user=%s", user_id)


# ---------------------------------------------------------------------------
# Periodic cleanup for abandoned sessions
# ---------------------------------------------------------------------------
async def _periodic_cleanup() -> None:
    """Clean up completed sessions where the user has been disconnected > 30 min."""
    while True:
        await asyncio.sleep(300)  # Check every 5 minutes
        now = time.time()
        for user_id in list(sessions.keys()):
            user_sessions = sessions.get(user_id, {})
            ws_holder = ws_holders.get(user_id)
            is_disconnected = ws_holder is None or ws_holder.ws is None

            if not is_disconnected:
                continue  # User is connected, skip

            for slug in list(user_sessions.keys()):
                last_active = session_last_active.get(slug, 0)
                task = active_tasks.get(slug)
                is_done = task is None or task.done()

                if is_done and (now - last_active) > ABANDON_TIMEOUT_SEC:
                    client = user_sessions.pop(slug, None)
                    if client:
                        try:
                            await asyncio.shield(client.disconnect())
                        except Exception:
                            pass
                    slug_locks.pop(slug, None)
                    session_meta.pop(slug, None)
                    session_last_active.pop(slug, None)
                    pending_prompts.pop(slug, None)
                    active_tasks.pop(slug, None)
                    logger.info("Cleaned up abandoned session slug=%s", slug)

            # If user has no sessions left, clean up user entry
            if not sessions.get(user_id):
                sessions.pop(user_id, None)
                ws_holders.pop(user_id, None)


@app.on_event("startup")
async def start_cleanup_task():
    asyncio.create_task(_periodic_cleanup())


# ---------------------------------------------------------------------------
# REST endpoints
# ---------------------------------------------------------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/sessions/{user_id}")
async def list_sessions(user_id: str):
    """Return list of active server-side sessions for a user."""
    user_sessions = sessions.get(user_id, {})
    active_slugs = list(user_sessions.keys())
    return {
        "active": active_slugs,
        "meta": {slug: session_meta.get(slug, {}) for slug in active_slugs},
    }


# ---------------------------------------------------------------------------
# WebSocket handler
# ---------------------------------------------------------------------------
@app.websocket("/ws/{user_id}")
async def chat(websocket: WebSocket, user_id: str):
    await websocket.accept()
    logger.info("WebSocket connected: user=%s", user_id)

    # Re-attach or create WsHolder
    if user_id in ws_holders:
        ws_holder = ws_holders[user_id]
        ws_holder.set_ws(websocket)
        logger.info("Re-attached WsHolder for user=%s", user_id)
        await _send_sync(user_id, websocket)
    else:
        ws_holder = WsHolder(websocket)
        ws_holders[user_id] = ws_holder

    try:
        while True:
            msg = await websocket.receive_json()
            logger.info("Received message: %s", msg)

            # Handle answers for pending interactive prompts
            if msg.get("type") == "answer":
                slug = msg.get("slug", "")
                answers = msg.get("answers", {})
                prompt_info = pending_prompts.get(slug)
                if prompt_info and not prompt_info["future"].done():
                    prompt_info["future"].set_result(answers)
                    logger.info("Answer received for slug=%s", slug)
                continue

            if msg.get("type") == "set_thinking":
                mode = msg.get("mode", "off")
                logger.info(
                    "Thinking mode set to %s for user=%s", mode, user_id
                )
                continue

            if msg.get("type") == "set_permission_mode":
                mode = msg.get("mode", "bypassPermissions")
                logger.info(
                    "Permission mode set to %s for user=%s", mode, user_id
                )
                continue

            query = msg.get("query")
            slug = msg.get("slug")
            session_id = msg.get("sessionId")
            text = msg.get("text") or msg.get("query") or msg.get("answer", "")

            if query and not slug:
                slug = generate_slug(query)
                session_meta[slug] = {
                    "query": query,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                }
                await websocket.send_json(
                    {"type": "ack", "slug": slug, "query": query}
                )

            if slug and text:
                client = await get_or_create_session(
                    user_id,
                    slug,
                    ws_holder,
                    session_id=session_id,
                )
                task = asyncio.create_task(
                    stream_to_ws(client, text, slug, ws_holder)
                )
                active_tasks[slug] = task
                task.add_done_callback(lambda t, s=slug: active_tasks.pop(s, None))

    except WebSocketDisconnect:
        # Only null out the WS — do NOT cleanup sessions
        if ws_holder.ws is websocket:
            ws_holder.set_ws(None)
        logger.info(
            "WebSocket disconnected: user=%s (sessions preserved)", user_id
        )
