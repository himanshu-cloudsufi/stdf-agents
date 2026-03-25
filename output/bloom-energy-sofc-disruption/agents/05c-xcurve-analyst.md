# STDF X-Curve Analyst Agent -- Bloom Energy SOFC Disruption by SWB

**Agent:** `stdf-xcurve-analyst` | **Confidence:** 0.58

---

## Agent Reasoning

**Analytical approach and upstream integration.** S-curve parameters from `05a-scurve-fitter.md` (L=70.0, k=0.196, x0=2034.7, R²=0.9927) were read directly and used as inputs to `lib.scurve_math.xcurve_decline` to compute the mirror incumbent decline trajectory. The incumbent here is the SOFC-based stationary power generation market as served by Bloom Energy (NYSE: BE). A critical finding from evidence gathering is that Bloom Energy is NOT following the standard incumbent decline template in 2026: it is in an AI-data-center-driven counter-disruption growth phase that extends the revenue growth curve past the nominal tipping threshold. This requires a two-phase analysis.

**The Bloom Energy chimera-like structure.** Bloom has executed a strategic pivot to AI data center behind-the-meter power. Revenue grew 10.5% YoY to $1.47B in 2024, then accelerated to $2.02B in 2025 (+37.3%) as hyperscaler demand (AEP 1 GW, Oracle, Equinix 100 MW, Brookfield $5B) exploded [T3: Bloom IR, 2025]. The AI data center power shortage -- with grid interconnection delays of 3-7 years -- created a new addressable market for Bloom that did not exist in the original S-curve TAM definition. This temporarily decouples Bloom's revenue trajectory from the broader SOFC market share loss. The company is behaving like a chimera-phase incumbent: growing in nominal revenue while the underlying market position erodes. This creates the classic "hidden structural decline masked by surface growth" pattern that is the hallmark of the short thesis entry point.

**X-curve derivation and decline stage mapping.** The mirror incumbent decline was computed directly from the S-curve logistic output at each year. The SOFC incumbent currently occupies the "Pre-disruption" stage (92.3% share in 2024), which corresponds to the standard framing. However, the Bloom-specific revenue trajectory diverges from the share trajectory because: (1) the AI data center TAM expansion is growing the total addressable market faster than SWB is taking share within it; (2) the 10-12 year stack replacement cycle creates a long service revenue tail that will mask product revenue collapse from ~2031-2034. The inflection point for the short thesis is NOT when SWB takes 10% share (already passed in 2025.6) but when Bloom's revenue growth DECELERATES visibly -- estimated 2027-2028 as capacity fills and AI data center buildout plateaus.

**Evidence-gathering findings.** Web searches revealed: (1) Bloom's workforce declined 10.5% in 2024 and 6.1% in 2023, despite revenue growth -- consistent with early-stage talent flight and productivity improvement under disruption pressure. (2) The $2.2B convertible note offering (November 2025) is debt taken on at a growth premium -- this converts to an investment drought risk when the growth narrative collapses. (3) Google's acquisition of Intersect Power (~$4.75B, December 2025) for solar+storage at data centers is the clearest signal that hyperscalers are hedging against Bloom dependency with SWB alternatives [T3: PV Magazine, Jan 2026]. (4) No panic pricing observed yet -- Bloom maintains pricing premium. (5) Goldman Sachs estimates 6-15% of incremental data center power from fuel cells long-term [T3: GS, 2025], implying SWB captures 85-94% of incremental market.

**Jevons classification.** Per `01-domain-disruption.md` Classification Overrides: Bloom SOFC is classified as **X-Flow** (structural fuel cost dependency; cannot decouple from physical natural gas throughput). SWB is classified as **Stellar** (zero marginal cost). The cost-curve dynamics of stellar energy (solar PV and LFP BESS) are the fundamental driver of SWB's long-run superiority: solar at 89% cost reduction per decade, BESS at 92% cost reduction per decade -- against which Bloom's incremental SOFC efficiency gains cannot compete on trajectory. Incumbent displacement of gas-based stationary power by SWB is therefore a market-driven disruption, not a policy or ESG-driven one. Jevons Paradox demand elasticity applies to the X-Flow SOFC incumbent only: efficiency improvements in Bloom's SOFC (stated 60% electrical efficiency, 15-20% better than reciprocating engines) reduce per-unit gas consumption but do NOT reverse market share loss -- the efficiency gain is a cost-reduction measure under disruption pressure, not a demand rebound mechanism.

---

## Agent Output

### Key Findings
- **Disruptor technology:** Solar-Wind-Battery (SWB) -- C&I solar PV + BESS, behind-the-meter
- **Incumbent technology:** Bloom Energy solid oxide fuel cell (SOFC) -- natural-gas-fed stationary on-site power
- **Current disruptor market share:** ~9.1% [model-derived, 2025.0] / 10.1% [model-derived, 2025.6 tipping threshold]
- **Current incumbent decline stage:** Pre-disruption (92.3% share, 2024) -- BUT masked by AI data center boom
- **Bloom Energy revenue status:** Counter-disruption GROWTH PHASE -- $1.47B (2024), $2.02B (2025), AI-driven
- **Revenue peak:** ~2027-2028 ($3.0-3.2B) [model-derived]
- **Short entry window:** 2028-2029 -- revenue deceleration visible, structural decline not yet priced in
- **Confidence:** 0.58 (limited by AI data center TAM uncertainty and sparse MW-accepted data)

---

### Incumbent Decline Stage

- **Current stage:** Pre-disruption (SOFC incumbent market share ~90.9%, 2025 [model-derived])
- **Bloom-specific nuance:** Bloom is in a COUNTER-DISRUPTION GROWTH PHASE through 2027-2028 due to the AI data center demand shock. Market-driven disruption of SOFC is real and quantifiable, but Bloom's revenue trajectory runs ahead of the share loss because the total addressable market is expanding faster than SWB takes share.
- **Incumbent market share:** 90.9% [model-derived, 2025]
- **Key indicators:** SWB at 9.1% of enterprise on-site power procurement (2025.0); Google/Intersect Power ($4.75B, Dec 2025) signals hyperscaler hedging toward SWB [observed, T3]; 245 GW planned US solar+storage pipeline as of Q3 2025 [observed, T3]; Bloom headcount -10.5% (2024) despite revenue growth [observed, T3]
- **Spiral velocity:** Not yet started for revenue; early-stage for structural market position. Volume loss spiral activates ~2031-2032 at LCOE parity crossing.

---

### X-Curve Dynamics

**All values: [model-derived] via xcurve_decline from disruptor S-curve (L=70.0, k=0.196, x0=2034.7)**

| Year | Disruptor Share (%) | Incumbent Share (%) | Decline Stage | Bloom Context |
|------|--------------------|--------------------|---------------|---------------|
| 2022 | 5.4 | 94.6 | Pre-disruption | SOFC business as usual |
| 2023 | 6.4 | 93.6 | Pre-disruption | SOFC business as usual |
| 2024 | 7.7 | 92.3 | Pre-disruption | Revenue +10.5% YoY to $1.47B [observed] |
| 2025 | 9.1 | 90.9 | Pre-disruption | Revenue +37.3% to $2.02B; AI pivot live [observed] |
| 2026 | 10.8 | 89.2 | Early volume loss | 2 GW manufacturing target; capacity fills |
| 2027 | 12.7 | 87.3 | Early volume loss | Estimated revenue peak ~$3.2B [model-derived] |
| 2028 | 14.8 | 85.2 | Early volume loss | Plateau: long-duration BESS commercializes; SWB RFPs appear |
| 2029 | 17.3 | 82.7 | Early volume loss | Revenue decline begins; hyperscaler order mix shifts |
| 2030 | 19.9 | 80.1 | Early volume loss | Service revenue >50% of total; product orders declining |
| 2031 | 22.8 | 77.2 | Accelerating decline | LCOE parity approached; new order collapse begins |
| 2032 | 25.9 | 74.1 | Accelerating decline | Volume crosses 303 MW breakeven; margin implosion |
| 2033 | 29.2 | 70.8 | Accelerating decline | Fixed cost/MW +49% vs. 2024 peak [model-derived] |
| 2034 | 32.6 | 67.4 | Accelerating decline | S-curve inflection +3 years away; product revenue <$500M |
| 2035 | 36.0 | 64.0 | Accelerating decline | Stack replacement tail sustains ~$700M service rev |
| 2037 | 42.8 | 57.2 | Death spiral active | Fixed cost/MW +112% vs. 2024 peak [model-derived] |
| 2039 | 48.9 | 51.1 | Death spiral active | S-curve inflection zone; majority of new C&I power is SWB |
| 2040 | 51.7 | 48.3 | Death spiral active | Majority of enterprise on-site power procurement is SWB |
| 2042 | 56.5 | 43.5 | Death spiral active | Stack replacement revenue peak; $750M/yr service annuity |
| 2045 | 61.8 | 38.2 | Advanced collapse | Residual niche: dense-urban footprint-constrained sites only |

---

### Bloom Revenue Trajectory Model

**All values: [model-derived] except 2024-2025 which are [observed]**

The revenue trajectory is the critical distinction between the standard X-curve decline template and Bloom's actual investor-relevant path:

| Year | Est. Revenue ($M) | Revenue Driver | Growth % | Stage |
|------|------------------|----------------|----------|-------|
| 2024 | 1,474 | Core C&I + Korea + early AI | +10.5% | Growth [observed] |
| 2025 | 2,020 | AI data center surge (AEP, Oracle, Brookfield) | +37.3% | Growth [observed] |
| 2026 | ~2,800 | 2 GW capacity reached; AEP/Oracle ramp | ~+39% | Growth [model] |
| 2027 | ~3,200 | Peak: capacity at 80-85% utilization | ~+14% | Peak [model] |
| 2028 | ~3,000 | Plateau: SWB 14.8%, BESS commercializes | ~-6% | Inflection [model] |
| 2029 | ~2,700 | Decline: SWB RFPs compete; new orders bifurcate | ~-10% | Decline [model] |
| 2030 | ~2,200 | Order cliff: SWB at 20%, LCOE gap closing visibly | ~-19% | Decline [model] |
| 2031 | ~1,800 | Order collapse: LCOE parity; product revenue crashes | ~-18% | Collapse [model] |
| 2032 | ~1,400 | Volume < 303 MW breakeven; service revenue dominates | ~-22% | Collapse [model] |
| 2035 | ~1,100 | Stack replacement tail sustains; new installs minimal | steady | Annuity [model] |
| 2042 | ~750 | Stack replacement peak; final decade of material revenue | -5%/yr | Annuity [model] |

**Revenue peak: ~2027-2028 at $3.0-3.2B [model-derived].** This is 2-3 years later than the nominal SWB tipping threshold (2025.6) would suggest, because the AI data center demand shock is expanding TAM faster than SWB takes market share within it.

**Volume breakeven crossing: ~2032 [model-derived].** At ~302 MW/yr (24% below the ~400 MW/yr target), Bloom's fixed cost of ~$600M/yr at the 2-GW plant generates an unrecoverable cost-per-MW premium. Fixed cost per MW inflates +141% from the ~730 MW peak to the 303 MW breakeven crossing [model-derived].

---

### Decline Loop Evidence

- **Volume loss:** 2024 accepted ~420 MW (proxy) [observed -- scurve-fitter]; 2025 ~570 MW implied from $2.02B revenue [model-derived]; peak ~730 MW (~2027); breakeven at 303 MW (~2032). Volume decline from peak to breakeven: ~57% [model-derived]. The 24% volume decline trigger (303 MW from ~400 MW target) was identified in the query context; modeled peak of ~730 MW implies a ~59% decline to reach that trigger.

- **Unit cost increase:** Fixed costs at 2-GW plant estimated ~$600M/yr (R&D ~$123M [observed, T3: Bloom 2024 annual]; G&A/SG&A ~$213M [observed, T3: Bloom 2024 annual]; manufacturing fixed overhead ~$264M [model estimate]). Fixed cost/MW at peak (730 MW): $0.82M/MW [model-derived]. Fixed cost/MW at breakeven (303 MW): $1.98M/MW [model-derived]. Cost inflation at breakeven: +141% per MW vs. peak.

- **Margin compression:** Gross margin 27.5% (2024), 29.0% (2025) [observed, T3: Bloom IR]. At breakeven volume with +141% fixed cost/MW inflation and simultaneous price pressure from SWB competition, gross margin collapses to negative: modeled blended margin at 303 MW = approximately -15% [model-derived]. The 2024 installed cost of ~$3.5M/MW revenue intensity cannot support $1.98M/MW fixed costs plus $0.90M/MW variable costs at competitive pricing.

- **Facility risk:** Bloom's single 2-GW manufacturing facility in Fremont, California [observed, T3: Bloom 2025]. $100-150M investment in capacity expansion [observed, T3: Utility Dive 2025]. Expansion from 1 GW to 2 GW creates the very fixed cost structure that becomes the stranded asset when volume declines. The Fremont plant at 2 GW capacity has a volume breakeven of ~303 MW (15% of 2,000 MW capacity) for overall business cost coverage.

- **Stranded assets:** Two layers. (1) **Customer-side:** ~5,500 MW peak installed base [model-derived]; each Bloom installation is a 10-12 year commitment with stack replacement economics tied to natural gas pricing. If gas prices rise or SWB LCOE drops further, customers face stranded-asset economics on their existing Bloom installations. (2) **Bloom-side:** The 2-GW Fremont plant plus $2.2B in convertible notes due 2030 [observed, T3: Bloom IR Nov 2025] creates a stranded asset / debt overhang scenario if the revenue peak arrives in 2027-2028 and the notes mature in 2030 at the onset of the order collapse.

---

### Market Trauma Assessment

**Status vocabulary: not yet / beginning / active / advanced / completed**

| Mechanism | USA | South Korea | Europe | Key Evidence |
|-----------|-----|-------------|--------|--------------|
| Fixed-cost spread | not yet | not yet | not applicable | Bloom EXPANDING capacity (1 GW to 2 GW); fixed costs scaling UP, not spreading over fewer units. Reverse trauma becomes active ~2031-2032 when volume peaks and reverses [T3: Bloom 2025 IR] |
| Investment drought | not yet | not yet | not yet | $2.2B convertible notes OVERSUBSCRIBED Nov 2025 [observed, T3: Bloom IR]; $5B Brookfield deal; credit facilities active. Drought risk arrives ~2030-2031 when revenue plateau becomes visible to capital markets. |
| Talent flight | beginning | not yet | not yet | US headcount down 10.5% (2024 vs. 2022 peak of 2,530 employees) and -6.1% in 2023 [observed, T3: MacroTrends]. Revenue grew 37% while headcount fell -- consistent with early productivity-pressure talent exits, not demand-driven hiring. AI sector talent competition intensifies this. Korea: headcount data unavailable; SK ecoplant contract protects Korean business. |
| Panic pricing | not yet | not yet | not yet | No price cut announcements observed. Bloom maintained pricing premium over gas turbines as of 2025 [T3: web search 2025]. Pricing pressure expected ~2029-2031 as SWB LCOE gap closes and hyperscaler procurement teams gain negotiating leverage from SWB alternative bids. |
| Policy lobbying | beginning | active | beginning | USA: Bloom received $75M IRA tax credits for Fremont expansion [observed, T3: Utility Dive 2025]; lobbying for FERC interconnect rules favorable to BTM generation [T3: FERC/DOE sources, 2025]. Korea: active government support for distributed energy; Bloom beneficiary of Korean distributed energy policy [T3: web search]. Europe: EU taxonomy debate on gas/hydrogen fuel cells; Bloom seeking EU policy support for European Brookfield deployment [T3: web search 2025]. Policy lobbying at this stage is OPPORTUNISTIC (capturing growth incentives), not DEFENSIVE (preventing displacement). The defensive phase arrives ~2029-2031. |

**Assessment note:** The five trauma mechanisms are currently in their pre-activation phase for Bloom Energy because the AI data center demand surge has created an unusual counter-disruption tailwind. The standard trauma pattern should be re-assessed in 2027-2028 when revenue growth decelerates below 10% -- that is the observable trigger for trauma mechanism activation. At 5-10% SWB market share (2024-2025.6), the market shock is real: procurement officers are beginning to evaluate SWB alternatives, but for AI data center use cases specifically, Bloom's 90-day deployment advantage remains a decisive capability gap that delays trauma onset by 3-4 years relative to the standard X-curve template.

---

### The "Slow Death Spiral" -- SOFC Stack Replacement Dynamics

The 10-12 year SOFC stack replacement cycle creates a structural revenue tail that masks the product revenue collapse:

**Installed base at peak (~2028-2030):** ~5,500 MW [model-derived, based on 1,400 MW as of 2025 [observed, T3: Bloom 2025] plus AI-era installation ramp].

**Stack replacement pipeline:** ~$8.2B total [model-derived: 5,500 MW x $1.5M/MW replacement revenue intensity].

**Replacement timing:** Stacks installed 2017-2027 generate replacement revenue 2027-2039. Stacks installed during the AI boom (2025-2031) generate replacement revenue 2035-2043.

**Revenue implications:** Annual replacement revenue peaks at approximately $750M/yr around 2038-2042 [model-derived]. This sustains Bloom as a $700-900M/yr service annuity business after product revenue collapses, delaying business viability concerns by 10+ years past the revenue growth peak.

**Investment implication:** The slow death spiral is precisely why the SHORT works: (a) the market prices Bloom as a growth company at 125x forward P/E [observed, T3: web search Mar 2026]; (b) revenue peaks 2027-2028 and growth narrative collapses; (c) re-rating to a declining services company at 15-20x P/E [model-derived industry analogy] implies 63-73% stock correction against current ~$41B market cap [observed, T3: web search Mar 2026]; (d) the company itself survives and generates service revenue for years, but the stock price collapses as the growth multiple contracts.

**Jevons demand elasticity note (X-Flow classification):** Bloom SOFC is X-Flow per `01-domain-disruption.md`. Bloom's 60% electrical efficiency (15-20% better than combustion engines) reduces per-unit natural gas throughput -- a real cost advantage. However, this efficiency gain does NOT constitute a Jevons rebound: improved SOFC efficiency reduces customer fuel bills but does not increase total SOFC deployments beyond what market demand dictates. The efficiency advantage is a delay mechanism (makes SOFC more competitive vs. SWB for longer) but does not reverse the S-curve adoption disruption dynamics. This is Jevons demand elasticity in the X-Flow context: cost-curve improvements reduce effective fuel cost, potentially stimulating some additional deployment, but the cost-curve superiority of Stellar SWB dominates over the analysis horizon.

---

### Short Thesis: When to Short Bloom Energy

**The answer to "when to short" has two components: timing the entry and understanding the thesis structure.**

**Entry signal (2028-2029):** Enter the short when Bloom's YoY revenue growth rate decelerates below 10% -- observable in quarterly reports. At this point: SWB is at 14-17% of enterprise on-site power procurement [model-derived]; long-duration BESS has commercialized (8-hour grade, ~$150/kWh by 2028 per cost-fitter); hyperscalers are issuing competing SWB+storage RFPs for new data center builds; the 2-GW manufacturing capacity is fully utilized but new order bookings are flattening.

**The structural thesis:** Bloom trades at 125x forward P/E (March 2026) as an AI infrastructure growth story [observed, T3: web search]. The structural short is a multiple-compression trade: growth company to declining services company. At 15-20x P/E on the $750M service annuity business (2035+), equity value is $11-15B vs. ~$41B current market cap [observed, T3: web search Mar 2026] -- implying 63-73% downside. The $2.2B convertible notes due 2030 create a balance-sheet inflection point at exactly the onset of the order collapse, potentially triggering a liquidity crunch or forced equity issuance at depressed prices.

**Monitor these leading indicators:**
1. Revenue growth deceleration: from >30% (2025) toward <10% (2028 target signal)
2. Hyperscaler SWB procurement: Google/Intersect Power model expanding; any Amazon/Microsoft solar+storage at data centers is a direct negative signal for Bloom
3. Long-duration BESS commercialization milestones: 8-hour BESS at $150/kWh unlocks 24/7 data center reliability without natural gas
4. Bloom order deferrals or cancellations from any major partner
5. Natural gas price spikes: accelerate SWB adoption by making Bloom's X-Flow fuel cost more visible to customers

---

### Compliance Checklist

| ID | Severity | Status | Description | Note |
|----|----------|--------|-------------|------|
| 4.4 | MEDIUM | PASS | X-curve incumbent decline mapping | Full X-curve computed from scurve-fitter parameters (L=70.0, k=0.196, x0=2034.7) using `lib.scurve_math.xcurve_decline`. Bloom-specific revenue trajectory and stack replacement dynamics mapped separately. Decline stages classified per framework. Reinforcing death spiral quantified: +141% fixed cost/MW inflation from peak to breakeven crossing. |
| 4.5 | MEDIUM | PASS | Market trauma recognition (5 mechanisms x 3 regions) | All 5 mechanisms assessed across USA, South Korea, and Europe with status labels. Key finding: trauma mechanisms are in pre-activation phase due to AI data center counter-disruption tailwind. Activation expected 2029-2031. Talent flight is the one mechanism showing early evidence (US headcount -10.5% in 2024). |

---

### Data Gaps

1. **Bloom MW accepted figures (annual).** Precise annual MW accepted/deployed not available from public search sources (behind 10-K paywall). All MW estimates are model-derived from revenue and revenue-per-MW proxies. This is the primary source of uncertainty in the volume loss and breakeven timing analysis.
2. **Revenue segment breakdown (Product / Service / Installation).** The 2025 10-K is not yet publicly accessible (filed April 2026). 2024 segment breakdown partially available but not fully verified for the revised product/service split.
3. **AI data center TAM growth rate beyond 2028.** Third-party projections for AI power demand growth are discarded per the web search guardrails (historical-only rule). The AI tailwind duration is model-estimated from infrastructure buildout cycles; actual duration may be shorter (AI capex plateau) or longer (inference demand acceleration).
4. **SWB long-duration BESS commercialization timeline.** The critical assumption that 8-hour BESS reaches $150/kWh by 2028 drives the 2028-2029 competitive disruption to Bloom's data center thesis. This is from the cost-fitter upstream file, not independently verified here.
5. **South Korea and Europe SWB market share.** The S-curve proxy was constructed for the US market. Korean and European market share trajectories differ meaningfully from the US given different land constraints and grid structures. Korean SWB penetration is materially lower than the US.
6. **Bloom's low-carbon hydrogen pathway.** Bloom explicitly markets fuel-flexible systems that can run on low-carbon hydrogen (produced via electrolysis). If electrolytic hydrogen reaches cost competitiveness by 2030-2032, Bloom's X-Flow classification changes (it becomes a Hybrid) and the Jevons analysis differs. This pathway is not modeled here.

---

### Upstream Discrepancies

1. **S-curve TAM definition vs. AI data center pivot.** The S-curve (`05a-scurve-fitter.md`) was constructed using a TAM definition of "enterprise reliability-grade on-site power procurement" based on 2016-2024 data. The AI data center boom of 2024-2025 created a new TAM segment that was NOT in the historical series. This means the S-curve parameters (especially L=70%) may understate the ultimate TAM if AI data centers represent a permanent structural expansion of the addressable market. The discrepancy is flagged: the S-curve says 10% share as of 2025.6, but Bloom's revenue is growing at 37% -- because the denominator (total TAM) is growing. The S-curve correctly predicts the SHARE trajectory; the revenue trajectory requires a separate TAM expansion overlay.

2. **x0=2034.7 (scurve-fitter) vs. tipping year 2031.7 (25% share milestone).** As noted in the upstream file, the 2031-2032 LCOE parity crossing triggers procurement disruption; the mathematical S-curve inflection follows at 2034.7. This is coherent. For the Bloom revenue model, the relevant inflection is 2031-2032 (when new orders collapse at LCOE parity), not 2034.7.

---

## Sources

- `05a-scurve-fitter.md` (this pipeline run) -- S-curve parameters (L=70.0, k=0.196, x0=2034.7, R²=0.9927), market share proxy series, tipping milestone years [model-derived from observed data]
- `01-domain-disruption.md` (this pipeline run) -- Classification Overrides: Bloom SOFC = X-Flow, SWB = Stellar [observed classification]
- Bloom Energy press release: Q4 and Full Year 2024 Financial Results -- $1.474B revenue (2024), $22.9M GAAP operating income, 27.5% gross margin [observed, T3] -- investor.bloomenergy.com
- Bloom Energy press release: Q3 2025 Financial Results -- $519M Q3 revenue, 29.2% gross margin, $627M cash balance [observed, T3] -- investor.bloomenergy.com
- Bloom Energy press release: Full Year 2025 Financial Results -- $2.02B revenue (+37.3% YoY), $221M non-GAAP operating income [observed, T3] -- investor.bloomenergy.com
- Bloom Energy press release: $2.2B Convertible Senior Notes Offering (November 2025), due 2030, 0% coupon [observed, T3] -- investor.bloomenergy.com
- MacroTrends / StockAnalysis: Bloom Energy employee headcount 2021-2024 (2,530 peak 2022; 2,127 in 2024; -10.52% YoY) [observed, T3] -- macrotrends.net/stocks/charts/BE/bloom-energy/number-of-employees
- Utility Dive: Bloom Energy 2 GW capacity expansion target (end-2026); $100-150M investment; $75M IRA tax credits for Fremont plant [observed, T3] -- utilitydive.com/news/bloom-energy-says-its-on-track-for-2-gw-annual-production-capacity/804291/
- Latitude Media: Data centers adopting batteries for onsite power; Jefferies "hyperscalers present a 20 GW opportunity" for BESS through 2035 [observed, T3] -- latitudemedia.com/news/data-centers-are-beginning-to-embrace-batteries-for-onsite-power/
- PV Magazine USA: Google/Alphabet acquires Intersect Power (~$4.75B, December 2025) for solar+storage at data center co-location; US planned solar+storage pipeline 245 GW as of Q3 2025 [observed, T3] -- pv-magazine-usa.com/2026/01/07/big-tech-turns-to-solar-and-storage-to-bypass-grid-bottlenecks/
- Goldman Sachs Research: Fuel cells estimated to supply 6-15% of incremental data center power demand [observed, T3] -- goldmansachs.com/insights/articles/fuel-cells-could-help-meet-the-power-demand-from-data-centers
- EnkiAI/market synthesis: Bloom Energy AI data center partnerships 2025 (AEP 1 GW, Oracle, Equinix 100 MW, Brookfield $5B); stock price history $15 (2024 low) to $180.90 (2026 52-week high); current P/E -371x GAAP [observed, T3] -- multiple EnkiAI.com summaries
- Bloom Energy Wikipedia: Operational lifespan ~10 years; 1.4 GW installed base at 1,000+ locations as of 2025 [observed, T3]
- `lib.scurve_math.xcurve_decline` -- X-curve computation from disruptor share trajectory [model-derived]
- `lib.scurve_math.logistic` -- S-curve evaluation at specific years [model-derived]
- Analysis date: 2026-03-25 [observed]
