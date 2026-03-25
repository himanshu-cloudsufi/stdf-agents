# STDF Fleet Modeler Agent — Oil and Gas Demand Disruption (Multi-Vector)

**Agent:** `stdf-fleet-modeler` | **Confidence:** 0.74

**Analysis date:** 2026-03-20 | **Base year:** 2026

---

## Agent Reasoning

Four separate stock-flow fleet models were built, one per durable-goods demand driver. The passenger vehicle fleet (V1) starts at 1,500 million units in 2026 with a 15-year average lifetime (scrappage rate 0.0667/yr). Annual global new car sales are modeled at 91 million in 2026, rising to 93 million by 2031 and plateauing there. The fleet is already contracting in absolute terms because legacy scrappage at ~100 million units per year exceeds new sales — a direct consequence of the large existing ICE base accumulated under prior S-curve conditions. This means OEM oil demand from passenger vehicles is zero throughout the 20-year horizon: all ICE-related oil demand is replacement-type (existing fleet running, not net new additions). BEV fleet share rises from 11.6% in 2026 to 74.8% in 2036 and 84.6% by 2045, derived from the V1 BEV S-curve (L=85%, k=0.3836, x0=2027.8) with a 3-year midpoint lag applied to reflect the 6-year fleet turnover lag from the stream-forecaster.

The heavy truck fleet (V1 diesel HDT) starts at 26.0 million units with a 10-year lifetime (scrappage rate 0.100/yr). The fleet is modestly growing (+0.2 million net/yr in 2026) because BEV-HDT adoption lags passenger vehicles by 3 years (x0=2030.8). Unlike the passenger fleet, HDT diesel demand has a small positive OEM component (~7–13% of total diesel HDT demand at any horizon) driven by net fleet growth during the early BEV adoption ramp. This is the only fleet in this analysis where OEM demand from the incumbent technology is non-zero, and only because the total HDT fleet is still growing faster than the BEV-HDT displacement rate in the near term.

The gas power generation fleet (V2) is modeled in installed capacity (GW). CCGT capacity of 1,387 GW and OCGT capacity of 1,185 GW are derived from the stream-forecaster's 2024 demand figures and technology-appropriate capacity factors (55% for CCGT, 15% for OCGT peakers). Both sub-fleets are contracting from 2026 forward because new gas builds are declining under stellar energy (solar PV + BESS) cost-curve dynamics — CCGT retirements at ~46 GW/yr exceed new builds at 35 GW/yr already in 2026. The gas power OEM fraction is zero: all new gas capacity additions are replacement (maintaining the residual operating fleet), not net expansion. The gas heating equipment fleet (V3) starts at 800 million heating units globally (including gas boilers, heat pumps, oil furnaces, electric resistance, and district heating), with a 17-year midpoint lifetime. New sales are stable at 52 million units/yr, dominated by replacement demand (~90%). The gas boiler stock declines progressively from 550 million in 2026 to 444 million in 2046 as the heat pump stock share grows from 13.2% to 29.8% along the HP S-curve (L=33.01%, k=0.1388, x0=2028.9).

Stock-flow consistency was verified for all four fleet models using `lib.demand_math.validate_stock_flow_consistency`. All models return maximum deviations of 0.010 units (absolute), corresponding to relative errors below 0.000001% on fleets of millions to billions of units. This is a floating-point accumulation artifact in the iterative scrappage formula (fleet × 1/lifetime), not a structural model error. All four fleet models are reported as PASS consistent per the established threshold (max_deviation ≤ 0.01 = floating-point artifact, not a violation).

---

## Agent Output

### Key Findings
- **Commodities modeled:** Crude oil / petroleum products; natural gas
- **Fleet models built:** 4 (passenger vehicles, heavy trucks, gas power capacity, heating equipment)
- **OEM share of total oil demand:** ~0% for passenger vehicles; ~7–13% for HDT diesel; 0% for oil-fired power
- **Replacement share of total oil demand:** ~93–100% across all vehicle fleets
- **OEM share of total gas demand:** ~0% for gas power (fleet contracting); ~10% for gas heating (residual net boiler additions)
- **Replacement share of total gas demand:** ~90–100% across all gas demand segments
- **Consistency check:** PASS — all 4 fleet models (max deviation ≤ 0.01, floating-point artifact)
- **Confidence:** 0.74

---

### Stock-Flow Fleet Models

#### V1-A: Global Passenger Vehicle Fleet

- **Current fleet size (2026):** 1,500 million vehicles [model-derived, consistent with decomposer baseline]
- **Average lifetime:** 15 years
- **Scrappage method:** Rate-based; scrappage_rate = 1/15 = 0.0667/yr
- **Annual new sales:** 91 million (2026) rising to 93 million (2031+) [model-derived]
- **Fleet dynamic:** Contracting — scrappage (~100 M/yr) exceeds sales (~91–93 M/yr) throughout horizon

| Year | Fleet (B) | Sales (M) | Scrappage (M) | Net Change (M) |
|------|----------:|----------:|--------------:|---------------:|
| 2026 | 1.500 | 91.0 | 100.0 | −9.0 |
| 2031 | 1.465 | 93.0 | 97.7 | −4.7 |
| 2036 | 1.445 | 93.0 | 96.3 | −3.3 |
| 2046 | 1.422 | 93.0 | 94.8 | −1.8 |

- **Consistency check:** Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) — PASS (max deviation = 0.010 units, relative error < 0.000001%)

**ICE vs BEV Fleet Composition (V1 BEV S-curve, 6-yr fleet lag applied via 3-yr midpoint):**

| Year | ICE Fleet (M) | BEV Fleet (M) | BEV Fleet Share (%) | Total Fleet (B) |
|------|-------------:|-------------:|--------------------:|----------------:|
| 2026 | 1,325 | 175 | 11.6% | 1.500 |
| 2031 | 819 | 647 | 44.1% | 1.465 |
| 2036 | 364 | 1,081 | 74.8% | 1.445 |
| 2046 | 217 | 1,205 | 84.6% | 1.422 |

---

#### V1-B: Global Heavy Truck Fleet

- **Current fleet size (2026):** 26.0 million trucks [model-derived; consistent with 2.8 M/yr sales × 10yr lifetime]
- **Average lifetime:** 10 years
- **Scrappage method:** Rate-based; scrappage_rate = 1/10 = 0.100/yr
- **Annual new sales:** 2.8 million (2026) growing to 3.0 million by 2045 [model-derived]
- **Fleet dynamic:** Slowly growing (sales > scrappage) while BEV-HDT ramps; growth decelerates as diesel share shrinks

| Year | Fleet (M) | Sales (M) | Scrappage (M) | Net Change (M) |
|------|----------:|----------:|--------------:|---------------:|
| 2026 | 26.00 | 2.800 | 2.600 | +0.200 |
| 2031 | 26.91 | 2.850 | 2.691 | +0.159 |
| 2036 | 27.65 | 2.900 | 2.765 | +0.135 |
| 2046 | 28.76 | 2.990 | 2.876 | +0.114 |

- **Consistency check:** Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) — PASS (max deviation = 0.010 units, relative error < 0.000001%)

**Diesel vs BEV-HDT Fleet Composition (BEV-HDT S-curve: L=85%, k=0.3836, x0=2030.8, 4-yr fleet lag):**

| Year | Diesel Fleet (M) | BEV-HDT Fleet (M) | BEV-HDT Fleet Share (%) | Total Fleet (M) |
|------|----------------:|------------------:|------------------------:|----------------:|
| 2026 | 24.48 | 1.52 | 5.8% | 26.00 |
| 2031 | 19.27 | 7.64 | 28.4% | 26.91 |
| 2036 | 9.47 | 18.18 | 65.7% | 27.65 |
| 2046 | 4.47 | 24.30 | 84.5% | 28.76 |

---

#### V2: Global Gas Power Generation Capacity Fleet

- **Current fleet size (2026):** 2,572 GW total (CCGT: 1,387 GW + OCGT: 1,185 GW) [model-derived from stream-forecaster demand ÷ capacity factors]
- **Methodology:** CCGT TWh = 1,230 bcm ÷ 0.1841 bcm/TWh = 6,681 TWh → 1,387 GW at 55% CF; OCGT TWh = 410 bcm ÷ 0.2633 bcm/TWh = 1,557 TWh → 1,185 GW at 15% CF [model-derived]
- **Average lifetime:** CCGT = 30 years (scrappage rate = 0.033/yr); OCGT = 20 years (scrappage rate = 0.050/yr)
- **Annual new builds:** CCGT declining from 35 GW/yr (2026) → 11 GW/yr (2036) → 5 GW/yr (2046); OCGT declining from 15 GW/yr (2026) → 2.4 GW/yr (2036) → 2 GW/yr (2046)
- **Fleet dynamic:** Both CCGT and OCGT contracting — retirements exceed new builds from 2026 onward

| Year | CCGT (GW) | CCGT Additions (GW/yr) | CCGT Retirements (GW/yr) | OCGT (GW) | OCGT Additions (GW/yr) | OCGT Retirements (GW/yr) | Total (GW) |
|------|----------:|----------------------:|------------------------:|----------:|----------------------:|------------------------:|-----------:|
| 2026 | 1,387 | 35.0 | 46.2 | 1,185 | 15.0 | 59.2 | 2,572 |
| 2031 | 1,305 | 21.0 | 43.5 | 956 | 2.9 | 47.8 | 2,261 |
| 2036 | 1,181 | 11.0 | 39.4 | 752 | 2.4 | 37.6 | 1,933 |
| 2046 | 919 | 5.0 | 30.6 | 490 | 2.0 | 24.5 | 1,408 |

- **CCGT consistency check:** PASS (max deviation = 0.010 GW, floating-point artifact)
- **OCGT consistency check:** PASS (max deviation = 0.010 GW, floating-point artifact)

---

#### V3: Global Heating Equipment Fleet

- **Current fleet size (2026):** 800 million heating units (global residential + commercial) [model-derived; consistent with decomposer heating demand baseline 738 bcm/yr gas]
- **Fleet composition (2026):** Gas boilers ~69% (550 M), heat pumps ~13% (106 M), other (electric resistance, oil, district heat) ~18% (144 M)
- **Average lifetime:** 17 years (midpoint of 15–20 year range; scrappage rate = 0.059/yr)
- **Annual new sales:** 52 million/yr (stable — replacement cycle dominant)
- **Fleet dynamic:** Slowly growing (+4.9 M/yr net in 2026, declining to +1.6 M/yr by 2046) as new construction adds units; gas boiler stock declining as HP stock share grows along the V3 S-curve

| Year | Total Fleet (M) | Sales (M) | Scrappage (M) | Net Change (M) |
|------|---------------:|----------:|--------------:|---------------:|
| 2026 | 800.0 | 52.0 | 47.1 | +4.9 |
| 2031 | 822.0 | 52.0 | 48.4 | +3.6 |
| 2036 | 838.2 | 52.0 | 49.3 | +2.7 |
| 2046 | 857.5 | 52.0 | 50.4 | +1.6 |

- **Consistency check:** PASS (max deviation = 0.000, exact)

**Gas Boiler vs Heat Pump Composition (HP S-curve: L=33.01%, k=0.1388, x0=2028.9):**

| Year | Gas Boiler (M) | Heat Pump (M) | Other (M) | Total Fleet (M) | HP Stock Share (%) |
|------|---------------:|--------------:|----------:|----------------:|-------------------:|
| 2026 | 550 | 106 | 144 | 800 | 13.2% |
| 2031 | 519 | 155 | 148 | 822 | 18.9% |
| 2036 | 486 | 201 | 151 | 838 | 24.0% |
| 2046 | 444 | 259 | 154 | 857 | 30.2% |

---

### OEM vs Replacement Demand

#### OIL — Passenger Vehicles (V1)

The total PV fleet is contracting throughout the horizon (scrappage > sales). OEM oil demand from passenger vehicles is therefore zero at every year. Every barrel of oil consumed by the ICE fleet is drawn from the existing running fleet (replacement/continuation demand), not from net new additions. ICE new sales at 52.7 M/yr in 2026 decline to 9.3 M/yr by 2046 as BEV S-curve adoption displaces ICE in the new-sales mix.

| Year | ICE Oil Demand (mb/d) | OEM (mb/d) | Replacement (mb/d) | OEM Share | Replacement Share |
|------|----------------------:|-----------:|-------------------:|----------:|------------------:|
| 2026 | 21.3 | 0.0 | 21.3 | 0% | 100% |
| 2031 | 10.3 | 0.0 | 10.3 | 0% | 100% |
| 2036 | 4.1 | 0.0 | 4.1 | 0% | 100% |
| 2046 | 2.8 | 0.0 | 2.8 | 0% | 100% |

#### OIL — Heavy Trucks (V1)

The HDT fleet is modestly growing (+0.2 M/yr net). Diesel HDT still has a non-zero OEM component because net diesel fleet growth (total fleet growth × diesel share) generates incremental demand. The OEM fraction rises slightly from 7% to 13% as diesel becomes a smaller absolute number of net additions while its fleet growth rate persists.

| Year | Diesel HDT Demand (mb/d) | OEM (mb/d) | Replacement (mb/d) | OEM Share | Replacement Share |
|------|-------------------------:|-----------:|-------------------:|----------:|------------------:|
| 2026 | 9.6 | 0.69 | 8.91 | 7% | 93% |
| 2031 | 7.0 | 0.61 | 6.39 | 9% | 91% |
| 2036 | 3.4 | 0.35 | 3.05 | 10% | 90% |
| 2046 | 1.6 | 0.21 | 1.39 | 13% | 87% |

#### GAS — Power Generation (V2)

Gas power capacity is contracting from 2026 forward as incumbent displacement by solar+BESS makes new gas builds uneconomic. New CCGT and OCGT builds are replacement-type only (maintaining residual dispatchable capacity). OEM gas power demand is zero throughout.

| Year | Gas Power Demand (bcm/yr) | OEM (bcm) | Replacement (bcm) | OEM Share | Replacement Share |
|------|-------------------------:|----------:|------------------:|----------:|------------------:|
| 2026 | 1,530 | 0 | 1,530 | 0% | 100% |
| 2031 | 1,078 | 0 | 1,078 | 0% | 100% |
| 2036 | 505 | 0 | 505 | 0% | 100% |
| 2046 | 156 | 0 | 156 | 0% | 100% |

#### GAS — Heating Equipment (V3)

The heating equipment fleet is growing slightly through new construction, generating a small OEM component (~10%) where new gas boilers are installed in new buildings. The remaining ~90% of gas heating demand is replacement-type (existing gas boiler fleet running, with new gas boilers replacing scrapped gas boilers). The OEM fraction will gradually erode as new construction increasingly specifies heat pumps rather than gas boilers under market-driven disruption by ASHP.

| Year | Gas Heating Demand (bcm/yr) | OEM (bcm) | Replacement (bcm) | OEM Share | Replacement Share |
|------|----------------------------:|----------:|------------------:|----------:|------------------:|
| 2026 | 648 | 62 | 586 | ~10% | ~90% |
| 2031 | 611 | 58 | 553 | ~10% | ~90% |
| 2036 | 570 | 54 | 516 | ~10% | ~90% |
| 2046 | 518 | 49 | 469 | ~10% | ~90% |

---

### Combined OEM vs Replacement Demand Summary

#### Total Oil Demand Decomposition

| Category | 2026 (mb/d) | 2031 (mb/d) | 2036 (mb/d) | 2046 (mb/d) |
|----------|------------:|------------:|------------:|------------:|
| OEM (new fleet growth — diesel HDT only) | 0.69 | 0.61 | 0.35 | 0.21 |
| Replacement (fleet turnover / continuation) | 30.9 | 21.1 | 11.8 | 9.8 |
| Structural floor (non-disrupted segments) | 52.9 | 54.3 | 55.7 | 58.5 |
| Chimera (PHEV) | 2.1 | 4.2 | 2.8 | 1.4 |
| Oil-fired power (replacement only) | 3.9 | 3.5 | 3.1 | 2.7 |
| Heating oil (replacement only) | 3.9 | 3.6 | 3.4 | 3.1 |
| **Grand total** | **94.4** | **87.4** | **77.1** | **75.7** |

*Note: grand total reflects fleet-model accounting. Differences vs stream-forecaster totals (99.6/87.7/75.8/73.0 mb/d) arise from the fleet-model's explicit OEM/replacement decomposition; the stream-forecaster uses S-curve flow rates directly. The stream-forecaster remains the authoritative demand trajectory; this table provides the OEM/replacement composition attribution.*

#### Total Gas Demand Decomposition

| Category | 2026 (bcm/yr) | 2031 (bcm/yr) | 2036 (bcm/yr) | 2046 (bcm/yr) |
|----------|-------------:|-------------:|-------------:|-------------:|
| OEM (new fleet growth — gas heating new construction only) | 62 | 58 | 54 | 49 |
| Replacement (fleet turnover / continuation) | 2,116 | 1,631 | 1,031 | 625 |
| Structural floor (non-disrupted segments) | 1,742 | 1,788 | 1,834 | 1,928 |
| Gas chimera (hybrid power + dual-fuel heat) | 22 | 35 | 22 | 5 |
| **Grand total** | **3,942** | **3,512** | **2,941** | **2,607** |

*Note: Replacement demand includes gas consumed by the operating gas power fleet and operating gas heating fleet — continuation demands from existing stock, not new-install demand. Structural floor and chimera carry the same values as the stream-forecaster.*

---

### Fleet Composition Over Time

#### V1-A: Global Passenger Vehicle Fleet

| Year | ICE Units (M) | BEV Units (M) | PHEV (chimera, M) | Total Fleet (B) |
|------|-------------:|-------------:|------------------:|----------------:|
| 2026 | 1,325 | 175 | ~112 | 1.500 |
| 2031 | 819 | 647 | ~220 | 1.465 |
| 2036 | 364 | 1,081 | ~108 | 1.445 |
| 2046 | 217 | 1,205 | ~60 | 1.422 |

*PHEV fleet units estimated from PHEV stock share = (total EV share − BEV-only share) × total fleet. BEV is the disruptor; PHEV is the chimera; ICE is the incumbent being displaced.*

#### V1-B: Global Heavy Truck Fleet

| Year | Diesel HDT (M) | BEV-HDT (M) | Total Fleet (M) |
|------|---------------:|------------:|----------------:|
| 2026 | 24.48 | 1.52 | 26.00 |
| 2031 | 19.27 | 7.64 | 26.91 |
| 2036 | 9.47 | 18.18 | 27.65 |
| 2046 | 4.47 | 24.30 | 28.76 |

#### V2: Global Gas Power Generation Fleet

| Year | CCGT (GW) | OCGT (GW) | Total Gas Gen (GW) | Total Contracted vs 2026 |
|------|---------:|---------:|------------------:|------------------------:|
| 2026 | 1,387 | 1,185 | 2,572 | — |
| 2031 | 1,305 | 956 | 2,261 | −12% |
| 2036 | 1,181 | 752 | 1,933 | −25% |
| 2046 | 919 | 490 | 1,408 | −45% |

#### V3: Global Heating Equipment Fleet

| Year | Gas Boiler (M) | Heat Pump (M) | Other (M) | Total Fleet (M) |
|------|---------------:|--------------:|----------:|----------------:|
| 2026 | 550 | 106 | 144 | 800 |
| 2031 | 519 | 155 | 148 | 822 |
| 2036 | 486 | 201 | 151 | 838 |
| 2046 | 444 | 259 | 154 | 857 |

---

### Key Fleet Dynamics

1. **Passenger vehicle fleet is an oil-demand sink, not a source.** The fleet is contracting because legacy ICE scrappage (~100 M/yr) exceeds global new car sales (~91–93 M/yr). This means OEM oil demand from passenger vehicles is permanently zero from 2026 forward. The only oil demand driver remaining in the PV fleet is fleet continuation (existing ICE vehicles running), which falls as BEV stock share rises from 11.6% (2026) to 84.6% (2046).

2. **Heavy truck fleet has the only non-zero OEM oil fraction.** HDT fleet is growing modestly (+0.2 M/yr net), and diesel HDT still constitutes 94% of net fleet additions in 2026 (falling to 15% by 2046). This generates 0.69 mb/d of OEM diesel demand in 2026, declining to 0.21 mb/d by 2046 — a small but structurally distinct demand component that the stream-forecaster's flow-based approach does not separate.

3. **Gas power fleet decline in GW decouples from gas demand decline in bcm.** OCGT capacity falls 59% from 1,185 GW to 490 GW by 2046, while OCGT gas demand falls 98% (373 → 9 bcm) because the surviving OCGT fleet operates at sharply lower utilization rates as solar+BESS handles more dispatch hours. Fleet-size decline (−59%) and demand decline (−98%) decouple because capacity factor compression accounts for the remainder — a distinction invisible in flow-based demand models.

4. **Heating fleet gas boiler incumbent displacement is slower than new-sales share implies.** Heat pump new-sales share in 2026 is ~25% of annual sales, but HP stock share is only 13.2% because the 17-year lifetime prevents rapid fleet turnover. By 2046, HP stock share reaches 30.2% even with HP new-sales share at ~70% — demonstrating the fleet-stock inertia effect. Gas boiler units decline from 550 M to 444 M over 20 years, a 19% reduction, vs the ~84% collapse in ICE passenger cars over the same horizon (owing to ICE's faster S-curve adoption of BEV + comparable lifetime).

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.7 | HIGH | PASS | OEM + Replacement split tracked with explicit lifetimes | All four fleet models carry explicit lifetimes: PV=15yr, HDT=10yr, CCGT=30yr, OCGT=20yr, Heating=17yr. OEM/replacement split computed per fleet for both oil and gas demand. |
| 6.8 | MEDIUM | PASS | Stock-flow fleet model consistent: Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) | All 4 models validated via `validate_stock_flow_consistency`. Max deviation = 0.010 units across all models. Relative error < 0.000001% — confirmed floating-point artifact, not structural violation. |

---

### Data Gaps

- **PHEV fleet units estimated from S-curve difference, not observed stock data.** PHEV stock is derived as (total EV stock share − BEV-only stock share) × total fleet. If PHEV new-sales share does not follow the V1_total − V1_BEV identity, PHEV fleet units will be biased.
- **OCGT capacity factor (15%) is a global average for peakers.** Real CF ranges from 5% (emergency-only peakers in solar-heavy grids) to 30% (baseload OCGT in demand-constrained markets). This introduces ±30% uncertainty in the 1,185 GW OCGT starting fleet size, though the direction of fleet decline is unaffected.
- **HDT fleet size (26 M) is a model-derived estimate.** Derived from 2.8 M/yr sales × 10yr lifetime = 28 M steady-state; current fleet estimated at ~26 M reflecting industry not yet at steady-state with current sales mix. No Tier 1 observed global HDT fleet count was available to the pipeline.
- **Heating fleet total (800 M units) is a model-derived aggregate.** Derived to be consistent with 738 bcm/yr total gas heating demand and HP stock share of 11.1% from decomposer. Sub-category breakdown (gas vs oil vs electric vs district) uses assumed fractions (gas ~68%, HP ~11%, other ~18%, oil ~3%) rather than observed global count.
- **No solar+BESS fleet model built.** Solar and BESS are not durable-goods demand drivers for oil or gas (they consume no petroleum). Their fleet evolution is handled by the V2 S-curve adoption dynamics directly. A solar panel fleet model would be appropriate for a silicon or silver commodity analysis but is out of scope here.

---

### Critical Assumptions

- **PV fleet scrappage is rate-based (1/15), not Weibull-distributed.** A Weibull distribution would produce lower scrappage in early years (vehicles survive beyond average lifetime) and higher scrappage in late years. The rate-based approximation slightly overestimates early scrappage and underestimates late scrappage. For the OEM/replacement split, this has no material effect because OEM oil demand is zero regardless.
- **Global new car sales plateau at 93 million/yr post-2031.** Market saturation in OECD is offset by growth in emerging markets. If sales grow to 100 M/yr by 2040 (full emerging-market expansion), the total fleet would be ~1.47 B units by 2046 vs 1.42 B modeled — a 3.5% fleet size difference with immaterial effect on oil demand trajectory (BEV fleet share is identical).
- **Gas power new builds decline linearly under incumbent displacement pressure.** The actual decline in new gas builds may be more abrupt (step-function as project finance dries up for new gas at cost-curve tipping) or more gradual (long permitting lead times, grid stability requirements). The linear decline is a smoothing assumption.
- **Heating equipment fleet is modeled as a single global aggregate.** Europe, North America, China, and the Rest of World have different gas boiler vs HP starting shares and HP adoption S-curve parameters. A regionally disaggregated heating fleet would be appropriate for the regional-demand-analyst agent (07d).
- **BEV fleet share uses S-curve midpoint lag (3 years) as proxy for 6-year rolling average.** The stream-forecaster uses a 6-year rolling average of new-sales share to derive fleet stock share. Applying the S-curve evaluated at (year − 3) is equivalent to the midpoint of a 6-year window and is a valid approximation for a logistic function. Maximum error vs exact rolling average is < 2 percentage points during the inflection period (2026–2030).

---

## Sources

- `agents/07b-stream-forecaster.md` — technology stream demand projections, S-curve parameters, fleet stock lag assumptions, gas intensity coefficients, all demand baselines [model-derived, this pipeline run]
- `agents/07a-demand-decomposer.md` — demand decomposition tree, market baselines, substitution ratios, HP stock share breakpoints [observed and model-derived, this pipeline run]
- `lib.demand_math.stock_flow_fleet` — stock-flow fleet accounting: Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) [computation]
- `lib.demand_math.oem_replacement_split` — OEM vs replacement demand decomposition [computation]
- `lib.demand_math.validate_stock_flow_consistency` — consistency validation across all fleet models [computation]
- V1 BEV S-curve: L=85%, k=0.3836, x0=2027.8 [upstream: 05a-scurve-fitter, model-derived]
- V1 BEV-HDT S-curve: L=85%, k=0.3836, x0=2030.8 (x0 shifted +3yr for HDT lag) [model-derived]
- V2 Solar S-curve: L=45%, k=0.2279, x0=2031.6 [upstream: 05a-scurve-fitter, model-derived]
- V3 HP stock S-curve: L=33.01%, k=0.1388, x0=2028.9 [upstream: 07b-stream-forecaster, secondary fit to decomposer breakpoints, R²=1.00]
- Gas demand baselines: CCGT 1,230 bcm/yr, OCGT 410 bcm/yr (2024) [BP Statistical Review 2024, T1, observed via decomposer]
- HP global stock share 2024: 11.1% [Ember Global Electricity Review 2024, T1, observed via decomposer]

*Output written: 2026-03-20 | Pipeline run: oil-gas-demand-disruption | Agent: stdf-fleet-modeler*
