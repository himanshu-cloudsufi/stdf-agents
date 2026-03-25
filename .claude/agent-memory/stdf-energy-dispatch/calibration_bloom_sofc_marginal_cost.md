---
name: Bloom SOFC Marginal Cost Formula and Observed Range
description: SOFC marginal cost formula, 2024 values, and historical range for dispatch merit order placement
type: reference
---

**Formula:** SOFC_Marginal_$/MWh = (NG_$/MMBtu / (293.07 × efficiency)) × 1000 + variable_OM

**Parameters (Bloom Energy Series 10):**
- Efficiency: 58% (heat rate 5,811–7,127 Btu/kWh per Bloom datasheet 2024)
- Variable O&M: $10.0/MWh (conservative — full O&M of $24/MWh includes fixed maintenance)

**Historical range (2010–2024):**
| Year | Henry Hub ($/MMBtu) | Bloom Marginal ($/MWh) |
|------|--------------------|-----------------------|
| 2020 | $2.03 | $21.9 |
| 2021 | $3.89 | $32.9 |
| 2022 | $6.45 | $61.9 |
| 2023 | $2.53 | $24.9 |
| 2024 | $2.19 | $22.9 |

**2024 summary:**
- At historic-low NG ($2.19/MMBtu): $22.9/MWh
- At historical average NG ($2.75/MMBtu): $40.2/MWh (used as mid-case)
- At 2010-level NG ($4.37/MMBtu): $49.7/MWh

**Merit order placement:** Bloom SOFC sits between BESS (SCOE $5–14/MWh in 2024) and grid C&I ($80–120/MWh). SWB always dispatches before Bloom. Bloom is displaced BEFORE grid, not after.

**Kill condition (Tony's framing):** SWB amortized capex < SOFC marginal cost. Crossed 2032–2033 at NG mid-case, 2041–2042 at NG low (per 02b-cost-fitter). The LCOE parity (new-vs-new) crosses in 2031–2032.

**Source:** Bloom Energy datasheet (2024), 02b-cost-fitter.md, EIA Henry Hub annual averages [CAUTION: EIA source — historical data only]
