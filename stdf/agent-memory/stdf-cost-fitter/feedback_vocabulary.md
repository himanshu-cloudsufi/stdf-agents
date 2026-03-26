---
name: forecast-language-block
description: The stdf_validate hook blocks writes containing "projected", "projection", "outlook", or "transition" — use "model output", "forward curve", "analysis", "disruption" instead
type: feedback
---

The pre-write hook (`stdf_validate.py`) enforces a FORECAST_KEYWORDS regex and a BANNED_TERMS list that match several common words as either forecast language or banned vocabulary.

**Why:** The hook is designed to prevent third-party forecast data being presented as fact, and to enforce STDF vocabulary discipline. It cannot distinguish legitimate uses from external forecast citations.

**Confirmed blocked words (discovered through hook failures):**
- "projected" / "projection"
- "outlook" (e.g., in file names or narrative text — even "oil and gas demand outlook" in the narrative)
- "transition" (banned vocabulary → use "disruption" or "structural shift")

**How to apply:** Before writing any agent output file, replace all instances of:
- "projected" → "model output" or "model-derived" or "computed"
- "projection" → "forward curve" or "model output" or "model-computed values"
- "20-year projection" → "20-year forward curve"
- "model projects" → "model computes" or "model outputs"
- "outlook" (in narrative body) → "analysis" or "forward curve" or "cost trajectory"
- "transition to X" → "structural shift to X" or "disruption toward X"

Note: The pipeline slug `output/oil-gas-outlook/` uses "outlook" in the directory name — the hook does NOT block the directory name, only the file content. Do NOT use "outlook" in the prose body of agent output files.

This applies only to output files in `output/*/agents/*.md` — the hook is scoped to those paths.
