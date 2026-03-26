---
name: project_ev_ice_analysis
description: EV vs ICE cost curve analysis results — empirical learning rates, thresholds, service-level conversions
type: project
---

## EV vs ICE Cost Curve Analysis (completed 2026-03-16)

### Battery pack learning rate (empirically derived):
- Global: 16.8%/year (from 15-year time series, 2010–2024)
- China: 15.9%/year (from 9-year time series)
- These are per-year rates; deployment-basis rates not derivable from catalog (no deployment volume time series)

### Competitive thresholds:
- **Battery pack $/kWh:** not directly comparable to ICE (different component)
- **Vehicle sticker price parity (USA):** ~2025 ($29,400 EV vs $29,500 ICE sedan)
- **Vehicle sticker price parity (China):** Already crossed in 2022 (lowest-cost EV segment)
- **Service-level $/mile parity:** Crossed in 2023 (EV $0.72/mi vs ICE $0.80/mi)
- **2024 position:** EV $0.66/mi vs ICE $0.85/mi — EV is 22% cheaper

### Inflection threshold (EV at 50–70% of ICE $/mile):
- 70% threshold: ~2025 (EV $0.60/$0.90 ICE = 0.67)
- 50% threshold: ~2027 (EV ~$0.49/$1.00 ICE = 0.49)

### Service-level unit conversion (EV $/mile):
- Vehicle depreciation: purchase price / 200,000 miles
- Electricity: 0.34 kWh/mile × electricity price
- Maintenance: $0.06/mile (EV, vs $0.10/mile ICE)
- Insurance + financing: ~$0.16–0.19/mile (scales with vehicle price)
- 2024 USA total: $0.66/mile for median EV ($31,000 purchase price)

### ICE structural cost drivers (confirmed):
- Fuel price: +31% above 2016 baseline by 2024 (WorldBank data)
- Vehicle MSRP: +$500/year linear rise (2010–2025 catalog)
- ICE $/mile: +$0.05/year (AAA data 2022–2025)

**Why:** Confirmed for downstream tipping point agent use.
**How to apply:** Use these thresholds as input to tipping-point agent; battery cost projections valid through ~2030.

## Oil Market Disruption — Extended Analysis (2026-03-16)

### Transport (EV vs. ICE $/km):
- 9-point EV $/km series 2011–2025 from catalog components: C(t) = 0.4423 × exp(−0.0326×(t−2011)), R²=0.989
- Parity crossed 2015–2016 (~$0.390–$0.395/km)
- 2024: EV=$0.293/km vs ICE=$0.528/km (EV is 55% of ICE)
- Inflection (50–70%): 2021–2025
- ICE cost: $0.466/km (2022) → $0.559/km (2025), rising +$0.011/km/yr

### Solar+BESS (vs. Gas Peaker $/MWh):
- Solar LCOE from catalog: 215.4 × exp(−0.1478×(t−2010)), R²=0.986
- Parity: solar standalone crossed peaker ~2013–2014; combined Solar+BESS already below peaker in 2019 (59.4 vs 129.7 $/MWh)
- 2024: combined=$38.0/MWh vs peaker=$125.7/MWh (30% of incumbent)
- Combined fit: 57.4 × exp(−0.0856×(t−2019)), R²=0.948; decay 8.6%/yr
- Gas peaker LCOE model: (WTI-linked nat gas × 10.8 MMBTU/MWh) + $87/MWh capital + $15/MWh O&M

### Heat Pump (vs. Oil Boiler $/MWh thermal):
- HP installed cost rising in USA: $12,000 (2015) → $15,500 (2024) — NO learning curve
- HP full cost 2024: $152.5/MWh (COP=2.8, $0.176/kWh elec)
- Oil boiler 2024 (WTI=$76): $120.9/MWh — HP is 26% more expensive full cost
- Full cost parity requires WTI > $120–125/bbl
- Running cost parity (fuel only): HP wins at WTI > $58.5/bbl — achieved in 8 of last 9 years
- HP running cost 2024: $62.9/MWh vs oil $75.4/MWh (HP 16.5% cheaper on fuel only)
- Oil boiler LCOH model: (WTI/42 + $0.75) / 0.0341 MWh_thermal/gal + capital + O&M

### Key service-level conversion factors validated:
- Heating oil: 137,000 BTU/gal × 0.85 AFUE = 0.0341 MWh thermal/gal
- Gas peaker heat rate: 10.8 MMBTU/MWh
- HP LCOH assumptions: 3-ton (10.5 kW), COP=2.8, 1,800 heating hrs/yr, 15-yr life
- BESS dispatch: 250 cycles/yr × 4hr × 0.85 RTE × 0.90 DOD = 0.765 MWh/kWh-cap/yr
