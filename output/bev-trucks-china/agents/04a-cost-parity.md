# STDF Cost Parity Checker Agent — BEV Heavy Trucks vs. LNG/NG Trucks (China)

**Agent:** `stdf-cost-parity-checker` | **Confidence:** 0.82

---

## Agent Reasoning

The cost-fitter output (`02b-cost-fitter.md`) delivers two distinct cost parity dimensions for this disruption: service-level TCO parity and purchase-price parity. On the primary service-level metric (CNY/km total cost of ownership), the BEV heavy tractor crossed below LNG TCO in **2019–2020** at normalized LNG fuel prices (CNY 4.3/kg), with the cost-fitter's 2020 model output placing BEV at 1.720 CNY/km vs. LNG at 1.800 CNY/km — a 4.4% BEV advantage that has since widened to −27.0% by 2024 (BEV 1.319 CNY/km vs. LNG 1.806 CNY/km). The TCO inflection — where the BEV advantage exceeded 15%, triggering self-reinforcing S-curve adoption dynamics — crossed in 2021–2022. On the secondary purchase-price metric, the cost-fitter identifies the crossover as occurring between 2024 and 2025 (model midpoint 2024.8), with 2024 observed data showing BEV at CNY 460,000 vs. LNG at CNY 420,000 — a 9.5% residual premium already inside the 10% range. Both dimensions independently support a MET determination.

Condition status is determined by applying the three-rule evaluation logic to the cost-fitter's competitive threshold outputs. The primary threshold — TCO service-level parity — was reached in 2019–2020, which is at or before the analysis date (2026-03-20), satisfying the MET criterion (threshold year <= analysis date and disruptor cost <= incumbent cost in service-level units). This is a market-driven disruption: cost-curve dynamics operating through LFP battery learning (16.70%/yr) and vehicle assembly scale are driving incumbent displacement of LNG and diesel tractors without reliance on subsidy or mandate — the cost-fitter notes BEV trucks reached 22% market share in H1 2025 at TCO levels already 27% below LNG. Confidence is set at 0.82, reflecting the HIGH-quality battery learning rate fit (R-squared = 0.957, 11 data points, 14-year span) that anchors the forward curve, partially offset by the upstream agent's overall confidence of 0.74 due to the 3-point CNY tractor price series and unquantified maintenance cost assumptions. Since cost parity has already been observed and confirmed in 2024 data, the condition determination does not rest on forward curve extrapolation.

---

## Agent Output

### Cost Parity Condition
- **Status:** MET
- **Year/Range:** 2019–2020 (TCO service-level, normalized fuel); 2024–2025 (purchase price)
- **Confidence:** high

### Evidence
- **Disruptor current cost:** 1.319 CNY/km [model-derived from observed 2024 inputs] (2024)
- **Incumbent current cost:** 1.806 CNY/km [model-derived from observed 2024 fuel/price inputs] (2024)
- **Cost gap:** −0.487 CNY/km; BEV is 27.0% cheaper than LNG on TCO basis
- **Competitive threshold year (TCO service-level):** 2019–2020 (from cost-fitter, `02b-cost-fitter.md`)
- **Competitive threshold year (purchase price):** 2024–2025 (from cost-fitter, `02b-cost-fitter.md`)
- **Exponential fit R-squared:** 0.957 (LFP battery long series — primary fit for TCO forward curve)
- **Learning rate:** 16.70%/yr (LFP battery, long series, R-squared = 0.957, 11 pts, 2010–2024)

### Secondary Purchase Price Evidence
- **BEV 49t tractor price 2024 (observed):** CNY 460,000 [T3 IEEFA]
- **LNG 49t tractor price 2024:** CNY 420,000 [T2/T3 catalog + web]
- **Purchase price gap 2024:** +CNY 40,000 (+9.5% BEV above LNG) — within 10% threshold
- **Purchase price parity crossover:** model-derived 2024.8 (late 2024 to early 2025)
- **Purchase price fit:** C(t) = 684,393 × exp(−0.1281 × (t − 2021)), R-squared = 0.993 [LOW-N: 3 pts — treat as indicative]

### Inflection Assessment
- **TCO inflection threshold year (>15% BEV advantage):** 2021–2022 (already passed)
- **Disruptor at TCO inflection:** ~1.51 CNY/km (2021) vs. LNG 1.864 CNY/km — BEV was −18.8% below LNG at inflection crossing
- **Purchase-price inflection (50–70% of LNG sticker):** 2028–2030 (curve-fitted from 3-pt tractor series; treat as directional)
- **2024 TCO status:** −27.0% BEV advantage over LNG — well past self-reinforcing adoption threshold

### TCO Crossover Summary (Service-Level CNY/km, from cost-fitter)

| Year | BEV TCO | LNG TCO | BEV vs LNG | Status |
|------|---------|---------|------------|--------|
| 2020 | 1.720 [model-derived] | 1.800 [model-derived] | −4.4% | **Parity MET** |
| 2021 | 1.513 [model-derived] | 1.864 [model-derived] | −18.8% | Past parity |
| 2022 | 1.475 [model-derived] | 2.652* [model-derived] | −44.4% | Past parity |
| 2023 | 1.388 [model-derived] | 2.229 [model-derived] | −37.7% | Past parity |
| 2024 | 1.319 [observed inputs] | 1.806 [observed inputs] | **−27.0%** | Past parity |

*2022 LNG TCO elevated by dual natural gas and input material price spike.

### Compliance Checklist
| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.3a | CRITICAL | PASS | Cost parity year extracted: 2019–2020 (TCO service-level); 2024–2025 (purchase price) |
| 5.3b | CRITICAL | PASS | Status: MET — TCO parity crossed 2019–2020, confirmed in 2024 observed data |
| 5.3c | HIGH | PASS | Disruptor 1.319 CNY/km vs. Incumbent 1.806 CNY/km (service-level TCO, 2024) |
| 5.3d | HIGH | PASS | All figures traced to `02b-cost-fitter.md` (TCO Crossover Summary, Competitive Threshold sections) |
| 5.3e | MEDIUM | PASS | R-squared = 0.957 (primary LFP long series, 11 data points) — HIGH confidence bracket |

### Data Gaps
1. **3-point CNY tractor price series.** The purchase-price parity determination (2024–2025) rests on only three T3 web data points (2021, 2023, 2024). The R-squared of 0.993 is spuriously high for a 3-point fit. This does not affect the TCO parity MET determination (which is independent), but the purchase-price crossover year should be treated as indicative with ±1-year uncertainty.
2. **Maintenance cost assumptions unverified.** BEV maintenance (CNY 0.05/km) and LNG maintenance (CNY 0.08/km) are point estimates from the upstream; ±20% on BEV maintenance shifts TCO advantage by approximately ±0.01 CNY/km. Even at the upper bound, BEV TCO advantage remains large enough that the MET determination is robust.
3. **Fuel price sensitivity.** TCO parity year (2019–2020) is computed at normalized LNG fuel of CNY 4.3/kg. At the 2020 trough price (CNY 3.25/kg), LNG TCO was ~1.44 CNY/km — briefly below BEV. The MET determination reflects the normalized-fuel basis used consistently by the cost-fitter.
4. **Battery swap economics not integrated.** Swap-model BEV trucks (29,569 units in 2024) have structurally different TCO profiles; cost-fitter flagged absence of time-series data for this sub-segment.

---

## Sources
- Upstream: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/bev-trucks-china/agents/02b-cost-fitter.md`
  - TCO Crossover Summary table (service-level, CNY/km)
  - Competitive Threshold section (purchase price parity: 2024–2025)
  - Inflection Threshold section (TCO inflection: 2021–2022; purchase price inflection: 2028–2030)
  - Exponential Fit — LFP Battery Pack (Long Series): R-squared = 0.957, 11 pts
  - Learning Rates table: 16.70%/yr (long series), confirmed primary rate
