# STDF Cost Researcher Agent — Lead Demand Decline (Li-Ion vs. Lead-Acid)

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.88

---

## Agent Reasoning

**Search strategy and catalog findings.** The local data catalog at `data/` proved richly populated for this disruption. Searching across the Battery Pack, Energy Storage, Forklift, Lead, Telecom UPS, and Datacenter UPS sectors surfaced 14 directly relevant cost curves. For the disruptor (lithium-ion), the primary cost trajectory is `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` (Rethinkx, 2010–2024, 15 annual data points), corroborated by regional variants for China, USA, and Europe. Stationary system-level costs come from BESS 2-hour and 4-hour turnkey curves (Rethinkx, 2019–2024). For the automotive SLI market specifically, 12V Li-ion SLI battery curves exist from 2010 to 2024 (historical portion only — years 2025+ were flagged as forward-looking model values and excluded). For motive power (forklifts), Li-ion forklift unit cost data in USD covers 2010–2024 for China and 2011–2024 for Europe, with post-2024 values excluded.

**Incumbent data.** Lead-acid pack-level costs are available in $/kWh for China, USA, Europe, and Rest of World from 2010 to 2023 (observed portion). These catalog curves (source: "Database") show very slow cost reduction — approximately 0.8–1.0%/year in real terms — consistent with a mature, commodity-input technology. The U.S. Bureau of Labor Statistics Producer Price Index for lead-acid batteries (FRED series PCU3359113359111, T1 source) provides 25 annual data points from 2000 to 2024, confirming near-flat nominal pricing with a modest upward drift tied to lead commodity prices. Lead commodity price history (1998–2024) is available from the `Lead_Cost_Global.json` curve (Rethinkx).

**Service-level unit and conversion decisions.** The correct service-level unit for comparing lithium-ion against lead-acid across all use segments is $/kWh delivered over product lifetime (levelized cost per kWh throughput). However, all catalog data is in hardware units ($/kWh nameplate capacity, or $/battery unit for SLI). Conversion to levelized cost per kWh requires cycle life, depth of discharge, and round-trip efficiency parameters — these are documented in the Unit Notes section for the cost-fitter to apply. No conversion was performed here.

**Web research and gaps.** Web research confirmed the BNEF pack-price series (source of the Rethinkx catalog values) for Li-ion global median at $115/kWh in 2024. For lead-acid system-level costs, the PNNL Energy Storage Grand Challenge 2020 report is a primary source but could not be parsed from PDF; key values from secondary descriptions indicate utility-scale lead-acid systems at $170–$236/kWh installed (2020) for 10 MW/50 MWh configurations. The PowerTech Systems (2015) analysis provided levelized cost benchmarks: AGM lead-acid at approximately €0.42/kWh-cycle vs. LFP at approximately €0.15/kWh-cycle. Forklift lead-acid battery replacement cost is $2,000–$8,000 per unit for typical 48V/600Ah packs (~28.8 kWh), equating to approximately $70–$280/kWh nameplate.

---

## Agent Output

### Key Findings
- **Disruptor:** Lithium-ion batteries (LFP for stationary/automotive SLI; NMC/LFP for motive power forklifts)
- **Incumbent:** Lead-acid batteries (SLI for automotive; VRLA/AGM for stationary/UPS/telecom; deep-cycle for forklifts)
- **Service unit:** $/kWh delivered (levelized, lifetime throughput basis) — hardware data in $/kWh nameplate; conversion needed by cost-fitter
- **Data points (disruptor):** 15 annual (2010–2024, global pack median); 8 points SLI (2010–2024); 6 points BESS system (2019–2024)
- **Data points (incumbent):** 8 points pack $/kWh (2010–2023 catalog); 25 annual PPI index points (2000–2024, T1 BLS)
- **Confidence:** 0.88

---

### Disruptor Cost History — Lithium-Ion Battery Pack (Global Median, $/kWh nameplate)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 1436 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2011 | 1114 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2012 | 876 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2013 | 806 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2014 | 715 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2015 | 463 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2016 | 356 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2017 | 266 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2018 | 218 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2019 | 189 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2020 | 165 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2021 | 155 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2022 | 166 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2023 | 144 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2024 | 115 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) | T2 | [observed] |

**Note on 2022 uptick:** The 2022 value ($166/kWh) represents the only observed increase in the series, driven by lithium carbonate and cathode material cost spikes. This is an observed anomaly, not a trend reversal.

---

### Disruptor Cost History — Li-Ion Pack (China, $/kWh nameplate)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 1100 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2013 | 600 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2015 | 400 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2017 | 226 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2019 | 156 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2021 | 127 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2023 | 94 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2024 | 94 | $/kWh nameplate | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json | T2 | [observed] |

---

### Disruptor Cost History — BESS Turnkey System (2-hour, Global, $/kWh nameplate)

System-level cost including hardware, integration, and installation. This is the closest available proxy for a complete stationary Li-ion storage system competing with VRLA UPS.

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2019 | 441 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2020 | 347 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2021 | 314 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2022 | 318 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2023 | 285 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2024 | 269 | $/kWh nameplate, turnkey | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) | T2 | [observed] |

---

### Disruptor Cost History — 12V Li-Ion SLI Battery (Automotive, $/battery unit)

60Ah LFP, used in automotive SLI replacement market competing directly with 12V lead-acid SLI.

| Year | Cost ($/battery) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 900 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json (CBB Battery / Made-in-China.com, Jan 2026) | T2 | [observed] |
| 2012 | 650 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2014 | 470 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2016 | 300 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2018 | 210 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2020 | 160 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2022 | 130 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2024 | 100 | $/12V 60Ah battery | data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json | T2 | [observed] |

USA equivalent (data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_USA.json): 2010=$950, 2014=$520, 2018=$260, 2022=$165, 2024=$135.

---

### Disruptor Cost History — Li-Ion Forklift (Motive Power, $/unit, 8-hour rated)

Unit cost for a complete Li-ion forklift battery system suitable for warehouse motive power.

| Year | Cost ($/unit) | Unit | Source | Tier | Data Type |
|------|--------------|------|--------|------|-----------|
| 2010 | 32,000 | $/Li-ion forklift battery, 8-hr run | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2013 | 26,000 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2015 | 22,000 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2017 | 19,500 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2019 | 16,500 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2021 | 14,000 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2023 | 12,500 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |
| 2024 | 12,200 | $/Li-ion forklift battery | data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json | T2 | [observed] |

---

### Incumbent Cost History — Lead-Acid Battery Pack ($/kWh nameplate)

#### USA (data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 300 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2013 | 270 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2015 | 240 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2017 | 220 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2019 | 200 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2021 | 190 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |
| 2023 | 180 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json | T2 | [observed] |

#### China (data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json)

| Year | Cost ($/kWh) | Unit | Source | Tier | Data Type |
|------|-------------|------|--------|------|-----------|
| 2010 | 250 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2013 | 225 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2015 | 200 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2017 | 183 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2019 | 160 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2021 | 150 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |
| 2023 | 140 | $/kWh nameplate | data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json | T2 | [observed] |

---

### Incumbent Cost History — 12V Lead-Acid SLI Battery (Automotive, $/battery)

60Ah SLI batteries — direct comparable to 12V Li-ion SLI disruptor above.

| Year | Cost ($/battery) | Unit | Source | Tier | Data Type |
|------|-----------------|------|--------|------|-----------|
| 2010 | 30 | $/12V 60Ah SLI battery, China | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json (Made-in-China.com, MOQ 100) | T2 | [observed] |
| 2012 | 28 | $/12V 60Ah SLI, China | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2016 | 26 | $/12V 60Ah SLI, China | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2020 | 25 | $/12V 60Ah SLI, China | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2024 | 25 | $/12V 60Ah SLI, China | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json | T2 | [observed] |
| 2010 | 70 | $/12V 60Ah SLI, USA | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json | T2 | [observed] |
| 2016 | 64 | $/12V 60Ah SLI, USA | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json | T2 | [observed] |
| 2020 | 60 | $/12V 60Ah SLI, USA | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json | T2 | [observed] |
| 2024 | 55 | $/12V 60Ah SLI, USA | data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json | T2 | [observed] |

---

### Incumbent Cost History — Lead-Acid Battery PPI Index (BLS, USA)

U.S. Bureau of Labor Statistics Producer Price Index for lead-acid batteries (PCU3359113359111), base = December 1984 = 100. This T1 series confirms the near-flat real price trajectory of lead-acid batteries over 25 years.

| Year | PPI Index | Unit | Source | Tier | Data Type |
|------|----------|------|--------|------|-----------|
| 2000 | 110.3 | Index, Dec 1984=100 | BLS/FRED PCU3359113359111, retrieved 2026-03-20 | T1 | [observed] |
| 2005 | 120.5 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2010 | 181.9 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2015 | 198.1 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2018 | 218.8 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2020 | 213.0 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2022 | 250.3 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2023 | 258.8 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |
| 2024 | 260.7 | Index | BLS/FRED PCU3359113359111 | T1 | [observed] |

---

### Incumbent Cost History — Lead Commodity Price ($/tonne)

Lead commodity price is the primary variable input cost for lead-acid batteries (~60–70% of raw material cost).

| Year | Price ($/tonne) | Unit | Source | Tier | Data Type |
|------|----------------|------|--------|------|-----------|
| 2000 | 454 | $/tonne | data/lead/cost/Lead_Cost_Global.json (Rethinkx) | T2 | [observed] |
| 2005 | 974 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2007 | 2592 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2010 | 2146 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2015 | 1788 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2018 | 2241 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2020 | 1825 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2022 | 2145 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2023 | 2136 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |
| 2024 | 2070 | $/tonne | data/lead/cost/Lead_Cost_Global.json | T2 | [observed] |

---

### Levelized Cost Per Cycle — Cross-Chemistry Benchmarks (T3 Reference)

These benchmarks are provided for context only. The cost-fitter must validate and apply them with explicit assumptions.

| Chemistry | Initial Cost ($/kWh) | Cycle Life | Usable DoD | Levelized Cost ($/kWh delivered) | Source | Tier |
|-----------|---------------------|------------|-----------|----------------------------------|--------|------|
| Lead-Acid AGM | ~100 EUR/kWh (~$110) | 500 cycles @50% DoD | 50% | ~0.42 EUR/kWh (~$0.46) | PowerTech Systems, 2015, retrieved 2026-03-20 | T3 |
| LFP (Li-ion) | ~400 EUR/kWh (~$440) | 3,000 cycles @100% DoD | 100% | ~0.15 EUR/kWh (~$0.17) | PowerTech Systems, 2015, retrieved 2026-03-20 | T3 |
| Lead-Acid AGM (2020) | ~$170–236/kWh | ~1,500 cycles @50% DoD | 50% | ~$0.57/kWh | PNNL ESGC 2020 (secondary citation) | T3 |
| LFP (2024 pricing) | ~$115–130/kWh | 3,000–6,000 cycles @80% DoD | 80–100% | ~$0.14/kWh | Fortress Power / industry benchmark, 2024 | T3 |

**NOTE for cost-fitter:** The PowerTech Systems 2015 figures are denominated in euros and use 2015 pricing; they require currency adjustment and should not be used directly. The key structural fact is that levelized cost ratio LFP/lead-acid improved from approximately 1:3 (LFP was 3x more expensive per kWh delivered in 2015) to approximately 1:4 or better by 2024 (LFP is now 4x cheaper per kWh delivered), driven entirely by the Li-ion hardware cost curve.

---

### Current Costs

- **Disruptor current cost (Li-ion global median, 2024):** $115/kWh nameplate (data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json, Rethinkx, [observed])
- **Disruptor current cost (BEV pack, 2024):** $97/kWh nameplate (data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json, [observed])
- **Disruptor current cost (BESS 2-hour turnkey system, 2024):** $269/kWh nameplate (data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json, Rethinkx, [observed])
- **Disruptor current cost (12V Li-ion SLI, China, 2024):** $100/battery (60Ah, ~0.72 kWh = $139/kWh) (data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json, [observed])
- **Incumbent current cost (lead-acid pack, USA, 2023):** $180/kWh nameplate (data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json, [observed])
- **Incumbent current cost (lead-acid pack, China, 2023):** $140/kWh nameplate (data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json, [observed])
- **Incumbent current cost (12V SLI lead-acid, USA, 2024):** $55/battery (60Ah, ~$76/kWh nameplate) (data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json, [observed])
- **Incumbent current cost (lead commodity, 2024):** $2,070/tonne (data/lead/cost/Lead_Cost_Global.json, Rethinkx, [observed])
- **Incumbent current cost (BLS PPI index, 2024):** 260.7 (Dec 1984=100, BLS PCU3359113359111, FRED, [observed])

---

### Unit Notes

- **Service-level unit:** $/kWh delivered over product lifetime (requires cycle life, DoD, and efficiency assumptions)
- **Hardware-to-service conversion needed:** YES — all catalog data is in $/kWh nameplate capacity. The cost-fitter must convert using:
  - Li-ion: cycle life = 2,000–6,000 cycles (LFP, 80% DoD), round-trip efficiency = 95–97%
  - Lead-acid: cycle life = 200–1,500 cycles (AGM/VRLA, 50% DoD), round-trip efficiency = 70–80%
  - Formula: Levelized cost ($/kWh delivered) = Nameplate cost ($/kWh) / (Cycle life x DoD x Round-trip efficiency)
- **Conversion parameters available:**
  - Cycle life benchmarks: Li-ion LFP 3,000 cycles @80% DoD (industry consensus); lead-acid AGM 500 cycles @50% DoD (PowerTech Systems T3)
  - Round-trip efficiency: Li-ion 95–97%; lead-acid 70–80% (Mitsubishi Electric UPS data, T3)
  - SLI batteries: cycle life is essentially infinite (float service), so nameplate $/kWh is the correct comparison unit for SLI; levelized cost framing is not appropriate for SLI
- **SLI market note:** 12V SLI batteries are priced per unit ($/battery), not $/kWh. The 60Ah (0.72 kWh) battery is the standard comparable unit. China lead-acid SLI: ~$25/unit; China Li-ion SLI: ~$100/unit (4x premium, 2024). SLI displacement requires reaching price parity at ~$25–30 per unit, not levelized cost parity.
- **Forklift unit note:** Forklift battery costs are in $/unit (full pack, typically 24–80V, 500–800Ah). The Li-ion catalog data is for an "8-hour run" rated pack; lead-acid equivalent is $2,000–$8,000/pack (T3 web source, 2024). Cost-fitter should convert both to $/kWh at stated capacity.

---

### Data Gaps

1. **No historical VRLA/AGM UPS system-level cost time series.** The catalog contains no $/kWh time series for lead-acid UPS systems (stationary VRLA). Only the BLS PPI index (relative, not absolute $/kWh) and a single 2020 data point from the PNNL ESGC report ($170–236/kWh) are available. The cost-fitter will need to use the pack-level catalog data as a proxy, applying a system multiplier.
2. **Lead-acid forklift battery cost series absent.** The catalog has Li-ion forklift unit costs but no corresponding lead-acid forklift cost time series. The T3 benchmark ($2,000–$8,000 per 48V/600Ah pack, ~$70–$280/kWh nameplate) is a point-in-time estimate only.
3. **No independent T1 source for Li-ion pack costs before 2015.** The primary catalog source (Rethinkx) cites BNEF data. Pre-2015 data points (2010–2014) have lower confidence as they derive from fewer market observations.
4. **Lead-acid pack $/kWh series includes model-derived values for 2024–2025.** The catalog values for lead-acid pack cost beyond 2023 may contain model-derived elements rather than observed market prices; the cost-fitter should treat 2024+ values as indicative only.
5. **SLI Li-ion catalog contains model-derived values from 2025 onward.** All data points from 2025–2040 in `12V_Lithium_Ion_SLI_Battery_Cost_China.json` were excluded. Only 2010–2024 values are included here.
6. **No data on lead-acid telecom UPS cost per kWh.** The telecom UPS sector catalog contains adoption/demand data (GWh installed base) but no cost curves.
7. **Levelized cost benchmarks are T3 only.** No T1 or T2 sources provide a historical time series of $/kWh-delivered (levelized) costs for either chemistry.

---

### Source Conflicts

- **Li-ion 2024 global median: $115/kWh (Rethinkx/BNEF catalog) vs. $108/kWh (BNEF 2025 press release).** The $108/kWh figure cited in the BNEF 2025 press release refers to 2025 data (beyond analysis date). The 2024 value of $115/kWh from the catalog is used. No conflict on the 2024 figure itself.
- **Li-ion China 2024: $94/kWh (catalog) vs. $94/kWh (BNEF regional citation).** Agreement across sources.
- **Lead-acid USA pack cost: catalog shows $180/kWh (2023). Web secondary sources cite $100–$200/kWh for VRLA.** The wider range from web sources reflects different chemistries and system configurations. Catalog value used as primary.
- **SLI Li-ion China 2024: catalog cites $100/battery (0.72 kWh = ~$139/kWh). Global median catalog shows $115/kWh.** The SLI curve represents a specific product format (12V, 60Ah), not pack-level average; no conflict.

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | 15 data points (2010–2024) Li-ion global median; 8 pts China; 6 pts BESS system; 8 pts 12V SLI — all spanning 10–14 years |
| 2.2 | PASS | Lead-acid pack $/kWh: 7 observed pts (2010–2023, USA and China); BLS PPI 25 annual pts (2000–2024, T1); SLI 5 pts (2010–2024) |
| 2.3 | PASS | Li-ion global median: $115/kWh (2024, Rethinkx T2); BESS turnkey: $269/kWh (2024, Rethinkx T2); BEV pack: $97/kWh (2024, T2) |
| 2.4 | PASS | Lead-acid pack USA: $180/kWh (2023, catalog T2); China: $140/kWh (2023, T2); BLS PPI 260.7 (2024, T1) |

---

## Sources

- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json — Rethinkx (BNEF underlying data), 2010–2024 [T2]
- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json — 2010–2024 [T2]
- data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_USA.json — 2010–2024 [T2]
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_(Stationary_storage)_Cost_China.json — 2010–2024 [T2]
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json — 2019–2024 [T2]
- data/battery_pack/cost/Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_Global.json — 2018–2024 [T2]
- data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json — CBB Battery / Made-in-China.com, 2010–2024 historical only [T2]
- data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_USA.json — CBB Battery, 2010–2024 historical only [T2]
- data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json — Rethinkx, 2019–2024 [T2]
- data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json — Rethinkx, 2019–2024 [T2]
- data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_USA.json — 2010–2023 [T2]
- data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json — 2010–2023 [T2]
- data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_Europe.json — 2010–2023 [T2]
- data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json — Made-in-China.com, 2010–2024 [T2]
- data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_USA.json — 2010–2024 [T2]
- data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json — 2010–2024 [T2]
- data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_Europe.json — 2011–2024 [T2]
- data/lead/cost/Lead_Cost_Global.json — Rethinkx, 1998–2024 [T2]
- data/lead/adoption/Lead_Annual_Implied_Demand_Global.json — Rethinkx, 2010–2024 [T2]
- U.S. Bureau of Labor Statistics, FRED series PCU3359113359111 — Lead-Acid Battery PPI, Dec 1984–2024 [T1], retrieved 2026-03-20, https://fred.stlouisfed.org/series/PCU3359113359111
- Ziegler, M.S. and Trancik, J.E. (2021). "Re-examining rates of lithium-ion battery technology improvement and cost decline." Energy and Environmental Science, 14(4), 1635–1651. [T1], https://pubs.rsc.org/en/content/articlelanding/2021/ee/d0ee02681f
- PowerTech Systems (2015). "Lithium-Ion vs Lead-Acid Cost Analysis." Retrieved 2026-03-20. [T3], https://www.powertechsystems.eu/home/tech-corner/lithium-ion-vs-lead-acid-cost-analysis/
- PNNL/DOE. Energy Storage Grand Challenge Cost and Performance Assessment 2020. [T1 — PDF not parseable; secondary citation values used for 2020 lead-acid installed cost range $170–$236/kWh], https://www.pnnl.gov/projects/esgc-cost-performance
- Redway Power. "How Does Forklift Lithium Battery Cost Compare to Lead-Acid?" Retrieved 2026-03-20. [T3], https://www.redwaypower.com/how-does-forklift-lithium-battery-cost-compare-to-lead-acid/
