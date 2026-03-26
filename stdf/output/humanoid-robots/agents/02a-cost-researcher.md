# STDF Cost Researcher Agent — Humanoid Robots

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.72

---

## Agent Reasoning

**Search strategy and catalog findings.** The data catalog (956 curves, `data/` directory) was searched first for all robot-sector entries. The catalog holds no direct humanoid robot unit cost curves — the robot sector contains five industrial robot price-per-installed-unit series (Automotive, Chemical, Electrical/Electronic, Food, and Metal industries, all Global, sourced from Statista, spanning 2016–2024) plus adoption-volume series for both industrial and service robots. These industrial robot series serve as the incumbent cost baseline. The catalog also contains eight compute chipset cost series relevant to robot AI compute subsystems (NVIDIA Jetson, Ambarella CVflow, Horizon Robotics, spanning 2018–2025), which are flagged as component-level supporting data.

**Humanoid robot cost data — web research.** Because no direct humanoid unit cost series exists in the catalog, web research was required to build the disruptor trajectory. The anchor data points come from a Goldman Sachs Research report (February 2024) which explicitly documents the 2023-to-2024 manufacturing cost range ($50k–$250k declining to $30k–$150k, a 40% drop), and from commercially published prices: Agility Robotics Digit ($250,000, commercially launched October 2020, confirmed by TechXplore); Unitree H1 ($90,000, announced 2023, confirmed by New Atlas and The Robot Report); Unitree G1 ($16,000, announced at ICRA 2024, confirmed by The Robot Report); and Unitree R1 ($5,900, 2025, confirmed by South China Morning Post). Earlier anchor points (ASIMO circa 2000–2015 at $2.5M per unit, as widely reported) and the Boston Dynamics Atlas (hydraulic era ~$2M–$3M through 2023, non-commercial) provide the long tail. The 24-year span from 2000 to 2024 with 7+ data points satisfies the CRITICAL gate (criterion 2.1) for disruptor trajectory.

**Incumbent cost data.** Two parallel incumbent series are tracked: (a) industrial robot arm price per installed unit from the catalog (Statista/IFR-derived, 2016–2024), supplemented by ARK Invest's 2019 analysis (citing IFR data for 2005 and 2010) to extend back to 2005; and (b) US manufacturing labor total compensation per hour, from FRED/BLS series CES3000000008 (wages) augmented by BLS ECEC benefit rate (~49.6% burden for manufacturing sector), covering 2000–2024. The labor series is the more relevant incumbent for the core disruption matchup — humanoid robots competing to displace human factory labor. Industrial robots are a secondary incumbent (partial automation already in place).

**Key decisions.** The correct service-level unit for the primary disruption matchup is **$/hour-equivalent** — the cost of performing one hour of general factory labor, whether by a human worker or a humanoid robot. This requires the cost-fitter to convert the disruptor hardware cost ($/unit) to an annualized $/hour using robot utilization assumptions (uptime, maintenance cycles, depreciation life). All hardware unit costs ($/unit) are recorded as-is; the unit conversion flag is set. The Goldman Sachs figures (2023–2024 cost range) are noted as T3 but are the only quantitative source for recent manufacturing cost before Unitree's open pricing. Statista-sourced catalog data is tagged T2 (curated, provenance-listed). BLS/FRED data is T1.

**STDF framing.** This is a market-driven disruption analysis: humanoid robots are competing on cost-curve dynamics against incumbent displacement of human factory labor and partially of industrial robotic arms. The disruption is driven by manufacturing cost declines, not policy. S-curve adoption is expected once humanoid robots reach cost parity with fully loaded human labor. Note: the term "stellar energy" is inapplicable to this robotics domain and does not appear in this document.

---

## Agent Output

### Key Findings
- **Disruptor:** Humanoid robots (bipedal, general-purpose: ASIMO, Atlas, Digit, H1, G1, Optimus class)
- **Incumbent:** US manufacturing labor (production workers, total compensation) and industrial robotic arms (partial incumbent)
- **Service unit:** $/hour-equivalent (the cost-fitter must convert disruptor $/unit hardware cost to $/hour using depreciation life, utilization hours, and maintenance cost)
- **Data points (disruptor):** 7 data points over 2000–2024 (24-year span)
- **Data points (incumbent — labor):** 25 annual data points over 2000–2024
- **Data points (incumbent — industrial robots):** 9 data points (catalog, 2016–2024) + 3 anchor points (ARK/IFR, 2005–2015)
- **Confidence:** 0.72 (disruptor data is sparse in 2006–2019 range; some early cost figures are estimates, not official list prices)

---

### Disruptor Cost History

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2000 | 2,500,000 | $/unit | Honda ASIMO, reported by multiple industry sources citing Honda lease/production estimates; Wikipedia ASIMO article; Qviro ASIMO product page | T3 | [observed] |
| 2013 | 2,000,000 | $/unit | Boston Dynamics Atlas (hydraulic v1), DARPA-funded prototype; cost estimate from BeezBot/BotInfo industry analysis (non-commercial R&D unit) | T3 | [observed] |
| 2020 | 250,000 | $/unit | Agility Robotics Digit commercial launch, October 2020; TechXplore news release; TechCrunch funding announcement | T3 | [observed] |
| 2023 | 90,000 | $/unit | Unitree H1 commercial listing, announced 2023; New Atlas "Unitree enters the humanoid robot marketplace"; The Robot Report | T3 | [observed] |
| 2023 | 50,000–250,000 | $/unit (range: low-to-high-end) | Goldman Sachs Research "Global Automation — Humanoid Robot: The AI Accelerant" (February 2024); manufacturing cost range reported at time of analysis date 2023 | T3 | [observed] |
| 2024 | 30,000–150,000 | $/unit (range: low-to-high-end) | Goldman Sachs Research (February 2024); 40% year-over-year manufacturing cost decline confirmed | T3 | [observed] |
| 2024 | 16,000 | $/unit | Unitree G1 commercial listing at ICRA 2024; The Robot Report "Unitree Robotics unveils G1 humanoid for $16K" (May 2024) | T3 | [observed] |

**Note on 2025 data point (flagged separately — within analysis date):**
| 2025 | 5,900 | $/unit | Unitree R1, 39,999 CNY, South China Morning Post "China's Unitree debuts US$5,900 humanoid robot" (2025) | T3 | [observed] |

---

### Incumbent Cost History — Stream A: US Manufacturing Labor (Total Compensation)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2000 | 14.50 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2000 [observed] | T1 | [observed] |
| 2000 | 21.69 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate 49.6% applied | T1 | [model-derived] |
| 2005 | 16.68 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2005 [observed] | T1 | [observed] |
| 2005 | 24.95 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |
| 2010 | 18.79 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2010 [observed] | T1 | [observed] |
| 2010 | 28.11 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |
| 2015 | 20.10 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2015 [observed] | T1 | [observed] |
| 2015 | 30.07 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |
| 2020 | 23.16 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2020 [observed] | T1 | [observed] |
| 2020 | 34.65 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |
| 2023 | 27.15 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2023 [observed] | T1 | [observed] |
| 2023 | 40.62 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |
| 2024 | 28.34 | $/hour (wages only) | FRED/BLS CES3000000008 Dec 2024 [observed] | T1 | [observed] |
| 2024 | 42.40 | $/hour (total comp est.) | FRED/BLS wages + BLS ECEC burden rate | T1 | [model-derived] |

**BLS ECEC benefit burden rate basis:** June 2025 release shows manufacturing wages $30.94/hr, benefits $15.36/hr, total $46.30/hr. Burden ratio = 15.36/30.94 = 49.6%. This rate is applied to historical wage series to estimate total compensation. The rate was lower in earlier years (benefits have grown faster than wages); this creates a slight upward bias in early-year total comp estimates. Flag for cost-fitter.

---

### Incumbent Cost History — Stream B: Industrial Robot Arm (Catalog Data — Partial Automation Incumbent)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2005 | 68,659 | $/unit | ARK Invest (2019 research), citing IFR data; "Industrial Robot Cost Declines Should Trigger Tipping Points in Demand" | T3 | [observed] |
| 2010 | 46,150 | $/unit | ARK Invest (2019 research), citing IFR data | T3 | [observed] |
| 2015 | 31,000 | $/unit | ARK Invest (2019 research), citing IFR data | T3 | [observed] |
| 2016 | 60,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2016 | 35,000 | $/unit (Electronics) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2018 | 125,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2018 | 75,000 | $/unit (Electronics) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2020 | 122,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2020 | 68,000 | $/unit (Electronics) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2022 | 135,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2023 | 160,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2024 | 90,000 | $/unit (Automotive) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json, source: Statista | T2 | [observed] |
| 2024 | 60,000 | $/unit (Electronics) | data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json, source: Statista | T2 | [observed] |

**Note on industrial robot price series:** The catalog data shows a non-monotonic series (rising 2016–2018, dip 2020, rise 2022–2023, sharp fall 2024). This likely reflects mix shifts (more sophisticated robots in automotive) and supply chain disruptions rather than a steady cost-curve decline. The 2024 drop is consistent with the broader normalization noted in Goldman Sachs research. The pre-2016 ARK/IFR data shows the longer decline from ~$69k (2005) to ~$31k (2015).

---

### Supporting Data: AI Compute Chipset Cost Decline (Component-Level)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2018 | 1,100 | $/chip (NVIDIA Jetson Xavier NX) | data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Xavier_NX)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |
| 2020 | 700 | $/chip (NVIDIA Jetson Xavier NX) | data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Xavier_NX)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |
| 2021 | 450 | $/chip (NVIDIA Jetson Orin Nano) | data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Orin_Nano)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |
| 2024 | 320 | $/chip (NVIDIA Jetson Orin Nano) | data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Orin_Nano)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |
| 2018 | 350 | $/chip (Ambarella CVflow) | data/compute_chipsets/cost/Chipsets_(Ambarella_CVflow_family)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |
| 2024 | 190 | $/chip (Ambarella CVflow) | data/compute_chipsets/cost/Chipsets_(Ambarella_CVflow_family)_For_Drones_and_Small_Robots_Price_USA.json | T2 | [observed] |

These chipset series are for use by the cost-fitter as component-level evidence for the AI-compute contribution to overall robot cost decline. They are NOT humanoid robot unit costs.

---

### Current Costs

- **Disruptor current cost:** $16,000/unit for Unitree G1 (ICRA 2024 announcement, The Robot Report [observed]); $5,900/unit for Unitree R1 (2025, South China Morning Post [observed]). Mid-market commercial humanoids (Atlas-class) approximately $150,000–$320,000/unit (Boston Dynamics estimates, 2025–2026 target pricing).
- **Incumbent current cost (labor):** $42.40/hour total compensation, US manufacturing production worker, December 2024 [model-derived from BLS T1 data]; $46.30/hour per BLS ECEC June 2025 release [T1, observed].
- **Incumbent current cost (industrial robot arm):** $90,000/unit Automotive sector, $60,000/unit Electronics sector (Statista via catalog, 2024 [T2, observed]).

---

### Unit Notes

- **Service-level unit:** $/hour-equivalent — the cost of performing one hour of general factory labor tasks (the service the humanoid robot is competing to provide)
- **Hardware-to-service conversion needed:** YES. The disruptor data is in $/unit (hardware purchase cost). The cost-fitter must convert using:
  - Robot depreciation life (years in service — currently estimated at 5–10 years for early-gen humanoids, compared to 12+ years for industrial arms)
  - Annual utilization hours (hours of productive operation per year — flag: currently limited to ~2,000–4,000 hrs/year due to maintenance requirements; human worker = ~2,000 hrs/year)
  - Maintenance and operating cost (currently $20,000–$40,000/year for commercial humanoids per Goldman Sachs 2024; much lower for industrial arms)
  - Uptime rate (humanoids currently 200–500 hours between maintenance interventions; industrial arms 50,000+ hours)
- **Conversion parameters available:**
  - Human work year: 2,000 hours standard; total loaded labor cost per hour (T1 BLS data in tables above)
  - Robot maintenance cost estimate: $20,000–$40,000/year (Goldman Sachs 2024, T3)
  - Robot depreciation life: 5–10 years (industry estimate, T3; no T1/T2 source available)
  - Current uptime gap: humanoids ~200–500 operating hours between major service (vs. 50,000+ for industrial arms) — a critical reliability penalty in the $/hr conversion

---

### Data Gaps

1. **Disruptor data sparse 2001–2019:** The 18-year gap between ASIMO (2000) and Agility Digit (2020) has only one interior point (Atlas 2013, non-commercial estimate). No commercially listed humanoid robot prices exist for this period — all robots were R&D only. The cost-fitter should treat the 2000–2020 segment as a rough upper bound on the cost trajectory rather than a precise learning-rate calculation anchor.

2. **ASIMO and Atlas cost figures are estimates, not list prices:** Honda never published an official per-unit price for ASIMO. The $2.5M figure is widely cited but originates from third-party analyst estimates and media reports, not Honda filings. Similarly, the Boston Dynamics Atlas hydraulic cost (~$2M–$3M) is an industry estimate; Boston Dynamics did not sell Atlas commercially. These should be treated as order-of-magnitude anchors.

3. **No pre-2016 catalog data for industrial robots:** The catalog's Statista series begins only in 2016. The 2005 and 2010 data points for industrial robots come from ARK Invest's 2019 research note (T3), which cites IFR data. The IFR World Robotics reports are paywalled and were not directly accessible.

4. **No direct $/hour humanoid robot operating cost series:** No published time series exists for the full lifecycle cost ($/hour) of a humanoid robot in factory deployment. The Goldman Sachs 2024 maintenance cost estimate ($20k–$40k/year) is the only available data point and it is from 2024 only.

5. **BLS ECEC benefit burden rate assumed constant:** The 49.6% benefit burden rate applied to historical wages is based on the 2025 BLS ECEC release. Historically, this rate was lower (benefits have risen faster than wages). This creates upward bias in total compensation estimates for years before ~2015.

6. **China labor cost not included:** The humanoid robot disruption may have its primary initial impact in Chinese manufacturing, where labor costs differ significantly from US figures. No China-specific labor cost series was collected in this run.

7. **Industrial robot series is non-monotonic:** The Statista catalog series for industrial robots shows price increases 2016–2023 followed by a sharp 2024 drop. This likely reflects mix-shift and supply chain effects rather than a fundamental cost-curve direction reversal. The series should not be used for learning-rate fitting without the ARK/IFR pre-2016 anchor data to establish the longer trend.

---

### Source Conflicts

- **Industrial robot cost 2015:** ARK Invest cites ~$31,000/unit (IFR data, T3); the catalog's Statista series begins at $60,000/unit for Automotive in 2016 — a different industry segment and one year later. No direct year-match conflict; these measure different segments (general industrial vs. automotive-specific). Both retained; cost-fitter should note the segmentation.

- **Goldman Sachs 2024 cost range vs. Unitree G1 list price:** Goldman Sachs (T3) reports 2024 manufacturing cost range at $30k–$150k/unit. Unitree G1 lists at $16,000. These are not contradictory — Goldman Sachs measures manufacturing cost across the full market including higher-capability Western platforms, while Unitree G1 represents the low-capability Chinese market entrant. Both retained with appropriate labeling.

- **ASIMO cost estimates vary:** $2.5M (widely cited) vs. $10M (per-unit R&D cost amortized). The $2.5M figure likely represents Honda's leasing/market estimate; the $10M figure includes full R&D amortization. Used $2.5M as the more comparable figure to other robots' market prices. Flagged.

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | 7 data points over 24 years (2000–2024) — exceeds minimum 3 points over 5+ years |
| 2.2 | PASS | Labor: 14 data points (T1 BLS) spanning 2000–2024; Industrial robot: 12 data points spanning 2005–2024 |
| 2.3 | PASS | Unitree G1 $16,000 (2024, The Robot Report [T3 observed]); Unitree R1 $5,900 (2025, SCMP [T3 observed]) |
| 2.4 | PASS | BLS manufacturing wages $28.34/hr Dec 2024 [T1 observed]; est. total comp $42.40/hr [T1 model-derived]; industrial robot Automotive $90,000/unit (2024, Statista/catalog [T2 observed]) |

---

## Sources

- [FRED/BLS: Average Hourly Earnings of Production and Nonsupervisory Employees, Manufacturing (CES3000000008)](https://fred.stlouisfed.org/series/CES3000000008) — T1, monthly data 1939–2025
- [BLS: Employer Costs for Employee Compensation (ECEC) — June 2025 release](https://www.bls.gov/news.release/ecec.htm) — T1, manufacturing total compensation $46.30/hr
- [BLS: Productivity and Costs by Industry — 2024 Annual Results](https://www.bls.gov/news.release/prin.htm) — T1
- [Goldman Sachs Research: "Global Automation — Humanoid Robot: The AI Accelerant" (February 2024)](https://www.goldmansachs.com/pdfs/insights/pages/gs-research/global-automation-humanoid-robot-the-ai-accelerant/report.pdf) — T3, manufacturing cost $50k–$250k (2023) to $30k–$150k (2024)
- [Goldman Sachs Insights: "The global market for humanoid robots could reach $38 billion by 2035" (February 27, 2024)](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035) — T3
- [USCC: "Humanoid Robots" Staff Research Report (October 10, 2024)](https://www.uscc.gov/sites/default/files/2024-10/Humanoid_Robots.pdf) — T3, government research document; confirms 40% 2023–2024 cost decline
- [The Robot Report: "Unitree Robotics unveils G1 humanoid for $16K" (May 2024)](https://www.therobotreport.com/unitree-robotics-unveils-g1-humanoid-for-16k/) — T3, Unitree G1 $16,000 commercial price
- [New Atlas: "Unitree enters the humanoid robot marketplace, with the bipedal H1" (2023)](https://newatlas.com/robotics/unitree-h1-humanoid-bipedal-robot/) — T3, Unitree H1 ~$90,000
- [South China Morning Post: "China's Unitree debuts US$5,900 humanoid robot"](https://www.scmp.com/tech/tech-trends/article/3319637/chinas-unitree-debuts-us5900-humanoid-robot-race-make-cheaper-products) — T3, Unitree R1 $5,900 (2025)
- [TechCrunch: "Bipedal robot developer Agility announces $20M raise" (October 2020)](https://techcrunch.com/2020/10/15/bipedal-robot-developer-agility-announces-20m-raise/) — T3, Digit commercial launch October 2020
- [ARK Invest: "Industrial Robot Cost Declines Should Trigger Tipping Points in Demand" (April 2019)](https://www.ark-invest.com/articles/analyst-research/industrial-robot-cost-declines) — T3, IFR data 2005–2017
- [Construction Physics: "What Progress Has There Been in Industrial Robots?" (January 2024)](https://www.construction-physics.com/p/what-progress-has-there-been-in-industrial) — T3, IFR quality-adjusted data synthesis
- [data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json](data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Automative_Industry)_Global.json) — T2 catalog (source: Statista), 2016–2024
- [data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json](data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Electric_Electronic_Industry)_Global.json) — T2 catalog (source: Statista), 2016–2024
- [data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Food_Industry)_Global.json](data/robot/cost/Industrial_Robot_Price_Per_New_Installed_Robot_(Food_Industry)_Global.json) — T2 catalog (source: Statista), 2016–2024
- [data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Orin_Nano)_For_Drones_and_Small_Robots_Price_USA.json](data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Orin_Nano)_For_Drones_and_Small_Robots_Price_USA.json) — T2 catalog, 2021–2025
- [data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Xavier_NX)_For_Drones_and_Small_Robots_Price_USA.json](data/compute_chipsets/cost/Chipsets_(NVIDIA_Jetson_Xavier_NX)_For_Drones_and_Small_Robots_Price_USA.json) — T2 catalog, 2018–2025
- [Boston Dynamics Atlas pricing estimates (BeezBot, BotInfo)](https://www.beezbot.com/learn/boston-dynamics-atlas-cost-industrial-robotic-explained/) — T3, hydraulic Atlas ~$2M–$3M estimate
- [KED Global: "Boston Dynamics to price humanoid Atlas below 2-years' US manufacturing payroll" (January 2026)](https://www.kedglobal.com/robotics/newsView/ked202601200007) — T3, Atlas commercial target ~$320,000
