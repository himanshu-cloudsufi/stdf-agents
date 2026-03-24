from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

CORS_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://del-c4x772g7hx.tail99fe31.ts.net",
]

REPO_ROOT = os.environ.get(
    "STDF_ROOT",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

ABANDON_TIMEOUT_SEC = 3600
TOOL_RESULT_PREVIEW_CHARS = 500
