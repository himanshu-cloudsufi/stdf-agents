---
name: reference_china_truck_catalog_coverage
description: What commercial vehicle, battery pack, and fuel cost data exists in the local catalog for China truck disruption analysis
type: reference
---

## Catalog Coverage for China Heavy Truck / BEV Disruption Analyses

### Commercial Vehicle Cost Curves — China (data/commercial_vehicle/cost/)
- `HCV_commercial_vehicle_(Range-400_KM)_Lowest_Cost_China.json` — BEV heavy commercial vehicle (400km range), USD, 2010–2025. Source tagged "Database" (unattributed smooth curve). Values: $260k (2010) → $110k (2024). Use as T2 baseline; cross-validate with T3 transaction data.
- `Commercial_Vehicle_(EV)_Median_Cost_China.json` — BEV commercial vehicle median, USD 22k–38k (2010–2025). WARNING: represents lighter commercial EVs, NOT Class 8 tractors.
- `LCV_commercial_vehicle_(Range-100_KM)_Lowest_Cost_China.json` — LCV BEV China, USD 14k–50k (2010–2025). Light commercial vehicles only.
- `Heavy_Duty_Commercial_Vehicle_(ICE)_Price_China.json` — ICE heavy truck, USD 40k–68k (2010–2024). Good for incumbent (diesel/LNG) baseline. Gently rising trend ($2k/yr increment in catalog).
- No NGV (natural gas vehicle) purchase price curve exists in the catalog for China.

### Battery Pack Cost Curves — China (data/battery_pack/cost/)
- `Lithium-Ion_Battery_Pack_E-Bus___Commercial_Cost_China.json` — LFP for e-bus and commercial vehicles, $/kWh, 2018–2024, source: Rethinkx. Most specific to trucks. Values: $177 (2018) → $90 (2024). Note: 2022 spike to $144 is real (lithium carbonate price event) — do not smooth.
- `Lithium_Ion_Battery_Pack_Median_Cost_China.json` — Li-ion median, $/kWh, 2010–2025. Values: $1,100 (2010) → $85 (2025). Good for long-run learning curve regression spanning 15 years.

### Fuel/Energy Cost Curves — China
- `Diesel_Average_Retail_Price_China.json` — WorldBank T1, USD/L, 2015–2025. Multi-series (12 provincial series concatenated); MUST compute median per year using python3 (not directly usable as-is). Medians: 2019=$0.930, 2020=$0.770, 2021=$1.025, 2022=$1.190, 2023=$1.080, 2024=$1.045. 2025 only has 3 series — use 2024 as current anchor.
- `Natural_Gas_Price_China.json` — FRED, USD/MMBTU, 1992–2024. Pipeline gas city gate price, NOT LNG station price for trucks.
- `Electricity_Residential_Price_China.json` — USD/kWh, 1995–2024. Residential rate floor. Commercial charging: CNY 0.60–0.80/kWh (industrial), up to CNY 0.88/kWh urban.

### Confirmed T3 Transaction Data Points (Observed, 2023–2024)
Source: chinatruck.net (retrieved 2026-03-20)
- Sep 2023: 440 kWh BEV heavy tractor = CNY 850,000 (~$120k)
- Apr 2024: 400 kWh BEV heavy tractor = CNY 650,000 (~$91k)
- Late 2024: 282 kWh BEV tractor (Shaanxi Auto Delong M3000E) = below CNY 400,000 (~$56k)
- 2024 bare vehicle cost (550hp, no battery) = ~CNY 210,000; battery CNY 600/kWh (from CNY 1,200/kWh)
- NDRC Price Monitor Center: BEV trucks CNY 300k–400k premium over diesel (2024)

### Operational Parameters for Per-km Cost Derivation
- BEV heavy truck energy consumption: 2.0 kWh/km (heavy-duty tractor, per ICCT/literature)
- Diesel heavy truck consumption: 0.30 L/km (30L/100km, heavy-duty standard)
- Annual utilization: 100,000–180,000 km/year (STO Express fleet data, T3)
- Per-km BEV savings over diesel: CNY 0.53–1.06/km depending on diesel price year

### Key Gaps Still Requiring Web Research (T3)
1. LNG station pump price CNY/kg by year — use CEIC Tianjin series
2. LNG truck purchase price — derive from diesel baseline + ~CNY 80,000 LNG premium
3. Pre-2020 BEV tractor real-world transaction prices (T3 not available; catalog T2 is unattributed)
4. Maintenance cost time series for BEV vs diesel (not available as time series in any source found)
5. Battery swap lease cost per km (new market structure, 2023–2024, no time series found)

### Reliable T3 Sources for China Heavy Trucks
- chinatruck.net — fleet transaction prices, most specific to heavy BEV tractors (BEST for 2023-2024 price anchors)
- IEEFA commentaries (annual) — BEV vs LNG market share and TCO; qualitative cost differentials
- 36Kr English (eu.36kr.com) — Chinese industry cost data in English; battery CNY/Wh, per-km savings
- ICCT publications (theicct.org) — China ZE-MHDV market reports (annual volumes, no recent price data); TCO framework from 2021 paper
- CEIC (ceicdata.com) — LNG station price series; industrial electricity by city

### Unit Confusion Patterns
- Catalog HCV curve is in USD; Chinese industry reports are in CNY
- CNY to USD exchange: 2019=6.90, 2020=6.90, 2021=6.45, 2022=6.73, 2023=7.10, 2024=7.15
- LFP battery pack pricing from Chinese sources often cited in CNY/Wh (not $/kWh); CNY 600/Wh = $84/kWh at 2024 rates
- ICCT/IEEFA PDFs are binary and cannot be fetched for text — use HTML pages or search summaries instead
- T2 catalog HCV BEV 2024 value ($110k) is higher than T3 market prices ($56k–$91k); report both
