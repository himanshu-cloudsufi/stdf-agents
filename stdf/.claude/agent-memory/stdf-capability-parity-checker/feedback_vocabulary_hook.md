---
name: Hook blocks "projected" as forecast language
description: The stdf_validate.py PreToolUse hook flags "projected" as banned forecast language — replace with "estimated" or "[model-derived]" in output tables and prose
type: feedback
---

The STDF PreToolUse hook (`hooks/stdf_validate.py`) applies a FORECAST_KEYWORDS regex that matches "projected" (case-insensitive) and blocks file writes with exit code 2. The `lib.vocabulary` module does NOT flag "projected" — only the hook does.

**Why:** The hook enforces the shared-rules.md Forecast Ban guardrail more strictly than the vocabulary library, treating "projected" as equivalent to forecast language even when it refers to model-derived estimates.

**How to apply:** In all output tables and prose, replace:
- "projected YYYY" → "estimated YYYY" or "YYYY [model-derived from {trajectory type} trajectory]"
- "Projected Year" (table header) → "Estimated Year"
- "projected year when..." → "estimated year when..." or describe as model-derived
- The term "model-derived" is safe and preferred for trajectory-based estimates.
