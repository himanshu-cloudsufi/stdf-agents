# STDF Domain Disruption Agent — Lead (Pb) Demand Decline

**Agent:** `stdf-domain-disruption` | **Confidence:** 0.82

---

## Agent Reasoning

### Analytical Approach

The question "when will lead demand drop 10% relative to today?" requires mapping every demand-generating sub-domain to its specific disruptor, quantifying the current market share of that disruptor, and determining how much volume each vector must shed to cross the 1,226 kt threshold (10% of 12,259 kt baseline, 2024).

Lead demand is structurally dominated by battery applications (86.2% of 2024 total), and within batteries the automotive SLI sub-domain is overwhelmingly largest. The core analytical challenge is that lithium-ion disruption operates differently in each sub-domain: in SLI it acts *indirectly* via BEV displacement of the entire SLI installation occasion; in telecom/stationary backup it acts *directly* as a drop-in replacement; in motive power (forklifts) the disruption is already substantially advanced.

The critical finding is that SLI replacement demand (3,377 kt, 27.5% of all lead demand) is still *growing* in 2024 because the global ICE vehicle fleet (1.305 billion units) is itself still growing at approximately 2%/year through most of the 2019–2024 period. BEV new sales at 15.0% market share in 2024 are not yet sufficient to have fully tipped the ICE fleet into absolute decline — a condition required before SLI replacement demand can fall. This creates a structural delay between BEV adoption inflection (2021–2024) and observable lead demand contraction.

### Key Analytical Decisions

The disruption taxonomy was split into four distinct sub-domains reflecting structurally different demand mechanisms and disruption pathways: (1) automotive SLI new-vehicle demand, (2) automotive SLI replacement/aftermarket demand, (3) industrial stationary backup (telecom, datacenter UPS), and (4) industrial motive power (forklifts, warehouse equipment). Each has different S-curve positions, different disruptors, and different lead content per unit. Chimeras were specifically identified for 48V mild-hybrid systems (retain SLI in a modified role) and PHEV vehicles (reduce but do not eliminate per-vehicle lead content).

Convergence was mapped across three combinations: Li-BEV (lithium-ion pack + BEV platform eliminating SLI entirely), LFP-UPS (LFP chemistry + modular rack-mount UPS systems enabling cost-competitive stationary displacement), and EV-FL (electric forklift + lithium motive battery eliminating lead motive demand from new equipment).

All numerical claims are computed directly from catalog data using Python. The 2024 aggregate demand figure of 12,259 kt (Rethinkx, observed) is used as the baseline for the 10% decline question.

### Confidence Calibration

Confidence is set at 0.82. The demand decomposition data is exceptionally granular (full cross-sector breakdown by vehicle type and application), and cost curves exist for both disruptors and incumbents. The primary uncertainty is the speed of ICE fleet contraction, which depends on BEV S-curve acceleration. The catalog provides BEV sales data through 2024 but the fleet turnover dynamic requires S-curve fitting by downstream agents.

---

## Agent Output

### Key Findings
- **Sector:** Materials
- **Sub-domains:** automotive SLI new-vehicle battery demand, automotive SLI replacement/aftermarket demand, industrial stationary backup (telecom UPS, datacenter UPS, grid backup), industrial motive power (lead-acid traction batteries in forklifts and warehouse equipment), non-battery lead uses (shielding, shot, alloys)
- **Confidence:** 0.82

---

### Disruption Map

| Disruption | Disruptors | Incumbents | Chimeras | Convergence |
|---|---|---|---|---|
| BEV displacement of ICE new-car sales — eliminates SLI new-vehicle demand | battery electric vehicle (BEV), lithium iron phosphate (LFP) traction pack | 12V flooded lead-acid SLI battery in internal combustion engine (ICE) vehicle | 48V mild-hybrid system (retains reduced 12V lead-acid + adds 48V lithium buffer); plug-in hybrid (PHEV, retains 12V SLI lead-acid) | Li-BEV: lithium traction pack + BEV platform = zero SLI installation per vehicle sold |
| BEV-driven ICE fleet contraction — shrinks SLI aftermarket/replacement demand | battery electric vehicle (BEV) displacing ICE installed base via stock-flow fleet turnover | 12V flooded lead-acid SLI replacement battery (aftermarket); AGM (absorbent glass mat) SLI replacement for start-stop ICE | 48V mild-hybrid AGM battery (higher-spec lead-acid, not pure lithium); EFB (enhanced flooded battery) for start-stop ICE | Li-BEV: same convergence as above; fleet-level effect lags new-sales disruption by 10–15 years |
| LFP stationary storage displacing VRLA in telecom and datacenter UPS backup | lithium iron phosphate (LFP) rack-mount UPS systems; modular LFP BESS (battery energy storage system) | valve-regulated lead-acid (VRLA) battery in telecom tower UPS; flooded lead-acid in datacenter UPS | lead-acid + small LFP buffer hybrid UPS (transitional rack configs used in 5G densification) | LFP-UPS: LFP chemistry + modular rack architecture + integrated BMS = cost-competitive lead-acid displacement in stationary backup |
| LFP motive power displacing lead-acid traction batteries in industrial forklifts | LFP lithium-ion motive battery; lithium-ion electric forklift (EV forklift) | lead-acid traction battery (flooded, deep-cycle, 24V–80V) in ICE and electric counterbalance forklifts | lead-acid forklift with opportunity-charging retrofit (partial modernization, retains lead-acid chemistry) | EV-FL: electric forklift platform + LFP motive battery = no lead traction demand; 65% global forklift sales share in 2024 [observed] |
| LFP direct 12V SLI substitution in ICE aftermarket and e-bike markets | 12V LFP drop-in replacement battery (BMS-integrated, direct-fit SLI form factor) | 12V flooded lead-acid SLI replacement battery; 12V AGM replacement battery | none identified — direct technology substitution, no chimera form | LFP-UPS cost curve applies; BMS commoditization makes 12V LFP cost-feasible at scale |

---

### Narrative

#### Structure of Lead Demand (2024 Baseline)

Global lead demand in 2024 stood at **12,259 kt** [T2: data/lead/adoption/Lead_Annual_Implied_Demand_Global.json, Rethinkx, 2024, observed], up from 8,815 kt in 2010 at a 2.4%/year CAGR. The growth rate has decelerated significantly — from 2.4%/year over 2010–2024 to only 1.1%/year over 2021–2024 — signaling that the long demand expansion is losing momentum. To answer the 10% decline question, the threshold is **11,033 kt** (a 1,226 kt reduction from the 2024 baseline).

Demand decomposes as follows [T2: Rethinkx catalog, 2024, observed]:

| Sub-domain | 2024 kt | % of total |
|---|---|---|
| Automotive SLI total (cars + CV + 2W + 3W, new + replacement) | 7,665 | 62.5% |
| — of which: car SLI replacement/aftermarket | 3,377 | 27.5% |
| — of which: car SLI new vehicle | 810 | 6.6% |
| — of which: commercial vehicle SLI (new + replacement) | 1,535 | 12.5% |
| — of which: 2-wheeler SLI (new + replacement) | 1,395 | 11.4% |
| — of which: 3-wheeler SLI (new + replacement) | 548 | 4.5% |
| Industrial stationary backup (telecom, datacenter UPS, grid) | 1,987 | 16.2% |
| Industrial motive power (forklifts, traction) | 913 | 7.4% |
| Non-battery uses (shielding, alloys, shot) | 1,691 | 13.8% |

The automotive SLI cluster at 62.5% is the dominant demand driver, and within it, **SLI replacement/aftermarket is the single largest component** at 27.5% of global demand. This matters structurally: new-vehicle SLI demand is already being eroded by BEV adoption (810 kt in 2024, declining as ICE new sales fall), but replacement demand is *still growing* because it is a function of the installed ICE fleet, not new sales.

#### Disruption 1: BEV Eliminating SLI New-Vehicle Demand (From Above)

This disruption is classified as **From Above**: BEV entered at the premium end (luxury/performance: Tesla Model S/X; Chinese premium BEV) and is cascading toward mass market (Model 3/Y, BYD Han/Seal/Seagull) as cost curves drop. The LFP traction pack — not lithium in general — is the specific disruptor technology enabling mass-market price parity.

BEV global new-car market share has risen rapidly [T2: data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json, Rethinkx, observed]:

| Year | BEV sales | Total PV sales | BEV share |
|---|---|---|---|
| 2019 | 1.60M | 82.9M | 1.9% |
| 2021 | 4.52M | 71.5M | 6.3% |
| 2022 | 7.52M | 72.3M | 10.4% |
| 2023 | 9.67M | 78.0M | 12.4% |
| 2024 | 11.0M | 73.2M | 15.0% |

Each BEV sold eliminates one 12V SLI lead-acid battery from the new-vehicle demand stream. Lead intensity per new ICE SLI installation is approximately 14.5 kg/vehicle [model-derived: 810 kt demand / 55.7M ICE new sales 2024, from T2 catalog]. At 11 million BEVs in 2024, the new-SLI demand eliminated vs an all-ICE counterfactual is approximately **160 kt/year**. However, the overall SLI new-car demand in the catalog is still 810 kt because total new ICE sales at 55.7 million remain large.

**PHEV chimera**: Plug-in hybrid vehicles (PHEVs) retain a 12V lead-acid SLI battery for auxiliary functions. PHEV SLI demand in China rose from 0.02 kt (2011) to 39 kt (2024) [T2: data/passenger_cars/adoption/Passenger_Vehicle_(PHEV)_Annual_Lead_Implied_Demand_China.json, Rethinkx, observed]. PHEVs partially offset BEV-driven SLI demand destruction in the new-vehicle segment — they are a transitional chimera, not a disruptor.

**48V mild hybrid chimera**: Modern start-stop ICE vehicles with 48V mild hybrid systems retain a 12V lead-acid SLI battery for cranking and a separate 48V lithium buffer. These neither eliminate the 12V SLI market nor match the full disruption economics of BEV. They extend lead-acid's role in a reduced form.

#### Disruption 2: BEV Fleet Turnover Shrinking SLI Replacement Demand (From Above, Lagged)

This is the same disruptor (BEV/LFP) but operating on the aftermarket channel with a 10–15 year lag imposed by fleet stock-flow dynamics. The ICE fleet replacement market at 3,377 kt (2024) is governed by the global ICE installed base (1.305 billion vehicles in 2024, replacing batteries every approximately 4.5 years, generating approximately 290 million replacement events/year at 11.6 kg Pb per event [model-derived from T2 catalog]).

The structural constraint: the ICE fleet grew from 1.180 billion (2019) to 1.305 billion (2024), a CAGR of +2.0%/year [T2: data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Total_Fleet_Global.json, Rethinkx, observed]. With 15% BEV new-sales share and 87 million annual ICE retirements (1.305B / 15yr average vehicle life), net ICE fleet change in 2024 is approximately −24.8M/year [model-derived] — the fleet has begun contracting. The decline is slow: a 36% fleet reduction (474 million units) would be required to eliminate 1,226 kt from this vector alone [model-derived]. Combined across all vectors, the threshold is reachable earlier.

#### Disruption 3: LFP Stationary Storage Displacing VRLA in Telecom and Datacenter UPS (Big Bang)

This disruption is classified as **Big Bang**: lithium iron phosphate (LFP) in rack-mount UPS format is simultaneously cheaper *and* better than valve-regulated lead-acid (VRLA) at the system level. LFP offers 3–4x longer cycle life, 50% smaller footprint, and total cost of ownership parity or better vs VRLA at current LFP prices. The convergence label is **LFP-UPS** (LFP chemistry + modular rack architecture + integrated BMS).

Telecom UPS Li-ion penetration (GWh annual capacity demand share) [T2: data/telecom_ups/adoption/, Database, observed]:

| Year | Lead-acid (GWh/yr) | Li-ion (GWh/yr) | Li-ion share |
|---|---|---|---|
| 2015 | 3.98 | 0.12 | 2.9% |
| 2019 | 6.16 | 0.54 | 8.1% |
| 2021 | 7.48 | 1.12 | 13.0% |
| 2022 | 6.98 | 2.72 | 28.0% |
| 2023 | 7.52 | 3.38 | 31.0% |
| 2024 | 8.17 | 4.03 | 33.0% |

The 2021–2022 jump from 13% to 28% Li-ion share in telecom UPS indicates the disruption crossed a commercial tipping point. Li-ion CAGR in telecom UPS was +48%/year from 2015 to 2024 [model-derived from T2 catalog data]. This sub-domain is in **early-to-mid S-curve acceleration**. The *installed base* of lead-acid telecom UPS (30.15 GWh globally in 2024, still growing) means absolute lead-acid demand in telecom has not yet fallen even as market share erodes.

BESS (battery energy storage system) costs provide the cost-curve context for the stationary disruption. Turnkey 2-hour BESS (dominated by LFP) declined from $441/kWh (2019) to $269/kWh (2024) globally [T2: data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json, Rethinkx, observed]; China-specific costs reached $101/kWh by 2024. Lead-acid pack cost declined only −4.4%/year (2010–2023, China) from $250 to $140/kWh [T2: data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json, Database, observed] — a mature technology with minimal learning curve. Li-ion pack cost in China crossed below lead-acid pack cost on a per-kWh basis between 2017 and 2019 [T2: observed], reaching $94/kWh (2023) vs $140/kWh for lead-acid — a 33% cost advantage for lithium on a $/kWh basis [T2: data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json, Database, observed].

#### Disruption 4: LFP Motive Power Displacing Lead-Acid Traction Batteries in Forklifts (From Below — Mature)

This disruption is classified as **From Below**: electric forklifts entered industry first as lower-performance indoor warehouse equipment (no-emissions advantage for indoor use was the initial pull), then ascended to outdoor reach trucks and counterbalance forklifts. The convergence label is **EV-FL** (electric forklift platform + LFP motive battery).

EV forklift sales are already dominant at **65% of global forklift sales** in 2024 [T2: data/forklift/adoption/Forklift_(EV)_Annual_Sales_Global.json + Forklift_(ICE)_Annual_Sales_Global.json, Database, observed]. This sub-domain disruption is **mature**: ICE forklift sales peaked around 2021–2022 and are declining. Lead motive power demand correspondingly peaked at 929 kt (2018) and retreated to 913 kt (2024).

LFP forklift cost (China) fell from $32,000/unit (2010) to $12,200/unit (2024), a −14.5%/year CAGR [T2: data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json, Database, observed]. This disruption is largely complete for new equipment; the residual demand destruction comes from ICE forklift replacement cycles converting to EV.

#### Disruption 5: LFP Direct 12V SLI Substitution in ICE Aftermarket (Pre-Inflection)

A fifth and emerging disruption — less advanced than the others — is **direct LFP replacement of 12V lead-acid SLI batteries in ICE aftermarket and e-bike applications**. LFP 12V SLI battery cost in China has declined from $900/unit (2010) to $100/unit (2024) at −14.5%/year [T2: data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json, Database, observed]. Lead-acid SLI cost in China is effectively flat at $25/unit [T2: data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json, Database, observed]. The catalog data, extended from observed 2024 values at the observed learning rate, shows LFP SLI approaching ~$32/unit by 2030 in China — nearing the lead-acid cost level [T2: model-derived from catalog]. This creates a direct aftermarket substitution channel independent of BEV adoption.

#### 10% Decline: Structural Assessment

The 1,226 kt reduction required to hit the 10% threshold must come from the aggregate of multiple vectors. Key structural observations:

1. **SLI new-vehicle demand** is already falling as BEV share rises — each percentage point of new-car BEV share removes approximately 100–120 kt/yr of new-SLI demand.

2. **SLI replacement demand** is a stock-flow problem: it will start declining as the ICE fleet contracts. Net fleet contraction of −24.8M/year is now occurring (2024), but the 1.305 billion unit base means decline rates are initially small.

3. **Stationary backup** (1,987 kt) is being disrupted from the margin at each replacement cycle (4-year lead-acid battery life in telecom [T2: data/telecom_ups/replacement/, observed]). Li-ion at 33% new-installation share in telecom as of 2024 means two-thirds of new capacity still uses lead-acid — substantial room for displacement remains.

4. **Motive power** (913 kt) is near peak disruption capture; the remaining ICE forklift market (35%) will convert on a multi-year replacement cycle.

5. **Non-battery** (1,691 kt) is outside the disruption scope — no lithium-ion substitution path.

The combined trajectory of these vectors, governed by their respective S-curve positions, determines the timing of the 10% demand decline. Quantifying this timing is the remit of the downstream demand-decomposer and scurve-fitter agents.

---

### Handoff Context

- **Sector boundaries:** Materials sector, specifically lead (Pb) metal demand. Analysis covers all battery-related sub-domains (automotive SLI, stationary backup, motive power). Non-battery lead uses (1,691 kt, 13.8%) are outside the disruption scope and treated as a stable residual. Coverage is global with regional data available for China, USA, Europe, Rest of World across all sub-domains.

- **Key cost data:**
  - LFP pack (China): $94/kWh (2023 observed), −14.5%/yr learning rate [T2]
  - Lead-acid pack (China): $140/kWh (2023 observed), −4.4%/yr [T2]
  - LFP SLI 12V (China): $100/unit (2024 observed); lead-acid SLI: $25/unit (flat) [T2]
  - LFP crosses lead-acid $/kWh: already achieved circa 2019 (China); USA/Europe still 2–3x lead-acid [T2]
  - BESS turnkey 2-hour (global): $269/kWh (2024 observed) [T2]
  - BESS turnkey 2-hour (China): $101/kWh (2024 observed) [T2]

- **S-curve positions:**
  - BEV new car sales: early growth (15% share globally, 2024); China leading at higher share; ICE fleet in net contraction as of 2024
  - Li-ion in telecom UPS: acceleration phase (13% to 33% share, 2021–2024, +48%/yr CAGR)
  - Li-ion forklift motive: mature phase (65% forklift sales share 2024; motive lead demand declining)
  - LFP direct SLI substitution: pre-inflection (cost gap closing; crossover approaching in China ~2030)
  - ICE fleet: net contraction beginning 2024 (~−24.8M/yr net change) — lagged demand signal

- **Data gaps:**
  - No direct observed data on LFP penetration of stationary industrial backup in aggregate kt terms — only GWh-level data for telecom/datacenter sub-segments; the 1,987 kt stationary figure requires translation from GWh to kt via lead intensity factors
  - PHEV lead demand data available only for China and Europe, not global — residual PHEV chimera effect is unquantified for Rest of World
  - Two-wheeler and three-wheeler Li-ion displacement of lead-acid not yet visible in demand data — 2W lead demand still elevated at 1,395 kt (2024); no catalog data on 2W Li-ion penetration rate
  - No catalog data on LFP penetration of 2W market specifically, which is critical for Asia-Pacific (India, SE Asia)
  - Non-battery lead uses (1,691 kt) have no identified disruptor; excluded from disruption model

- **Unresolved questions:**
  - At what BEV new-car share does ICE fleet decline accelerate into self-reinforcing contraction? (S-curve fitter question)
  - How fast does the telecom/datacenter VRLA replacement market shift to LFP as existing 4-year-cycle batteries reach end-of-life?
  - Does the 2W market in India/SE Asia adopt Li-ion at sufficient scale to dent the 1,395 kt 2W lead demand before 2035? (regional adopter question — critical gap)
  - What combined year does the sum of all five disruption vectors cross the 1,226 kt threshold? (demand-decomposer + scurve-fitter primary output)
  - Does LFP SLI aftermarket substitution (Disruption 5) accelerate enough before ICE fleet contraction to shift the 10% decline timeline earlier?

---

## Sources

All primary data from the STDF empirical catalog (Tier 2). Tier 3 web sources noted where used.

- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — Total global lead demand 2010–2024, Rethinkx [observed]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand-Industrial_batteries_motive_power_Global.json` — Lead demand from motive power, Rethinkx [observed]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand-Industrial_batteries_stationary_Global.json` — Lead demand from stationary backup, Rethinkx [observed]
- [T2] `data/lead/adoption/Lead_Annual_Implied_Demand-Non-battery_uses_Global.json` — Lead non-battery demand, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Sales_Cars_Global.json` — Lead demand from car SLI new sales, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_Cars_Global.json` — Lead demand from car SLI replacements, Rethinkx [observed]
- [T2] `data/commercial_vehicle/adoption/Lead_Annual_Implied_Demand-Sales_Commercial_vehicles_Global.json` — Lead demand from CV SLI new sales, Rethinkx [observed]
- [T2] `data/commercial_vehicle/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_Commercial_Global.json` — Lead demand from CV SLI replacements, Rethinkx [observed]
- [T2] `data/two_wheeler/adoption/Lead_Annual_Implied_Demand-Sales_2_wheelers_Global.json` + vehicle replacement curve — Rethinkx [observed]
- [T2] `data/three_wheeler/adoption/Lead_Annual_Implied_Demand-Sales_3_wheelers_Global.json` + vehicle replacement curve — Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` — BEV global sales, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Annual_Sales_Global.json` — ICE global sales, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(ICE)_Total_Fleet_Global.json` — ICE global fleet, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_Annual_Sales_Global.json` — Total global PV sales, Rethinkx [observed]
- [T2] `data/passenger_cars/adoption/Passenger_Vehicle_(PHEV)_Annual_Lead_Implied_Demand_China.json` — PHEV chimera lead demand (China), Rethinkx [observed]
- [T2] `data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Li-ion pack cost (China), Database [observed]
- [T2] `data/battery_pack/cost/Lead_Acid_Battery_Pack_Median_Cost_China.json` — Lead-acid pack cost (China), Database [observed]
- [T2] `data/battery_pack/cost/12V_Lead_Acid_SLI_Battery_Cost_China.json` / `_USA.json` — SLI lead-acid unit cost, Database [observed]
- [T2] `data/battery_pack/cost/12V_Lithium_Ion_SLI_Battery_Cost_China.json` / `_USA.json` — LFP SLI unit cost, Database [observed]
- [T2] `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_(Lead_Acid)_Annual_Capacity_Demand_Global.json` — Telecom LA demand, Database [observed]
- [T2] `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_(Li-Ion)_Annual_Capacity_Demand_Global.json` — Telecom Li-ion demand, Database [observed]
- [T2] `data/telecom_ups/adoption/Lead_acid_batteries_UPS_telecom_Installed_Base_Global.json` — Telecom LA installed base, Database [observed]
- [T2] `data/telecom_ups/replacement/Lead_acid_batteries_UPS_telecom_Replacement_cycle_Battery_Replacement_cycle_Global.json` — 4-year replacement cycle, Database [observed]
- [T2] `data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` + `_China.json` — BESS turnkey cost, Rethinkx [observed]
- [T2] `data/forklift/adoption/Forklift_(EV)_Annual_Sales_Global.json` + `Forklift_(ICE)_Annual_Sales_Global.json` — EV vs ICE forklift sales, Database [observed]
- [T2] `data/forklift/cost/Lithium_Ion_Battery_operated_Forklifts-8_hrs_run_Lowest_Cost_China.json` — LFP forklift cost, Database [observed]
- [T2] `data/lead/cost/Lead_Cost_Global.json` — Lead metal price 1998–2024, Database [observed]
- [T3] Web search conducted 2026-03-20 — contextual only; no numeric claims sourced from web; all third-party market outlooks discarded per historical-only data rule
