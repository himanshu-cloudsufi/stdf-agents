---
name: reference_liion_leadacid_batteries
description: Validated exponential fit parameters, learning rates, service-level conversion assumptions, and threshold years for Li-ion vs. lead-acid battery analysis (lead demand decline pipeline, 2026-03-20)
type: reference
---

## Li-Ion vs. Lead-Acid Battery Cost Analysis (2026-03-20)

Pipeline: `output/lead-demand-decline/` — Question: "When will demand for lead drop by 10%?"

### Li-Ion Global Median Pack Cost Exponential Fit

- **Formula:** C(t) = 1240.70 × exp(−0.1841 × (t − 2010))
- **C0:** 1240.70 $/kWh nameplate
- **r:** 0.1841 per year
- **R-squared:** 0.9541
- **Data points:** 15 annual (2010–2024)
- **Learning rate:** 16.81%/yr (per_year basis); 8.46%/doubling (time basis)
- **2024 validation deviation:** 18% (model: $94.3 vs actual: $115 — terminal segment slightly steeper than recent data due to 2022 spike recovery). Flag as low-confidence terminal segment.
- **2022 anomaly:** Li-ion cost spiked to $166/kWh in 2022 (lithium carbonate input cost spike). Retained in fit; excluding it worsens 2024 validation further.

### SLI Li-Ion China ($/battery unit, 60Ah 12V)

- **Formula:** C(t) = 857.97 × exp(−0.1608 × (t − 2010))
- **R-squared:** 0.9897 (8 data points, 2010–2024)
- **Learning rate:** 14.84%/yr

### Service-Level Conversion Parameters

**Li-ion (LFP stationary/deep-cycle):**
- Cycle life: 3,000 cycles
- DoD: 80%
- Round-trip efficiency: 96%
- Conversion factor: 1 / (3000 × 0.96 × 0.80) = 1/2304
- 2024 service-level cost: $0.0499/kWh delivered (from $115/kWh nameplate)

**Lead-acid (AGM/VRLA stationary):**
- Cycle life: 500 cycles
- DoD: 50%
- Round-trip efficiency: 75%
- Conversion factor: 1 / (500 × 0.75 × 0.50) = 1/187.5
- 2023 service-level cost USA: $0.96/kWh delivered (from $180/kWh nameplate)
- 2023 service-level cost China: $0.747/kWh delivered (from $140/kWh nameplate)

**SLI (automotive starter):** SLI is float/start-stop service, NOT cycle-limited. Do NOT apply levelized cost conversion to SLI. Use $/battery unit directly. 60Ah × 12V = 0.72 kWh for $/kWh equivalent reporting only.

### Key Insight: Levelized Parity Predates Dataset

Li-ion was already cheaper on a service-level ($/kWh delivered) basis in 2010 ($0.62/kWh_del) vs lead-acid USA ($1.60/kWh_del). The "2014 levelized parity" claim often cited in literature is incorrect for pack-level costs. NAMEPLATE parity occurred in 2019–2020 (USA) and 2020–2021 (China). The 24x service-level cost advantage (2024) means levelized disruption is complete; remaining lead-acid demand is driven by initial-cost sensitivity and SLI unit-price parity, not levelized economics.

### Threshold Years

| Comparison | Market | Parity Year | Type |
|------------|--------|------------|------|
| Nameplate $/kWh | USA | 2019–2020 | Competitive |
| Nameplate $/kWh | China | 2020–2021 | Competitive |
| Nameplate $/kWh | USA | 2021–2023 | Inflection (50–70% of incumbent) |
| Nameplate $/kWh | China | 2022–2025 | Inflection |
| SLI $/battery | USA ($55 target) | 2027–2028 | Competitive |
| SLI $/battery | China ($25 target) | 2031–2032 | Competitive |
| SLI $/battery | USA | 2029–2032 | Inflection |
| SLI $/battery | China | 2034–2037 | Inflection |
| Service-level | Both | Pre-2010 | Parity already reached |

### Lead-Acid Incumbent Trend

- Pack cost (catalog T2): nominally declining at −3.85%/yr (USA CAGR 2010–2023) and −4.36%/yr (China)
- BLS PPI T1 (USA producer prices): rising at +3.2%/yr nominal — authoritative signal of real-cost stagnation
- Structural drivers: mature learning curve (150+ years), lead commodity exposure (60–70% BOM), electrochemical energy density ceiling, stranded smelting/recycling infrastructure, regulatory burden under REACH/EPA

### Model-Derived Forward Costs (nameplate $/kWh, Li-ion global median)

| Year | Nameplate ($/kWh) | Service-Level ($/kWh_del) |
|------|------------------|--------------------------|
| 2025 | 78.4 | 0.0394 |
| 2026 | 65.3 | 0.0328 |
| 2028 | 45.2 | 0.0227 |
| 2030 | 31.2 | 0.0157 |

Note: 18% terminal deviation means these should be treated as lower bounds on near-term cost; use actual observed prices when available for 2025+.
