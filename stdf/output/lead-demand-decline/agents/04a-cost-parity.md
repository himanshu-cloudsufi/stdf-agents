# STDF Cost Parity Checker Agent — Lead Demand Decline (Li-Ion vs. Lead-Acid)

**Agent:** `stdf-cost-parity-checker` | **Confidence:** 0.87

---

## Agent Reasoning

The cost-fitter's output identifies three structurally distinct cost comparison segments within this Li-ion vs. lead-acid disruption, each requiring its own condition evaluation. On a service-level ($/kWh delivered) basis, Li-ion was already cheaper than lead-acid before the data series begins in 2010: model C0 for Li-ion service-level cost is $0.54/kWh_del at 2010 versus lead-acid USA at $1.60/kWh_del and China at $1.33/kWh_del. This parity predates 2010 and the condition is unambiguously MET — cost-curve dynamics governing this chemistry have been decisive for over a decade. On a nameplate ($/kWh pack hardware) basis, parity was reached in 2019–2020 for USA and 2020–2021 for China — both BEFORE the analysis date of 2026-03-20. For the SLI automotive segment — the structurally most important segment at 62.5% of global lead demand — the picture is materially different: Li-ion SLI unit cost stands at $100/battery (China) and $135/battery (USA) in 2024 against lead-acid targets of $25 (China) and $55 (USA), a 4x and 2.5x premium respectively. The cost-fitter's SLI exponential fit (R²=0.990, 8 data points) places SLI parity at 2027–2028 for USA and 2031–2032 for China.

The overall condition status for criterion 5.3 is therefore segment-dependent. This report adopts a PRIMARY / SECONDARY structure: the primary evaluation uses nameplate pack cost (the canonical STDF hardware parity measure, consistent with the cost-fitter's "Competitive Threshold" section); secondary evaluations cover service-level and SLI separately. Nameplate parity for both USA and China is MET. SLI parity is NOT_MET, with USA flagged IMMINENT within a 2-year window (2027–2028, which is 1.5–2.5 years from analysis date). Confidence is inherited from the cost-fitter at 0.87, reflecting the high R² (0.954) and 15-point data series moderated by the 18% terminal deviation at 2024.

---

## Agent Output

### Cost Parity Condition — Segment Summary

| Segment | Unit | Status | Parity Year | Current Disruptor Cost | Current Incumbent Cost |
|---------|------|--------|-------------|----------------------|----------------------|
| Service-level (stationary/motive) — USA | $/kWh_del | **MET** | Pre-2010 | $0.050/kWh_del (2024) | $0.960/kWh_del (2023) |
| Service-level (stationary/motive) — China | $/kWh_del | **MET** | Pre-2010 | $0.050/kWh_del (2024) | $0.747/kWh_del (2023) |
| Nameplate pack cost — USA | $/kWh_cap | **MET** | 2019–2020 | $115/kWh (2024) | $228.6/kWh (mean) |
| Nameplate pack cost — China | $/kWh_cap | **MET** | 2020–2021 | $115/kWh (2024) | $186.9/kWh (mean) |
| SLI automotive unit cost — USA | $/battery | **IMMINENT** | 2027–2028 | $135/battery (2024) | $55/battery (2024) |
| SLI automotive unit cost — China | $/battery | **NOT_MET** | 2031–2032 | $100/battery (2024) | $25/battery (2024) |

### Primary Cost Parity Condition (Nameplate Pack Cost)
- **Status:** MET
- **Year/Range:** 2019–2020 (USA); 2020–2021 (China)
- **Confidence:** high

### SLI Automotive Cost Parity Condition (62.5% of Lead Demand)
- **Status:** IMMINENT (USA) / NOT_MET (China)
- **Year/Range:** 2027–2028 (USA); 2031–2032 (China)
- **Confidence:** high

---

### Evidence

**Service-Level Parity (Pre-2010, MET)**
- **Disruptor current cost:** $0.050/kWh_del (Li-ion LFP, 2024) [model-derived from observed $115/kWh nameplate via 3,000 cycles × 80% DoD × 96% RTE conversion]
- **Incumbent current cost:** $0.960/kWh_del (lead-acid USA, 2023) / $0.747/kWh_del (China, 2023) [model-derived from observed nameplate via 500 cycles × 50% DoD × 75% RTE]
- **Cost gap:** Li-ion is 5.2% of lead-acid USA service-level cost; 6.7% of China — a 19x and 15x advantage respectively
- **Competitive threshold year:** Pre-2010 (from cost-fitter: "levelized parity predates 2010")

**Nameplate Parity (2019–2020 USA / 2020–2021 China, MET)**
- **Disruptor current cost:** $115/kWh nameplate (Li-ion global median, 2024) [observed, T2]
- **Incumbent current cost:** $228.6/kWh nameplate USA mean / $186.9/kWh China mean [observed, T2]
- **Cost gap:** Li-ion is 50.3% of lead-acid USA nameplate cost (49.7% cheaper); 61.5% of China nameplate cost (38.5% cheaper)
- **Competitive threshold year:** 2019–2020 (USA), 2020–2021 (China) (from cost-fitter Competitive Threshold table)
- **Exponential fit R-squared:** 0.9541 (primary fit, 15 data points, 2010–2024)
- **Learning rate:** 16.81% per year (from r=0.1841, formula: (1 − exp(−r)) × 100)

**SLI Automotive Parity (2027–2028 USA / 2031–2032 China, IMMINENT/NOT_MET)**
- **Disruptor current cost:** $135/battery USA / $100/battery China (Li-ion 12V 60Ah SLI, 2024) [observed, T2]
- **Incumbent current cost:** $55/battery USA / $25/battery China (lead-acid 12V 60Ah SLI, 2024) [observed, T2]
- **Cost gap:** USA: $80/battery excess (Li-ion at 245% of incumbent, 145% premium); China: $75/battery excess (Li-ion at 400% of incumbent, 300% premium)
- **Competitive threshold year:** 2027–2028 (USA), 2031–2032 (China) (from cost-fitter SLI table)
- **SLI exponential fit R-squared:** 0.9897 (8 data points, 2010–2024)
- **SLI learning rate:** 14.84% per year (from r=0.1608)

---

### Inflection Assessment

**Service-Level ($/kWh delivered):**
- **Inflection threshold year:** Pre-2010 (50–70% of incumbent cost reached before data series begins)
- **Status:** Inflection concluded; incumbent displacement is now governed by installed-base replacement rates and channel economics, not cost competitiveness

**Nameplate ($/kWh pack):**
- **Inflection threshold year:** 2021–2023 (USA); 2022–2025 (China)
- **Disruptor at inflection:** $114–$160/kWh (50–70% of USA mean $228.6/kWh); $93–$131/kWh (50–70% of China mean $186.9/kWh)
- **Current position:** Li-ion at $115/kWh (2024) is at the lower bound of the USA inflection zone (50.3% of incumbent) — well within and exiting the zone toward full parity

**SLI ($/battery):**
- **Inflection threshold year:** 2029–2032 (USA, target: $27.50–$38.50/battery); 2034–2037 (China, target: $12.50–$17.50/battery)
- **Current position:** USA Li-ion SLI at $135 = 245% of incumbent; China at $100 = 400% of incumbent — inflection zone not yet reached in either market

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.3a | CRITICAL | PASS | Cost parity year extracted: 2019–2020 (USA nameplate), 2020–2021 (China nameplate), 2027–2028 (SLI USA), 2031–2032 (SLI China) |
| 5.3b | CRITICAL | PASS | Status: MET (service-level and nameplate); IMMINENT (SLI USA); NOT_MET (SLI China) |
| 5.3c | HIGH | PASS | Disruptor $0.050/kWh_del vs Incumbent $0.960/kWh_del (service-level); $115/kWh vs $228.6/kWh (nameplate); $135 vs $55/battery (SLI USA) |
| 5.3d | HIGH | PASS | All figures traced to 02b-cost-fitter.md (Competitive Threshold table, SLI table, Disruptor/Incumbent trajectory tables) |
| 5.3e | MEDIUM | PASS | R-squared = 0.9541 (15 data points, primary fit); SLI fit R² = 0.9897 (8 data points); confidence 0.87 reflects terminal deviation flag |

**Overall: COMPLIANT**

---

### Data Gaps

1. **Terminal deviation at 2024: 18%.** The cost-fitter's primary exponential model computes $94.3/kWh vs observed $115/kWh at 2024 — an 18% deviation above the 15% flag threshold. Forward cost projections (particularly SLI parity timelines) carry widening uncertainty beyond 2026. SLI parity years carry ±2 year uncertainty per cost-fitter notation.
2. **SLI segment is 62.5% of global lead demand.** Despite nameplate pack cost parity being MET, the dominant lead consumption channel remains cost-incompetitive for Li-ion. The condition MET result for criterion 5.3 (primary) does not imply demand displacement has materialized — SLI unit economics remain the binding constraint on actual lead demand reduction.
3. **Lead-acid 2024 cost is model-derived.** The catalog lead-acid series terminates at 2023 (observed). The 2024 incumbent cost figures used in gap computations are extrapolated from the cost-fitter's linear declining trend ($180/kWh_cap USA, $140/kWh_cap China in 2023 as last observed points).
4. **Levelized cost conversion parameters are T3.** The 3,000-cycle LFP and 500-cycle lead-acid parameters are T3 benchmarks (PowerTech Systems). No T1 or T2 source provides a historical time series of $/kWh delivered for either chemistry.
5. **No experience-curve learning rate.** Cumulative deployment data is absent; the 16.81%/yr rate is time-series derived, not cost-vs-GWh experience curve derived.

---

## Sources

- Upstream: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/lead-demand-decline/agents/02b-cost-fitter.md`
- Figures: cost-fitter Competitive Threshold (Cost Parity) section, SLI Automotive table, Disruptor Cost Trajectory table, Incumbent Cost Trajectory table, Exponential Fit sections, Inflection Threshold section
- Computation: `lib.tipping_math.check_tipping_conditions` (cost_parity_year inputs: 2019.19, 2020.28, 2027.5, 2031.5) — all returning `cost_parity.met = True` for their respective parity year; status labels (MET/IMMINENT/NOT_MET) applied per criterion 5.3 evaluation rules against analysis date 2026-03-20
