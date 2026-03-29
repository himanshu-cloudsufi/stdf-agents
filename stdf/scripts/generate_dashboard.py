#!/usr/bin/env python3
"""
STDF Pipeline Dashboard Generator
Creates a self-contained interactive HTML visualization of all STDF analysis runs.

Usage:  python3 scripts/generate_dashboard.py
Output: output/dashboard.html
"""

import json
import re
import sys
from pathlib import Path

# ── Pipeline DAG topology ───────────────────────────────────────────

PIPELINE = {
    "tiers": [
        {"id": "t1", "label": "Tier 1 — Foundation", "agents": [
            {"id": "domain-disruption", "name": "Domain Disruption"},
            {"id": "cost-researcher", "name": "Cost Researcher"},
            {"id": "capability", "name": "Capability"},
        ]},
        {"id": "t2", "label": "Tier 2 — Cost Fitting", "agents": [
            {"id": "cost-fitter", "name": "Cost Fitter"},
        ]},
        {"id": "t3", "label": "Tier 3 — Condition Check", "agents": [
            {"id": "cost-parity", "name": "Cost Parity"},
            {"id": "cap-parity", "name": "Capability Parity"},
            {"id": "adopt-readiness", "name": "Adoption Readiness"},
        ]},
        {"id": "t4", "label": "Tier 4 — Tipping", "agents": [
            {"id": "tipping-synthesizer", "name": "Tipping Synthesizer"},
        ]},
        {"id": "t5a", "label": "Tier 5a — S-Curve", "agents": [
            {"id": "scurve-fitter", "name": "S-Curve Fitter"},
        ]},
        {"id": "t5b", "label": "Tier 5b — Regional / X-Curve", "agents": [
            {"id": "regional-adopter", "name": "Regional Adopter"},
            {"id": "xcurve-analyst", "name": "X-Curve Analyst"},
        ]},
        {"id": "t6", "label": "Tier 6 — Commodity Chain", "agents": [
            {"id": "demand-decomposer", "name": "Demand Decomposer"},
            {"id": "stream-forecaster", "name": "Stream Forecaster"},
            {"id": "fleet-modeler", "name": "Fleet Modeler"},
            {"id": "regional-demand", "name": "Regional Demand"},
        ]},
        {"id": "t7", "label": "Tier 7 — Energy Chain", "agents": [
            {"id": "energy-dispatch", "name": "Energy Dispatch"},
            {"id": "gas-supply", "name": "Gas Supply"},
        ]},
        {"id": "final", "label": "Final — Synthesis", "agents": [
            {"id": "synthesizer", "name": "Synthesizer"},
        ]},
        {"id": "eval", "label": "Evaluation", "agents": [
            {"id": "evaluator", "name": "Evaluator"},
        ]},
    ],
    "edges": [
        ["domain-disruption", "cost-parity"],
        ["domain-disruption", "cap-parity"],
        ["domain-disruption", "adopt-readiness"],
        ["domain-disruption", "demand-decomposer"],
        ["domain-disruption", "energy-dispatch"],
        ["cost-researcher", "cost-fitter"],
        ["cost-fitter", "cost-parity"],
        ["cost-fitter", "xcurve-analyst"],
        ["cost-fitter", "demand-decomposer"],
        ["cost-fitter", "energy-dispatch"],
        ["capability", "cap-parity"],
        ["cost-parity", "tipping-synthesizer"],
        ["cap-parity", "tipping-synthesizer"],
        ["adopt-readiness", "tipping-synthesizer"],
        ["tipping-synthesizer", "scurve-fitter"],
        ["scurve-fitter", "regional-adopter"],
        ["scurve-fitter", "xcurve-analyst"],
        ["demand-decomposer", "stream-forecaster"],
        ["stream-forecaster", "fleet-modeler"],
        ["stream-forecaster", "regional-demand"],
        ["energy-dispatch", "gas-supply"],
    ],
}

AGENT_NAME_MAP = {
    "domain-disruption": "domain-disruption",
    "cost-researcher": "cost-researcher",
    "cost-fitter": "cost-fitter",
    "capability": "capability",
    "cost-parity": "cost-parity",
    "cap-parity": "cap-parity",
    "adopt-readiness": "adopt-readiness",
    "tipping-synthesizer": "tipping-synthesizer",
    "scurve-fitter": "scurve-fitter",
    "regional-adopter": "regional-adopter",
    "xcurve-analyst": "xcurve-analyst",
    "synthesizer": "synthesizer",
    "evaluation": "evaluator",
    "evaluator": "evaluator",
    "demand-decomposer": "demand-decomposer",
    "stream-forecaster": "stream-forecaster",
    "fleet-modeler": "fleet-modeler",
    "regional-demand": "regional-demand",
    "regional-demand-analyst": "regional-demand",
    "energy-dispatch": "energy-dispatch",
    "gas-supply": "gas-supply",
    "gas-supply-decomposer": "gas-supply",
    # Legacy v1 agent names
    "cost-curve": "cost-fitter",
    "tipping-point": "tipping-synthesizer",
    "adoption-scurve": "scurve-fitter",
}


# ── Parsing helpers ─────────────────────────────────────────────────

def extract_confidence(text):
    for pat in [
        r"\*\*Confidence(?:\s+Score)?:\*\*\s*([\d.]+)",
        r"Confidence(?:\s+Score)?:\s*([\d.]+)",
        r"confidence[:\s]+([\d.]+)",
    ]:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                pass
    return None


def extract_section(text, headers):
    for header in headers:
        pat = rf"^##\s+{re.escape(header)}\s*\n(.*?)(?=\n## |\Z)"
        m = re.search(pat, text, re.DOTALL | re.MULTILINE)
        if m:
            return m.group(1).strip()
    return ""


def extract_tables(text, max_tables=3):
    tables = []
    table_pat = r"(?:^\|.+\|$\n?)+"
    for m in re.finditer(table_pat, text, re.MULTILINE):
        lines = [l.strip() for l in m.group().strip().split("\n") if l.strip()]
        if len(lines) < 2:
            continue
        rows = []
        is_header = True
        for line in lines:
            if re.match(r"^\|[\s\-:|]+\|$", line):
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            rows.append({"cells": cells, "header": is_header})
            is_header = False
        if rows:
            tables.append(rows)
        if len(tables) >= max_tables:
            break
    return tables


# ── File parsers ────────────────────────────────────────────────────

def parse_agent_file(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    stem = path.stem
    name = re.sub(r"^\d+[a-z]?-", "", stem)
    agent_id = AGENT_NAME_MAP.get(name, name)
    confidence = extract_confidence(text)
    findings = extract_section(text, [
        "Key Findings", "Executive Summary", "Agent Output",
        "Summary", "Findings", "Output",
    ])
    if not findings:
        # Fallback: take first substantial paragraph after frontmatter
        chunks = text.split("\n\n")
        for chunk in chunks[1:]:
            cleaned = chunk.strip()
            if len(cleaned) > 80 and not cleaned.startswith("#") and not cleaned.startswith("|") and not cleaned.startswith("**Agent"):
                findings = cleaned
                break
    if len(findings) > 1500:
        findings = findings[:1500] + "..."
    tables = extract_tables(text)
    return {
        "id": agent_id,
        "file": path.name,
        "confidence": confidence,
        "key_findings": findings,
        "tables": tables,
    }


def parse_readme(readme_path):
    text = readme_path.read_text(encoding="utf-8", errors="replace")
    r = {}
    # Title
    m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    r["title"] = m.group(1).strip() if m else readme_path.parent.name
    # Config
    m = re.search(r"\*\*(?:Pipeline|Configuration|Preset):\*\*\s*(\S+)", text)
    r["config"] = m.group(1).strip(" |()") if m else "UNKNOWN"
    # Date
    m = re.search(r"\*\*(?:Date|Analysis Date):\*\*\s*([\d-]+)", text)
    r["date"] = m.group(1) if m else ""
    # Confidence — handle all observed formats
    conf_val = 0
    for pat in [
        r"\*\*(?:Pipeline [Cc]onfidence|Confidence|Aggregate confidence|Overall Synthesis Confidence|Mean confidence):\*\*\s*([\d.]+)",
        r"\*\*(?:Pipeline [Cc]onfidence|Confidence|Aggregate confidence|Overall Synthesis Confidence|Mean confidence)[:\s]+([\d.]+)\*\*",
        r"(?:Pipeline [Cc]onfidence|Aggregate confidence|Mean confidence)[:\s]+([\d.]+)",
    ]:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                conf_val = float(m.group(1))
            except ValueError:
                pass
            break
    r["confidence"] = conf_val
    # Rupture Window
    m = re.search(r"\*\*Rupture Window:\*\*\s*(.+?)(?:\n|\||\*)", text)
    r["rupture_window"] = m.group(1).strip() if m else ""
    # Tipping Point
    m = re.search(r"\*\*Tipping Point:\*\*\s*(.+?)(?:\n|\*)", text)
    r["tipping_point"] = m.group(1).strip() if m else ""
    # Agent count
    m = re.search(r"\*\*(?:Agents|Total Agents|Agents completed):\*\*\s*(\d+)", text)
    r["agent_count"] = int(m.group(1)) if m else 0
    # Query
    m = re.search(r'\*\*(?:Query|Analysis):\*\*\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    r["query"] = m.group(1).strip() if m else ""
    # Key conclusion
    conclusion = extract_section(text, ["Key Conclusion", "Key Findings"])
    r["key_conclusion"] = conclusion[:800] if conclusion else ""
    # Execution table
    exec_text = extract_section(text, ["Execution Summary", "Pipeline Status"])
    r["execution_table"] = extract_tables(exec_text, max_tables=1)
    # Data gaps
    gaps = extract_section(text, ["Data Gaps"])
    r["data_gaps"] = gaps[:500] if gaps else ""
    # Evaluation
    ev = extract_section(text, ["Evaluation Result", "Guardrail Validation"])
    r["evaluation"] = ev[:400] if ev else ""
    # Skipped
    sk = extract_section(text, ["Agents Skipped", "Skipped"])
    r["skipped"] = sk[:300] if sk else ""
    return r


def parse_synthesis_phases(path):
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    phases = []

    # Executive summary
    m = re.search(r"^## Executive Summary\s*\n(.*?)(?=\n##\s)", text, re.DOTALL | re.MULTILINE)
    if m:
        phases.append({"title": "Executive Summary", "content": m.group(1).strip()[:2000]})

    # Strategy 1: ## Phase N: Title (energy-storage style)
    parts = re.split(r"^(## Phase \d+[:\s].+?)$", text, flags=re.MULTILINE)
    if len(parts) > 2:
        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                phases.append({
                    "title": parts[i].replace("## ", "").strip(),
                    "content": parts[i + 1].strip()[:2000],
                })
        return phases

    # Strategy 2: ### Phase N — Title (oil-gas style, nested under ## 7-Phase Narrative)
    parts = re.split(r"^(### Phase \d+\s*[—\-:].+?)$", text, flags=re.MULTILINE)
    if len(parts) > 2:
        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                phases.append({
                    "title": parts[i].replace("### ", "").strip(),
                    "content": parts[i + 1].strip()[:2000],
                })
        return phases

    # Strategy 3: Grab all ## sections after Executive Summary as ad-hoc phases
    # (bloom-energy style with custom section titles)
    all_sections = re.split(r"^(## .+?)$", text, flags=re.MULTILINE)
    found_exec = False
    stop_headers = {"Key Conclusion", "Rupture Window", "Aggregated Confidence Score",
                    "Risk Factors", "Sources", "Regional Dynamics Summary",
                    "Data Gaps", "Confidence"}
    for i in range(1, len(all_sections), 2):
        title = all_sections[i].replace("## ", "").strip()
        if "Executive Summary" in title:
            found_exec = True
            continue
        if not found_exec:
            continue
        if any(title.startswith(sh) for sh in stop_headers):
            break
        if i + 1 < len(all_sections):
            phases.append({
                "title": title,
                "content": all_sections[i + 1].strip()[:2000],
            })

    return phases


# ── Scanner ─────────────────────────────────────────────────────────

def scan_analyses(output_dir):
    analyses = []
    for d in sorted(output_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        readme = d / "README.md"
        synthesis = d / "00-final-synthesis.md"
        if not readme.exists() and not synthesis.exists():
            continue
        meta = parse_readme(readme) if readme.exists() else {
            "title": d.name, "config": "?", "date": "", "confidence": 0,
            "rupture_window": "", "tipping_point": "", "agent_count": 0,
            "query": "", "key_conclusion": "", "execution_table": [],
            "data_gaps": "", "evaluation": "", "skipped": "",
        }
        agents = {}
        agents_dir = d / "agents"
        if agents_dir.exists():
            for f in sorted(agents_dir.glob("*.md")):
                if f.name == "README.md":
                    continue
                ad = parse_agent_file(f)
                agents[ad["id"]] = ad
        synth_phases = parse_synthesis_phases(synthesis)
        analyses.append({"slug": d.name, **meta, "agents": agents, "synthesis_phases": synth_phases})
    return analyses


# ── HTML Template ───────────────────────────────────────────────────

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>STDF Pipeline Dashboard</title>
<style>
:root{--bg:#06080d;--bg2:#0d1117;--card:rgba(255,255,255,0.03);--card-hover:rgba(255,255,255,0.07);
--border:rgba(255,255,255,0.06);--border-hover:rgba(255,255,255,0.14);--text:#e2e8f0;--text2:#94a3b8;
--muted:#475569;--cyan:#00d4ff;--purple:#a855f7;--green:#10b981;--amber:#f59e0b;--red:#ef4444;
--font:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;
--mono:'SF Mono','Fira Code','Cascadia Code',monospace}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:
  radial-gradient(ellipse 80% 60% at 20% 10%,rgba(0,212,255,0.05),transparent),
  radial-gradient(ellipse 60% 50% at 80% 90%,rgba(168,85,247,0.04),transparent);pointer-events:none;z-index:0}
.hidden{display:none!important}
a{color:var(--cyan);text-decoration:none}
h1{font-size:2.6rem;font-weight:800;letter-spacing:-0.04em}
h2{font-size:1.5rem;font-weight:600;letter-spacing:-0.02em}
h3{font-size:1.15rem;font-weight:600}
h4{font-size:0.95rem;font-weight:600;color:var(--text2)}
.gradient-text{background:linear-gradient(135deg,var(--cyan),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.badge{font-size:0.7rem;padding:3px 10px;border-radius:6px;font-weight:600;letter-spacing:0.03em;text-transform:uppercase}
.badge-config{background:rgba(0,212,255,0.12);color:var(--cyan);border:1px solid rgba(0,212,255,0.2)}
.badge-date{background:rgba(148,163,184,0.08);color:var(--text2);border:1px solid rgba(148,163,184,0.12)}

/* ── Landing ── */
#landing{position:relative;z-index:1;max-width:1400px;margin:0 auto;padding:60px 32px 80px}
.landing-header{text-align:center;margin-bottom:52px}
.landing-header h1{margin-bottom:10px}
.subtitle{color:var(--text2);font-size:1.1rem;margin-bottom:28px}
.stats-bar{display:flex;gap:40px;justify-content:center;flex-wrap:wrap}
.stat{display:flex;flex-direction:column;align-items:center;gap:4px}
.stat-val{font-size:1.8rem;font-weight:800;font-family:var(--mono)}
.stat-label{font-size:0.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em}

/* Heatmap */
.heatmap-section{margin-bottom:40px;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;overflow-x:auto}
.heatmap-section h3{margin-bottom:4px}
.heatmap-section .hint{font-size:0.78rem;color:var(--muted);margin-bottom:16px}
.heatmap{display:grid;gap:2px;font-size:0.7rem}
.hm-cell{width:100%;aspect-ratio:1;border-radius:4px;display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:0.65rem;font-weight:600;cursor:default;transition:all .15s;position:relative}
.hm-cell:hover{transform:scale(1.15);z-index:2;box-shadow:0 0 12px rgba(0,0,0,0.5)}
.hm-cell[data-tip]:hover::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 6px);left:50%;
  transform:translateX(-50%);background:#1e293b;color:var(--text);padding:4px 8px;border-radius:5px;
  font-size:0.7rem;white-space:nowrap;pointer-events:none;z-index:10;border:1px solid var(--border)}
.hm-label{font-size:0.7rem;color:var(--text2);text-align:right;padding-right:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hm-col-label{font-size:0.62rem;color:var(--muted);text-align:center;writing-mode:vertical-rl;transform:rotate(180deg);height:70px;overflow:hidden}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:22px 24px;
  cursor:pointer;transition:all .25s ease;position:relative;overflow:hidden}
.card:hover{background:var(--card-hover);border-color:var(--border-hover);transform:translateY(-4px);
  box-shadow:0 16px 48px rgba(0,0,0,0.35)}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,var(--cyan),var(--purple));opacity:0;transition:opacity .25s}
.card:hover::before{opacity:1}
@keyframes cardIn{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
.card{animation:cardIn .5s ease backwards}
.card-title{font-size:1.08rem;font-weight:600;margin-bottom:8px;line-height:1.3}
.card-meta{display:flex;gap:8px;align-items:center;margin-bottom:12px;flex-wrap:wrap}
.card-conclusion{font-size:0.82rem;color:var(--text2);line-height:1.55;margin-bottom:14px;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.card-footer{display:flex;justify-content:space-between;align-items:center}
.confidence-mini{display:flex;align-items:center;gap:8px}
.conf-ring{width:36px;height:36px;position:relative}
.conf-ring svg{width:100%;height:100%}
.conf-ring-text{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-size:0.68rem;font-weight:700;font-family:var(--mono)}
.rupture-tag{font-size:0.78rem;color:var(--amber);font-weight:600;font-family:var(--mono)}
.tier-dots{display:flex;gap:3px;margin-top:12px}
.tier-dot{width:10px;height:10px;border-radius:3px;transition:all .2s}
.tier-dot:hover{transform:scale(1.3)}

/* ── Dashboard ── */
#dashboard{position:relative;z-index:1;max-width:1440px;margin:0 auto;padding:0 28px 60px}
.dash-nav{display:flex;align-items:center;gap:16px;padding:20px 0;border-bottom:1px solid var(--border);
  margin-bottom:28px;position:sticky;top:0;background:var(--bg);z-index:10}
.back-btn{background:var(--card);border:1px solid var(--border);color:var(--text2);padding:7px 16px;
  border-radius:8px;cursor:pointer;font-size:0.85rem;transition:all .2s}
.back-btn:hover{background:var(--card-hover);color:var(--text)}
.dash-nav h2{flex:1}

.overview-strip{display:grid;grid-template-columns:180px 1fr 1fr 1.3fr;gap:16px;margin-bottom:32px}
@media(max-width:900px){.overview-strip{grid-template-columns:1fr 1fr}}
.ov-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;display:flex;flex-direction:column;gap:6px}
.ov-label{font-size:0.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.05em}
.ov-value{font-size:1.1rem;font-weight:700}
.ov-sub{font-size:0.82rem;color:var(--text2);line-height:1.45}

.gauge-wrap{display:flex;align-items:center;justify-content:center;padding:8px 0}
.gauge-svg{width:120px;height:120px}
.gauge-track{fill:none;stroke:rgba(255,255,255,0.06);stroke-width:10}
.gauge-fill{fill:none;stroke-width:10;stroke-linecap:round;transition:stroke-dashoffset 1.5s cubic-bezier(.4,0,.2,1)}
.gauge-text{font-family:var(--mono);font-weight:800;font-size:22px;fill:var(--text);text-anchor:middle;dominant-baseline:central}
.gauge-label{font-size:8px;fill:var(--muted);text-anchor:middle;text-transform:uppercase;letter-spacing:0.12em}

/* ── DAG ── */
.dag-section{margin-bottom:32px}
.dag-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.dag-header h3{margin:0}
.dag-controls{display:flex;gap:8px;align-items:center}
.replay-btn{background:linear-gradient(135deg,rgba(0,212,255,0.15),rgba(168,85,247,0.15));
  border:1px solid rgba(0,212,255,0.3);color:var(--cyan);padding:6px 14px;border-radius:8px;
  cursor:pointer;font-size:0.8rem;font-weight:600;transition:all .2s;display:flex;align-items:center;gap:6px}
.replay-btn:hover{background:linear-gradient(135deg,rgba(0,212,255,0.25),rgba(168,85,247,0.25));transform:scale(1.03)}
.replay-btn svg{width:14px;height:14px}
.dag-hint{font-size:0.78rem;color:var(--muted)}
.dag-scroll{overflow-x:auto;padding:8px 0 16px;-webkit-overflow-scrolling:touch;
  background:rgba(0,0,0,0.2);border-radius:12px;border:1px solid var(--border)}
.dag-scroll::-webkit-scrollbar{height:6px}
.dag-scroll::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
#dag-svg{display:block;margin:0 auto}

/* DAG elements */
.dag-edge{fill:none;stroke:rgba(255,255,255,0.04);stroke-width:1.5;transition:all .6s ease}
.dag-edge.active{stroke:rgba(0,212,255,0.2);stroke-width:2}
.dag-edge.active.lit{stroke:rgba(0,212,255,0.45);stroke-dasharray:8 4;animation:dashFlow 1s linear infinite}
.dag-edge.synth-edge{stroke-dasharray:3 3}
@keyframes dashFlow{to{stroke-dashoffset:-12}}

.dag-node{opacity:0.12;transition:all .6s cubic-bezier(.4,0,.2,1)}
.dag-node.lit{opacity:1}
.dag-node-bg{rx:10;ry:10;fill:rgba(255,255,255,0.015);stroke:rgba(255,255,255,0.05);stroke-width:1;transition:all .5s}
.dag-node.lit .dag-node-bg{fill:rgba(13,17,23,0.9);stroke-width:1.5}
.dag-node.lit .dag-node-bg:hover{fill:rgba(0,212,255,0.08);cursor:pointer}
.dag-node-name{font-size:9.5px;fill:var(--muted);text-anchor:middle;pointer-events:none;font-weight:500;transition:fill .5s}
.dag-node.lit .dag-node-name{fill:var(--text)}
.dag-node-conf-bar{rx:2;ry:2;fill:rgba(255,255,255,0.04);transition:all .5s}
.dag-node-conf-fill{rx:2;ry:2;transition:all .8s cubic-bezier(.4,0,.2,1)}
.dag-node-conf-text{font-size:8px;font-family:var(--mono);font-weight:700;fill:var(--muted);text-anchor:end;pointer-events:none;transition:fill .5s}
.dag-glow{transition:all .6s}
.dag-tier-label{font-size:8px;fill:var(--muted);text-anchor:middle;text-transform:uppercase;letter-spacing:0.08em;font-weight:600}
.dag-tier-bg{fill:rgba(255,255,255,0.01);rx:8;ry:8}

/* Particle dots on edges */
.dag-particle{r:2.5;opacity:0;transition:opacity .3s}
.dag-particle.lit{opacity:1;animation:particleMove var(--dur,2s) linear infinite}

/* ── Agent Panel ── */
#agent-panel{background:var(--bg2);border:1px solid var(--border);border-radius:14px;margin-bottom:32px;
  overflow:hidden;animation:slideUp .35s ease}
@keyframes slideUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.panel-header{display:flex;justify-content:space-between;align-items:center;padding:16px 22px;
  border-bottom:1px solid var(--border);background:var(--card)}
.panel-header h3{display:flex;align-items:center;gap:10px}
.close-btn{background:none;border:1px solid var(--border);color:var(--text2);width:30px;height:30px;
  border-radius:8px;cursor:pointer;font-size:1.1rem;display:flex;align-items:center;justify-content:center;transition:all .2s}
.close-btn:hover{background:var(--card-hover);color:var(--text)}
#panel-content{padding:22px;max-height:600px;overflow-y:auto}
#panel-content::-webkit-scrollbar{width:5px}
#panel-content::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
.panel-findings{font-size:0.88rem;line-height:1.65;color:var(--text2)}
.panel-findings strong{color:var(--text)}
.panel-findings h3,.panel-findings h4{color:var(--text);margin:14px 0 6px}
.panel-table{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.82rem}
.panel-table th{background:rgba(0,212,255,0.06);color:var(--cyan);font-weight:600;text-align:left;
  padding:8px 12px;border-bottom:1px solid var(--border)}
.panel-table td{padding:7px 12px;border-bottom:1px solid var(--border);color:var(--text2)}
.panel-table tr:hover td{background:rgba(255,255,255,0.02)}

/* ── Synthesis ── */
.synthesis-section{margin-bottom:32px}
.synthesis-section h3{margin-bottom:16px}
.phase-list{display:flex;flex-direction:column;gap:3px}
.phase-item{background:var(--card);border:1px solid var(--border);border-radius:10px;overflow:hidden;transition:all .2s}
.phase-header{padding:14px 20px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;transition:background .2s}
.phase-header:hover{background:var(--card-hover)}
.phase-header h4{font-size:0.9rem;color:var(--text)}
.phase-num{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:6px;
  background:rgba(0,212,255,0.1);color:var(--cyan);font-size:0.7rem;font-weight:700;margin-right:10px;flex-shrink:0}
.phase-arrow{color:var(--muted);transition:transform .25s;font-size:0.75rem}
.phase-item.open .phase-arrow{transform:rotate(90deg)}
.phase-body{max-height:0;overflow:hidden;transition:max-height .4s ease}
.phase-item.open .phase-body{max-height:3000px}
.phase-content{padding:0 20px 18px;font-size:0.85rem;line-height:1.65;color:var(--text2)}
.phase-content strong{color:var(--text)}

/* ── Footer ── */
.footer-section{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px}
@media(max-width:700px){.footer-section{grid-template-columns:1fr}}
.footer-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px}
.footer-card h4{margin-bottom:8px;color:var(--text2)}
.footer-card p{font-size:0.82rem;line-height:1.5;color:var(--muted)}
</style>
</head>
<body>

<div id="landing">
  <div class="landing-header">
    <h1>STDF Pipeline <span class="gradient-text">Visualizer</span></h1>
    <p class="subtitle">Multi-Agent Technology Disruption Analysis &mdash; Query Lifecycle &amp; Agent Workflow</p>
    <div class="stats-bar" id="global-stats"></div>
  </div>
  <div class="heatmap-section">
    <h3>Confidence Heatmap &mdash; All Analyses &times; All Agents</h3>
    <p class="hint">Each cell shows an agent's confidence score for that analysis. Click any cell to jump to it.</p>
    <div id="heatmap"></div>
  </div>
  <h3 style="margin-bottom:16px">Analysis Runs</h3>
  <div class="grid" id="analysis-grid"></div>
</div>

<div id="dashboard" class="hidden">
  <nav class="dash-nav">
    <button onclick="showLanding()" class="back-btn">&larr; All Analyses</button>
    <h2 id="dash-title"></h2>
    <span class="badge badge-config" id="dash-config"></span>
  </nav>
  <div id="query-bar" style="margin-bottom:20px;padding:14px 20px;background:var(--card);border:1px solid var(--border);border-radius:10px;font-size:0.88rem;color:var(--text2);line-height:1.5"></div>
  <div class="overview-strip" id="overview"></div>
  <div class="dag-section">
    <div class="dag-header">
      <div>
        <h3>Agent Pipeline Flow</h3>
        <p class="dag-hint">Click any active node to inspect findings. Nodes light up in execution order.</p>
      </div>
      <button class="replay-btn" onclick="replayDAG()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M1 4v6h6M23 20v-6h-6"/><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"/></svg>
        Replay
      </button>
    </div>
    <div class="dag-scroll"><svg id="dag-svg"></svg></div>
  </div>
  <div id="agent-panel" class="hidden"></div>
  <div class="synthesis-section" id="synthesis-section">
    <h3>Final Synthesis</h3>
    <div class="phase-list" id="phase-list"></div>
  </div>
  <div class="footer-section" id="footer-info"></div>
</div>

<script>
const DATA = /*__DATA__*/;
const analyses = DATA.analyses;
const pipeline = DATA.pipeline;

// ── Helpers ──
function confColor(c){
  if(c==null)return'#475569';if(c>=0.85)return'#10b981';if(c>=0.7)return'#00d4ff';
  if(c>=0.55)return'#f59e0b';return'#ef4444';
}
function confBg(c){
  if(c==null)return'rgba(71,85,105,0.15)';if(c>=0.85)return'rgba(16,185,129,0.12)';
  if(c>=0.7)return'rgba(0,212,255,0.12)';if(c>=0.55)return'rgba(245,158,11,0.12)';return'rgba(239,68,68,0.12)';
}
function md(t){if(!t)return'';return t
  .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
  .replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>').replace(/\*(.+?)\*/g,'<em>$1</em>')
  .replace(/^#### (.+)$/gm,'<h4 style="margin:10px 0 4px">$1</h4>')
  .replace(/^### (.+)$/gm,'<h3 style="margin:14px 0 6px">$1</h3>')
  .replace(/^- (.+)$/gm,'<div style="padding-left:16px;margin:2px 0">&bull; $1</div>')
  .replace(/\n\n/g,'<br><br>').replace(/\n/g,'<br>');}
function renderTable(rows){if(!rows||!rows.length)return'';let h='<table class="panel-table">';
  for(const r of rows){h+='<tr>';const t=r.header?'th':'td';for(const c of r.cells)h+=`<${t}>${c}</${t}>`;h+='</tr>';}
  return h+'</table>';}
function miniRing(conf,size=36){const c=2*Math.PI*13;const o=c*(1-(conf||0));const col=confColor(conf);
  return`<div class="conf-ring" style="width:${size}px;height:${size}px"><svg viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="13" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="3"/>
  <circle cx="16" cy="16" r="13" fill="none" stroke="${col}" stroke-width="3" stroke-linecap="round"
  stroke-dasharray="${c}" stroke-dashoffset="${o}" transform="rotate(-90 16 16)"/></svg>
  <span class="conf-ring-text" style="color:${col}">${conf?conf.toFixed(2):'—'}</span></div>`;}

// ── Landing ──
const sorted=[...analyses].sort((a,b)=>(b.date||'').localeCompare(a.date||'')||a.slug.localeCompare(b.slug));

function renderGlobalStats(){
  const ta=analyses.reduce((s,a)=>s+Object.keys(a.agents).length,0);
  const ac=analyses.filter(a=>a.confidence>0);
  const avg=ac.length?(ac.reduce((s,a)=>s+a.confidence,0)/ac.length).toFixed(2):'—';
  const dates=analyses.map(a=>a.date).filter(Boolean).sort();
  document.getElementById('global-stats').innerHTML=`
    <div class="stat"><span class="stat-val" style="color:var(--cyan)">${analyses.length}</span><span class="stat-label">Analyses</span></div>
    <div class="stat"><span class="stat-val" style="color:var(--purple)">${ta}</span><span class="stat-label">Agent Runs</span></div>
    <div class="stat"><span class="stat-val" style="color:var(--green)">${avg}</span><span class="stat-label">Avg Confidence</span></div>
    <div class="stat"><span class="stat-val" style="color:var(--text2)">${dates[0]||'—'} &rarr; ${dates[dates.length-1]||'—'}</span><span class="stat-label">Date Range</span></div>`;
}

function renderHeatmap(){
  const agentIds=['domain-disruption','cost-researcher','capability','cost-fitter','cost-parity','cap-parity',
    'adopt-readiness','tipping-synthesizer','scurve-fitter','regional-adopter','xcurve-analyst',
    'demand-decomposer','stream-forecaster','fleet-modeler','regional-demand','energy-dispatch','gas-supply','synthesizer','evaluator'];
  const shortNames=['Domain','Cost Res','Capab','Cost Fit','Cost Par','Cap Par','Adopt','Tipping',
    'S-Curve','Regional','X-Curve','Demand','Stream','Fleet','Reg Dem','Dispatch','Gas','Synth','Eval'];
  const cols=agentIds.length;
  const el=document.getElementById('heatmap');
  const gCols=`140px repeat(${cols},1fr)`;
  let h=`<div class="heatmap" style="grid-template-columns:${gCols}">`;
  // Column headers
  h+=`<div></div>`;
  for(let i=0;i<cols;i++) h+=`<div class="hm-col-label">${shortNames[i]}</div>`;
  // Rows
  for(let ri=0;ri<sorted.length;ri++){
    const a=sorted[ri];
    const name=a.title.replace(/STDF (?:Analysis|Pipeline Run): ?/i,'').substring(0,22);
    h+=`<div class="hm-label" title="${a.title}">${name}</div>`;
    for(let ci=0;ci<cols;ci++){
      const ag=a.agents[agentIds[ci]];
      const c=ag?.confidence;
      const bg=c!=null?confBg(c):'rgba(255,255,255,0.015)';
      const txt=c!=null?c.toFixed(2):'';
      const tip=`${shortNames[ci]}: ${c!=null?c.toFixed(2):'—'} (${a.slug})`;
      h+=`<div class="hm-cell" style="background:${bg};color:${confColor(c)}" data-tip="${tip}"
        onclick="showDashboard(${ri})${ag?`;setTimeout(()=>openPanel('${agentIds[ci]}'),300)`:''}">${txt}</div>`;
    }
  }
  h+='</div>';
  el.innerHTML=h;
}

function renderLanding(){
  renderGlobalStats();
  renderHeatmap();
  const grid=document.getElementById('analysis-grid');
  grid.innerHTML=sorted.map((a,idx)=>{
    const conf=a.confidence||0;const color=confColor(conf||null);
    const activeAgents=Object.keys(a.agents);
    const tierDots=pipeline.tiers.map(t=>{
      const has=t.agents.some(ag=>activeAgents.includes(ag.id));
      const tc=t.agents.filter(ag=>a.agents[ag.id]?.confidence!=null).map(ag=>a.agents[ag.id].confidence);
      const at=tc.length?tc.reduce((s,v)=>s+v,0)/tc.length:0;
      return`<div class="tier-dot" title="${t.label}" style="background:${has?confColor(at):'rgba(255,255,255,0.04)'}"></div>`;
    }).join('');
    return`<div class="card" onclick="showDashboard(${idx})" style="animation-delay:${idx*50}ms">
      <div class="card-title">${a.title}</div>
      <div class="card-meta">
        <span class="badge badge-config">${a.config}</span>
        ${a.date?`<span class="badge badge-date">${a.date}</span>`:''}
        <span style="font-size:0.75rem;color:var(--muted)">${activeAgents.length} agents</span>
      </div>
      ${a.key_conclusion?`<div class="card-conclusion">${a.key_conclusion.replace(/\*\*/g,'')}</div>`:''}
      <div class="card-footer">
        <div class="confidence-mini">${miniRing(conf,38)}
          <span style="font-family:var(--mono);font-size:0.82rem;font-weight:700;color:${color}">${conf?conf.toFixed(2):'—'}</span>
        </div>
        ${a.rupture_window?`<span class="rupture-tag">${a.rupture_window}</span>`:''}
      </div>
      <div class="tier-dots">${tierDots}</div>
    </div>`;
  }).join('');
}

// ── Dashboard ──
let currentAnalysis=null;
function showLanding(){document.getElementById('landing').classList.remove('hidden');
  document.getElementById('dashboard').classList.add('hidden');currentAnalysis=null;}

function showDashboard(idx){
  currentAnalysis=sorted[idx];const a=currentAnalysis;
  document.getElementById('landing').classList.add('hidden');
  document.getElementById('dashboard').classList.remove('hidden');
  document.getElementById('dash-title').textContent=a.title;
  document.getElementById('dash-config').textContent=a.config;
  document.getElementById('query-bar').innerHTML=a.query
    ?`<strong style="color:var(--text)">Query:</strong> ${a.query}`
    :`<strong style="color:var(--text)">Analysis:</strong> ${a.title}`;
  renderOverview(a);renderDAG(a);closePanel();renderSynthesis(a);renderFooter(a);
  window.scrollTo(0,0);
  setTimeout(()=>animateDAG(a),100);
}

function renderOverview(a){
  const conf=a.confidence||0;const circ=2*Math.PI*42;const off=circ*(1-conf);const col=confColor(conf||null);
  document.getElementById('overview').innerHTML=`
    <div class="ov-card gauge-wrap">
      <svg class="gauge-svg" viewBox="0 0 100 100">
        <circle class="gauge-track" cx="50" cy="50" r="42"/>
        <circle class="gauge-fill" cx="50" cy="50" r="42" stroke="${col}"
          stroke-dasharray="${circ}" stroke-dashoffset="${off}" transform="rotate(-90 50 50)"/>
        <text class="gauge-text" x="50" y="45">${conf?conf.toFixed(2):'—'}</text>
        <text class="gauge-label" x="50" y="62">confidence</text>
      </svg>
    </div>
    <div class="ov-card">
      <div class="ov-label">Rupture Window</div>
      <div class="ov-value" style="color:var(--amber)">${a.rupture_window||'—'}</div>
      ${a.tipping_point?`<div class="ov-sub">Tipping: ${a.tipping_point}</div>`:''}
      <div class="ov-sub" style="margin-top:4px">${a.date?'Analysis date: '+a.date:''}</div>
    </div>
    <div class="ov-card">
      <div class="ov-label">Configuration</div>
      <div class="ov-value">${a.config}</div>
      <div class="ov-sub">${a.agent_count?a.agent_count+' agents in pipeline':Object.keys(a.agents).length+' agent outputs'}</div>
    </div>
    <div class="ov-card">
      <div class="ov-label">Key Conclusion</div>
      <div class="ov-sub">${a.key_conclusion?a.key_conclusion.substring(0,280).replace(/\*\*/g,'')+(a.key_conclusion.length>280?'...':''):'See synthesis below'}</div>
    </div>`;
}

// ── DAG ──
const NP={
  'domain-disruption':{x:140,y:30,tier:1},'cost-researcher':{x:140,y:100,tier:1},'capability':{x:140,y:170,tier:1},
  'cost-fitter':{x:290,y:100,tier:2},
  'cost-parity':{x:440,y:30,tier:3},'cap-parity':{x:440,y:100,tier:3},'adopt-readiness':{x:440,y:170,tier:3},
  'tipping-synthesizer':{x:590,y:100,tier:4},
  'scurve-fitter':{x:740,y:65,tier:5},
  'regional-adopter':{x:890,y:30,tier:5.5},'xcurve-analyst':{x:890,y:120,tier:5.5},
  'demand-decomposer':{x:740,y:260,tier:6},'stream-forecaster':{x:890,y:260,tier:6},
  'fleet-modeler':{x:1040,y:235,tier:6},'regional-demand':{x:1040,y:295,tier:6},
  'energy-dispatch':{x:740,y:350,tier:7},'gas-supply':{x:890,y:350,tier:7},
  'synthesizer':{x:1040,y:100,tier:8},'evaluator':{x:1190,y:100,tier:9},
};
const NW=125,NH=48;

// Edge labels: what data flows between agents
const EDGE_LABELS={
  'cost-researcher->cost-fitter':'cost data','cost-fitter->cost-parity':'fitted curves',
  'capability->cap-parity':'benchmarks','cost-parity->tipping-synthesizer':'cost condition',
  'cap-parity->tipping-synthesizer':'cap condition','adopt-readiness->tipping-synthesizer':'readiness',
  'tipping-synthesizer->scurve-fitter':'tipping params','scurve-fitter->regional-adopter':'S-curve',
  'scurve-fitter->xcurve-analyst':'adoption curve','energy-dispatch->gas-supply':'dispatch model',
  'demand-decomposer->stream-forecaster':'demand streams',
};

function renderDAG(a){
  const svg=document.getElementById('dag-svg');
  const active=new Set(Object.keys(a.agents));
  const hasLower=['demand-decomposer','stream-forecaster','fleet-modeler','regional-demand','energy-dispatch','gas-supply'].some(id=>active.has(id));
  const svgH=hasLower?410:220;
  svg.setAttribute('width',1320);svg.setAttribute('height',svgH);svg.setAttribute('viewBox',`0 0 1320 ${svgH}`);

  let h='<defs><filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>';

  // Tier background bands
  const tierBands=[{x:120,label:'TIER 1'},{x:270,label:'TIER 2'},{x:420,label:'TIER 3'},
    {x:570,label:'TIER 4'},{x:720,label:'TIER 5'},{x:870,label:'TIER 5B'},
    {x:1020,label:'SYNTH'},{x:1170,label:'EVAL'}];
  for(const tb of tierBands){
    h+=`<rect class="dag-tier-bg" x="${tb.x-5}" y="18" width="${NW+10}" height="${svgH-28}" opacity="0.3"/>`;
    h+=`<text class="dag-tier-label" x="${tb.x+NW/2}" y="12">${tb.label}</text>`;
  }
  if(hasLower) h+=`<text class="dag-tier-label" x="${740+NW/2}" y="244">CONDITIONAL TIERS</text>`;

  // Edges (drawn first, behind nodes)
  const allEdges=[...pipeline.edges];
  // Add synth fan-in edges
  if(active.has('synthesizer')){
    for(const id of active){
      if(id==='synthesizer'||id==='evaluator')continue;
      if(!NP[id])continue;
      const hasOutEdge=pipeline.edges.some(([f,t])=>f===id&&active.has(t));
      if(!hasOutEdge) allEdges.push([id,'synthesizer']);
    }
  }
  if(active.has('synthesizer')&&active.has('evaluator')) allEdges.push(['synthesizer','evaluator']);

  for(const [from,to] of allEdges){
    const p1=NP[from],p2=NP[to];if(!p1||!p2)continue;
    const x1=p1.x+NW,y1=p1.y+NH/2,x2=p2.x,y2=p2.y+NH/2;
    const isActive=active.has(from)&&active.has(to);
    const isSynth=to==='synthesizer'&&!pipeline.edges.some(([f,t])=>f===from&&t===to);
    const mx=(x1+x2)/2;
    const cls=`dag-edge${isActive?' active':''}${isSynth?' synth-edge':''}`;
    const opa=isSynth?'opacity:0.12':'';
    h+=`<path class="${cls}" data-from="${from}" data-to="${to}" d="M${x1} ${y1} C${mx} ${y1},${mx} ${y2},${x2} ${y2}" style="${opa}"/>`;
    // Edge label
    const lk=from+'->'+to;
    if(EDGE_LABELS[lk]&&isActive){
      const lx=(x1+x2)/2,ly=(y1+y2)/2-6;
      h+=`<text x="${lx}" y="${ly}" text-anchor="middle" font-size="7" fill="rgba(0,212,255,0.35)" font-style="italic">${EDGE_LABELS[lk]}</text>`;
    }
  }

  // Query node
  h+=`<g><rect x="10" y="84" width="80" height="32" rx="16" fill="rgba(0,212,255,0.06)" stroke="var(--cyan)" stroke-width="1.5"/>
    <text x="50" y="104" text-anchor="middle" fill="var(--cyan)" font-size="10" font-weight="700">QUERY</text></g>`;
  ['domain-disruption','cost-researcher','capability'].forEach(tid=>{
    const tp=NP[tid];if(!tp)return;
    h+=`<path d="M90 100 C115 100,115 ${tp.y+NH/2},${tp.x} ${tp.y+NH/2}" class="dag-edge${active.has(tid)?' active':''}"/>`;
  });

  // Nodes
  for(const[id,pos]of Object.entries(NP)){
    const isA=active.has(id);const ag=a.agents[id];const conf=ag?.confidence;const col=confColor(conf);
    const name=id.split('-').map(w=>w[0].toUpperCase()+w.slice(1)).join(' ');
    const lines=name.length>17?name.replace(/ /g,'\n').split('\n'):[name];

    h+=`<g class="dag-node" data-agent="${id}" data-tier="${pos.tier}" ${isA?`onclick="openPanel('${id}')"`:''}>`;
    // Glow
    if(isA&&conf) h+=`<rect class="dag-glow" x="${pos.x-5}" y="${pos.y-5}" width="${NW+10}" height="${NH+10}" rx="14"
      fill="none" stroke="${col}" stroke-width="1.5" filter="url(#glow)" opacity="0"/>`;
    // Background
    h+=`<rect class="dag-node-bg" x="${pos.x}" y="${pos.y}" width="${NW}" height="${NH}"${isA?` style="stroke:${col}"`:''}/>`;
    // Name
    if(lines.length===1){
      h+=`<text class="dag-node-name" x="${pos.x+NW/2}" y="${pos.y+(conf!=null?17:NH/2)}">${lines[0]}</text>`;
    }else{
      h+=`<text class="dag-node-name" x="${pos.x+NW/2}" y="${pos.y+14}">${lines[0]}</text>`;
      h+=`<text class="dag-node-name" x="${pos.x+NW/2}" y="${pos.y+25}">${lines[1]||''}</text>`;
    }
    // Confidence bar inside node
    if(isA&&conf!=null){
      const barW=NW-16,barH=5,barX=pos.x+8,barY=pos.y+NH-12;
      h+=`<rect class="dag-node-conf-bar" x="${barX}" y="${barY}" width="${barW}" height="${barH}"/>`;
      h+=`<rect class="dag-node-conf-fill" x="${barX}" y="${barY}" width="${barW*conf}" height="${barH}" fill="${col}" opacity="0.7"/>`;
      h+=`<text class="dag-node-conf-text" x="${pos.x+NW-8}" y="${barY-2}" style="fill:${col}">${conf.toFixed(2)}</text>`;
    }
    h+='</g>';
  }

  svg.innerHTML=h;
}

// ── DAG Animation ──
let animTimer=null;
function animateDAG(a){
  if(animTimer)clearTimeout(animTimer);
  const nodes=document.querySelectorAll('#dag-svg .dag-node');
  const edges=document.querySelectorAll('#dag-svg .dag-edge');
  const active=new Set(Object.keys(a.agents));
  // Reset
  nodes.forEach(n=>{n.classList.remove('lit');const g=n.querySelector('.dag-glow');if(g)g.style.opacity='0';});
  edges.forEach(e=>e.classList.remove('lit'));

  // Group nodes by tier
  const tierMap={};
  nodes.forEach(n=>{const t=parseFloat(n.dataset.tier)||0;(tierMap[t]=tierMap[t]||[]).push(n);});
  const tiers=Object.keys(tierMap).sort((a,b)=>a-b);

  let delay=0;
  for(const t of tiers){
    const tierNodes=tierMap[t];
    animTimer=setTimeout(()=>{
      tierNodes.forEach(n=>{
        if(active.has(n.dataset.agent)){
          n.classList.add('lit');
          const g=n.querySelector('.dag-glow');if(g)g.style.opacity='0.5';
          // Light up incoming edges
          edges.forEach(e=>{
            if(e.dataset.to===n.dataset.agent&&active.has(e.dataset.from))e.classList.add('lit');
          });
        }
      });
    },delay);
    delay+=350;
  }
}
function replayDAG(){if(currentAnalysis)animateDAG(currentAnalysis);}

// ── Agent Panel ──
function openPanel(agentId){
  if(!currentAnalysis)return;const agent=currentAnalysis.agents[agentId];if(!agent)return;
  const panel=document.getElementById('agent-panel');
  const conf=agent.confidence;const col=confColor(conf);
  const name=agentId.split('-').map(w=>w[0].toUpperCase()+w.slice(1)).join(' ');
  let tabH='';if(agent.tables?.length)for(const t of agent.tables)tabH+=renderTable(t);
  panel.innerHTML=`
    <div class="panel-header">
      <h3><span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:${col}"></span>
        ${name}<span style="font-family:var(--mono);font-size:0.85rem;color:${col};margin-left:8px">${conf!=null?conf.toFixed(2):'—'}</span></h3>
      <div style="display:flex;gap:10px;align-items:center">
        <span style="font-size:0.75rem;color:var(--muted)">${agent.file}</span>
        <button onclick="closePanel()" class="close-btn">&times;</button></div>
    </div>
    <div id="panel-content"><div class="panel-findings">${md(agent.key_findings)}</div>${tabH}</div>`;
  panel.classList.remove('hidden');panel.scrollIntoView({behavior:'smooth',block:'nearest'});
}
function closePanel(){document.getElementById('agent-panel').classList.add('hidden');}

// ── Synthesis ──
function renderSynthesis(a){
  const list=document.getElementById('phase-list');
  if(!a.synthesis_phases?.length){document.getElementById('synthesis-section').classList.add('hidden');return;}
  document.getElementById('synthesis-section').classList.remove('hidden');
  list.innerHTML=a.synthesis_phases.map((p,i)=>{
    const m2=p.title.match(/Phase\s*(\d+)/i);const num=m2?m2[1]:(i===0?'E':(i));
    return`<div class="phase-item${i===0?' open':''}">
      <div class="phase-header" onclick="this.parentElement.classList.toggle('open')">
        <h4><span class="phase-num">${num}</span>${p.title.replace(/^Phase\s*\d+\s*[:\-—]\s*/i,'')}</h4>
        <span class="phase-arrow">&#9654;</span></div>
      <div class="phase-body"><div class="phase-content">${md(p.content)}</div></div></div>`;
  }).join('');
}

// ── Footer ──
function renderFooter(a){
  const f=document.getElementById('footer-info');const p=[];
  if(a.data_gaps)p.push(`<div class="footer-card"><h4>Data Gaps</h4><p>${md(a.data_gaps)}</p></div>`);
  if(a.evaluation)p.push(`<div class="footer-card"><h4>Evaluation</h4><p>${md(a.evaluation)}</p></div>`);
  if(a.skipped)p.push(`<div class="footer-card"><h4>Agents Skipped</h4><p>${md(a.skipped)}</p></div>`);
  f.innerHTML=p.join('');
}

// ── Init ──
renderLanding();
</script>
</body>
</html>"""


# ── Generator ───────────────────────────────────────────────────────

def generate_html(analyses_list, pipeline_def):
    data = {"analyses": analyses_list, "pipeline": pipeline_def}
    data_json = json.dumps(data, ensure_ascii=False)
    return HTML_TEMPLATE.replace("/*__DATA__*/", data_json)


def main():
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir.parent / "output"
    if not output_dir.exists():
        print(f"Error: output directory not found: {output_dir}", file=sys.stderr)
        sys.exit(1)

    print("Scanning analyses...")
    analyses_list = scan_analyses(output_dir)
    print(f"Found {len(analyses_list)} analyses with {sum(len(a['agents']) for a in analyses_list)} total agent outputs")

    html = generate_html(analyses_list, PIPELINE)
    out_path = output_dir / "dashboard.html"
    out_path.write_text(html, encoding="utf-8")
    size_kb = out_path.stat().st_size / 1024
    print(f"Dashboard written to: {out_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
