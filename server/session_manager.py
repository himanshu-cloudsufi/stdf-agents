from __future__ import annotations

import logging
import os
from typing import Any

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

from server.agents import AGENT_DEFINITIONS, build_system_prompt_append
from server.config import DEV_MODEL, REPO_ROOT
from server.state import WsHolder, sessions
from server.tool_permissions import make_can_use_tool

# Model ID mapping: short names → full API model IDs
_MODEL_IDS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-6",
}
_DEFAULT_ORCHESTRATOR_MODEL = "claude-opus-4-6"

logger = logging.getLogger("stdf-server")


async def get_or_create_session(
    user_id: str,
    slug: str,
    ws_holder: WsHolder,
    session_id: str | None = None,
) -> ClaudeSDKClient:
    user_sessions = sessions.setdefault(user_id, {})
    if slug not in user_sessions:
        options: dict[str, Any] = {
            "model": _MODEL_IDS.get(DEV_MODEL, DEV_MODEL) if DEV_MODEL else _DEFAULT_ORCHESTRATOR_MODEL,
            "system_prompt": {
                "type": "preset",
                "preset": "claude_code",
                "append": build_system_prompt_append(slug, user_id),
            },
            "setting_sources": ["project"],
            "agents": AGENT_DEFINITIONS if AGENT_DEFINITIONS else None,
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

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key:
            options["env"] = {**os.environ, "ANTHROPIC_API_KEY": api_key}
        if session_id:
            options["resume"] = session_id
            logger.info("Resuming session slug=%s with session_id=%s", slug, session_id)

        client = ClaudeSDKClient(options=ClaudeAgentOptions(**options))
        await client.__aenter__()
        user_sessions[slug] = client

    return user_sessions[slug]

