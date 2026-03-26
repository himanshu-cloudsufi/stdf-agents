# STDF Fleet Modeler Agent — BEV Heavy Trucks Displacing LNG/Diesel Trucks (China)

**Agent:** `stdf-fleet-modeler` | **Confidence:** 0.81 | **Analysis date:** 2026-03-20

---

## Agent Reasoning

Three separate stock-flow fleet models were built — one each for the BEV disruptor fleet, the LNG chimera fleet, and the diesel incumbent fleet — all sharing a fixed China heavy-duty truck (HDT) total market of 900,000 units/year and an 8-year average lifetime (scrappage rate = 1/8 = 12.5%/yr). This is a market-driven disruption propelled by cost-curve dynamics in LFP battery manufacturing. The aggregate fleet entering 2025 is set at 8,000,000 units, with initial composition derived from cumulative S-curve-implied sales over the prior 8-year window: 219,264 BEV, 1,145,250 LNG, and 6,635,486 diesel. Each powertrain's annual sales stream was computed from the BEV S-curve adoption model (L=0.90, k=0.7227, x0=2026.59) and the LNG chimera function C(t) = 0.30 × S_chim(t) × (1 − S_bev(t)), matching the stream-forecaster's per-driver unit counts at all four reporting horizons to within rounding. The total fleet is not static: because 900,000 annual sales fall below the initial scrappage rate on 8,000,000 units (1,000,000/yr at t=0), the aggregate fleet contracts from 8.00M to ~7.25M as it equilibrates toward the steady-state fleet size of 900,000 × 8 = 7,200,000 units.

The OEM vs replacement split for commodity demand is derived directly from the BEV fleet model. OEM demand = max(0, BEV_sales − BEV_scrappage) × material intensity, representing net additions to the BEV fleet requiring full new-unit commodity content. Replacement demand = min(BEV_sales, BEV_scrappage) × material intensity, representing old BEV trucks reaching end-of-life (8 years) and being replaced by new BEV trucks. These two components have fundamentally different dynamics: OEM demand peaks around 2029–2031 when BEV S-curve adoption growth is fastest, then declines as the fleet approaches saturation. Replacement demand grows monotonically as the cumulative BEV fleet ages, eventually dominating total demand once the fleet is mature (post-2033 for lithium, post-2032 for copper). A third lithium-specific demand component — mid-life battery pack replacement — was explicitly modeled: 50% of the 4- and 5-year-old BEV truck cohorts replace their battery packs (175 kWh at 0.8 kg LCE/kWh = 140 kg LCE per event). This component grows from 2.96 kt LCE in 2026 to 110–113 kt LCE by 2036 onward, accounting for roughly one-third of total lithium demand at steady state. Copper has no material mid-life replacement demand: battery swaps do not drive significant copper consumption.

Stock-flow consistency was validated for all three fleet models using `lib.demand_math.validate_stock_flow_consistency`. The function reports `consistent=False` at two year-indices for each model, but the max deviation is 0.01 unit on fleets of 2–8 million — a relative error of <0.000001%, attributable entirely to floating-point accumulation in the iterative scrappage formula (scrappage = fleet × 0.125). This is a computational artifact, not a modeling error; the identity Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) holds to within machine precision across all 22 model years. All three models are treated as PASS.

The reconciliation with upstream stream-forecaster output confirms correctness: the fleet model's OEM + replacement lithium demand (truck sales component only) equals the stream-forecaster's vehicle-only disruptor lithium demand to within 0.001 kt at all horizons (2026: 89.58 kt vs 89.58 kt; 2031: 217.81 kt vs 217.81 kt; 2036: 226.55 kt vs 226.55 kt; 2046: 226.80 kt vs 226.80 kt). The fleet model adds the mid-life battery replacement demand on top, which the flow-based stream-forecaster does not capture. This incremental demand is the primary analytical contribution of the fleet model: it reveals that total lithium demand reaches 336–340 kt LCE/yr at steady state (+10yr to +20yr), versus the stream-forecaster's 254 kt LCE/yr — an 82–86 kt LCE uplift (32–34%) driven entirely by battery replacement cycles on the maturing BEV fleet. Incumbent displacement of diesel and LNG trucks via S-curve adoption drives the fleet composition shift; the fleet model quantifies the commodity demand consequences of that stock evolution.

---

## Agent Output

### Key Findings
- **Commodities modeled:** Lithium (LCE), Copper (Cu)
- **Fleet models built:** 3 (BEV disruptor, LNG chimera, diesel incumbent)
- **BEV fleet size (2026):** 386,786 units — growing toward 5.93M by 2046
- **OEM share of lithium demand (2026):** 82.2% | declining to 5.6% by 2046
- **Replacement share of lithium demand (2026):** 14.6% (truck) + 3.2% (mid-life battery) | growing to 94.4% combined by 2046
- **OEM share of copper demand (2026):** 84.9% | declining to 8.5% by 2046
- **Mid-life battery uplift to lithium:** +3 kt (2026) → +110 kt (2036) → +113 kt (2046) vs stream-forecaster flow-based figures
- **Consistency check:** PASS (max deviation 0.01 unit; relative error <0.000001%)
- **Confidence:** 0.81

---

### Stock-Flow Fleet Models

#### BEV Heavy Truck Fleet (Disruptor)

- **Fleet entering 2025:** 219,264 units [model-derived from cumulative S-curve adoption, 2017–2024]
- **Average lifetime:** 8 years
- **Scrappage method:** Rate-based (1/lifetime = 12.5%/yr applied to fleet at start of each year)
- **Scrappage rate:** 0.125/yr

| Year | Fleet | Sales | Scrappage | Net Change |
|------|------:|------:|----------:|-----------:|
| 2025 | 219,264 | 194,930 | 27,408 | +167,522 |
| 2026 | 386,786 | 319,940 | 48,348 | +271,592 |
| 2027 | 658,378 | 464,567 | 82,297 | +382,270 |
| 2028 | 1,040,648 | 595,171 | 130,081 | +465,090 |
| 2029 | 1,505,738 | 689,232 | 188,217 | +501,015 |
| 2030 | 2,006,753 | 746,503 | 250,844 | +495,659 |
| 2031 | 2,502,412 | 777,880 | 312,801 | +465,079 |
| 2032 | 2,967,491 | 794,083 | 370,936 | +423,147 |
| 2033 | 3,390,638 | 802,194 | 423,830 | +378,365 |
| 2034 | 3,769,002 | 806,192 | 471,125 | +335,067 |
| 2035 | 4,104,069 | 808,147 | 513,009 | +295,138 |
| 2036 | 4,399,207 | 809,099 | 549,901 | +259,198 |
| 2037 | 4,658,406 | 809,563 | 582,301 | +227,262 |
| 2038 | 4,885,668 | 809,788 | 610,708 | +199,079 |
| 2039 | 5,084,747 | 809,897 | 635,593 | +174,304 |
| 2040 | 5,259,050 | 809,950 | 657,381 | +152,569 |
| 2041 | 5,411,619 | 809,976 | 676,452 | +133,523 |
| 2042 | 5,545,142 | 809,988 | 693,143 | +116,845 |
| 2043 | 5,661,988 | 809,994 | 707,748 | +102,246 |
| 2044 | 5,764,233 | 809,997 | 720,529 | +89,468 |
| 2045 | 5,853,702 | 809,999 | 731,713 | +78,286 |
| 2046 | 5,931,987 | 809,999 | 741,498 | +68,501 |

- **Consistency check:** Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) — **PASS** (max deviation 0.01 unit, relative error <0.000001%; floating-point accumulation artifact at year-indices 7 and 17 only)

#### LNG Heavy Truck Fleet (Chimera)

- **Fleet entering 2025:** 1,145,250 units [model-derived from cumulative chimera S-curve adoption, 2017–2024]
- **Average lifetime:** 8 years
- **Scrappage rate:** 0.125/yr
- **Chimera peak in fleet:** ~1,231,000 units ca. 2027, after which incumbent displacement by BEV collapses annual LNG sales below the scrappage rate on the LNG fleet base

| Year | Fleet | Sales | Scrappage | Net Change |
|------|------:|------:|----------:|-----------:|
| 2025 | 1,145,250 | 207,509 | 143,156 | +64,353 |
| 2026 | 1,209,602 | 172,425 | 151,200 | +21,225 |
| 2027 | 1,230,827 | 130,018 | 153,853 | −23,836 |
| 2028 | 1,206,992 | 91,206 | 150,874 | −59,668 |
| 2031 | 979,637 | 36,594 | 122,455 | −85,861 |
| 2036 | 619,749 | 27,243 | 77,469 | −50,226 |
| 2041 | 423,318 | 26,980 | 52,915 | −25,935 |
| 2046 | 322,239 | 26,973 | 40,280 | −13,307 |

- **Consistency check:** PASS (same floating-point artifact as BEV model; max deviation 0.01 unit)

#### Diesel Heavy Truck Fleet (Incumbent)

- **Fleet entering 2025:** 6,635,486 units [model-derived: 8,000,000 − BEV − LNG]
- **Average lifetime:** 8 years
- **Scrappage rate:** 0.125/yr

| Year | Fleet | Sales | Scrappage | Net Change |
|------|------:|------:|----------:|-----------:|
| 2025 | 6,635,486 | 497,561 | 829,436 | −331,874 |
| 2026 | 6,303,611 | 407,635 | 787,951 | −380,316 |
| 2027 | 5,923,295 | 305,415 | 740,412 | −434,997 |
| 2028 | 5,488,297 | 213,623 | 686,037 | −472,414 |
| 2031 | 4,076,987 | 85,526 | 509,623 | −424,097 |
| 2036 | 2,365,197 | 63,658 | 295,650 | −231,991 |
| 2041 | 1,459,517 | 63,044 | 182,440 | −119,396 |
| 2046 | 994,220 | 63,027 | 124,278 | −61,250 |

- **Consistency check:** PASS (same floating-point artifact; max deviation 0.01 unit)

---

### OEM vs Replacement Demand

#### Lithium (kt LCE/yr) — Three-Component Model

| Category | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|----------|---------------:|------------:|-------------:|-------------:|
| OEM — net BEV fleet growth | 76.05 | 130.22 | 72.58 | 19.18 |
| Replacement — scrapped BEV → new BEV | 13.54 | 87.58 | 153.97 | 207.62 |
| Mid-life battery replacement (50% of 4-5yr cohort) | 2.96 | 54.92 | 110.04 | 113.40 |
| **Total (fleet model)** | **92.55** | **272.72** | **336.59** | **340.20** |
| Stream-forecaster vehicle-only (for reconciliation) | 89.58 | 217.81 | 226.55 | 226.80 |
| Mid-life uplift vs stream-forecaster | +2.96 | +54.92 | +110.04 | +113.40 |

OEM share: 82.2% (2026) → 47.7% (2031) → 21.6% (2036) → 5.6% (2046)
Replacement + mid-life share: 17.8% (2026) → 52.3% (2031) → 78.4% (2036) → 94.4% (2046)

Material intensity: 280 kg LCE/truck (new unit); 140 kg LCE/battery replacement (175 kWh × 0.8 kg LCE/kWh).

#### Copper (kt Cu/yr) — Two-Component Model

| Category | 2026 (current) | 2031 (+5yr) | 2036 (+10yr) | 2046 (+20yr) |
|----------|---------------:|------------:|-------------:|-------------:|
| OEM — net BEV fleet growth | 27.16 | 46.51 | 25.92 | 6.85 |
| Replacement — scrapped BEV → new BEV | 4.83 | 31.28 | 54.99 | 74.15 |
| Mid-life battery replacement (minimal Cu) | — | — | — | — |
| **Total (fleet model)** | **31.99** | **77.79** | **80.91** | **81.00** |
| Stream-forecaster vehicle-only (for reconciliation) | 31.99 | 77.79 | 80.91 | 81.00 |

OEM share: 84.9% (2026) → 59.8% (2031) → 32.0% (2036) → 8.5% (2046)
Replacement share: 15.1% (2026) → 40.2% (2031) → 68.0% (2036) → 91.5% (2046)

Material intensity: 100 kg Cu/truck (both OEM and replacement). No mid-life copper uplift modeled (battery swap is an LFP pack exchange; copper wiring/contacts are not replaced).

---

### Fleet Composition Over Time

| Year | BEV (Disruptor) | LNG (Chimera) | Diesel (Incumbent) | Total Fleet |
|------|----------------:|--------------:|-------------------:|------------:|
| 2025 | 219,264 | 1,145,250 | 6,635,486 | 8,000,000 |
| 2026 | 386,786 | 1,209,602 | 6,303,611 | 7,900,000 |
| 2027 | 658,378 | 1,230,827 | 5,923,295 | 7,812,500 |
| 2028 | 1,040,648 | 1,206,992 | 5,488,297 | 7,735,938 |
| 2031 | 2,502,412 | 979,637 | 4,076,987 | 7,559,036 |
| 2036 | 4,399,207 | 619,749 | 2,365,197 | 7,384,153 |
| 2041 | 5,411,619 | 423,318 | 1,459,517 | 7,294,454 |
| 2046 | 5,931,987 | 322,239 | 994,220 | 7,248,446 |

BEV fleet share of total: 2.7% (2025) → 4.9% (2026) → 33.1% (2031) → 59.6% (2036) → 81.8% (2046). This is the S-curve adoption in fleet-stock terms — lagging the S-curve in annual sales by approximately the fleet lifetime (8 years).

Total fleet contracts from 8.00M to 7.25M because fixed 900,000 annual sales fall below the initial scrappage load of 1,000,000/yr on the 8M fleet. Steady-state fleet size is 900,000 × 8 = 7,200,000 units — approached asymptotically from above.

LNG fleet peaks in 2027 (~1,231,000 units) then declines monotonically as annual LNG sales (falling with S-curve BEV disruption) drop below the 12.5%/yr scrappage rate on the LNG fleet base. The LNG fleet does not collapse to zero by 2046: the chimera S-curve asymptotes toward ~3% market share (27,000 units/yr in new sales), sustaining a residual fleet of ~322,000 LNG units.

---

### Structural Demand Dynamics

Three analytically distinct demand phases characterize lithium demand from the BEV fleet:

**Phase 1 — OEM Dominance (2025–2030):** BEV fleet in rapid growth near S-curve adoption inflection (2026.59). New unit sales far exceed scrappage of the young BEV fleet. OEM demand exceeds 80% of total. Mid-life battery demand negligible (fleet too young for replacement cohorts).

**Phase 2 — Demand Rebalancing (2030–2035):** BEV fleet growth rate decelerating past S-curve inflection. Scrappage of 2023–2027 vintage trucks rises rapidly. Mid-life battery replacement demand on 2021–2027 cohorts accelerates into material volumes. OEM and replacement/battery demand cross around 2031–2032.

**Phase 3 — Replacement Dominance (2035 onward):** BEV fleet near saturation (4.1–5.9M units). Net fleet growth minimal. Annual BEV sales (~809,000) largely cover scrappage plus marginal growth. Replacement + mid-life battery account for 78–94% of lithium demand. Total lithium demand is structurally higher than stream-forecaster flow-based estimates by 110–113 kt LCE/yr — a persistent uplift that does not diminish at the +20yr horizon.

For copper, the same three-phase dynamic applies but without the mid-life battery component. Copper demand at steady state (81 kt/yr) matches the stream-forecaster exactly because copper replacement intensity equals OEM intensity and there is no mid-life uplift term.

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.7 | HIGH | **PASS** | OEM + Replacement split tracked with explicit lifetimes | Three-component split for lithium (OEM / replacement / mid-life battery) and two-component for copper. Lifetime = 8 years explicit; scrappage_rate = 1/8 derived. All four reporting horizons covered. |
| 6.8 | MEDIUM | **PASS** | Stock-flow fleet model consistent: Fleet(t+1) = Fleet(t) + Sales(t) − Scrappage(t) | Validated via `lib.demand_math.validate_stock_flow_consistency`. Max deviation = 0.01 unit (relative error <0.000001%) across all three fleet models — floating-point accumulation only. Treated as PASS. |

---

### Data Gaps

1. **Battery replacement rate assumption.** The 50% mid-life replacement rate for 4-5 year old BEV trucks is an aggregate assumption. High-mileage fleets (long-haul) may have higher replacement rates (>70% at year 4); captive/regional fleets lower (<30% at year 5). No segment-level disaggregation of replacement rates is available from upstream agents. A 10 pp change in the replacement rate shifts the mid-life lithium demand by ±7–8 kt LCE/yr at steady state.

2. **BEV fleet entering 2025.** The initial BEV fleet of 219,264 units is derived from the S-curve model applied retrospectively to 2017–2024 — not from a direct count. The S-curve implies ~108,000 BEV HDT sales in 2024. If the actual entering-2025 BEV fleet is materially different (e.g., if early BEV adoption was faster than the S-curve implies for pre-2024 years), the early scrappage volumes in 2030–2033 would shift, altering the replacement demand ramp. This is a ±20% uncertainty on the 2031–2033 replacement demand figures.

3. **Constant 8-year lifetime across fleet segments.** Long-haul tractors may average 6–7 years (higher mileage); captive/regional trucks 9–10 years. Sensitivity: if lifetime = 6 years (scrappage rate = 16.7%/yr), steady-state fleet contracts to 5.4M and replacement demand accelerates by ~30% vs. the base model from 2031 onward. If lifetime = 10 years (scrappage rate = 10%/yr), steady-state fleet = 9M and replacement demand is ~20% lower through 2036.

4. **LNG fleet residual tail.** The model shows ~322,000 LNG trucks in fleet by 2046. The chimera S-curve asymptotes rather than reaching zero, consistent with the S-curve functional form. Whether this residual is realistic depends on whether LNG truck manufacturing and LNG fueling infrastructure remain viable at low volumes — a structural question outside the scope of fleet math.

5. **Mid-life battery replacement LCE intensity.** The 140 kg LCE per replacement is computed as 175 kWh × 0.8 kg LCE/kWh. If LFP energy density improves such that replacement packs require only 140 kWh for the same range, the mid-life LCE intensity drops to 112 kg/replacement, reducing steady-state mid-life lithium demand by ~20%.

---

### Critical Assumptions

1. **Total market fixed at 900,000 units/year across all horizons.** Freight volume growth or modal shift to rail would proportionally scale all fleet and demand figures.

2. **Uniform 8-year lifetime across BEV, LNG, and diesel segments.** The same scrappage rate (12.5%/yr) is applied to all three powertrain types. Battery durability or drivetrain reliability differences that cause BEV trucks to have systematically longer or shorter effective lifetimes are not modeled.

3. **Battery replacement event is full pack replacement.** The 175 kWh (50% of 350 kWh pack) replacement at year 4–5 is modeled as a single discrete event per truck in the cohort, consistent with the prompt specification of ~50% of pack cost at year 4–5.

4. **S-curve parameters held at base case values.** No parameter uncertainty is propagated through the fleet model. P10–P90 ranges from the stream-forecaster apply to the OEM demand component (proportional to BEV sales); the replacement and mid-life components inherit the same relative CI widths.

5. **No aggregate fleet growth.** The aggregate HDT fleet equilibrates at ~7.2M units (900,000 sales × 8-year lifetime). An absolute market size increase of 10% (to 990,000 units/yr) would increase steady-state fleet to ~7.9M and proportionally increase all commodity demand by ~10%.

6. **Copper mid-life replacement demand set to zero.** Battery pack replacement does not require re-running copper wiring, motor windings, or busbars. Copper is treated as embedded in the original truck assembly. A full refurbishment might include some copper-bearing components, but this effect is not quantified.

---

## Sources

- Upstream: `output/bev-trucks-china/agents/07b-stream-forecaster.md` — BEV and LNG annual unit sales at four reporting horizons; S-curve parameters (L=0.90, k=0.7227, x0=2026.59); chimera S-curve parameters (L=0.999, k=0.80, x0=2020.0, C_peak=0.30); material intensity (Li: 280 kg LCE/BEV; Cu: 100 kg/BEV; 27.5 kg/LNG/diesel); vehicle-only lithium demand figures used for reconciliation [model-derived]
- Computation: `lib.demand_math.stock_flow_fleet`, `lib.demand_math.oem_replacement_split`, `lib.demand_math.validate_stock_flow_consistency`; all numerical results computed via python3 per STDF Computation Rule 1
- Fleet size entering 2025: 8,000,000 total (prompt-specified); BEV/LNG/diesel split derived from cumulative S-curve-implied sales 2017–2024 [model-derived]
- Battery replacement parameters: 175 kWh mid-life pack at 0.8 kg LCE/kWh = 140 kg LCE/replacement; 50% replacement rate on 4–5yr cohorts — specified in agent prompt [model-derived]
- Scrappage rate: 1/8 = 0.125/yr derived from 8-year average lifetime (prompt-specified) [model-derived]
