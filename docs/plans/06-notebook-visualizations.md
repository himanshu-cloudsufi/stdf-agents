# Plan 06: Jupyter Notebook Visualizations

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| NotebookEdit tool exists | VERIFIED | Schema: `notebook_path`, `new_source`, `cell_id`, `cell_type`, `edit_mode` |
| Read tool handles .ipynb | VERIFIED | Returns raw JSON; large notebooks may truncate at 2000 lines |
| NotebookEdit can create/modify/delete cells | VERIFIED | Modes: `replace`, `insert`, `delete` |
| NotebookEdit can run cells | INCORRECT | Edits JSON only — no execution. Use `jupyter nbconvert --execute` |
| No Jupyter kernel required | VERIFIED | Edits .ipynb JSON directly |
| Cell types: code, markdown, raw | PARTIALLY CORRECT | Only `code` and `markdown` — no `raw` support |
| Agents can create notebooks from scratch | INCORRECT | NotebookEdit requires existing file — use Write/Bash `cp` first |
| Template copy-then-modify works | VERIFIED | Must use Bash `cp` first, then NotebookEdit for cell edits |
| Numeric cell indices ("Cell 2") | INCORRECT | Uses `cell_id` string from notebook JSON metadata, not position numbers |
| Plots rendered in notebooks | REQUIRES EXTRA STEP | Must run `jupyter nbconvert --execute` after editing |
| NotebookRead tool | REMOVED | Was deprecated; Read tool handles .ipynb as raw JSON |
| Cell ID hallucination risk | REAL ISSUE | Sonnet may fabricate cell_id values — extract real IDs first |
| Notebook corruption in CI | DOCUMENTED ISSUE | .ipynb JSON can be corrupted under automation |

### Critical Corrections

1. **NotebookEdit cannot create new files** — must `cp` template or Write valid .ipynb JSON first
2. **NotebookEdit cannot execute cells** — must run `jupyter nbconvert --execute` separately
3. **Cell targeting uses `cell_id` strings**, not numeric indices — templates must have human-readable IDs
4. **Agents must extract real cell IDs** before editing — never fabricate them
5. **Static PNG/HTML should be the primary output** for headless runs; notebooks are optional interactive enhancement

## What We Get

- **Interactive cost curve plots** — exponential decay curves with data points, fit line, R², threshold
- **S-curve adoption charts** — logistic curves per region with fitted parameters
- **Agent confidence radar chart** — 6-axis radar showing per-agent scores
- **Static PNG/HTML charts** — always-work primary output for headless/CI runs
- **Optional Jupyter notebooks** — interactive exploration for users with Jupyter installed

## How We Do This

### Architecture Decision: Static Charts Primary, Notebooks Optional

Given NotebookEdit's limitations (no execution, corruption risk in CI, cell ID hallucination), the plan uses a **two-tier approach**:

1. **Primary: Static charts via python3 scripts** — always works, no Jupyter dependency
2. **Optional: Jupyter notebooks** — for interactive exploration when Jupyter is available

```
output/<analysis-slug>/
├── README.md
├── 00-final-synthesis.md
├── charts/                        ← PRIMARY: static PNG + HTML, always generated
│   ├── cost_curve.png
│   ├── adoption_scurve.png
│   ├── confidence_radar.png
│   └── phase_timeline.png
├── notebooks/                     ← OPTIONAL: interactive, requires jupyter
│   ├── cost_curve.ipynb
│   ├── adoption_scurve.ipynb
│   └── analysis_summary.ipynb
└── agents/
    └── ...
```

### Step 1: Create Visualization Helper Script

**`scripts/stdf_plots.py`** — reusable plotting functions called via Bash:

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def plot_cost_curve(disruptor_data, incumbent_data, fit_params, threshold_year, output_path):
    """Plot disruptor vs incumbent cost trajectories with crossover."""
    # ... matplotlib code ...
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

def plot_scurve(params_by_region, title, output_path):
    """Plot logistic S-curves for multiple regions."""
    # ... matplotlib code ...
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

def plot_xcurve(adoption_params, decline_params, output_path):
    """Plot X-curve: rising disruptor + declining incumbent."""
    # ... matplotlib code ...
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

def plot_confidence_radar(agent_scores, output_path):
    """6-axis radar chart of agent confidence scores."""
    # ... matplotlib code ...
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

def plot_phase_timeline(phases, output_path):
    """Horizontal timeline of 7 disruption phases."""
    # ... matplotlib code ...
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

Agents call via Bash:
```bash
python3 scripts/stdf_plots.py cost_curve --data '{"disruptor": [...], "incumbent": [...]}' --output output/<slug>/charts/cost_curve.png
```

### Step 2: Create Template Notebooks (with Human-Readable Cell IDs)

Templates must use **human-readable `cell_id` values** so agents can target them reliably.

**`templates/cost_curve_analysis.ipynb`** (minimal valid structure):
```json
{
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.12.0"}
 },
 "cells": [
  {
   "id": "imports",
   "cell_type": "code",
   "source": ["import matplotlib.pyplot as plt\nimport numpy as np\nfrom scipy.optimize import curve_fit"],
   "metadata": {}, "outputs": [], "execution_count": null
  },
  {
   "id": "data-input",
   "cell_type": "code",
   "source": ["# AGENT WRITES HERE: disruptor and incumbent cost data arrays"],
   "metadata": {}, "outputs": [], "execution_count": null
  },
  {
   "id": "cost-curve-plot",
   "cell_type": "code",
   "source": ["# AGENT WRITES HERE: exponential fit and cost curve visualization"],
   "metadata": {}, "outputs": [], "execution_count": null
  },
  {
   "id": "threshold-plot",
   "cell_type": "code",
   "source": ["# AGENT WRITES HERE: competitive threshold visualization"],
   "metadata": {}, "outputs": [], "execution_count": null
  },
  {
   "id": "learning-rate",
   "cell_type": "code",
   "source": ["# AGENT WRITES HERE: learning rate comparison chart"],
   "metadata": {}, "outputs": [], "execution_count": null
  }
 ]
}
```

Similar templates for `adoption_scurve.ipynb` and `pipeline_summary.ipynb`.

### Step 3: Agent Notebook Workflow (Correct Sequence)

For each agent that generates visualizations:

```
1. Bash: mkdir -p output/<slug>/charts output/<slug>/notebooks

2. PRIMARY — Generate static charts:
   Bash: python3 scripts/stdf_plots.py cost_curve --data '<json>' --output output/<slug>/charts/cost_curve.png

3. OPTIONAL — Populate notebook:
   a. Bash: cp templates/cost_curve_analysis.ipynb output/<slug>/notebooks/cost_curve.ipynb
   b. NotebookEdit:
        notebook_path: /abs/path/output/<slug>/notebooks/cost_curve.ipynb
        cell_id: "data-input"
        edit_mode: replace
        new_source: "years = [2015, 2017, 2019, 2021, 2023]\ncosts = [350, 220, 157, 132, 92]..."
   c. NotebookEdit:
        notebook_path: /abs/path/output/<slug>/notebooks/cost_curve.ipynb
        cell_id: "cost-curve-plot"
        edit_mode: replace
        new_source: "<plotting code>"

4. OPTIONAL — Execute notebook (requires jupyter):
   Bash: jupyter nbconvert --to notebook --execute output/<slug>/notebooks/cost_curve.ipynb --output cost_curve.ipynb
   Bash: jupyter nbconvert --to html output/<slug>/notebooks/cost_curve.ipynb
```

**Critical**: Steps 3-4 are optional and should fail gracefully if Jupyter isn't installed.

### Step 4: NotebookEdit Safety Rules

Add to agent definitions that use NotebookEdit:

```markdown
## NotebookEdit Rules
- ALWAYS use Bash `cp` to copy a template before using NotebookEdit on a new notebook
- NotebookEdit CANNOT create new files — it requires an existing .ipynb
- ALWAYS use absolute paths for notebook_path
- ALWAYS extract real cell IDs before editing:
  python3 -c "import json; nb=json.load(open('PATH')); [print(c['id']) for c in nb['cells']]"
- NEVER fabricate cell_id values — use only IDs from the actual file
- Only `code` and `markdown` cell types are supported (no `raw`)
- NotebookEdit does NOT execute cells — use jupyter nbconvert --execute separately
- After editing, validate: jupyter nbformat validate PATH
```

### NotebookEdit Schema Reference (Official)

```json
{
  "notebook_path": "string (absolute path, REQUIRED)",
  "new_source": "string (new cell content, REQUIRED)",
  "cell_id": "string (target cell ID, optional on insert)",
  "cell_type": "code | markdown (required on insert)",
  "edit_mode": "replace | insert | delete (default: replace)"
}
```

| Mode | Behavior |
|------|----------|
| `replace` | Replace content of cell with matching `cell_id` |
| `insert` | Insert new cell AFTER `cell_id` (beginning if omitted) |
| `delete` | Remove cell with matching `cell_id` |

### Known Issues & Mitigations

| Issue | Source | Mitigation |
|-------|--------|------------|
| Cell insertion order bug | GitHub #5197 | Always specify `cell_id` for insert — don't rely on default positioning |
| Sonnet hallucinating cell IDs | GitHub #5197 | Extract real IDs via python3 before editing |
| .ipynb JSON corruption in CI | GitHub #1839 | Use static charts as primary; notebooks as optional |
| NotebookRead removed | GitHub #9440 | Read tool gives raw JSON; limit notebook size |
| Large notebooks overflow context | GitHub #9440 | Keep notebooks under ~50 cells; use separate notebooks per chart |

### Alternative: marimo Notebooks

For fully headless/CI environments, consider [marimo](https://marimo.io/) notebooks which store as `.py` files — editable with standard Edit tool, no JSON corruption risk, and execute as Python scripts.

## Files to Create

```
templates/
  cost_curve_analysis.ipynb      (with human-readable cell IDs)
  adoption_scurve.ipynb
  pipeline_summary.ipynb
scripts/
  stdf_plots.py                  (primary static chart generator)
```

## Files to Modify

```
.claude/agents/stdf-cost-curve.md      — add chart generation step + NotebookEdit rules
.claude/agents/stdf-adoption-scurve.md — add chart generation step + NotebookEdit rules
.claude/agents/stdf-synthesizer.md     — add summary chart generation + NotebookEdit rules
CLAUDE.md                              — update output directory structure
```

## Dependencies

- `matplotlib`, `numpy`, `scipy` — required for static charts (primary)
- `jupyter`, `nbconvert` — optional for notebook execution
- `NotebookEdit` tool already listed in agent tool sets
- Templates must be created with valid .ipynb JSON and human-readable cell IDs
