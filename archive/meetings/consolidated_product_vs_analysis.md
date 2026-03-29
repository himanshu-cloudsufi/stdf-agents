# Consolidated Report: Product Features vs Analysis Features

**Source:** 4 Stellar Capital team meetings (2026-03-06, 2026-03-11, 2026-03-20, 2026-03-26)
**Compiled:** 2026-03-27

---

## PRODUCT FEATURES

### 1. Observability Hub
- **Status:** Existing (released)
- **Who asked:** Tony (originally requested visibility into agents/data factories)
- **Meetings:** Mar 6
- **Details:** Accessible from user initials in the UI. Shows agent network, compliance checklist, Stellar Sense (cron jobs), and data factory overview.

### 2. Agent Network View
- **Status:** Existing
- **Meetings:** Mar 6
- **Details:** Shows all 21 active agents, their purpose, status (active/in-dev), and domain models. Blue = in development, active = live. Part of the Observability Hub.

### 3. Compliance Checklist (C1-C10)
- **Status:** Existing (major release)
- **Who drives:** Dr. Ali / Waleed
- **Meetings:** Mar 6
- **Details:** 10 dimensions of the STDF framework with weighted criteria (critical, high, good-to-have). Includes cost curve analysis, capability analysis, data integrity, adoption curves, tipping points, etc. ~73 micro-agents planned to check compliance. Described by Dr. Ali as "the biggest item we are releasing."

### 4. Online (Real-Time) Evaluation
- **Status:** Existing
- **Meetings:** Mar 6
- **Details:** Quick sanity checks on responses before delivery -- verifies cost-curve-driven analysis, capability-driven analysis, correct data sources.

### 5. Offline (Batch) Evaluation
- **Status:** Existing
- **Meetings:** Mar 6
- **Details:** Comprehensive scoring of all historical chat responses against 10 STDF dimensions. Takes 40-60 minutes per batch run.

### 6. Stellar Sense / Cron Jobs
- **Status:** Existing, being significantly expanded
- **Who drives:** Vasul, Tony (primary demander of expansion)
- **Meetings:** Mar 6, Mar 11, Mar 20, Mar 26
- **Details:**
  - Mar 6: Automated queries on daily/weekly/monthly schedules. Topics adapt based on user conversations. Email delivery being switched to autonomystellar.com.
  - Mar 11: Newsletter feature being built on top of Stellar Sense. Tony wants it to add intelligence, not just news -- convergence signals, bottlenecks, tipping points.
  - Mar 20: Tony demands proactive, SIBA-based insights -- correlation breaks, threshold alerts, risk flags. "What I really want is unprompted self-initiated insights from the software."
  - Mar 26: Central to the "flip" -- Stellar Sense becomes the primary delivery mechanism for the autonomous agent model. Channels: email, WhatsApp, voice. "The response is so proactive that you don't have to wait for it."

### 7. Data Factory Overview Dashboard
- **Status:** Existing
- **Meetings:** Mar 6, Mar 11, Mar 20
- **Details:**
  - Mar 6: Shows health of data factory, ~1,000 curves (cost, adoption, time series), 17 core data providers, refresh status by color (blue = updated, orange = retrying, purple = calculated). Regional/country-level data coverage.
  - Mar 11: 1,108 total curves built. 581 refreshed, 441 pending. Many free sources moved behind paid APIs.
  - Mar 20: Bloomberg data access granted; expected to reach 91% coverage by end of month.

### 8. Auto-Refresh Agent
- **Status:** Existing, being improved
- **Who drives:** Dr. Waleed, Vasul
- **Meetings:** Mar 6, Mar 11, Mar 20, Mar 26
- **Details:**
  - Mar 6: Active, runs 5x/week (business days). Some data daily (Tesla FSD, Waymo). Detects sources, verifies, runs quality checks. Goal: "paint this entire picture blue."
  - Mar 11: AV and automobile data pipelines completed and refreshing daily.
  - Mar 20: Tony demands real-time fetching before analysis: "Let's go fetch the latest data." Jitin proposes auto-detection of stale data.
  - Mar 26: Historical data refresh expected complete by next week. Forecasts start from 2026.

### 9. Data References / Source Provenance
- **Status:** In development (tested), being pushed to production
- **Who asked:** Robert (primary), Tony
- **Meetings:** Mar 6, Mar 20
- **Details:**
  - Mar 6: Shows primary source link and data foundry source link on every response. Robert demands this for validation.
  - Mar 20: References now shown with C3/C5 labels. "W" for web-sourced data. Planning internal source notation and direct links. Tony wants per-source thumbs up/down feedback.

### 10. Email Notification for Long-Running Queries
- **Status:** Built
- **Who asked:** Tony (frustrated by overnight-running prompts)
- **Meetings:** Mar 11
- **Details:** Toggle button -- fire a query, enable notification, get email when response ready, click through to resume chat.

### 11. Fast/Urgent Response Toggle Mode
- **Status:** Proposed/planned
- **Who asked:** Tony
- **Meetings:** Mar 11
- **Details:** Toggle where user signals "response is more important" and system skips non-essential processing for faster delivery. "The model knows that the user needs something immediate."

### 12. Estimated Response Time Display
- **Status:** Proposed
- **Meetings:** Mar 11
- **Details:** Show users an estimate of how long a response will take. Tony: "that makes sense."

### 13. Newsletter Feature
- **Status:** In development (first iteration)
- **Who asked:** Tony
- **Meetings:** Mar 11
- **Details:** First iteration = curated news. Tony's demand: next iteration must add analytical intelligence -- implications, convergence, bottlenecks, tipping points, things not being paid attention to.

### 14. Team Data Input via UI (User Data Upload)
- **Status:** Planned
- **Who asked:** Tony, Richard
- **Meetings:** Mar 11, Mar 20
- **Details:**
  - Mar 11: Allow authorized users to manually add/update data points. Access restricted to a few people (Brad's team, Sachin for testing).
  - Mar 20: Building capability for PowerPoint uploads from field research (Peter, Guido). Connecting to shared folders for China data.

### 15. Per-Source Feedback (Thumbs Up/Down)
- **Status:** Requested
- **Who asked:** Tony
- **Meetings:** Mar 20
- **Details:** Individual thumbs up/down on data citations. Currently have like/dislike at end of chat sessions; per-source is new.

### 16. Data Freshness Detection
- **Status:** Proposed
- **Who asked:** Tony, Jitin
- **Meetings:** Mar 20
- **Details:** System should auto-detect when data is outdated and suggest fetching newer data. "If we are in March 2026 and the data is still February 2026, model should automatically identify that."

### 17. Session-Based Data Gap Resolution
- **Status:** In development
- **Meetings:** Mar 20
- **Details:** Offline processing of all queries to identify data gaps, hunt for missing data, resolve tickets, then re-run queries with updated data.

### 18. Morning Meeting Transcript Integration
- **Status:** Requested
- **Who asked:** Tony
- **Meetings:** Mar 20
- **Details:** System should process morning meeting transcripts and derive insights -- both from individual meetings and cumulatively over 6-9 months.

### 19. Local LLM Processing
- **Status:** Under exploration
- **Who asked:** Tony
- **Meetings:** Mar 20
- **Details:** Tony offered to upgrade Mac hardware. Team to brainstorm options.

### 20. Real-Time Portfolio Monitoring Module
- **Status:** Requested (new)
- **Who asked:** Tony
- **Meetings:** Mar 26
- **Details:** For each portfolio position, define 5-10 tracked metrics. Daily or hourly data collection. Automatic pattern detection and alerts to Tony and Robert. LNG example: track oil prices, EU gas, US gas daily.

### 21. Correlation Break Detection
- **Status:** Requested
- **Who asked:** Tony
- **Meetings:** Mar 20, Mar 26
- **Details:** Monitor scaling properties across technologies and markets. Flag when established correlations break. "Correlations breaking is a huge investment opportunity."

### 22. Proactive Notification System (Multi-Channel)
- **Status:** Requested (expansion of Stellar Sense)
- **Who asked:** Tony
- **Meetings:** Mar 26
- **Details:** Push intelligence via email, WhatsApp, voice. Configurable nudges -- frequency, topics, priority. System prompts users instead of users prompting system.

### 23. Bloomberg Terminal Integration
- **Status:** Initiated
- **Meetings:** Mar 26
- **Details:** Discussions with Peter and Guido. Plan to plug Bloomberg data directly into Stellar Edge for portfolio-related data.

### 24. Bug Fixes Noted
- **System not knowing current date** -- acknowledged as bug (Mar 20)
- **Disruptor cost forecasting going to zero** -- linear projection bug fixed (Mar 26). Lithium-ion SLA batteries for USA 2040 now shows $12 instead of $0.

### 25. Data Heat Map
- **Status:** Exists (confirmed by Vasul)
- **Who asked:** Tony
- **Meetings:** Mar 6
- **Details:** Shows where data has matured vs. white spaces. Tony: "Do you guys have a heat map where we know where the model is... which are the white spaces?"

### 26. Micro-Agents (73 planned)
- **Status:** Planned
- **Meetings:** Mar 6
- **Details:** One per criteria element in the compliance checklist. Each has a specific task and success criteria.

### 27. Dashboard-Based Parameter Tuning
- **Status:** Planned (currently via chat)
- **Meetings:** Mar 6
- **Details:** Currently possible via chat; planned for dashboard UI.

---

## ANALYSIS FEATURES

### 1. SIBA/STDF Framework (Core Methodology)
- **Status:** Existing, continuously reinforced
- **Who drives:** Tony (primary), Robert (validates), Dr. Ali (implements)
- **Meetings:** All 4
- **Details:** Cost curves, S-curves, adoption parameters, tipping points, convergence, bottlenecks, feedback loops, thresholds (10%, 80%), rupture points, scaling properties. Tony demands it as the starting point for EVERY analysis. Mainstream economics (Phillips curve, Laffer curve) is secondary context only.

### 2. AI/Labor (AL) Disruption Model
- **Status:** Existing, actively iterated
- **Who drives:** Jitin (builds), Tony and Robert (demand/validate)
- **Meetings:** All 4
- **Evolution:**
  - Mar 6: Bottom-up model -- 341 BLS occupations, 12,000 tasks (O*NET), 90,000 sub-tasks. For each sub-task: token estimate, cognitive classification, time estimate. Tipping point at AI cost < 50% human cost. S-curve adoption after tipping point. Configurable parameters: capability doubling time (7 months), tipping point threshold (50%), adoption time 10-80% (4 years), cost decline rate (70%/year), adoption ceiling (80%), replacement vs. productivity split (50/50). Model predicted 18-20% unemployment but had zero fit to actual data.
  - Mar 11: Task-level clustering explored -- rule-based (E0/E1/E2 exposure categories) and unsupervised (K-means, hierarchical). Parameters per cluster: time to 80% adoption, adoption lag, replacement ratio, ceiling. Calibration against youth unemployment as target signal. Back-testing framework against 3 years of data.
  - Mar 20: ML-based clustering into 4 clusters (manual tasks, admin/tech, cognitive high-exposure, cognitive already penetrated). Different S-curves per cluster. Aggregated back to task level (away from 90,000 subtasks) for better alignment with real unemployment data. UK model being finalized.
  - Mar 26: 12 feature vectors per task from ONET. K-Medoids clustering into 4 clusters. Full pipeline: capability parity > cost parity > S-curve adoption > hours freed > risk vs. productivity split > ceiling cap. Back-tested against 5 months actual data. Under-predicts -- needs calibration. US and UK reports going live Mar 27. Can tweak parameters in-product.

### 3. Lead Disruption Model
- **Status:** Existing, actively iterated
- **Who drives:** Jitin (builds), Tony (directs)
- **Meetings:** Mar 20, Mar 26
- **Details:**
  - Mar 20: Split 12V battery costs into SLA and EV auxiliary segments. Tipping points moved from 2030-2032 to 2026 (China) / ~2029 (other countries). Supply-side modeling added (primary + secondary from retirements). No cost floors allowed.
  - Mar 26: Two supply-demand views -- (A) annual surplus only, (B) cumulative stockpile with inventory carryover. Tony confirmed: use cumulative stockpile (Table B). Shows surplus in 2026. Tony wants to know when it "falls off a cliff" and prices go negative. Do NOT model recycling decline.

### 4. Back-Testing Framework
- **Status:** In development, actively used
- **Who drives:** Robert (original demand), Tony (reinforces), Jitin (implements)
- **Meetings:** All 4
- **Details:**
  - Mar 6: Robert discovered zero fit to actual data. Proposed use first 3 months to find parameters, test against next 3 months. Start with customer service and software engineering.
  - Mar 11: Backtesting against 3 years of real data since ChatGPT launch. Iterative improvement goal: reduce dispersion.
  - Mar 20: Back-testing against unemployment data (overall, youth, by education level). Tony: "The most important thing is that when we do the back test it kind of fits."
  - Mar 26: Back-tested against 5 months actual data. Model under-predicts. Job-specific back-testing as next step.

### 5. S-Curve Adoption Modeling
- **Status:** Existing
- **Who drives:** Tony (framework), Jitin (implementation)
- **Meetings:** Mar 6, Mar 11, Mar 20, Mar 26
- **Details:** S-curve from 10% to 80% penetration. Different parameters per task cluster. Tony insists on validating where we are on the curve: "We're assuming 10 to 80 percent S curve, but we don't know where we are." Rupture points at 5-10% market share.

### 6. Convergence Analysis
- **Status:** NOT yet done (identified gap)
- **Who drives:** Tony
- **Meetings:** Mar 20
- **Details:** Tony: "We haven't really done convergence... we have as a group threatened to come back to do convergence but we really haven't done it." Convergence, bottlenecks, and feedback loops are "essential to the SIBA framework."

### 7. Correlation Monitoring & Scaling Properties
- **Status:** Requested (analytical capability)
- **Who drives:** Tony
- **Meetings:** Mar 20, Mar 26
- **Details:**
  - Oil/gas price correlation broke at beginning of year before Iran war.
  - Logic chips (Nvidia, AMD) vs memory chips (Hynix, Micron) have different scaling properties.
  - Distributed tech (solar, batteries) scales exponentially; centralized infrastructure (grid) scales incrementally.
  - "Correlations breaking is a huge investment opportunity."

### 8. Rupture Point Detection
- **Status:** Conceptual, being built into Stellar Sense
- **Who drives:** Tony
- **Meetings:** Mar 20, Mar 26
- **Details:** Rupture points at ~5-10% market penetration when new tech becomes cheaper than incumbent even in one market. Software should flag when any market is approaching a rupture point.

### 9. Capacity Factor Analysis
- **Status:** Under consideration (not yet implemented)
- **Who drives:** Tony (proposed concept), Jitin (evaluating)
- **Meetings:** Mar 26
- **Details:** Distinguishes adoption rate from actual utilization. Cars used 5% of the time; TaaS takes it to 50-80%. "Adoption in terms of S-curve is not the same thing as using the technology to its fullest extent." Only add if it improves predictive accuracy.

### 10. Cumulative Surplus / Inventory Modeling
- **Status:** Built (for lead)
- **Who drives:** Jitin, Tony
- **Meetings:** Mar 26
- **Details:** Accounts for inventory buildup over time. Critical for byproduct commodities where supply cannot be shut off (lead from zinc mining + recycling). Shows when surplus becomes overwhelming and prices collapse.

### 11. Supply-Side Constraint Modeling
- **Status:** Being incorporated
- **Who drives:** Tony
- **Meetings:** Mar 6, Mar 26
- **Details:** Tony: "We're assuming straight S curves without checking the potential supply of those tasks from existing data centers." Market trauma = new product cheaper than incumbent but supply is not there. Applied to lead (opposite problem -- supply cannot be stopped) and to copper (supply bottleneck).

### 12. Cost Curve Generalizability
- **Status:** Existing (via compliance checklist)
- **Who drives:** Dr. Ali, Tony
- **Meetings:** Mar 6
- **Details:** Framework enables analysis of new cost curves (DNA printing, GLP-1) even without prior analysis. Tony: "When we have a new cost curve, say DNA printing, essentially, it would know how to do an analysis even though it hasn't done it before."

### 13. Predictive Power Warning / Wealth Warning
- **Status:** Requested
- **Who asked:** Robert
- **Meetings:** Mar 6
- **Details:** System should flag when the model has no recent predictive applicability. Also should flag when disruption IS starting to show up. Robert: "Put it aside and come back and look at it in three months."

### 14. Self-Learning Model
- **Status:** Requested
- **Who asked:** Robert
- **Meetings:** Mar 6
- **Details:** Model should refine its own assumptions and assessments as new data comes in, if data is judged reliable.

### 15. Time-Travel Analysis
- **Status:** Proposed (not yet built)
- **Who asked:** Robert
- **Meetings:** Mar 11 (reported)
- **Details:** Ask the system to forget future knowledge and predict from a past vantage point. Useful for model validation and scenario analysis.

### 16. Task-Level Clustering
- **Status:** Implemented (4 clusters via K-Medoids)
- **Who drives:** Jitin
- **Meetings:** Mar 6 (proposed), Mar 11 (approaches explored), Mar 20 (ML-based clustering done), Mar 26 (K-Medoids with 12 features finalized)
- **Evolution:** Moved from uniform parameters across 90,000 subtasks to 4 distinct clusters with differentiated adoption parameters (manual tasks, admin/tech, cognitive high-exposure, cognitive already penetrated).

### 17. Reaction Functions (Secondary Analysis)
- **Status:** Existing but deprioritized
- **Who drives:** Tony (acknowledges utility as secondary)
- **Meetings:** Mar 20
- **Details:** Mainstream economic reaction functions (Phillips curve, Laffer curve) are useful for understanding policymaker behavior but must always come after SIBA analysis. "It's interesting for the software to come back and do Laffer curve and Phillips curves... which is what policymakers are gonna use."

### 18. Orchestration Layer
- **Status:** Existing
- **Meetings:** Mar 6
- **Details:** Reformulator, clarification agent, lightweight agent, planning agent, main STDF agent, plus micro-agents being built.

### 19. STDF Compliance Framework (C1-C10)
- **Status:** Existing
- **Who drives:** Dr. Ali
- **Meetings:** Mar 6
- **Details:** 10 dimensions with sub-criteria, each weighted. Used for both guiding new analyses and evaluating existing ones. Enables generalizability -- any new cost curve or domain can be analyzed using the same structured approach.

---

## FEATURE EVOLUTION TIMELINE

| Week | Product Focus | Analysis Focus |
|------|--------------|----------------|
| **Mar 6** | Observability Hub release, compliance checklist release, data references in dev, auto-refresh agent active | AL model architecture (90K subtasks), STDF compliance framework, cost curve generalizability |
| **Mar 11** | Email notifications for long queries, urgent toggle proposed, newsletter v1, data factory at 1,108 curves | Task clustering approaches (rule-based + unsupervised), calibration against youth unemployment, backtesting framework |
| **Mar 20** | Source provenance improvements, per-source feedback requested, user data upload, speed/local LLM exploration, unprompted insights proposed | Lead model updated (no cost floors), AL model at task level with 4 ML clusters, convergence identified as gap, correlation monitoring requested |
| **Mar 26** | Portfolio monitoring module requested, multi-channel notifications, Bloomberg integration initiated, autonomous agent paradigm articulated | Cumulative surplus modeling, capacity factor under consideration, K-Medoids clustering finalized, back-testing against 5 months data, rupture point detection |

**Key shift:** From Mar 6 to Mar 26, the product vision evolved from "better chat tool with observability" to "24/7 autonomous agent that prompts the users." The analysis features evolved from "single uniform model" to "clustered, back-tested, multi-commodity framework with proactive insight generation."
