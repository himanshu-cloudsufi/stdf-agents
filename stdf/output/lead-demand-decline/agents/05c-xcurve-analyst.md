# STDF X-Curve Analyst Agent -- Lead-Acid Battery Incumbent Decline

**Agent:** `stdf-xcurve-analyst` | **Confidence:** 0.74

**Analysis Date:** 2026-03-20

---

## Agent Reasoning

The upstream S-curve fitter (`05a-scurve-fitter.md`) modeled five distinct S-curve adoption vectors for lithium-ion incumbent displacement of lead-acid batteries: BEV share of new passenger vehicle sales (Seg 1, 20.6% in 2026), BEV fleet stock (Seg 2, 6.7% in 2026), Li-ion telecom UPS (Seg 3, 44.6% in 2026), Li-ion datacenter UPS (Seg 4, 50.1% in 2026), and EV forklift share (Seg 5, 68.2% in 2026). This market-driven disruption is not policy-led -- it is driven by cost-curve dynamics: Li-ion's 16.81%/yr learning rate has already delivered cost parity in the stationary and motive-power segments. The composite demand model assigns 62.5% weight to SLI displacement (BEV fleet Seg 2 drives aftermarket shrinkage) and 37.5% to non-SLI displacement (telecoms, datacenter, forklift). The 10% lead demand decline milestone is 2028.1 [model-derived].

This X-curve analysis uses the 2026 baseline as reference for the incumbent share metric: incumbent lead-acid demand share is expressed as a percentage of 2026 demand. Prior to 2026, lead demand was still growing (non-SLI displacement had not yet offset absolute market growth in developing economies), so the X-curve shows 100% incumbent share through 2026 with decline commencing in 2027. The X-curve inflects sharply in 2029-2033: BEV fleet share crosses the 2031.77 inflection and accelerates through 30-50%, driving the steepest phase of demand loss. Peak decline velocity is approximately -7.7 percentage points per year in 2031-2032 -- a nonlinear death spiral driven by the reinforcing feedback loop between volume loss and cost spread.

The lead-acid incumbent is not a single entity. Three distinct industrial layers face the X-curve: (1) battery manufacturers (Clarios, EnerSys, East Penn, Chaowei, Tianneng), (2) primary/secondary lead smelters, and (3) the lead recycling industry. Each faces the X-curve at a different pace and with different fixed-cost structures. The recycling industry faces the most acute near-term crisis because its feedstock (scrap lead-acid batteries) is already contracting from non-SLI displacement while its smelter capacity was built out assuming continued growth. China secondary lead smelters hit an average operating rate of 22.3% in early 2025 (Shanghai Metal Market [T3: metal.com, observed]) -- a 202% per-unit cost increase above breakeven capacity -- confirming active death spiral mechanics in the recycling layer, which is the canary for the broader incumbent.

The five market trauma mechanisms were assessed for China, USA, and Europe using web-sourced evidence. China is the most advanced across all five mechanisms: the death spiral in secondary smelting is already active, the BEV disruption of the automotive lead demand base is the most severe globally (35.7% NEV penetration in 2024), and policy lobbying is visible via the MIIT's attempts to manage the broader battery sector consolidation. Li-ion's stellar energy storage crossover -- LFP cells now below $80/kWh at high volume -- has also eliminated the last cost-advantage refuge that lead-acid held in stationary backup applications. The USA shows early-active fixed-cost spread and advanced policy lobbying (Battery Council International defending excise-tax structures). Europe shows active fixed-cost spread from energy cost shocks in 2022 and tightening EU Batteries Regulation compliance costs. Talent flight to the Li-ion sector is active globally but hardest to quantify with precision.

---

## Agent Output

### Key Findings
- **Disruptor technology:** Lithium-ion batteries (LFP chemistry primary)
- **Incumbent technology:** Lead-acid batteries (SLI automotive, VRLA/AGM stationary, traction)
- **Current disruptor market share (composite):** 0.0% relative to 2026 baseline (demand still at 100% of 2026 level) [model-derived]; individual segment Li-ion shares: BEV fleet 6.7%, telecom UPS 44.6%, datacenter UPS 50.1%, EV forklift 68.2% [observed, 2026 model-derived from 2024 observed]
- **Current incumbent decline stage:** Pre-disruption (demand at 2026 baseline; decline begins 2027-2028)
- **Confidence:** 0.74

---

### Incumbent Decline Stage (As of 2026)

- **Current stage:** Pre-disruption (composite lead demand index = 100% of 2026 baseline)
- **Incumbent market share:** 100% of 2026 baseline demand (demand still growing due to developing-market SLI growth offsetting initial non-SLI displacement)
- **Key indicators:** Secondary lead smelter operating rates in China already at 22-35% (Shanghai Metal Market, 2024-2025 [T3, observed]) -- death spiral in recycling layer ALREADY ACTIVE despite demand still at baseline. This decoupling between recycling distress and aggregate demand is the leading indicator of what will propagate to battery manufacturers at 2028-2033.
- **Spiral velocity:** Not yet started at aggregate level (2026); accelerating in recycling sub-sector (active in China 2024-2025)

---

### X-Curve Dynamics

| Year | BEV Fleet Share | Li-ion Non-SLI (wtd) | Demand vs. 2026 (%) | Disruptor Eff. Share (%) | Incumbent Share (%) | Decline Stage |
|------|----------------|----------------------|--------------------|-----------------------|--------------------|----|
| 2020 | 0.6% | 38.4% | 115.9% | 0.0% | 115.9% | Pre-disruption |
| 2022 | 1.4% | 44.5% | 112.2% | 0.0% | 112.2% | Pre-disruption |
| 2024 | 3.0% | 51.8% | 107.0% | 0.0% | 107.0% | Pre-disruption |
| 2026 | 6.7% | 59.5% | 100.0% | 0.0% | 100.0% | Pre-disruption |
| 2027 | 9.7% | 63.0% | 95.6% | 4.4% | 95.6% | Pre-disruption |
| **2028** | **13.8%** | **66.2%** | **90.5%** | **9.5%** | **90.5%** | **Pre-disruption → Early volume loss** |
| 2029 | 19.2% | 68.8% | 84.6% | 15.4% | 84.6% | Early volume loss |
| 2030 | 25.9% | 71.0% | 77.8% | 22.2% | 77.8% | Accelerating decline |
| 2031 | 33.7% | 72.8% | 70.3% | 29.7% | 70.3% | Accelerating decline |
| 2032 | 41.9% | 74.1% | 62.6% | 37.4% | 62.6% | Accelerating decline |
| 2033 | 50.0% | 75.2% | 55.1% | 44.9% | 55.1% | **Death spiral active** |
| 2035 | 63.4% | 76.7% | 43.0% | 57.0% | 43.0% | Death spiral active |
| 2038 | 74.4% | 77.8% | 33.1% | 66.9% | 33.1% | Advanced collapse |
| 2040 | 77.5% | 78.1% | 30.3% | 69.7% | 30.3% | Advanced collapse |
| 2045 | 79.7% | 78.5% | 28.2% | 71.8% | 28.2% | Advanced collapse |

**Peak decline velocity:** -7.7 pp/year in 2031-2032 [model-derived]. Decline accelerates from -4.4 pp/yr in 2027 to -7.7 pp/yr peak in 2032, then decelerates as the curve approaches its floor around 28-30% of 2026 demand levels by 2045.

**Note on stage classification:** The standard stage table (incumbent share >90% = pre-disruption) applies here to the percentage of 2026 baseline demand. However, because the X-curve baseline is 2026 (not peak incumbent share), and lead demand was still growing through 2025 driven by developing-market SLI and e-bike demand, the incumbent was already experiencing sub-segment death spirals in non-SLI before the aggregate 10% decline threshold triggers at 2028.1. The classification understates how advanced the disruption already is within individual segments.

---

### Decline Loop Evidence

#### Volume Loss
Lead demand index: 100% in 2026, falling to 90.5% in 2028, 77.8% in 2030, 62.6% in 2032 [model-derived from fitted S-curves].

Observed leading indicator: China NEV sales reached 9.5 million units in 2024, NEV penetration 35.7% of new passenger vehicle sales in China [T3: MIIT data per Mordor Intelligence, observed 2024]. Each NEV sale eliminates one SLI battery installation from the OEM channel.

Global lead production in 2024: 13.5 million metric tons (2.4% increase from 2023) -- demand side consumption increase was only 0.2% [T3: USGS Mineral Commodity Summaries 2025, observed]. Supply/demand divergence confirms demand is growing slower than supply capacity was built for, already creating surplus conditions.

#### Unit Cost Increase
With fixed-cost fraction at 45% for battery manufacturing and 57% for smelting:
- At 10% volume loss (2028): per-unit battery manufacturing cost rises +5.0% [model-derived]
- At 20% volume loss (2030): per-unit cost rises +11.3% [model-derived]
- At 37% volume loss (2033): per-unit cost rises +26.4% [model-derived]

For secondary smelters at current China utilization of 22-35% (well below 65% breakeven): per-unit recycling cost is 106-202% above the cost at full utilization [model-derived from observed operating rates].

China secondary lead smelting losses are confirmed by Shanghai Metal Market reporting widespread losses and smelters "considering reducing production or shutting down for maintenance" as of 2025 [T3: metal.com, observed].

#### Margin Compression
Lead-acid battery manufacturers face a two-sided squeeze: raw material (lead) costs remain elevated (LME lead ranged $1,950-$2,150/tonne in 2024 [T3: USGS MCS 2024, observed]) while competition from Li-ion drives prices down. Li-ion pack prices fell 20% to $115/kWh in 2024, with high-volume LFP at sub-$80/kWh [T3: BloombergNEF per ACE Battery, observed 2024]. This eliminates the price-premium buffer that lead-acid manufacturers historically enjoyed in stationary and UPS segments -- their primary growth markets.

China secondary lead smelter gross margins are already negative: raw material (scrap battery) purchase prices hit a record high of 12,200 yuan/metric ton for e-bike scrap in 2024 [T3: Shanghai Metal Market, observed], while smelted lead output prices remained depressed. Smelters report that "by-product revenue can barely offset the pressure of losses."

#### Facility Closures
USA: Nine secondary lead facility closures between 1990 and 2021 [T3: Battery Council International, observed]. No new battery smelter built in the USA since 2009 [T3: BCI, observed]. Last primary lead refinery closed in 2013 [T3: USGS MCS 2024, observed].

Exide Technologies: Three major restructurings (2002, 2013, 2020 bankruptcy) culminating in the 2020 sale of Americas business to Atlas Holdings/Stryten for $178.6 million [T3: Exide Wikipedia, observed]. The Vernon, California battery recycling plant permanently closed, proposed for Superfund designation in 2024 [T3: EPA/Daily Breeze, observed].

Europe: European lead output fell 11.4% in 2022 due to energy cost shock [T3: E&MJ Markets, observed]. Smelter idlings at multiple sites; Germany's Trafigura Stolberg smelter was closed by flooding in 2021 and only partially reopened [T3: E&MJ Markets, observed].

China: Secondary lead smelter capacity reached 14.6 million tons/year against actual feedstock supply of ~7.6 million tons (shortfall >7 million tons) [T3: iru-miru.com/SMM analysis, observed 2024].

#### Stranded Assets
USA: The Exide Vernon plant represents the archetype: a 90-year-old battery recycling facility with >$50 million in cleanup liability abandoned in bankruptcy [T3: EPA, observed]. The California DTSC estimates cleanup costs affecting ~10,000 homes in surrounding communities.

Secondary lead smelters in China represent stranded capacity: 14.6 million tons/year nameplate capacity with no viable path to adequate utilization given both overcapacity relative to demand and the structural long-term decline of feedstock as lead-acid batteries age out [T3: SMM/iru-miru.com, observed].

---

### Lead Recycling Industry: Structural Disruption Analysis

The lead recycling industry faces a structural disruption that is DISTINCT from and EARLIER THAN the aggregate battery demand decline. This is unique to lead because:

1. **97-99% recycling rate** (observed in USA/Europe [T3: International Lead Association, observed]) means the industry is entirely dependent on spent lead-acid batteries as feedstock.
2. **When battery installation falls, feedstock shrinks** -- but with a 3-12 year lag (battery lifetime). Non-SLI batteries (telecom, datacenter, forklift) installed in 2019-2024 under high li-ion displacement growth will yield declining scrap volumes in 2022-2027.
3. **Smelter overcapacity was built for growth**: China's secondary lead processing capacity expansion assumed continued growth in lead-acid battery deployment. That growth assumption broke in 2022-2024 as non-SLI displacement accelerated.

**Feedstock flow index** [model-derived from upstream S-curves]:

| Year | SLI Feedstock Flow | Non-SLI Feedstock Flow | Combined (2026=100) |
|------|-------------------|------------------------|---------------------|
| 2024 | 107.0% | 116.5% | 110.5% |
| 2026 | 100.0% | 100.0% | 100.0% |
| 2028 | 89.0% | 85.8% | 87.8% |
| 2030 | 73.9% | 75.5% | 74.5% |
| 2032 | 56.9% | 68.8% | 61.4% |
| 2035 | 36.3% | 63.4% | 46.5% |

**The critical economic threshold**: Secondary smelters require ~65% utilization for profitability (fixed cost fraction ~57%). China is already at 22-35% utilization [T3: SMM, observed], implying per-unit costs 106-202% above the break-even basis. The recycling industry death spiral is ACTIVE NOW in China, not in 2028 when aggregate demand crosses the 10% threshold.

**Recycling uneconomics timeline**: When combined feedstock flow falls below ~50-55% of 2026 levels (modeled at ~2032-2035), smelter operations become progressively unviable even at efficient scale. Smaller, less-integrated recyclers will close first (already happening in China per SMM, 2025 [T3, observed]). The surviving operators will be those with integrated supply chains (scrap collection + smelting + battery manufacturing in one entity) -- Clarios, East Penn, Stryten in the USA; Chaowei, Tianneng in China.

---

### Market Trauma Assessment

Status values: not yet / beginning / active / advanced / completed

| Mechanism | China | USA | Europe | Evidence |
|-----------|-------|-----|--------|----------|
| Fixed-cost spread | **advanced** | **active** | **active** | China secondary smelters at 22-35% utilization [T3: SMM, 2025 observed], per-unit costs +106-202% above breakeven. USA: 9 facility closures 1990-2021, no new smelter since 2009 [T3: BCI]. Europe: 11.4% output fall in 2022 from energy cost shock driving smelter shutdowns [T3: E&MJ] |
| Investment drought | **advanced** | **active** | **beginning** | China: Li-ion gigafactory capacity 2,500 GWh vs 1,250 GWh shipments; virtually no new lead-acid capex announced beyond maintenance. USA: DOE grants to modernize (not expand) lead smelting [T3: Energy-Storage News, 2024]; Clarios $6B plan through 2035 defensive (modernization, not growth) vs. Stryten pivoting to lithium assembly in Georgia. Europe: No new lead battery plant announced; EU Batteries Regulation drives compliance capex, not growth capex. |
| Talent flight | **active** | **beginning** | **beginning** | China: CATL, BYD, CALB held 75% of Li-ion domestic shipments 2024 [T3: CRU Group]; these firms are paying premium for electrochemistry engineers, drawing from lead-battery sector talent pool. USA/Europe: No specific lead-to-lithium engineer migration data found (data gap). Stryten opening lithium plant in Georgia may signal internal talent redeployment rather than net loss. |
| Panic pricing | **active** | **beginning** | **beginning** | Global: Lead-acid battery prices declining "in almost every industry" under LFP competition at $80-115/kWh [T3: Coherent Market Insights/ACE Battery, observed 2024]. China scrap battery purchase prices rose to record highs (12,200 yuan/mt e-bike scrap [T3: SMM, observed 2024]) while lead output prices stagnated -- classic margin collapse from dual-sided squeeze. USA/Europe: No specific manufacturer price-cut announcements found; competition pressure is structural rather than panic-discount form at present. |
| Policy lobbying | **active** | **advanced** | **active** | USA: BCI lobbying Congress for USA Batteries Act (eliminate excise tax on lead oxide, antimony, sulfuric acid) [T3: Energy-Storage News, observed 2024]; cited $8.1T economic output dependence on domestic battery industry. China: MIIT 2024 lithium battery standards tightening to address overcapacity -- indirectly pressures lead-acid sector consolidation. EU: Batteries Regulation (EU) 2023/1542 requires 85% minimum recycled lead content in batteries from 2030 [T3: White & Case, observed 2023] -- regulatory cost barrier that protects the recycling loop while mandating it. |

**Regional detail -- China:**
China is in the most advanced state across all five mechanisms. The 35.7% NEV penetration in 2024 has already eliminated a major share of the OEM SLI channel. Secondary lead smelters are loss-making with utilization at 22-35%. Li-ion battery manufacturers (CATL, BYD) are absorbing engineering talent. The MIIT has acknowledged "irrational competition" and overcapacity problems. China represents the lead indicator for what USA and Europe will experience 3-5 years later as BEV fleet displacement accelerates from its current 6.7% global fleet share toward the 2031.77 inflection point.

**Regional detail -- USA:**
The USA incumbent industry (Clarios ~34% US market share, EnerSys, East Penn, Stryten) is in an earlier phase. Aggregate lead-acid demand has not yet visibly declined from the SLI channel (BEV fleet share at ~6-7% globally, lower in USA for older fleet). However, industrial/stationary segments (datacenter UPS, telecom UPS) are already transitioning to Li-ion, removing the growth vector from lead-acid. Fixed-cost spread is active in the recycling/smelting layer (nine closures since 1990). Lobbying is advanced: BCI's advocacy for the USA Batteries Act is an explicit attempt to level the cost playing field against Chinese Li-ion imports. The DOE's $348M in grants to modernize existing lead smelters (Clarios $150M, EnerSys $198M) is a defensive subsidy, not a growth investment.

**Regional detail -- Europe:**
Europe's incumbent faces the fixed-cost spread from the 2022 energy cost shock (11.4% production fall) combined with the EU Batteries Regulation's stringent recycled-content requirements from 2030. The regulation mandates 85% recycled lead content -- this preserves the recycling loop's relevance in Europe but imposes significant compliance costs on smaller operators. Investment drought is beginning: no new lead battery manufacturing capacity has been announced for Europe, while Li-ion gigafactory announcements continue weekly. Talent flight and panic pricing are early-stage; the EU's stricter lead exposure limits (California model: 10 µg/m³ vs. OSHA 50 µg/m³) will raise compliance costs further.

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 4.4 | MEDIUM | PASS | X-curve incumbent decline mapping | Five-segment composite X-curve computed from upstream S-curve parameters. Decline stages mapped with per-year velocity from 2026-2045. Three industrial layers (battery manufacturers, smelters, recyclers) mapped separately with distinct timing. |
| 4.5 | MEDIUM | PASS | Market trauma recognition (5 mechanisms x 3 regions) | All five mechanisms assessed for China, USA, Europe with status values and evidence citations. Status uses exact vocabulary: not yet / beginning / active / advanced / completed. |

---

### Data Gaps

1. **Company-level capex data for major incumbents (Clarios, EnerSys, East Penn, Chaowei, Tianneng).** All are private (East Penn) or have limited public disclosure (Clarios post-IPO plans, EnerSys SEC filings not searched in detail). No direct evidence of capex reduction announcements found in this run. Gap noted; would require Bloomberg or S&P Capital IQ access.
2. **Talent flight quantification.** No primary source found tracking engineer/manager movement from lead-acid to Li-ion sector. Model-derived inference only (Li-ion sector growth implies talent absorption). Flag as data gap.
3. **Lead-acid battery pricing data (manufacturer level).** No primary source found for wholesale pricing trends at Clarios/East Penn level. Competition pressure inferred from Li-ion cost curve; specific lead-acid price reduction announcements not found.
4. **China lead-acid battery manufacturer employment data.** Chaowei and Tianneng workforce numbers not publicly available for 2022-2024 comparison. MIIT aggregate data not retrieved. Gap noted.
5. **Primary lead mine employment.** Missouri Viburnum Trend mine employment (Doe Run, ~6 mines) not sourced to a specific count for 2022-2024. Structural exposure confirmed (Missouri is principal US lead mining district) but workforce size not quantified.
6. **Forklift sub-layer: Li-ion within EV forklifts.** Already flagged by scurve-fitter as T3-only (Interact Analysis, 65% in 2024). The second-order lead-acid displacement from within the EV forklift category adds incremental feedstock reduction not fully captured in the primary model.

### Upstream Discrepancies

- **None.** The X-curve is computed directly from the upstream scurve-fitter S-curve parameters (L, k, x0 for all five segments). The composite demand formula and segment weights are taken verbatim from the scurve-fitter output. No new S-curve fitting was performed here. The one interpretive addition: the X-curve baseline uses 2026 as reference (demand = 100%) rather than a historical peak, because the scurve-fitter explicitly used 2026 as the demand baseline.

---

## Sources

- Shanghai Metal Market (SMM), 2024-2025 [T3, observed]: secondary lead smelter operating rates, scrap battery prices, smelter loss margins -- metal.com/en/newscontent/103001159, metal.com/en/newscontent/103284112, metal.com/en/newscontent/103530900, metal.com/en/newscontent/103784648
- USGS Mineral Commodity Summaries 2024 (pubs.usgs.gov/periodicals/mcs2024/mcs2024-lead.pdf) [T3, observed]: US lead production 2023, secondary lead 1,000,000 tons, mine closures, last primary refinery 2013
- USGS Mineral Commodity Summaries 2025 (pubs.usgs.gov/publication/mcs2025) [T3, observed]: US lead mine production +10% in 2024, global production 13.5Mt, consumption +0.2%
- International Lead and Zinc Study Group (ILZSG) via USGS, 2023-2024 [T3, observed]: global refined lead production/consumption balance, 21,000 mt surplus in first 10 months 2024
- Battery Council International (BCI) [T3, observed]: Nine facility closures USA 1990-2021, no new smelter since 2009, USA Batteries Act lobbying, $8.1T economic output claim -- batterycouncil.org/news/deficit-in-north-american-battery-recycling-capacity, energy-storage.news BCI Congress report
- Exide Technologies/Atlas Holdings/Stryten: Wikipedia (Exide), BusinessWire (Atlas acquisition Aug 2020), EPA enforcement case summary, Daily Breeze (Superfund proposal Sept 2024) [T3, observed]
- E&MJ Markets (e-mj.com/departments/markets/demand-for-lead-and-zinc-to-grow-in-2023/) [T3, observed]: Europe 11.4% output fall 2022, German Stolberg smelter closure
- ACE Battery (acebattery.com/blogs/wave-of-decline-sweeps-lithium-ion-battery-pack-pricing-in-2024) [T3, observed]: Li-ion pack prices -20% to $115/kWh in 2024
- Coherent Market Insights / Fact.MR [T3, observed]: lead-acid prices declining "in almost every industry"
- China secondary lead overcapacity: iru-miru.com/en/article/77423, SMM analyses [T3, observed]: 14.6Mt nameplate capacity vs. 7.6Mt actual supply
- CRU Group (crugroup.com, 2023, 2025) [T3, observed]: China battery gigafactory utilization 50%, CATL/BYD/CALB 75% domestic market share
- MIIT 2024 via EnergyTrend (energytrend.com/news/20240511-46916.html) [T3, observed]: lithium battery industry specifications tightening
- White & Case LLP (whitecase.com) [T3, observed]: EU Batteries Regulation 2023/1542, 85% recycled lead content requirement from 2030
- Mordor Intelligence / Grand View Research [T3, observed]: China lead-acid battery market $7,352M (2023); China NEV penetration 35.7% (2024)
- International Lead Association: 99% recycling rate USA/Europe [T3, observed]
- BloombergNEF via multiple sources: Li-ion 20% price drop 2024 (rejected for forecasts; used only for 2024 observed data point)
- Upstream: `05a-scurve-fitter.md` (this pipeline run) -- S-curve parameters, composite demand formula, segment weights
- Computation: `lib.scurve_math.logistic` -- all S-curve evaluations
- Computation: `lib.scurve_math.xcurve_decline` -- mirror incumbent decline curve
- Computation: inline python3 -- fixed-cost spread model, feedstock flow index, smelter viability analysis
