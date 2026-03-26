#!/usr/bin/env python3
"""STDF PreToolUse hook validator.

Reads Claude Code hook stdin JSON, extracts file_path and content from
Write or Edit tool inputs, and validates STDF compliance on output files.

Only enforces on files matching:
  - output/*/agents/*.md
  - output/*/00-final-synthesis.md

Exit codes:
  0 — pass (no violations or file not in scope)
  2 — block (violations found, write should be prevented)
"""

import json
import re
import sys
from pathlib import Path

# Add project root to path so we can import lib modules
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from lib.vocabulary import scan_banned, scan_banned_sources


# Patterns for STDF output files that should be validated
SCOPE_PATTERNS = [
    re.compile(r"output/[^/]+/agents/.*\.md$"),
    re.compile(r"output/[^/]+/00-final-synthesis\.md$"),
]

# Forecast language near future years
FORECAST_KEYWORDS = re.compile(
    r"\b(forecast|projected|outlook|expected\s+to\s+reach|will\s+reach|estimated\s+to\s+reach)\b",
    re.IGNORECASE,
)

# Anti-pattern phrases
ANTI_PATTERNS = re.compile(
    r"\b(linear\s+extrapolation|linear\s+growth|green\s+hydrogen|net\s+zero\s+target)\b",
    re.IGNORECASE,
)


def is_in_scope(file_path: str) -> bool:
    """Check if the file path matches STDF output patterns."""
    for pattern in SCOPE_PATTERNS:
        if pattern.search(file_path):
            return True
    return False


def validate(content: str, filename: str) -> list[str]:
    """Run all validation checks. Returns list of violation messages."""
    violations = []

    # 1. Banned vocabulary
    banned_hits = scan_banned(content)
    for hit in banned_hits:
        count = len(hit["positions"])
        violations.append(
            f"Banned term '{hit['term']}' ({count} occurrences) → {hit['replacement']}"
        )

    # 2. Banned source URLs
    source_hits = scan_banned_sources(content)
    for hit in source_hits:
        violations.append(f"Banned URL pattern '{hit['pattern']}' → {hit['reason']}")

    # 3. Forecast language
    for m in FORECAST_KEYWORDS.finditer(content):
        keyword = m.group(0)
        violations.append(f"Forecast language '{keyword}' detected")

    # 4. Anti-pattern phrases
    for m in ANTI_PATTERNS.finditer(content):
        phrase = m.group(0)
        violations.append(f"Anti-pattern phrase '{phrase}' detected")

    return violations


def main():
    """Read hook input from stdin, validate, and exit with appropriate code."""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            sys.exit(0)
        hook_input = json.loads(raw)
    except (json.JSONDecodeError, Exception):
        # If we can't parse input, let the write through
        sys.exit(0)

    tool_input = hook_input.get("tool_input", {})
    tool_name = hook_input.get("tool_name", "")

    # Extract file path and content based on tool type
    file_path = tool_input.get("file_path", "")
    if not file_path:
        sys.exit(0)

    # Check scope — only validate STDF output files
    if not is_in_scope(file_path):
        sys.exit(0)

    # Get content to validate
    if tool_name == "Write":
        content = tool_input.get("content", "")
    elif tool_name == "Edit":
        content = tool_input.get("new_string", "")
    else:
        sys.exit(0)

    if not content:
        sys.exit(0)

    filename = Path(file_path).name
    violations = validate(content, filename)

    if violations:
        msg = f"STDF COMPLIANCE BLOCK — {len(violations)} violations in {filename}:\n"
        for v in violations:
            msg += f"  - {v}\n"
        msg += "Fix all violations before writing."
        print(msg, file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
