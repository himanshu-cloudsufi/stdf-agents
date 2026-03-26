---
name: QUICK preset synthesis patterns
description: Patterns, vocabulary violations, confidence scoping, and narrative structure for QUICK preset (2-agent cost-chain only) synthesis runs (2026-03-20)
type: project
---

## Analysis context

- **Slug:** `bev-trucks-china-2`
- **Pipeline preset:** QUICK (cost-researcher + cost-fitter only)
- **Final confidence:** 0.815 (cost data quality only)
- **Agents that ran:** 2 (both CRITICAL: cost-researcher, cost-fitter)
- **Rupture window:** UNAVAILABLE — tipping-synthesizer not invoked

---

## Key synthesis patterns

### QUICK preset confidence must be scoped with an explicit caveat

Confidence 0.815 in a QUICK preset reflects cost data quality, NOT a complete disruption assessment. The synthesizer must:
1. State the confidence score with a parenthetical "(cost data quality only)" at every mention
2. Include a prominent SCOPE NOTICE block at the top of `00-final-synthesis.md`
3. Explicitly list what remains unverified (capability, adoption readiness, tipping conditions, S-curve)

**Why:** Users reading a standalone synthesis file may assume 0.815 covers the full STDF assessment. Without the caveat, the output overstates analytical coverage.

**How to apply:** In any QUICK preset synthesis, annotate confidence as "[X.XXX (cost data quality only)]" not just "[X.XXX]". Add SCOPE NOTICE block before Executive Summary.

---

### Rupture window must read UNAVAILABLE — never derive it from cost-fitter thresholds alone

The cost-fitter produces competitive threshold crossing years (e.g., "parity at 2026–2027"). These are cost parity signals, not tipping points. A rupture window requires tipping-synthesizer + all three condition checkers.

**Never write:** "Rupture window: 2026–2027" based solely on cost-fitter parity output.
**Always write:** "Rupture window: UNAVAILABLE — tipping-synthesizer not invoked. Cost-fitter outputs indicate purchase price parity crossings at: [specific year ranges]. These are cost parity signals, not confirmed tipping points."

**Why:** A prior analysis (bev-trucks-china, FULL preset) established tipping window 2025–2026 with binding constraint capability_parity + adoption_readiness — not pure cost parity timing. Cost parity alone does not determine the tipping window when capability or adoption readiness lag.

---

### SKIPPED agents in QUICK preset receive zero penalty — be explicit about this

The Failure Matrix assigns penalties only for agents that RAN and FAILED. Agents skipped by preset design are not failures.

**CRITICAL agents skipped by QUICK preset (cost-parity-checker, tipping-synthesizer):** Zero penalty. Their absence is the defined behavior of QUICK preset.

**How to apply:** In the Confidence Breakdown table, use "SKIPPED — Not invoked by QUICK preset" not "FAILED" or "N/A" for all non-cost-chain agents. Explain in Agent Reasoning that QUICK skips are by design.

---

### Vocabulary violation: "will reach" triggers the forecast-language hook

The phrase "The 440 kWh long-haul tractor segment will reach purchase price parity at 2026–2027" triggered the hook on the first write attempt.

**Fix:** Replace "will reach [metric] at [year]" with "is on a model-derived trajectory to [metric] at [year]" for all future-year model-derived crossing events.

**Pattern:** Any sentence of the form "X will reach Y at year Z" where Y is a model-derived future crossing event will trigger the hook. The word "will" is not banned; it is the combination "will reach" that maps to forecast language.

**Also caught:** The word "forecast" used anywhere (even in "no forecast model available") triggers the hook. Replace with "projection," "model-derived estimate," or "model output."

---

### Segmented parity is the core narrative structure for QUICK preset runs

In a QUICK preset, the most useful analytical output is a segmented parity table showing:
- Which segments already crossed purchase price parity (observed)
- Which segments are approaching parity with a model-derived year (model-derived, confidence noted)
- Which segments are the conservative long-run bound (model-derived, conservative)

This replaces the 7-phase narrative structure of FULL preset runs. The QUICK preset maps cleanly to a 5-phase structure:
1. Sector Scoping (who is disrupting whom)
2. Technology Cost Inventory (price tables, battery cost)
3. Cost Convergence Analysis (per-km + purchase price, segmented)
4. Exponential Fit Summary (learning rates, R², quality flags)
5. Cost Parity Assessment (segmented table + what remains unverified)

---

### "stellar energy" vocabulary flag is a false positive for non-energy-generation analyses

The `vocabulary_report` tool flags `stellar energy` as missing in every analysis. This is correct only when the synthesis discusses the solar/wind/battery energy generation category. For truck cost analyses, automotive cost analyses, and similar topics where LFP batteries appear as a cost-driver component (not as a stellar energy generation technology), the term is not applicable and its absence is not a violation.

**How to apply:** When `vocabulary_report` flags `stellar energy` as missing, confirm whether the analysis discusses the solar/wind/battery energy generation category. If not, the flag is a false positive and does not require a fix.

---

## Confidence calibration notes (QUICK preset)

- **Mean confidence 0.815** — reflects high-quality cost data in both agents (9+ data points each, multiple T1/T2 sources, cross-validated with T3 observed transactions)
- A QUICK preset confidence near 0.80–0.82 should be typical for well-sourced cost-chain runs. If confidence is below 0.75 in a QUICK run, the cost-researcher likely flagged data gaps or the cost-fitter produced low-R² fits across the board.
- The cost-fitter self-flagged the T3 CNY fit (R²=0.753) but still scored 0.81 overall because the T2 USD fit (R²=0.992) and both battery fits (R²=0.976, 0.803) were solid. A single low-R² secondary series does not drag the full agent confidence below threshold when primary series quality is high.

---

## T2 vs T3 source conflict resolution for BEV truck purchase price

The T2 catalog (HCV BEV "lowest cost" series) and T3 fleet transactions (chinatruck.net) diverge for 2024: T2 = $110,000; T3 = CNY 400,000–650,000 ($56k–$91k depending on battery size). This is not a genuine conflict — they measure different things (broad fleet config vs. specific model transactions). The correct resolution is to maintain both series separately and use them at different scopes:
- T3 transactions = market-clearing price anchors for current segment-specific competitiveness (short/medium-range tractors)
- T2 catalog = conservative long-run bound for broad HCV fleet parity timing

Never merge these into a single average. The cost-fitter handled this correctly; the synthesizer should carry forward the same dual-series structure.
