# STDF Cost Parity Checker Agent — Oil and Gas Demand Disruption (Multi-Vector)

**Agent:** `stdf-cost-parity-checker` | **Confidence:** 0.69 (aggregate across 3 vectors)

**Analysis date:** 2026-03-20

---

## Agent Reasoning

This is a three-vector cost parity evaluation drawn entirely from `02b-cost-fitter.md`. The cost-fitter delivered structured competitive threshold determinations for each vector with explicit cost figures, fit parameters, and data quality flags. The agent's task is to read those outputs, apply the MET/NOT_MET/IMMINENT evaluation rules against the analysis date of 2026-03-20 (decimal year 2026.22), and produce a formal criterion 5.3 judgment.

**Vector 1 (EV vs ICE TCO):** The cost-fitter back-extrapolated the competitive threshold to 2020–2021, anchored on 2022–2024 direct Consumer Reports/Atlas observations showing EV at $0.65/mile vs ICE at $0.75/mile at first observation. Since the threshold midpoint (2020.5) is before the analysis date (2026.22), the status is MET. The threshold year carries ±1–2 year uncertainty — it was back-extrapolated from a 3-point fit, not directly observed. By 2024 the gap has widened further: EV $0.319/mile vs ICE $0.850/mile — EV is 62.5% below ICE. The primary learning rate anchor is the 10-point battery pack fit (R²=0.957), but the TCO threshold relies on a 3-point back-extrapolation fit, constraining confidence to the medium-low range (0.65). This is a market-driven disruption rooted in cost-curve dynamics, not policy effects.

**Vector 2 (Solar+BESS vs NGCC LCOE):** The competitive threshold was directly observed in 2023–2024 data — combined LCOE crossed from above ($83.7/MWh in 2022 during supply chain spike) to near parity ($74.2/MWh in 2023 vs NGCC $70/MWh) then firmly below ($70.0/MWh in 2024 vs NGCC $76/MWh). The threshold midpoint (2023.5) is before the analysis date. Status is MET. The BESS fit quality is high (R²=0.900, 6 points), and the 2024 observed crossover provides direct confirmation, yielding a high confidence score (0.82). The full-series solar LCOE fit (R²=0.756) is flagged low-confidence but is not the binding fit for the threshold determination. This disruption is driven by stellar energy cost-curve dynamics and BESS learning rates, not grid mandates.

**Vector 3 (Heat pump vs gas furnace):** The cost-fitter found no competitive threshold crossed and no crossing on any near-term forward cost trajectory under US average energy prices. Heat pump installed costs are rising (89% since 2010), the operating cost break-even electricity price ($0.088/kWh) is half the 2024 US residential average ($0.176/kWh), and the HP/gas cost ratio widened from 1.185 in 2010 to 1.985 in 2024. With no threshold on the forward cost curve within any reasonable analysis horizon, and the disruptor moving in the wrong cost direction, the status is NOT_MET with no horizon year. Confidence is limited by T3-only data and the absence of a learning curve, though the cost direction is unambiguous (0.60). This vector lacks the cost-curve dynamics that drive incumbent displacement in Vectors 1 and 2.

---

## Agent Output

### Cost Parity Condition — Multi-Vector Summary

| Vector | Disruptor | Incumbent | Status | Year/Range | Confidence |
|--------|-----------|-----------|--------|-----------|------------|
| V1: Transport | BEV TCO | ICE TCO | **MET** | 2020–2021 | medium (0.65) |
| V2: Power Generation | Solar PV + 4hr BESS LCOE | Natural gas CCGT LCOE | **MET** | 2023–2024 | high (0.82) |
| V3: Heating | Air source heat pump | Natural gas furnace | **NOT_MET** | No horizon year | low (0.60) |

**Multi-vector aggregate confidence: 0.69**

---

### Vector 1 — BEV vs ICE TCO

#### Cost Parity Condition
- **Status:** MET
- **Year/Range:** 2020–2021
- **Confidence:** medium (0.65)

#### Evidence
- **Disruptor current cost:** $0.319/mile BEV TCO (2024) [observed, Consumer Reports/Atlas]
- **Incumbent current cost:** $0.850/mile ICE TCO (2024) [observed, AAA catalog]
- **Cost gap:** EV is 62.5% below ICE as of 2024
- **Competitive threshold year:** 2020–2021 (back-extrapolated from 2022 anchor; uncertainty range ±1–2 yr, could be 2019–2022)
- **Cost at parity:** ~$0.70/mile
- **Primary exponential fit R-squared:** 0.957 (battery pack, 10-point, 2010–2024) — HIGH quality learning rate basis
- **TCO-direct fit R-squared:** 0.948 (BEV TCO, 3-point, 2022–2024) — directional confirmation only; 3-pt fit with limited statistical weight
- **Learning rate:** 16.45%/yr (battery pack, primary basis); 5.54%/yr (BEV TCO direct, low-confidence)
- **Incumbent trend:** ICE TCO rising at +$0.050/mile/yr (linear, structurally driven by fuel price, declining scale economies, aging fleet maintenance)

#### Inflection Assessment
- **Inflection threshold (70% of ICE):** Already entered — BEV at $0.319/mile is 37.5% of ICE, well within the disruption zone
- **Inflection threshold (50% of ICE):** Model-derived forward curve: ~2027 — disruptor at ~$0.425/mile = 50% of ~$0.90/mile ICE (model-derived, not an observed data point)
- **2024 position:** 37.5% of incumbent — disruptor is in deep disruption territory

---

### Vector 2 — Solar PV + BESS vs Natural Gas CCGT

#### Cost Parity Condition
- **Status:** MET
- **Year/Range:** 2023–2024
- **Confidence:** high (0.82)

#### Evidence
- **Disruptor current cost:** $70.0/MWh Solar+BESS combined LCOE (2024) [model-derived from observed IRENA solar $43/MWh + BESS at $255/kWh]
- **Incumbent current cost:** $76.0/MWh NGCC LCOE (2024) [observed, Lazard LCOE+ v17.0]
- **Cost gap:** Solar+BESS is 7.9% below NGCC as of 2024
- **Competitive threshold year:** 2023–2024 (confirmed by direct observed cost data)
- **Cost at parity:** ~$73/MWh
- **BESS fit R-squared:** 0.900 (6-point, 2019–2024) — HIGH quality
- **Solar LCOE fit R-squared:** 0.951 (early period 2009–2018, 9-pt) / 0.756 (full period — LOW CONFIDENCE FLAG)
- **Learning rates:** Solar PV 19.99%/yr (early phase); BESS 9.04%/yr
- **Incumbent trend:** NGCC rising at +$4.40/MWh/yr (2020–2024, R²=0.964) — structurally rising due to fuel price exposure, supply chain costs, and stranded fixed-cost effects from incumbent displacement by stellar energy
- **Note:** Solar PV alone crossed NGCC LCOE in 2016 ($55/MWh vs $63/MWh). The combined Solar+BESS threshold of 2023–2024 is the relevant service-level determination for dispatchable capacity comparison.

#### Inflection Assessment
- **Inflection threshold (70% of NGCC):** Model-derived forward curve: ~2028 — combined reaches ~$61–65/MWh = 66% of ~$93/MWh NGCC on current trajectory
- **Inflection threshold (50% of NGCC):** Beyond 2035 on current trajectory
- **2024 position:** 92.1% of incumbent ($70/$76) — recently crossed parity; gap widening on the forward cost curve

---

### Vector 3 — Heat Pump vs Natural Gas Furnace

#### Cost Parity Condition
- **Status:** NOT_MET
- **Year/Range:** No horizon year — threshold not crossed and no convergence on forward cost curve
- **Confidence:** low (0.60)

#### Evidence
- **Disruptor current cost:** $0.0776/kWh thermal (heat pump total, 2024) [model-derived: electricity $0.176/kWh ÷ COP 3.0 + capex amortization]
- **Incumbent current cost:** $0.0391/kWh thermal (gas furnace total, 2024) [model-derived: gas $0.82/therm ÷ (29.3 kWh_th/therm × AFUE 0.95) + capex amortization]
- **Cost gap:** Heat pump is 98.5% more expensive than gas furnace (ratio 1.985×) as of 2024
- **Competitive threshold year:** NOT REACHED — cost direction is adverse and widening
- **Break-even electricity price:** $0.088/kWh (operating cost only); $0.061/kWh (full TCO) — vs. current US average $0.176/kWh
- **Gap to break-even:** Electricity would need to fall to half of current US residential price for operating cost parity; full TCO parity requires a 65% decline
- **HP cost trend:** RISING — installed cost +89% since 2010 in nominal terms; no exponential decay applies; cost-curve dynamics absent for this vector
- **Gas furnace incumbent cost trend:** Structurally flat (R²=0.000) — mean-reverting US gas prices at ~$2–4/MMBTU Henry Hub

#### Inflection Assessment
- **Inflection threshold:** Not applicable — competitive threshold not crossed; cost ratio widening year over year
- **2024 position:** 198.5% of incumbent — disruptor is nearly 2× more expensive and the gap is growing
- **Regional caveat:** In markets with higher gas prices (Europe post-2021: $3–4/therm) AND lower electricity prices (Pacific NW: $0.11/kWh), operating cost parity approaches but has not been broadly observed in annual cost data; country-level or utility-level analysis required

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.3a | CRITICAL | PASS | Cost parity years extracted: V1 2020–2021 (back-extrapolated); V2 2023–2024 (observed); V3 NOT REACHED |
| 5.3b | CRITICAL | PASS | Status: V1 MET; V2 MET; V3 NOT_MET — all three explicitly stated |
| 5.3c | HIGH | PASS | V1: $0.319/mile BEV vs $0.850/mile ICE; V2: $70.0/MWh vs $76.0/MWh; V3: $0.0776 vs $0.0391/kWh_th |
| 5.3d | HIGH | PASS | All figures traced to 02b-cost-fitter.md Competitive Threshold, Disruptor Cost Trajectory, and Exponential Fit sections |
| 5.3e | MEDIUM | PASS | V1 0.65 (3-pt TCO fit, back-extrapolated threshold, battery pack R²=0.957); V2 0.82 (BESS R²=0.900 + observed 2024 crossover); V3 0.60 (T3 data only, no decay curve) |

---

### Data Gaps

1. **V1 threshold year uncertainty:** The 2020–2021 competitive threshold is back-extrapolated from 2022 observations, not directly observed. Uncertainty range ±1–2 years (true crossing could be 2019–2022). The 3-point BEV TCO fit anchors the back-extrapolation.
2. **V1 methodology gap:** Pre-2022 model-derived EV TCO uses China lowest vehicle prices; 2022–2024 direct observations use US market vehicles. The ~$0.20–0.30/mile gap reflects a market difference, not a learning curve inflection. The threshold year applies to China market conditions, not US market.
3. **V2 full-series solar fit is low confidence:** Full-period R²=0.756 (flagged LOW CONFIDENCE). This does not affect the threshold determination — the 2023–2024 crossover is established by direct observed data — but limits forward trajectory precision.
4. **V2 threshold is margin-thin:** Solar+BESS at $70.0/MWh vs NGCC at $76.0/MWh (7.9% gap) means a modest NGCC fuel-price decline (Henry Hub returning to $1.50–2.00/MMBTU) could temporarily reverse the crossover. The threshold is real but not deeply established.
5. **V3 US-average framing:** The NOT_MET determination is for US average energy prices. In specific markets (European gas prices $3–4/therm; Pacific NW electricity $0.11/kWh), partial operating-cost parity conditions may exist. A regional analysis would differentiate.
6. **V3 data quality:** All heat pump installed cost data is Tier 3 only (no catalog equivalent). Five anchor points 2010–2024. The rising direction is robust and confirmed by regulatory and refrigerant-change context; the precise slope is indicative only.

---

## Sources

- Upstream: `output/oil-gas-out​look/agents/02b-cost-fitter.md`
- All cost figures, fit parameters, and threshold determinations traced to cost-fitter sections: Competitive Threshold Summary, Disruptor Cost Trajectory tables, Exponential Fit subsections, and Incumbent Trend subsections for each vector
- No independent data collection performed — this agent is a synthesis/evaluation agent operating from upstream file data only
