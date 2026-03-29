# Consolidated Report: Sector & Commodity Breakdown

**Source:** 4 Stellar Capital team meetings (2026-03-06, 2026-03-11, 2026-03-20, 2026-03-26)
**Compiled:** 2026-03-27

---

## 1. LEAD

### Overview
Lead is Tony's chosen canonical template for recursive disruption modeling. It gets the most detailed treatment of any commodity across the 4 meetings because its dynamics (byproduct supply, recycling, EV displacement of lead-acid batteries) create a self-reinforcing loop that templates other disruptions.

### Discussion by Meeting

**Mar 6:** Mentioned as part of the commodity-level domain models covered by the data factory. Not discussed in depth.

**Mar 20 (Major focus):**
- Jitin presented an updated lead disruption model. Split 12V battery costs into two segments: SLA (sealed lead-acid) batteries and EV auxiliary batteries, each with separate cost curves.
- Tipping points moved forward dramatically: from 2030-2032 to **2026 (China)** and **~2029 (other countries)**.
- Added previously missing demand data (stationary and motive industrial batteries).
- Built proper supply-side modeling: primary supply + secondary supply from vehicle/battery retirements.
- Identified ~60 kilotons as residual with caveat for data gaps.
- Tony demanded: **no cost floors**. Removed raw-material-cost-based floors from the model.
- 10% oversupply timing is a key model output.
- Tony: "If we can get the lead disruption right, it's a good template to get other disruptions right. That's why I'm emphasizing lead -- because of the recursive nature of that disruption."

**Mar 26 (Major focus):**
- Two supply-demand models built:
  - **(A) Annual surplus only** -- shows surplus arriving in 2029.
  - **(B) Cumulative stockpile with inventory carryover** -- shows surplus in **2026 (this year)**.
- Tony confirmed: **use the cumulative stockpile view** (Table B).
- Supply dynamics are unique: lead is a byproduct of zinc mining, so primary supply cannot be shut off when lead demand drops. Recycling supplies ~99% of retired lead batteries.
- Tony explicitly said: **do NOT model recycling decline**. The point is to see when the surplus overwhelms the market.
- Tony: "I want to understand when it's going to fall off a cliff. That's what I really want to understand. Because that's when the price is gonna just go negative."
- Tony: "Supply will increase as demand drops, and that's what makes this trade work."
- The surplus progression: 10% oversupply becomes 20%, then 80%, then 90%. "At some point folks are gonna be like, okay, take it at any cost."

### Key Data Points & Thresholds
- China tipping point: 2026
- Other countries tipping point: ~2029
- Cumulative surplus begins: 2026 (Table B)
- Annual surplus begins: 2029 (Table A)
- ~60 kilotons residual with data gap caveat
- 99% of retired lead batteries are recycled
- Price expectation: "go negative" when oversupply becomes overwhelming

### Recursive Dynamics
Falling lithium-ion battery costs --> EV adoption --> displacement of lead-acid batteries --> lead surplus --> lead cannot be cut (byproduct + recycling) --> surplus grows --> price collapse --> further acceleration of switch to lithium-ion.

### Action Items
- Remove cost floors (done Mar 20)
- Use cumulative stockpile view, not annual-only
- Model should start from 2026, not retroactively
- Auto-refresh data for lead model expected by next week (Mar 26)

---

## 2. COPPER

### Overview
Copper is framed as the **opposite dynamic to lead** -- a bottleneck commodity where demand scales faster than supply.

### Discussion by Meeting

**Mar 6:** Mentioned as part of commodity coverage in the data factory. Not discussed in detail.

**Mar 26 (First substantive discussion):**
- Tony: "In the case of copper, the supply will not scale as quickly as the demand will."
- Demand driven by electrification (SWB, EVs, grid infrastructure).
- Supply constrained by mining timelines, permitting, geological limitations.
- Tony: "If we do the work every day on how demand for copper is increasing... but the supply is not scaling as quickly, then we can identify when bottlenecks may emerge before they emerge."

### Key Insight
Copper is a bottleneck commodity -- the disruption opportunity is in identifying when supply/demand imbalance becomes acute, not in tracking price collapse (as with lead).

### Action Items
- Track daily supply/demand dynamics to identify bottleneck emergence before it becomes visible to the market.

---

## 3. LITHIUM / BATTERIES

### Overview
Lithium-ion batteries are central to the disruption thesis -- they are the disruptor in the lead trade, a key component of EV/TaaS disruption, and a beneficiary of cost curve dynamics.

### Discussion by Meeting

**Mar 6:**
- Referenced as an example of "market trauma" -- cheaper than incumbent but supply constrained. Tony: "That's happening in solar and in batteries."
- Regional cost approach already applied to solar and batteries.

**Mar 11:**
- Tony references real-time cost data from direct company conversations: "we know what the cost of lithium ion is today because we spoke with the company today."
- Field intelligence from analysts (Peter, Guido in China) is a key data source.

**Mar 20:**
- Battery cost curves are the disrupting force in the lead model. Split into SLA and EV auxiliary segments.
- Tony: no cost floors on battery cost projections. Let the cost curve run.
- China tipping point for lithium-ion SLA batteries displacing lead-acid: 2026.

**Mar 26:**
- Bug fix: linear projection was driving lithium-ion SLA battery costs to $0. Fixed -- USA 2040 now shows $12 instead of $0.
- Cost floors still removed per Tony's directive (no artificial floors), but the projection methodology was corrected.
- Part of the recursive loop in the lead disruption model.

### Key Data Points
- China tipping point (lithium-ion cheaper than lead-acid SLA): 2026
- Other countries: ~2029
- USA 2040 projected cost (lithium-ion SLA): $12 (after bug fix)
- Cost data sourced partly from direct company conversations

### Action Items
- Continue tracking battery cost curves without imposing floors
- Incorporate field intelligence from China trips (Peter, Guido)

---

## 4. LNG / NATURAL GAS

### Overview
LNG is an active portfolio position for Stellar Capital. The Iran conflict caused significant price disruption. Tony uses LNG as an example of both analytical failure (system didn't use SIBA framework) and the potential of proactive monitoring.

### Discussion by Meeting

**Mar 6:**
- Iran conflict is a major factor. Robert: "What's relevant today is the Iran war."
- Robert had "significant issues trading this labor disruption into this Iraq/Iran war."

**Mar 11:**
- Iran conflict triggered LNG/CNG price spikes, echoing Ukraine invasion pattern (prices went from ~20 to 200, now spiked to 50-60).
- Tony's LNG analysis may be "irrelevant after the Iran war" but SIBA framework should still apply.
- Tony suggests crises may accelerate adoption of renewable energy.

**Mar 20:**
- Tony frustrated that an LNG query "went off and did all kinds of things without doing any cost curves or whatever... to go off and do an analysis of LNG without doing cost curves of solar wind and battery and so on, doesn't add anything."
- Trump social media / TTF mapping: Tony asked ChatGPT to map Trump's social media postings about Iran with the price of natural gas in Europe (TTF). Correlation was striking.
- Oil and gas price correlations broke simultaneously around beginning of the year, before the war started.

**Mar 26:**
- Tony: "For the LNG positions... we want to track oil prices every day. We want to track natural gas prices in Europe and natural gas prices in the US."
- "If we had tracked just those three things, we would have detected that oil prices had been going up since January 1st to end of Feb, even before the war started."
- This is the canonical example for the portfolio monitoring module.

### Key Data Points
- LNG price spike to 50-60 (from ~20 base, echoing Ukraine pattern that hit 200)
- Oil/gas price correlation broke at beginning of 2026, before Iran war
- Trump social media postings correlated with TTF price movements

### Action Items
- Track oil prices, EU natural gas, US natural gas daily for LNG positions
- Apply SIBA framework (solar, wind, battery cost curves as disruptors) to any LNG analysis
- Implement proactive pattern detection for early warning

---

## 5. OIL

### Overview
Oil is tracked as part of the macro fund's portfolio and as a reference point for energy disruption dynamics.

### Discussion by Meeting

**Mar 6:**
- Oil disruption agent is in development (blue/in-dev status in agent network).
- Oil disruption analysis would use the compliance checklist -- demand drivers identified, incumbent vs. disruptor cost curves for each driver.

**Mar 11:**
- Referenced as a topic they are "paying attention to."

**Mar 20:**
- Oil/gas price correlation broke at beginning of year.
- Tony wants this flagged as a correlation break signal.

**Mar 26:**
- Oil prices tracked daily as part of LNG position monitoring.
- "Oil prices had been going up since January 1st to end of Feb, even before the war started."

### Action Items
- Oil disruption agent to be completed
- Track oil prices as part of portfolio monitoring
- Monitor oil/gas price correlation for break signals

---

## 6. SOLAR PV & WIND

### Overview
Solar PV and wind are the disruptive technologies that undermine fossil fuel incumbents. Tony frames them as exponentially scaling distributed technologies versus incrementally scaling centralized infrastructure.

### Discussion by Meeting

**Mar 6:**
- Referenced as examples of "market trauma" -- cheaper than incumbent but supply constrained.
- Regional cost approach already applied.

**Mar 11:**
- Tony suggests Iran energy crisis "might accelerate adoption of stellar energy" (solar/renewable energy investments).

**Mar 20:**
- Solar, wind, and battery cost curves are the disrupting technologies that MUST be analyzed in any LNG/fossil fuel query. Tony: "To go off and do an analysis of LNG without doing cost curves of solar wind and battery... doesn't add anything."

**Mar 26:**
- Tony: "Solar PV distributed and batteries installed can scale at a way faster pace than the existing grid. The existing grid is a kludge, it's a disaster, it can only increase incrementally."
- **Pakistan example:** "In Pakistan it went from essentially zero to 18 gigawatts of solar in a 30 gigawatt grid. The stock exchange tripled."
- Track importation and installation data of solar PV and batteries by country as leading indicators.
- Rupture points at 5-10% market share when new is cheaper than old.

### Key Data Points
- Pakistan: zero to 18 GW solar in a 30 GW grid; stock exchange tripled
- Rupture points at 5-10% market penetration
- Distributed scaling (exponential) vs. grid scaling (incremental)

### Action Items
- Track solar PV and battery importation/installation data by country
- Include solar/wind/battery cost curves in every fossil fuel analysis
- Monitor for rupture points approaching in new markets

---

## 7. EVs / TRANSPORT

### Overview
EVs and autonomous vehicles are a major part of the disruption thesis, connecting battery cost curves, lead displacement, and the Transport as a Service (TaaS) concept.

### Discussion by Meeting

**Mar 6:**
- Data factory heavily focused on autonomous vehicle and automobile data. AV dashboards created.
- Tesla FSD and Waymo data refreshed daily.
- Tony: "ICE vehicles are done... it's just it's over."

**Mar 11:**
- AV data pipeline completed and refreshing daily.
- Automobile data pipeline completed and refreshing daily.
- EVs referenced as a topic they are "paying attention to."

**Mar 20:**
- Ford, Porsche, Honda doing $10 billion+ write-offs -- signals of disruption. Tony wants these flagged as unprompted insights.
- EV auxiliary batteries modeled separately from SLA batteries in the lead model.

**Mar 26:**
- **TaaS (Transport as a Service)** is Tony's canonical example of capacity factor disruption: "We use cars 5% of the time. We park it 95% of the time. The reason that transport as a service is gonna be so disruptive is that it's gonna take that 5% capacity factor to 50 or 80%."
- EVs and autonomous vehicles implicit in the TaaS framing.

### Key Data Points
- Tesla FSD and Waymo data refreshed daily
- Ford, Porsche, Honda: $10B+ write-offs
- Cars used 5% of the time; TaaS targets 50-80% capacity factor
- ICE vehicles declared "done" by Tony

### Key Concepts
- **Capacity Factor Disruption:** The disruption isn't just EV vs. ICE (product substitution) -- it's owned-vehicle vs. TaaS (business model disruption). Increasing utilization from 5% to 50-80% fundamentally changes the economics.
- **Company Write-Offs as Signal:** Massive write-offs by legacy automakers are leading indicators of disruption reaching critical mass.

### Action Items
- Continue daily AV/automobile data refresh
- Flag large corporate write-offs as proactive disruption signals
- Model TaaS capacity factor impact

---

## 8. AI / EMPLOYMENT

### Overview
The AI/employment (AL) disruption model is the single most discussed analytical topic across all 4 meetings. It is the core investment thesis for the fund.

### Discussion by Meeting

**Mar 6 (Foundation):**
- Bottom-up model: 341 US occupations from BLS, 12,000 tasks (O*NET), 90,000 sub-tasks.
- For each sub-task: token estimate, cognitive classification, time estimate.
- Tipping point: AI cost < 50% of human cost. S-curve adoption after tipping point.
- Parameters: capability doubling every 7 months (METI blog source), cost decline 70%/year, adoption time 10-80% = 4 years, adoption ceiling 80%, replacement vs. productivity 50/50.
- 12 historical cost curves for AI.
- Model predicted ~18-20% unemployment but had **zero fit** to recent actual data (Robert's discovery).
- Robert's 9 hypotheses for model failure (economic upswing, wrong thesis, non-linear thresholds, GPU supply lag, regulatory barriers, install time, startup growth time, labor regulations, capacity sufficient only for augmentation).
- Current limitations: uniform parameters across all subtasks, some LLM-generated data, only models replacement (not new job creation).
- Tony: focus on accessible price, not lowest price. Use regional costs, not PPP.
- Tony: "You guys are all in the software business. Do you agree that you're all going out of business inside of four years? No, no, of course not."

**Mar 11 (Clustering & Calibration):**
- Tony: unemployment > GDP growth. Priority: US > UK > China > EU.
- Youth unemployment and college graduate unemployment as specific targets.
- Two clustering approaches explored: rule-based (E0/E1/E2 from Anthropic economic index) and unsupervised (K-means, hierarchical).
- Parameters per cluster: time to 80% adoption, adoption lag, replacement ratio, ceiling.
- Calibration against youth unemployment as target signal.
- Back-testing against 3 years since ChatGPT launch.
- Tony: "is 2028 gonna be nine to sixteen percent or nine to eleven... if we can get it to that degree of more precision that would be amazing."
- US and UK both experiencing rising youth unemployment; UK described as "worse."
- Signal vs. noise: Block laying off 50% of workforce, RI Advisory eliminating 800-900 advisors -- Tony treats these as noise, insists on statistical data.

**Mar 20 (ML Clustering & UK Model):**
- ML-based clustering into 4 clusters: (1) manual tasks, (2) admin and tech tasks, (3) cognitive high-exposure tasks, (4) cognitive tasks already penetrated by AI.
- Different adoption parameters and S-curves per cluster.
- Aggregated back to task level (from 90,000 subtasks) for better alignment with real unemployment data.
- Back-testing against historical unemployment (overall, youth, by education level).
- UK model being finalized (US model is the detailed one). Full UK disruption framework expected by next Wednesday.
- METR data (AI capability benchmarks) available but not updated fast enough in the system.

**Mar 26 (K-Medoids & Live Reports):**
- 12 feature vectors per task from ONET job-task pairs.
- K-Medoids clustering into 4 clusters with labeled adoption parameters (ceiling, time to 80% adoption, base floor adoption %).
- Full pipeline: capability parity check > cost parity check > S-curve adoption > hours freed > risk vs. productivity split > ceiling cap.
- Aggregation: subtask > task > job > job group > economy.
- Back-tested against 5 months actual unemployment data.
- Model currently **under-predicts** unemployment -- needs parameter calibration.
- US and UK reports expected live in product by Mar 27.
- Can tweak cluster parameters in-product and regenerate unemployment numbers.
- Capacity factor concept proposed but not yet implemented -- contingent on predictive value.

### Key Data Points & Thresholds
- 341 BLS occupations, 12,000 tasks, 90,000 sub-tasks
- AI capability doubling: every 7 months
- AI cost decline: 70%/year
- Tipping point threshold: AI cost < 50% of human cost
- Model prediction: ~18-20% unemployment (initial, zero fit to data)
- 4 task clusters via K-Medoids (final methodology)
- Current status: under-predicts actual unemployment (needs calibration)
- Priority geographies: US > UK > China > EU

### Evolution
Uniform model (Mar 6) --> clustering proposed (Mar 11) --> ML clustering implemented, task-level aggregation (Mar 20) --> K-Medoids with 12 features, back-tested, live reports (Mar 26)

### Action Items
- Calibrate parameters to improve fit (currently under-predicts)
- Back-test job-specific unemployment (not just aggregate)
- US and UK reports live Mar 27
- Evaluate whether capacity factor improves predictions
- Continue tracking youth unemployment and college graduate unemployment

---

## 9. SEMICONDUCTORS

### Overview
Semiconductors are discussed primarily through the lens of different scaling properties between logic chips and memory chips.

### Discussion by Meeting

**Mar 20:**
- Tony: Logic chips (Nvidia, AMD) vs. memory chips (SK Hynix, Micron) have different scaling properties. Something changed over the last year that made memory chip stocks outperform. "Knowing that a year ago would have kind of been great."

**Mar 26:**
- Tony: "We all know by now that memory does not scale the same way as logic chips. If we had identified this a year ago, we could have put money into Heinex [Hynix] and Micron and made a bundle of money."
- This is the canonical example of a "correlation break" investment opportunity.

### Key Insight
Different semiconductor subsectors have fundamentally different scaling properties. When these diverge, it creates a tradeable opportunity. The system should have been tracking this and flagging it proactively.

### Companies Mentioned
- **Logic:** Nvidia, AMD
- **Memory:** SK Hynix, Micron

### Action Items
- Track scaling properties of different semiconductor subsectors
- Build correlation monitoring between logic and memory chip performance
- Flag when scaling property correlations break

---

## 10. AI CAPABILITY / INFRASTRUCTURE

### Overview
AI infrastructure (data centers, GPUs, token pricing) is both a driver of the AL disruption model and a potential bottleneck.

### Discussion by Meeting

**Mar 6:**
- Token pricing data is problematic: inconsistent data ("8.5 cents per thousand" vs. "a million and a half bucks per million").
- Tony: care about accessible price, not lowest price.
- Supply-side constraint: "We're assuming straight S curves without checking the potential supply of those tasks from existing data centers."
- GPU supply/infrastructure lag identified by Robert as one of 9 possible reasons the model doesn't fit.
- 12 historical cost curves for AI in the model.

**Mar 11:**
- Anthropic Economic Index used for task exposure categories (E0/E1/E2) and conversation penetration percentages.

**Mar 20:**
- METR data (AI capability benchmarks) available but not updated fast enough.
- Tony: "The METR data is out there, but it hasn't been updated... the software started the analysis Feb of 2025, even though we have data until Feb 2026."

**Mar 26:**
- AI capability data fed into the AL model pipeline (capability parity check).
- Anthropic paper features incorporated as new data source.

### Key Data Points
- AI capability doubling every 7 months (METI blog)
- 12 historical cost curves for AI
- Input vs. output token cost distinction matters
- Accessible price > lowest price

---

## 11. OTHER SECTORS

### DNA Printing
- **Meetings:** Mar 6
- **Context:** Tony mentions as an example of a new cost curve the compliance framework should be able to analyze. "When we have a new cost curve, say DNA printing, essentially, it would know how to do an analysis even though it hasn't done it before."
- **Status:** Not yet analyzed; used as a test case for framework generalizability.

### GLP-1 (Weight Loss Drugs)
- **Meetings:** Mar 6
- **Context:** Mentioned alongside DNA printing as an example of a new cost curve. Vasul: "Any new cost curve comes, GLP-1 out there."
- **Status:** Not yet analyzed; used as a test case for framework generalizability.

### UK Macro
- **Meetings:** Mar 11, Mar 20
- **Context:**
  - Mar 11: UK experiencing rising youth unemployment, described as "worse" than the US. UK separated from EU in analysis priority because they have different central banks.
  - Mar 20: Tony queried "when will UK unemployment make a material difference driving disinflation" -- wanted SIBA framework answer, not Phillips curve. UK AL disruption model being finalized.
- **Key threshold:** When does AI-driven unemployment become large enough to drive disinflationary pressure in the UK?
- **Action items:** UK AL model expected by next Wednesday (from Mar 20); US and UK reports live by Mar 27 (from Mar 26).

### China
- **Meetings:** Mar 11, Mar 20
- **Context:**
  - Mar 11: Peter (analyst) currently in China gathering intelligence; Guido going next week. Priority #3 geography for unemployment analysis (US > UK > China > EU).
  - Mar 20: "China is definitely one of the top disruptors in pretty much everything, so getting Chinese data is kind of important." Field teams (Peter, Guido) collecting on-the-ground data. PowerPoints from China trips to be ingested into the system.
  - Mar 20: Already have Chinese data for unemployment and battery costs but gaps exist.
  - Mar 20: Lead tipping point for China specifically at 2026.
- **Action items:** Ingest China field research data. Fill data gaps for Chinese unemployment and battery costs.

### SolarEdge
- **Meetings:** Mar 20
- **Context:** Richard mentioned "what he found in Solar Edge" as a topic but it was not discussed in detail in the transcription.
- **Status:** Unknown -- flagged but not elaborated.

---

## CROSS-SECTOR THEMES

### Byproduct Commodities (Lead, potentially others)
Supply cannot respond to demand drops. This creates a unique dynamic where surplus accelerates, eventually forcing fire-sale prices. Lead is the template; the framework should be applicable to other byproduct commodities.

### Bottleneck Commodities (Copper)
Supply cannot scale as fast as demand. Creates opposite dynamic -- shortages and price spikes. Track daily supply/demand to identify bottleneck emergence.

### Distributed vs. Centralized Scaling
Solar PV and batteries (distributed) can scale exponentially. Grid infrastructure and centralized supply (centralized) can only scale incrementally. This asymmetry is a fundamental driver of disruption across energy, transport, and potentially other sectors.

### Correlation Breaks as Signals
- Oil/gas price correlation broke before Iran war
- Logic/memory chip scaling properties diverged
- These are actionable trading signals that the system should detect proactively.

### Cost Curves Never Stop (Until Physics Says So)
Applied to batteries, solar, AI tokens, semiconductors. No artificial floors. Let the model follow the math.

### Recursive Disruption Loops
Lead is the template: falling battery costs --> EV adoption --> lead-acid displacement --> lead surplus --> further acceleration. Similar recursive loops exist in solar/grid, AI/employment, and potentially other sectors.

---

## SECTOR PRIORITY RANKING (Implied by Meeting Focus)

| Priority | Sector | Reason |
|----------|--------|--------|
| 1 | AI / Employment | Core investment thesis; most meeting time; active positions |
| 2 | Lead | Canonical template for recursive disruption; approaching tipping point |
| 3 | LNG / Natural Gas | Active portfolio position; recent losses; Iran war impact |
| 4 | Solar PV / Batteries | Disrupting force behind lead, LNG, transport |
| 5 | EVs / Transport | Connected to lead, batteries, TaaS thesis |
| 6 | Copper | Bottleneck commodity; emerging opportunity |
| 7 | Semiconductors | Correlation break opportunity (logic vs. memory) |
| 8 | UK Macro | Key geography for unemployment thesis |
| 9 | China | Major disruptor; data gap |
| 10 | Oil | Portfolio tracking; correlation monitoring |
| 11 | DNA Printing / GLP-1 | Framework generalizability test cases; not yet active |
