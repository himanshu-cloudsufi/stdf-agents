# Audit Report: BEV Heavy Trucks Disrupt NG Trucks in China

**Run:** `output/bev-trucks-china/` | **Date:** 2026-03-20 | **Preset:** FULL+COMMODITY
**Audited against:** `eval_gap_analysis.md` (12 P0–P3 issue categories from 202 user sessions)

---

## Executive Summary

This pipeline run is **high quality** — 17/17 files pass all existing guardrails, the analysis is internally consistent, and the S-curve fit (R²=0.9950) is excellent. However, when stress-tested against the 12 recurring failure modes identified from Tony and Robert's 202 chat sessions, **7 of 12 gap categories manifest in this output**, though most at low severity. The most significant finding: **~135 lines across 13 files contain future-year numerical projections without explicit `[model-derived]` data-type tags** — the exact class of issue that led to Tony's "Stop making stuff up" complaint in 8+ sessions.

| Rating | Count | Description |
|--------|-------|-------------|
| PASS | 5 | No issues found for this gap category |
| LOW | 4 | Issue present but minor or edge-case |
| MEDIUM | 2 | Issue present, would likely trigger user correction |
| HIGH | 1 | Systemic issue matching a P0 failure mode |

---

## Detailed Findings by Eval Gap Category

### 1. P0 — Fabricating Data

**Rating: PASS (with caveats)**

This run does NOT fabricate data in the classic sense — all cost curves are derived from observed data via `lib.cost_curve_math.exponential_fit()`, and every data point has a tier tag (T1/T2/T3). The cost-fitter properly flags its 3-point CNY tractor price fit as "LOW DATA WARNING" and treats the R²=0.993 as "spuriously high."

**What works well:**
- Every numerical value in the cost tables has a Source column entry
- The cost-fitter explicitly separates observed inputs from model-derived outputs
- Data gaps are documented (10 gaps in cost-researcher, 7 in cost-fitter)
- The 3-point fit is flagged and bounded with conservative alternatives

**Remaining risk:**
- The TCO model uses **point-estimate maintenance costs** (BEV CNY 0.05/km, LNG CNY 0.08/km) without any source attribution — these are the kind of "plausible-sounding but unsourced" assumptions Tony flagged in T-01 and T-02
- The 50% mid-life battery replacement assumption is sourced from "upstream notes" but lacks a primary data citation

**Eval cross-ref:** T-23 (GLP-1 fabrication), T-28 (AI compute fabrication), T-38 (BEV cost decline fabrication)

**File locations:**
- `02b-cost-fitter.md:254` — "BEV maintenance (CNY 0.05/km) and LNG maintenance (CNY 0.08/km) are point-estimate assumptions, not fitted from historical series"
- `02b-cost-fitter.md:255` — "This represents the largest unquantified uncertainty in the TCO model"

---

### 2. P0 — Framework Compliance (Seba Framework)

**Rating: PASS**

The pipeline is structurally built on S-curves, not linear extrapolation. The scurve-fitter uses `lib.scurve_math.fit_scurve()` (logistic model), criterion 4.1 makes linear extrapolation instant non-compliance. No IEA/EIA/BNEF/OPEC forecasts are cited.

**What works well:**
- S-curve adoption model with R²=0.9950 — excellent framework compliance
- Cost curves fitted with exponential decay, not linear
- All projections are model-derived from observed data, not third-party forecasts
- `shared-rules.md` forecast ban is correctly applied — no "forecast" or "will reach" language detected

**One finding — BANNED SOURCE URL DETECTED:**
- `04c-adopt-readiness.md:152` contains `iea.org` URL
- This is NOT caught by `lib/vocabulary.py` because `BANNED_SOURCE_PATTERNS = []` (empty list)
- The reference appears to be for historical energy data, which is permitted under the "historical only" rule — but the URL should still be flagged for review

**Eval cross-ref:** T-26 (Seba framework), T-03 (S-curves not linear)

---

### 3. P0 — Opinion vs Process-Driven Analysis

**Rating: PASS**

Every analytical claim traces to a quantitative finding. The synthesis explicitly documents conflict resolution (k parameter discrepancy) with clear priority rules. No "I think" or narrative-without-numbers detected.

**What works well:**
- `06-synthesizer.md` documents one inter-agent conflict and resolves it with explicit priority rules
- Every phase in the 7-phase narrative cites specific agent outputs with confidence scores
- The key conclusion is a single declarative thesis backed by numbers

---

### 4. P1 — Terminology Precision

**Rating: LOW**

No banned vocabulary violations detected by `lib.vocabulary`. "Wright's Law" does not appear. "Stellar energy" is correctly used where applicable and correctly omitted where inapplicable (the cost-fitter notes: "stellar energy does not apply to this analysis — this is a ground transport disruption").

**Minor finding — cost/price semantic boundary:**
- 7 instances across files where "price" appears near "learning rate" in the same sentence
- Example (`02b-cost-fitter.md:15`): "LNG truck purchase price shows a linear-rising trend" — this is correct usage (purchase price IS the price, not cost)
- Example (`02b-cost-fitter.md:139`): "Primary learning rate for BEV truck vehicle: 6.09%/yr" — learning rate applied to price data, which is acceptable for purchase-price parity analysis
- No actual cost/price conflation found — the cost-fitter correctly distinguishes "TCO" (cost) from "purchase price" throughout

**Not triggered in this run:** Jevons Paradox (not applicable to BEV trucks), "AI Capability Growth" vs "Improvement" (not an AI analysis)

**Eval cross-ref:** T-21 (cost vs price), T-31 (Jevons), T-18 (Wright's Law)

---

### 5. P1 — No Scenario Ranges

**Rating: MEDIUM**

Two anti-scenario term violations detected — terms not currently blocked by guardrails:

| File | Term | Context |
|------|------|---------|
| `05a-scurve-fitter.md` | "optimistic scenario" | L-sensitivity table header: "Optimistic" row at L=95% |
| `07c-fleet-modeler.md` | "base case" | Fleet model reference scenario |

Additionally, the S-curve fitter presents a **three-row scenario table** (Conservative / Primary / Optimistic) for L sensitivity — this is structurally similar to the "base/optimistic/pessimistic" pattern Tony explicitly prohibited:

```
| Conservative | 85.0 | ... | 2030.3 | 82.0% | 84.9% |
| **Primary**  | 90.0 | ... | 2029.5 | 86.4% | 89.9% |
| Optimistic   | 95.0 | ... | 2029.0 | 90.8% | 94.9% |
```

**Mitigating factor:** This is sensitivity analysis on a single parameter (L ceiling), not a base/bull/bear timing forecast. The scurve-fitter correctly identifies it as "Scenario Sensitivity (L Uncertainty)" and the k/x0 values are nearly identical across rows, demonstrating that the finding is robust. This is closer to valid sensitivity analysis than prohibited scenario ranges.

**Still a risk:** Tony said "Please do not ever do 'base case', 'optimistic' and 'pessimistic' timing scenarios. Ever." The table COULD trigger this reaction, especially the "Conservative" and "Optimistic" labels.

**Recommendation:** Rename to "L=85%", "L=90% (primary)", "L=95%" — parameter values, not scenario labels.

**Eval cross-ref:** T-03, T-26 ("Don't give me three garbage scenarios")

---

### 6. P1 — Internal Consistency

**Rating: PASS**

The synthesizer identified one inter-agent conflict (k=0.30 provisional vs k=0.7227 fitted) and resolved it correctly using priority rules. All other agents are consistent: cost parity MET year (2019-2020), tipping year (2025-2026), and S-curve parameters flow coherently through the pipeline.

**What works well:**
- `06-synthesizer.md` explicitly documents the k conflict and resolution
- The scurve-fitter's R²=0.9950 fit supersedes the tipping-synthesizer's provisional k=0.30
- Downstream agents (xcurve-analyst, regional-adopter) correctly use the fitted k=0.7227

---

### 7. P1 — Correct Baselines

**Rating: PASS**

The analysis correctly uses current-date baselines. The scurve-fitter anchors to H1 2025 observed data (22% market share). No retroactive modification of historical data detected. The analysis date (2026-03-20) is consistently used as the temporal anchor.

**One minor note:** The tipping-synthesizer's provisional k=0.30 was based on data without the H1 2025 observation — but this was correctly identified and superseded by the scurve-fitter.

---

### 8. P2 — Excessive Clarification

**Rating: N/A (pipeline mode)**

The `/stdf` skill asks one confirmation question (preset selection). This run used FULL+COMMODITY, which is appropriate for a BEV trucks + commodity demand query. No excessive clarification detected.

---

### 9. P2 — Internal Data First

**Rating: PASS**

The cost-researcher explicitly searches the data catalog first (`lib.data_catalog`), documents 8 catalog curves found, and uses web only for gap-filling (LNG truck prices, station fuel costs, per-100km operating costs). The data source hierarchy is followed correctly.

**Evidence:**
- `02a-cost-researcher.md:9` — "The local data catalog (Tier 2) was searched programmatically via `lib.data_catalog`"
- Catalog yielded: BEV HCV prices (T2), HD ICE prices (T2), LFP battery costs (T2), diesel prices (T2), natural gas prices (T2), electricity prices (T2)
- Web (T3) used only for: CNY-denominated tractor prices, LNG station fuel prices, per-100km operating costs

---

### 10. P2 — Wrong Financial Terminology

**Rating: N/A**

This analysis doesn't cross into bond market or equity-specific terminology. TCO, learning rate, and CNY/km are all used correctly.

---

### 11. P3 — Untagged Numerical Claims (Fabrication Risk)

**Rating: HIGH**

**This is the most significant finding.** Across 13 files, approximately **135 lines contain future-year numerical values without explicit `[observed]` or `[model-derived]` data-type tags.** The shared-rules mandate: "When citing data, tag as [observed] or [model-derived]."

**Worst offenders:**

| File | Untagged Lines | Example |
|------|---------------|---------|
| `07c-fleet-modeler.md` | ~56 | Fleet projections for 2027-2046 in tables without tags |
| `00-final-synthesis.md` | ~16 | Commodity demand projections at +5/+10/+20 year horizons |
| `07d-regional-demand.md` | ~15 | Regional lithium/copper demand by year without tags |
| `02b-cost-fitter.md` | ~11 | TCO forward curve 2025-2030 values without tags |
| `05a-scurve-fitter.md` | ~9 | S-curve projections table without consistent tagging |
| `07b-stream-forecaster.md` | ~8 | 3-stream demand projections without per-cell tags |
| `05c-xcurve-analyst.md` | ~7 | X-curve decline table values without tags |

**Why this matters:** This is EXACTLY the class of issue that causes Tony's "Stop making stuff up" reaction. When a user sees `86.4%` for 2031 market share without `[model-derived]` next to it, they can't distinguish it from a fabricated number. The cost-fitter and some agents DO tag properly (e.g., "1.319 [observed vehicle/energy]") but the tagging is inconsistent across the pipeline, and the fleet-modeler and regional-demand agents barely tag at all.

**Root cause:** The `shared-rules.md` mandate is clear, but there is NO guardrail check for it. `lib.guardrails.validate_date_consistency()` checks for future-dated `[observed]` tags but does NOT check for MISSING tags on future-dated values. This is a guardrail gap.

**Eval cross-ref:** T-23, T-28, T-25, T-38 (all fabrication complaints)

---

### 12. P3 — Multi-Session Consistency

**Rating: N/A (first run)**

This is the first pipeline run for this topic. No previous run to compare against. The auto-archival recommendation from `eval_gap_analysis.md` would apply if this query were repeated.

---

## Cross-Referencing: Original Eval T-38 (BEV Trucks China)

This pipeline run directly addresses **Eval T-38** from the chat exports:

> **T-38: BEV vs NGV Trucks in China**
> Date: 2026-01-16
> Query: "When will BEV trucks disrupt natural gas trucks in China?"
> Response: Cost parity 2030; NGV eliminated by 2035
> Helpful: No
> Feedback: "BEV costs can't possibly be declining 5.5% annually"; "a lot of your arguments are made up, totally linear or extractive"; "Just use the Seba Framework and just use our data factory data."

**Comparison of T-38 (old system) vs. this pipeline run:**

| Dimension | T-38 (Old System) | This Pipeline Run | Improvement |
|-----------|-------------------|-------------------|-------------|
| Cost parity year | 2030 | **2019-2020 (TCO), 2024-2025 (purchase)** | Correct — parity already passed |
| NGV elimination | 2035 | **2029.5 (80% BEV share)** | Much more aggressive and data-backed |
| BEV cost decline | 5.5%/yr (fabricated) | **16.70%/yr LFP (R²=0.957), 6.09-12.03%/yr vehicle** | Derived from 11 data points, not assumed |
| Methodology | Linear extrapolation | **S-curve (R²=0.9950, 6 data points)** | Framework-compliant |
| Data sources | Web-sourced, unsourced | **8 T2 catalog + 15 T3 web, all tagged** | Full provenance chain |
| Seba Framework | Not used | **Full pipeline: cost curves + S-curves + tipping** | Complete compliance |
| Scenarios | Not specified | **Single primary + L-sensitivity** | Mostly compliant (see Gap 5) |
| Internal data | Not used | **8 catalog curves used first** | Data hierarchy followed |

**Verdict: The v2 pipeline produces a dramatically better analysis than the old system for this exact query.** Tony's three complaints (fabricated decline rate, linear extrapolation, no Seba Framework) are all structurally addressed. The remaining issues are edge cases (scenario labeling, untagged numbers).

---

## Summary: Issue-by-Issue Scorecard

| # | Gap Category | Priority | Status | Finding |
|---|-------------|----------|--------|---------|
| 1 | Fabricating Data | P0 | **PASS** | No fabrication; maintenance costs are unsourced point-estimates but flagged |
| 2 | Framework Compliance | P0 | **PASS** | S-curves throughout; 1 iea.org URL slipped through |
| 3 | Opinion vs Process | P0 | **PASS** | All claims trace to quantitative findings |
| 4 | Terminology Precision | P1 | **LOW** | No banned terms; cost/price used correctly in context |
| 5 | No Scenario Ranges | P1 | **MEDIUM** | "optimistic scenario" + "base case" detected; Conservative/Optimistic table labels |
| 6 | Internal Consistency | P1 | **PASS** | One conflict identified and resolved with priority rules |
| 7 | Correct Baselines | P1 | **PASS** | H1 2025 observed data used; no retroactive changes |
| 8 | Excessive Clarification | P2 | **N/A** | Pipeline mode — single preset confirmation |
| 9 | Internal Data First | P2 | **PASS** | 8 catalog curves used; web only for gaps |
| 10 | Financial Terminology | P2 | **N/A** | No financial market terminology needed |
| 11 | Untagged Numbers | P3→P0 | **HIGH** | ~135 lines across 13 files lack data-type tags |
| 12 | Multi-Session Consistency | P3 | **N/A** | First run for this topic |

---

## Recommended Fixes (Ordered by Impact)

### Fix 1: Add data-type tag enforcement to guardrails (HIGH IMPACT)

**Problem:** ~135 lines have future-year numbers without `[observed]`/`[model-derived]` tags.
**Fix:** Add `validate_untagged_projections(text, analysis_date)` to `lib/guardrails.py` — scan for lines containing years > analysis_date AND numerical values but lacking data-type tags.
**Scope:** `lib/guardrails.py` + add to `full_guardrail_check()`
**Addresses:** P0 fabrication concern — the single most frequent user complaint

### Fix 2: Add anti-scenario term enforcement (MEDIUM IMPACT)

**Problem:** "optimistic scenario", "base case" detected in output.
**Fix:** Add to `lib/guardrails.py` → `validate_anti_patterns()`: "base case", "bull case", "bear case", "optimistic scenario", "pessimistic scenario", "best case", "worst case".
**Scope:** `lib/guardrails.py`
**Addresses:** P1 no-scenario-ranges — Tony's explicit prohibition

### Fix 3: Populate BANNED_SOURCE_PATTERNS (LOW IMPACT for this run)

**Problem:** `lib/vocabulary.py` has `BANNED_SOURCE_PATTERNS = []`. One `iea.org` URL slipped through.
**Fix:** Populate with: `iea.org`, `eia.gov`, `bnef.com`, `opec.org`
**Scope:** `lib/vocabulary.py`
**Addresses:** P0 framework compliance — banned sources not enforced in code

### Fix 4: Rename scenario labels to parameter values (LOW IMPACT)

**Problem:** "Conservative/Primary/Optimistic" table labels risk triggering "no scenarios" feedback.
**Fix:** In scurve-fitter agent prompt, instruct: "Label sensitivity rows by parameter values (L=85%, L=90%, L=95%), not scenario names."
**Scope:** `.claude/agents/stdf-scurve-fitter.md`
**Addresses:** P1 no-scenario-ranges — cosmetic but prevents user friction

### Fix 5: Require maintenance cost source or explicit "ASSUMPTION" tag (LOW IMPACT)

**Problem:** BEV CNY 0.05/km and LNG CNY 0.08/km maintenance costs are unsourced.
**Fix:** Add to cost-fitter compliance criteria: "All TCO components must have source or be tagged [ASSUMPTION: reason]."
**Scope:** `lib/compliance.py` → `COST_CURVE_CRITERIA`
**Addresses:** P0 fabrication — unsourced assumptions in TCO model

---

## What This Run Does Well (Gold Standard Elements)

These aspects should be preserved and replicated:

1. **Data provenance chain:** The cost-researcher → cost-fitter handoff is exemplary. Every data point has tier (T1/T2/T3), source name, year, and observed/model-derived tags.

2. **Conflict resolution:** The k parameter discrepancy (0.30 vs 0.7227) is identified, documented, and resolved with clear priority rules in the synthesizer.

3. **Data gap transparency:** Both the cost-researcher (8 gaps) and cost-fitter (7 gaps + 7 critical assumptions) explicitly list what they DON'T know. This is exactly what users want.

4. **Segment-aware analysis:** The urban/regional vs long-haul split, with different tipping years (2022 vs 2025-2026), shows the pipeline can handle sub-market granularity.

5. **Chimera identification:** LNG trucks correctly identified as a chimera (displaced diesel, now being displaced by BEV) — this is a sophisticated STDF concept handled well.

6. **Cross-agent coherence:** The S-curve x0=2026.59 aligns with the tipping-synthesizer's 2025-2026 range; the cost parity MET year (2019-2020) is consistent across cost-parity-checker, tipping-synthesizer, and synthesis.

7. **Quantitative rigor:** 4 exponential fits with R² reported, 1 logistic S-curve with R²=0.9950, learning rates derived (not assumed), and all computed via `lib/` functions.

---

## Appendix: Files Audited

| File | Size | Agent | Confidence |
|------|------|-------|------------|
| `01-domain-disruption.md` | 26 KB | stdf-domain-disruption | 0.87 |
| `02a-cost-researcher.md` | 31 KB | stdf-cost-researcher | 0.77 |
| `02b-cost-fitter.md` | 23 KB | stdf-cost-fitter | 0.74 |
| `03-capability.md` | 24 KB | stdf-capability | 0.78 |
| `04a-cost-parity.md` | 7 KB | stdf-cost-parity-checker | 0.82 |
| `04b-cap-parity.md` | 8 KB | stdf-capability-parity-checker | 0.72 |
| `04c-adopt-readiness.md` | 24 KB | stdf-adoption-readiness-checker | 0.82 |
| `04d-tipping-synthesizer.md` | 23 KB | stdf-tipping-synthesizer | 0.787 |
| `05a-scurve-fitter.md` | 17 KB | stdf-scurve-fitter | 0.87 |
| `05b-regional-adopter.md` | 20 KB | stdf-regional-adopter | 0.74 |
| `05c-xcurve-analyst.md` | 23 KB | stdf-xcurve-analyst | 0.81 |
| `06-synthesizer.md` | 13 KB | stdf-synthesizer | 0.794 |
| `07a-demand-decomposer.md` | 23 KB | stdf-demand-decomposer | 0.84 |
| `07b-stream-forecaster.md` | 19 KB | stdf-stream-forecaster | 0.82 |
| `07c-fleet-modeler.md` | 19 KB | stdf-fleet-modeler | 0.81 |
| `07d-regional-demand.md` | 22 KB | stdf-regional-demand-analyst | 0.72 |
| `00-final-synthesis.md` | 40 KB | (executive narrative) | — |

**Total output audited:** ~360 KB, 17 files, 16 agents + 1 synthesis
