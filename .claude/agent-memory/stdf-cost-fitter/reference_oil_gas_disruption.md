---
name: oil-gas-disruption-cost-fit
description: Validated exponential fit parameters, learning rates, unit conversions, and threshold years for three-vector oil and gas demand disruption analysis (2026-03-20)
type: reference
---

## Analysis Context

Three simultaneous disruption vectors attacking oil and gas demand. Analysis date 2026-03-20.

---

## Vector 1: Transport — BEV vs ICE ($/mile TCO)

### Li-Ion Battery Pack (Primary Learning Rate Basis)
- Formula: C(t) = 1,240.13 × exp(−0.1797 × (t − 2010)) $/kWh_capacity
- R² = 0.957, 10 pts, 14-yr span (2010–2024)
- Learning rate: **16.45%/yr**
- Validation 2024: model=$100.2 vs. actual=$115 (12.9% — acceptable, 2022 spike distortion)

### EV Vehicle Price Fits (hardware, not service-level)
- China lowest: C(t) = 47,040 × exp(−0.1204 × (t − 2013)), R²=0.865, 9 pts
  - Learning rate: 11.34%/yr
- USA median: C(t) = 53,407 × exp(−0.0396 × (t − 2010)), R²=0.988, 7 pts
  - Learning rate: 3.88%/yr

### BEV TCO Fit (direct observations, short series)
- C(t) = 0.65 × exp(−0.0570 × (t − 2022)), R²=0.948, 3 pts only
- Learning rate: 5.54%/yr — LOW CONFIDENCE (3-point fit)

### ICE TCO Incumbent
- linear_rising, slope=+$0.05/mile/yr, R²=1.00 (3 collinear points)

### Thresholds
- Competitive threshold (EV TCO = ICE TCO): **2020–2021** (back-extrapolated from 2022 observations)
- Inflection threshold: **ALREADY IN RANGE** at 68.2% of ICE in 2024
- 50% inflection: ~2027

### TCO Reconstruction Methodology (AAA-comparable)
- Annual mileage: 15,000 miles/yr; lifetime: 10yr/150,000 miles
- Depreciation: 50% of purchase price over lifetime
- Fixed annual overhead: $3,000 (finance + insurance + registration)
- EV energy: $0.176/kWh × 0.30 kWh/mile = $0.053/mile
- EV maintenance: $500/yr; ICE maintenance: $1,000/yr
- ICE fuel: 30 MPG at catalog gas prices (EIA, $/gallon)

---

## Vector 2: Power Generation — Solar PV + BESS vs NGCC ($/MWh LCOE)

### Solar PV LCOE — Early Period (Primary)
- C(t) = 269.70 × exp(−0.2230 × (t − 2009)) $/MWh
- R² = 0.9506, 9 pts, 2009–2018
- Learning rate: **19.99%/yr**

### Solar PV LCOE — Full Period (Low Confidence)
- C(t) = 175.55 × exp(−0.1228 × (t − 2009)) $/MWh
- R² = 0.7556 — BELOW 0.80 THRESHOLD
- Learning rate: 11.56%/yr
- Cause of low R²: plateau effect 2018–2024 ($36–50/MWh range, no clear trend)

### BESS 4-Hour Turnkey
- C(t) = 407.83 × exp(−0.0948 × (t − 2019)) $/kWh
- R² = 0.9001, 6 pts, 2019–2024
- Learning rate: **9.04%/yr**
- Validation 2024: model=$253.9 vs. actual=$255 (0.4% — excellent)

### BESS Blended Addition Methodology
- BESS $/kWh_cap → $/MWh dispatched: (BESS × 1000) / (350 cycles × 15yr × 0.90 RTE × 0.80 DOD)
- Blended addition = cost_per_MWh_stored × 0.40 storage fraction
- 2024 result: $255/kWh → $27.0/MWh blended addition

### NGCC Incumbent
- Full period (2009–2024): flat, slope=−$0.55/yr, R²=0.094 (two opposing regimes)
- Recent period (2020–2024): linear_rising, slope=+$4.40/yr, R²=0.964
- Use RECENT period for forward analysis

### Thresholds
- Solar alone vs. NGCC: **2015–2016** ($55/MWh solar vs. $63/MWh NGCC)
- Solar+BESS combined vs. NGCC: **2023–2024** (combined $70 vs. NGCC $76)
- 70% inflection threshold: ~2028 (combined ~$61–65/MWh = 66% of NGCC ~$93/MWh)
- 50% inflection: beyond 2035 at current trajectory

---

## Vector 3: Heating — Heat Pump vs Gas Furnace ($/kWh thermal)

### Key Finding: Cost-Curve Disruption Mechanism Absent
- ASHP installed costs RISING: $4,500 (2010) → $8,500 (2024), +89% nominal
- Disruptor trend: linear_rising, slope=+$0.0019/kWh_th/yr, R²=0.864
- No exponential decay fit applicable

### Service-Level Conversion
- HP: electricity price ($/kWh) / COP (3.0) = $/kWh_th operating
- Gas: gas price ($/therm) / (29.3 kWh_th/therm × AFUE 0.95) = $/kWh_th operating
- Gas residential price = Henry Hub $/MMBTU / 10 + $0.60/therm delivery
- Annual thermal output: 30,000 kWh_th/yr

### 2024 US Avg Costs
- HP total: $0.0776/kWh_th
- Gas total: $0.0391/kWh_th
- Ratio: 1.985 (HP is 2x gas)

### Break-Even Conditions
- Operating parity requires electricity ≤ $0.088/kWh (vs. current $0.176/kWh)
- Full TCO parity requires electricity ≤ $0.061/kWh

### Threshold
- **NOT REACHED** under any observed US market conditions
- Even 2022 gas spike ($1.245/therm) did not produce parity

---

## Cross-Vector Notes

### Fit Quality Patterns
- Battery/BESS data: clean exponential fits (R²=0.90–0.96) despite 2022 lithium spike
- Solar LCOE: steep-then-plateau pattern causes low full-series R² (0.756); split-period analysis required
- TCO series: very short (3 pts); only directional use possible
- Incumbent: ICE rising (collinear 3pts), NGCC two-regime (use recent period)

### Banned Language (pre-write hook blocks)
- "projected/projection" → use "model-derived" or "forward curve"
- "transition" → use "disruption" or "structural shift"
- "outlook" → use "analysis" or "forward curve"
