from __future__ import annotations

import logging
from typing import Any

from fastapi import WebSocket

from server.state import active_tasks, pending_prompts, session_meta, sessions

logger = logging.getLogger("stdf-server")


async def send_sync(user_id: str, websocket: WebSocket) -> None:
    """Send rehydration state to reconnected clients."""
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

        prompt_info = pending_prompts.get(slug)
        if prompt_info and not prompt_info["future"].done():
            entry["pendingPrompt"] = {
                "type": prompt_info["type"],
                **prompt_info["payload"],
            }

        sync_data[slug] = entry

    if sync_data:
        try:
            await websocket.send_json({"type": "sync", "sessions": sync_data})
            logger.info(
                "Sent sync to user=%s: %d sessions (%s streaming)",
                user_id,
                len(sync_data),
                sum(1 for value in sync_data.values() if value["status"] == "streaming"),
            )
        except Exception:
            logger.warning("Failed to send sync to user=%s", user_id)

