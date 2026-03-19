---
name: stdf-validate
description: Validates STDF agent output files against compliance guardrails including banned vocabulary, banned sources, forecast language violations, anti-patterns, date consistency, and citation provenance. Works on individual files or entire output directories. Triggers on 'validate', 'check output', 'scan for issues', 'guardrail check', or '/stdf-validate'.
---

# STDF Guardrail Validator

Validates STDF agent output files against the compliance guardrails: banned vocabulary, banned sources, forecast language, anti-patterns, date consistency, and citation provenance.

## Usage

The argument should be a path to either:
- A single agent output file: `/stdf-validate output/energy-storage/agents/02b-cost-fitter.md`
- An entire output directory: `/stdf-validate output/energy-storage/`
- No argument: validate the most recent output directory

## Execution

### If a directory path is given (or no argument):

Resolve the target directory. If no argument, find the most recent:
```bash
ls -td output/*/ 2>/dev/null | head -1
```

Then run the full pipeline validation:
```bash
python3 .claude/skills/stdf-validate/scripts/validate_pipeline.py "<resolved-path>"
```

To override the analysis date (e.g., for a past run):
```bash
python3 .claude/skills/stdf-validate/scripts/validate_pipeline.py --date 2026-03-01 "<resolved-path>"
```

### If a single file path is given:

```bash
python3 .claude/skills/stdf-validate/scripts/validate_pipeline.py "<file-path>"
```

## Gotchas

- **Empty output files pass validation** — check file sizes first. An agent that creates a file but writes nothing won't trigger any violations.
- **Date parameter should match the pipeline's analysis date**, not necessarily today's date. If validating a past run, use `--date`.

## Presenting Results

After running validation:
1. Show the results table
2. If there are critical violations, list each one with the specific term/pattern and its replacement
3. If there are warnings, summarize them grouped by type
4. Suggest fixes for any violations found
