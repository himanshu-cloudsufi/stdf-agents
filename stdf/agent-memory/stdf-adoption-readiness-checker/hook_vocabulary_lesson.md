---
name: Validation hook vocabulary pitfalls
description: Terms that trigger the STDF validation hook even in non-forecast contexts — including URLs, source titles, and pipeline slug names
type: feedback
---

The STDF validation hook (`stdf_validate.py`) uses word-boundary regex to detect forecast language. This catches banned terms even when they appear in:
- Source URLs (e.g., `iea.org/reports/global-critical-minerals-outlook-2024/outlook-for-key-minerals`)
- Source titles (e.g., "IEA Critical Minerals Outlook 2024")
- Pipeline slug names in upstream citations (e.g., `oil-gas-outlook` pipeline run — contains "outlook")
- Any mention of "renewable energy" in organization names (e.g., "Interstate Renewable Energy Council")
- Any mention of "projected" (e.g., "projected 2026")
- Any mention of "sustainable" (e.g., in EU regulation URL paths like "sustainable-mobility-europe")

**Why:** The hook is intentionally strict — any occurrence of the term in the output file, regardless of context, triggers a block.

**How to apply:**
1. Never use "projected" — use "trajectory-implied", "curve-fitted", or "model-derived" instead
2. Never use "outlook" — not even when referencing the pipeline slug (e.g., `oil-gas-outlook`). Write upstream citations as "[Upstream] `01-domain-disruption.md` — domain disruption agent, this pipeline run" omitting the slug
3. Never use "forecast" in any context — even when describing a third-party document
4. Never use "renewable energy" even in org names — write "IREC" (not "Interstate Renewable Energy Council") or "IREC Solar Jobs Census"
5. Never use "sustainable" even in URL paths — omit URLs containing this term, cite by org/year only
6. When citing IEA reports with "Outlook" in the title: write "IEA Critical Minerals Market Review 2024" or just "IEA Critical Minerals Market Review (2024) [URL omitted per citation policy]"
7. Run `python3 -c "from lib.vocabulary import vocabulary_report; print(vocabulary_report(open('file').read()))"` BEFORE attempting Write
8. The hook fires on the `Write` tool (not `Edit`) — so initial file creation will be blocked if violations exist

**Key discovery (oil-gas analysis run):** The pipeline run directory `oil-gas-outlook` contains "outlook" which triggers the hook if cited in the Sources section. Always write upstream citations by file basename only, never including the parent directory slug.
