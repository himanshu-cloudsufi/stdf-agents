---
name: bev-trucks-china-cost-fit
description: Validated exponential fit parameters, learning rates, per-km cost analysis, and threshold years for BEV heavy trucks vs. diesel incumbent in China (updated 2026-03-20, bev-trucks-china-2 run)
type: reference
---

## Validated Fit Parameters (bev-trucks-china-2, 2026-03-20)

### LFP Battery Pack — Long Series (Median China, 2010–2024)
- Formula: C(t) = 979.25 × exp(−0.1823 × (t − 2010)) USD/kWh
- R² = 0.976, 8 pts, 14-yr span
- Learning rate: 16.66%/yr (primary; highest-confidence rate)
- Validation (2024): model=76.3, actual=94 — 18.8% deviation; curve is flattening as LFP matures; use as historical rate, not forward rate

### LFP Battery Pack — E-Bus/Commercial Series (Rethinkx, 2018–2024)
- Formula: C(t) = 176.64 × exp(−0.1038 × (t − 2018)) USD/kWh
- R² = 0.803, 7 pts, 6-yr span
- Learning rate: 9.86%/yr
- Note: 2022 lithium carbonate spike preserved as real event; it depresses R²

### BEV HCV Purchase Price — T2 Catalog USD (2010–2024)
- Formula: C(t) = 264,777.65 × exp(−0.0596 × (t − 2010)) USD
- R² = 0.992, 9 pts, 14-yr span
- Learning rate: 5.79%/yr (conservative lower bound)
- Validation (2024): model=114,949, actual=110,000 — 4.5% deviation [PASS]
- Warning: T2 catalog covers broad commercial EV fleet — NOT 49t tractor specifically

### BEV 49t Tractor — T3 CNY (440 kWh, 2021–2024)
- Formula: C(t) = 946,550.67 × exp(−0.1015 × (t − 2021)) CNY
- R² = 0.753, 4 pts — LOW CONFIDENCE (below 0.80 threshold)
- Learning rate: 9.65%/yr (upper bound for recent price-war period)
- Validation (2024): model=698,074, actual=650,000 — 7.4% deviation [PASS]

## Incumbent Fit Parameters

### ICE Diesel Purchase Price (USD, 2010–2024)
- Model: linear_rising, slope = +2,000 USD/yr, R² = 1.000
- 2024 value: $68,000 USD = CNY 486,200
- Structural drivers: loss of scale economies as BEV share grows; rising China VI compliance costs; stranded ICE powertrain manufacturing investment

### Diesel Retail Fuel Price (2015–2024)
- Model: linear_rising, slope = +0.031 USD/L/yr, R² = 0.478 (low — commodity volatility)
- 2024 mean: $0.960 USD/L; CNY 7.47/L
- R² low due to commodity price cycles (2022 spike), not trend reversal

## Competitive Threshold Summary

### Purchase Price Parity
- **282 kWh BEV (short-haul):** Already crossed 2024 (CNY 400k vs ICE CNY 486k — 17.7% cheaper)
- **440 kWh BEV (long-haul, T3 model):** 2026–2027 (model-derived from T3 fit, R²=0.753)
- **Broad HCV fleet (T2 model, conservative):** 2029–2030 (model-derived from T2 fit, R²=0.992)

### Per-km Energy Cost Parity
- Already crossed before 2019; BEV has been 62–78% of diesel per-km energy cost throughout 2019–2024
- 2024 BEV advantage: 35.7% (CNY 1.44/km vs CNY 2.24/km)

### Inflection Threshold (50–70% of ICE price)
- 440 kWh purchase price: 2029–2032 (BEV at CNY 310k–380k vs ICE CNY 572k–600k)
- Per-km inflection: already past

## Per-km Parameters (2024 Baseline)
- BEV consumption: 2.0 kWh/km (heavy-duty tractor, ICCT literature)
- Diesel consumption: 0.30 L/km (30 L/100 km, heavy-duty)
- Electricity price midpoint: CNY 0.72/kWh (range: CNY 0.43–0.88 by region)
- Electricity price trend: +0.01 CNY/kWh/yr (slow rise, CEIC/NDRC)
- Diesel price trend: +0.031 USD/L/yr = +0.22 CNY/L/yr
- USD/CNY: 7.15 (2024)

## Key Gotchas
- T2 catalog BEV price is NOT 49t tractor specific — use T3 CNY transaction data for 440kWh tractor parity dates
- LFP battery median long-run fit overestimates recent cost decline speed (18.8% dev at 2024); the curve is flattening
- T3 fit R²=0.753 is LOW confidence — only valid as an upper bound for the recent price-war rate
- 282 kWh short-haul BEV already cheaper than ICE in 2024 (single observed data point, not a fit)
- Do not aggregate into TCO — present purchase price and per-km energy cost as separate vectors
