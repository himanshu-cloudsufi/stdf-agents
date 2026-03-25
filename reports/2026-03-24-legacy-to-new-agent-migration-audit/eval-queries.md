# STDF v2 Pipeline Eval Queries — Legacy Comparison Set

**Date:** 2026-03-25
**Purpose:** 25 queries from legacy chat exports to run through the new `/stdf` pipeline and compare against legacy outputs. Ranked by eval value.

---

## Tier 1: High-Impact (legacy failed badly or crashed)

| # | Query | User | Legacy File | Legacy Outcome | v2 Preset | Why Run This |
|---|---|---|---|---|---|---|
| 1 | "Consider all the cost curves in our database, what are the top four likely areas of credit stress in the next four years" | Tony | `tony/2026-03-11_11-15-07_cc05df.md` | **CRASHED** — 10 messages, 8 empty, zero output | FULL (x4 parallel) | Legacy completely died. Multi-disruption meta-query — hardest possible test |
| 2 | "When will lead supply exceed demand by 10%?" | Tony | `tony/2026-03-17_17-11-05_8c607a.md` | Latest attempt, outcome unknown | FULL+COMMODITY | 5th attempt at this query across dates. Run with exact wording for clean comparison |
| 3 | "When will BEV trucks disrupt natural gas trucks in China?" | Tony | `tony/2026-01-16_00-34-48_f6c8aa.md` | Legacy skill-based | FULL | Tests commodity-specific disruption with regional focus |
| 4 | "When do you think oil markets will have a 3 million barrel excess supply surplus?" | Tony | `tony/2026-01-05_17-30-02_1da057.md` | Script crashed (`KeyError`), partial output | FULL+COMMODITY | Legacy crashed mid-analysis; tests oil demand decomposition |
| 5 | "What is the total market of LNG by 2032?" | Tony | `tony/2026-03-02_11-24-19_52566b.md` | Unknown | ENERGY_GAS | Tests energy dispatch + gas supply decomposer chain |

## Tier 2: Core Disruption Queries (tests framework compliance)

| # | Query | User | Legacy File | Legacy Outcome | v2 Preset | Why Run This |
|---|---|---|---|---|---|---|
| 6 | "What are the demand drivers for copper?" | Tony | `tony/2026-01-26_01-36-12_7e841a.md` | Unknown | FULL+COMMODITY | Commodity demand decomposition — tests the full demand chain |
| 7 | "What will be the copper demand by 2030? Give me YoY timeline" | Jagannath | `jagannath/2026-01-28_16-30-06_28a6df.md` | Unknown | FULL+COMMODITY | Same commodity, different framing — tests demand-decomposer + stream-forecaster |
| 8 | "When will natural gas demand peak in Germany? Which will generate peak gas demand?" | Jagannath | `jagannath/2025-12-17_08-09-48_44de1f.md` | Multiple retries (5+ sessions) | ENERGY_FULL | Tests energy dispatch for specific region. Legacy tried this many times |
| 9 | "How should I think about demand for fuel cells in America going forward?" | Robert | `rgibbins/2025-12-18_22-10-29_1deed3.md` | Unknown | FULL | Tests whether pipeline correctly identifies fuel cells as chimera |
| 10 | "What is the humanoid robot cost curve over the next 20 years?" | Tony | `tony/2026-02-18_08-06-42_cf0ee7.md` | Unknown | COST_FOCUS | Tests cost-researcher + cost-fitter on emerging technology with thin data |
| 11 | "When will drones disrupt tanks?" | Jitin/Jagannath | `jitin/2025-12-15_12-27-38_57a8d5.md` | Multiple attempts | FULL | Military disruption — tests domain-disruption on non-energy sector |
| 12 | "What will be the lithium-ion demand in the next few years globally?" | Jagannath | `jagannath/2026-02-16_17-56-20_8ce9a4.md` | Multiple retries (8+ sessions) | FULL+COMMODITY | Most-retried commodity query — clear legacy pain point |

## Tier 3: Energy and Power (tests dispatch chain)

| # | Query | User | Legacy File | Legacy Outcome | v2 Preset | Why Run This |
|---|---|---|---|---|---|---|
| 13 | "What is the existing battery and solar install capacity in the USA?" | Robert | `rgibbins/2025-12-18_20-03-56_6fdf4f.md` | Unknown | COST_FOCUS | Tests data catalog retrieval for US energy capacity |
| 14 | "How should I think about the US 'energy dominance' policy?" | Robert | `rgibbins/2025-12-19_18-48-10_8ed8bb.md` | Unknown | ENERGY_FULL | Energy policy through disruption lens — tests SWB framing |
| 15 | "What is the consequence of the first 100, 300 and 500 GW of solar deployment?" | Robert | `rgibbins/2025-12-20_12-15-26_8280eb.md` | Unknown | ENERGY_FULL | Capacity threshold analysis — tests energy dispatch modeling |
| 16 | "How will SWB impact the LNG market by 2030-2032?" | Robert | `rgibbins/2026-02-28_16-42-45_ad6e0a.md` | Unknown | ENERGY_GAS | Direct test of energy-dispatch + gas-supply-decomposer |
| 17 | "What is the UK annual power generation in TWh since 2000?" | Tony | `tony/2026-02-17_21-08-42_772f40.md` | Unknown | QUICK | Data retrieval test — verifies catalog access |

## Tier 4: Labor and Macro (tests framework boundaries)

| # | Query | User | Legacy File | Legacy Outcome | v2 Preset | Why Run This |
|---|---|---|---|---|---|---|
| 18 | "Let's look at the artificial labor disruption of human labor" | Tony | `tony/2026-01-18_19-34-07_ce64c5.md` | Unknown | FULL | AI labor disruption — tests whether pipeline can handle non-energy disruptions |
| 19 | "When will 50% of customer service jobs be displaced?" | Jagannath | `jagannath/2025-12-16_09-19-33_65b26b.md` | Unknown | ADOPTION_FOCUS | AI labor S-curve — tests scurve-fitter on labor data |
| 20 | "When will AI be able to automate more than 50% of the tasks performed by software engineers?" | Jagannath | `jagannath/2025-12-16_08-10-05_6c1a89.md` | Unknown | FULL | AI capability assessment for specific occupation |
| 21 | "Is AI a deflationary shock or not and why?" | Robert | `rgibbins/2026-03-05_20-42-27_a0a6c7.md` | Unknown | FULL | Macro-disruption framing through STDF lens |

## Tier 5: Edge Cases and Stress Tests

| # | Query | User | Legacy File | Legacy Outcome | v2 Preset | Why Run This |
|---|---|---|---|---|---|---|
| 22 | "When would you short Bloom Energy?" | Tony | `tony/2026-01-08_23-42-47_e75276.md` | Unknown | FULL | Investment thesis from disruption — tests chimera identification (fuel cells) |
| 23 | "Oklo: should I be long short or indifferent. Run a full process" | Robert | `rgibbins/2026-01-21_15-38-02_161ae6.md` | Unknown | FULL | Nuclear as chimera — tests domain-disruption's ability to classify |
| 24 | "What is the impact of electrification of cars on coal demand?" | Jitin | `jitin/2025-12-15_22-13-16_95f9f0.md` | Unknown | FULL+COMMODITY | Cross-sector cascade: EVs → electricity → coal displacement |
| 25 | "When might Russia suffer a catastrophic economic issue due to technology disruption?" | Jagannath | `jagannath/2026-02-10_11-58-31_53599f.md` | Unknown | FULL | Geopolitical + commodity stress — tests xcurve-analyst market trauma |

---

## Execution Priority

**Batch 1 (run first — highest eval value):**
- #1 Credit stress (crashed)
- #4 Oil 3M barrel surplus (crashed)
- #8 Germany gas peak (5+ retries)
- #12 Lithium demand (8+ retries)

**Batch 2 (core disruptions):**
- #2 Lead surplus (5th attempt)
- #3 BEV trucks China
- #6 Copper demand drivers
- #10 Humanoid robot cost curve
- #11 Drones vs tanks

**Batch 3 (energy chain):**
- #5 LNG market 2032
- #13 US battery/solar capacity
- #15 Solar deployment thresholds
- #16 SWB vs LNG

**Batch 4 (labor/macro):**
- #18 AI labor disruption
- #19 Customer service displacement
- #21 AI deflationary shock

**Batch 5 (edge cases):**
- #22 Short Bloom Energy
- #23 Oklo long/short
- #24 EVs → coal impact
- #25 Russia economic risk

---

## Scoring Criteria for Each Run

For each query, compare legacy vs. v2 on:

| Criterion | Weight | How to Score |
|---|---|---|
| **First-pass accuracy** | 25% | Did v2 answer correctly without correction rounds? |
| **Framework compliance** | 20% | No TCO, no "transition", no mainstream sources, S-curves used |
| **Data provenance** | 15% | All numbers tagged [T1/T2/T3/model-derived]? |
| **Demand decomposition** | 15% | Market products identified, material intensity computed? |
| **Regional analysis** | 10% | Per-region breakdown with S-curve parameters? |
| **Robustness** | 10% | Did it complete without crashes? Degradation documented? |
| **Answer precision** | 5% | Single estimate with confidence interval, not scenarios? |
