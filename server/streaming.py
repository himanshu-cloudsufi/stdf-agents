from __future__ import annotations

import asyncio
import logging
import time
from typing import Any

from claude_agent_sdk import ClaudeSDKClient, ResultMessage, StreamEvent

from server.state import WsHolder, session_last_active, session_meta, slug_locks
from server.utils import extract_tool_result_previews

logger = logging.getLogger("stdf-server")


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

            current_block_type: str | None = None
            current_tool_id: str | None = None
            current_tool_name: str | None = None

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
                            payload: dict[str, Any] = {
                                "type": "tool_start",
                                "slug": slug,
                                "toolId": current_tool_id,
                                "name": current_tool_name,
                            }
                            if parent_id:
                                payload["parentToolId"] = parent_id
                            await ws_holder.safe_send(payload)

                    elif evt_type == "content_block_delta":
                        delta = raw.get("delta", {})
                        delta_type = delta.get("type")
                        if delta_type == "text_delta":
                            if current_block_type != "tool_use":
                                payload = {
                                    "type": "text",
                                    "slug": slug,
                                    "chunk": delta.get("text", ""),
                                }
                                if parent_id:
                                    payload["parentToolId"] = parent_id
                                await ws_holder.safe_send(payload)
                        elif delta_type == "thinking_delta":
                            payload = {
                                "type": "thinking",
                                "slug": slug,
                                "chunk": delta.get("thinking", ""),
                            }
                            if parent_id:
                                payload["parentToolId"] = parent_id
                            await ws_holder.safe_send(payload)
                        elif delta_type == "input_json_delta" and current_tool_id:
                            payload = {
                                "type": "tool_input",
                                "slug": slug,
                                "toolId": current_tool_id,
                                "json": delta.get("partial_json", ""),
                            }
                            if parent_id:
                                payload["parentToolId"] = parent_id
                            await ws_holder.safe_send(payload)

                    elif evt_type == "content_block_stop":
                        if current_block_type == "tool_use" and current_tool_id:
                            logger.info(
                                "Tool end: %s (parent=%s)",
                                current_tool_name,
                                parent_id,
                            )
                            payload = {
                                "type": "tool_end",
                                "slug": slug,
                                "toolId": current_tool_id,
                            }
                            if parent_id:
                                payload["parentToolId"] = parent_id
                            await ws_holder.safe_send(payload)
                        current_block_type = None
                        current_tool_id = None
                        current_tool_name = None

                else:
                    tool_results = extract_tool_result_previews(event)
                    if tool_results:
                        parent_id = getattr(event, "parent_tool_use_id", None)
                        for tool_result in tool_results:
                            logger.info(
                                "Tool result: %s (parent=%s, truncated=%s)",
                                tool_result["toolId"],
                                parent_id,
                                tool_result["truncated"],
                            )
                            payload: dict[str, Any] = {
                                "type": "tool_result",
                                "slug": slug,
                                "toolId": tool_result["toolId"],
                                "result": tool_result["result"],
                                "truncated": tool_result["truncated"],
                                "isError": tool_result["isError"],
                            }
                            if parent_id:
                                payload["parentToolId"] = parent_id
                            await ws_holder.safe_send(payload)

                if isinstance(event, ResultMessage):
                    logger.info("Result for slug=%s cost=%s", slug, event.total_cost_usd)
                    if slug in session_meta:
                        session_meta[slug]["session_id"] = event.session_id
                        session_meta[slug]["cost"] = event.total_cost_usd

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

