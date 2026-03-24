from __future__ import annotations

import asyncio
import logging
import time

from server.config import ABANDON_TIMEOUT_SEC
from server.state import (
    active_tasks,
    pending_prompts,
    session_last_active,
    session_meta,
    sessions,
    slug_locks,
    ws_holders,
)

logger = logging.getLogger("stdf-server")


async def periodic_cleanup() -> None:
    """Clean completed sessions for disconnected users after timeout."""
    while True:
        await asyncio.sleep(300)
        now = time.time()
        for user_id in list(sessions.keys()):
            user_sessions = sessions.get(user_id, {})
            ws_holder = ws_holders.get(user_id)
            is_disconnected = ws_holder is None or ws_holder.ws is None

            if not is_disconnected:
                continue

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

            if not sessions.get(user_id):
                sessions.pop(user_id, None)
                ws_holders.pop(user_id, None)

