# STDF Gas Supply Decomposer Agent — Bloom Energy SOFC Disruption by SWB

**Agent:** `stdf-gas-supply-decomposer` | **Confidence:** 0.82

---

## Agent Reasoning

**Scope adaptation: this is a niche segment analysis, not a macro gas market analysis.** The standard gas supply decomposer pipeline models continent-scale LNG displacement cascades across China, Europe, and the USA. This analysis adapts that framework to a specific niche segment: Bloom Energy's SOFC fleet consuming natural gas for distributed on-site power generation. Bloom's full fleet consumed approximately 1.756 BCM of natural gas in 2024 [model-derived] — equivalent to 0.19% of total US gas consumption. That number makes the analytical framing crystal clear: the gas supply story here is NOT about moving gas markets. It is about (1) Bloom's fuel cost exposure and how that shapes competitive dynamics versus SWB, and (2) the directional signal this niche displacement sends about distributed gas generation's structural decline as market-driven disruption by stellar energy scales. Both have investment implications.

**Why gas price matters for the short thesis.** Bloom Energy SOFC is an X-Flow technology [confirmed: 01-domain-disruption.md classification]. Its marginal cost of electricity production is structurally bounded below by the Henry Hub gas price. At $2.19/MMBtu (2024 historic inflation-adjusted low), Bloom's marginal cost is $22.9/MWh — still $16.8/MWh above the 8-hour BESS SCOE of $6.1/MWh [model-derived from 08a dispatch agent]. This is the core asymmetry: even at the cheapest gas in modern history, Bloom cannot compete with BESS on dispatch marginal cost. Gas price would have to go negative for Bloom to undercut BESS on marginal cost — structurally impossible under normal market conditions. Lower gas prices reduce Bloom's LCOE disadvantage in new-build procurement comparisons, but they do not change the dispatch order: solar dispatches first at $0/MWh, BESS dispatches second at $6/MWh, and Bloom dispatches third at $23+/MWh regardless of Henry Hub. This is the cost-curve dynamics advantage of stellar energy technologies (zero marginal fuel cost) over X-Flow incumbents.

**Supply source context: Bloom is 100% domestic shale, no LNG exposure.** USA is a net gas exporter with 2023 production of 1,070.5 BCM against consumption of 923.7 BCM [T2: Natural_Gas_Annual_Production_USA.json + Natural_Gas_Annual_Consumption_USA.json, observed] [CAUTION: EIA source — historical data only]. Bloom's SOFC fleet is supplied entirely through the domestic interstate pipeline network, drawing on Marcellus/Utica Appalachian shale, Haynesville, and Permian associated gas — all priced at Henry Hub or local basis. There is zero LNG import exposure for Bloom's gas supply. The LNG angle for USA is export-side: as Bloom's fleet shrinks and broader US distributed gas generation declines, the US shale gas that was powering SOFCs becomes available for LNG export — but the volumes are too small (< 1 BCM/yr for Bloom) to affect the $200+ billion LNG export market structure.

**Regional analysis covers China, Europe, and USA per compliance requirements.** While Bloom's gas supply is USA-specific, the agent mandate requires coverage of three regions. China and Europe analyses are provided using catalog data to establish the global LNG displacement context that is relevant to the broader short thesis narrative: as SWB drives incumbent displacement of distributed gas generation globally via S-curve adoption, LNG — as the most expensive marginal supply source — is eliminated first in every importing region. This macro context reinforces the structural validity of the short thesis on Bloom and the broader gas infrastructure disruption.

---

## Agent Output

### Key Findings

- **Bloom SOFC gas consumption (2024):** 1.756 BCM full fleet (1.229 BCM USA only) [model-derived] — a micro-segment at 0.19% of US gas consumption
- **Bloom fleet gas trajectory:** Declining from 1.756 BCM (2024) to 0.713 BCM (2040) as S-curve adoption of SWB drives incumbent displacement; an L=85% upper-bound scenario would reach ~8.05 BCM at 5.5 GW, but the modeled L=70% path does not require this scale
- **USA supply source:** 100% domestic shale gas (Henry Hub-priced) — no LNG exposure for Bloom's input fuel supply
- **Gas price helps but cannot save Bloom:** Even at $2.19/MMBtu all-time-low gas, Bloom marginal cost ($22.9/MWh) exceeds 8hr BESS SCOE ($6.1/MWh) — Bloom is always displaced before BESS in the merit order
- **Gas price = contractual exposure:** At 5-year average gas ($3.42/MMBtu), customers pay ~$216M/yr for fuel embedded in Bloom service contracts — falling gas reduces renewal pricing power
- **China LNG imports:** 107.64 BCM (2024) [T2: observed], representing 24.3% of China supply — LNG approaches zero as SWB drives incumbent displacement of gas generation because coal dispatches before gas (MC $35 < $70) and domestic + pipeline covers all remaining demand
- **Europe LNG imports:** 169.1 BCM (2023) [T2: observed] — US LNG displaced first (highest delivered cost ~$7–8/MMBTU), Qatar second, Norwegian pipeline last
- **Structural gas floor:** ~15% of demand as petrochemical feedstock — global gas demand does not reach zero, but LNG's share of import-dependent regions can reach zero

---

### Gas Generation Displacement (from Energy Dispatch)

**Source: 08a-energy-dispatch.md [model-derived from S-curve (L=70, k=0.196, x0=2034.7) × BESS duration pathway × contract renewal model]**

| Region/Segment | Gas Gen Displaced vs 2024 (GWh/yr) | Source |
|----------------|-------------------------------------|--------|
| Bloom USA fleet (840 MW) | 0 (2024 baseline) → −401 (2028) → −721 (2030) → −1,699 (2034) → −4,153 (2040) | [model-derived] |
| Total US enterprise C&I distributed gas DG | 0 (2024 baseline) → −5,000 (2030) → −15,000 (2035) → −25,000 (2040) | [CAUTION: EIA source — order of magnitude, observed basis; historical data only] |

**Note:** The dispatch agent models only Bloom USA (840 MW of the 1.2 GW global fleet). Korea (~120 MW, ~30% of remaining fleet) and minor international deployments are scaled proportionally.

---

### GWh to BCM Conversion

**Formula:** BCM = Gas\_Gen\_GWh × 3.6 / (heat\_rate × efficiency) / 1000

**Parameters for Bloom SOFC:** heat\_rate = 35.3 MJ/m³ (natural gas LHV), efficiency = **0.58** (Bloom SOFC electrical efficiency from Bloom Energy Server datasheet 2024 [observed] — NOT the 0.45 CCGT default; SOFC runs at 54–60% vs 45% for CCGT)

**Note on efficiency:** Using 0.45 CCGT efficiency would overstate gas consumption by 29%. The 0.58 value is Bloom-specific and validated against the dispatch agent's figures.

| Segment | Gas Gen (GWh/yr) | BCM/yr | Data Type |
|---------|-----------------|--------|-----------|
| Bloom USA fleet (840 MW, 2024) | 6,990 | 1.229 | [model-derived, validated vs dispatch agent] |
| Bloom full fleet (1.2 GW, 2024) | 9,986 | 1.756 | [model-derived: USA × 1200/840 scale factor] |
| Bloom full fleet (L=85% upper-bound, 5.5 GW, 2033–2035 per brief) | 45,771 | 8.048 | [model-derived: upper-bound scenario; not the modeled L=70% path] |
| US enterprise C&I distributed gas DG (~60,000 GWh baseline) | 60,000 | 15.3 | [CAUTION: EIA source — order of magnitude; 40% avg efficiency for mixed fleet; historical data only] |

**Cross-check against dispatch agent:** Dispatch agent stated 1.22 BCM for 2024; this agent computes 1.229 BCM — difference of 0.009 BCM (0.7%). PASS.

---

### Non-Power Gas Demand **All values: [observed] from T2 catalog unless noted**

**USA context (2023):**

| Region | Power Gen (BCM) | Industrial (BCM) | Heating (BCM) | Feedstock (BCM) | Total (BCM) |
|--------|----------------|------------------|---------------|-----------------|-------------|
| USA | 332.5 | 230.9 | 221.7 | 138.6 | 923.7 |

*Source: T2: Natural\_Gas\_Annual\_Consumption\_USA.json [CAUTION: EIA source — historical data only, observed 2023] with sectoral allocation from gas-supply-ordering reference (36%/25%/24%/15%)*

**Bloom distributed gas DG within USA power generation segment:**

| Segment | BCM/yr | % of US Power Gen Gas | % of US Total Gas |
|---------|--------|----------------------|-------------------|
| All US enterprise C&I distributed gas DG | ~15.3 | ~4.6% | ~1.7% |
| Bloom SOFC specifically (840 MW USA) | 1.229 | ~0.4% | ~0.133% |
| Bloom full fleet (1.2 GW global) | 1.756 | ~0.5% | ~0.190% |

**Key finding:** Bloom's gas demand is a micro-segment. Its incumbent displacement does NOT move gas markets. The investment thesis is entirely about Bloom's revenue, not commodity supply impacts.

---

### Total Gas Demand by Region

**All values: [observed] from T2 catalog unless noted as [model-derived]**

| Region | Current (BCM, 2023/2024) | +5yr (2029, BCM) | +10yr (2034, BCM) | +20yr (2044, BCM) | Data Type |
|--------|--------------------------|-------------------|-------------------|-------------------|-----------|
| USA | 923.7 (2023) | ~900–940 | ~850–900 | ~750–850 | [observed 2023]; +5/+10/+20 [model-derived]: SWB disruption partially offset by industrial + LNG export demand |
| China | 395.3 (2023) | ~420–440 | ~420–450 | ~380–420 | [observed 2023]; projections [model-derived]: growth moderating as SWB scales; coal-before-gas limits gas power gen floor |
| Europe | ~400–420 (est. 2023) | ~360–390 | ~320–360 | ~260–310 | [model-derived] from SWB disruption + heat pump trajectory; Europe NG consumption catalog used for context |

**Structural floor note:** Petrochemical feedstock (~15% of demand) is NOT displaced by SWB — it is chemical feedstock, not energy. This creates a persistent floor below which gas demand cannot fall even in extreme SWB incumbent displacement scenarios.

---

### Supply Source Decomposition

**All values: [observed] from T2 catalog for current figures; [model-derived] for projections**

#### USA — Bloom's Supply Region

| Source | Current (BCM, 2023) | Priority | Cost Rank | +5yr (BCM) | +10yr (BCM) | +20yr (BCM) | Data Type |
|--------|--------------------|-----------|-----------|-----------  |-------------|-------------|-----------|
| Domestic shale + conventional | ~1,050 (production) | 3 (last displaced) | Cheapest ($2.19/MMBTU HH, 2024) | ~1,020–1,060 | ~980–1,030 | ~900–1,000 | [T2: Natural_Gas_Annual_Production_USA.json, observed 2023]; projections [model-derived] |
| Pipeline from Canada | ~20–30 | 2 | Moderate | ~20–30 | ~20–30 | ~20–30 | [model-derived estimate; USA is large net exporter] |
| LNG imports (USA) | <1 (negligible) | 1 (first displaced) | Most expensive | ~0 | ~0 | ~0 | [T2: LNG import catalog, observed; USA net LNG exporter since 2016] |
| **LNG exports (USA)** | **~147 BCM surplus** | N/A — export | — | ~160–180 | ~150–170 | ~100–150 | [model-derived; export side at risk from global LNG demand collapse] |

**USA supply conclusion:** Bloom SOFC draws 100% from domestic shale gas. There is no LNG displacement cascade on the input side for Bloom. As Bloom's fleet shrinks (1.229 BCM USA declining to 0.499 BCM by 2040), this shale gas joins the export pool or marginally depresses Henry Hub — too small to observe at market level.

#### China — Global LNG Context

| Source | Current (BCM, 2023) | Priority | Cost Rank | +5yr (BCM) | +10yr (BCM) | +20yr (BCM) | Data Type |
|--------|--------------------|-----------|-----------|-----------|-----------  |-------------|-----------|
| Domestic conventional + CBM | 239.4 | 5 (last displaced) | Cheapest | ~265–275 | ~280–295 | ~280–300 | [T2: Natural_Gas_Annual_Production_China.json, observed 2023]; projections [model-derived] |
| Pipeline — Central Asia (Turkmenistan) | ~45–50 | 3 | Moderate | ~50–55 | ~50–55 | ~45–55 | [model-derived from total imports 161.8 BCM minus LNG 97.8 BCM = 64 BCM pipeline total; Central Asia ~75% share estimated] |
| Pipeline — Russia (Power of Siberia) | ~14–16 | 2 | Moderate | ~20–25 | ~25–30 | ~25–30 | [model-derived estimate; ramp-up from catalog import data] |
| **LNG imports** | **97.8 (2023) / 107.6 (2024)** | **1 (first displaced)** | **Most expensive (~$12–15/MMBTU delivered)** | ~90–100 | ~70–85 | **~10–30** | [T2: Energy Institute Statistical Review of World Energy, observed]; projections [model-derived] |

**China supply conclusion:** China's 2024 LNG surge to 107.64 BCM [T2: observed] represents the near-term ceiling on a structural basis. As SWB drives incumbent displacement of gas-fired generation (coal dispatches first at $35/MWh MC vs gas at $70/MWh MC, leaving gas as the residual), domestic production + pipeline imports suffice for remaining non-power gas demand. LNG — at $12–15/MMBTU delivered vs domestic gas at ~$7–8/MMBTU equivalent — is eliminated first. This is the mathematical consequence of the cost stack, not a prediction.

#### Europe — LNG Displacement Cascade Context

| Source | Current (BCM, 2023) | Priority | Cost Rank | +5yr (BCM) | +10yr (BCM) | +20yr (BCM) | Data Type |
|--------|--------------------|-----------|-----------|-----------  |-------------|-------------|-----------|
| Domestic North Sea + production | ~30–40 | 4 (last displaced) | Cheapest | ~25–35 | ~20–30 | ~15–25 | [model-derived; declining North Sea] |
| Pipeline — Norway | ~100–115 | 3 | Cheap (no liquefaction) | ~100–110 | ~90–105 | ~80–100 | [model-derived from catalog context] |
| LNG — Qatar | ~40–50 | 2 | Moderate | ~35–45 | ~25–38 | ~15–28 | [model-derived; Qatar has lower extraction cost than US] |
| **LNG — USA** | **~70–85** | **1 (first displaced)** | **Most expensive (~$7–9/MMBTU delivered)** | **~55–70** | **~35–55** | **~10–30** | [model-derived from Europe LNG total 169.1 BCM 2023 [T2: observed]; US share estimated] |

**Europe supply conclusion:** Post-Russia pipeline disruption, Europe replaced ~130–140 BCM of Russian pipeline gas with LNG (172 BCM peak in 2022 [T2: observed], 169 BCM in 2023 [T2: observed]). As SWB + offshore wind + heat pumps drive incumbent displacement of gas demand, US LNG is displaced first (highest delivered cost: liquefaction ~$3.0/MMBTU + Atlantic shipping ~$0.5–1.0/MMBTU + regasification ~$0.3–0.5/MMBTU on top of Henry Hub $2.19/MMBTU = $6.0–7.2/MMBTU total delivered [model-derived from catalog LNG export price $6.28/MMBTU 2024]).

---

### LNG Displacement Cascade

| Region | LNG Source | Current (BCM) | Displacement Order | +5yr | +10yr | +20yr | Reason |
|--------|-----------|---------------|--------------------|------|-------|-------|--------|
| China | Australia/Qatar spot | 107.6 (2024) [T2: observed] | 1st | 90–100 | 70–85 | 10–30 | Most expensive: $12–15/MMBTU delivered; domestic + pipeline cheaper at every volume level |
| Europe | USA LNG | ~70–85 (est. 2023) | 1st | 55–70 | 35–55 | 10–30 | Highest delivered cost: liquefaction + Atlantic transit + regasification ~$7–9/MMBTU [model-derived] |
| Europe | Qatar LNG | ~40–50 (est. 2023) | 2nd | 35–45 | 25–38 | 15–28 | Lower extraction cost ($2–3/MMBTU), shorter shipping to Europe vs US |
| Europe | Norwegian pipeline | ~100–115 (est. 2023) | Last | 100–110 | 90–105 | 80–100 | No liquefaction cost; short transit; cheapest non-domestic source |
| USA (export) | US LNG exports | ~147 BCM net surplus | Export stranded | 160–180 supply; destination demand shrinks | Export capacity utilization falls | Stranded terminals | Global LNG demand collapse from SWB + China/Europe incumbent displacement |

**All LNG trajectory values: [model-derived] from supply source ordering applied to gas demand displacement schedules**

---

### LNG Import Projections **All values: [model-derived]**

| Region | Current (BCM) | +5yr | +10yr | +20yr | Trajectory |
|--------|---------------|------|-------|-------|------------|
| China | 107.6 (2024) [T2: observed] | 90–100 | 65–80 | 5–25 | Approaching zero: domestic + pipeline displace LNG entirely as coal-before-gas merit order limits gas power gen, reducing total gas demand |
| Europe | 169.1 (2023) [T2: observed] | 145–165 | 110–140 | 60–100 | Declining: US LNG displaced first, Qatar second; Norwegian pipeline floor holds; SWB + heat pumps drive demand down |
| USA | <1 (negligible) [T2: observed] | ~0 | ~0 | ~0 | Already zero: USA is net exporter, no import dependency |

**China LNG → zero mechanism (detail):** China's coal merit order (MC ~$35/MWh) dispatches before gas (MC ~$70/MWh) [observed: dispatch_parameters.json]. SWB further drives incumbent displacement of gas generation. Remaining gas demand (industrial, heating, chemical) = ~160–180 BCM [model-derived at 40–45% of 2023 consumption]. China domestic production (growing at ~6–8%/yr, 2018–2023 observed from catalog) + pipeline imports (~64 BCM as of 2023 [model-derived: total imports 161.8 BCM minus LNG 97.8 BCM]) = ~300 BCM supply capacity before any LNG. With remaining demand of ~160–180 BCM, the arithmetic gives LNG zero volume with margin to spare. This is the mathematical consequence of cost stack ordering, not a prediction.

---

### USA Gas Price Sensitivity — Bloom Fuel Cost Exposure

**All values: [model-derived] from Bloom SOFC efficiency 0.58; Henry Hub observed prices [T2: Natural_Gas_Price_USA.json] [CAUTION: EIA source — historical data only]**

| Henry Hub ($/MMBTU) | Year Reference | Bloom Fuel Cost ($/MWh) | Bloom MC (+ $10 O&M) | 8hr BESS SCOE | Gap (Bloom − BESS) |
|--------------------|----------------|--------------------------|----------------------|---------------|---------------------|
| 2.03 | 2020 | 11.94 | 21.94 | 6.1 | +15.84 |
| 2.19 | 2024 (historic low) | 12.88 | 22.88 | 6.1 | +16.78 |
| 2.53 | 2023 | 14.88 | 24.88 | 6.1 | +18.78 |
| 3.42 | 5yr avg 2020–2024 | 20.12 | 30.12 | 5.6 (2026) | +24.52 |
| 3.89 | 2021 | 22.88 | 32.88 | 5.0 (2028) | +27.88 |
| 6.45 | 2022 spike | 37.95 | 47.95 | 3.4 (2030) | +44.55 |

**Critical conclusion:** For Bloom's marginal cost to equal 8hr BESS SCOE, the fuel cost component would need to be negative ($−3.9/MWh) — requiring Henry Hub below $0/MMBTU. Structurally impossible under any normal market condition. Lower gas prices reduce Bloom's LCOE disadvantage for new-build procurement comparisons, but they do not change the dispatch order. BESS is ALWAYS cheaper to dispatch than Bloom, at every gas price above zero. This is the definitive cost-curve dynamics statement: stellar energy technology (zero marginal cost) structurally dominates X-Flow technology (positive marginal cost) at every dispatch decision.

---

### Annual Fuel Cost Exposure (Full Fleet)

**Bloom full fleet = 1.756 BCM/yr (2024) [model-derived]; Henry Hub prices [T2: Natural_Gas_Price_USA.json] [CAUTION: EIA source — historical data only, observed]**

| Scenario | Henry Hub ($/MMBTU) | Annual Fuel Cost | % of Bloom 2024 Revenue |
|---------|---------------------|-----------------|--------------------------|
| 2024 historic low | 2.19 | $0.139B/yr | 9% |
| 5yr average 2020–2024 | 3.42 | $0.216B/yr | 15% |
| 2022 spike | 6.45 | $0.408B/yr | 28% |

*Fuel cost conversion: 1 BCM = 36.02 TBTU = 36.02×10⁶ MMBTU [model-derived]; Bloom 2024 revenue = $1.47B [observed: Bloom 10-K 2024]*

**Note:** Most Bloom service contracts include fuel cost pass-through provisions. This means Bloom customers — not Bloom itself — absorb Henry Hub volatility. However, at contract renewal, high historical gas costs provide procurement officers with a quantified justification to switch to SWB. At the 2022 gas spike, customers were implicitly paying a $408M/yr fuel surcharge across the fleet — a powerful retrospective argument for switching via S-curve adoption of SWB alternatives.

---

### Bloom Fleet Gas Trajectory (USA Fleet, 840 MW Starting Point)

**All values: [model-derived] from dispatch agent 08a; BCM computed with formula stated above**

| Year | Bloom USA (GWh/yr) | BCM USA | BCM Full Fleet | BCM Displaced vs 2024 | BESS Standard | % of 2024 |
|------|-------------------|---------|----------------|-----------------------|---------------|-----------|
| 2024 | 6,990 | 1.229 | 1.756 | 0 (baseline) | 4hr | 100% |
| 2026 | 6,823 | 1.200 | 1.714 | 0.042 | 4hr | 97.6% |
| 2028 | 6,589 | 1.159 | 1.656 | 0.100 | 6hr | 94.3% |
| 2030 | 6,269 | 1.102 | 1.574 | 0.182 | 8hr | 89.7% |
| 2032 | 5,842 | 1.027 | 1.467 | 0.289 | 8hr | 83.6% |
| 2034 | 5,291 | 0.930 | 1.329 | 0.427 | 12hr | 75.7% |
| 2036 | 4,605 | 0.810 | 1.157 | 0.599 | 16hr | 65.9% |
| 2038 | 3,784 | 0.665 | 0.950 | 0.806 | 16hr | 54.1% |
| 2040 | 2,837 | 0.499 | 0.713 | 1.043 | 16hr | 40.6% |

**Revenue implication:** Each BCM of Bloom incumbent displacement = ~$563M in lost revenue at $99/MWh Series 10 pricing [model-derived: 1 BCM = 5,687 GWh at 58% efficiency; $99/MWh × 5,687 GWh = $563M]. By 2040, Bloom's USA fleet has displaced 0.730 BCM (0.730 × $563M = ~$411M/yr in lost revenue from 2024 baseline), confirmed by the dispatch agent's GWh-based revenue analysis.

---

### LNG Exporter Vulnerability Assessment

| Risk Tier | Companies | Exposure Type | Key Risk |
|-----------|-----------|---------------|----------|
| High | Venture Global, Woodside, NextDecade, New Fortress, Golar | Spot/unsanctioned or recently FID'd | Demand collapse before project payback on 30yr asset life; incumbent displacement by stellar energy accelerates |
| Lower (but not safe) | Cheniere | Take-or-pay contracts through 2040s | Revenue floor through 2040s, but volume utilization falls; no growth pathway as S-curve adoption of SWB scales |
| Stranded infrastructure risk | All US LNG terminals if China → near-zero | Export capacity overhang | 147 BCM US surplus + China LNG demand collapse = structural spot price collapse; terminals built for $7–10/MMBTU break-even face $3–5/MMBTU spot |

**Financial cascade logic (no stabilization):** When LNG spot prices fall below $5/MMBTU (oversupply from demand collapse + US export surplus): (1) marginal exporters breach break-even; (2) project cancellations cascade (FID deferrals, construction halts); (3) stranded infrastructure — terminals built for 30-year life face < 50% utilization; (4) no stabilization mechanism — the cost-curve dynamics of stellar energy (SWB) have no floor — they continue declining at -13.5%/yr (solar) and -15.8%/yr (BESS), preventing any LNG demand recovery.

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 9.1 | HIGH | **PASS** | GWh→BCM conversion with explicit formula | Formula stated: BCM = GWh × 3.6 / (35.3 × 0.58) / 1000. SOFC efficiency 0.58 (not CCGT 0.45). Cross-validated against dispatch agent to within 0.7%. |
| 9.2 | HIGH | **PASS** | Supply sources ordered by cost/priority per region | USA: domestic shale (cheapest) → pipeline → LNG imports (near-zero). China: domestic (cheapest) → pipeline → LNG (most expensive, first displaced). Europe: North Sea → Norwegian pipeline → Qatar LNG → US LNG (first displaced). |
| 9.3 | HIGH | **PASS** | ≥3 regions covered | USA (primary — Bloom's market), China (global LNG context), Europe (LNG cascade context). |
| 9.4 | MEDIUM | **PASS** | LNG displacement priority stated per region | USA: no LNG imports (net exporter). China: LNG first displaced (domestic + pipeline cheaper at every volume). Europe: US LNG first displaced (highest delivered cost $7–9/MMBTU), Qatar second. Rationale quantified in each case. |

---

### Data Gaps

1. **China pipeline import breakdown.** The 64.0 BCM pipeline figure [model-derived: total imports 161.8 BCM minus LNG 97.8 BCM] combines Central Asia (Turkmenistan/Kazakhstan via CACG pipeline) and Russia (Power of Siberia). The sub-split between sources is not directly in the catalog. Estimate: Central Asia ~48–52 BCM, Russia ~12–16 BCM based on public reporting. This does not affect the core LNG displacement conclusion.

2. **Bloom Korea gas supply chain.** Korea (~120 MW, ~30% of Bloom non-USA fleet) is supplied by Korean domestic gas distribution, which is predominantly LNG-sourced (Korea Gas Corporation imports). This means Bloom's Korea operations DO have LNG input exposure — unlike USA. The Korea fleet is not modeled explicitly in this agent due to data limitations. This is a secondary gap; Korea is ~15–18% of Bloom revenue.

3. **European gas consumption catalog.** Europe NG consumption total is not directly in the catalog for the non-power segments. Sectoral breakdown (power/industrial/heating/feedstock) is estimated from the gas-supply-ordering reference proportions rather than direct European data.

4. **US LNG export volume by destination.** The US LNG export volume attributable to China vs Europe vs other destinations is not in the catalog. This matters for the cascade analysis — if China's LNG demand declines, which US export terminals lose the most volume? This detail is not required for the Bloom investment thesis but is relevant for LNG exporter vulnerability assessment.

5. **Bloom contract fuel pass-through terms.** The degree to which Bloom passes Henry Hub volatility to customers vs. absorbs it in margin is not disclosed in public filings. If Bloom bears significant fuel price risk directly, the 2022 gas spike ($6.45/MMBTU) would have materially impaired Bloom's gross margins. If passed through, it raises customer renewal motivation — supporting the short thesis on S-curve adoption of SWB alternatives at renewal.

---

### Critical Assumptions

1. **Bloom SOFC efficiency = 0.58** (58%). Source: Bloom Energy Server datasheet 2024 [observed]. This is the central efficiency assumption for all BCM calculations. Bloom quotes 54–60% electrical efficiency range; 0.58 is the midpoint and matches dispatch agent's BCM figures to within 0.7%.

2. **USA fleet = 70% of global installed base (840 MW of 1.2 GW).** Based on Bloom investor communications and deal geography (US deals dominate public announcements). The dispatch agent models USA only; full-fleet figures scale by 1200/840 = 1.429.

3. **All Bloom gas demand is natural gas from domestic US shale.** Bloom offers biogas and hydrogen capability but the overwhelming majority of operating deployments run on pipeline natural gas. No LNG is consumed in the US Bloom fleet.

4. **China supply source ordering follows coal-before-gas merit order.** Gas MC (~$70/MWh) > coal MC (~$35/MWh) means SWB first displaces gas generation (not coal), reducing total gas demand and exposing LNG as the marginal supply source. This ordering is from dispatch_parameters.json and China power market fundamentals.

5. **Henry Hub gas price will not go durably negative.** This is the structural floor assumption. If gas prices went negative (as has happened episodically during Permian basin curtailment events), Bloom's fuel cost would be zero or negative — but this is a temporary anomaly, not a durable competitive state.

---

## Sources

- `output/bloom-energy-sofc-disruption/agents/08a-energy-dispatch.md` — Gas displacement schedule (BCM by year), merit order stack, Bloom USA generation trajectory, SOFC efficiency = 0.58 [model-derived from observed inputs]
- `output/bloom-energy-sofc-disruption/agents/01-domain-disruption.md` — Bloom installed base 1.2 GW, SOFC X-Flow classification, revenue $1.47B 2024, SOFC efficiency 54–60% [observed: Bloom 10-K 2024, Bloom Energy Server datasheet 2024]
- `data/natural_gas/adoption/Natural_Gas_Annual_Consumption_USA.json` — US gas consumption 923.67 BCM (2023) [CAUTION: EIA source — historical data only, observed]
- `data/natural_gas/adoption/Natural_Gas_Annual_Production_USA.json` — US gas production 1,070.46 BCM (2023) [CAUTION: EIA source — historical data only, observed]; net surplus confirms zero LNG import dependency
- `data/natural_gas/cost/Natural_Gas_Price_USA.json` — Henry Hub prices 1997–2024: $2.03 (2020) to $6.45 (2022) to $2.19 (2024) [CAUTION: EIA source — historical data only, observed]
- `data/natural_gas/adoption/Natural_Gas_Annual_Consumption_China.json` — China gas consumption 395.34 BCM (2023) [CAUTION: EIA source — historical data only, observed]
- `data/natural_gas/adoption/Natural_Gas_Annual_Production_China.json` — China gas production 239.40 BCM (2023) [CAUTION: EIA source — historical data only, observed]
- `data/natural_gas/adoption/Natural_Gas_Annual_Import_China.json` — China total gas imports 161.81 BCM (2023) [CAUTION: EIA source — historical data only, observed]
- `data/natural_gas/adoption/Liquefied_Natural_Gas_Annual_Import_China.json` — China LNG imports 97.8 BCM (2023), 107.64 BCM (2024) [T2: Energy Institute Statistical Review of World Energy, observed]
- `data/natural_gas/adoption/Liquefied_Natural_Gas_Annual_Import_Europe.json` — Europe LNG imports 172.1 BCM (2022), 169.1 BCM (2023) [T2: Energy Institute Statistical Review of World Energy, observed]
- `data/natural_gas/cost/Liquefied_Natural_Gas_Export_Price_USA.json` — US LNG export price $6.41/Mcf ($6.28/MMBTU) in 2024 [CAUTION: EIA source — historical data only, observed]
- `.claude/skills/stdf/references/gas-supply-ordering.md` — Regional supply stack ordering methodology, LNG exporter vulnerability tiers, non-power gas demand shares
- `data/energy_sector/config/dispatch_parameters.json` — China gas MC $70/MWh, coal MC $35/MWh (merit order basis)
- [Bloom Energy Server Datasheet 2024](https://www.bloomenergy.com/wp-content/uploads/bloom-energy-server-datasheet-2024.pdf) — SOFC electrical efficiency 54–60%, heat rate 5,811–7,127 Btu/kWh [T3: Bloom Energy, observed]
- [Bloom Energy 2024 Annual Report (10-K)](https://www.sec.gov/Archives/edgar/data/1664703/000162828025016212/a202410kars.pdf) — Revenue $1.47B, installed base 1.2 GW [T3: observed]
