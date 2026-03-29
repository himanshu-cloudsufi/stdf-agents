# Consolidated Report: Tony vs Robert -- Wants, Priorities & Tensions

**Source:** 4 Stellar Capital team meetings (2026-03-06, 2026-03-11, 2026-03-20, 2026-03-26)
**Compiled:** 2026-03-27

---

## TONY -- What He Wants, Demands, and Prioritizes

### 1. Data Quality & Precision

Tony's #1 operational demand, repeated in every meeting with increasing intensity.

- **Mar 6:** "To make this investable, a lot hinges on accuracy and precision." Demands real-time, accurate, up-to-the-minute data as "non-negotiable."
- **Mar 11:** Willing to pay for premium data sources -- "if we think that that data might be useful, then shout... let's see what we can do." Confirms Bloomberg credentials are available.
- **Mar 20:** Escalates: "The model is improving in terms of thinking but not in terms of precision and without precision nothing else... without precision we are gonna lose money." Demands real-time data fetching before any analysis runs -- "Let's go fetch the latest data... let's do it real time rather than start the processing with whatever data we have."
- **Mar 26:** Reiterates that complexity without predictive power is unwelcome: "It has to be predictive. If it's not predictive, we don't want to introduce complexity just to introduce complexity."

**Evolution:** Moved from "data must be accurate" (Mar 6) to "precision is the difference between making and losing money" (Mar 20) to "only add what improves prediction" (Mar 26).

### 2. SIBA/STDF Framework as the Non-Negotiable Edge

The framework (cost curves, S-curves, tipping points, convergence, bottlenecks, feedback loops) is sacred.

- **Mar 6:** "You always say it's always a capability cost curve. That's how it flows."
- **Mar 11:** "It's important to always do the SIBA framework... that's not optional." One of his sessions failed to run it.
- **Mar 20:** Erupts when a UK unemployment query returned Phillips curve analysis instead of SIBA: "I don't really care about Phillips curve and Laffer curve... that's mainstream economics. To me, it really adds no value." Also: "That is our edge. And if we don't do it, then we're not doing anything."
- **Mar 20:** Same problem on LNG: "To go off and do an analysis of LNG without doing cost curves of solar wind and battery and so on, doesn't add anything."
- **Mar 26:** SIBA is the foundation for all proactive insight generation -- Stellar Sense must track signals as evidence for/against SIBA hypotheses.

**Evolution:** From framework reminder (Mar 6) to non-negotiable commandment (Mar 11) to frustrated correction of violations (Mar 20) to embedding it as the core of the autonomous agent (Mar 26).

### 3. Speed of Response

- **Mar 11:** A prompt ran overnight: "it took so long, I just walked... I woke up to it." Wants a toggle for urgency -- in meetings with Robert, they need real-time answers.
- **Mar 20:** Asks about local LLM processing, willing to upgrade Mac hardware. But: "I don't want to sacrifice precision" for speed.
- **Mar 20:** "I don't want bad results quickly."

**Evolution:** Speed is important but consistently subordinated to precision. Willing to pay more for faster tokens.

### 4. Analysis Methodology

#### No Cost Floors
- **Mar 20:** Interrupts Jitin on battery cost floors: "Wrong wrong. Do not do that, please." Tells the Moore's Law story -- people at Intel in 1992 said the cost curve couldn't continue, and it's still going and accelerating.
- **Mar 20:** "Cost curves are like gravity, and they will continue until of course they don't... it's not up to you or me to determine when that is the case."
- **Mar 26:** Confirmed again in lead model -- no declining recycling rates, no cost floors.

#### Unemployment Over GDP
- **Mar 11:** "I want us to focus on unemployment more than on GDP growth." Ranked geography priority: US > UK > China > EU. Wants youth unemployment and college graduate unemployment tracked specifically.

#### Regional Costs, Not PPP
- **Mar 6:** "Let's not use purchasing power parity... Let's use cost, right? Cost is real, but it's different in every market."

#### Back-Testing is Mandatory
- **Mar 6:** Validates Robert's back-testing demand.
- **Mar 11:** "If we don't test it on actual data, what are we gonna test it on?"
- **Mar 20:** "The most important thing is that when we do the back test it kind of fits."
- **Mar 26:** Back-testing against 5 months of actual unemployment data; model under-predicts -- needs calibration.

#### Convergence Analysis is Overdue
- **Mar 20:** "We haven't really done convergence... we have as a group threatened to come back to do convergence but we really haven't done it."

#### Clustering for Validation
- **Mar 6:** "We can't do it for all the tasks, but maybe we can cluster them."

### 5. Product Direction

#### Unprompted, Self-Initiated Insights (Biggest Shift)
- **Mar 20:** First articulated -- wants cron-job-based proactive insights: correlation breaks, threshold alerts, risk flags, scaling property changes. "What I really want is unprompted self-initiated insights from the software." Start with 5 things.
- **Mar 26:** This becomes the central product vision: "We need to flip Stellar Edge from essentially a chat-based kind of exercise to around the clock, infinite loop kind of software. Basically, we don't prompt the software, it prompts us."

#### Portfolio Position Tracking
- **Mar 26:** "We need a module for portfolio -- each position and 5 or 7 or 10 things that we should be tracking every day." LNG example: track oil prices, EU natural gas, US natural gas daily.

#### Correlation Break Detection
- **Mar 20:** Oil/gas correlation broke at the beginning of the year before the Iran war. "It would have been nice for us to understand that."
- **Mar 26:** "Correlations breaking is a huge investment opportunity for us."

#### Newsletter Must Add Intelligence, Not Just News
- **Mar 11:** "News is super abundant and not that interesting anymore." Wants: convergence signals, emerging bottlenecks, tipping points, systemic implications, "things not being paid attention to."

#### Open Innovation / Hackathon
- **Mar 6:** Wants to discover model blind spots through open innovation challenge.
- **Mar 11:** Wants it as "a branding exercise" and a technology exercise. Advertise on Dor Cache and top AI podcasts.

### 6. Investment Approach & Edge Timing

- **Mar 11:** "The usefulness, the value of this tool is never gonna be bigger than now... there's never gonna be as big a difference between our edge and the market than now." Mainstream economists believe new jobs will replace lost ones; this narrative has "probably another year" of life.
- **Mar 20:** "Our opportunity is now... as long as we can do this right."
- **Mar 11:** Believes GDP growth and unemployment growth will happen concurrently -- the market does not expect this.
- **Mar 20:** "We're a macro fund. We trade not just stocks, but also commodities, currencies, rates."

### 7. Data Sources & Chinese Intelligence

- **Mar 20:** "A lot of our disruptions -- China is definitely one of the top disruptors in pretty much everything, so getting Chinese data is kind of important."
- **Mar 11:** Wants field intelligence from analysts at conferences ingested into the system: "we know what the cost of lithium ion is today because we spoke with the company today."
- **Mar 20:** Wants Jane's macro economics data fed in for context. Wants PowerPoints from Peter and Guido's China trips ingested.

---

## ROBERT -- What He Wants, Demands, and Prioritizes

### 1. Data Accuracy Is the #1 Problem

Robert's primary and most passionately stated demand.

- **Mar 6:** "I think a lot of problems with the data." Spent hours fighting incorrect data -- system couldn't find the Fed funds rate correctly, insisted on wrong data, used "tertiary sources," didn't check timestamps. Web search quality is "really just wrong."
- **Mar 6:** Wants data reference links on every response so he can validate sources himself.
- **Mar 20:** Continues actively querying the system and needing source clarity.

### 2. Back-Testing & Predictive Validation

Robert's defining analytical demand.

- **Mar 6:** "My realization... I went from super comfortable to not at all comfortable was when I said, okay, with these assumptions, go back six months and predict what the next five months of data would be... And there's no fit whatsoever."
- **Mar 6:** "Why are we pretending that this is insightful and predictive when it actually today has no predictive power?"
- **Mar 6:** The model predicted ~18-20% unemployment but had zero fit to actual data.

### 3. Model Self-Awareness & Wealth Warnings

- **Mar 6:** Model should flag when it has no predictive power: "The model should say, 'Hey, just so you know, looking at the last recent data, this model does not appear to have applicability.' ... Put it aside and come back in three months."
- **Mar 6:** Model should also flag when disruption IS starting to show up in the data.
- **Mar 6:** Model should self-learn and self-refine from incoming data.

### 4. Non-Linear Disruption Thresholds

Robert articulated a key insight about AI capability and disruption thresholds:

- **Mar 6:** "At 16 minutes [between hallucinations], maybe it doesn't show up. At 20 minutes, maybe it's an augmenter of my productivity. At four hours, it's a fucking beast. And at 64 hours, I'm gone."
- This framing connects AI reliability milestones to specific disruption outcomes -- augmentation vs. replacement is non-linear.

### 5. Time-Travel Analysis

- **Mar 11 (reported):** Robert tried to "time travel with the model" -- asking the system to forget future knowledge and predict from a past vantage point (e.g., go back to 2000 and predict mobile phone evolution). The team noted this is a good feature idea but not yet built.

### 6. Humility About Predictions

- **Mar 6:** "There's no reason to believe that anything we predict for DEC 26 will take place. Nothing. Zip. Because the last three months and last six months, zip of what we predicted came true."
- Robert has made real trading decisions based on model outputs and "taken significant risk" that resulted in "very big mistakes."

### 7. Power User of the Platform

- **Mar 26 (Tony speaking):** "Even Robert sits in front of this like hours at a time, but even four hours is just one sixth of the day."
- Robert is actively querying the system for AI/employment disruption analysis alongside Tony.

---

## SHARED -- Where Tony and Robert Agree

### Data Accuracy is Make-or-Break
Both insist that inaccurate data destroys the product's value. Tony frames it as precision for investment decisions; Robert frames it as trust through validation. Both demand source provenance on every data point.

### Back-Testing is Non-Negotiable
Both demand models be validated against historical data. Tony: "if we don't test it on actual data, what are we gonna test it on?" Robert: back-testing is "the ABC."

### The Edge is Now
Both believe the analytical window is at its maximum. Tony states it explicitly (Mar 11, Mar 20). Robert's urgency shows through his heavy daily usage and willingness to trade on model outputs.

### AI/Employment is the Core Thesis
Both are heavily using the AL disruption model. Tony ranks it as the top analytical priority. Robert's sessions define the questions the team should pursue.

### SIBA Framework is the Foundation
Tony is more vocal, but Robert's analytical approach (going back to test predictions, seeking non-linear thresholds) is consistent with the SIBA methodology.

### Alerts and Proactive Intelligence
Tony explicitly demands the flip to autonomous agents (Mar 26). Robert would be a primary beneficiary -- Tony specifically says alerts should go to "me or Robert."

---

## TENSIONS -- Where They Differ or Emphasize Different Things

### Philosophical vs. Operational Emphasis

| Dimension | Tony | Robert |
|-----------|------|--------|
| **Primary frame** | Vision and edge -- "this is our edge, the opportunity is now" | Empirical validation -- "show me the data fits" |
| **Reaction to model failure** | Push forward, iterate, keep the disruption thesis | Step back, acknowledge zero predictive power, question everything |
| **Risk tolerance** | Dogmatic on certain disruptions: "ICE vehicles are done," "cost curves are like gravity" | More cautious: "There's no reason to believe anything we predict" |
| **Speed vs. precision** | Wants both, but willing to trade speed for precision | Wants the model to admit when it doesn't know |

### Trust in the Model

- **Tony** maintains conviction in the disruption framework even when the model fails to predict near-term data. He treats model failures as calibration problems, not framework problems.
- **Robert** questions whether the framework itself has current applicability when predictions diverge from reality. He frames the model as "pre-tipping point" and suggests shelving it when it lacks predictive power.

### Near-Term vs. Long-Term Focus

- **Tony** is comfortable being "very dogmatic about certain things" because the long-term disruption thesis is intact.
- **Robert** is focused on near-term trading reality -- "What's relevant today is the Iran war." He has been "burned by being too dogmatic about the disruption thesis when near-term macro dominated."

### Reasons for Model Failure

When the AL model showed zero fit to actual unemployment data:
- **Tony** treats this as a parameter calibration problem to be solved through iteration.
- **Robert** generates 9+ hypotheses for why the model might not work (economic upswing masking displacement, regulatory barriers, infrastructure lag, non-linear thresholds, startup growth timelines, etc.) -- more willing to question the thesis itself.

### Self-Awareness vs. Conviction

- **Robert** wants the model to issue "wealth warnings" when it lacks applicability -- essentially an automated humility mechanism.
- **Tony** wants the model to be assertive about the disruption thesis and use SIBA as the starting point for every analysis, with mainstream economics relegated to secondary context.

These are complementary tensions rather than contradictions -- Robert provides the empirical discipline that prevents Tony's conviction from becoming blind faith, while Tony provides the strategic direction that prevents Robert's caution from becoming paralysis.
