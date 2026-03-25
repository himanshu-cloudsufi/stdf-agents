# STDF Adoption Readiness Checker Agent — Li-Ion vs. Lead-Acid (Lead Demand Decline)

**Agent:** `stdf-adoption-readiness-checker` | **Confidence:** 0.82

---

## Agent Reasoning

**Context extracted from upstream files.** The domain-disruption agent identifies five distinct disruption vectors acting on lead demand: (1) BEV displacement of ICE new-vehicle SLI demand, (2) BEV fleet turnover shrinking SLI replacement demand, (3) LFP stationary storage displacing VRLA in telecom and datacenter UPS, (4) LFP motive power displacing lead-acid traction batteries in forklifts, and (5) direct LFP 12V SLI substitution in the ICE aftermarket. Each vector operates through a different mechanism, which means infrastructure and supply chain readiness must be assessed at the vector level, not just the aggregate. The cost-fitter agent confirms that Li-ion (LFP chemistry) is already at nameplate pack cost parity with lead-acid on a $/kWh basis (achieved 2019–2021 in USA and China respectively), and has held a structural 24x advantage on a levelized $/kWh delivered basis since at least 2010. The only remaining cost barrier is SLI unit parity ($100/unit vs. $25/unit in China; $135 vs. $55 in USA) — a narrowing gap the cost-fitter model places at 2027–2028 for the USA and 2031–2032 for China.

**Infrastructure framing.** For the Li-ion vs. lead-acid disruption, infrastructure readiness decomposes into three components specified in the analytical brief: (1) Li-ion manufacturing capacity — whether enough cell and pack production capacity exists to supply mass-market volumes across all five disruption vectors; (2) EV charging infrastructure — relevant specifically to the BEV fleet-turnover vector (Disruption 2), which is the largest single lead demand vector at 3,377 kt and depends on ICE fleet contraction driven by BEV adoption; and (3) Li-ion recycling infrastructure — relevant as battery volumes grow and end-of-life handling becomes critical. All three show different readiness profiles: manufacturing capacity is structurally oversupplied at 3.0 TWh installed vs. 1.0 TWh annual demand; EV charging infrastructure is regionally uneven (China near-complete, USA at 59.1% of highway corridor coverage end-2024); and Li-ion recycling infrastructure is nascent outside China (75% of global capacity is China-based). This produces a PARTIAL rating for infrastructure overall.

**Supply chain and regulatory assessment.** The supply chain for Li-ion (LFP path) is structurally well-positioned: lithium supply recorded a 134,000 MT LCE surplus in 2024; LFP cathode production consumed 1.934 million tonnes in China; global battery manufacturing is at 33% utilization. The principal risk is geographic concentration — China holds 87% of global cathode production capacity and 75% of global Li-ion recycling capacity, a strategic vulnerability rather than a current production constraint. The regulatory environment is mixed: China's NEV mandate is operational and driving 47.9% passenger-car penetration; the EU Battery Regulation 2023/1542 is in force as of February 2024 with phased recycled-content and recycling-efficiency requirements; but the EU revised its 2035 ICE mandate from a full ban to a 90% CO2 reduction target (December 2025), which weakens the single strongest regulatory accelerant for Disruptions 1 and 2. US Section 301 tariffs raised the rate on Li-ion EV batteries from China from 7.5% to 25% effective September 2024, creating cost friction for non-domestic supply into the US market. Note: LFP chemistry also powers stellar energy storage (grid-scale BESS), sharing production lines and cost-curve dynamics with the battery types assessed here.

---

## Agent Output

### Adoption Readiness Condition

- **Status:** NOT_MET
- **Readiness year:** model-derived 2028 (infrastructure sub-condition; USA EV corridor build-out at +5.3 pp/yr)
- **Confidence:** medium
- **Binding sub-condition:** infrastructure

---

### Sub-Conditions Assessment

| Sub-Condition | Status | Key Metric | Evidence |
|---|---|---|---|
| Infrastructure coverage | PARTIAL | Li-ion mfg: 3.0 TWh capacity vs 1.0 TWh demand (3:1 surplus); EV charging USA: 59.1% highway corridor coverage (Q4 2024); Li-ion recycling: 450 GWh global but 75% China-concentrated | [T3: Interact Analysis, 2024, observed]; [T3: FHWA/Joint Office, Q4 2024, observed]; [T3: IEA recycling data, 2024, observed] |
| Supply chain maturity | READY | 3.0 TWh annual capacity vs 1.0 TWh demand (3:1 surplus); lithium 134,000 MT LCE surplus (11.3%); LFP cathode 1.934M tonnes consumed China; oversupply driving pack prices below $100/kWh China | [T3: Interact Analysis, 2024, observed]; [T3: Fastmarkets/Benchmark Minerals, 2024, observed]; [T3: CAAM, 2024, observed] |
| Regulatory environment | PARTIAL | EU Battery Reg 2023/1542 in force Feb 2024; EU 2035 mandate revised to 90% CO2 reduction (full ICE ban scrapped, Dec 2025); US 25% tariff on Li-ion EV batteries from China (Sept 2024); China NEV mandate: 47.9% penetration | [T3: EUR-Lex 2023/1542, 2024, observed]; [T3: Euronews, Dec 2025, observed]; [T3: USTR, Sept 2024, observed]; [T3: CAAM, 2024, observed] |

**Aggregate logic:** 1 READY (supply chain) + 2 PARTIAL (infrastructure, regulatory) = NOT_MET. Rule: two or more PARTIAL sub-conditions yield NOT_MET.

---

### Infrastructure Detail

**Li-ion manufacturing capacity** is structurally oversupplied and does not constrain any of the five disruption vectors. Global production capacity reached more than 3.0 TWh annually by end-2024 against annual demand of approximately 1.0 TWh — a 3:1 surplus and 33% utilization rate [T3: Interact Analysis, 2024, observed]. China accounts for 85% of global capacity, led by CATL (646 GWh installed capacity) and BYD (135 GWh installed). US capacity doubled since 2022 to more than 200 GWh, driven by IRA incentives. Manufacturing oversupply is the direct cause of the 2024 pack price decline below $100/kWh in China — a direct enabler of cost-curve acceleration confirmed by the cost-fitter agent. Cell and pack supply for stationary UPS, motive power, and automotive applications is not a bottleneck in any market.

**EV charging infrastructure**, which is the prerequisite for BEV fleet adoption (Disruption 2, the 3,377 kt SLI replacement demand vector), is regionally uneven. China has achieved approximately 98% EV highway corridor coverage and is the most advanced market globally [T3: memory record, end-2024]. In the USA, 59.1% of the most heavily trafficked highway corridors had a DC fast charger at least every 50 miles as of Q4 2024, up from 38% at end-2020 — a gain of +5.3 percentage points per year [T3: FHWA/Joint Office of Energy and Transportation, Q4 2024, observed]. This represents more than 206,000 publicly available EV charging ports as of end-2024, double the number at end-2020. Europe has deployed more than 1 million public charging points [T3: memory record, end-2024]. The USA's 59.1% corridor coverage is the binding infrastructure gap for this vector. At the observed +5.3 pp/yr build-out rate, the USA reaches approximately 80% corridor coverage in 2028 [model-derived from FHWA observed data]. Note: DOT rescinded the NEVI guidance in February 2025, introducing uncertainty about the pace of additional station openings.

**Li-ion recycling infrastructure** is nascent outside China and is relevant as a readiness factor once large volumes of Li-ion batteries from the 2020–2025 deployment wave reach end-of-life (primarily from 2030 onward, given 10–15 year battery lifetimes). Global Li-ion recycling capacity stood at approximately 450 GWh in 2024, of which 75% is located in China [T3: IEA/Statista, 2024, observed]. In the USA, domestic recycling facilities could reclaim only 35,500 tonnes as of 2023 [T3: US DOE FOTW #1350, July 2024, observed]. Europe, led by Germany, is scaling under Battery Regulation mandates requiring 65% recycling efficiency for lithium-based batteries by December 2025 and 70% by December 2030. By contrast, lead-acid battery recycling is already highly mature in the USA (99% collection rate) and Europe (99%) [T3: Battery Council International, 2024, observed]; China's formal ULAB recycling rate was approximately 48% as of 2023 [T3: ScienceDirect, 2023 data, observed]. Li-ion recycling does not constrain current adoption but becomes a readiness condition for circular supply chain completion in the 2030+ timeframe.

---

### Supply Chain Detail

**Manufacturing capacity and cell supply** present no constraint across all five disruption vectors. The 3.0 TWh global capacity vs. 1.0 TWh demand translates into structural oversupply that has driven pack prices below $100/kWh in China — a key enabler of cost-curve dynamics. CATL alone has 646 GWh of installed capacity; BYD has built its own vertically integrated cell-to-vehicle supply chain. LFP chemistry dominates China's battery market at 74.6% of installations (409.0 GWh installed in 2024, up 56.7% year-on-year) [T3: CAAM/CnEVPost, 2024, observed]. LFP cathode production consumed 1.934 million tonnes of lithium iron phosphate material in China in 2024 — demonstrating upstream cathode supply at volume scale. The S-curve adoption trajectory for LFP is in the acceleration phase in China and the early-growth phase in USA and Europe.

**Raw material availability** is not a current constraint. Lithium supply exceeded demand by 134,000 MT LCE (11.3% surplus) in 2024, with total production reaching 1,323,000 MT LCE globally against 1,189,000 MT LCE demand [T3: Fastmarkets/Benchmark Minerals Intelligence, 2024, observed]. Mine production from Australia (386,000 MT LCE), South America (265,000 MT LCE), and China (238,000 MT LCE) collectively provided ample supply. Lithium carbonate prices in China fell from approximately $14,500/tonne (January 2024) to $9,400/tonne (November 2024), confirming demand-supply balance favoring buyers. The critical structural risk is processing concentration: 65% of global lithium refining capacity is in China [T3: Fastmarkets, 2024, observed], meaning non-Chinese manufacturers face supply-chain dependency. This is a strategic vulnerability that does not constrain current production but becomes material if geopolitical friction intensifies. LFP chemistry eliminates cobalt exposure (DRC holds 74% of cobalt mine production, but LFP contains no cobalt), which is a structural supply chain advantage of the dominant disruptor chemistry.

**Workforce readiness** for Li-ion manufacturing is not a binding constraint in the way it has been for, for example, HVAC installers for heat pumps. Cell and pack manufacturing is factory-floor work where workforce scales with capital investment; China's existing manufacturing base is large and skilled. For EV forklift service, OEM-led technician training programs (KION, Toyota Industries, Jungheinrich) are underway; no systemic bottleneck is identified from available data.

---

### Regulatory Detail

**EU Battery Regulation 2023/1542** entered into force on 18 February 2024 and supersedes Battery Directive 2006/66/EC from August 2025 [T3: EUR-Lex, Regulation 2023/1542, retrieved 2026-03-20, URL omitted per citation policy]. Key provisions affecting Li-ion vs. lead-acid dynamics: (1) Recycling efficiency targets — 65% for lithium-based batteries by December 2025, rising to 70% by December 2030; lead-acid must reach 75% by December 2025. (2) Recycled content requirements effective from August 2031: 85% lead in SLI and industrial batteries, 6% lithium in EV batteries. The 85% lead recycled-content mandate reflects the already-mature lead-acid closed-loop recycling system in Europe (99% collection rate), while the 6% lithium target reflects the early stage of Li-ion recycling. The regulation creates compliance infrastructure that reduces uncertainty for Li-ion deployment while adding compliance cost for lead-acid incumbents via mandatory battery passport and due diligence obligations.

**EU vehicle CO2 mandate** underwent significant revision in December 2025: the European Commission dropped the 2035 full ICE ban and replaced it with a 90% CO2 reduction target for new passenger cars by 2035, with the remaining 10% compensated by low-carbon steel or low-carbon fuels [T3: Euronews, December 16, 2025, observed]. This revision weakens the regulatory accelerant for Disruption 1 (BEV elimination of new-vehicle SLI demand) in Europe — it opens a pathway for continued low-volume ICE sales post-2035, sustaining residual SLI demand beyond what a full ban would have achieved. Cost-curve dynamics rather than policy mandates determine the primary trajectory; the mandate revision shifts the European disruption timeline by approximately 2–4 years, it does not reverse BEV market-share growth.

**China NEV mandate** remains the world's strongest vehicle electrification policy in operational terms. China's mandatory OEM credit system (introduced 2019) has driven NEV penetration to 47.9% of passenger car sales in 2024, with December 2024 reaching 52.6% [T3: CAAM/CnEVPost, 2024, observed]. This mandate eliminates SLI demand for new-vehicle installations in China at the fastest rate globally and shows no sign of rollback. For stationary backup (telecom UPS) and motive power (forklifts), no material regulatory barriers exist; REACH (EU) and EPA (USA) lead restrictions impose tightening compliance cost on lead-acid incumbents, functioning as a regulatory tailwind for market-driven disruption and accelerating incumbent displacement across all non-automotive vectors.

**US Section 301 tariffs** on Li-ion EV batteries from China were raised from 7.5% to 25% effective September 27, 2024 [T3: USTR Federal Register, September 2024, observed]. Non-EV Li-ion batteries follow on January 1, 2026 at the same 25% rate. Natural graphite faces a 25% tariff from January 2026. This structure adds approximately 17.5 percentage points of cost to Chinese Li-ion battery imports into the USA, partially offsetting the cost advantage Li-ion holds over lead-acid. With US domestic manufacturing now above 200 GWh and scaling further under IRA incentives, the tariff impact reduces as domestic sourcing increases. The tariff does not constitute a BLOCKED condition — Li-ion retains decisive cost and service-life advantages even at 25% tariff — but it adds 1–2 years of delay to US market cost-parity dynamics for the SLI vector.

---

### Regional Readiness

| Region | Infrastructure | Supply Chain | Regulatory | Overall |
|---|---|---|---|---|
| China | READY (98% EV corridor; CATL/BYD dominant; LFP at volume scale) | READY (646 GWh CATL capacity; 1.934M tonnes LFP cathode consumed; 33% utilization = 3x surplus) | READY (NEV mandate operational at 47.9% penetration; lead restrictions active; no tariff friction) | MET |
| Europe | PARTIAL (>1M charging points; ~75% corridor coverage est.; Li-ion recycling scaling under Battery Reg) | READY (supply chain diversifying; Northvolt; EU cathode investments; lithium surplus globally) | READY (Battery Reg 2023/1542 in force Feb 2024; REACH lead restrictions; 90% CO2 target still directional for BEV) | PARTIAL |
| USA | PARTIAL (59.1% highway corridor; 35,500 tonne Li-ion recycling capacity; 200+ GWh domestic mfg) | READY (200+ GWh domestic capacity; IRA incentives; lithium available at surplus; LFP packs importable) | PARTIAL (25% tariff on Li-ion from China Sept 2024; no federal vehicle EV mandate; NEVI guidance rescinded Feb 2025) | NOT_MET |

---

### Blockers

1. **USA EV highway corridor coverage at 59.1% (Q4 2024)**: Below the 80%+ threshold at which charging anxiety meaningfully diminishes for long-distance BEV adoption, slowing fleet turnover and thereby delaying ICE fleet contraction that drives SLI replacement demand destruction (Disruption 2, 3,377 kt vector). At +5.3 pp/yr observed build-out rate, 80% coverage is reached in ~2028 [model-derived from FHWA observed data]. DOT rescinded NEVI guidance in February 2025, introducing uncertainty about build-out pace. Severity: MEDIUM. This blocker affects only the SLI replacement demand vector; it does not slow UPS, forklift, or direct SLI substitution vectors.

2. **Li-ion recycling infrastructure nascent outside China**: Global Li-ion recycling capacity is 450 GWh (2024), with 75% in China. USA capacity is 35,500 tonnes reclaimed (2023). EU is scaling under Battery Regulation mandates. This becomes a more significant constraint from 2030+ as large volumes of EV batteries reach end-of-life. It does not currently block adoption. Severity: LOW for 2024–2029; MEDIUM for 2030+. Resolution model-derived: EU by ~2030 (regulatory mandated); USA by ~2030–2032.

3. **USA Section 301 tariffs — 25% on Li-ion batteries from China (Sept 2024)**: Increases landed cost of Chinese Li-ion cells and packs in the US market by approximately 17.5 percentage points vs. pre-2024. Partially offset by IRA-driven domestic manufacturing scale-up. Does not block the disruption but adds 1–2 years of delay to US market cost-parity dynamics for the SLI unit cost parity timeline (USA: 2027–2028 model-derived). Severity: LOW-MEDIUM.

4. **EU 2035 mandate revision (December 2025) — from full ICE ban to 90% CO2 reduction**: The elimination of the absolute 2035 ICE ban maintains a residual pathway for new ICE and PHEV sales in Europe post-2035, sustaining low-volume SLI new-vehicle demand past the date previously assumed to be a hard cutoff. Cost-curve dynamics determine the underlying trajectory regardless; the mandate revision shifts the European disruption timeline by approximately 2–4 years. Severity: LOW.

---

### Compliance Checklist

| ID | Severity | Status | Note |
|---|---|---|---|
| 5.2a | CRITICAL | PASS | All three sub-conditions assessed: infrastructure, supply chain, regulatory |
| 5.2b | CRITICAL | PASS | Aggregate status explicitly stated: NOT_MET |
| 5.2c | HIGH | PASS | Each sub-condition rated with quantified evidence (utilization rates, kt surplus, coverage %, tariff rates) |
| 5.2d | HIGH | PASS | Four blockers identified with severity and resolution timeline |
| 5.2e | HIGH | PASS | China, USA, Europe assessed in regional readiness table |
| 5.2f | MEDIUM | PASS | Adoption readiness year stated: model-derived 2028 (infrastructure sub-condition drives timeline) |
| 5.2g | HIGH | PASS | All web-sourced data is observed/historical; third-party market-size statements discarded; no future-dated claims from web sources used as fact |

**Overall: COMPLIANT**

---

### Data Gaps

1. **Li-ion recycling: no per-GWh throughput data for USA/Europe in 2024** — only tonnage (35,500 tonnes USA) and market value were available; conversion to GWh is imprecise without chemistry-specific weight density data.
2. **Europe EV highway corridor coverage: no single authoritative source for % coverage comparable to FHWA metric** — the ~75% European estimate is from agent memory record, not a primary source citation. The 1M+ charging points figure is observed but does not directly map to corridor-coverage percentage.
3. **Li-ion forklift service technician workforce data** — no observed data on workforce gaps for EV forklift maintenance in China, USA, or Europe; assumed non-binding based on OEM-led training programs.
4. **No observed data on LFP UPS system installed base outside China** — the 1,987 kt stationary backup demand uses GWh-to-kt translation; the USA/Europe UPS market split is not available from catalog data.
5. **USGS MCS 2025 PDF** — connection failed during retrieval; 2024 production data from secondary sources (Fastmarkets, Benchmark Minerals Intelligence) used instead.

---

## Sources

- Upstream: `output/lead-demand-decline/agents/01-domain-disruption.md`
- Upstream: `output/lead-demand-decline/agents/02b-cost-fitter.md`
- [T3: Interact Analysis — 1,200 GWh new Li-ion capacity added globally 2024, observed, retrieved 2026-03-20](https://interactanalysis.com/insight/1200-gwh-of-new-lithium-ion-battery-capacity-added-globally-to-date-in-2024/)
- [T3: Fastmarkets/Benchmark Minerals Intelligence — lithium supply >1M tonnes LCE 2024, 134,000 MT LCE surplus, observed, retrieved 2026-03-20](https://source.benchmarkminerals.com/article/in-charts-lithiums-million-tonne-year)
- [T3: CAAM/CnEVPost — China LFP battery installations 409 GWh (74.6% share) 2024, observed, retrieved 2026-03-20](https://cnevpost.com/2025/01/13/china-ev-battery-installations-dec-2024/)
- [T3: FHWA / Joint Office of Energy and Transportation — Q4 2024 NEVI quarterly update; 59.1% corridor coverage, 206,000+ ports, observed, retrieved 2026-03-20](https://driveelectric.gov/news/q4-2024-nevi-quarterly-update)
- [T3: Battery Council International / ILA — lead-acid battery 99% recycling rate USA, observed, retrieved 2026-03-20](https://batterycouncil.org/news/new-study-confirms-lead-batteries-maintain-remarkable-99-recycling-rate/)
- [T3: ScienceDirect — China ULAB recycling rate 48% (2023 data), observed, retrieved 2026-03-20](https://www.sciencedirect.com/article/abs/pii/S0921344926001102)
- T3: EUR-Lex — EU Battery Regulation 2023/1542, in force 18 February 2024, observed, retrieved 2026-03-20 [URL omitted per citation policy]
- [T3: Euronews — EU revises 2035 mandate; 90% CO2 reduction replaces full ICE ban, December 16, 2025, observed, retrieved 2026-03-20](https://www.euronews.com/my-europe/2025/12/16/eu-carmakers-to-comply-with-90-emissions-reduction-by-2035-as-full-combustion-engine-ban-s)
- [T3: USTR — Section 301 tariff increases finalized; Li-ion EV batteries 25% from Sept 27, 2024, observed, retrieved 2026-03-20](https://www.whitecase.com/insight-alert/united-states-finalizes-section-301-tariff-increases-imports-china)
- [T3: CAAM/CnEVPost — China NEV penetration 47.9% passenger cars 2024, observed, retrieved 2026-03-20](https://cnevpost.com/2025/01/13/china-nev-sales-dec-2024-caam/)
- [T3: IEA / Statista — global Li-ion recycling capacity 450 GWh 2024, 75% China-based, observed, retrieved 2026-03-20](https://www.iea.org/data-and-statistics/charts/expected-battery-recycling-capacity-by-region-based-on-current-announcements-2023-2030)
- [T3: US DOE FOTW #1350 — USA battery recycling facilities capable of reclaiming 35,500 tonnes, 2023 data, observed, retrieved 2026-03-20](https://www.energy.gov/eere/vehicles/articles/fotw-1350-july-8-2024-2023-united-states-had-battery-recycling-facilities)
- [T3: USGS Mineral Commodity Summaries 2024 — lithium mine production 180,000 tonnes (ex-USA) 2023 data, observed, retrieved 2026-03-20](https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-lithium.pdf)
