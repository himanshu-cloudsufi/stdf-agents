from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

from server.config import TOOL_RESULT_PREVIEW_CHARS


def obj_get(obj: Any, key: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def content_to_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, (int, float, bool)):
        return str(content)
    if isinstance(content, list):
        return "".join(content_to_text(item) for item in content)
    if isinstance(content, dict):
        block_type = content.get("type")
        if block_type == "text":
            text = content.get("text")
            return text if isinstance(text, str) else ""
        if "content" in content:
            return content_to_text(content.get("content"))
        text = content.get("text")
        return text if isinstance(text, str) else str(content)

    block_type = getattr(content, "type", None)
    if block_type == "text":
        text = getattr(content, "text", None)
        return text if isinstance(text, str) else ""

    nested = getattr(content, "content", None)
    if nested is not None:
        return content_to_text(nested)

    text = getattr(content, "text", None)
    if isinstance(text, str):
        return text
    return str(content)


def extract_tool_result_previews(message: Any) -> list[dict[str, Any]]:
    content = obj_get(message, "content")
    if content is None:
        return []

    blocks = content if isinstance(content, list) else [content]
    previews: list[dict[str, Any]] = []

    for block in blocks:
        if obj_get(block, "type") != "tool_result":
            continue

        tool_id = (
            obj_get(block, "tool_use_id")
            or obj_get(block, "toolUseId")
            or obj_get(block, "tool_useId")
        )
        if not isinstance(tool_id, str) or not tool_id:
            continue

        result_text = content_to_text(obj_get(block, "content")).strip()
        if not result_text:
            result_text = "[no textual output]"

        is_error = bool(obj_get(block, "is_error", obj_get(block, "isError", False)))
        if is_error and not result_text.startswith("[tool error]"):
            result_text = f"[tool error]\n{result_text}"

        previews.append(
            {
                "toolId": tool_id,
                "result": result_text[:TOOL_RESULT_PREVIEW_CHARS],
                "truncated": len(result_text) > TOOL_RESULT_PREVIEW_CHARS,
                "isError": is_error,
            }
        )

    return previews


def generate_slug(query: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", query.lower())[:50].strip("-")
    return f"{slug}-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}"
