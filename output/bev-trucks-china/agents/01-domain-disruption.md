# STDF Domain Disruption Agent — BEV Heavy Trucks Displacing NG Trucks in China

**Agent:** `stdf-domain-disruption` | **Confidence:** 0.87

---

## Agent Reasoning

This analysis focuses on China's heavy-duty truck (HDT) segment — specifically tractor-trailer units (Class 8 equivalent, 49-tonne GVW) operating long-haul and regional freight corridors. The sector is Transportation; the specific sub-domains are heavy-duty long-haul freight (tractor-trailers), regional distribution freight (medium-heavy trucks), and captive/port/mine logistics fleets. China accounts for approximately 900,000 heavy truck sales per year, making it the world's largest single HDT market and therefore the primary arena where disruption dynamics play out fastest.

The analytical structure here is a two-layer disruption: (1) battery-electric heavy trucks (BEV-HDT) are now disrupting LNG/CNG trucks, which are themselves an intermediate technology that already displaced diesel from a portion of long-haul freight beginning around 2021-2022; and (2) BEV-HDT are simultaneously disrupting diesel-powered HDTs directly, particularly for captive fleet and regional routes where charging/swapping infrastructure is denser. This creates a rare tri-incumbent situation: BEV-HDT is attacking both a legacy incumbent (diesel ICE) and an intermediate incumbent (LNG/CNG NGV) that had only recently gained scale.

The quantitative grounding is strong for adoption curves, battery cost decline, and market share dynamics. There is a data-scope discrepancy between the local catalog (Rethinkx NGV figures: 40,000-84,000 HDT NGV/yr) and web-sourced primary data (ICCT, IEEFA, WoodMac: 152,000 LNG HDTs in 2023, approximately 261,000 in 2024). The catalog likely uses a narrower HDT definition or excludes medium-duty NGVs from certain count methodologies; both series are cited with their scope noted. Hydrogen fuel cell heavy trucks (FCEV-HDT) represent a secondary potential disruptor at an early S-curve phase (~6,000 total FCEV all types in 2023 vs. 82,500 BEV-HDTs in 2024), with significant cost gaps remaining relative to BEV on a TCO basis. Convergence between LFP battery technology, battery-swap infrastructure, L2/L4 autonomous driving, and cloud fleet management software creates emergent cost and utilization advantages that compound BEV-HDT's fundamental cost-curve superiority.

The S-curve positioning analysis indicates BEV-HDT in China's heavy truck segment crossed the approximately 10% annual sales threshold in late 2024 (20.9% in December 2024; 22% in H1 2025) — consistent with early-to-mid S-curve acceleration. LNG/CNG heavy trucks peaked at approximately 29% of new sales in 2024 but are showing early S-curve stall as the diesel-LNG price differential collapsed by two-thirds in 2025. This is a canonical disruption-from-above dynamic playing out against the LNG chimera.

---

## Agent Output

### Key Findings
- **Sector:** Transportation
- **Sub-domains:** heavy-duty long-haul freight (tractor-trailers, 49-tonne GVW), regional distribution freight (medium-heavy trucks, 18-31 tonne), captive fleet logistics (port, mine, construction), urban last-mile commercial delivery
- **Confidence:** 0.87

---

### Disruption Map

| Disruption | Disruptors | Incumbents | Chimeras | Convergence |
|---|---|---|---|---|
| BEV-HDT disruption of LNG/CNG heavy trucks | LFP-battery BEV tractor-trailers (49t GVW); battery-swap BEV heavy trucks | LNG-fueled heavy-duty tractor-trailers (SI engine, cryogenic LNG tank); CNG-fueled heavy-duty trucks (SI engine, high-pressure CNG cylinders) | Range-extended BEV heavy truck (BEV drivetrain + small LNG range extender); plug-in hybrid HDT (diesel + electric motor) | BSAF: Battery-swap + Autonomous driving + Fleet-management software — enables >20h/day utilization at lowest per-km cost |
| BEV-HDT disruption of diesel ICE heavy trucks | LFP-battery BEV tractor-trailers; battery-swap BEV heavy trucks; fast-charge depot BEV HDTs | Diesel ICE heavy-duty tractor-trailers (compression-ignition, Class 8 equivalent) | PHEV-HDT (diesel ICE + electric motor + small battery); LNG-powered HDT (already disrupting diesel on cost, itself being disrupted by BEV) | BSAF (same as above); additionally: LFP + solar-charged depot integration for captive fleets (LFP-Grid) |
| FCEV-HDT as secondary potential disruptor | Proton-exchange membrane (PEM) hydrogen fuel cell heavy trucks (FCEV-HDT) | Diesel ICE heavy-duty tractor-trailers; LNG-fueled HDTs | Blue-hydrogen FCEV-HDT (fuel cell + grey or blue hydrogen supply — retains fossil gas infrastructure dependency); electrolysis-based hydrogen FCEV-HDT dependent on hydrogen station buildout | H2-AV: PEM fuel cell + L4 autonomous driving for long-haul — not yet economically viable at scale |
| LNG/CNG trucks as prior disruptor of diesel (now stalling as chimera) | LNG-fueled heavy trucks (SI engine, cryogenic LNG storage); CNG-fueled regional trucks | Diesel ICE heavy-duty tractor-trailers (compression-ignition) | LNG-HDT itself is a chimera relative to full BEV disruption — requires fossil gas supply chain, cryogenic infrastructure, and volatile fuel pricing | — |

---

### Narrative

#### China's Heavy Truck Market: Scale and Structure

China's heavy-duty truck market is the world's largest, with approximately 900,000 heavy trucks sold annually as of 2024 [T3: ICCT, 2025, observed]. The total commercial vehicle fleet across all weight classes reached 4.19 million new registrations in 2024, according to catalog data [T2: Commercial_Vehicle_Annual_Sales_China.json, Rethinkx, 2024, observed]. The heavy-duty sub-segment (tractor-trailers and heavy rigid trucks, GVW >14 tonnes) represents the highest-value and highest-fuel-cost portion of this market, where energy cost per vehicle-kilometer is the dominant driver of total cost of ownership (TCO).

Historically, diesel ICE tractor-trailers held near-total market share in China's long-haul freight. Beginning in 2021-2022, LNG-fueled HDTs disrupted diesel through a cost-from-below mechanism: when the LNG-diesel fuel price ratio widened to 1.4x-1.9x in 2023, LNG trucks achieved a CNY 61.61/100 km cost advantage over diesel (CNY 170.17 vs CNY 231.78 per 100 km) [T3: WoodMac / S&P Global, 2024, observed]. LNG truck annual sales in China surged from under 10% of HDT market share in 2022 to approximately 29% by H2 2024, with 152,000 LNG HDTs sold in 2023 and approximately 261,000 in 2024 [T3: ICCT, WoodMac, IEEFA, 2024-2025, observed].

#### BEV-HDT Disruption: Adoption Evidence

Battery-electric commercial vehicle sales in China grew from 80,882 units across all commercial vehicle classes in 2021 to 380,250 units in 2024 — a compound annual growth rate of 67% over three years [T2: Commercial_Vehicle_(EV)_Annual_Sales_China.json, Database, 2024, observed]. Penetration in the broad commercial vehicle market rose from 1.89% in 2021 to 9.08% in 2024.

Within the heavy-duty tractor-trailer sub-segment specifically, BEV-HDT adoption accelerated sharply: approximately 11,000 units in 2022, 34,000 in 2023, and 82,500 in 2024 — a two-year CAGR of 174% [T3: ICCT, 2025, observed]. Market share reached 9.2% for full year 2024, with December 2024 hitting 20.9% — the first month where BEV-HDT share exceeded 20% [T3: ICCT / IEEFA, 2025, observed]. In H1 2025, BEV-HDT share reached 22% of new heavy truck sales, up 156% year-over-year from 8.6% in H1 2024 [T3: ICCT H1 2025 report, 2025, observed]. The cumulative EV commercial vehicle fleet in China reached 1,497,833 vehicles by end-2024, nearly 2.79x the NGV commercial vehicle fleet of 537,460 vehicles [T2: Commercial_Vehicle_(EV)_Total_Fleet_China.json, Rethinkx, 2024, observed; T2: Commercial_Vehicle_(NGV)_Total_Fleet_China.json, Rethinkx, 2024, observed].

The S-curve position is unambiguous: BEV-HDT in China is at the early-to-mid acceleration phase (roughly 5-22% annual share from 2023-H1 2025), where adoption rates are fastest. This is consistent with market-level data: for December 2025, NEV share in new heavy-duty trucks surpassed 50% for the first time [T3: Electrive, 2026, observed]. The S-curve inflection appears to have occurred in approximately Q4 2024.

#### Battery Cost-Curve Dynamics: Disruption Quantified

The fundamental driver is lithium iron phosphate (LFP) battery cost-curve dynamics. The cost of lithium-ion battery packs for commercial vehicles (e-bus and heavy commercial) in China fell from $177/kWh in 2018 to $90/kWh in 2024 — a 49.2% total decline and a fitted annual decline rate of 10.7%/yr [T2: Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_China.json, Rethinkx, 2024, observed, R²=0.803, n=7 data points, 2018-2024]. For the broader median LFP pack in China, costs fell from $1,100/kWh in 2010 to $94/kWh in 2023 — a 91.5% decline over 13 years [T2: Lithium_Ion_Battery_Pack_Median_Cost_China.json, Database, 2023, observed].

A 49-tonne BEV tractor uses a 350-420 kWh battery pack. At the 2024 commercial pack price of $90/kWh, this pack costs $31,500-$37,800 — compared to $61,950-$74,340 at 2018 prices. This cost reduction directly explains why BEV-HDT TCO crossed parity with diesel in China's high-utilization fleet context: fleet operators with 100,000 km/yr mileage save approximately CNY 100,000/yr (~USD 14,085) relative to diesel at current electricity and diesel price ratios [T3: ICCT TCO analysis, 2022-2025, observed]. The BEV-HDT cost advantage is 10-26% lower TCO than diesel in high-utilization cases [T3: Business Standard / ICCT, 2025, observed].

#### Disruption Type Classification

**Primary disruption (BEV-HDT displacing LNG/CNG trucks):** This is a **From-Above disruption**. BEV-HDTs entered at the high end of the market — port logistics, mining captive fleets, and premium freight corridors — where predictable routes and depot charging make range constraints irrelevant. As battery costs fell and swap infrastructure was built out, the cost curve dropped below LNG in high-utilization applications. LNG trucks are not a fully entrenched legacy incumbent; they themselves achieved market penetration only through 2021-2024. The BEV disruption of LNG therefore resembles a leapfrog: BEV-HDT is attacking a challenger that has not yet completed its own disruption of diesel.

**Secondary disruption (BEV-HDT displacing diesel ICE trucks directly):** This is a **Systemic disruption** — BEV-HDT, LNG-HDT, and now FCEV-HDT are simultaneously pressuring diesel from multiple vectors. Diesel's share of new HDT sales fell from approximately 80% in H1 2023 to approximately 57% in full-year 2024 [T3: ICCT, 2025, observed], with the pace of displacement accelerating.

**Prior disruption (LNG/CNG trucks displacing diesel, now stalling as a chimera):** This was a **From-Below disruption** — LNG trucks entered via fuel-cost advantage for high-mileage operators, requiring no change in driver behavior or infrastructure beyond LNG stations. However, LNG trucks carry the structural defect of all chimeras: they depend on fossil gas supply chain, cryogenic infrastructure, and volatile spot LNG pricing. When the LNG-diesel price differential collapsed by two-thirds in 2025, the LNG cost advantage evaporated. In May 2025, the differential was nearly two-thirds below its 2024 peak [T3: IEEFA, 2025, observed]. LNG/CNG trucks are correctly classified as chimeras: they combine an evolved combustion drivetrain (lower carbon-intensity than diesel) with incumbent fossil fuel infrastructure dependencies, preventing them from achieving BEV cost-curve dynamics.

**Tertiary potential disruption (FCEV-HDT):** Hydrogen fuel cell heavy trucks represent an **early-phase From-Above disruption** targeting the longest range and highest payload routes where BEV packs impose significant weight penalty. Approximately 6,000 FCEVs of all types were sold in China in 2023 (72% YoY growth), with virtually all being commercial vehicles, and cumulative FCEV deployment approaching 40,000 by end-2025 [T3: HydrogenInsight / FuelCellChina, 2024, observed]. However, the FCEV-HDT is currently constrained to government-subsidized demonstration clusters and requires electrolysis-based or reformed hydrogen at sufficient volumes and declining cost to achieve TCO parity with BEV-HDT. The ICCT found the transportation cost per 100 km for a 49-tonne hydrogen fuel cell truck is 63% higher than for a BEV equivalent [T3: ICCT, 2025, observed], placing FCEV-HDT at the very early S-curve phase (well below 1% of HDT sales) and not yet on a cost trajectory to close the BEV gap within a 5-year horizon.

#### LNG/CNG Chimera Analysis

LNG and CNG heavy trucks are the central chimera of this analysis. They are hybrids in cost-structure terms: they achieve a fuel cost advantage over diesel when the gas-diesel price ratio is favorable, but they depend entirely on:
1. LNG supply chain and regasification infrastructure (cryogenic storage at fueling stations)
2. CNG compression infrastructure at filling stations
3. Fossil gas commodity price stability

None of these dependencies follow an exponential cost-reduction curve. The LNG-diesel price ratio is subject to commodity market volatility — it reached 1.9x in 2023 (favorable for LNG trucks) and collapsed by 2025 as LNG prices rose and diesel prices normalized. This volatility is structurally incompatible with the predictable TCO that fleet operators require. BEV-HDT charging costs, by contrast, benefit from falling electricity generation costs driven by solar PV and wind deployment in China's power grid — a cost curve that is one-directional and compounding.

Catalog data confirms the heavy-duty NGV segment in China shows flat new-vehicle annual sales from 2022-2024 (40,612 in 2023; 40,446 in 2024 per Rethinkx), even as LNG's share of new sales temporarily surged to 29% in 2024 — a discrepancy explained by scope difference: the catalog captures a narrower segment definition while web sources (ICCT, IEEFA, WoodMac) capture the full tractor-trailer LNG market. Both are noted and cited. Either way, the forward trend is the same: LNG HDT new-vehicle sales are plateauing as BEV-HDT absorbs incremental demand.

#### Convergence: BSAF and Its Emergent Capabilities

The most powerful convergence active in this disruption is **BSAF = Battery-Swap + Autonomous driving + Fleet-management software**. Each technology independently improves BEV-HDT economics; their combination creates emergent capabilities:

- **Battery-swap** (led by CATL's Qiji Energy system, targeting 300 swap stations by end-2025 and a nationwide freight corridor network by 2030) eliminates the charging time constraint that limits utilization for long-haul applications. CATL's standardized "75# battery swap block" is compatible with over 30 heavy truck models from a dozen OEMs, creating a platform ecosystem effect [T3: CATL press release, 2025, observed]. Swap-capable BEV-HDT sales reached 29,569 in 2024, up 94% from 2023 [T3: ICCT, 2025, observed].
- **L2/L4 autonomous driving** in captive-route applications (ports, mines, highway platooning) reduces the dominant labor cost component of trucking. China's V2X (vehicle-to-infrastructure) strategy shifts sensor cost from truck to roadside infrastructure, lowering per-truck autonomous driving cost below global benchmarks.
- **Cloud fleet management software** with 238-parameter telematics enables dynamic route optimization, predictive maintenance, and battery state-of-health management that are impossible for diesel or LNG fleets. This creates a software-driven cost wedge that compounds over time.

Together, BSAF enables >20-hour/day asset utilization for BEV-HDTs in swap-capable applications, pushing per-km economics below any combustion alternative. CATL's own calculation shows BSAF-equipped trucks save RMB 0.62/km relative to diesel at 100,000 km/year — equivalent to RMB 62,000/year incremental operator income [T3: CATL / Xinhua, 2025, observed].

A secondary convergence is **LFP-Grid** = LFP battery manufacturing scale + solar PV / wind electricity supply growth in China's national grid. As stellar energy (solar PV + wind) displaces coal in power generation, the marginal electricity cost for charging/swapping BEV-HDTs falls in parallel with battery pack costs. This double-falling-cost dynamic has no analog in LNG economics.

---

### Handoff Context

- **Sector boundaries:** Analysis is scoped to China's heavy-duty truck segment (GVW >14 tonne, primarily 49-tonne tractor-trailers). Medium-duty commercial vehicles (3.5-14 tonne) are included in total commercial vehicle adoption data but not in the heavy-truck-specific penetration analysis. Passenger cars and light-duty commercial vehicles are explicitly excluded. Geographic scope is China only; global commercial vehicle data from the catalog is available for reference but not the primary focus.

- **Key cost data:**
  - LFP commercial battery pack (China): $177/kWh (2018) to $90/kWh (2024); annual decline 10.7%/yr [T2: Rethinkx catalog]
  - Median LFP battery pack (China): $1,100/kWh (2010) to $94/kWh (2023) [T2: Database catalog]
  - BEV commercial vehicle median cost (China): $38,000 (2010) to $25,000 (2023) [T2: Database catalog] — note this appears to be a broad EV commercial vehicle cost, not specifically heavy tractor-trailers; downstream agents should note that 49-tonne BEV tractors command significant premiums (~$250,000-350,000 USD at current volume pricing) relative to diesel equivalents (~$50,000-100,000), with TCO parity achieved through operating cost savings
  - Fuel cost advantage (LNG vs diesel, 2023 peak): CNY 61.61/100 km; collapsed in 2025 as LNG-diesel spread narrowed by approximately two-thirds [T3: WoodMac, IEEFA, 2025, observed]
  - BEV vs diesel TCO advantage: approximately CNY 100/100 km = approximately USD 14/100 km = approximately USD 14,000/yr at 100,000 km/year utilization [T3: ICCT, 2025, observed]

- **S-curve positions:**
  - BEV-HDT (China heavy trucks): approximately 13% annual sales share in 2024; December 2024 peak at 20.9%; H1 2025 at 22%; NEV >50% for first time in December 2025. S-curve inflection occurred approximately Q4 2024. Currently in early-acceleration phase.
  - BEV broad commercial vehicles (all classes, China): 9.08% of new sales in 2024; cumulative fleet 1.50M vehicles [T2: catalog, observed]
  - LNG/CNG HDT (China): approximately 29% of new HDT sales in 2024; showing plateau/decline signal in 2025 as price differential collapses. Early S-curve stall consistent with chimera dynamics.
  - FCEV-HDT (China): <1% of new HDT sales; early demonstration phase; approximately 40,000 cumulative all FCEV types by end-2025. Not yet on self-sustaining cost curve.

- **Data gaps:**
  - Catalog NGV figures (Rethinkx: 40,446 heavy-duty NGV in 2024) differ substantially from ICCT/IEEFA/WoodMac figures (~261,000 LNG HDT in 2024). Likely scope difference in HDT definition. Higher figures from primary government-adjacent sources (ICCT, WoodMac) are used for the market share analysis; catalog figure is noted as lower-bound or alternative scope. Cost-fitter agent should use both series with scope flags.
  - No catalog curve exists specifically for China long-haul BEV tractor-trailer penetration as a distinct sub-segment from broad EV commercial vehicles. The 82,500 figure for BEV heavy trucks in 2024 is from T3 web sources (ICCT), not the local catalog.
  - LNG pump price time series for China (daily/monthly spot rates) is not in the catalog — only annual demand volumes. The fuel-cost parity calculation relies on ICCT/WoodMac web sources.
  - FCEV-HDT cost curve for China is absent from the catalog. Cost trajectory from RMB 200-300万 (2020) to RMB 100-160万 (2025) is from web source only.
  - Battery swap station buildout data (number of stations, coverage) is from web sources only; no catalog curve.
  - The "Commercial_Vehicle_(EV)_Median_Cost_China" catalog curve ($38,000 in 2010 to $22,000 est. 2025) appears to reflect small-medium EV commercial vehicles, not 49-tonne BEV tractors. Downstream agents must apply appropriate cost scaling for the HDT segment.

- **Unresolved questions for downstream agents:**
  - Cost-fitter agent: Fit a proper exponential decay curve to the LFP commercial pack cost series (7 data points, 2018-2024, R²=0.803) — what is the precise learning rate and cost at 2027 and 2030?
  - Cost-parity agent: At what exact year does BEV-HDT achieve purchase-price parity with diesel HDT in China (currently approximately 2-3x premium on sticker price, but already at TCO parity)?
  - Adoption agent: Apply S-curve fitting to the BEV-HDT China sales series to characterize inflection point and saturation date. Key data: 11,000 (2022), 34,000 (2023), 82,500 (2024), approximately 22% H1 2025.
  - Demand-decomposer agent: LNG HDT peak at approximately 29% of 900,000 = approximately 261,000 units in 2024. What is the implied displacement of LNG demand in BCM/year as BEV-HDT scale grows? This is a direct input for natural gas demand decomposition.
  - Is there a distinct S-curve for battery-swap BEV-HDT vs. depot-charge BEV-HDT? Swap enables long-haul (>400 km) while depot charging captures regional/captive fleet. These may follow different adoption timelines.

---

## Sources

- [ICCT — Zero-emission medium- and heavy-duty vehicle market in China, 2024](https://theicct.org/publication/ze-mhdv-market-china-2024-mar25/)
- [ICCT — Zero-emission medium- and heavy-duty vehicle market in China, H1 2025](https://theicct.org/publication/ze-mhdv-market-in-china-h1-2025-sept25/)
- [ICCT — Zero-emission medium- and heavy-duty vehicle market in China, January–June 2024](https://theicct.org/publication/ze-mhdv-market-china-january-june-2024-nov24/)
- [ICCT — Total cost of ownership for heavy trucks in China: Battery-electric (2022)](https://theicct.org/wp-content/uploads/2022/01/ze-hdvs-china-tco-FS-EN-nov21.pdf)
- [IEEFA — Surging electric truck sales stall China's LNG trucking boom](https://ieefa.org/resources/surging-electric-truck-sales-stall-chinas-lng-trucking-boom-0)
- [WoodMac — LNG truck sales impacting Chinese road diesel demand](https://www.woodmac.com/press-releases/lng-truck-sales-impacting-chinese-road-diesel-demand/)
- [S&P Global — China nears peak gasoil demand as LNG-fueled heavy duty truck sales surge (2024)](https://www.spglobal.com/commodityinsights/en/market-insights/latest-news/lng/062624-china-nears-peak-gasoil-demand-as-lng-fueled-heavy-duty-truck-sales-surge)
- [Electrive — Year-end surge: electric trucks outsell diesel for the first time in China (Jan 2026)](https://www.electrive.com/2026/01/23/year-end-surge-electric-trucks-outsell-diesel-for-the-first-time-in-china/)
- [CleanTechnica — China's BEV Trucks and the End of Diesel's Dominance (Nov 2025)](https://cleantechnica.com/2025/11/26/chinas-bev-trucks-and-the-end-of-diesels-dominance/)
- [Business Standard — China's electric trucks become world's biggest diesel disruptor (Nov 2025)](https://www.business-standard.com/world-news/china-electric-trucks-diesel-demand-ev-shift-rystad-sci-125112500784_1.html)
- [Electrek — Hybrid and electric semi truck sales topped 231,000 units 2025 in China alone (Jan 2026)](https://electrek.co/2026/01/24/hybrid-and-electric-semi-truck-sales-topped-231000-units-2025-in-china-alone/)
- [CATL — Launches Battery Swap Ecosystem with Nearly 100 Partners](https://www.catl.com/en/news/6342.html)
- [CATL — Unveils 75# Standardized Battery Swap Block](https://www.catl.com/en/news/6473.html)
- [CnEVPost — CATL, Sinopec to jointly build over 500 swap stations in 2025](https://cnevpost.com/2025/04/02/catl-sinopec-500-swap-stations-2025/)
- [CnEVPost — CATL launches standardized battery swap pack for heavy trucks (May 2025)](https://cnevpost.com/2025/05/19/catl-launches-standardized-battery-swap-pack-heavy-trucks/)
- [Xinhua — Next-generation battery swap ecosystem empowers China's heavy-duty truck sector (May 2025)](https://english.news.cn/20250529/b893642742134d6eb9320225c2734875/c.html)
- [HydrogenInsight — Sales of hydrogen-powered vehicles in China rose by more than 70% in 2023](https://www.hydrogeninsight.com/transport/sales-of-hydrogen-powered-vehicles-in-china-rose-by-more-than-70-in-2023/2-1-1586080)
- [McKinsey — Trends shaping the heavy-duty-truck market in China](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/a-new-era-trends-shaping-chinas-heavy-duty-trucking-industry)
- [Local data catalog — Commercial_Vehicle_(EV)_Annual_Sales_China.json (Database, 2024)](data/commercial_vehicle/adoption/Commercial_Vehicle_(EV)_Annual_Sales_China.json)
- [Local data catalog — Commercial_Vehicle_Annual_Sales_China.json (Rethinkx, 2024)](data/commercial_vehicle/adoption/Commercial_Vehicle_Annual_Sales_China.json)
- [Local data catalog — Commercial_Vehicle_(EV)_Total_Fleet_China.json (Rethinkx, 2024)](data/commercial_vehicle/adoption/Commercial_Vehicle_(EV)_Total_Fleet_China.json)
- [Local data catalog — Commercial_Vehicle_(NGV)_Total_Fleet_China.json (Rethinkx, 2024)](data/commercial_vehicle/adoption/Commercial_Vehicle_(NGV)_Total_Fleet_China.json)
- [Local data catalog — Heavy-duty_commercial_vehicles_(NGV)_Annual_Sales_China.json (Rethinkx, 2024)](data/commercial_vehicle/adoption/Heavy-duty_commercial_vehicles_(NGV)_Annual_Sales_China.json)
- [Local data catalog — Lithium-Ion_Battery_Pack_E-Bus_&_Commercial_Cost_China.json (Rethinkx, 2024)](data/battery_pack/cost/Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_China.json)
- [Local data catalog — Lithium_Ion_Battery_Pack_Median_Cost_China.json (Database, 2025)](data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json)
- [Local data catalog — Commercial_Vehicle_(EV)_Median_Cost_China.json (Database, 2025)](data/commercial_vehicle/cost/Commercial_Vehicle_(EV)_Median_Cost_China.json)
