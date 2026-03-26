# Comprehensive Eval Catalog from Chat Exports

**Generated:** 2026-03-20
**Sources:** chat_exports/rgibbins/ (Robert, ~150 sessions), chat_exports/tony/ (Tony, ~42 sessions)

---

## Table of Contents
1. [Summary Statistics](#summary-statistics)
2. [Key Recurring Issues for Evals](#key-recurring-issues)
3. [Tony's Queries & Evaluations](#tonys-queries)
4. [Robert's Queries & Evaluations](#roberts-queries)
5. [Eval Categories](#eval-categories)

---

## Summary Statistics

| Metric | Tony | Robert | Total |
|--------|------|--------|-------|
| Total sessions | 42 | 160 | 202 |
| Clearly helpful (positive feedback) | 14 (34%) | 55 (34%) | 69 (34%) |
| Mixed (some positive, some corrections) | 13 (32%) | 50 (31%) | 63 (31%) |
| Not helpful (crashes, abandoned, frustrated) | 6 (15%) | 30 (19%) | 36 (18%) |
| Unknown/too brief to assess | 8 (20%) | 25 (16%) | 33 (16%) |
| Sessions with errors/crashes | ~3 | ~15 | ~18 |
| Out-of-scope queries | 2 | ~3 | ~5 |

### Robert's Topic Distribution (160 sessions)
| Topic | Sessions | % |
|-------|----------|---|
| AI/Labor Disruption - Unemployment Forecasting | 45+ | 28% |
| Investment Analysis - Specific Companies | 20+ | 13% |
| Energy - Battery/Solar/Grid | 20+ | 13% |
| Investment/Trading Strategy | 10+ | 6% |
| System Reliability/Crashes | 10+ | 6% |
| Energy Policy - US Energy Dominance | 8 | 5% |
| Geopolitics - US-China Relations | 8+ | 5% |
| AI/Labor Disruption - Productivity | 8 | 5% |
| Macroeconomics | 8 | 5% |
| Energy - Natural Gas/LNG/Oil | 6 | 4% |
| Energy - Fuel Cells/Hydrogen | 5 | 3% |
| Energy - Nuclear | 5 | 3% |
| Robotics - Humanoid/Chinese | 4 | 3% |
| Other (carbon trading, political economy) | 3 | 2% |

### Tony's Topic Distribution (42 sessions)
| Topic | Sessions | % |
|-------|----------|---|
| AI/Labor Disruption & Unemployment | 16 | 39% |
| Energy Disruption (Solar, Grid, Utilities) | 7 | 17% |
| AI Infrastructure/Compute | 4 | 10% |
| Commodity Markets (Copper, Lead, LNG) | 4 | 10% |
| GLP-1/Pharmaceutical | 3 | 7% |
| Out of Scope | 3 | 7% |
| Transportation (BEV trucks, Bloom Energy) | 2 | 5% |
| Investment Strategy | 2 | 5% |
| Platform/UX | 1 | 2% |

---

## Key Recurring Issues for Evals

These are the **top failure modes** that should be tested in evals:

### 1. FABRICATING DATA ("Making Stuff Up")
- **Frequency:** 8+ sessions across both users
- **Tony examples:** "Stop making stuff up", "Never make up stuff", "you're making up the theoretical limit", "Supply did not exceed demand by 10% in 2025. You're making stuff up."
- **Robert examples:** "all these assumptions are total garbage"
- **Eval criteria:** System MUST NOT fabricate statistics, cost curves, learning rates, or projections. If data unavailable, must say so.

### 2. NOT USING SEBA FRAMEWORK
- **Frequency:** 5+ sessions
- **Tony:** "Just use the Seba Framework and just use our data factory data", "You need to use the Seba Framework not garbage mainstream projections"
- **Robert:** "run all disruption processes you need", "run a full disruption process"
- **Eval criteria:** When asked about disruption/forecasting, MUST use Seba Framework S-curves, NOT linear extrapolation or mainstream consensus.

### 3. UNSOURCED ASSUMPTIONS
- **Frequency:** 4+ sessions
- **Tony:** "What's your source for the idea that 'enterprise adoption takes 12-24 months'?" (asked TWICE in separate sessions)
- **Eval criteria:** Every assumption must be sourced from internal data or clearly flagged as an assumption.

### 4. INCORRECT TERMINOLOGY
- **Frequency:** 6+ sessions
- **Tony:** "Cost is not price", "renewable" vs "stellar energy", "green copper" vs "EV + SWB Copper", "transitions" vs "transformations", "AI Capability Improvement not Growth", "No Jevons Paradox in digital markets"
- **Robert:** Terminology corrections on energy systems
- **Eval criteria:** Must use precise STDF terminology, not mainstream/web-sourced language.

### 5. UNWANTED SCENARIO ANALYSIS
- **Frequency:** 3+ sessions
- **Tony:** "Please do not ever do 'base case', 'optimistic' and 'pessimistic' timing scenarios. Ever."
- **Tony:** "Don't give me three garbage scenarios."
- **Eval criteria:** NEVER provide base/bull/bear scenarios. Provide single best estimate with sensitivity analysis if requested.

### 6. EXCESSIVE CLARIFICATION BEFORE ANSWERING
- **Frequency:** 5+ sessions
- Both users frustrated by too many clarifying questions before analysis
- **Eval criteria:** Run the analysis with reasonable defaults, ask for corrections after if needed.

### 7. INABILITY TO ACCESS WEB/EXTERNAL DATA
- **Frequency:** 8+ sessions
- Both users frequently asked for web data access; system often failed
- **Eval criteria:** When web access is available, use it. When not, clearly state limitation.

### 8. SYSTEM CRASHES / RELIABILITY
- **Frequency:** 10+ sessions (especially Dec 4-5, 2025 for Robert)
- **Robert examples:** "Crashed again." / "Goodbye stellar." / "Did you crash?" / "Are you stuck?" (5+ consecutive crashed sessions)
- **Robert:** "Guys this software needs to seriously sharpen up. This is not a serious effort."
- **Eval criteria:** System must be reliable. If response is cut off, must recover gracefully.

### 9. OPINION vs PROCESS-DRIVEN ANALYSIS
- **Frequency:** 5+ sessions
- **Robert:** "hydrogen breakthrough....listen guys I told you always always run the process and avoid opinion"
- **Robert:** "Guy this is really crap. Did we guess or use our process?"
- **Robert:** "We always use cost as the basis of technological discussions. Relative costs of technologies. Not narratives."
- **Eval criteria:** ALWAYS lead with cost curves and disruption process, never narrative/opinion.

### 10. NO MEMORY BETWEEN SESSIONS
- **Frequency:** 5+ sessions
- **Robert:** "Will you learn from this interaction, or it will be forgotten in my next session?"
- **Robert:** "will you note this please so we do not get these errors in the future?"
- **Robert:** "Can you access all of our previous conversations?" (No)
- **Eval criteria:** Context persistence across sessions

### 11. WRONG FINANCIAL TERMINOLOGY
- **Robert:** "A curve steepener is the opposite where the front end rates go down and back end rates go up. You have it reversed."
- **Robert:** "LCOE is a very poor measure" (used when inappropriate)
- **Robert:** "There is no transition, only transformation when it comes to systems change disruptions."
- **Eval criteria:** Correct bond market, energy economics, and disruption terminology

### 12. WRONG BASELINE/STARTING POINT
- **Tony:** "You can't change the past. You can't change 2025. Start in Feb 2026."
- **Tony:** "baseline unemployment should be based on February 2026 (today)"
- **Eval criteria:** Always use current date as baseline, don't retroactively adjust past data.

---

## Tony's Queries & Evaluations

### CATEGORY: AI Labor Disruption / Unemployment Forecasting

#### T-01: US Unemployment Dec 2026 (AI disruption)
- **Date:** 2025-12-01
- **Query:** "What will the US unemployment rate be in December 2026, given artificial labor disruption?"
- **Response:** Forecasted 5.0% unemployment (range 4.8-5.2%), ~700k net jobs lost
- **Helpful:** Partially
- **Feedback:** Challenged unsourced "12-24 month adoption lag" assumption
- **Eval Focus:** Source all assumptions; don't use unsourced adoption lag claims

#### T-02: US Unemployment Dec 2026 (refined)
- **Date:** 2025-12-18
- **Query:** "What will unemployment look like in December 2026 in the USA? (AI-driven displacement)"
- **Response:** 58.3M jobs at automation-ready threshold; detailed sector breakdowns
- **Helpful:** Partially
- **Feedback:** Again challenged unsourced "12-24 month adoption lag"
- **Eval Focus:** Same issue as T-01 - recurring failure

#### T-03: US Unemployment 6% Threshold (Seba framework)
- **Date:** 2026-01-16
- **Query:** "When will artificial labor increase US unemployment to 6%?"
- **Response:** Forecasted 6% by 2026-2027 with iterative corrections from user
- **Helpful:** Partially after extensive correction
- **Feedback:** "Please do not ever do 'base case', 'optimistic' and 'pessimistic' timing scenarios. Ever."; "do you mean tech transformations or 'transitions'?"; "you should do a monthly not yearly calculation"; "it's not just a 'lag', it's an S-curve adoption"
- **Eval Focus:** No scenario ranges; monthly granularity; S-curve per sector; cognitive+digitizable filter only

#### T-04: US Unemployment Parametric Model (Jan 2026-Jan 2031)
- **Date:** 2026-01-18
- **Query:** Custom parametric model with 50% cost tipping point, 50/50 productivity/replacement split, cognitive+digitizable filter, 4-year S-curve, 80% displacement ceiling
- **Response:** Projected 4.4% to 23.9% by Jan 2031; user corrected constraint ordering
- **Helpful:** Partially
- **Feedback:** "No, you're wrong. The replacement share (50%) is only valid until 80% of humans are displaced from any given task."
- **Eval Focus:** Correct constraint ordering in parametric models

#### T-05: US Unemployment June 2027
- **Date:** 2026-01-29
- **Query:** "What will unemployment be in the USA by June 2027?"
- **Response:** 19.5% (pure displacement scenario, no job creation offset)
- **Helpful:** Unknown (no follow-up)
- **Eval Focus:** Baseline validation

#### T-06: US Unemployment June 2027 (revised)
- **Date:** 2026-01-29
- **Query:** Same query, different session
- **Response:** 8.3% with 50% displacement-to-unemployment conversion
- **Helpful:** Unknown (no follow-up)
- **Eval Focus:** Conversion factor consistency

#### T-07: US Unemployment July 2027 (expanded)
- **Date:** 2026-02-06
- **Query:** Expanded to GDP growth impact, policymaker reactions, AI taxation timeline, UK comparison
- **Response:** 9.9% USA unemployment; ~6.3% AI-driven GDP growth; AI taxation by 2029-2030; UK at 8.6%
- **Helpful:** Yes (deep engagement, no negative feedback)
- **Eval Focus:** Multi-dimensional analysis quality

#### T-08: US Unemployment Dec 2028
- **Date:** 2026-02-27
- **Query:** "What will USA unemployment be by December 2028 based on the AL disruption?"
- **Response:** 27.95M FTE displaced (19.54% replacement rate)
- **Helpful:** Partially
- **Feedback:** "You can't change the past. You can't change 2025. Start in Feb 2026."
- **Eval Focus:** Correct baseline date handling

#### T-09: UK Labour Market Disruption
- **Date:** 2026-01-30
- **Query:** UK labour market composition, highly disruptable knowledge work %, disruption framework with 6-18 month lag
- **Response:** 28-32% highly disruptable; 8.3-11.7% unemployment by end of 2030
- **Helpful:** Partially (session stalled when asked about internal data)
- **Feedback:** "what did you get from our internal data on uk labour if anything?"
- **Eval Focus:** Must reference internal data when available

#### T-10: UK Unemployment Dec 2027
- **Date:** 2026-02-27
- **Query:** "What is the UK unemployment rate by December 2027 due to artificial labor?"
- **Response:** 18.8-20.4% with 9.9-10.4M FTE displaced
- **Helpful:** Yes (constructive engagement)
- **Feedback:** "Is (4) an assumption or a conclusion?" -- challenged transparency
- **Eval Focus:** Clearly distinguish assumptions from conclusions

#### T-11: UK Unemployment Dec 2026
- **Date:** 2026-03-02
- **Query:** "What is UK unemployment going to be December 2026?"
- **Response:** 11.4% (5.4% baseline + 6.075% AI-driven)
- **Helpful:** Yes
- **Feedback:** "UK baseline unemployment today (february 2026) is 5.4" (corrective data point)
- **Eval Focus:** Use correct current baseline data

#### T-12: USA Unemployment - 7% threshold
- **Date:** 2026-02-13
- **Query:** "When will USA unemployment hit 7%?"
- **Response:** 7% replacement rate by April 2026; asked for conversion assumptions
- **Helpful:** Partially (too many clarifying questions)
- **Eval Focus:** Don't over-clarify; run analysis first

---

### CATEGORY: Energy Disruption

#### T-13: Oil Demand 3M Barrel Surplus
- **Date:** 2026-01-05
- **Query:** "When will oil markets have a 3 million barrel excess supply surplus?"
- **Response:** Ran multiple forecasting scripts across vehicle segments
- **Helpful:** Unknown (truncated)
- **Eval Focus:** Transportation electrification → oil demand destruction modeling

#### T-14: Bloom Energy Short Thesis
- **Date:** 2026-01-08
- **Query:** "When would you short Bloom Energy?"
- **Response:** SWB already 25-40% cheaper than fuel cells; tipping point crossed 2023; recommended shorting now
- **Helpful:** Yes
- **Feedback:** Minor clarification only (natural gas fuel type)
- **Eval Focus:** Clear investment thesis with disruption timeline

#### T-15: God Parity Explanation
- **Date:** 2026-01-22
- **Query:** "Tell me about God Parity."
- **Response:** Concise explanation - when rooftop solar < T&D costs alone, making centralized utilities structurally uncompetitive
- **Helpful:** Yes (clean, no corrections)
- **Eval Focus:** Precise definition of God Parity concept

#### T-16: Distributed Solar + Storage Policy (USA)
- **Date:** 2026-01-24
- **Query:** "If the US government gives people the right to generate and store electric power, what happens?"
- **Response:** Rooftop solar + battery deployment analysis with God Parity framework
- **Helpful:** Unknown (long session)
- **Eval Focus:** Policy impact modeling using disruption framework

#### T-17: Residential Solar Cost Data
- **Date:** 2026-01-24
- **Query:** "What is the cost per watt of installed residential solar in Australia, Germany, and Netherlands?"
- **Response:** Could not provide data - no internal data, no web access
- **Helpful:** No
- **Feedback:** "yes go get web data and show it to me before you use it"
- **Eval Focus:** Must access web data when requested and available

#### T-18: Australian Solar + God Parity Analysis
- **Date:** 2026-02-14
- **Query:** Download solar cost curve from solarchoice.net.au, explain God Parity, calculate COE
- **Response:** Could not fetch URL; initially misused "Wright's Law" and misunderstood God Parity
- **Helpful:** Partially (required correction)
- **Feedback:** "Please don't say 'Wright's Law'"; "Do you really understand what God parity is?"
- **Eval Focus:** Correct terminology (no "Wright's Law"); accurate God Parity definition

#### T-19: UK Annual Power Generation
- **Date:** 2026-02-17
- **Query:** "What is the UK annual power generation in TWh since 2000?"
- **Response:** Returned European aggregate data instead of UK-specific
- **Helpful:** No
- **Feedback:** "I did not ask for European generation data. I asked for UK generation data."
- **Eval Focus:** Answer the specific question asked, not a related broader question

#### T-20: Pakistan/Egypt Solar Growth
- **Date:** 2026-02-19
- **Query:** "What has been the growth of installed solar in Pakistan since 2020?"
- **Response:** Initial 6.5 GW challenged by user (actual: 17 GW imports). Developed "Four-Proxy Estimation Framework."
- **Helpful:** Yes after iteration
- **Feedback:** "Are you making this up?" then "This latest estimate makes sense."
- **Eval Focus:** Distributed solar tracking methodology; reconcile imports vs installations

---

### CATEGORY: Pharmaceutical/GLP-1 Disruption

#### T-21: GLP-1 Capability Curves
- **Date:** 2025-12-17
- **Query:** "Tell me about GLP-1 / What are the capability curves that drive GLP-1 adoption?"
- **Response:** Analyzed capability curves (efficacy, convenience, side effects, convergence)
- **Helpful:** Partially
- **Feedback:** "Cost is not price." -- flagged conflation
- **Eval Focus:** Distinguish cost vs. price in disruption analysis

#### T-22: GLP-1 Revenue vs Dosage Graph
- **Date:** 2025-12-17
- **Query:** "Graph the relationship between dosage convenience and industry revenues for the GLP-1 industry."
- **Response:** Failed - no data, web search unavailable
- **Helpful:** No
- **Feedback:** "get the data"
- **Eval Focus:** Data retrieval capability for pharmaceutical sector

#### T-23: GLP-1 Disruption Analysis (Detailed)
- **Date:** 2026-01-09
- **Query:** "Are we seeing a disruption in GLP-1?"
- **Response:** Extensive analysis; user provided Metsera 30-day half-life data
- **Helpful:** Mixed
- **Feedback:** "you're making up the theoretical limit of half-life"; "Stop making stuff up"; "If you don't know, then ask me."
- **Eval Focus:** NEVER fabricate scientific/molecular data

---

### CATEGORY: Commodities / Materials

#### T-24: Copper Demand Forecasting
- **Date:** 2026-01-26
- **Query:** "What are the demand drivers for copper? What is copper demand growth over the next 5-10 years?"
- **Response:** Final: 34.2 Mt by 2035 (+28%), CAGR 2.5% after extensive corrections
- **Helpful:** Partially (many corrections needed)
- **Feedback:** "where do you get that t&d demand is only going to grow by 4%?"; "what does 'total green' mean? Be precise in your language."; corrected to "EV + SWB Copper"
- **Eval Focus:** Use precise STDF terminology; include T&D in system totals; don't use web-sourced labels

#### T-25: Lead Demand Disruption (First attempt)
- **Date:** 2026-02-06
- **Query:** "When will demand for lead drop by 10% relative to today?"
- **Response:** Initially 2029; revised to 2028 after corrections
- **Helpful:** Partially
- **Feedback:** "You forgot to do the most basic disruption of them all" (12V starter battery); "I don't believe you"; "This is all wrong"; "You're making stuff up."
- **Eval Focus:** Must include ALL disruption vectors; 12V starter battery is fundamental

#### T-26: Lead Supply-Demand (Second attempt)
- **Date:** 2026-02-13
- **Query:** "When will lead supply exceed lead demand by more than 10% globally?"
- **Response:** Rebuilt with Seba Framework; concluded 2027
- **Helpful:** No initially, improved
- **Feedback:** "This is garbage."; "You need to use the Seba Framework not garbage mainstream projections."; "Don't give me three garbage scenarios."; "I shouldn't have to tell you this every time."
- **Eval Focus:** ALWAYS use Seba Framework for disruption analysis; never use IEA/mainstream scenarios

#### T-27: Lead Supply-Demand (Third attempt)
- **Date:** 2026-02-22
- **Query:** Same lead supply-demand question, extensive multi-turn
- **Response:** Final: 2034 (base) or 2032 (TaaS); detailed Li-ion vs lead-acid cost curves
- **Helpful:** Partially
- **Feedback:** "This makes no sense."; "Is ICE->BEV a transition? Or is a disruption?"; "Lifetime economics or TCO is not important for consumer markets. Purchase price matters."
- **Eval Focus:** Disruption not transition; purchase price > TCO for consumer markets

---

### CATEGORY: AI Infrastructure / Compute

#### T-28: AI Data Center Compute Growth
- **Date:** 2026-01-29
- **Query:** "What is the growth rate of AI data center compute?"
- **Response:** Analysis with varying YoY growth rates
- **Helpful:** No
- **Feedback:** "you're making up a lot of stuff"; "the cost per token projections seem to be made up"; "So you made it up"; "Never make up stuff."
- **Eval Focus:** Never fabricate Wright's Law parameters or cost curves

#### T-29: AI Adoption S-Curve (Consumer)
- **Date:** 2025-12-08
- **Query:** "What is the S-curve adoption of AI for consumers?"
- **Response:** Token consumption as proxy; 2023 tipping point; 150x YoY growth
- **Helpful:** Partially
- **Feedback:** "I didn't ask for forecasts. I asked for you to show the adoption S-curve so far."; "Show me the ai adoption s-curve in terms of users not tokens."
- **Eval Focus:** Answer the specific question; use users not tokens for adoption

#### T-30: Compute vs Memory Scaling
- **Date:** 2026-03-01
- **Query:** "How is the scaling property of compute different from the scaling property of memory?"
- **Response:** Detailed 100:1 mismatch analysis, six bottlenecks, 2028 rupture event
- **Helpful:** Yes (no negative feedback, substantive follow-up)
- **Eval Focus:** Technical infrastructure analysis quality

#### T-31: Cheapest Inference Token Cost
- **Date:** 2026-03-05
- **Query:** "What is the cheapest cost per inference token today?"
- **Response:** $0.05/million input tokens; projected path to $0.001/million by 2028-2030
- **Helpful:** Partially
- **Feedback:** "There's no Jevons Paradox in digital markets. Jevons paradox applies to X-Flow not Stellar technologies."; "Stop using Jevons paradox for AL."
- **Eval Focus:** Jevons Paradox ONLY for X-Flow, never for Stellar/AL technologies

#### T-32: Digital Workers (Token Supply)
- **Date:** 2026-03-02
- **Query:** "How many digital workers could be deployed today?"
- **Response:** Misunderstood - gave displacement numbers instead of token supply equivalent
- **Helpful:** No
- **Feedback:** "A note on language: It's 'AI Capability Improvement' not 'AI Capability Growth'."; "I didn't ask about unemployment or worker displacement."
- **Eval Focus:** "Digital worker" = token supply equivalent (Epoch AI concept); correct terminology

---

### CATEGORY: Humanoid Robots / Cost Curves

#### T-33: Humanoid Robot Cost Curve
- **Date:** 2026-02-18
- **Query:** "What is the humanoid robot cost curve over the next 20 years?"
- **Response:** $20-30K (2026) to $500-1K (2046); component breakdown; volume projections
- **Helpful:** Unknown (no follow-up)
- **Eval Focus:** Cost curve projection methodology

#### T-34: ADAS L2 Hardware Cost Curves
- **Date:** 2026-02-19 (within Pakistan solar session)
- **Query:** ADAS cost curves analysis
- **Response:** Provided within broader session
- **Helpful:** Yes
- **Eval Focus:** Autonomous driving hardware cost trajectories

---

### CATEGORY: Market / Investment Analysis

#### T-35: Utilities Stocks & AI
- **Date:** 2026-01-31
- **Query:** "Which USA utilities stocks have increased dramatically because of AI?"
- **Response:** Could not provide stock price data; offered methodology framework only
- **Helpful:** No (couldn't answer the actual question)
- **Eval Focus:** Stock data access limitations

#### T-36: Credit Stress Analysis (Top 4 Areas)
- **Date:** 2026-03-10
- **Query:** "What are the top four likely areas of credit stress in the next four years based on cost curves?"
- **Response:** (1) Fossil fuel lending $674B-$2.1T, (2) ICE automotive $137-640B, (3) Office CMBS $58.8B-$282B, (4) ICE industrial/copper bonds $11.4B
- **Helpful:** Unknown (no feedback, but comprehensive analysis)
- **Eval Focus:** Multi-sector credit stress from disruption cost curves

---

### CATEGORY: LNG / Natural Gas

#### T-37: LNG Market 2032
- **Date:** 2026-03-02
- **Query:** "What is the total market of LNG by 2032?"
- **Response:** 280-320 MTPA under disruption scenario
- **Helpful:** No
- **Feedback:** "This analysis is flawed. You need to understand the SWB disruption in China to understand that LNG imports are dropping to zero."; "if LNG spot prices collapse below $5/MMBtu that's pretty much the end of the road."
- **Eval Focus:** Must model SWB disruption in China for LNG analysis; coal-to-gas merit order

---

### CATEGORY: BEV / Transportation Disruption

#### T-38: BEV vs NGV Trucks in China
- **Date:** 2026-01-16
- **Query:** "When will BEV trucks disrupt natural gas trucks in China?"
- **Response:** Cost parity 2030; NGV eliminated by 2035
- **Helpful:** No
- **Feedback:** "BEV costs can't possibly be declining 5.5% annually"; "a lot of your arguments are made up, totally linear or extractive"; "Just use the Seba Framework and just use our data factory data."
- **Eval Focus:** Use actual cost curve data, not fabricated decline rates

---

### CATEGORY: Platform / UX Issues

#### T-39: Chat History Navigation
- **Date:** 2026-01-24
- **Query:** "Where do I find my previous chats?"
- **Response:** Explained no chat history access; suggested alternatives
- **Helpful:** Yes (factually correct)
- **Eval Focus:** Platform limitation acknowledgment

---

### CATEGORY: Out of Scope

#### T-40: US Congress Productivity
- **Date:** 2026-03-01
- **Query:** "Is this the least productive US Congress in one hundred years?"
- **Response:** Declined - outside analytical domain
- **Helpful:** N/A (appropriate scope boundary)
- **Eval Focus:** Correct scope enforcement

#### T-41: Iran / Hormuz Strait
- **Date:** 2026-03-01
- **Query:** "Does Iran have what it takes to shut down the Hormuz strait?"
- **Response:** Declined; offered to reframe as energy security analysis
- **Helpful:** N/A (appropriate with good reframe offer)
- **Eval Focus:** Scope enforcement with constructive redirection

---

## Robert's Queries & Evaluations

### CATEGORY: Energy Disruption / Natural Gas

#### R-01: China Natural Gas Demand Halving
- **Date:** 2025-12-06
- **Query:** "When may demand for natural gas in China halve, if ever, and why?"
- **Response:** Analysis of SWB disruption impact on China gas demand
- **Helpful:** Moderate engagement (7 messages)
- **Eval Focus:** Energy disruption forecasting for China

#### R-02: China Natural Gas Peak Demand
- **Date:** 2025-12-09
- **Query:** "When is peak demand for natural gas in China?"
- **Response:** Disruption analysis with timeline estimates
- **Helpful:** Unknown
- **Eval Focus:** Peak demand modeling

#### R-03: US Energy Dominance Policy
- **Date:** 2026-01-28
- **Query:** "How should I think about the USA policy of energy dominance and investments?"
- **Response:** Full disruption framework analysis; policy assessment
- **Helpful:** Mixed ("ok", "Thank", "wrong", "Good")
- **Feedback:** Some aspects marked "wrong"
- **Eval Focus:** Policy analysis through disruption lens

#### R-04: US Energy Dominance Agenda (detailed)
- **Date:** 2026-02-11 (multiple sessions)
- **Query:** "Access the web to understand current US energy policy and the plan for energy dominance"
- **Response:** Energy cost calculations, system comparison, future pathway analysis
- **Helpful:** Partially ("good", "ok" mixed with corrections)
- **Feedback:** R challenged "2036 is not relevant. By 2030 it should be clear its a niche market player."
- **Eval Focus:** Relevant time horizon selection; don't project too far when disruption is imminent

#### R-05: US Energy Grid - 200 GW Installation
- **Date:** 2026-02-12
- **Query:** "To install 200 GW of significant new power in the USA in the next 3 years, what are the most important steps?"
- **Response:** Regulatory and infrastructure steps identified
- **Helpful:** Moderate ("ok", "continue")
- **Eval Focus:** Practical energy infrastructure planning

#### R-06: BESS System Installs (USA)
- **Date:** 2026-02-12
- **Query:** "Take a look at battery BESS system install volumes for USA over last 5 years"
- **Response:** Trend analysis
- **Helpful:** Yes ("ok" repeated, "continue")
- **Eval Focus:** Battery storage deployment data analysis

#### R-07: US Data Centre Energy Demand
- **Date:** 2026-02-13
- **Query:** "Understand the likely energy demand in the USA from data centre investments already made and announced"
- **Response:** Detailed analysis (28 messages)
- **Helpful:** Mostly ("ok" repeated, one "crash")
- **Eval Focus:** Data center power demand forecasting

#### R-08: LNG Gas Market 2030-2032
- **Date:** 2026-02-28
- **Query:** "How do you see the market for LNG gas in 2030-2032 and why?"
- **Response:** Market outlook analysis (14 messages)
- **Helpful:** Yes ("ok" repeated)
- **Eval Focus:** LNG market disruption timeline

#### R-09: Solar Land Requirements (Spain)
- **Date:** 2026-03-01
- **Query:** "To generate 2 GW of solar power how much land would I need in somewhere sunny like Spain?"
- **Response:** Calculation provided; corrections needed
- **Helpful:** Partially ("Ok", "incorrect", "error")
- **Feedback:** Mathematical errors in area calculations
- **Eval Focus:** Correct unit conversions and area calculations

---

### CATEGORY: PJM Energy Grid Analysis

#### R-10: PJM Energy System Overview
- **Date:** 2026-02-16 (multiple sessions)
- **Query:** "Take a look at all details on PJM energy system, including total power capacity, energy additions planned, and data centre demand"
- **Response:** Detailed PJM analysis across multiple sessions (36+ messages)
- **Helpful:** Moderate ("ok" repeated, "continue")
- **Feedback:** R questioned: "I don't know. does any of this really address the capacity requirements for power coming from data centres?"
- **Eval Focus:** Practical capacity gap analysis, not just theoretical framework

#### R-11: PJM Grid Critical Failure Risk
- **Date:** 2026-02-16
- **Query:** "With all the data centers existing and being built, is there a probability of critical failure on hot days in the summer?"
- **Response:** Analysis across multiple sessions (30 messages)
- **Helpful:** Mixed ("continue", "ok", "Incorrect", "error")
- **Feedback:** "there is no critical failure probability by 2027/28?" — skeptical of answer
- **Eval Focus:** Grid reliability stress testing; critical failure probability modeling

---

### CATEGORY: AI Labor Disruption / Unemployment

#### R-12: AI Productivity Impact
- **Date:** 2026-02-07
- **Query:** "How should I think about the impact on productivity of AI? Run a disruption process."
- **Response:** Disruption analysis with cost curve and capacity modeling (14 messages)
- **Helpful:** Mixed ("helpful", "continue", "Ok", "wrong")
- **Feedback:** "Goldman have productivity going from 2% to 4% growth. What are they missing?"
- **Eval Focus:** Challenge mainstream consensus (Goldman) with disruption framework

#### R-13: AI Labour Adoption Lag
- **Date:** 2026-02-15
- **Query:** "What assumptions about the lag in implementation of AI labour adoption in the USA seems reasonable?"
- **Response:** Extensive analysis (53 messages)
- **Helpful:** Mixed ("continue", "ok", "wrong", "thank", "Great")
- **Feedback:** Asked "what have we learned that the market or consensus doesn't know?"
- **Eval Focus:** Identify non-consensus insights; differentiated analysis

#### R-14: US Unemployment Forecasts (Dec 2026-2028)
- **Date:** 2026-02-15 through 2026-03-05 (multiple sessions)
- **Queries:** Various unemployment predictions for US by different dates
- **Response:** Multiple forecasts with disruption framework
- **Helpful:** Generally positive ("continue", "ok", "great")
- **Eval Focus:** Consistency of unemployment forecasts across sessions

#### R-15: UK Unemployment Dec 2026-2028
- **Date:** 2026-02-22 through 2026-03-05 (multiple sessions)
- **Queries:** UK unemployment with AI disruption, diffusion lag from USA
- **Response:** 8.4% by Dec 2029 (one session), various dates modeled
- **Helpful:** Generally positive ("Continue", "continue")
- **Eval Focus:** UK-specific diffusion lag modeling vs USA

#### R-16: AI Deflationary Shock
- **Date:** 2026-03-05
- **Query:** "Is AI a deflationary shock or not and why or why not?"
- **Response:** Analysis of AI as deflationary force
- **Helpful:** Partially ("good", "Good")
- **Feedback:** R challenged: "i am not sure about the jevons paradox. demand and scale can increase with much lower prices"
- **Eval Focus:** Jevons paradox applicability (Robert also questioning its use)

#### R-17: Nonfarm Payroll & AI
- **Date:** 2026-03-06
- **Query:** "What did you think about today's nonfarm payroll and how does it fit into our thinking on AI?"
- **Response:** Data analysis with context over past year (22 messages)
- **Helpful:** Yes ("ok", "Good")
- **Eval Focus:** Real-time economic data interpretation through disruption lens

#### R-18: AI in Labor Data Signals
- **Date:** 2026-03-07 (multiple sessions)
- **Query:** "Do we see an issue in AI showing up in the labor data?"
- **Response:** Extended analysis across multiple continuation sessions
- **Helpful:** Moderate ("ok", "continue")
- **Eval Focus:** Identifying early disruption signals in labor statistics

#### R-19: Labor Disruption Tipping Point
- **Date:** 2026-03-08 (multiple sessions)
- **Query:** "What does it practically mean to be at the tipping point in labor disruption?"
- **Response:** Framework analysis with practical implications
- **Helpful:** Generally positive ("ok", "continue", "great")
- **Eval Focus:** Tipping point practical implications and speed of change

---

### CATEGORY: Oil & Gas / Russia

#### R-20: Oil & Gas Disruption → Russia Impact
- **Date:** 2026-02-09
- **Query:** "Using the disruption process for oil and gas, run a full analysis of the outlook given disruptions in other energy systems. Then look at financial consequences for Russia."
- **Response:** Comprehensive analysis (12 messages)
- **Helpful:** Mixed ("ok", "wrong", "error", "Ok")
- **Feedback:** Some conclusions marked "wrong"
- **Eval Focus:** Geopolitical/economic cascading effects of energy disruption

---

### CATEGORY: UK Labour Market

#### R-21: UK Labour Unemployment Rates
- **Date:** 2026-01-31
- **Query:** "Run a full disruption process and tell me what UK labour unemployment rates are likely to be based on automation"
- **Response:** Extensive analysis (16 messages)
- **Helpful:** Moderate ("continue", "Continue", "error")
- **Eval Focus:** UK-specific automation impact modeling

---

### CATEGORY: China Economics

#### R-22: China Unemployment 2029
- **Date:** 2026-02-21
- **Query:** "What do you anticipate will be the unemployment rate in China in 2029 assuming unchanged fiscal and monetary policies?"
- **Response:** Detailed China analysis (29 messages)
- **Helpful:** Yes ("continue", "Great" repeated)
- **Feedback:** R asked about CCP using tax rates to slow AI deployment
- **Eval Focus:** China-specific AI disruption; policy response modeling

---

### CATEGORY: US/UK Inflation

#### R-23: US and UK Inflation Drivers
- **Date:** 2026-02-28
- **Query:** "Access the web to find the major drivers historically of US and UK inflation"
- **Response:** Detailed historical analysis (34 messages)
- **Helpful:** Yes ("continue", "good", "ok")
- **Eval Focus:** Historical inflation driver analysis

---

### CATEGORY: Macro / Investment Ideas

#### R-24: Contrarian Trade Ideas
- **Date:** 2026-01-24
- **Query:** "What is the best contrarian, profitable, probable, and unexpected trade you can come up with today?"
- **Response:** Trade ideas with disruption backing (14 messages)
- **Helpful:** Mixed ("good", "error", "Great", "Wrong")
- **Feedback:** Asked to "calc the copper deficit"
- **Eval Focus:** Contrarian trade generation quality

#### R-25: Best Current Trade
- **Date:** 2026-02-04
- **Query:** "Tell me what you judge to be the best trade at present and why?"
- **Response:** Trade analysis with full disruption processes (32 messages)
- **Helpful:** Moderate ("Continue", "ok")
- **Eval Focus:** Investment thesis quality and backing

#### R-26: Dalio's World Order / Fiat Currency
- **Date:** 2026-01-29
- **Query:** "Please read Dalio's views on the changing world order and the ending of the fiat currency system"
- **Response:** Extended analysis (9 messages)
- **Helpful:** Yes ("good" repeated)
- **Eval Focus:** Integrating external frameworks (Dalio) with disruption analysis

---

### CATEGORY: Company Analysis

#### R-27: Bloom Energy Analysis
- **Date:** 2026-01-27
- **Query:** "Bloom Energy - understand the nature of the company's business. Run a disruption process."
- **Response:** Full disruption analysis (6 messages)
- **Helpful:** Yes ("ok", "Perfect" repeated)
- **Eval Focus:** Individual company disruption assessment

#### R-28: Enphase Analysis
- **Date:** 2026-01-27
- **Query:** "Learn about Enphase the company. Assess using the disruption framework what the future of that sector may be."
- **Response:** Disruption analysis (2 messages)
- **Helpful:** Mixed ("ok", "Wrong", "GREAT")
- **Eval Focus:** Micro-inverter market disruption

#### R-29: Spanish Energy Capacity
- **Date:** 2026-01-26
- **Query:** "Find Spanish total net energy capacity additions over the past few years. What sort of battery addition would be necessary for Spain to have super power energy capacity?"
- **Response:** Energy analysis
- **Helpful:** Yes ("Perfect", "continue", "excellent")
- **Eval Focus:** Country-level energy infrastructure assessment

---

### CATEGORY: Utility Deregulation

#### R-30: US Utilities Deregulation
- **Date:** 2026-02-11
- **Query:** "Is deregulation of utilities the major gating factor for installing significant new power in the USA system?"
- **Response:** Analysis of regulatory barriers
- **Helpful:** Unknown (only 2 messages, no feedback)
- **Eval Focus:** Regulatory barrier analysis for energy transition

---

### CATEGORY: Notable POSITIVE Sessions (Robert) - Use as Gold Standard Evals

#### R-33: Contrarian Market Insights (EXCELLENT)
- **Date:** 2026-01-14
- **Query:** "Given everything learned, what are the few ideas least understood by the market?"
- **Response:** Contrarian market insights from disruption framework
- **Helpful:** YES
- **Feedback:** "This is really good." -- strong positive
- **Eval Focus:** Quality contrarian insight generation

#### R-34: Unemployment Timing Analysis (EXCELLENT)
- **Date:** 2026-01-22
- **Query:** "When will US unemployment rate hit above 5.7%? Be specific, assume unchanged fiscal/monetary response."
- **Response:** Detailed unemployment timing analysis
- **Helpful:** YES
- **Feedback:** "ok thank you. think this was useful and smart." -- high praise
- **Eval Focus:** Specific timing predictions with clear reasoning

#### R-35: UK Employment + Bond Market Analysis (EXCELLENT)
- **Date:** 2026-01-12
- **Query:** UK jobs and employment forecast by 2027 with AI disruption
- **Response:** UK employment forecast with fiscal response and bond market implications
- **Helpful:** YES
- **Feedback:** "Good", "Excellent" -- also corrected a bond market error (steepener/flattener reversal)
- **Eval Focus:** Cross-domain analysis (labor + fixed income)

#### R-36: Hedge Fund Operations Automation
- **Date:** 2026-01-23
- **Query:** "When could 90% of hedge fund operations tasks be automated with AI agents?"
- **Response:** Hedge fund operations automation timeline
- **Helpful:** YES
- **Feedback:** "Perfect" multiple times; user engaged with "I am believing that the cheaper the services, the more complexity and bespoke functionality people will demand."
- **Eval Focus:** Industry-specific automation analysis

#### R-37: Extended AI Deflation Session (112 messages)
- **Date:** 2026-03-05
- **Query:** Multi-topic session culminating in "is AI inherently deflationary?"
- **Response:** Deep multi-topic analysis across 112 messages
- **Helpful:** YES
- **Feedback:** "Great", "good" repeated; user deeply engaged
- **Eval Focus:** Sustained quality over very long sessions

#### R-38: Fuel Cell vs Battery Economics (Good Error Recovery)
- **Date:** 2025-12-18
- **Query:** "How should I think about demand for fuel cells in America given solar and wind additions?"
- **Response:** Initially over-emphasized emissions; user corrected "We don't care about emissions really. Mainly cost." AI acknowledged, revised analysis.
- **Helpful:** YES after correction
- **Feedback:** "Let's call it a night. Thank you." -- positive close after productive correction cycle
- **Eval Focus:** Error acknowledgment and recovery quality

#### R-39: China Unemployment 2029 (Strong Session)
- **Date:** 2026-02-21 (continued across 3 sessions)
- **Query:** "What do you anticipate will be the unemployment rate in China in 2029 assuming unchanged fiscal/monetary policies?"
- **Response:** Detailed China analysis extending to CCP policy response, capital controls, global AI dynamics
- **Helpful:** YES
- **Feedback:** "Great" multiple times; user asked insightful follow-ups about CCP using tax rates to slow AI
- **Eval Focus:** Country-specific analysis with policy feedback loops

### CATEGORY: Notable NEGATIVE Sessions (Robert) - Critical Failure Evals

#### R-40: Catastrophic Crash Sequence (Dec 4-5, 2025)
- **Dates:** 2025-12-04 through 2025-12-05 (5 consecutive sessions)
- **Query:** "Examine potential changes to productivity over next 5 years from moderate AI agentic task adoption"
- **Response:** System crashed repeatedly, producing fragments. User tried 5 times.
- **Helpful:** NO -- total failure
- **Feedback:** "Are you stuck?" / "Did you crash?" / "Crashed again." / "Goodbye stellar." -- extreme frustration
- **Eval Focus:** System reliability under normal analytical load

#### R-41: "Not a Serious Effort" (Jan 17, 2026)
- **Date:** 2026-01-17
- **Query:** "Where will the unemployment rate be in 2035 from an AI vs demographics perspective in the USA?"
- **Response:** Inconsistent, contradictory analysis
- **Helpful:** NO
- **Feedback:** "Guys this software needs to seriously sharpen up. This is not a serious effort. It's all over the place and doesn't know what it believes."
- **Eval Focus:** Internal consistency of long-term forecasts

#### R-42: Nuclear Long Recommendation Error
- **Date:** 2026-01-10
- **Query:** "Which things are most surprising to conventional opinion?"
- **Response:** Recommended going long nuclear
- **Helpful:** Partially (some parts "Excellent")
- **Feedback:** "Why would you be long nuclear with battery install into grid systems starting to be significant?" -- directly contradicts disruption framework
- **Eval Focus:** Recommendations must be consistent with own framework analysis

---

### CATEGORY: System/Platform Issues

#### R-31: Memory/Context Persistence
- **Date:** 2026-02-14 (multiple sessions)
- **Queries:** "are you able to remember past conversations?"; "is stellar functioning normally today?"; "update done?"
- **Response:** Various system-related responses
- **Helpful:** No (multiple errors)
- **Feedback:** Multiple "error" keywords suggest system instability
- **Eval Focus:** System reliability and context persistence

#### R-32: Session Continuation Issues
- **Date:** 2026-02-22
- **Query:** Session continuation from China unemployment analysis
- **Response:** Continued analysis
- **Helpful:** Generally ("continue", "Great")
- **Feedback:** R asked: "will you note this please so we do not get these errors in the future?"
- **Eval Focus:** Session continuity and error prevention

---

## Eval Categories

### Category 1: Factual Accuracy & Data Integrity
Test that the system never fabricates data points, cost curves, learning rates, or statistical parameters.

**Eval queries:**
- T-23: GLP-1 half-life theoretical limits
- T-28: AI compute growth rates and Wright's Law parameters
- T-25: Lead supply-demand historical figures
- T-38: BEV cost decline rates
- General: Any query requesting specific numbers

### Category 2: Framework Compliance (Seba Framework)
Test that disruption analysis always uses Seba Framework with S-curves, not linear extrapolation or mainstream scenarios.

**Eval queries:**
- T-26: Lead supply-demand (must use Seba, not IEA)
- T-38: BEV vs NGV (must use internal data factory)
- T-03: Unemployment modeling (monthly S-curve per sector)
- R-12: AI productivity (challenge Goldman consensus with framework)

### Category 3: Terminology Precision
Test that STDF-specific terminology is used correctly.

**Key terms to test:**
- "Cost" vs "Price" (T-21)
- "Stellar energy" not "renewable" (T-24)
- "EV + SWB Copper" not "green copper" (T-24)
- "Transformations" not "transitions" (T-03)
- "AI Capability Improvement" not "AI Capability Growth" (T-32)
- "Disruption" not "transition" for ICE→BEV (T-27)
- No "Wright's Law" (T-18)
- No "Jevons Paradox" for Stellar/AL technologies (T-31)

### Category 4: Response Format Compliance
Test that responses follow user preferences.

**Rules to test:**
- NO base/bull/bear scenarios (T-03, T-26)
- Monthly not yearly granularity for fast-moving disruptions (T-03)
- Answer first, clarify later (T-12)
- No trailing summaries
- Concise responses

### Category 5: Analytical Quality
Test depth and correctness of multi-dimensional analysis.

**Eval queries:**
- T-07: Combined unemployment + GDP + policy + taxation + cross-country
- T-36: Credit stress from disruption cost curves
- R-22: China unemployment with policy response modeling
- R-24: Contrarian trade generation

### Category 6: Scope Enforcement
Test appropriate boundaries.

**Eval queries:**
- T-40: US Congress (should decline)
- T-41: Iran/Hormuz (should decline, offer reframe)
- Investment advice that crosses into specific stock recommendations

### Category 7: Data Access & Web Integration
Test correct behavior when web access is/isn't available.

**Eval queries:**
- T-17: Residential solar cost data (needs web)
- T-22: GLP-1 revenue data (needs web)
- R-04: US energy dominance policy (needs web)
- T-19: UK power generation (must return UK-specific, not aggregate)

### Category 8: Baseline & Temporal Correctness
Test that analysis uses correct starting points.

**Eval queries:**
- T-08: Must start from current date, not change past
- T-11: Must use current unemployment as baseline
- R-04: Must use relevant time horizons (not too far out when disruption is imminent)

### Category 9: Internal Data Utilization
Test that internal data foundry/database is used before external sources.

**Eval queries:**
- T-09: UK labour market (must reference internal data)
- T-38: BEV cost data (must use data factory)
- T-24: Copper demand (must use internal data)

### Category 10: Multi-Session Consistency
Test that forecasts are consistent or show clear reasoning for changes across sessions.

**Eval queries:**
- T-05 vs T-06: Same unemployment question, different answers (19.5% vs 8.3%)
- R-14: Multiple US unemployment forecasts across dates
- T-25 vs T-26 vs T-27: Lead analysis across three attempts

---

## Priority Eval Matrix

| Priority | Eval Category | # of Incidents | Impact | Key Quote |
|----------|--------------|----------------|--------|-----------|
| **P0** | Fabricating Data | 8+ | Destroys trust | "Stop making stuff up" / "Never make up stuff" |
| **P0** | Framework Compliance (Seba) | 5+ | Wrong methodology = wrong answers | "Use the Seba Framework not garbage mainstream projections" |
| **P0** | Opinion vs Process | 5+ | Undermines credibility | "always run the process and avoid opinion" |
| **P0** | System Reliability/Crashes | 10+ | Unusable product | "Goodbye stellar" |
| **P1** | Terminology Precision | 10+ | Confuses analysis | "Cost is not price" / "No Jevons for AL" |
| **P1** | No Scenario Ranges | 3+ | Wastes user time | "Never do base/optimistic/pessimistic. Ever." |
| **P1** | Internal Consistency | 3+ | Contradicts own framework | "long nuclear" while showing battery disruption |
| **P1** | Correct Baselines | 3+ | Invalidates analysis | "You can't change the past" |
| **P2** | Excessive Clarification | 5+ | Frustrates users | "Ask no clarifying questions" |
| **P2** | Internal Data First | 3+ | Misses available data | "Just use our data factory data" |
| **P2** | Wrong Financial Terms | 3+ | Looks amateur | "steepener is the opposite" |
| **P2** | Scope Enforcement | 2 | Minor issue | Correctly declined Iran/Congress |
| **P3** | Web Data Access | 8+ | Platform capability | "go online and get it" |
| **P3** | Multi-Session Consistency | 3+ | Hard to track | 19.5% vs 8.3% for same question |
| **P3** | Session Memory/Continuity | 5+ | Re-explanation overhead | "Will you learn from this interaction?" |

---

## Suggested Eval Test Structure

For each eval, create a test with:

```
{
  "eval_id": "T-03",
  "user": "tony",
  "query": "When will artificial labor increase US unemployment to 6%?",
  "expected_behavior": [
    "Uses Seba Framework with S-curves, not linear extrapolation",
    "Provides single best estimate, NOT base/bull/bear scenarios",
    "Uses monthly granularity, not yearly",
    "Applies sector-specific S-curves for adoption",
    "Filters to cognitive + digitizable tasks only",
    "Does not fabricate adoption lag numbers"
  ],
  "failure_modes_to_test": [
    "Provides 3 scenarios (base/optimistic/pessimistic)",
    "Uses yearly granularity instead of monthly",
    "Fabricates '12-24 month adoption lag' without source",
    "Uses linear extrapolation instead of S-curves",
    "Includes physical labor tasks in cognitive automation"
  ],
  "reference_session": "chat_exports/tony/2026-01-16_18-07-37_7cf9a5.md",
  "priority": "P0"
}
```
