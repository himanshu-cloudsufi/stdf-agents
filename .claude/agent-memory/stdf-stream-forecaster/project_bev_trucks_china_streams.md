---
name: bev-trucks-china stream forecast results
description: Three-stream demand projections for BEV trucks displacing LNG/diesel in China — chimera peak year, stream ratios, CI widths, and key model parameters
type: project
---

BEV heavy truck disruption of China HDT market (900,000 units/yr) produces distinct three-stream commodity dynamics across lithium, copper, natural gas, and diesel.

**Why:** This case is the reference implementation for chimera hump-shape modeling in ground transport. LNG trucks are the canonical chimera — they rose from ~15% to ~29% share (2018–2024) then collapsed as BEV trucks surpassed TCO parity.

**How to apply:** Use these calibrated parameters and stream ratios as priors for any future heavy truck commodity disruption analysis.

---

## Key Model Parameters (BEV S-curve)
- L=0.90, k=0.7227, x0=2026.59 (R²=0.9950 from scurve-fitter)
- Chimera (LNG): L=0.999, k=0.80, x0=2020.0, C_peak=0.30

## Chimera Dynamics
- Model-derived peak: 2023.3 at 25.8% share (232,529 units)
- Observed 2024 LNG peak: ~29% — 3.2 pp gap; chimera S-curve slightly undershoots before BEV suppresses it
- By 2031 (+5yr): chimera collapses to 4.1% share (~37,000 units)
- Streams cross (LNG displacement > LNG chimera consumption): between 2026 and 2027

## Stream Outcomes by Commodity

### Lithium (kt LCE/yr)
| Year | Disruptor (incl. infra) | Incumbent | Chimera | Total |
|------|----------------------:|----------:|--------:|------:|
| 2026 | 100.52 | 0 | 0 | 100.52 |
| 2031 | 244.40 | 0 | 0 | 244.40 |
| 2036 | 254.20 | 0 | 0 | 254.20 |
| 2046 | 254.49 | 0 | 0 | 254.49 |
- Infrastructure (swap stations) = 10.9% of Li demand in 2026, ~10.9% at saturation
- Incumbent and chimera streams identically zero — LNG/diesel carry no traction batteries

### Copper (kt Cu/yr)
| Year | Disruptor | Incumbent | Chimera | Total |
|------|----------:|----------:|--------:|------:|
| 2026 | 32.07 | 11.21 | 4.74 | 48.02 |
| 2031 | 77.97 | 2.35 | 1.01 | 81.33 |
| 2036 | 81.10 | 1.75 | 0.75 | 83.60 |
| 2046 | 81.19 | 1.73 | 0.74 | 83.66 |
- All three streams non-zero (all powertrains use Cu)
- BEV intensity premium (100 vs 27.5 kg/unit) drives total upward monotonically

### Natural Gas/LNG (Mt/yr)
- 2026: Chimera consumption 2.07 Mt > Displacement 0.95 Mt (net +1.12 Mt)
- 2031: Chimera consumption 0.44 Mt < Displacement 2.31 Mt (net -1.87 Mt) — structural flip
- LNG fraction of BEV displacement: 24.7% (48,938 / 198,000 BEV units)

### Diesel (Mbbl/yr)
- Incumbent consumed: 16.65 (2026) → 2.57 (2046) — 84.6% collapse
- BEV displacement: 9.84 (2026) → 24.92 (2046)
- Diesel fraction: 75.3%

## Confidence Interval Widths
- Current year (+0yr): Very wide. Li P10–P90 spans 2.5× (62 to 154 kt) — near S-curve inflection
- +5yr: Narrow. Li P10–P90 spans ~15% (227 to 261 kt) — past inflection, trajectory determined
- +10yr/+20yr: Approximately same as +5yr — S-curve effectively saturated at L=90%

## Infrastructure Scaling
- Swap stations scale at 0.00303 stations/BEV unit (600/198,000)
- Each station: 50 CATL 75# blocks × 225.6 kg LCE = 11,280 kg LCE
- Infra adds ~10.9% to Li demand at all horizons (ratio constant with BEV fleet)
