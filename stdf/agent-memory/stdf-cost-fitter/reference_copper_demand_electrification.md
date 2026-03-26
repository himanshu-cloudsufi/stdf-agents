---
name: reference_copper_demand_electrification
description: Validated exponential fits, learning rates, BESS service-level conversion, and threshold years for multi-vector copper demand analysis (Li-ion, solar PV, onshore wind, BESS, EV) (2026-03-25)
type: reference
---

## Multi-Vector Copper Demand Electrification Analysis

### Validated Exponential Fit Parameters (2026-03-25)

| Vector | Technology | C0 | r (decay) | ref_year | R² | Data Pts | Year Span |
|--------|-----------|-----|----------|---------|-----|---------|----------|
| 1 | Li-Ion Battery Pack ($/kWh) | 1257.75 | 0.1883 | 2010 | 0.956 | 14 | 2010–2024 |
| 2 | Solar PV LCOE ($/MWh) | 430.97 | 0.1824 | 2010 | 0.975 | 10 | 2010–2024 |
| 3 | Onshore Wind LCOE ($/MWh) | 117.40 | 0.0908 | 2009 | 0.934 | 9 | 2009–2024 |
| 5 | BESS $/MWh delivered | 131.92 | 0.0872 | 2019 | 0.873 | 6 | 2019–2024 |
| 6 | EV Purchase Price ($/vehicle) | 53275.54 | 0.0394 | 2010 | 0.990 | 7 | 2010–2024 |
| Solar-hw | Solar PV Installed $/kW | 4770.36 | 0.1455 | 2010 | 0.986 | 15 | 2010–2024 |

### Learning Rates (empirically derived)

- Li-Ion Battery Pack: 17.2%/yr (NORMAL: 12–28%)
- Solar PV LCOE: 16.7%/yr (NORMAL: 5–35%)
- Onshore Wind LCOE: 8.7%/yr (NORMAL: 8–18% at lower bound)
- BESS $/MWh delivered: 8.3%/yr (CAUTION: below 12–28% expected range — BOP costs slower to decline)
- EV Purchase Price: 3.9%/yr (N/A bounds — reflects net vehicle pricing, not cell cost alone)

### BESS Service-Level Conversion

$$\text{service\_cost} = \frac{\text{capex\_per\_kWh} \times 1000}{\text{cycle\_life} \times \text{duration\_hrs} \times \text{RTE} \times \text{DoD}}$$

Parameters: cycle_life=4,000, duration_hrs=2, RTE=0.85, DoD=0.90
- 2024: $269/kWh_cap → $87.9/MWh_delivered
- 2019: $441/kWh_cap → $144.1/MWh_delivered
- Sensitivity: at cycle_life=3,000 → 2024 = $117/MWh_delivered

### Competitive Thresholds (parity year)

- Solar PV vs. Gas Peaker LCOE ($169.5/MWh mean): parity 2015–2016 (~$150/MWh)
- Onshore Wind vs. Gas CCGT ($76/MWh): parity 2013–2014 (~$76/MWh)
- BESS ($/MWh delivered) vs. Gas Peaker ($168/MWh): parity 2019–2020
- EV vs. ICE purchase price ($29,000): parity 2025–2026

### Inflection Thresholds (50–70% of incumbent)

- Solar vs. Gas Peaker: 2017–2019 ($84–$118/MWh). Already passed: 2024 solar at 26% of gas peaker
- Wind vs. CCGT: 2017–2022 ($38–$53/MWh). Already passed: 2024 wind at 45% of CCGT
- BESS vs. Gas Peaker: 2020–2025 ($84–$118/MWh). In inflection: 2024 BESS at 52% of gas peaker
- EV vs. ICE: 2034–2044 (slow decay; copper demand from EVs driven by volume, not cost dominance)

### Copper Demand by Electrification Vector (key data points)

| Year | EV (kt) | Solar (kt) | Wind (kt) | Total Elec (kt) | Share (%) |
|------|---------|-----------|-----------|-----------------|-----------|
| 2015 | 231 | 161 | 161 | 553 | 2.4 |
| 2024 | 1,367 | 547 | 410 | 2,324 | 8.5 |

CAGRs 2015–2024: EV 21.9%/yr, Solar 14.5%/yr, Wind 10.9%/yr, Total copper 1.9%/yr

Copper intensity (CDA/ICA observed): BEV=83 kg/vehicle, Solar=5.0 t/MW, Onshore Wind=3.0 t/MW (±50% uncertainty)

### Incumbent Trends

- Gas peaker LCOE: flat (+$1.35/MWh/yr, R²=0.30 fuel-price noise), mean $169.5/MWh
- ICE vehicle: linear rising +$500/vehicle/yr (R²=1.00)
- Copper mining cost: linear rising +$145/tonne/yr (R²=0.855), mean $3,549/tonne

### Key Analytical Notes

- 2022 Li-ion anomaly ($166/kWh spike) excluded from fit — documented supply-chain/Li carbonate shock
- Solar LCOE plateau 2020–2024: only -10% over 4 years. Pre-plateau fit (2010–2020): r=0.210, R²=0.994
- Solar bottom-up LCOE from installed cost ($700/kW, CF=16.3%, WACC=7%, 25yr) = $54/MWh vs IRENA $43/MWh — gap from lower WACC in developing markets
- BESS LCOE CAUTION: cell-level LR is 17.2%/yr; system-level BESS LR is only 8.3%/yr due to BOP costs
- Offshore wind: only 4 LCOE data points (2010, 2022, 2023, 2024) — excluded from primary fit analysis
- Copper demand share data from "Database" catalog (unattributed) — needs ICSG verification before use in stream-forecaster
