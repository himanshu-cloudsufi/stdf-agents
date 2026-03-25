"""Integration tests for the STDF PreToolUse hook validator script."""

import json
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HOOK_SCRIPT = PROJECT_ROOT / ".claude" / "hooks" / "stdf_validate.py"


def run_hook(tool_name: str, tool_input: dict) -> subprocess.CompletedProcess:
    """Simulate a PreToolUse hook invocation."""
    hook_input = {
        "tool_name": tool_name,
        "tool_input": tool_input,
    }
    return subprocess.run(
        [sys.executable, str(HOOK_SCRIPT)],
        input=json.dumps(hook_input),
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )


def test_hook_blocks_banned_vocabulary():
    """Write with banned vocab to an STDF output file should be blocked (exit 2)."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/agents/01-domain-disruption.md",
        "content": "The transition to clean energy is driven by IEA forecasts.",
    })
    assert result.returncode == 2
    assert "STDF COMPLIANCE BLOCK" in result.stderr
    assert "transition" in result.stderr.lower()


def test_hook_blocks_banned_source_urls():
    """Write with banned source URLs should be blocked."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/agents/02-cost-curve.md",
        "content": "Data from https://www.iea.org/data shows cost trends.",
    })
    assert result.returncode == 2
    assert "iea" in result.stderr.lower()


def test_hook_blocks_forecast_language():
    """Write with forecast language should be blocked."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/agents/03-capability.md",
        "content": "Battery costs are projected to decline. The outlook is positive.",
    })
    assert result.returncode == 2
    assert "projected" in result.stderr.lower() or "outlook" in result.stderr.lower()


def test_hook_blocks_anti_patterns():
    """Write with anti-pattern phrases should be blocked."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/agents/05-adoption-scurve.md",
        "content": "Using linear extrapolation we see linear growth.",
    })
    assert result.returncode == 2
    assert "linear" in result.stderr.lower()


def test_hook_passes_clean_content():
    """Clean content in an STDF output file should pass (exit 0)."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/agents/01-domain-disruption.md",
        "content": "disruption of incumbent technologies driven by cost-curve dynamics and S-curve adoption.",
    })
    assert result.returncode == 0


def test_hook_passes_non_output_files():
    """Files outside output/ should always pass regardless of content."""
    result = run_hook("Write", {
        "file_path": "lib/vocabulary.py",
        "content": "The transition to clean energy is driven by IEA forecasts.",
    })
    assert result.returncode == 0


def test_hook_passes_non_agent_output_files():
    """Non-agent files in output/ (like README.md) should pass."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/README.md",
        "content": "The transition to clean energy is driven by IEA forecasts.",
    })
    assert result.returncode == 0


def test_hook_validates_edit_tool():
    """Edit tool with banned vocab in new_string should be blocked."""
    result = run_hook("Edit", {
        "file_path": "output/test-analysis/agents/02-cost-curve.md",
        "old_string": "placeholder",
        "new_string": "The transition to renewable energy.",
    })
    assert result.returncode == 2
    assert "transition" in result.stderr.lower()


def test_hook_edit_clean_passes():
    """Edit tool with clean new_string should pass."""
    result = run_hook("Edit", {
        "file_path": "output/test-analysis/agents/02-cost-curve.md",
        "old_string": "placeholder",
        "new_string": "disruption of incumbent technologies.",
    })
    assert result.returncode == 0


def test_hook_handles_empty_stdin():
    """Empty stdin should pass gracefully."""
    result = subprocess.run(
        [sys.executable, str(HOOK_SCRIPT)],
        input="",
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )
    assert result.returncode == 0


def test_hook_handles_invalid_json():
    """Invalid JSON should pass gracefully."""
    result = subprocess.run(
        [sys.executable, str(HOOK_SCRIPT)],
        input="not json",
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )
    assert result.returncode == 0


def test_hook_validates_final_synthesis():
    """00-final-synthesis.md should also be in scope."""
    result = run_hook("Write", {
        "file_path": "output/test-analysis/00-final-synthesis.md",
        "content": "The transition to clean energy is underway.",
    })
    assert result.returncode == 2
