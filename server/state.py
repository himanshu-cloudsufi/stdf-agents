from __future__ import annotations

import asyncio
from typing import Any

from claude_agent_sdk import ClaudeSDKClient
from fastapi import WebSocket


class WsHolder:
    """Mutable WebSocket reference that survives reconnects."""

    def __init__(self, ws: WebSocket | None = None):
        self._ws: WebSocket | None = ws

    @property
    def ws(self) -> WebSocket | None:
        return self._ws

    def set_ws(self, ws: WebSocket | None) -> None:
        self._ws = ws

    async def safe_send(self, data: dict[str, Any]) -> bool:
        ws = self._ws
        if ws is None:
            return False
        try:
            await ws.send_json(data)
            return True
        except Exception:
            self._ws = None
            return False


sessions: dict[str, dict[str, ClaudeSDKClient]] = {}
ws_holders: dict[str, WsHolder] = {}
slug_locks: dict[str, asyncio.Lock] = {}
pending_prompts: dict[str, dict[str, Any]] = {}
plan_content_cache: dict[str, str] = {}
session_meta: dict[str, dict[str, Any]] = {}
active_tasks: dict[str, asyncio.Task[Any]] = {}
session_last_active: dict[str, float] = {}
