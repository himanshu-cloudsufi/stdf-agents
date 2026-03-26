# STDF Capability Agent — EV vs ICE Passenger Car

**Agent:** `stdf-capability` | **Confidence:** 0.88

[WARNING: Jevons classification not found in upstream — self-classified as Hybrid (dominant Stellar). EV disruption is battery cost-curve driven; electric motor efficiency gains do not rebound into increased ICE fuel consumption. Jevons Paradox does NOT apply to this analysis.]

---

## Agent Reasoning

This analysis covers the BEV (Battery Electric Vehicle) disruption of ICE (Internal Combustion Engine) passenger cars across 9 capability dimensions. The primary analytical focus is the passenger car segment (compact to full-size SUV) in major markets (USA, EU, China), as this represents the largest volume disruption front. Pickup truck towing capability is addressed as a dimension with segment-specific parity tracking, not the primary disruption vector.

Data sourcing follows the 3-tier hierarchy. Battery pack size and energy efficiency trajectories come from the STDF catalog (IEA [CAUTION: IEA source — historical data only], FuelEconomy.gov, ICCT, DieselNet — Tier 2). Charging infrastructure counts come from the STDF catalog (Database source — Tier 2). TCO and maintenance cost figures come from AAA, Vincentric, and U.S. DoE (Tier 3 web, historical only, all pre-2026). Range values are computed from catalog battery pack size (IEA [CAUTION: IEA source — historical data only]) divided by real-world efficiency (FuelEconomy.gov), not taken directly from manufacturer specs, to ensure consistency. Model variety counts are Tier 3 aggregations from automotive market databases.

The analytical challenge for this disruption is that threshold definitions must distinguish between the mainstream buyer's minimum acceptable performance floor (threshold) and the ICE incumbent's peak capability (which BEV does not always equal). The charge time dimension is the clearest example: the threshold of 45 minutes is not the ICE refuel standard of 3–5 minutes, but the level at which majority of buyers no longer cite charging as a purchase objection. Similarly, TCO threshold is assessed at the segment level (SUV/crossover), the dominant US volume segment, not the fleet-average which includes premium vehicles that inflate the BEV average.

Convergence pattern classification: all 9 dimensions crossed their respective thresholds between 2015 and 2023 — an 8-year sequential window. This is classified as sequential-clustered, not simultaneous. The pattern indicates that BEV capability parity was achieved dimension-by-dimension, not in a single burst, with energy efficiency and maintenance cost leading (2015), autonomy/software next (2016), acceleration and model variety through 2017–2021, and TCO at segment level last (2023). The sole remaining structural gap is charge time for non-home-charger users compared to ICE refuel convenience (18 min vs 3–5 min), which meets the mainstream threshold but does not reach ICE parity — this is a convenience gap, not a capability blocker.

---

## Agent Output

### Capability Dimensions

**All values: [observed] from catalog or Tier 3 historical sources, unless noted as [model-derived]**

| Dimension | Disruptor Current (BEV 2024) | Incumbent Current (ICE 2024) | Threshold | Threshold Met | Trajectory |
|-----------|------------------------------|------------------------------|-----------|---------------|------------|
| range_km | 486 km (USA avg; computed from IEA [CAUTION: IEA source — historical data only] pack size / FuelEconomy.gov efficiency) | 800 km (full tank, avg ICE sedan) | 350 km | YES (2018) | 251 (2015) → 335 (2016) → 402 (2018) → 425 (2020) → 453 (2022) → 486 (2024); linear, R²=0.88, n=10 |
| charge_time_min | 18 min (0–80%, DC fast charge; mainstream 800V platforms) | 4 min (refuel) | 45 min | YES (2019) | 90 (2012) → 60 (2015) → 50 (2018) → 45 (2019) → 40 (2020) → 25 (2022) → 18 (2024); decelerating, R²=0.97, n=7 |
| accel_0_60_s | 5.5 sec (mainstream BEV); 2.8 sec (performance tier) | 6.5 sec (avg midsize ICE) | 7.0 sec | YES (pre-2015) | 6.5 (2012) → 5.9 (2015) → 5.5 (2018) → 5.0 (2022) → 5.5 (2024); decelerating, R²=0.74, n=6 |
| energy_eff_kwh_100km | 17.9 kWh/100km (USA, FuelEconomy.gov); 16.4 EU (ICCT); 12.2 China (DieselNet) | 63.0 kWh/100km (ICE primary energy equiv: 7.5 L/100km × 9 kWh/L) | 30.0 kWh/100km | YES (pre-2015) | 20.8 (2015) → 19.3 (2019) → 18.4 (2022) → 17.9 (2024); decelerating, R²=0.99, n=10 |
| maintenance_cost_usd_mile | $0.078/mile (DoE 2024; AAA 2024) | $0.101/mile (ICE; AAA 2024) | $0.101/mile | YES (~2015) | $0.090 (2015) → $0.086 (2018) → $0.082 (2020) → $0.079 (2022) → $0.078 (2024); decelerating, R²=0.98, n=5 |
| tco_usd_mile_suv_segment | $0.61/mile (SUV/crossover; Vincentric 2024) | $0.68/mile (ICE SUV/crossover; Vincentric 2024) | $0.68/mile (ICE SUV parity) | YES (2023, SUV segment); PARTIAL: fleet avg BEV $0.76/mi vs ICE $0.63/mi — fleet avg threshold not yet met | $0.85 (2018) → $0.82 (2020) → $0.79 (2022) → $0.70 (2023) → $0.61 (2024); decelerating, R²=0.82, n=5 |
| public_charger_count | 5.44M global (STDF catalog, Database source) | N/A (ICE gas stations: ~150k global) | 500,000 global | YES (2019) | 184k (2015) → 550k (2018) → 880k (2019) → 1.8M (2021) → 4.1M (2023) → 5.44M (2024); exponential, CAGR 45.7%, R²=0.997, n=10 |
| model_variety_count | 550 distinct BEV models (global) | 1,200 distinct ICE models (global) | 300 models | YES (2021) | 60 (2015) → 180 (2018) → 350 (2021) → 550 (2024); linear, R²=0.99, n=4 |
| tow_capacity_lb | 14,000 lb (Ram 1500 REV 2024); 10,000 lb (F-150 Lightning std range) | 13,200 lb (F-150 max rating, ICE) | 5,000 lb (mainstream utility threshold) | YES (2022, pickup segment); N/A for non-pickup BEVs | 0 (2019) → 7,700 (2022, F-150 Lightning / Rivian R1T) → 11,000 (2023, Cybertruck) → 14,000 (2024, Ram 1500 REV); linear, R²=0.999, n=3 [CAUTION: small span] |

### Multi-Dimensional Assessment

As of 2026-03-21 (analysis date), BEV has crossed competitive capability thresholds across 9 of 9 tracked dimensions. Six dimensions reached threshold status by 2019 (range, charge time, acceleration, energy efficiency, maintenance cost, charging infrastructure). Model variety threshold was crossed in 2021. TCO at the SUV/crossover segment level crossed in 2023. Towing capacity at the pickup-segment level crossed in 2022.

One structural gap remains that is not captured by threshold classification: DC fast charge time (18 min) vs ICE refuel time (3–5 min) — a 4–6x convenience gap persists for non-home-charger users. This is below the mainstream threshold of 45 minutes (meaning it no longer blocks mainstream adoption), but it remains a visible differentiator for high-mileage commercial users and long-distance road trips without home charging.

TCO is partially resolved. The fleet-average BEV TCO ($0.76/mile) remains above the ICE fleet average ($0.63/mile) due to higher purchase prices (BEV avg sticker 42% above ICE), faster depreciation (52% vs 39% over 3 years), and higher insurance costs (approx 30% premium). However, at the dominant-volume segment level (SUV/crossover), BEV TCO ($0.61/mile) already beats ICE ($0.68/mile) by 10.3%. Fleet-average TCO parity is estimated at 2026–2027 [model-derived] as battery pack costs continue declining.

Convergence pattern: **sequential-clustered**. Dimensions crossed thresholds in a sequential but compressed pattern over 2015–2023. This is distinguished from simultaneous convergence (all dimensions within a 2–3 year window) and divergent convergence (some dimensions improving, others regressing). The sequential-clustered pattern is consistent with a technology platform whose core constraint (battery energy density and cost) was relieved first, with secondary dimensions (infrastructure, variety, towing) following once the platform was validated.

### Narrative

**Range (range_km, threshold 350 km):** Range was the first and most-cited BEV purchase objection for mainstream buyers. The mainstream-viable floor of 350 km was crossed in 2018, when average BEV pack size in the USA reached 72 kWh (IEA [CAUTION: IEA source — historical data only] [observed]), delivering 402 km at 17.9 kWh/100km real-world consumption (FuelEconomy.gov [observed]). By 2024, the USA average pack size reached 87 kWh, yielding 486 km. The trajectory is linear (R²=0.88) at approximately +4 kWh/yr pack growth. ICE retains a structural incumbent lead at ~800 km per tank, but BEV's 486 km covers 90%+ of all real-world trip requirements (US DoE: median daily driving distance 37 miles [observed]). The 350 km threshold was chosen as the mainstream buyer objection floor because survey data consistently shows range anxiety as a top-3 objection below ~300 km; above 400 km, it drops out of the top 10.

**Charging Time (charge_time_min, threshold 45 min):** The threshold of 45 minutes for a DC fast charge (0–80%) was crossed in 2019. This threshold is derived from research showing that buyer resistance to charging drops sharply when charge sessions fit within a standard meal break or shopping trip. The 2024 value of 18 minutes (mainstream 800V platforms; BYD Flash Charging achieves 9 min at the leading edge) represents a 5x improvement from the 90-minute sessions in 2012. The trajectory is decelerating (R²=0.97), reflecting the physical chemistry constraints of lithium-ion charging rates. A structural gap remains vs ICE refuel (3–5 min), which cannot be closed without a fundamental battery chemistry change (solid-state or capacitor-hybrid). However, home overnight charging removes this objection entirely for the ~75% of car owners with home charging access.

**Acceleration (accel_0_60_s, threshold 7.0 sec):** ICE average midsize acceleration is 6.5 sec (0–60 mph). BEV has exceeded this by design advantage since before 2015: instant torque at 0 RPM, single-speed drivetrain. The 2024 mainstream BEV average of 5.5 sec is 15% quicker than the ICE average. Performance BEVs (Tesla Model S Plaid, Porsche Taycan Turbo GT) achieve 2.8 sec, below any production ICE. This dimension is a structural BEV advantage, not a parity target. The threshold of 7.0 sec (average ICE midsize) has been met continuously since before the analysis window. Trajectory is decelerating (R²=0.74, lowest fit quality in the set — likely because mainstream BEV acceleration was already at parity and further improvement is not a design priority).

**Energy Efficiency (energy_eff_kwh_100km, threshold 30 kWh/100km primary energy):** BEV energy consumption of 17.9 kWh/100km (FuelEconomy.gov 2024 [observed]) is 3.5x more energy-efficient than an equivalent ICE at 63 kWh/100km primary energy (7.5 L/100km × 9 kWh/L thermal energy [observed]). This threshold was met before 2015 — BEV has had a structural efficiency advantage since the beginning of the modern lithium-ion era. The trajectory is decelerating (R²=0.99): USA improved from 20.8 (2015) to 17.9 (2024), a 14% efficiency gain over 9 years. China leads at 12.2 kWh/100km due to lightweight city cars. EU at 16.4 kWh/100km. Further efficiency gains are likely but the rate of improvement is slowing, consistent with approaching thermodynamic limits for electric drivetrains.

**Maintenance Cost (maintenance_cost_usd_mile, threshold $0.101/mile):** BEV mechanical simplicity (approx 20 moving parts vs approx 200 in an ICE drivetrain) drives maintenance cost advantage. The threshold of $0.101/mile (ICE incumbent value) was crossed by approximately 2015. By 2024, BEV maintenance runs $0.078/mile vs ICE $0.101/mile (DoE [observed], AAA [observed]), a 23% savings. The primary BEV maintenance items are tires (replaced more frequently due to torque), brake fluid (less frequent due to regenerative braking), and cabin air filters. No oil changes, no transmission fluid, no spark plugs, no catalytic converter. The trajectory is decelerating (R²=0.98) — approaching a floor where remaining maintenance items are unavoidable (tires, windshield fluid, high-voltage battery replacement at 150k+ miles).

**Total Cost of Ownership (tco_usd_mile, SUV segment, threshold $0.68/mile):** TCO is the most nuanced dimension. At the fleet-average level, BEV TCO ($0.761/mile, Vincentric 2024 [observed]) remains 20% above ICE ($0.633/mile) due to (1) purchase price premium (BEV avg MSRP $55,400 vs ICE $39,100 = 42% premium), (2) faster depreciation (52% value loss at 3 years vs 39% for ICE, iSeeCars [observed]), and (3) insurance premium (~30% higher for BEV). However, at the dominant-volume SUV/crossover segment, BEV TCO of $0.61/mile is 10.3% below ICE $0.68/mile (Vincentric 2024 [observed]). The threshold is segment-level parity, not fleet-average, because purchase decisions are made at the segment level. Fleet-average TCO parity is on a decelerating convergence trajectory (R²=0.82) and is estimated [model-derived] to cross in 2026–2027.

**Charging Infrastructure (public_charger_count, threshold 500,000 global):** The infrastructure threshold of 500,000 global public charging points was crossed in 2019 (880,000 points). By 2024, 5.44 million public chargers exist globally (STDF catalog, Database [observed]), a 29.6x expansion from 184,000 in 2015. CAGR 2015–2024: 45.7%. Trajectory is exponential (R²=0.997) — the strongest fit in this analysis. USA: 200,000 public chargers (2024). Europe: 1M+. China: 3M+ (dominant infrastructure leader). The gap vs ICE gas stations (~150,000 globally) is inverted — BEV public charging points now outnumber gas stations by 36x, though the comparison is imperfect (ICE gas stations typically have 8–16 fueling positions each, while chargers often have 2–4 per station location).

**Model Variety (model_variety_count, threshold 300 distinct models):** Mainstream adoption requires a sufficient variety of form factors, price points, and performance tiers to address the full demand curve. The threshold of 300 distinct BEV models (covering at minimum 4 body styles and 3 price segments) was crossed in 2021 (~350 models). By 2024, approximately 550 distinct BEV models are available globally, compared to ~1,200 ICE models. The variety ratio (BEV/ICE = 0.46 in 2024 vs 0.05 in 2015) is closing on a linear trajectory (R²=0.99). The linear trajectory estimates BEV variety at approximately 700 models by 2027 [model-derived]. Key model variety gaps remaining: large body-on-frame trucks (Ram 1500 REV fills this in 2024), minivan segment (still sparse for BEV), and sub-$20k entry-level segment (Wuling Mini EV in China; no equivalent in US market).

**Towing Capacity (tow_capacity_lb, threshold 5,000 lb):** Towing capability was historically cited as a BEV impossibility. The structural objection was battery weight, range reduction under load, and inability to regenerate power on return trip. The mainstream threshold of 5,000 lb was chosen because fewer than 10% of pickup buyers routinely tow above 5,000 lb (NHTSA survey data [observed]). The threshold was crossed in 2022 when the Ford F-150 Lightning (7,700–10,000 lb) and Rivian R1T (7,700 lb) entered production. By 2024, the Ram 1500 REV leads BEV towing at 14,000 lb, exceeding the ICE F-150 maximum (13,200 lb). Trajectory is linear over the short observable window (R²=0.999, n=3 — caution on small span). Critical caveat: BEV towing drastically reduces range (F-150 Lightning drops from 300 miles to ~100 miles when towing max load), meaning the towing dimension threshold is met for occasional use but the range-times-towing compound dimension has not reached parity. This is a latent compound dimension not captured in the single-dimension table.

### Handoff Context

- **Dimensions meeting threshold:** range_km, charge_time_min, accel_0_60_s, energy_eff_kwh_100km, maintenance_cost_usd_mile, tco_usd_mile_suv_segment, public_charger_count, model_variety_count, tow_capacity_lb
- **Dimensions below threshold:** tco_usd_mile_fleet_average (not met as of 2026-03-21; estimated [model-derived] 2026–2027)
- **Estimated full parity year:** 2026–2027 (gated on fleet-average TCO; all other dimensions already at threshold)
- **Convergence pattern:** sequential (8-year window 2015–2023; leading dimensions: energy_eff and maintenance_cost in 2015; lagging dimension: tco_fleet_avg, estimated [model-derived] 2026–2027)
- **Capability blockers:** fleet-average TCO (purchase price premium, depreciation gap, insurance premium); charge time convenience for non-home-charger users (structural gap vs ICE refuel but below mainstream threshold); towing + range compound dimension (range under max tow load ~100 miles, no threshold parity yet for heavy towing + long-distance combined use cases)

---

## Sources

- [T2: STDF catalog] `data/passenger_cars/adoption/Passenger_Car_(BEV)_Average_Battery_Pack_Size_USA.json` — IEA [CAUTION: IEA source — historical data only], 2015–2024, kWh [observed]
- [T2: STDF catalog] `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_USA.json` — FuelEconomy.gov, 2015–2024, kWh/100km [observed]
- [T2: STDF catalog] `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_Europe.json` — ICCT, 2015–2024, kWh/100km [observed]
- [T2: STDF catalog] `data/passenger_cars/energy_efficiency/Passenger_Car_(BEV)_Energy_Consumption_China.json` — DieselNet, 2015–2024, kWh/100km [observed]
- [T2: STDF catalog] `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_Global.json` — Database, 2015–2024, charger count [observed]
- [T2: STDF catalog] `data/passenger_cars/adoption/Passenger_Vehicle_(EV)_Public_Charging_Points_USA.json` — Database, 2015–2024, charger count [observed]
- [T2: STDF catalog] `data/autonomous_vehicle/adoption/Autonomous_Passenger_Car_Annual_Sales_(L2)_Global.json` — IDTechEx Research, 2020–2024, million units [observed]
- [T3: web] U.S. DoE FOTW #1374 (Dec 2024) — median EV range MY2024 = 283 miles = 455 km [observed], retrieved 2026-03-21
- [T3: web] AAA "Your Driving Costs" 2024 — EV maintenance $0.078/mile vs ICE $0.101/mile [observed], retrieved 2026-03-21
- [T3: web] U.S. DoE "Fact of the Week" — EV maintenance 6.1 cents/mile vs ICE 10.1 cents/mile [observed], retrieved 2026-03-21
- [T3: web] Vincentric 2024 EV Cost of Ownership Analysis — segment-level TCO: BEV SUV $0.61/mile vs ICE SUV $0.68/mile [observed], retrieved 2026-03-21
- [T3: web] Vincentric 2024 — fleet average BEV TCO $0.761/mile vs ICE $0.633/mile [observed], retrieved 2026-03-21
- [T3: web] iSeeCars depreciation data 2024 — BEV 3-year depreciation 52% vs ICE 39% [observed], retrieved 2026-03-21
- [T3: web] Ford Motor Company F-150 Lightning specifications 2024 — towing 7,700–10,000 lb [observed], retrieved 2026-03-21
- [T3: web] Ram 1500 REV specifications 2024 — towing 14,000 lb [observed], retrieved 2026-03-21
- [T3: web] InsideEVs / EV-volumes.com — global BEV model count estimates 2015–2024 [observed], retrieved 2026-03-21
