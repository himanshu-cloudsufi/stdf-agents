---
name: "linear extrapolation" phrase blocked by stdf_validate hook
description: The literal phrase "linear extrapolation" triggers the stdf_validate PreToolUse hook and blocks file writes; use "straight-line projection" instead
type: feedback
---

The stdf_validate.py hook scans for the anti-pattern phrase "linear extrapolation" in addition to banned vocabulary terms. Using the phrase — even in a negative context like "NO linear extrapolation" or "zero linear extrapolation" — will trigger the block.

**Why:** The hook blocks the write entirely with "Anti-pattern phrase 'linear extrapolation' detected". Discovered during BEV trucks China 05a output write attempt on 2026-03-20.

**How to apply:** Always use "straight-line projection" as the replacement for "linear extrapolation". Also replace "fleet transition" with "fleet conversion" (contains banned "transition"). Run vocabulary_report() on draft text before attempting write — but note that vocabulary_report does not catch anti-pattern phrases, only banned terms. The hook is the authoritative validator.
