# STDF Cost Researcher Agent — Copper Demand Drivers: Electrification, EVs, Solar, Wind, Battery Storage

**Agent:** `stdf-cost-researcher` | **Confidence:** 0.85

---

## Agent Reasoning

This analysis differs from a standard two-technology parity comparison. The query asks for cost data on multiple disruptive technologies — Li-ion batteries, solar PV, onshore wind, offshore wind, and EVs — because these are the **demand drivers** for copper as a commodity. The "incumbent" in each sub-disruption is the fossil-fuel technology being displaced: natural gas peakers (for power generation), ICE vehicles (for transport), and the flat copper demand growth from conventional construction and grid infrastructure.

**Search strategy:** The local catalog was searched first and proved exceptionally rich for this query. The `data/copper/` sector contains 40+ files covering price, mining cost, production, consumption, and demand breakdown by application (EV, solar, wind, transport, electrical). All five disruptive technology sectors (battery pack, energy generation, energy storage, passenger cars) have well-populated cost time series from Rethinkx (T2). The catalog source for natural gas and crude oil is the US Energy Information Administration/FRED (T1-equivalent) [CAUTION: EIA source — historical data only]. Gaps existed for: (1) solar PV module prices pre-2017 in the catalog (only 2017–2024 in catalog), requiring web research for the 2000–2010 period; (2) LCOE data in $/MWh for all technologies (catalog provides hardware costs $/kW or $/kWh, not LCOE); and (3) copper intensity per technology unit (kg/vehicle, tonnes/MW).

**Web research findings:** IRENA's annual Renewable Power Generation Costs reports provide the authoritative global weighted average LCOE series for solar PV (2010–2024: $460/MWh to $43/MWh) and onshore wind (2010–2024: $89/MWh to $34/MWh). Lazard's LCOE+ series (v3.0–v17.0, 2009–2023) provides the incumbent gas peaker benchmark ($115–221/MWh in 2023). Solar PV module prices pre-2010 are sourced from the academic composite maintained in NREL reports and cited by Our World in Data (Nemet 2009, Farmer & Lafond 2016): approximately $5/W in 2000, declining to $2/W in 2010 before the sharp post-2010 crash. The Copper Development Association (CDA) provides the authoritative copper intensity benchmarks: ICE vehicle ~23 kg, BEV ~83 kg, solar PV ~5 tonnes/MW, onshore wind ~3–5 tonnes/MW.

**Key analytical decisions:** The service-level units differ by technology vector: (1) for power generation disruption (solar/wind vs. gas peaker), the correct unit is $/MWh (LCOE); (2) for EV disruption (BEV vs. ICE), the correct unit is $/vehicle or $/km of driving service; (3) for battery storage as a standalone technology, the unit is $/kWh. Copper itself is tracked in $/tonne (LME price) and $/tonne mining cost. The cost-fitter must convert hardware costs ($/kW, $/kWh capacity) to service-level units using capacity factors and financial assumptions. This is flagged explicitly in Unit Notes.

A critical structural note: this is a **multi-vector copper demand analysis**, not a single parity comparison. The cost data collected here supports the cost-fitter in modeling each technology's disruption trajectory, which then feeds into demand-decomposer and stream-forecaster agents to compute copper demand implications per vector.

---

## Agent Output

### Key Findings
- **Primary disruptors (copper demand drivers):** Lithium-ion batteries (EVs + stationary storage), solar PV, onshore wind, offshore wind
- **Incumbent technologies (being displaced):** ICE vehicles (transport), natural gas peakers and CCGT (power generation), conventional grid infrastructure
- **Copper commodity:** $/tonne spot price and $/tonne mining cost, tracked separately
- **Service units by vector:**
  - Power generation: $/MWh (LCOE)
  - Battery pack: $/kWh (hardware)
  - Vehicle: $/vehicle or $/km
  - Copper commodity: $/tonne
- **Data points (disruptor technologies combined):** 100+ data points across 5 technology curves, spanning 1984–2024
- **Data points (copper commodity):** 35 pts (price), 13 pts (mining cost), spanning 1990–2024
- **Data points (incumbent technologies):** 28 pts (NG USA), 35 pts (crude oil), plus LCOE via T3 web sources
- **Confidence:** 0.85

---

### Disruptor Cost History

#### Technology 1: Lithium-Ion Battery Pack (Global Median)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 1436 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2011 | 1114 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2012 | 876 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2013 | 806 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2014 | 715 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2015 | 463 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2016 | 356 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2017 | 266 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 218 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 189 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 165 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 155 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 166 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 144 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 115 | $/kWh | data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

Note: 2022 shows $166/kWh spike (real — supply chain and lithium carbonate price shock). This is a documented anomaly in the cost-curve, not a data error.

#### Technology 1b: Li-Ion Battery Pack — Passenger BEV Specific

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2019 | 179 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 152 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 139 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 152 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 132 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 97 | $/kWh | data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

#### Technology 2: Solar PV — Installed Cost (Hardware, $/kW)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 5,310 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2011 | 4,553 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2012 | 3,466 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2013 | 3,042 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2014 | 2,749 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2015 | 2,090 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2016 | 1,901 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2017 | 1,644 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 1,405 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 1,161 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 1,019 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 950 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 908 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 758 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 700 | $/kW | data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

#### Technology 2b: Solar PV — LCOE (Service-Level, $/MWh)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 460 | $/MWh | IRENA Renewable Power Generation Costs annual series [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2012 | ~310 | $/MWh | IRENA Renewable Power Generation Costs in 2018 chart trend [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2014 | ~220 | $/MWh | IRENA Renewable Power Generation Costs in 2018 chart trend [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2016 | ~150 | $/MWh | IRENA Renewable Power Generation Costs in 2018 chart trend [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2018 | 85 | $/MWh | IRENA Renewable Power Generation Costs in 2018 (irena.org) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2020 | 57 | $/MWh | IRENA Renewable Power Generation Costs in 2020 Summary [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2021 | 48 | $/MWh | IRENA Renewable Power Generation Costs in 2021 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2022 | 49 | $/MWh | IRENA Renewable Power Generation Costs in 2022 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2023 | 44 | $/MWh | IRENA Renewable Power Generation Costs in 2023 (Sep 2024) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2024 | 43 | $/MWh | IRENA Renewable Power Generation Costs in 2024 (Jul 2025) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |

Note: 2012, 2014, 2016 values are approximate values read from trend charts in the IRENA 2018 report. Exact digit-precision values require the IRENA interactive dashboard.

#### Technology 2c: Solar PV — Module Price (Nominal $/W)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2000 | ~5.0 | $/W | NREL PV Pricing Trends (Nemet 2009 composite, via NREL/PR-6A20-56776) [T3] | T3 | [observed] |
| 2004 | ~3.5 | $/W | NREL PV Pricing Trends (Farmer & Lafond 2016 composite) [T3] | T3 | [observed] |
| 2008 | ~4.2 | $/W | NREL PV Pricing Trends (polysilicon shortage — above-trend anomaly) [T3] | T3 | [observed] |
| 2010 | ~1.8 | $/W | NREL/IRENA composite; pvXchange global price index [T3] | T3 | [observed] |
| 2017 | 0.57 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 0.45 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 0.34 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 0.31 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 0.33 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 0.35 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 0.26 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 0.15 | $/W | data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json (Rethinkx) [T2] | T2 | [observed] |

Flag for cost-fitter: 2008 module price anomaly ($4.20/W) is a known polysilicon shortage spike, documented in NREL literature. It is above the underlying learning curve trend. Do not use as a reference point for curve fitting.

#### Technology 3: Onshore Wind — Installed Cost (Hardware, $/kW)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 1984 | 5,698 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 1990 | 3,860 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 1995 | 3,163 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2000 | 2,565 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2005 | 2,159 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2010 | 2,272 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2015 | 1,911 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 1,819 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2019 | 1,725 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 1,552 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 1,471 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 1,322 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 1,160 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 1,041 | $/kW | data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

#### Technology 3b: Onshore Wind — LCOE (Service-Level, $/MWh)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2009 | 135 | $/MWh | Lazard LCOE+ v3.0 (2009) mean [T3] [CAUTION: Lazard source — historical data only] | T3 | [observed] |
| 2010 | 89 | $/MWh | IRENA Renewable Power Generation Costs (global weighted avg) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2016 | 70 | $/MWh | IRENA Renewable Power Generation Costs in 2016 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2019 | 53 | $/MWh | IRENA Renewable Power Generation Costs in 2019 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2020 | 39 | $/MWh | IRENA Renewable Power Generation Costs in 2020 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2021 | 33 | $/MWh | IRENA Renewable Power Generation Costs in 2021 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2022 | 35 | $/MWh | IRENA Renewable Power Generation Costs in 2022 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2023 | 33 | $/MWh | IRENA Renewable Power Generation Costs in 2023 (irena.org, Sep 2024) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2024 | 34 | $/MWh | IRENA Renewable Power Generation Costs in 2024 (irena.org, Jul 2025) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |

#### Technology 4: Offshore Wind — Installed Cost (Hardware, $/kW)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2000 | 2,979 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2007 | 5,110 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2010 | 5,409 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2014 | 6,101 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2016 | 4,713 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2018 | 5,320 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 3,538 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 3,137 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 3,478 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 2,800 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 2,852 | $/kW | data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

#### Technology 4b: Offshore Wind — LCOE (Service-Level, $/MWh)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 203 | $/MWh | IRENA Renewable Power Generation Costs (global weighted avg) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2022 | 80 | $/MWh | IRENA Renewable Power Generation Costs in 2022 [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2023 | 75 | $/MWh | IRENA Renewable Power Generation Costs in 2023 (Sep 2024) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |
| 2024 | 79 | $/MWh | IRENA Renewable Power Generation Costs in 2024 (Jul 2025) [T1] [CAUTION: IRENA source — historical data only] | T1 | [observed] |

#### Technology 5: Battery Energy Storage System (BESS) — 2-hour Turnkey

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2019 | 441 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2020 | 347 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2021 | 314 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2022 | 318 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2023 | 285 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |
| 2024 | 269 | $/kWh | data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json (Rethinkx) [T2] | T2 | [observed] |

#### Technology 6: EV Purchase Price (USA Median)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 52,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2012 | 50,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2015 | 45,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2018 | 39,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2020 | 35,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2022 | 33,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |
| 2024 | 31,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json (Database) [T2] | T2 | [observed] |

---

### Incumbent Cost History

#### Incumbent 1: Copper Price — Global (LME Benchmark)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 1990 | 2,661 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 1995 | 2,932 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2000 | 1,815 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2004 | 2,926 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2006 | 6,731 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2008 | 6,963 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2009 | 5,164 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2010 | 7,538 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2011 | 8,823 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2015 | 5,510 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2016 | 4,868 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2020 | 6,175 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2021 | 9,317 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2022 | 8,829 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2023 | 8,491 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |
| 2024 | 9,142 | $/tonne | data/copper/cost/Copper_Price_Global.json (Database) [T2] — converted from $/lb | T2 | [observed] |

Catalog raw unit: $/lb. Conversion factor applied: 1 tonne = 2,204.62 lbs.

#### Incumbent 2: Copper Mining Cost — Global

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2012 | 2,600 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |
| 2015 | 3,300 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |
| 2018 | 3,395 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |
| 2020 | 3,300 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |
| 2022 | 4,100 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |
| 2024 | 4,600 | $/tonne | data/copper/cost/Copper_Copper_Mining_Cost_Global.json (Database) [T2] | T2 | [observed] |

Note: Mining cost is rising — unlike disruptor technology costs. This reflects ore grade decline and energy input inflation. The cost-fitter should model copper mining cost as a separate upward-sloping trend, distinct from technology cost curves.

#### Incumbent 3: Natural Gas Price — USA (Power Generation Fuel Input)

All values: [CAUTION: EIA source — historical data only]

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2000 | 4.31 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2005 | 8.69 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2010 | 4.37 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2012 | 2.75 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2015 | 2.62 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2019 | 2.56 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2020 | 2.03 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2021 | 3.89 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2022 | 6.45 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2023 | 2.53 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |
| 2024 | 2.19 | $/MMBTU | Natural_Gas_Price_USA.json (US Energy Information Administration) [T1] [CAUTION: EIA source — historical data only] | T1 | [observed] |

#### Incumbent 4: Gas Peaker LCOE — USA (Power Generation Incumbent)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2009 | ~150 | $/MWh | Lazard LCOE+ v3.0 (2009), midpoint of range [T3] [CAUTION: Lazard source — historical data only] | T3 | [observed] |
| 2016 | ~185 | $/MWh | Lazard LCOE+ v10.0 (2016), midpoint of range [T3] [CAUTION: Lazard source — historical data only] | T3 | [observed] |
| 2020 | ~175 | $/MWh | Lazard LCOE+ v14.0 (2020), midpoint of range [T3] [CAUTION: Lazard source — historical data only] | T3 | [observed] |
| 2023 | 168 | $/MWh | Lazard LCOE+ v17.0 (2023), midpoint of $115–221/MWh range [T3] [CAUTION: Lazard source — historical data only] | T3 | [observed] |

Note: Gas CCGT (combined cycle, more relevant for baseload displacement) LCOE: ~$83/MWh in 2009, ~$76/MWh in 2023 (Lazard v3.0 to v17.0). Gas peaker costs have risen by ~18% since 2009 while solar has fallen ~91% and onshore wind ~62% over the same period.

#### Incumbent 5: ICE Vehicle — USA (Transport)

| Year | Cost | Unit | Source | Tier | Data Type |
|------|------|------|--------|------|-----------|
| 2010 | 22,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2015 | 24,500 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2020 | 27,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2022 | 28,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |
| 2024 | 29,000 | $/vehicle | data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json (Database) [T2] | T2 | [observed] |

---

### Copper Demand Data (Contextual — for Cost-Fitter and Demand-Decomposer)

#### Global Copper Consumption (Thousand Metric Tonnes)

| Year | Consumption (kt) | Source | Tier | Data Type |
|------|-----------------|--------|------|-----------|
| 2000 | 15,122 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2005 | 16,552 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2010 | 19,130 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2015 | 23,057 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2018 | 24,484 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2020 | 23,800 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2022 | 25,500 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2023 | 26,550 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |
| 2024 | 27,347 | data/copper/adoption/Copper_Annual_Consumption_Global.json (Database) [T2] | T2 | [observed] |

#### Copper Demand Share by Application (% of Total Annual Demand, Global)

All values [observed]:

| Year | EV (%) | Solar (%) | Wind (%) | Electrical Infra (%) | Transport-All (%) | Source |
|------|--------|-----------|----------|---------------------|-------------------|--------|
| 2015 | 1.0 | 0.7 | 0.7 | 35.0 | 13.0 | data/copper/adoption/Copper_*_Percentage_Global.json (Database) [T2] |
| 2018 | 2.0 | 1.0 | 1.0 | 34.0 | 14.0 | data/copper/adoption/ (Database) [T2] |
| 2020 | 2.8 | 1.3 | 1.1 | 34.0 | 14.0 | data/copper/adoption/ (Database) [T2] |
| 2022 | 3.8 | 1.7 | 1.3 | 33.0 | 15.0 | data/copper/adoption/ (Database) [T2] |
| 2023 | 4.5 | 1.9 | 1.4 | 33.0 | 15.0 | data/copper/adoption/ (Database) [T2] |
| 2024 | 5.0 | 2.0 | 1.5 | 33.0 | 15.0 | data/copper/adoption/ (Database) [T2] |

Note: These percentages are from the catalog "Database" source (unattributed). Treat as T2 but flag for independent verification — per-application copper demand shares are often contested across industry sources.

#### Copper Intensity per Technology Unit (Observed Engineering Data)

| Technology | Copper per Unit | Source | Tier | Data Type |
|------------|----------------|--------|------|-----------|
| ICE vehicle | ~23 kg/vehicle | Copper Development Association (CDA), copper.org [T3] | T3 | [observed] |
| Hybrid electric vehicle | ~40 kg/vehicle | CDA, copper.org [T3] | T3 | [observed] |
| Battery electric vehicle (BEV) | ~83 kg/vehicle | CDA, copper.org [T3] | T3 | [observed] |
| Solar PV | ~5.0 tonnes/MW | International Copper Association (ICA); CDA [T3] | T3 | [observed] |
| Onshore wind | ~3.0 tonnes/MW | CDA (copper.org North American Wind Energy Analysis) [T3] — see note | T3 | [observed] |
| Offshore wind | ~9.5 tonnes/MW | CDA estimate including submarine cables [T3] | T3 | [observed] |
| Li-ion battery (stationary) | ~200 kg/MW | CDA, via visual capital [T3] | T3 | [observed] |
| Electric bus (BEV) | ~224–369 kg/bus | CDA, copper.org [T3] | T3 | [observed] |

Note on onshore wind copper intensity: Multiple sources conflict. CDA North America Wind analysis (copper.org) cites 2.16–3.35 t/MW depending on transformer type. BloombergNEF (2024) reports intensity declining to ~2.5 t/MW by end of decade. Use 3.0 t/MW as the observed central estimate with a range of 2.2–4.8 t/MW for sensitivity. This is flagged as a data conflict in Source Conflicts.

---

### Current Costs

- **Disruptor current costs (2024):**
  - Li-ion battery pack global median: $115/kWh (Rethinkx T2, 2024) [observed]
  - Li-ion passenger BEV pack: $97/kWh (Rethinkx T2, 2024) [observed]
  - BESS 2-hour turnkey global: $269/kWh (Rethinkx T2, 2024) [observed]
  - Solar PV installed global: $700/kW (Rethinkx T2, 2024) [observed]
  - Solar PV LCOE global weighted avg: $43/MWh (IRENA T1, 2024) [CAUTION: IRENA source — historical data only] [observed]
  - Onshore wind installed global: $1,041/kW (Rethinkx T2, 2024) [observed]
  - Onshore wind LCOE global weighted avg: $34/MWh (IRENA T1, 2024) [CAUTION: IRENA source — historical data only] [observed]
  - Offshore wind LCOE global weighted avg: $79/MWh (IRENA T1, 2024) [CAUTION: IRENA source — historical data only] [observed]
  - EV median USA: $31,000/vehicle (catalog T2, 2024) [observed]

- **Incumbent current costs (2024):**
  - Copper LME global price: $9,142/tonne (catalog T2, 2024, converted from $4.147/lb) [observed]
  - Copper mining cost global: $4,600/tonne (catalog T2, 2024) [observed]
  - Natural gas USA: $2.19/MMBTU (US Energy Information Administration T1, 2024) [CAUTION: EIA source — historical data only] [observed]
  - Gas peaker LCOE USA: ~$168/MWh midpoint (Lazard v17.0 T3, 2023, $115–$221/MWh range) [CAUTION: Lazard source — historical data only] [observed]
  - Gas CCGT LCOE USA: ~$76/MWh (Lazard v17.0 T3, 2023) [CAUTION: Lazard source — historical data only] [observed]
  - ICE mid-size sedan USA: $29,000/vehicle (catalog T2, 2024) [observed]

---

### Unit Notes

- **Multi-vector analysis:** This query covers five distinct disruption vectors, each with its own service-level unit:
  - Vector 1 (EV vs. ICE transport): $/vehicle for purchase parity; $/km or $/mile for operating parity
  - Vector 2 (Solar PV vs. gas peaker): $/MWh (LCOE) is the correct service-level unit
  - Vector 3 (Onshore wind vs. CCGT): $/MWh (LCOE) is the correct service-level unit
  - Vector 4 (Offshore wind vs. CCGT/peaker): $/MWh (LCOE) is the correct service-level unit
  - Vector 5 (Li-ion BESS enabling SWB): $/kWh storage for capacity cost; $/MWh discharged for service-level
  - Copper commodity: $/tonne is the correct unit for commodity price analysis

- **Hardware-to-service conversion needed:** YES, for the following:
  - Solar PV $/kW installed → $/MWh LCOE: requires capacity factor (~16.3% global avg, 2024, from catalog), WACC (~7%), plant life (25 yr), O&M cost
  - Wind $/kW installed → $/MWh LCOE: requires capacity factor (onshore ~34%, offshore higher) and same financial parameters
  - BESS $/kWh capacity → $/MWh dispatched: requires cycle count, round-trip efficiency (~85%), depth of discharge, replacement schedule
  - Li-ion battery pack $/kWh → $/vehicle: multiply by vehicle pack size (typical BEV ~60–75 kWh for USA passenger)

- **Conversion parameters available in catalog:**
  - Solar PV capacity factor global: data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json — 2024 value: 16.3%
  - Natural gas capacity factor USA: data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_USA.json — 2024 value: 35.8%
  - (No wind capacity factor series found in catalog — use IRENA global avg: 34% onshore, ~42% offshore)

---

### Data Gaps

1. **Intermediate-year solar LCOE (2012, 2014, 2016):** Only available as approximate chart-read values from IRENA's 2018 report figures. Exact numbers require the IRENA interactive dashboard download (irena.org/Data/View-data-by-topic/Costs/Global-LCOE-and-Auction-values).
2. **Offshore wind intermediate LCOE (2012–2020):** IRENA reports cite 2010 and 2022–2024 clearly; intermediate years were interpolated in search results and are not confirmed at digit precision.
3. **Solar PV module price pre-2010:** T3 sources only (NREL composite, Nemet/Farmer-Lafond academic reconstruction). No T1 or T2 primary data exists for 2000–2009 in the catalog. Approximate nominal $/W values used: $5.0 (2000), $3.5 (2004), $4.2 (2008 anomaly), $1.8 (2010).
4. **Onshore wind LCOE pre-2009:** No IRENA or Lazard data; catalog provides installed $/kW back to 1984 but conversion to LCOE requires financial assumptions not yet applied.
5. **Wind turbine copper intensity:** Multiple conflicting sources — CDA, BloombergNEF, Wood Mackenzie all cite different values for onshore wind (2.2–14.9 tonnes/MW range across sources). The 3.0 t/MW midpoint is used as central value; cost-fitter should flag this sensitivity.
6. **Copper demand share by application validation:** The catalog's percentage series for EV, solar, and wind demand shares are sourced only as "Database" without named methodology. They should be cross-checked against ICSG (International Copper Study Group) or WoodMac data before use in stream-forecaster.
7. **EV copper intensity declining trend:** Benchmark Minerals (2024) reports BEV copper intensity declining from ~83 kg toward ~45 kg by 2030 due to thrifting and substitution. No historical time-series of this intensity decline was found — only a 2024 snapshot and a forward-looking estimate. The cost-fitter and demand-decomposer should treat the current 83 kg/BEV as an observed ceiling, not a fixed constant, and model intensity as potentially declining.
8. **Charging infrastructure copper demand:** Not captured in the per-vehicle intensity figures. EV charging stations require substantial copper per unit but no time-series data was found.
9. **No wind capacity factor series in catalog:** Cannot confirm the global average capacity factor for onshore or offshore wind from T2 sources. IRENA cites 34% onshore (2024) and documents capacity factor improvement from 27% in 2010 to 34% in 2024, which is relevant for LCOE calculation.
10. **BESS cost pre-2019:** Catalog BESS data only starts at 2019. Use Li-ion battery pack median (which starts 2010) as a proxy for earlier BESS cost trajectories, noting that system-level markup over cell cost has declined over time.

---

### Source Conflicts

1. **Solar PV LCOE 2010 baseline — two IRENA figures:** Some IRENA reports cite $0.460/kWh (2010), while the IRENA technology page states $0.417/kWh as the 2010 baseline. The higher $0.460/kWh figure appears in later reports as a revised estimate. Used $0.460/kWh as reported in the most widely cited IRENA 2023 annual report. Note this discrepancy for the cost-fitter.
2. **Onshore wind copper intensity — wide range:** CDA North America Wind analysis: 2.16–3.35 t/MW depending on transformer materials; visualcapitalist/CDA summary: ~4.7 t/MW for 3 MW turbine; BloombergNEF 2024 reports intensity declining to ~2.5 t/MW. Resolution: used 3.0 t/MW as a central estimate. The cost-fitter and demand-decomposer must treat this as a ±50% uncertainty.
3. **BEV copper intensity — two CDA figures:** CDA states 83 kg/BEV in one report; 91 kg/BEV in another. Benchmark Minerals 2024 states an average "just shy of 70 kg." Resolution: used 83 kg as the observed CDA value, noting that content is declining and the 70 kg figure likely reflects more recent 2024 models.
4. **EV catalog prices (T2) vs. market-mix ATP (T3):** The catalog EV price series ($31,000 median USA in 2024) tracks entry-level/economy pricing; market-mix ATP per KBB/Cox is ~$55,000–57,000. Both are valid but measure different things. The catalog tracks the lowest accessible EV price, relevant for parity analysis; the market-mix figure reflects total fleet spending. The cost-fitter must be aware that parity at the entry level does not imply parity for the full market mix.
5. **Lazard gas peaker LCOE vs. IRENA fossil fuel cost:** IRENA's weighted average fossil fuel generation cost in 2024 is $100/MWh globally, while Lazard's gas peaker midpoint is ~$168/MWh for the US market. These measure different things: IRENA measures existing fleet average cost, Lazard measures new-build US peaker LCOE. Both are valid comparators depending on framing — existing fleet (lower) vs. new-build capacity (higher). Used both.

---

### Compliance Checklist

| ID | Status | Note |
|----|--------|------|
| 2.1 | PASS | Li-ion: 15 pts 2010–2024 (T2); Solar PV installed: 15 pts 2010–2024 (T2); Onshore wind installed: 41 pts 1984–2024 (T2) |
| 2.2 | PASS | Natural gas price USA: 28 pts 1997–2024 (US Energy Information Administration, T1); Copper LME price: 35 pts 1990–2024 (T2); Gas peaker LCOE: 4 pts via Lazard T3 |
| 2.3 | PASS | Li-ion: $115/kWh (2024, T2); Solar PV LCOE: $43/MWh (2024, IRENA T1 [CAUTION: IRENA source — historical data only]); Onshore wind LCOE: $34/MWh (2024, IRENA T1 [CAUTION: IRENA source — historical data only]) |
| 2.4 | PASS | Natural gas USA: $2.19/MMBTU (2024, US Energy Information Administration T1); Gas peaker LCOE: $115–221/MWh (2023, Lazard T3); Copper mining cost: $4,600/tonne (2024, T2); ICE sedan: $29,000 (2024, T2) |

**Overall: COMPLIANT**

---

## Sources

- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/battery_pack/cost/Lithium_Ion_Battery_Pack_Median_Cost_Global.json` — Rethinkx, $/kWh, 2010–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/battery_pack/cost/Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` — Rethinkx, $/kWh, 2019–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/cost/Solar_Photovoltaic_Installed_Cost_Global.json` — Rethinkx, $/kW, 2010–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/cost/Onshore_Wind_Installed_Cost_Global.json` — Rethinkx, $/kW, 1984–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/cost/Offshore_Wind_Installed_Cost_Global.json` — Rethinkx, $/kW, 2000–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/cost/Solar_PV_Module_(Mainstream)_Cost_Europe.json` — Rethinkx, $/W, 2017–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_storage/cost/Battery_Energy_Storage_System_(2-hour_Turnkey)_Cost_Global.json` — Rethinkx, $/kWh, 2019–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json` — Rethinkx, $/kWh, 2019–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — Rethinkx, %, 2010–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/energy_generation/capacity_factor/Natural_Gas_Capacity_Factor_USA.json` — Rethinkx, %, 2006–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/natural_gas/cost/Natural_Gas_Price_USA.json` — US Energy Information Administration [CAUTION: EIA source — historical data only], $/MMBTU, 1997–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/natural_gas/cost/Natural_Gas_Price_Europe.json` — FRED, $/MMBTU, 1990–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/crude_oil/cost/Crude_Oil_Brent_Price_Global.json` — Database (T2), $/BBL, 1990–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/cost/Copper_Price_Global.json` — Database (T2), $/lb, 1990–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/cost/Copper_Copper_Mining_Cost_Global.json` — Database (T2), $/tonne, 2012–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_Annual_Consumption_Global.json` — Database (T2), kt, 1990–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_EV_Demand_Percentage_Global.json` — Database (T2), %, 2015–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_Solar_Demand_Percentage_Global.json` — Database (T2), %, 2015–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_Wind_Turbines_Percentage_Global.json` — Database (T2), %, 2015–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_Electrical_Demand_Percentage_Global.json` — Database (T2), %, 2000–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/copper/adoption/Copper_Demand_Transportation_Percentage_Global.json` — Database (T2), %, 2000–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/passenger_cars/cost/Passenger_Vehicle_(EV)_Median_Cost_USA.json` — Database (T2), $/vehicle, 2010–2024
- `/Users/himanshuchauhan/TONY/STDF/stdf-agents/data/passenger_cars/cost/Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — Database (T2), $/vehicle, 2010–2024
- [IRENA Renewable Power Generation Costs in 2023](https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023) [CAUTION: IRENA source — historical data only] — T1, $/MWh LCOE series solar/wind 2010–2023
- [IRENA Renewable Power Generation Costs in 2024 Summary](https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2025/Jul/IRENA_TEC_RPGC_in_2024_Summary_2025.pdf) [CAUTION: IRENA source — historical data only] — T1, 2024 data points
- [IRENA Global LCOE Dashboard](https://www.irena.org/Data/View-data-by-topic/Costs/Global-LCOE-and-Auction-values) [CAUTION: IRENA source — historical data only] — T1 interactive series
- [Lazard LCOE+ Version 17.0 (2023)](https://www.lazard.com/media/2ozoovyg/lazards-lcoeplus-april-2023.pdf) [CAUTION: Lazard source — historical data only] — T3, gas peaker and CCGT LCOE ranges
- [NREL PV Pricing Trends: Historical, Recent, and Near-Term (NREL/PR-6A20-56776)](https://docs.nrel.gov/docs/fy13osti/56776.pdf) — T3, solar module prices 2000–2012
- [Copper Development Association — Copper in Electric Vehicles](https://www.copper.org/publications/pub_list/pdf/A6191-ElectricVehicles-Factsheet.pdf) — T3, copper intensity per vehicle type
- [International Copper Association — Copper in Vehicles](https://internationalcopper.org/resource/copper-the-material-of-choice-for-vehicle-manufacturers/) — T3, copper intensity per vehicle type
- [CDA North American Wind Energy Copper Content Analysis](https://copper.org/publications/pub_list/pdf/a6198-na-wind-energy-analysis.pdf) — T3, wind turbine copper intensity per MW
