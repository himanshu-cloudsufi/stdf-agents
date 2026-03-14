#!/usr/bin/env python3
"""STDF v2 — Claude Code headless pipeline.

Runs the 5-agent STDF pipeline using `claude -p` subprocess calls.
Each agent gets its full system prompt loaded from the prompts directory.

Usage:
    # Run single agent
    python3 scripts/stdf_v2_cc.py agent domain_disruption -Q "Analyze the energy sector disruption"
    python3 scripts/stdf_v2_cc.py agent cost_curve -Q "Li-ion battery cost dynamics vs gas peakers"

    # Run full pipeline (3-phase DAG)
    python3 scripts/stdf_v2_cc.py pipeline -Q "Transportation sector disruption analysis"

    # List agents
    python3 scripts/stdf_v2_cc.py list

Prerequisites:
    npm install -g @anthropic-ai/claude-code
    export ANTHROPIC_API_KEY=...
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "prompts" / "multiagent" / "stdf"

SEPARATOR = "-" * 80

# ── Agent definitions ────────────────────────────────────────────────────────

AGENTS = {
    "domain_disruption": {
        "prompt_file": "domain_disruption_system.txt",
        "description": "Category 1 — Sector, sub-domains, disruption map, convergence",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
    "cost_curve": {
        "prompt_file": "cost_curve_system.txt",
        "description": "Category 2 — Cost trajectories, learning rates, thresholds",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
    "capability": {
        "prompt_file": "capability_system.txt",
        "description": "Category 3 — Multi-dimensional capability comparison",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
    "tipping_point": {
        "prompt_file": "tipping_point_system.txt",
        "description": "Category 5 — Tipping conditions, post-tipping dynamics",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
    "adoption_scurve": {
        "prompt_file": "adoption_scurve_system.txt",
        "description": "Category 4 — S-curve adoption, regional breakdown, X-curve",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
    "synthesizer": {
        "prompt_file": "synthesizer_system.txt",
        "description": "Synthesizer — Merges 5 outputs into unified 7-phase analysis",
        "tools": "Read,Grep,Glob,Bash",
        "model": "sonnet",
    },
}


# ── Claude Code subprocess ───────────────────────────────────────────────────

def run_claude(
    prompt: str,
    system_prompt_file: Optional[Path] = None,
    system_prompt: Optional[str] = None,
    tools: str = "Read,Grep,Glob,Bash",
    model: str = "sonnet",
    cwd: Optional[Path] = None,
    verbose: bool = False,
) -> str:
    """Run claude -p and return text output."""
    cmd = ["claude", "-p", prompt, "--output-format", "text"]

    if system_prompt_file and system_prompt_file.exists():
        cmd += ["--system-prompt-file", str(system_prompt_file)]
    elif system_prompt:
        cmd += ["--system-prompt", system_prompt]

    cmd += ["--allowedTools", tools]
    cmd += ["--model", model]

    if verbose:
        print(f"  CMD: {' '.join(cmd[:6])}...")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(cwd or ROOT),
        timeout=600,  # 10 min timeout per agent
    )

    if result.returncode != 0:
        raise RuntimeError(f"claude exited with code {result.returncode}: {result.stderr[:500]}")

    return result.stdout.strip()


# ── Single agent runner ──────────────────────────────────────────────────────

def run_agent(
    name: str,
    query: str,
    context: Optional[str] = None,
    upstream_context: Optional[str] = None,
    verbose: bool = False,
) -> str:
    """Run a single STDF agent via claude -p. Returns the agent's text output."""
    agent_cfg = AGENTS[name]
    prompt_file = PROMPTS_DIR / agent_cfg["prompt_file"]

    parts = [query]
    if context:
        parts.append(f"\nAdditional context: {context}")
    if upstream_context:
        parts.append(f"\nUpstream agent outputs:\n{upstream_context}")

    full_prompt = "\n".join(parts)

    print(f"\n  Running {name}...")
    start = time.monotonic()

    output = run_claude(
        prompt=full_prompt,
        system_prompt_file=prompt_file,
        tools=agent_cfg["tools"],
        model=agent_cfg["model"],
        verbose=verbose,
    )

    elapsed = time.monotonic() - start
    print(f"  {name} completed in {elapsed:.1f}s")

    return output


# ── Pipeline ─────────────────────────────────────────────────────────────────

def run_pipeline(
    query: str,
    context: Optional[str] = None,
    verbose: bool = False,
) -> dict[str, Optional[str]]:
    """Run the full 3-phase STDF pipeline via sequential claude -p calls."""
    results: dict[str, Optional[str]] = {}
    total_start = time.monotonic()

    print(f"\n{SEPARATOR}")
    print(f"  STDF v2 Pipeline — {query}")
    print(SEPARATOR)

    # Phase 1: Domain + CostCurve + Capability
    print("\n>>> Phase 1: Independent analyses")
    for name in ["domain_disruption", "cost_curve", "capability"]:
        try:
            results[name] = run_agent(name, query, context=context, verbose=verbose)
        except Exception as e:
            print(f"  ERROR: {name} failed: {e}")
            if name == "cost_curve":
                print("  HARD FAIL — cost_curve is CRITICAL. Aborting pipeline.")
                return results
            results[name] = None

    # Build upstream context for Phase 2
    upstream_phase1 = "\n\n".join(
        f"=== {name} ===\n{results[name]}"
        for name in ["domain_disruption", "cost_curve", "capability"]
        if results.get(name)
    )

    # Phase 2: Tipping Point
    print("\n>>> Phase 2: Tipping Point (with Phase 1 context)")
    try:
        results["tipping_point"] = run_agent(
            "tipping_point", query, context=context,
            upstream_context=upstream_phase1, verbose=verbose,
        )
    except Exception as e:
        print(f"  HARD FAIL — tipping_point is CRITICAL: {e}")
        return results

    # Build upstream context for Phase 3
    upstream_all = "\n\n".join(
        f"=== {name} ===\n{results[name]}"
        for name in ["domain_disruption", "cost_curve", "capability", "tipping_point"]
        if results.get(name)
    )

    # Phase 3: Adoption S-Curve
    print("\n>>> Phase 3: Adoption S-Curve (with Phase 1+2 context)")
    try:
        results["adoption_scurve"] = run_agent(
            "adoption_scurve", query, context=context,
            upstream_context=upstream_all, verbose=verbose,
        )
    except Exception as e:
        print(f"  WARNING: adoption_scurve failed (degraded): {e}")
        results["adoption_scurve"] = None

    # Synthesize
    print("\n>>> Synthesize: Merging all 5 outputs")
    all_outputs = "\n\n".join(
        f"=== {name} ===\n{results[name] or 'DEGRADED — output unavailable'}"
        for name in ["domain_disruption", "cost_curve", "capability", "tipping_point", "adoption_scurve"]
    )

    try:
        results["synthesis"] = run_agent(
            "synthesizer", query, context=context,
            upstream_context=all_outputs, verbose=verbose,
        )
    except Exception as e:
        print(f"  ERROR: Synthesis failed: {e}")
        results["synthesis"] = None

    total_elapsed = time.monotonic() - total_start

    # Summary
    print(f"\n{SEPARATOR}")
    print(f"  Pipeline complete — {total_elapsed:.1f}s total")
    print(SEPARATOR)
    for name in ["domain_disruption", "cost_curve", "capability", "tipping_point", "adoption_scurve", "synthesis"]:
        status = "OK" if results.get(name) else "FAILED/DEGRADED"
        print(f"  {name:25s} {status}")

    return results


# ── CLI ──────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stdf_v2_cc",
        description="STDF v2 analysis pipeline using Claude Code.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single agent
  %(prog)s agent domain_disruption -Q "Analyze solar energy disruption"

  # Full pipeline (sequential subprocess calls)
  %(prog)s pipeline -Q "Transportation sector disruption"

  # List agents
  %(prog)s list
""",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-o", "--output", type=str, help="Save output to file")

    sub = parser.add_subparsers(dest="command")

    # agent
    p = sub.add_parser("agent", help="Run a single STDF agent")
    p.add_argument("name", choices=list(AGENTS.keys()))
    p.add_argument("--query", "-Q", required=True)
    p.add_argument("--context", "-c", type=str)
    p.add_argument("--upstream-file", type=str, help="File with upstream context")

    # pipeline
    p = sub.add_parser("pipeline", help="Run full 3-phase pipeline")
    p.add_argument("--query", "-Q", required=True)
    p.add_argument("--context", "-c", type=str)

    # list
    sub.add_parser("list", help="List available agents")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "list":
        print(f"\n{SEPARATOR}")
        print("  STDF v2 Agents (Claude Code)")
        print(SEPARATOR)
        for name, cfg in AGENTS.items():
            print(f"  {name:25s} {cfg['description']}")
        print(f"\n  Agent definitions:       .claude/agents/stdf-*.md")
        print(f"  System prompts:          prompts/multiagent/stdf/*.txt")
        return 0

    if args.command == "agent":
        upstream = None
        if args.upstream_file:
            upstream = Path(args.upstream_file).read_text()
        output = run_agent(args.name, args.query, context=args.context,
                           upstream_context=upstream, verbose=args.verbose)
        print(f"\n{SEPARATOR}")
        print(output)

        if args.output:
            Path(args.output).write_text(output)
            print(f"\n  Output saved to {args.output}")

    elif args.command == "pipeline":
        results = run_pipeline(args.query, context=args.context, verbose=args.verbose)

        # Print final synthesis
        if results.get("synthesis"):
            print(f"\n{SEPARATOR}")
            print("  Final Synthesis:")
            print(SEPARATOR)
            print(results["synthesis"])

        if args.output:
            Path(args.output).write_text(
                "\n\n".join(
                    f"=== {name} ===\n{text}"
                    for name, text in results.items()
                    if text
                )
            )
            print(f"\n  Output saved to {args.output}")

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
