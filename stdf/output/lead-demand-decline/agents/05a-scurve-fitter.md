# STDF S-Curve Fitter Agent — Lead Demand Decline (Li-Ion vs. Lead-Acid)

**Agent:** `stdf-scurve-fitter` | **Confidence:** 0.82

**Analysis Date:** 2026-03-20

---

## Agent Reasoning

This is a five-segment S-curve adoption analysis. The market-driven disruption of lead-acid batteries by lithium-ion is not a single market substitution — it operates through five structurally distinct adoption vectors, each with its own S-curve adoption parameters, data density, and inflection timing. Incumbent displacement is driven by cost-curve dynamics (16.81%/yr learning rate from cost-fitter), not policy mandates. The five segments are: (1) BEV share of new passenger vehicle sales (eliminates SLI installations in new ICE vehicles), (2) BEV fleet share (stock displacement drives shrinkage of aftermarket SLI replacement demand), (3) Li-ion share of telecom UPS battery market, (4) Li-ion share of datacenter UPS battery market, and (5) EV electric forklift share of all forklifts (motive power, lead's second-largest non-SLI demand vector). Segments 3, 4, and 5 together constitute the non-SLI portion (37.5% of lead demand); segments 1 and 2 together drive the SLI portion (62.5% of lead demand). Each was fitted independently using `lib.scurve_math.fit_scurve` from observed empirical catalog data.

The BEV fleet share (Segment 2) is the most consequential driver for the 10% lead demand decline question. At 3.0% of the global fleet in 2024, BEV stock displacement is still in the rupture phase. The S-curve inflection for fleet share is modelled at x0 = 2031.77 with L = 80% — meaning the installed base of ICE vehicles (and their SLI replacement demand) does not begin its steepest decline until ~2032. However, the new-vehicle sales share curve (Segment 1, already at 11.96% in 2024, tipping phase) feeds fleet share with a 12-15 year lag (average vehicle lifetime). Both BEV curves require fixed-L fitting because all observed data points fall below the inflection: free-L optimization diverges to unrealistic values when the entire historical series is pre-inflection (confirmed by prior memory: `feedback_free_l_divergence.md`). L was fixed at 80% for fleet and 85% for new-vehicle sales, reflecting the probability that a small residual of ICE vehicles persists in specialized or low-income markets post-2040.

The non-SLI segments (telecom UPS, datacenter UPS, forklift) are further advanced. Notably, LFP cells manufactured for stellar energy storage (BESS applications) share production lines with telecom and datacenter UPS cells, and this shared-factory volume is a structural contributor to the 16.81%/yr learning rate that the cost-fitter empirically derived: all are in the rapid_growth phase (33-37% market share for telecom/datacenter UPS Li-ion, 65% for EV forklifts). Telecom and datacenter UPS S-curves show inflections in 2024-2025, consistent with tipping-synthesizer's finding that these segments tipped in 2021-2024. The forklift S-curve (free-L converges to L=70.66%, R²=0.935) is post-inflection — the rapid-growth phase peaked around 2019-2020 and the curve is now decelerating toward saturation at ~70% EV share. Within EV forklifts, Li-ion is at ~65% and displacing lead-acid traction batteries, adding a second-order displacement layer within the motive-power vector.

The composite demand model weights SLI (62.5%) and non-SLI (37.5%) S-curve displacement trajectories against the 2026 baseline. The model-derived 10% demand decline crossing is **2028.1** [model-derived], within the 2027.4-2028.8 scenario range. This is a moderate divergence from the tipping-synthesizer's interpolated 2027.5 crossing — 7 months later — explained by the higher non-SLI displacement acceleration visible in the catalog data (telecom Li-ion jumped from 13% to 28% between 2021 and 2022, indicating the 2022 data point was a step-change driven by the 5G infrastructure buildout, not a smooth S-curve trajectory). This step-change means the non-SLI composite in 2026 is already at ~59%, meaning further displacement from this segment is decelerating toward saturation. The bulk of the 10% decline must therefore come from the SLI vector, which is slower and gates the milestone at 2028.

---

## Agent Output

### Key Findings
- **Disruptor technology:** Lithium-ion batteries (LFP chemistry primary)
- **Incumbent technology:** Lead-acid batteries (SLI automotive, VRLA/AGM stationary, traction)
- **Global market share — BEV new vehicle sales:** 11.96% (2024, Rethinkx catalog [T2, observed])
- **Global market share — Li-Ion telecom UPS:** 33.0% (2024, catalog [T2, observed])
- **Global market share — Li-Ion datacenter UPS:** 37.0% (2024, catalog [T2, observed])
- **Global market share — EV forklifts of all forklifts:** 64.9% (2024, catalog [T2, observed])
- **Global market share — BEV fleet share:** 3.0% (2024, catalog [T2, observed])
- **Primary adoption phase (BEV new vehicle sales):** tipping (11.96%, boundary 5-15%)
- **Confidence:** 0.82

---

### S-Curve Parameters — All Segments

#### Segment 1: BEV Share of New Global Passenger Vehicle Sales

This segment is the *flow* metric: new BEV installations eliminate SLI demand from the new-vehicle channel. It is the leading indicator for fleet stock displacement.

- **L (ceiling):** 85.0% — residual ICE vehicles persist in low-income markets and specialty segments post-2035; EU 2035 mandate revision (90% CO2 reduction, not full ban) preserves residual ICE new sales in Europe. Sensitivity range: L=80-90% produces R² variation of <0.001, confirming L-insensitivity at this data density.
- **k (growth rate):** 0.3492
- **x0 (inflection year):** 2028.83
- **R-squared:** 0.9621
- **Data points used:** 15
- **Year span:** 2010–2024
- **L fixed:** Yes — all 15 observations are pre-inflection (max 11.96%); free-L diverges
- **Data source:** Rethinkx catalog `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` [T2, observed]; total vehicle sales denominator from OICA 2010-2024 series [T3, observed]

#### Segment 2: BEV Fleet Share (Global Passenger Car Stock)

This segment is the *stock* metric: the fraction of the total 1.305B vehicle fleet that is BEV. It directly measures what fraction of SLI replacement demand (aftermarket) is eliminated. Fleet share lags new-vehicle sales by ~12-15 years (average vehicle lifetime).

- **L (ceiling):** 80.0% — ICE fleet residual higher than new-vehicle sales residual because the stock turns over more slowly and contains older vehicles purchased prior to cost parity
- **k (growth rate):** 0.4155
- **x0 (inflection year):** 2031.77
- **R-squared:** 0.9979
- **Data points used:** 15
- **Year span:** 2010–2024
- **L fixed:** Yes — 3.0% in 2024, pre-inflection; free-L diverges
- **Data source:** `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Total_Fleet_Global.json` (Rethinkx) [T2, observed]; total fleet denominator from OICA/MarkLines global fleet estimates [T3, observed]

#### Segment 3: Li-Ion Share of Global Telecom UPS Battery Market

- **L (ceiling):** 85.0% — developing-market telecoms retain lead-acid for low-upfront-cost reasons; 15% residual consistent with 2030+ market structure
- **k (growth rate):** 0.3659
- **x0 (inflection year):** 2024.84
- **R-squared:** 0.9620
- **Data points used:** 15
- **Year span:** 2010–2024
- **L fixed:** Yes — 33% in 2024, pre-inflection; conservative ceiling prevents divergence
- **Data source:** `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_Annual_Capacity_Demand_Global.json` and `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_(Lead_Acid)_Annual_Capacity_Demand_Global.json` [T2, observed]
- **Note:** 2022 saw a step-change jump from 13% to 28% Li-ion share, driven by 5G base-station deployment accelerating energy-density requirements. This compresses the S-curve's pre-inflection phase and increases uncertainty on the inflection year estimate.

#### Segment 4: Li-Ion Share of Global Datacenter UPS Battery Market

- **L (ceiling):** 90.0% — datacenters are high-uptime, cost-tolerant buyers; near-complete displacement expected; 10% residual for legacy installed base slow to replace
- **k (growth rate):** 0.2569
- **x0 (inflection year):** 2024.90
- **R-squared:** 0.9797
- **Data points used:** 15
- **Year span:** 2010–2024
- **L fixed:** Yes — 37% in 2024, approaching inflection; free-L sensitivity L=85-95 produces R² variation of 0.002
- **Data source:** `data/datacenter_ups/adoption/Data_Center_Battery_Demand_(Li-Ion)_Annual_Capacity_Demand_Global.json` and `data/datacenter_ups/adoption/Data_Center_Battery_Demand_Annual_Capacity_Demand_Global.json` [T2, observed]

#### Segment 5: EV Electric Forklift Share of All Global Forklift Sales

- **L (ceiling):** 70.66% — free-L converges to 70.66% (post-inflection data available, optimizer stable). ICE forklifts (propane/diesel) retain 29% due to outdoor/heavy-lift applications where electric charging infrastructure is impractical.
- **k (growth rate):** 0.1891
- **x0 (inflection year):** 2009.61
- **R-squared:** 0.9351
- **Data points used:** 15
- **Year span:** 2010–2024
- **L fixed:** No — post-inflection data available from 2019 onward; free-L converges
- **Data source:** `data/forklift/adoption/Forklift_(EV)_Annual_Sales_Global.json` and `data/forklift/adoption/Forklift_Annual_Sales_Global.json` [T2, observed]
- **Note:** This measures EV forklifts vs. all forklifts (EV includes both lead-acid traction and Li-ion traction batteries). Li-ion within EV forklifts estimated at ~65% (2024) based on industry reports [T3, Interact Analysis 2024], adding a second-order displacement layer not captured in the primary metric. R²=0.9351 is below the 0.95 threshold — confidence interval widened accordingly.

---

### Projections

#### Segment 1: BEV New Vehicle Sales Share (L=85%, k=0.3492, x0=2028.83)

| Horizon | Year | Market Share (%) | Confidence Interval |
|---------|------|-----------------|---------------------|
| Current | 2026 | 20.6 | — |
| 5-year  | 2031 | 57.9 | [55.7, 59.9] |
| 10-year | 2036 | 78.6 | [76.0, 80.5] |
| 20-year | 2046 | 84.8 | [84.5, 84.9] |

- **80% absolute share year:** 2036.8 [model-derived]

#### Segment 2: BEV Fleet Share (L=80%, k=0.4155, x0=2031.77)

| Horizon | Year | Market Share (%) | Confidence Interval |
|---------|------|-----------------|---------------------|
| Current | 2026 | 6.7 | — |
| 5-year  | 2031 | 33.7 | [32.7, 34.6] |
| 10-year | 2036 | 68.2 | [65.3, 70.6] |
| 20-year | 2046 | 79.8 | [79.5, 79.9] |

- **64% fleet share (80% of L) year:** 2035.1 [model-derived]

#### Segment 3: Li-Ion Telecom UPS Share (L=85%, k=0.3659, x0=2024.84)

| Horizon | Year | Market Share (%) | Confidence Interval |
|---------|------|-----------------|---------------------|
| Current | 2026 | 44.6 | — |
| 5-year  | 2031 | 76.9 | [74.1, 79.1] |
| 10-year | 2036 | 83.6 | [82.4, 84.2] |
| 20-year | 2046 | 85.0 | [84.9, 85.0] |

- **80% absolute share year:** 2032.4 [model-derived]

#### Segment 4: Li-Ion Datacenter UPS Share (L=90%, k=0.2569, x0=2024.90)

| Horizon | Year | Market Share (%) | Confidence Interval |
|---------|------|-----------------|---------------------|
| Current | 2026 | 50.1 | — |
| 5-year  | 2031 | 74.5 | [71.2, 77.3] |
| 10-year | 2036 | 85.1 | [82.7, 86.7] |
| 20-year | 2046 | 89.6 | [89.1, 89.8] |

- **80% absolute share year:** 2033.0 [model-derived]

#### Segment 5: EV Forklift Share (L=70.66%, k=0.1891, x0=2009.61)

| Horizon | Year | Market Share (%) | Confidence Interval |
|---------|------|-----------------|---------------------|
| Current | 2026 | 68.2 | — |
| 5-year  | 2031 | 69.4 | [68.5, 70.0] |
| 10-year | 2036 | 70.2 | [69.7, 70.4] |
| 20-year | 2046 | 70.6 | [70.5, 70.6] |

- **Saturation note:** Approaching ceiling of 70.66%. Marginal lead-acid displacement in motive power from this point comes from Li-ion within EV forklifts (second-order layer, not fitted here due to sparse T3-only data).

---

### Composite Lead Demand Decline Model

The composite demand model weights SLI displacement (BEV fleet share, 62.5% of lead demand) and non-SLI displacement (telecom + datacenter + forklift S-curves, weighted 33%/17%/50% within the 37.5% non-SLI bucket) to produce a demand index relative to the 2026 baseline.

**Formula:** `Demand(t) = 1 − 0.625 × SLI_displacement(t)/100 − 0.375 × NonSLI_composite(t)/100`

| Year | SLI Displacement | Non-SLI Displacement | Demand vs. 2026 | Lead Demand Decline |
|------|-----------------|----------------------|-----------------|---------------------|
| 2024 | 3.0% | 51.8% | 107.0% | +7.0% (above 2026) |
| 2026 | 6.7% | 59.5% | 100.0% | baseline |
| 2027 | 9.7% | 63.0% | 95.6% | −4.4% |
| 2028 | 13.8% | 66.2% | 90.5% | −9.5% |
| **2028.1** | **14.0%** | **66.3%** | **90.0%** | **−10.0% [milestone]** |
| 2029 | 19.2% | 68.8% | 84.6% | −15.4% |
| 2030 | 25.9% | 71.0% | 77.8% | −22.2% |
| 2032 | 41.9% | 74.1% | 62.6% | −37.4% |
| 2035 | 63.4% | 76.7% | 43.0% | −57.0% |
| 2040 | 77.5% | 78.1% | 30.3% | −69.7% |

**10% demand decline milestone: 2028.1 [model-derived]**

**Scenario range:**
| Scenario | BEV Fleet Parameters | 10% Decline Year |
|----------|---------------------|-----------------|
| Optimistic | L=85%, k=0.45, x0=2029.8 | 2027.4 |
| Primary | L=80%, k=0.4155, x0=2031.8 | 2028.1 |
| Conservative | L=75%, k=0.35, x0=2033.8 | 2028.8 |
| NEVI delay | L=80%, k=0.30, x0=2033.8 | 2028.6 |

---

### Adoption Phase

#### Primary metric: BEV share of new global passenger vehicle sales
- **Current phase:** tipping
- **Phase justification:** 11.96% market share in 2024 [T2, observed]; boundary is 5-15% for tipping phase
- **Completion year (80% absolute):** 2036.8 [model-derived]

#### Summary by segment:

| Segment | 2024 Share | Phase |
|---------|-----------|-------|
| BEV new vehicle sales | 12.0% | tipping |
| BEV fleet stock | 3.0% | rupture |
| Li-Ion telecom UPS | 33.0% | rapid_growth |
| Li-Ion datacenter UPS | 37.0% | rapid_growth |
| EV forklift (all) | 64.9% | rapid_growth |

---

### Upstream Discrepancies

1. **10% demand decline year: this model 2028.1 vs. tipping-synthesizer 2027.5.** Difference of ~7 months. The tipping-synthesizer used L=90, k=0.22, x0=2028 for non-SLI and L=80, k=0.25, x0=2029 for SLI — parameters derived analytically rather than from catalog data. This model's S-curve parameters for non-SLI are fitted from the catalog and find faster non-SLI displacement already underway (telecom at 33% in 2024 vs. tipping-synthesizer's implied ~25-28% at 2026). The consequence is that the non-SLI bucket is already near saturation by 2028, contributing less incremental displacement than the tipping-synthesizer model — the 10% milestone is therefore more dependent on SLI, which is slower, shifting the crossing to 2028.1. Both models agree on the order of magnitude (2027-2028 range). The difference is not materially significant for the user's question ("when will demand drop 10%"); the answer from both models is "2027-2028."

2. **Non-SLI S-curve shape: inflection at 2024-2025 vs. tipping-synthesizer's x0=2028.** Catalog data shows telecom Li-ion had a step-change in 2022 (13% to 28%) and datacenter has been on a smooth S-curve with x0~2025. The tipping-synthesizer used x0=2028 for non-SLI, which appears to underestimate how far advanced non-SLI displacement already is. The 2022 telecom step-change is the likely driver of this discrepancy — it was not visible to the tipping-synthesizer's analytical model.

3. **BEV fleet share phase: this model (rupture, 3.0%) vs. tipping-synthesizer (implied further along).** The tipping-synthesizer's composite demand trajectory shows 2024 demand at 111.6% of 2026 (demand still growing), which this model confirms (2024 = 107% of 2026 baseline). Consistent.

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 4.1 | CRITICAL | PASS | S-curve model required (no straight-line projection) | All projections use logistic f(t)=L/(1+exp(-k(t-x0))) fitted with scipy via lib.scurve_math; no straight-line projection anywhere |
| 4.2 | HIGH | PASS | Current market share with source | BEV new vehicle sales 11.96% (2024, Rethinkx T2 observed); BEV fleet 3.0% (2024, Rethinkx T2 observed); telecom UPS 33.0% (2024, catalog T2 observed); datacenter UPS 37.0% (2024, catalog T2 observed); EV forklift 64.9% (2024, catalog T2 observed) |
| 4.3 | HIGH | PASS | Adoption phase classification | tipping (BEV new vehicles 11.96%, 5-15% boundary); rupture (BEV fleet 3.0%, 2-5% boundary); rapid_growth (telecom 33%, datacenter 37%, forklift 65%, all 15-80%) |

---

### Data Gaps

1. **Total global new vehicle sales denominator (T3 only for post-2020).** OICA global vehicle production data used for 2010-2024; 2020-2024 values are T3 web estimates. Uncertainty on total sales denominator is ±2%, translating to ±0.2 percentage points on the BEV market share calculation — not material.
2. **Telecom UPS 2022 step-change.** The Li-ion share jumped from 13.0% (2021) to 28.0% (2022) — a 15 percentage point single-year jump inconsistent with smooth S-curve behavior. This may reflect a data break in the catalog series (methodology change, geographic scope change) rather than a real-market step-change, or it may reflect concentrated 5G base-station deployment in that specific year. The S-curve fit accommodates this as an observed outlier but R² = 0.962 reflects this imperfect fit. Widen confidence intervals for telecom UPS projections.
3. **Li-ion within EV forklifts — T3 only.** No T1 or T2 source provides Li-ion's share within EV forklifts. Interact Analysis (T3) cited 65% (2024). This second-order displacement layer adds incremental non-SLI lead demand reduction not captured in the primary EV forklift S-curve. If Li-ion within EV forklifts reaches 85% by 2030 (S-curve continuation from 65%), the forklift lead-demand share declines further within the already-plateauing EV share figure. This is a conservative gap — actual non-SLI displacement may be slightly faster than the model implies.
4. **BEV fleet share denominator: total global vehicle fleet.** Estimated from OICA/MarkLines at 1.305B in 2024 [T3]. Uncertainty on total fleet: ±3%, translating to ±0.09 pp on fleet share — not material.
5. **LFP SLI aftermarket substitution (Segment not separately fitted).** The tipping-synthesizer noted LFP SLI as a direct lead-acid replacement in the aftermarket channel (cost parity in USA 2027-2028). No empirical S-curve data exists for this sub-segment — it is captured indirectly by the BEV fleet share curve's ceiling (L=80% reflects BEV displacement + some LFP SLI aftermarket penetration combined). A separate LFP SLI aftermarket S-curve would require post-2027 sales data not yet available.

---

## Sources

- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — Rethinkx, 2010–2024 [T2, observed]
- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Total_Fleet_Global.json` — Rethinkx, 2010–2024 [T2, observed]
- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_China.json` — Rethinkx, 2010–2024 [T2, observed]
- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Europe.json` — Rethinkx, 2010–2024 [T2, observed]
- `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_USA.json` — Rethinkx, 2010–2024 [T2, observed]
- `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_Annual_Capacity_Demand_Global.json` — Database, 2010–2025 [T2, observed]
- `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_(Lead_Acid)_Annual_Capacity_Demand_Global.json` — Database, 2010–2025 [T2, observed]
- `data/datacenter_ups/adoption/Data_Center_Battery_Demand_(Li-Ion)_Annual_Capacity_Demand_Global.json` — Database, 2010–2025 [T2, observed]
- `data/datacenter_ups/adoption/Data_Center_Battery_Demand_Annual_Capacity_Demand_Global.json` — Database, 2010–2025 [T2, observed]
- `data/forklift/adoption/Forklift_(EV)_Annual_Sales_Global.json` — Database, 2010–2024 [T2, observed]
- `data/forklift/adoption/Forklift_Annual_Sales_Global.json` — Database, 2010–2024 [T2, observed]
- `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — Rethinkx, 2010–2024 [T2, observed]
- OICA (Organisation Internationale des Constructeurs d'Automobiles) — Global vehicle production and fleet estimates [T3, observed], retrieved 2026-03-20
- Interact Analysis (2024) — Li-ion share within EV forklifts [T3, observed]
- Upstream: `output/lead-demand-decline/agents/04d-tipping-synthesizer.md` — tipping year, segment weights, S-curve provisional parameters
- Upstream: `output/lead-demand-decline/agents/02b-cost-fitter.md` — Li-ion learning rate 16.81%/yr, SLI parity years
- Computation: `lib.scurve_math.fit_scurve` — all S-curve fitting
- Computation: `lib.scurve_math.project_scurve` — all forward projections
- Computation: `lib.scurve_math.classify_phase` — phase classification
- Computation: `lib.scurve_math.completion_year` — 80% completion year estimates
- Computation: `scipy.optimize.brentq` — 10% demand decline crossing year (2028.1)
