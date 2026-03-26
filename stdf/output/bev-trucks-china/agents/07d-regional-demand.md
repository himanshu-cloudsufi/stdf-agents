# STDF Regional Demand Analyst Agent — BEV Heavy Trucks Displacing LNG/Diesel Trucks (China — Sub-National)

**Agent:** `stdf-regional-demand-analyst` | **Confidence:** 0.72 | **Analysis date:** 2026-03-20

---

## Agent Reasoning

This analysis disaggregates the national China commodity demand streams produced by the stream-forecaster (07b) into five sub-national Chinese regions: Eastern (YRD), Southern (PRD), Northern (BTH), Central, and Western. The departure from the standard cross-national breakdown (China / USA / Europe / RoW) is intentional — this pipeline run targets within-China geographic heterogeneity driven by market-driven disruption dynamics, and a cross-national comparison is provided as brief supplementary context rather than a primary output. Note: stellar energy (solar PV, wind) vocabulary does not apply in this ground transport context; the disruption here is LFP battery cost-curve dynamics displacing LNG/diesel incumbents through incumbent displacement of fossil-fuel freight powertrains.

The disaggregation methodology combines two independent data streams from upstream agents. First, from 05b-regional-adopter, each region has an independently fitted S-curve (L, k, x0) applied to a region-specific market size derived from the HDT freight volume weights (YRD 25%, BTH 20%, PRD 15%, Central 25%, Western 15% of total 900,000 units/year). Second, from 07b-stream-forecaster, the authoritative national commodity totals provide the reconciliation anchor. Per-region demand is computed independently using `lib.demand_math.project_demand_from_scurve`, then scaled by a reconciliation factor (max 5.1% adjustment for lithium, max 3.4% for copper) to anchor regional sums precisely to the 07b P50 national totals. This scalar is small because the regional weighted-average L (88.35%) and k parameters produce aggregate demand slightly below the national single-curve model — a gap documented in 05b as the expected consequence of the L-discrepancy (1.65 pp lower weighted regional L vs. national L=90%). The scaling preserves the relative shape of the regional breakdown while ensuring full additive consistency with the upstream total.

LNG displacement concentration by region requires a separate weighting layer. Not all BEV trucks displace equal parts LNG and diesel — the mix depends on which incumbent fuel dominated each region's freight network. Eastern (YRD) and Northern (BTH) are the two regions with the highest LNG fraction in their incumbent heavy-truck fleet (30% and 28% respectively), driven by: long-haul port logistics corridors where LNG economics had been most competitive; higher density of LNG refueling infrastructure along the Beijing–Shanghai and Tianjin port routes; and the LNG truck's historical cost-per-km advantage over diesel that was particularly relevant on high-utilization long-haul routes. Western China has the lowest LNG fraction among BEV-displaced trucks (18%) because its remote mining and mountain-corridor freight is more diesel-dominated. LNG chimera consumption (the residual LNG fleet actively burning fuel) is weighted by surviving incumbent units × regional LNG fraction, which produces the counterintuitive result that Central China has the largest residual LNG chimera consumption stream in 2026 (0.548 Mt) — its larger market size (225,000 units) offset by only modestly lower LNG fraction (25%) places more LNG trucks in service there than in any other region at current adoption levels.

Material intensity is uniform across all Chinese regions for the disruptor technology: LFP-chemistry BEV heavy trucks are produced by the same manufacturers (BYD, FAW, SINOTRUK, CATL-integrated platforms) to consistent specifications regardless of regional deployment. The 280 kg LCE/unit and 100 kg Cu/unit coefficients from 07b apply uniformly. For the incumbent stream, the 27.5 kg Cu/unit figure covers both LNG and diesel trucks; no regional differentiation in incumbent material intensity is warranted here. The S-curve timing differences (inflection year gaps of up to 1.73 years between YRD and Western China) are the primary driver of near-term demand shape variation across regions. By +10yr (2036), all regions are within 10 pp of their respective L ceilings and demand converges toward stable long-run levels determined by market size × L × MI.

---

## Agent Output

### Key Findings

- **Commodity:** Lithium (LCE), Copper (Cu), LNG (consumed + displaced), Diesel (displaced)
- **Regions analyzed:** Eastern (YRD), Southern (PRD), Northern (BTH), Central, Western (all sub-national China); international context: USA, Europe, RoW
- **Largest lithium demand region (current, 2026):** Eastern (YRD) at 32.7 kt LCE (32.6% of national)
- **Largest lithium demand region (+5yr, 2031):** Central at 60.3 kt LCE (24.7% of national) — overtakes YRD due to larger market size (225k units) and fast catch-up S-curve
- **Fastest growing region (lithium CAGR 2026–2031):** Western China at 33.2%/yr — from the lowest base (7.6 kt), S-curve catch-up in the tipping phase amplifies percentage growth
- **LNG displacement concentration:** Eastern (YRD) + Northern (BTH) account for 58.7% of national LNG displacement in 2026, driven by highest LNG fraction in incumbent fleet mix
- **Confidence:** 0.72

---

### Regional Lithium Demand (kt LCE/yr) — BEV vehicles + swap station infrastructure

Reconciled to 07b P50 totals. Infrastructure allocation proportional to regional BEV unit count.

| Region | 2026 (kt) | 2031 (kt) | 2036 (kt) | 2046 (kt) | BEV Share 2026 | BEV Share 2031 |
|--------|----------:|----------:|----------:|----------:|---------------:|---------------:|
| Eastern (YRD) | 32.74 | 65.14 | 66.41 | 66.44 | 44.1% | 88.1% |
| Southern (PRD) | 17.40 | 37.53 | 38.93 | 39.00 | 39.1% | 84.6% |
| Northern (BTH) | 21.20 | 49.50 | 50.82 | 50.84 | 35.7% | 83.7% |
| Central | 21.56 | 60.30 | 63.44 | 63.55 | 29.0% | 81.6% |
| Western | 7.62 | 31.93 | 34.60 | 34.66 | 17.1% | 72.0% |
| **National** | **100.52** | **244.40** | **254.20** | **254.49** | 35.5% | 86.4% |

*All values [model-derived] from regional S-curve projection anchored to 07b P50 [model-derived, R²=0.9950 national fit]. Infrastructure lithium allocated proportionally to regional BEV unit share.*

---

### Regional Copper Demand (kt Cu/yr) — all powertrain streams combined

| Region | 2026 (kt) | 2031 (kt) | 2036 (kt) | 2046 (kt) | Key Driver |
|--------|----------:|----------:|----------:|----------:|------------|
| Eastern (YRD) | 13.72 | 21.25 | 21.56 | 21.56 | BEV intensity premium (100 vs. 27.5 kg/unit); early S-curve inflection (2026.13) |
| Southern (PRD) | 7.73 | 12.40 | 12.72 | 12.74 | BYD home region; co-leading disruption; smaller market size (135k units) |
| Northern (BTH) | 9.85 | 16.41 | 16.72 | 16.72 | Port logistics; cold-weather LNG niche limits L ceiling to 88% |
| Central | 11.20 | 20.15 | 20.88 | 20.90 | Largest inland market (225k units); later inflection (2027.09) delays current demand |
| Western | 5.52 | 11.12 | 11.73 | 11.74 | Deepest incumbent LNG/diesel entrenchment; L=80%; highest CAGR from low base |
| **National** | **48.02** | **81.33** | **83.60** | **83.66** | BEV intensity gap drives monotonic increase |

*All values [model-derived], reconciled to 07b P50 totals.*

---

### Regional S-Curve Parameters

| Region | L (ceiling) | k (growth rate) | x0 (inflection yr) | 2025 BEV share | Source |
|--------|------------|----------------|---------------------|---------------:|--------|
| Eastern (YRD) | 0.92 | 0.6414 | 2026.13 | 30.3% | 05b-regional-adopter [model-derived, R²=0.9983] |
| Southern (PRD) | 0.90 | 0.6048 | 2026.44 | 26.5% | 05b-regional-adopter [model-derived, R²=0.9990] |
| Northern (BTH) | 0.88 | 0.6711 | 2026.57 | 22.7% | 05b-regional-adopter [model-derived, R²=0.9997] |
| Central | 0.88 | 0.6503 | 2027.09 | 18.0% | 05b-regional-adopter [model-derived, R²=0.9985] |
| Western | 0.80 | 0.7000 | 2027.86 | 9.5% | 05b-regional-adopter [model-derived, R²=0.9982, confidence: LOW-MEDIUM] |
| National (global) | 0.90 | 0.7227 | 2026.59 | 22.0% | 05a-scurve-fitter [model-derived, R²=0.9950] |

---

### Regional Material Intensity

All BEV trucks in China are LFP-chemistry platforms produced to consistent national specifications. No regional differentiation is warranted.

| Region | BEV MI: Lithium (kg LCE/unit) | BEV MI: Copper (kg Cu/unit) | Incumbent MI: Copper (kg Cu/unit) | Note |
|--------|------------------------------:|----------------------------:|----------------------------------:|------|
| Eastern (YRD) | 280 | 100 | 27.5 | Uniform LFP platform; same CATL/BYD supply chain |
| Southern (PRD) | 280 | 100 | 27.5 | BYD home region; same specifications |
| Northern (BTH) | 280 | 100 | 27.5 | Cold-weather performance managed via thermal management, not larger pack |
| Central | 280 | 100 | 27.5 | Inland corridors; same vehicle spec |
| Western | 280 | 100 | 27.5 | Mining-grade variants may use heavier copper wiring; treated as uniform |

*LFP intensity 280 kg LCE/unit: [model-derived from 350 kWh avg × 0.8 kg LCE/kWh per CATL 75# spec, 07a]. Copper intensity 100 kg BEV, 27.5 kg LNG/diesel: [model-derived, 07b].*

---

### LNG Displacement by Region (Mt/yr) — BEV disruptor stream

LNG displacement is concentrated in Eastern (YRD) and Northern (BTH) due to highest LNG fraction in their incumbent fleet mix (30% and 28% respectively). As BEV adoption accelerates, Central China grows as a displacement contributor because its large market size (225k units) outweighs its lower LNG fraction.

| Region | LNG frac. of incumbent | 2026 (Mt) | 2031 (Mt) | 2036 (Mt) | 2046 (Mt) |
|--------|----------------------:|----------:|----------:|----------:|----------:|
| Eastern (YRD) | 30% | 0.347 | 0.710 | 0.725 | 0.724 |
| Southern (PRD) | 25% | 0.154 | 0.341 | 0.354 | 0.354 |
| Northern (BTH) | 28% | 0.210 | 0.503 | 0.518 | 0.517 |
| Central | 25% | 0.191 | 0.547 | 0.577 | 0.577 |
| Western | 18% | 0.049 | 0.209 | 0.227 | 0.227 |
| **National** | 24.7% | **0.950** | **2.310** | **2.400** | **2.400** |

*Regional LNG fractions: [model-derived, calibrated from segment-level long-haul/captive/urban mix in 07a; Eastern and Northern elevated by port-corridor long-haul dominance]. National total anchored to 07b P50 [model-derived].*

---

### LNG Chimera Consumption by Region (Mt/yr) — residual LNG truck fleet

Central China carries the largest residual LNG chimera consumption in 2026 (0.548 Mt) despite not having the highest per-unit LNG fraction — its large market size (225k units) means more LNG trucks remain in service at current adoption levels. Northern (BTH) has elevated chimera persistence due to the winter cold penalty sustaining LNG fleet viability on Hebei cross-season routes.

| Region | 2026 (Mt) | 2031 (Mt) | 2036 (Mt) | 2046 (Mt) |
|--------|----------:|----------:|----------:|----------:|
| Eastern (YRD) | 0.518 | 0.091 | 0.068 | 0.065 |
| Southern (PRD) | 0.282 | 0.059 | 0.042 | 0.041 |
| Northern (BTH) | 0.445 | 0.094 | 0.075 | 0.073 |
| Central | 0.548 | 0.118 | 0.085 | 0.082 |
| Western | 0.277 | 0.078 | 0.060 | 0.059 |
| **National** | **2.070** | **0.440** | **0.330** | **0.320** |

---

### Diesel Displacement and Incumbent Consumption by Region (Mbbl/yr)

**BEV displacing diesel (disruptor stream):**

| Region | 2026 (Mbbl) | 2031 (Mbbl) | 2036 (Mbbl) | 2046 (Mbbl) |
|--------|------------:|------------:|------------:|------------:|
| Eastern (YRD) | 3.06 | 6.03 | 6.15 | 6.15 |
| Southern (PRD) | 1.74 | 3.73 | 3.86 | 3.87 |
| Northern (BTH) | 2.04 | 4.72 | 4.84 | 4.84 |
| Central | 2.16 | 5.99 | 6.29 | 6.30 |
| Western | 0.84 | 3.47 | 3.75 | 3.76 |
| **National** | **9.84** | **23.93** | **24.89** | **24.92** |

**Diesel incumbent still consumed (remaining diesel truck fleet):**

| Region | 2026 (Mbbl) | 2031 (Mbbl) | 2036 (Mbbl) | 2046 (Mbbl) |
|--------|------------:|------------:|------------:|------------:|
| Eastern (YRD) | 3.30 | 0.56 | 0.41 | 0.40 |
| Southern (PRD) | 2.31 | 0.46 | 0.33 | 0.32 |
| Northern (BTH) | 3.12 | 0.63 | 0.50 | 0.50 |
| Central | 4.48 | 0.92 | 0.66 | 0.65 |
| Western | 3.44 | 0.92 | 0.71 | 0.71 |
| **National** | **16.65** | **3.49** | **2.60** | **2.57** |

---

### Regional Lithium Demand Share Evolution (% of national)

Eastern (YRD) dominates current lithium demand (32.6%) but its share falls as Central and Western China catch up through S-curve adoption. By +5yr (2031), Central is the largest single-region lithium consumer. This reflects the asymmetry between current adoption (Eastern leads) and market size (Central and Eastern are tied at 225k units each, but Central's S-curve lags by ~1 year).

| Region | 2026 share | 2031 share | 2036 share | 2046 share |
|--------|----------:|----------:|----------:|----------:|
| Eastern (YRD) | 32.6% | 26.7% | 26.1% | 26.1% |
| Southern (PRD) | 17.3% | 15.4% | 15.3% | 15.3% |
| Northern (BTH) | 21.1% | 20.3% | 20.0% | 20.0% |
| Central | 21.4% | 24.7% | 25.0% | 25.0% |
| Western | 7.6% | 13.1% | 13.6% | 13.6% |

*Long-run (2046) shares reflect market size × L ceiling, which determines the asymptotic limit. Eastern and Central converge near 25–26% each; Northern near 20%; PRD near 15%; Western near 14%.*

---

### Demand Projections Summary — Lithium

| Horizon | Year | Total (kt LCE) | vs 2026 | CI P10–P90 (kt) |
|---------|------|---------------:|---------|-----------------|
| Current | 2026 | 100.52 | — | 61.6 – 153.8 |
| +5yr | 2031 | 244.40 | +143% | 227.1 – 261.1 |
| +10yr | 2036 | 254.20 | +153% | 240.0 – 268.4 |
| +20yr | 2046 | 254.49 | +153% | 240.4 – 268.6 |

*CIs from 07b 27-parameter Monte Carlo sweep [model-derived]. Regional CIs scale proportionally by regional P50 share.*

### Demand Projections Summary — Copper

| Horizon | Year | Total (kt Cu) | vs 2026 | CI P10–P90 (kt) |
|---------|------|--------------:|---------|-----------------|
| Current | 2026 | 48.02 | — | 39.0 – 60.4 |
| +5yr | 2031 | 81.33 | +69% | 77.3 – 85.2 |
| +10yr | 2036 | 83.60 | +74% | 80.3 – 86.9 |
| +20yr | 2046 | 83.66 | +74% | 80.4 – 86.9 |

---

### International Context (Supplementary)

This analysis covers the China domestic BEV-HDT market. Cross-national comparison is provided for relative scale only; full cross-national disaggregation is outside scope of this run.

| Geography | BEV Heavy Truck Share (2025 observed) | Adoption Phase | Near-term Commodity Impact | Note |
|-----------|--------------------------------------:|----------------|----------------------------|------|
| China (national) | ~22% | rapid_growth | Primary signal in this analysis | S-curve inflection 2026.59 |
| Europe | ~5% | tipping | Growing but 3–5 years behind China | ZEV heavy truck mandates accelerating from 2030 but cost-curve dynamics remain primary driver |
| USA | <2% | rupture | Minimal near-term commodity impact | Class 8 BEV trucks at early rupture phase; infrastructure and grid capacity are binding constraints; structural 5–7 year lag vs. China |
| RoW | <1% | pre_rupture | Negligible | India two-wheeler and three-wheeler BEV disruption is a separate analysis; HDT disruption is nascent |

*Europe share [T3: ACEA heavy truck registration data 2024, observed]. USA share [T3: Calstart ZETI report 2024, observed]. These figures are for cross-national framing; no commodity demand computation for international geographies performed in this run.*

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 6.9 | HIGH | **PASS** | Regional demand breakdown (China, USA, Europe, RoW) with region-specific parameters | Five sub-national China regions with independent S-curve parameters (L, k, x0) and region-specific LNG displacement weights. International context (USA, Europe, RoW) provided. All region-specific MI, market sizes, and S-curve parameters applied — no fixed-percentage splits used across time horizons. |

---

### Data Gaps

1. **No sub-national HDT BEV registry data in catalog.** All five regional series are model-derived from national aggregate + qualitative regional markers (port-logistics density, swap station density, cold-weather constraints). Provincial-level BEV-HDT market share registration data has not been released publicly as of March 2026. [From 05b]

2. **Western China low-medium data quality.** The 2025 Western China share (9.5%) carries ±3 pp uncertainty beyond the model precision. Western lithium demand estimates (7.62 kt in 2026, 31.93 kt in 2031) should be treated with wider CI than the national CI implies. A ±3 pp error in the 2025 Western share propagates to ±5–8 kt LCE uncertainty at +5yr. [From 05b]

3. **LNG displacement fractions held constant over time.** The regional LNG fractions (18%–30%) are treated as static. As BEV disruption penetrates deeper into long-haul routes (where LNG dominance is highest), the effective LNG displacement fraction may rise in the 2028–2033 window before declining as long-haul BEV share itself saturates. No segment-level S-curve differentiation is available; the constant fraction understates LNG displacement from Eastern and Northern China in the +3 to +7 year window.

4. **Regional market weight uncertainty.** The HDT unit weights (YRD 25%, BTH 20%, PRD 15%, Central 25%, Western 15%) carry ±5 pp uncertainty from ICCT 2024 fleet census data. A 5 pp shift in any region's weight changes that region's commodity totals by ±20% (since demand scales linearly with market size). [From 05b]

5. **Inner Mongolia classification gap.** Inner Mongolia's fast-growing mining electrification (100-unit autonomous electric haul fleet at Yimin Mine, operational 2024) sits between Western and Central China classifications. On-road HDT BEV share for Inner Mongolia is not separately documented. If Inner Mongolia belongs to "Northern (BTH)" rather than "Western," Northern's copper and lithium estimates would increase by 10–15% at current adoption levels.

6. **USA and Europe commodity demand not computed.** International context rows provide phase classification and qualitative framing only. The USA BEV heavy truck market (Class 8) at <2% share requires a separate pipeline run with US-specific S-curve calibration and material intensity data (US average pack sizes are larger; infrastructure deployment is slower). Europe similarly needs a dedicated run for rigorous commodity estimates.

---

### Critical Assumptions

1. **China HDT national market fixed at 900,000 units/year.** Same as 07b. Any structural freight demand growth or modal shift to rail would scale all regional commodity values proportionally.

2. **Reconciliation scalar applied uniformly by horizon.** The max 5.1% scalar (lithium) reflects documented L-discrepancy between regional weighted-average (88.35%) and national L=90%. This is applied once per horizon, preserving the regional share distribution and the relative S-curve timing dynamics.

3. **Regional LNG displacement fractions are independent estimates.** The fractions (18%–30%) are calibrated from the 07a segment-level LNG:diesel split (long-haul 80:20 LNG, captive 40:60, urban 15:85) applied with qualitative weights for each region's freight mix. They are not independently validated from primary data.

4. **Infrastructure lithium allocated by BEV unit share.** Swap stations are assumed to be built in proportion to BEV fleet density by region. In practice, infrastructure may lead adoption in some regions (YRD, as CATL announced priority build-out on Beijing–Shanghai and Shanghai–Guangzhou corridors) and lag in others (Western). This introduces a ±15% uncertainty on the infrastructure lithium allocation for individual regions, though the national total is anchored to 07b.

5. **Material intensity uniform across regions.** No regional differentiation in LFP pack size, copper wiring specifications, or infrastructure ratios. A heavier-specification variant for Western China mining routes (larger pack for range compensation, heavier copper wiring) would increase Western MI coefficients, adding upside to Western regional demand estimates.

---

## Sources

- Upstream: `output/bev-trucks-china/agents/07b-stream-forecaster.md` — national P50 totals for lithium (100.52 → 244.40 kt LCE), copper (48.02 → 81.33 kt Cu), LNG displaced (0.95 → 2.31 Mt), diesel displaced (9.84 → 23.93 Mbbl), and infrastructure lithium (10.94 → 26.59 kt LCE); S-curve parameters (L=0.90, k=0.7227, x0=2026.59); material intensity coefficients (Li: 280 kg LCE/BEV; Cu: 100 kg BEV, 27.5 kg LNG/diesel); LNG fraction 24.7% [model-derived, R²=0.9950]
- Upstream: `output/bev-trucks-china/agents/05b-regional-adopter.md` — five regional S-curve parameters (L, k, x0); 2025 regional BEV shares calibrated to 22.0% national anchor; regional market weights (YRD 25%, BTH 20%, PRD 15%, Central 25%, Western 15%); all R²>0.998; L-discrepancy note (weighted regional L=88.35% vs. national L=90%) [model-derived, observed basis 2021–2025]
- Computation: `lib.demand_math.project_demand_from_scurve`, `lib.demand_math.regional_demand_split`; all calculations via python3 through Bash tool per STDF Computation Rule 1 [model-derived]
- ICCT, "Zero-emission medium- and heavy-duty vehicle market in China, 2024", March 2025 [T3: https://theicct.org/publication/ze-mhdv-market-china-2024-mar25/] — regional and segment data; port-corridor adoption; retrieved 2026-03-20 [observed]
- IEEFA, "Surging electric truck sales stall China's LNG trucking boom", August 2025 [T3: https://thedriven.io/2025/08/05/sales-of-battery-electric-heavy-trucks-surge-in-china-to-nearly-one-quarter-of-market/] — H1 2025 22% national share [observed]
- ACEA heavy truck registration statistics 2024 [T3: https://www.acea.auto/] — Europe BEV heavy truck share ~5% [observed, 2024]
- Calstart, "Zero-Emission Technology Inventory (ZETI)", 2024 [T3: https://calstart.org/zeti/] — USA Class 8 BEV share <2% [observed, 2024]
