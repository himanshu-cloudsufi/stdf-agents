from __future__ import annotations

import asyncio
import glob
import logging
import os
import time
from typing import Any

from claude_agent_sdk.types import (
    PermissionResultAllow,
    PermissionResultDeny,
    ToolPermissionContext,
)

from server.config import REPO_ROOT
from server.state import WsHolder, pending_prompts, plan_content_cache

logger = logging.getLogger("stdf-server")


def make_can_use_tool(slug: str, ws_holder: WsHolder):
    """Create a can_use_tool callback that intercepts interactive tools."""

    async def can_use_tool(
        tool_name: str,
        tool_input: dict[str, Any],
        context: ToolPermissionContext,
    ):
        del context
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

        if tool_name == "TodoWrite":
            todos = tool_input.get("todos", [])
            await ws_holder.safe_send(
                {"type": "todo_update", "slug": slug, "todos": todos}
            )
            logger.info("TodoWrite intercepted for slug=%s, %d todos", slug, len(todos))
            return PermissionResultAllow()

        if tool_name == "AskUserQuestion":
            logger.info("AskUserQuestion intercepted for slug=%s", slug)
            payload = {"questions": tool_input.get("questions", [])}
            await ws_holder.safe_send({"type": "ask_user", "slug": slug, **payload})
            future: asyncio.Future[Any] = asyncio.get_event_loop().create_future()
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
            plan_content = plan_content_cache.pop(slug, "")
            if plan_content:
                logger.info(
                    "Using cached plan content for slug=%s (%d chars)",
                    slug,
                    len(plan_content),
                )
            else:
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
                        for plan_file in plan_files:
                            if now - os.path.getmtime(plan_file) < 120:
                                with open(plan_file) as f:
                                    plan_content = f.read()
                                logger.info("Read plan from %s", plan_file)
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
            future: asyncio.Future[Any] = asyncio.get_event_loop().create_future()
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
            return PermissionResultDeny(
                message=result.get("feedback", "User rejected the plan"),
            )

        logger.info("Tool allowed: %s for slug=%s", tool_name, slug)
        return PermissionResultAllow()

    return can_use_tool

