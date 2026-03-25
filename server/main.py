"""STDF Chat UI FastAPI entrypoint.

This module keeps routing/composition only. Stateful logic lives in dedicated
server modules for maintainability and testability.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timezone

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from server.cleanup import periodic_cleanup
from server.config import CORS_ORIGINS
from server.session_manager import get_or_create_session
from server.state import (
    WsHolder,
    active_tasks,
    pending_prompts,
    session_meta,
    sessions,
    ws_holders,
)
from server.streaming import stream_to_ws
from server.sync import send_sync
from server.utils import generate_slug

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("stdf-server")

app = FastAPI(title="STDF Chat UI", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_cleanup_task() -> None:
    asyncio.create_task(periodic_cleanup())


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/sessions/{user_id}")
async def list_sessions(user_id: str) -> dict[str, object]:
    """Return active server-side sessions for a user."""
    user_sessions = sessions.get(user_id, {})
    active_slugs = list(user_sessions.keys())
    return {
        "active": active_slugs,
        "meta": {slug: session_meta.get(slug, {}) for slug in active_slugs},
    }


@app.websocket("/ws/{user_id}")
async def chat(websocket: WebSocket, user_id: str) -> None:
    await websocket.accept()
    logger.info("WebSocket connected: user=%s", user_id)

    if user_id in ws_holders:
        ws_holder = ws_holders[user_id]
        ws_holder.set_ws(websocket)
        logger.info("Re-attached WsHolder for user=%s", user_id)
        await send_sync(user_id, websocket)
    else:
        ws_holder = WsHolder(websocket)
        ws_holders[user_id] = ws_holder

    try:
        while True:
            msg = await websocket.receive_json()
            logger.info("Received message: %s", msg)

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
                logger.info("Thinking mode set to %s for user=%s", mode, user_id)
                continue

            if msg.get("type") == "set_permission_mode":
                mode = msg.get("mode", "bypassPermissions")
                logger.info("Permission mode set to %s for user=%s", mode, user_id)
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
                await websocket.send_json({"type": "ack", "slug": slug, "query": query})

            if slug and text:
                client = await get_or_create_session(
                    user_id,
                    slug,
                    ws_holder,
                    session_id=session_id,
                )
                task = asyncio.create_task(stream_to_ws(client, text, slug, ws_holder))
                active_tasks[slug] = task
                task.add_done_callback(lambda _task, target_slug=slug: active_tasks.pop(target_slug, None))

    except WebSocketDisconnect:
        if ws_holder.ws is websocket:
            ws_holder.set_ws(None)
        logger.info("WebSocket disconnected: user=%s (sessions preserved)", user_id)
