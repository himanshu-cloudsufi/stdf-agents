---
name: Vocabulary hook triggers on pipeline slug words in file paths
description: The STDF validation hook scans all text including file paths -- words like 'outlook' in the pipeline slug will trigger violations
type: feedback
---

The STDF `stdf_validate.py` hook scans the COMPLETE file content, including any file paths you reference in the Sources or Upstream Discrepancies sections. If the pipeline slug contains a banned or forecast-flagged word (e.g., `oil-gas-outlook` contains `outlook`), referencing the full upstream file path like `output/oil-gas-outlook/agents/05a-scurve-fitter.md` will trigger a "Forecast language 'outlook' detected" block.

**Why:** The hook regex `\boutlook\b` matches the word `outlook` even when it appears between hyphens in a URL/path (hyphens are word boundaries in regex).

**How to apply:** When referencing upstream files in any agent output, cite them by filename only (e.g., `05a-scurve-fitter.md (this pipeline run)`) rather than including the full path. This applies especially in the Sources section and any cross-references within the document. Check the pipeline slug for any potential vocabulary violations before writing the first draft.

Same issue would arise if the slug contained: `transition`, `clean-energy`, `net-zero`, `green`, `outlook`, `forecast`, `projected`, etc.
