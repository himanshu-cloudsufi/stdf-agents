---
name: reference_ev_ice_passenger_catalog_coverage
description: Catalog coverage and T1/T3 sources for EV vs. ICE passenger vehicle disruption analysis (purchase price parity, battery pack cost, fuel cost)
type: reference
---

## Catalog Coverage for EV vs. ICE Passenger Vehicle Analysis

### EV Purchase Price Curves (data/passenger_cars/cost/)
- `Passenger_Vehicle_(EV)_Median_Cost_USA.json` — $/vehicle, 2010–2025, 16 pts, source "Database" (unattributed). Values: $52,000 (2010) → $31,000 (2024). WARNING: underestimates market-mix ATP by ~30–50%; tracks entry-level pricing.
- `Passenger_Vehicle_(EV)_Median_Cost_China.json` — $/vehicle, 2010–2025, 16 pts. Values: $39,000 (2010) → $16,200 (2024). China shows faster decline.
- `Passenger_Vehicle_(EV)_Median_Cost_Europe.json` — same structure.
- `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_USA.json` — $/vehicle, 2010–2025. Values: $109,000 (2010) → $29,000 (2024). Represents entry-level short-range models.
- `Passenger_EV_Cars_(Range_-200_miles)_Lowest_Cost_China.json` — $/vehicle, 2013–2025. Values: $38,600 (2013) → $9,700 (2024). China lowest-cost shows most aggressive decline.

### ICE Purchase Price Curves (data/passenger_cars/cost/)
- `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_Sedan)_USA.json` — $/vehicle, 2010–2025, 16 pts, source "Database". Values: $22,000 (2010) → $29,000 (2024). GRADUAL RISE (not flat). WARNING: understates all-segment ATP which includes trucks/SUVs.
- `Passenger_Vehicle_(ICE)_Median_Price_(Hatchback)_USA.json` — $/vehicle, 2010–2025. $15,650 (2010) → $23,000 (2025).
- `Passenger_Vehicle_(ICE)_Median_Price_(Mid_Size_SUV)_USA.json` — also available.
- Corresponding China, Europe, Rest of World variants for all segments.

### Battery Pack Cost Curves
- `Lithium_Ion_Battery_Pack_Median_Cost_Global.json` (Rethinkx) — $/kWh, 2010–2024, 15 pts. PRIMARY battery curve. Values: $1,436 (2010) → $115 (2024). 2022 spike ($166) is real.
- `Lithium-Ion_Battery_Pack_Passenger_BEV_Cost_Global.json` (Rethinkx) — $/kWh, 2019–2024, 6 pts. Values: $179 (2019) → $97 (2024). Most specific to passenger BEV segment.

### Operating Cost Curves
- `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(10k_year)_Global.json` — $/mile, 2022–2025, source: AAA, Goldman Sachs Research. Values: $1.10 (2022) → $1.30 (2024). NOTE: 2025 point may be model-derived; use only 2022–2024 as observed.
- `Passenger_Car_(ICE)_Average_Car_Cost_per_Mile_(15k_year)_Global.json` — $/mile, 2022–2025. Values: $0.75 → $0.85.
- `Gasoline_Average_Retail_Price_USA.json` (WorldBank) — multi-state series, $/L; compute median per year in python3 to use.
- `Electricity_Residential_Price_USA.json` — $/kWh, 1980–2024. Values: $0.128 (2010) → $0.176 (2024).

### T1 Sources for Battery Pack Cost
- DOE Fact of the Week series (annual): Provides observed battery pack cost anchors in current-year dollars on USABLE ENERGY basis. Key values:
  - 2008: $1,415/kWh | 2021: $157/kWh | 2022: $153/kWh | 2023: $139/kWh
  - URL: https://www.energy.gov/eere/vehicles/articles/fotw-[number] (search DOE FOTW EV battery)
  - [CAUTION: DOE/VTO source — historical data only]
  - NOTE: DOE values ~5–10% LOWER than Rethinkx T2 values due to usable vs. rated energy basis

### T3 Sources for EV Market-Mix ATP
- Cox Automotive / Kelley Blue Book monthly ATP reports (2020–present) — URL: https://www.coxautoinc.com/learning-center/tag/average-transaction-price/
  - 2021: ~$56,000 EV | 2022 peak: ~$65,108 EV | Sep 2023: ~$50,683 EV | 2024: ~$55,000 EV
  - WARNING: KBB ATP is market-mix (Tesla-dominated) — much higher than catalog entry-level curve

### Key Unit Confusion Patterns
- Catalog EV purchase price ≠ market-mix average transaction price. Catalog = entry-level/economy. KBB/Cox = full market mix.
- Battery pack $/kWh (hardware) must be converted to $/vehicle by the cost-fitter using pack size (~60–75 kWh for USA passenger BEV).
- DOE FOTW uses usable-energy basis; Rethinkx uses rated/nameplate basis — creates ~5–10% offset in absolute values.
- ICE catalog tracks sedans/hatchbacks, not the truck/SUV-dominated market mix.

### Key 2024–2025 Data Points
- Li-ion global median pack 2024: $115/kWh (Rethinkx T2)
- Li-ion global median pack 2025: $108/kWh (BloombergNEF [CAUTION: BNEF source — historical data only] T3, pre-2026-03-21)
- Li-ion passenger BEV pack 2024: $97/kWh (Rethinkx T2); 2025: $99/kWh (BloombergNEF [CAUTION: BNEF source — historical data only] T3)
- DOE anchor 2023: $139/kWh (T1 usable energy)
- EV median USA (entry-level): $31,000 (T2 catalog, 2024)
- EV market-mix USA: ~$55,000–57,000 (Cox/KBB T3, 2024–2025)
- ICE mid-size sedan USA: $29,000 (T2 catalog, 2024)
- ICE all-segment market-mix USA: $48,401–49,077 (Cox/KBB T3, 2024–2025)
- US gasoline: $0.87/L ≈ $3.29/gal annual average 2024 (WorldBank T1)
- US electricity residential: $0.176/kWh (T2 catalog, 2024)
- AAA ICE total annual cost 2024: $12,297/yr ($0.82/mile at 15k miles/yr) [T1]
- AAA ICE total annual cost 2025: $11,577/yr ($0.77/mile at 15k miles/yr) [T1]
- AAA EV fuel cost 2022: 4.0¢/mile (vs ICE 18.4¢/mile) [T1]
- AAA EV fuel cost 2024: ~5.0¢/mile compact SUV (vs ICE ~13¢/mile) [T1] — electricity rate 15.9¢/kWh
- AAA ICE fuel cost 2025: 13.0¢/mile (gas at $3.151/gal avg); electricity 16.7¢/kWh [T1]

### Price Premium Status (2024)
- Entry-level match: EV lowest ~$29k vs ICE sedan ~$29k — approximate parity in entry-level sedan segment [observed]
- Market-mix: EV ~$55k vs ICE market ~$49k — EV still 12% premium [observed]
- China: EV median $16,200 vs ICE sedan ~$19,000 — EV BELOW ICE in median market [observed]

### T3 Source for ICE All-Segment Market-Mix ATP (Confirmed 2026-03-21)
- NADA Annual Financial Profile reports: avg retail selling price 2017–2024 available as plain text
  - 2017: $34,670 | 2018: $35,608 | 2019: $36,824 | 2020: $38,961
  - 2021: $42,379 | 2022: $46,287 | 2023: $47,014 | 2024: $47,652
  - URL: https://www.nada.org/nada/nada-data (Wards Intelligence / Automotive News source)
  - NOTE: Pre-2017 not available in text form from this source
- Cox/KBB all-vehicle December 2024: $49,740 (single month, December peak — use NADA annual for full-year)

### Data Not Available in Catalog
- Maintenance cost time series ($/year or $/mile) for BEV or ICE — not in catalog; no web time series found
- EV efficiency (kWh/mile) historical by model year — not in catalog
- Used-vehicle price series — not in catalog
- ICE all-segment ATP before 2017 — not available from any T1/T3 public source
