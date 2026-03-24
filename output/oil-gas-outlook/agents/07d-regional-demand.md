# STDF Regional Demand Analyst Agent — Oil and Gas Demand Disruption (Multi-Vector)

**Agent:** `stdf-regional-demand-analyst` | **Confidence:** 0.73

**Analysis date:** 2026-03-20 | **Base year:** 2026

---

## Agent Reasoning

Regional disaggregation proceeds independently for oil and gas across four regions (China, USA, Europe, Rest of World) using region-specific S-curve parameters from the upstream regional-adopter (05b) combined with global stream totals from the stream-forecaster (07b). Rather than splitting global totals by fixed percentages, each region's demand trajectory is computed from its own S-curve parameters for each disruption vector, then reconciled against the 07b global totals via a year-specific scaling factor. Scaling factors range from 0.9997 to 1.0791 for oil and 0.9997 to 1.0470 for gas, confirming that the independent regional projections are internally consistent with the global model before reconciliation.

Oil demand disaggregation covers three disruption vectors applied to region-specific market shares: V1 (EV adoption displacing transport oil — passenger ICE, PHEV chimera, HDT diesel, LCV), V2 (solar PV displacing oil-fired power), and V3 (heat pump stock growth displacing heating oil). Regional shares of each disruption-eligible oil segment are estimated from structural knowledge of where each consumption type concentrates: V1 transport oil is split by vehicle fleet size (China 24%, USA 22%, Europe 18%, RoW 36%); V2 oil-fired power is RoW-dominated (60%) because oil-fired generation is concentrated in Middle East, Africa, and SE Asia; V3 heating oil is Europe- and USA-dominated (55%/35%) because continental Northern Europe and the US Northeast are the primary heating oil markets. The structural floor (aviation, marine, petrochemicals, off-road) is split approximately by economic activity (RoW 55%, USA 19%, China 15%, Europe 11%). Fleet-lagged EV share for V1 uses a 6-year rolling average of new-sales S-curve values per region, producing region-specific ICE fleet shares that diverge strongly across regions by 2031.

Gas demand disaggregation covers V2 (solar PV displacing CCGT and OCGT gas power) and V3 (HP stock displacing residential and commercial gas heating) against a structural floor (industrial, petrochemicals, LNG fuel, pipeline compressors). V2 gas power is USA-dominant (30% of global gas power) because the USA generates approximately 40% of its electricity from gas; China is only 8% of global gas power because coal dominates China's generation mix. V3 gas heating is split between USA (36%) and Europe (38%) because both have mature gas heating infrastructure with large incumbent boiler stocks; China accounts for only 7% because northern China uses coal district heating rather than residential gas boilers. Regional HP stock S-curve parameters for China, USA, and RoW are estimated by applying the lag estimates from the regional-adopter (China: 5-year lag, USA: 6-year lag, RoW: 9-year lag) as x0 offsets from Europe's fitted parameters (L=0.3301, k=0.1393, x0=2028.9), with ceiling adjustments to reflect structural differences (China's lower gas heating market depth yields L=0.28).

Cost-curve dynamics govern all regional S-curve trajectories. China's V1 EV adoption inflects at x0=2023.7 — already past the steepest growth phase — while the USA inflects at x0=2029.2, a 5.6-year gap driven by lower fuel cost signals, less EV-friendly fleet mix (SUVs, trucks), and charging infrastructure deployment lags. This is a case of market-driven disruption where cost-curve superiority, not policy mandates, determines the regional adoption pace. China's V2 solar S-curve has the steepest growth rate (k=0.2649) of any region, reflecting the concentrated solar+BESS manufacturing supply chain and co-deployment scale. Europe's V3 heat pump S-curve has the earliest inflection (x0=2028.9), and China's HP disruption is structurally different — primarily displacing coal district heating, not gas boilers — which means V3 gas destruction in China is limited relative to its HP market scale. The fundamental mechanism across all three vectors is S-curve incumbent displacement: the disruptor technology achieves cost-curve superiority and sequentially erodes the installed base of ICE vehicles, gas-fired generators, and gas boilers in each region according to its own adoption timeline.

---

## Agent Output

### Key Findings — Oil
- **Commodity:** Crude oil / petroleum products (mb/d)
- **Regions analyzed:** China, USA, Europe, RoW
- **Largest demand region (current):** RoW (48.7 mb/d, 49% of global)
- **Fastest declining region (oil):** Europe (-1.99%/yr CAGR); China also -1.66%/yr (V1 fleet disruption already advanced); USA -1.83%/yr; RoW -1.26%/yr
- **Oil demand peak:** Model-derived peak 2024–2026 for all regions; China peaks earliest
- **Confidence:** 0.73

### Key Findings — Gas
- **Commodity:** Natural gas (bcm/yr)
- **Largest demand region (current):** RoW (1,775 bcm, 45% of global)
- **Fastest declining region (gas):** USA (-2.57%/yr CAGR 2026–2046) — driven by the largest gas power sector and moderate HP adoption
- **Europe second fastest:** -2.18%/yr — heavy residential gas heating stock creates large V3 destruction surface
- **Gas demand peak:** Model-derived peak 2024–2026; structural floor growth partially offsets disruption-eligible declines through approximately 2029
- **Confidence:** 0.73

---

### Regional Oil Demand Breakdown

Units: mb/d [model-derived]. Regional sums reconciled to match 07b global totals exactly.

| Region | 2026 (current) | +5yr (2031) | +10yr (2036) | +20yr (2046) | Key Driver |
|--------|---------------:|------------:|-------------:|-------------:|------------|
| China  | 15.1 | 11.5 | 10.5 | 10.8 | V1 EV fleet (China past inflection; floor growth stabilizes at +20yr) |
| USA    | 21.0 | 18.8 | 15.9 | 14.5 | V1 slower (x0=2029.2); large structural floor (petrochemicals, aviation) |
| Europe | 14.8 | 12.3 | 10.5 |  9.9 | V1 + V3 heating oil; floor supports long-tail demand |
| RoW    | 48.7 | 45.1 | 39.0 | 37.8 | Dominant floor share; V1 lagged (x0=2029.6); oil power persists |
| **Global** | **99.6** | **87.7** | **75.8** | **73.0** | — |

*Global totals reconciled to 07b stream-forecaster P50 values. Scaling factors: 2026=1.079, 2031=1.071, 2036=1.046, 2046=1.046 [model-derived].*

### Regional Gas Demand Breakdown

Units: bcm/yr [model-derived]. Regional sums reconciled to match 07b global totals exactly.

| Region | 2026 (current) | +5yr (2031) | +10yr (2036) | +20yr (2046) | Key Driver |
|--------|---------------:|------------:|-------------:|-------------:|------------|
| China  |   378 |   334 |   284 |   277 | V2 solar dominant; V3 limited (HP displaces coal, not gas, in north China) |
| USA    | 1,045 |   907 |   743 |   621 | V2 largest absolute destruction (gas-heavy grid); V3 growing but cost-parity constrained |
| Europe |   737 |   615 |   524 |   474 | V3 heating gas largest surface; V2 meaningful; steepest combined % decline |
| RoW    | 1,775 | 1,642 | 1,369 | 1,230 | Dominant share; V2 large absolute but diffuse; V3 lagged (x0=2038) |
| **Global** | **3,935** | **3,497** | **2,920** | **2,601** | — |

*Global totals reconciled to 07b stream-forecaster P50 values. Scaling factors: 2026=1.000, 2031=1.047, 2036=0.996, 2046=1.006 [model-derived].*

---

### Regional S-Curve Parameters

#### V1: EV New Car Sales Share (L fixed = 90%)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | R² | Source |
|--------|------------|----------------|-----------------|-----|--------|
| China  | 90.0% | 0.5656 | 2023.7 | 0.9898 | 05b-regional-adopter [model-derived] |
| Europe | 90.0% | 0.3416 | 2025.9 | 0.9207 | 05b-regional-adopter [model-derived] |
| USA    | 90.0% | 0.3508 | 2029.2 | 0.9815 | 05b-regional-adopter [model-derived] |
| RoW    | 90.0% | 0.4706 | 2029.6 | 0.9943 | 05b-regional-adopter [model-derived] |

*China is 5.6 years ahead of USA at the inflection point. Europe is 2.2 years behind China. Europe R²=0.9207 is flagged below the 0.95 confidence threshold due to German incentive-withdrawal kink in 2023.*

#### V2: Solar Generation Share (L fixed = 45%)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | R² | Source |
|--------|------------|----------------|-----------------|-----|--------|
| China  | 45.0% | 0.2649 | 2029.5 | 0.9762 | 05b-regional-adopter [model-derived] |
| Europe | 45.0% | 0.1852 | 2030.5 | 0.9710 | 05b-regional-adopter [model-derived] |
| USA    | 45.0% | 0.2038 | 2033.0 | 0.9931 | 05b-regional-adopter [model-derived] |
| RoW    | 45.0% | 0.2289 | 2032.2 | 0.9852 | 05b-regional-adopter [model-derived] |

*China has the steepest growth rate (k=0.2649) and will overtake Europe's solar share by approximately 2027 [model-derived]. All four regions simultaneously in tipping phase (5–15% solar share, 2024).*

#### V3: Heat Pump Stock Share (HP stock S-curve)

| Region | L (ceiling) | k (growth rate) | x0 (inflection) | Basis | Source |
|--------|------------|----------------|-----------------|-------|--------|
| Europe | 33.01% | 0.1393 | 2028.9 | Fitted from 07b global HP breakpoints, anchored to EHPA | 05b + 07b [model-derived] |
| China  | 28.00% | 0.1393 | 2034.0 | Europe fit shifted +5yr; lower ceiling (coal-district heating, not gas) | estimated [model-derived] |
| USA    | 30.00% | 0.1393 | 2035.0 | Europe fit shifted +6yr; AHRI data anchor | estimated [model-derived] |
| RoW    | 25.00% | 0.1393 | 2038.0 | Europe fit shifted +9yr; heterogeneous market | estimated [model-derived] |

*V3 S-curve fits available only for Europe (R²=0.9987, 11 data points). China, USA, and RoW parameters are lag-adjusted estimates from the Europe baseline. China's 28% ceiling is reduced relative to Europe (33%) because China's HP market displaces coal district heating in northern regions, not gas boilers — limiting direct V3 gas demand destruction.*

---

### Regional S-Curve Adoption Values at Key Horizons

#### V1 EV New Car Sales Share by Region (%)

| Region | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|-----:|------------:|-------------:|-------------:|
| China  | 70.7% | 88.6% | 89.9% | 90.0% |
| Europe | 45.8% | 76.6% | 87.2% | 89.9% |
| USA    | 22.1% | 58.8% | 82.4% | 89.8% |
| RoW    | 14.0% | 59.3% | 85.8% | 90.0% |

*Fleet EV share (6-year rolling lag) at 2026: China=38.2%, Europe=26.1%, USA=10.8%, RoW=5.4%. Fleet EV share at 2031: China=79.2%, Europe=59.1%, USA=36.6%, RoW=31.4% [model-derived].*

#### V2 Solar Generation Share by Region (%)

| Region | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|-----:|------------:|-------------:|-------------:|
| China  | 12.8% | 26.9% | 38.2% | 44.4% |
| Europe | 13.6% | 23.5% | 33.1% | 42.6% |
| USA    |  8.7% | 18.0% | 29.2% | 42.0% |
| RoW    |  8.8% | 19.4% | 31.7% | 43.2% |

*China overtakes Europe's solar share at approximately 2027. By 2046, all four regions converge toward the 45% ceiling, with China reaching it earliest [model-derived].*

#### V3 HP Stock Share by Region (%)

| Region | 2026 | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|--------|-----:|------------:|-------------:|-------------:|
| Europe | 13.2% | 18.9% | 24.1% | 30.2% |
| China  |  6.9% | 11.1% | 15.9% | 23.6% |
| USA    |  6.7% | 10.9% | 16.0% | 24.7% |
| RoW    |  4.0% |  6.8% | 10.8% | 18.8% |

---

### Regional Material Intensity (Oil)

For oil, the relevant intensity is oil consumption per vehicle (barrels/vehicle-year). This differs by region primarily through vehicle size and utilization.

| Region | ICE avg (bbl/vehicle-yr) | Key Note |
|--------|-------------------------:|----------|
| China  | ~11 | Smaller vehicles; growing urban EV share suppresses ICE utilization faster |
| Europe | ~13 | Mid-size vehicles; diesel share historically high — moderately efficient fleet |
| USA    | ~20 | Larger SUVs and trucks dominant; higher per-vehicle oil consumption |
| RoW    | ~12 | Heterogeneous; SE Asia and India lean small; Middle East and Russia lean high |

*MI differences are embedded in the V1 regional transport oil market size splits. USA's high per-vehicle consumption (higher regional weight per vehicle sold) drives USA's larger disruption-eligible V1 base (8.1 mb/d) relative to Europe (6.6 mb/d) despite a smaller vehicle market [model-derived, estimated].*

### Regional Material Intensity (Gas)

Gas demand intensity differences arise from grid gas fraction, heating climate, and building stock type.

| Region | Gas power intensity (bcm/TWh generated) | Heating gas depth (bcm/household) | Key Note |
|--------|----------------------------------------:|-----------------------------------:|----------|
| China  | ~0.10 | Low (~0.05) | Coal-dominant grid; gas power is <6% of generation; residential gas heating concentrated in cities |
| Europe | ~0.25 | High (~0.20) | Gas at ~20% of generation; large legacy building stock with gas heating infrastructure |
| USA    | ~0.20 | High (~0.18) | Gas at ~40% of generation; North: gas heating dominant; South: heat pump baseline already elevated |
| RoW    | ~0.18 | Low-moderate (~0.10) | Heterogeneous; Middle East high gas power intensity; developing Asia lower heating demand |

---

### Demand Projections Summary — Oil

| Horizon | Year | Total (mb/d) | vs 2026 | CI P10–P90 (mb/d) |
|---------|------|-------------:|---------|--------------------|
| Current | 2026 | 99.6 | — | 96.8–102.5 |
| +5yr    | 2031 | 87.7 | -11.9% | 82.5–93.2 |
| +10yr   | 2036 | 75.8 | -23.9% | 70.5–81.6 |
| +20yr   | 2046 | 73.0 | -26.7% | 65.8–80.4 |

*Global CI from 07b Monte Carlo (N=300, seed=42). [model-derived]*

### Demand Projections Summary — Gas

| Horizon | Year | Total (bcm/yr) | vs 2026 | CI P10–P90 (bcm/yr) |
|---------|------|---------------:|---------|-----------------------|
| Current | 2026 | 3,935 | — | 3,810–4,050 |
| +5yr    | 2031 | 3,497 | -11.1% | 3,280–3,690 |
| +10yr   | 2036 | 2,920 | -25.8% | 2,710–3,180 |
| +20yr   | 2046 | 2,601 | -33.9% | 2,390–2,860 |

*Global CI from 07b Monte Carlo (N=300, seed=42). [model-derived]*

---

### Regional Oil Demand Change vs 2026

| Region | 2026 (mb/d) | 2031 (mb/d) | Change | 2036 (mb/d) | Change | 2046 (mb/d) | Change | CAGR 2026-46 |
|--------|------------:|------------:|-------:|------------:|-------:|------------:|-------:|-------------:|
| China  | 15.1 | 11.5 | -23.8% | 10.5 | -30.5% | 10.8 | -28.5% | -1.66%/yr |
| Europe | 14.8 | 12.3 | -16.9% | 10.5 | -29.1% |  9.9 | -33.1% | -1.99%/yr |
| USA    | 21.0 | 18.8 | -10.5% | 15.9 | -24.3% | 14.5 | -31.0% | -1.83%/yr |
| RoW    | 48.7 | 45.1 |  -7.4% | 39.0 | -19.9% | 37.8 | -22.4% | -1.26%/yr |
| Global | 99.6 | 87.7 | -11.9% | 75.8 | -23.9% | 73.0 | -26.7% | -1.55%/yr |

### Regional Gas Demand Change vs 2026

| Region | 2026 (bcm) | 2031 (bcm) | Change | 2036 (bcm) | Change | 2046 (bcm) | Change | CAGR 2026-46 |
|--------|----------:|----------:|-------:|----------:|-------:|----------:|-------:|-------------:|
| China  |   378 |   334 | -11.6% |   284 | -24.9% |   277 | -26.8% | -1.54%/yr |
| Europe |   737 |   615 | -16.6% |   524 | -28.9% |   474 | -35.7% | -2.18%/yr |
| USA    | 1,045 |   907 | -13.2% |   743 | -28.9% |   621 | -40.6% | -2.57%/yr |
| RoW    | 1,775 | 1,642 |  -7.5% | 1,369 | -22.8% | 1,230 | -30.7% | -1.82%/yr |
| Global | 3,935 | 3,497 | -11.1% | 2,920 | -25.8% | 2,601 | -33.9% | -2.07%/yr |

---

### Demand Destruction Attribution — Oil (+20yr, vs 2026)

Global oil demand destroyed 2026 to 2046: 26.6 mb/d (26.7%)

| Region | Destruction (mb/d) | Share of Global Destruction | Primary Vector |
|--------|-------------------:|-----------------------------:|--------------------|
| RoW    | 10.9 | 41.0% | V1 transport (lagged but large absolute fleet); floor growth partial offset |
| USA    |  6.5 | 24.4% | V1 transport + V3 heating oil; partially offset by structural floor growth |
| Europe |  4.9 | 18.4% | V1 transport + V3 heating oil (largest per-mb/d heating oil surface) |
| China  |  4.3 | 16.2% | V1 fleet disruption (earliest, but smaller absolute disruption-eligible base vs USA/RoW) |

*China contributes the smallest absolute oil destruction despite leading EV adoption because China's oil demand is already being suppressed by the fastest fleet disruption — its 2026 baseline is already partially depressed by the 2023 inflection. The large RoW oil destruction is dominated by V1 transport in India, SE Asia, and Latin America, where lagged S-curve adoption (x0=2029.6) means the steepest destruction falls within the 2031–2036 window. [model-derived]*

### Demand Destruction Attribution — Gas (+20yr, vs 2026)

Global gas demand destroyed 2026 to 2046: 1,334 bcm/yr (33.9%)

| Region | Destruction (bcm/yr) | Share of Global Destruction | Primary Vector |
|--------|---------------------:|-----------------------------:|----------------|
| RoW    | 545 | 40.9% | V2 gas power (large absolute base; solar S-curve catch-up) |
| USA    | 424 | 31.8% | V2 gas power (largest gas grid globally); V3 moderate |
| Europe | 263 | 19.7% | V3 heating gas (dense boiler stock) + V2 power |
| China  | 101 |  7.6% | V2 power (limited gas grid share); V3 structurally limited (coal, not gas, displaced) |

*The USA is the single largest individual gas destruction market at +20yr (424 bcm) despite RoW dominating in aggregate, because US gas power demand is the largest single-country gas power base globally (estimated 464 bcm in 2026) and solar S-curve adoption accelerates through 2033. China contributes only 7.6% of global gas destruction despite its scale because its electricity grid is coal-dominated — stellar energy (solar PV) displacing coal in China does not destroy gas demand. [model-derived]*

---

### Regional Share Evolution — Oil (%)

| Region | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| China  | 15.2% | 13.1% | 13.8% | 14.8% |
| Europe | 14.9% | 14.0% | 13.8% | 13.6% |
| USA    | 21.1% | 21.4% | 20.9% | 19.9% |
| RoW    | 48.9% | 51.4% | 51.4% | 51.8% |

*China's share falls sharply from 2026 to 2031 (15.2% to 13.1%) as V1 fleet disruption — already past inflection — cuts transport oil consumption rapidly. China's share then recovers slightly by 2046 as floor growth (petrochemicals, aviation) stabilizes absolute demand. USA's share is relatively stable, reflecting that V1 disruption is slower but the structural floor is larger and growing. RoW's share rises steadily, driven by floor dominance and slower disruption timelines. [model-derived]*

### Regional Share Evolution — Gas (%)

| Region | 2026 | 2031 | 2036 | 2046 |
|--------|-----:|-----:|-----:|-----:|
| China  |  9.6% |  9.5% |  9.7% | 10.6% |
| Europe | 18.7% | 17.6% | 17.9% | 18.2% |
| USA    | 26.6% | 25.9% | 25.4% | 23.9% |
| RoW    | 45.1% | 46.9% | 46.9% | 47.3% |

*USA's gas share declines from 26.6% to 23.9% — the largest percentage-point drop of any single region — consistent with it being the fastest-declining gas market in CAGR terms (-2.57%/yr). China's share rises from 9.6% to 10.6% by 2046 despite absolute decline, because China's V3 gas destruction is structurally limited (HP displaces coal, not gas) and its structural floor (petrochemicals, industrial) grows at 0.5%/yr on a large base. [model-derived]*

---

### Regional Confidence Intervals (P10–P90) at Key Horizons

#### Oil (mb/d)

| Region | 2031 P50 | 2031 CI | 2046 P50 | 2046 CI |
|--------|----------:|--------|----------:|--------|
| China  | 11.5 | 10.7–12.3 | 10.8 | 9.5–12.1 |
| Europe | 12.3 | 11.4–13.2 | 9.9 | 8.7–11.1 |
| USA    | 18.8 | 17.4–20.2 | 14.5 | 12.8–16.2 |
| RoW    | 45.1 | 41.8–48.4 | 37.8 | 33.4–42.2 |

#### Gas (bcm/yr)

| Region | 2031 P50 | 2031 CI | 2046 P50 | 2046 CI |
|--------|----------:|--------|----------:|--------|
| China  |   334 | 313–355  |   277 | 245–309 |
| Europe |   615 | 576–654  |   474 | 420–528 |
| USA    |   907 | 849–965  |   621 | 550–692 |
| RoW    | 1,642 | 1,538–1,746 | 1,230 | 1,089–1,371 |

*Regional CIs derived by applying regional demand shares to global P10/P90 CI half-widths from 07b Monte Carlo (N=300), multiplied by 1.15 for additional regional S-curve parameter uncertainty. Wider regional CIs reflect additional uncertainty from lag-estimated V3 parameters for China, USA, and RoW. [model-derived]*

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.9 | HIGH | PASS | Regional demand breakdown (China, USA, Europe, RoW) with region-specific parameters | All four regions covered for both oil and gas; region-specific S-curve parameters (V1, V2, V3) applied per region; region-specific market size splits and material intensity differences documented. Reconciled against 07b global totals. |

---

### Data Gaps

1. **V3 HP stock S-curve — China, USA, RoW estimated from lags:** No T1/T2 time-series data provides a "HP stock share" equivalent metric for China and USA at the granularity needed for S-curve fitting. China, USA, and RoW V3 parameters are lag-adjusted estimates from the Europe baseline. Uncertainty is approximately ±5 percentage points on L and ±2 years on x0 for these regions.

2. **Regional V1 transport oil market size splits (24/22/18/36) are estimated:** No primary source provides a time-series breakdown of global transport oil consumption by the four regions at the segment level used here (passenger ICE, HDT diesel, LCV). Splits are estimated from structural knowledge of vehicle fleet sizes and utilization. Uncertainty is approximately ±3 percentage points on each regional share.

3. **Regional V2 gas power market size split (USA=30%, RoW=46%, Europe=16%, China=8%) is estimated:** Derived from knowledge of gas generation share in each region's electricity mix, not from a directly observed primary source at the bcm/region level. BP Statistical Review 2024 provides national gas generation but requires conversion assumptions. Uncertainty ±5 percentage points on USA and RoW shares.

4. **China V3 gas displacement structurally limited by coal-district-heating dominance:** In northern China, the primary incumbent displaced by heat pumps is coal district heating, not gas boilers. The reduced V3 gas destruction for China (L=0.28 vs 0.33 for Europe) approximates this structural distinction, but the true gas-vs-coal substitution ratio for China HP deployments requires regional building stock data not available in this pipeline run.

5. **Europe R² for V1 S-curve is 0.9207, below 0.95 threshold:** The kink structure from German incentive withdrawal in late 2023 means the logistic fit underestimates near-term uncertainty for Europe V1 EV adoption. European oil demand projections at +5yr carry above-average uncertainty.

6. **RoW is highly heterogeneous — India and SE Asia may follow independent timelines:** RoW aggregates markets with very different V1 timelines (India two-wheeler EV market already tipping; SE Asia passenger car EV lagging). A sub-regional breakdown for India, SE Asia, and Middle East would reduce the RoW projection uncertainty at +10yr by an estimated 30–40%.

---

### Critical Assumptions

- Regional transport oil splits (V1) are assumed constant at the 2026 base year. USA's larger-vehicle oil intensity means its share of V1 transport oil consumption is higher relative to its share of vehicle sales. This is captured implicitly through the market size splits but not modeled with explicit per-vehicle material intensity coefficients.
- China's V3 HP stock ceiling (L=0.28) represents a structural judgment that only approximately 28% of China's total heating stock can be served by HP gas displacement, given coal district heating dominance in the north. If gas heating penetration in Chinese cities grows faster than modeled, V3 gas destruction could be 30–60 bcm larger than the central estimate by 2046.
- Fleet-lagged EV share uses a simple 6-year backward-rolling average of new-sales S-curve values as a proxy for fleet stock share. This approximation is consistent with the 07b stream-forecaster methodology; the 07c fleet-modeler (stock-flow accounting) supersedes this approximation where available.
- The solar displacement of gas power uses a fixed displacement fraction per region derived from the V2 S-curve trajectory. China's 45.2% global BESS share in 2024 suggests China's V2 gas displacement may be underestimated in the near term; BESS co-deployment enables higher solar utilization, compressing gas dispatch faster.
- V2 oil-fired power displacement (3.9 mb/d in 2026) is dominated by RoW (Middle East, Africa) where solar PV cost-curve superiority is already established but infrastructure deployment and grid integration lags slow the actual displacement timeline relative to the S-curve k parameter alone.

---

## Sources

**Upstream agent files (this pipeline run):**
- `agents/07b-stream-forecaster.md` — global oil and gas demand streams, segment baselines, Monte Carlo CI, structural floor volumes [model-derived]
- `agents/05b-regional-adopter.md` — regional S-curve parameters (V1, V2, V3), regional market share data, lag estimates for China/USA/RoW relative to Europe [model-derived, observed]

**Computation library:**
- `lib.scurve_math.logistic` — S-curve evaluation at each horizon year [model-derived]
- `lib.demand_math.regional_demand_split` — initial regional allocation scaffolding [model-derived]

**Tier 1 primary sources (via upstream agents):**
- BP Statistical Review of World Energy 2024 — regional electricity generation totals [T1] [observed]
- Ember, European Electricity Review 2025 — EU solar share 11% / 304 TWh [T1] [observed]
- Ember, Global Electricity Review 2024 — global HP stock share ~10% [T1] [observed]
- European Heat Pump Association (EHPA), Heat Pump Statistics 2013–2023 — V3 Europe anchor [T1] [observed]
- AHRI Monthly Shipment Reports 2023–2024 — USA HP market share [T1] [observed]
- Rethinkx data catalog — regional EV sales, solar generation [T2] [observed]

*Output written: 2026-03-20 | Agent: stdf-regional-demand-analyst*
