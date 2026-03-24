# STDF v2 Disruption Analysis: Oil and Gas Demand — Multi-Vector

**Sector:** Oil and Gas | **Framework:** STDF v2 | **Date:** 2026-03-20
**Pipeline Confidence:** 0.383 | **Rupture Window:** 2027–2028 (V1+V2 composite)

---

## Executive Summary

Three simultaneous disruption vectors attack oil and gas demand from different angles: V1 (BEV displacing ICE in road transport), V2 (solar PV + BESS displacing gas in power generation), and V3 (heat pumps displacing gas in heating). Cost parity has been reached for V1 (2020–2021) and V2 (2023–2024); V3 remains below cost-parity threshold under US average energy prices. Capability sufficiency is PARTIAL for V1 and V2 (both model-derived full parity 2027–2028), and NOT MET for V3 gross-ducted retrofit. The composite tipping window is 2027–2028, driven by capability parity as the binding constraint for both V1 and V2 (tipping-synthesizer, confidence 0.75). Oil demand has reached structural peak in 2024–2026; gas demand peaks later at 2030–2032 net total as solar displacement of power-sector gas is partially offset by structural floor growth. Pipeline confidence is 0.383 — materially degraded by two missing agents: fleet-modeler (MEDIUM, −0.10) and regional-demand-analyst (HIGH, −0.30).

---

## 7-Phase Narrative

### Phase 1 — Sector Scoping

**Sector boundary:** Global oil and natural gas demand across all end-use sectors. Total addressable commodity volumes: oil at 103.4 mb/d (2024, observed, BP Statistical Review 2024) and natural gas at 4,103 bcm/yr (2023, observed, BP Statistical Review 2024).

**Sub-domains identified** (domain-disruption, confidence 0.82):
- Road transport petroleum (V1 disruption front)
- Electric power generation gas (V2 disruption front)
- Residential and commercial space heating gas (V3 disruption front)
- Structural floor demand: aviation jet fuel, marine bunker, petrochemical feedstock, industrial process gas, LNG fuel use

**Primary disruptors:** Battery electric vehicles (BEV) — V1; Solar PV + BESS (stellar energy) — V2; Air-source heat pumps (ASHP) — V3.

**Primary incumbents:** ICE passenger vehicles, diesel heavy trucks — V1; CCGT and OCGT gas turbines — V2; Natural gas boilers and furnaces — V3.

**Disruption-eligible demand** (demand-decomposer, confidence 0.80): 49.0 mb/d of oil (47.4% of total) and 2,378 bcm/yr of gas (58.0% of total) face viable incumbent displacement within a 15-year horizon. The remaining 54.4 mb/d oil and 1,725 bcm gas are structural floor demand (aviation, marine, petrochemicals, industrial process gas) with no disruptor vector within this analysis horizon.

---

### Phase 2 — Technology Inventory

**V1 — BEV vs. ICE petroleum:**
- BEV TCO: $0.58/mile (2024, observed, cost-researcher); ICE TCO: $0.85/mile (2024, observed, cost-researcher) — BEV at 68.2% of ICE, parity already surpassed (cost-fitter)
- Battery pack learning rate: 16.45%/yr (R²=0.9574, 10 data points 2010–2024; cost-fitter); C(t) = 1,240.13 × exp(−0.1797 × (t−2010)) $/kWh
- Global BEV sales: 11.0M (2024, observed); EV all-types share of new car sales: 23.89% (2024, observed, scurve-fitter)
- Global ICE passenger car oil demand: 24.3 mb/d (2024, observed, demand-decomposer); ICE intensity: 11.32 bbl/vehicle-year (model-derived, demand-decomposer)

**V2 — Solar PV + BESS vs. gas power generation:**
- Solar LCOE: $43/MWh (2024, observed, cost-researcher); NGCC LCOE: $76/MWh (2024, observed, cost-researcher, Lazard v17.0)
- Solar early-period learning rate: 19.99%/yr (R²=0.9506; cost-fitter); BESS learning rate: 9.04%/yr (R²=0.9001; cost-fitter)
- Solar generation share: 6.92% of global electricity (2024, observed, scurve-fitter); BESS installed capacity: 370,112 MWh globally (2024, observed, scurve-fitter)
- NGCC gas intensity: 0.1841 bcm/TWh; OCGT gas intensity: 0.2633 bcm/TWh (model-derived, demand-decomposer)
- Gas power sector demand: CCGT 1,230 bcm + OCGT 410 bcm = 1,640 bcm/yr total (2024, observed, demand-decomposer)

**V3 — ASHP vs. gas heating:**
- ASHP installed cost: ~$8,500 (2024, observed, cost-researcher); gas furnace installed: ~$5,800 (2024, observed, cost-researcher)
- HP upfront cost ratio: 1.985× vs. ≤3.0× threshold — cost parity NOT MET; electricity break-even $0.088/kWh vs. actual $0.176/kWh (US average; cost-fitter)
- Gas heating demand: residential 574 bcm + commercial 164 bcm = 738 bcm/yr total (2024, observed, demand-decomposer)
- EU heat pump share of new heating installations: 24.0% (2023, observed, EHPA; scurve-fitter); global HP stock share: ~10% (2024, observed, Ember; scurve-fitter)

---

### Phase 3 — Convergence Analysis

**V1 convergence — sequential (domain-disruption):**
Battery pack cost decline (16.45%/yr) drives TCO parity first, enabling mass-market BEV penetration, which drives further battery cost reduction through volume. The cost-fitter competitive threshold for V1 was back-extrapolated to 2020–2021 (BEV at 68.2% of ICE TCO by 2024). The inflection threshold (~50% of competitive threshold) is modeled at approximately 2027 (cost-fitter). V1 convergence is market-driven disruption — lower per-mile TCO, not mandate compliance.

**V2 convergence — sequential with cross-vector amplification (domain-disruption + tipping-synthesizer):**
Solar LCOE ($43/MWh) crossed below NGCC LCOE ($76/MWh) in 2023–2024, creating a 43.4% cost advantage. The cost-fitter identified NGCC LCOE rising at +$4.40/MWh/yr (R²=0.9644, 2020–2024) — widening the cost gap. BESS cost decline (9.04%/yr) enables the dispatchability extension that closes the remaining capability gap. Critical cross-vector amplification: V1 battery supply chain subsidizes V2 BESS cost decline by an estimated 1–2 years of acceleration (tipping-synthesizer).

**V3 convergence — divergent (domain-disruption + cost-fitter):**
V3 is a divergent convergence case — ASHP cost is NOT declining (heat pump costs rising in 2024), while US natural gas prices ($2.19/MMBtu, 2024) are extremely low. The cost-fitter calculates a gross break-even electricity price of $0.088/kWh versus actual $0.176/kWh — a 2.0× gap. Under European gas prices ($10.89/MMBtu), V3 reaches cost parity, explaining the structural EU vs. USA divergence in adoption rates. V3 is not driven by capital cost-curve dynamics; it is driven purely by operating-cost advantage in high-gas-price markets.

**V2 inflection note — scurve-fitter vs. tipping-synthesizer discrepancy (resolved):** The tipping-synthesizer used provisional parameters (L=85, k=0.30, x0=2027.5) based on solar share of new capacity additions. The scurve-fitter authoritative parameters use solar generation share (L=45, k=0.2279, x0=2031.6). Per conflict resolution protocol (granular specialist over generalist), the scurve-fitter parameters are authoritative for downstream projections. The tipping year of 2027–2028 from the tipping-synthesizer remains valid — it is based on capability parity, not the S-curve inflection year.

---

### Phase 4 — Disruption Pattern

**V1 disruption type:** Market-driven S-curve displacement with positive feedback loop. BEV cost-curve dynamics (battery learning rate 16.45%/yr) are self-reinforcing — more sales drive lower costs, lower costs drive more sales. This is the canonical S-curve disruption pattern with a steep k=0.4281 (scurve-fitter), consistent with the battery learning rate.

**V1 capability status** (capability, confidence 0.82; capability-parity-checker, confidence 0.81):
- 7 of 9 capability dimensions MET (capability agent)
- Residual gaps: fleet-average TCO (model parity 2026–2027) and cold-weather range (model parity 2027)
- Status: PARTIAL — capability parity year 2027 (capability-parity-checker)

**V2 disruption type:** Cost-floor disruption of the power sector merit order. Solar+BESS does not need to compete on all capability dimensions simultaneously — it enters via economic dispatch (lowest LCOE first), progressively pushing gas generation to the margin, then off the grid entirely. OCGT peakers are most acutely exposed (first displaced as BESS achieves 4–6 hour duration).

**V2 capability status** (capability, confidence 0.82; capability-parity-checker, confidence 0.81):
- 9 of 10 scoreable dimensions MET
- Residual gap: dispatchability index at 70% vs. 80% threshold (model parity 2027–2028)
- Status: PARTIAL — capability parity year 2027–2028 (capability-parity-checker)

**V3 disruption type:** Niche beachhead disruption — ASHP achieves cost-parity under high-gas-price conditions (Europe), but cannot penetrate the largest markets (USA, China cold-climate) due to upfront cost barrier and infrastructure constraints. V3 is NOT a full-market disruption within the analysis horizon; it is a partial-market disruption in price-favorable geographies.

**V3 capability status** (capability, confidence 0.82; capability-parity-checker, confidence 0.81):
- Upfront cost ratio: 5.0× vs. <3.0× threshold — NOT MET (gross ducted retrofit)
- Ducted retrofit complexity: 3.5/5 vs. ≤2.5/5 — NOT MET, no trajectory
- Model-derived gross parity: 2036–2043 (capability agent); lib calculation 2043 (capability-parity-checker; discrepancy documented, prefer lib value)
- Status: NOT MET (gross ducted) / PARTIAL (ductless + subsidy pathway)

---

### Phase 5 — Business Model Shift

**V1 cost parity crossing** (cost-parity-checker, confidence 0.65 for V1):
Cost parity MET in 2020–2021 (back-extrapolated). By 2024, BEV TCO = $0.58/mile vs. ICE $0.85/mile — a 31.8% BEV advantage. The business model implication is direct: fleet operators, ride-hail companies, and price-sensitive consumers face a compelling economic case for BEV over ICE in markets with sufficient charging infrastructure. ICE vehicle residual value erosion is already underway, suppressing new ICE demand further.

**V2 cost parity crossing** (cost-parity-checker, confidence 0.82 for V2):
Cost parity MET in 2023–2024. Solar LCOE $43/MWh vs. NGCC $76/MWh — a 43.4% solar advantage with the gap widening (NGCC rising at +$4.40/MWh/yr). The business model implication for power generators is existential: new gas capacity investment is economically irrational in all markets where solar+BESS installation is feasible. The 2,300 GW US interconnection queue (adopt-readiness) represents latent solar+BESS demand currently bottlenecked by grid infrastructure, not economics.

**V3 cost parity status** (cost-parity-checker, confidence 0.60 for V3):
NOT MET under US average energy prices. Heat pump cost ratio 1.985× in 2024, widening. Business model implication: ASHP adoption in the USA remains economically marginal for most households without subsidies. European markets (gas at $10.89/MMBtu) represent the economic frontier; US gas markets ($2.19/MMBtu) create a persistent cost barrier that suppresses V3 market-driven disruption in North America.

**Integrated tipping conditions** (tipping-synthesizer, confidence 0.75):

| Vector | Cost Parity | Capability Parity | Adoption Readiness | Tipping Year | Binding Constraint |
|--------|------------|------------------|-------------------|-------------|-------------------|
| V1 (BEV vs. ICE) | MET (2020–2021) | PARTIAL → 2027 | PARTIAL → 2026 | **2027** | capability_parity |
| V2 (Solar vs. gas) | MET (2023–2024) | PARTIAL → 2027–2028 | PARTIAL → 2027 | **2027–2028** | capability_parity |
| V3 (ASHP vs. gas) | NOT_MET | NOT_MET | NOT_MET | **CONTINGENT 2035–2043** | cost_parity |

**Post-tipping dynamics** (tipping-synthesizer):
- V1 post-tipping: ICE death spiral activates as EV volume drives battery cost below the point where any new ICE vehicle can offer competitive TCO. New car sales 80% BEV by 2031–2034; 54,000 EU auto sector jobs already cut in 2024 (xcurve-analyst); 121 of 465 global refineries at closure risk (xcurve-analyst).
- V2 post-tipping: Gas power virtuous cycle of solar+BESS — lower BESS costs extend dispatchability, displacing more gas, generating more revenue, funding further BESS deployment. OCGT gas demand collapses 98% from 2024 levels by 2046 (stream-forecaster, model-derived).
- V3 post-tipping: CONTINGENT — only triggers if US gas price rises above $0.088/kWh electricity break-even equivalent or upfront cost falls below 3.0× ratio. Not assigned within primary analysis horizon.

#### Commodity Demand Impact

Oil and gas demand follows three simultaneous streams with no disruptor stream — BEV, solar+BESS, and ASHP consume zero petroleum or gas directly (stream-forecaster, confidence 0.77):

**Oil demand trajectory** (stream-forecaster + demand-decomposer):
- Peak oil: 2024–2026 (model-derived, demand-decomposer); structural floor growth offset by BEV fleet disruption from 2025
- Total oil demand: 99.6 mb/d (2026) → 87.7 mb/d (2031) → 75.8 mb/d (2036) → 73.0 mb/d (2046)
- Monte Carlo P10/P90 at +20yr: 65.8–80.4 mb/d (stream-forecaster, N=300)
- PHEV chimera peak: 4.2 mb/d in 2031, declining to 1.4 mb/d by 2046
- Structural floor: 54.4 mb/d (2024) growing to ~60.7 mb/d (2046) — 74% of 2046 total

| Oil Stream | 2026 | 2031 | 2036 | 2046 |
|-----------|------|------|------|------|
| Incumbent ICE (mb/d) | 97.4 | 83.4 | 73.0 | 71.6 |
| Disruptor BEV (mb/d) | 0.0 | 0.0 | 0.0 | 0.0 |
| Chimera PHEV (mb/d) | 2.1 | 4.2 | 2.8 | 1.4 |
| **Total** | **99.6** | **87.7** | **75.8** | **73.0** |

**Gas demand trajectory** (stream-forecaster + demand-decomposer):
- Gas demand structural peak in disruption-eligible segments: 2024–2026; net total peaks 2030–2032 as floor growth offsets early disruption
- Total gas demand: 3,935 bcm (2026) → 3,497 bcm (2031) → 2,920 bcm (2036) → 2,601 bcm (2046) — a 33.9% reduction
- Monte Carlo P10/P90 at +20yr: 2,390–2,860 bcm (stream-forecaster, N=300)
- OCGT peakers: 410 bcm (2024) → 9 bcm (2046) — 98% collapse (stream-forecaster, model-derived)
- Gas chimera (dual-fuel heating + gas+solar hybrid): negligible peak of 36 bcm in 2030–2031 (<1% of total)

| Gas Stream | 2026 | 2031 | 2036 | 2046 |
|-----------|------|------|------|------|
| Incumbent CCGT/OCGT/Heat (bcm) | 3,913 | 3,462 | 2,898 | 2,596 |
| Disruptor solar/ASHP (bcm) | 0 | 0 | 0 | 0 |
| Chimera hybrids/dual-fuel (bcm) | 22 | 35 | 22 | 5 |
| **Total** | **3,935** | **3,497** | **2,920** | **2,601** |

**Key substitution ratios** (demand-decomposer, model-derived):
- 1M BEVs in fleet = 0.031 mb/d oil displaced
- 1 additional solar TWh = 0.101 bcm/yr gas displaced (0.55 displacement ratio × 0.1841 bcm/TWh CCGT intensity)

---

### Phase 6 — Adoption and S-Curve Dynamics

**S-curve parameters** (scurve-fitter, confidence 0.82):

| Vector | L (%) | k | x0 | R² | Phase (2024) |
|--------|-------|---|-----|-----|-------------|
| V1: EV all-types | 90.0 | 0.4281 | 2026.3 | 0.9902 | rapid_growth (23.89%) |
| V1: BEV-only | 85.0 | 0.3836 | 2027.8 | 0.9736 | rapid_growth |
| V2: Solar generation share | 45.0 | 0.2279 | 2031.6 | 0.9965 | tipping (6.92%) |
| V3: HP EU new installations | 79.13 | 0.1393 | 2028.9 | 0.9987 | rapid_growth EU (24.0%) |

V1 model projections: 2029: 68.7% EV share; 2034: 86.8%; 2044: 90.0% (scurve-fitter, model-derived).
V2 model projections: 2029: 16.1% solar share; 2034: 28.6%; 2044: 42.5% (scurve-fitter, model-derived).
V3 EU model projections: 2028: 37.1% HP share; 2033: 50.6%; 2043: 69.4% (scurve-fitter, model-derived).
BEV fleet stock share: 2026: 15.3% → 2031: 47.6% → 2036: 75.1% → 2046: 84.7% (stream-forecaster, model-derived).

**Regional adoption dynamics** (regional-adopter, confidence 0.78):

*V1 regional (EV new car sales share, 2024):*
- China: 47.36% (rapid_growth; x0=2023.7; already past inflection; death-spiral active per xcurve-analyst)
- Europe: 26.91% (rapid_growth; x0=2025.9; R²=0.9207 — below 0.95 flag due to Germany incentive kink)
- USA: 11.59% (tipping; x0=2029.2; 5.6 years behind China at inflection)
- Rest of World: 6.13% (tipping; x0=2029.6)

*V2 regional (solar generation share, 2024):*
- Europe: 10.48% (tipping; x0=2030.5; current share leader)
- China: 9.03% (tipping; x0=2029.5; +52.8% YoY solar generation growth; overtakes Europe ~2027, model-derived)
- USA: 6.07% (tipping; x0=2033.0; 1,000+ GW solar+storage in interconnection queue)
- Rest of World: 5.90% (tipping; x0=2032.2)

All four regions are simultaneously in the tipping phase for V2 — the divergence is in growth rate (China k=0.2649 vs. Europe k=0.1852) and inflection year, not phase label. China's BESS capacity (167,401 MWh, 45.2% of global, +145% YoY) creates the most favorable solar utilization trajectory.

*V3 regional (heat pump share, 2023):*
- Europe: 24.0% of new heating installations (rapid_growth; x0=2028.9; S-curve fitted)
- China: ~12% est. (tipping; T3 data; primary incumbent is coal district heating, not gas)
- USA: ~10% (tipping; AHRI data; structurally bifurcated — southern states accelerating, northern states slow)

**Incumbent decline stage** (xcurve-analyst, confidence 0.75):

| Incumbent | Stage | Key Evidence |
|-----------|-------|-------------|
| ICE passenger vehicles (global) | Accelerating decline | VW: 3 factory closures; 54,000 EU auto jobs cut 2024 |
| ICE/oil incumbents (China) | Death spiral active | Model-derived death spiral activation: 2025.8; 47.36% EV share |
| Gas CCGT/OCGT (power sector) | Pre-disruption (gen share metric) / Early volume loss (merit order) | Solar displacing ~24% of 2024 gas generation by 2030; ~86% by 2034 (model-derived, xcurve-analyst) |
| Gas boiler EU | Accelerating decline | Death spiral activation EU: 2029.1 (model-derived); gas boiler new install share declining |
| Oil refinery sector | Structural stress | 121 of 465 global refineries at closure risk; $485B pipeline stranded assets |
| OPEC fiscal stress | Revenue erosion | Saudi Arabia fiscal break-even ~$80–85/barrel vs. Brent $74 (Dec 2024) |

---

### Phase 7 — Synthesis and Tipping Point

**Composite tipping assessment** (tipping-synthesizer, confidence 0.75):

The three-condition framework (cost parity + capability parity + adoption readiness) yields:
- V1: All three conditions on track for simultaneous satisfaction in **2027**. Binding constraint: capability_parity (fleet-average TCO and cold-weather range — model parity 2027). Adoption readiness PARTIAL (US highway DCFC coverage 59.1% vs. ~80% threshold; China 98% — regional divergence).
- V2: All three conditions on track for satisfaction in **2027–2028**. Binding constraint: capability_parity (dispatchability index 70% vs. 80% threshold — BESS duration extension to 4–6 hours modeled by 2027–2028).
- V3: CONTINGENT. Cost parity NOT MET under US prices. No tipping year assigned; earliest plausible window 2035–2043 under favorable conditions (European ducted pathway, lib parity year 2043).

**Composite oil/gas tipping window:** 2027–2028 (V1+V2 simultaneous). Gas demand structural peak: 2030–2032 (tipping-synthesizer). Oil demand structural peak: 2024–2026 (demand-decomposer + tipping-synthesizer).

**Post-tipping completion timeline** (tipping-synthesizer):
- V1 completion (80% BEV new sales): 2031–2034
- V2 completion (75% solar+BESS new capacity): 2033–2036
- V3 completion: NOT ASSIGNED — CONTINGENT

**Five incumbent displacement mechanisms active** (xcurve-analyst):
1. Merit-order displacement — CCGT pushed to margin by solar+BESS cost advantage (V2)
2. ICE fleet residual value erosion — BEV depreciation superiority suppresses ICE demand (V1)
3. Refinery throughput compression — 121 of 465 global refineries at closure risk as oil demand falls
4. Gas producer fiscal stress — Saudi Arabia fiscal break-even ~$80–85/barrel vs. Brent $74 signals producer vulnerability
5. Death spiral — China ICE market (activation year 2025.8, model-derived); EU gas boiler market (activation year 2029.1, model-derived)

#### Commodity Demand Impact — Phase 7 Summary

The commodity demand consequences of the 2027–2028 composite tipping point compound over time. At the tipping point (2027–2028), oil demand has already begun structural decline and gas power-sector displacement is accelerating through the S-curve growth phase (V2 x0=2031.6). Three dynamics govern the post-tipping trajectory:

1. **Oil demand ratchet:** Peak oil at 2024–2026, then irreversible decline. The 103.4 mb/d 2024 baseline falls to 87.7 mb/d by 2031 (−12.5%), 75.8 mb/d by 2036 (−26.7%), and 73.0 mb/d by 2046. The structural floor (54.4 mb/d rising to ~60.7 mb/d) provides a demand floor that stabilizes oil demand above zero — but the disruption-eligible 49.0 mb/d is largely displaced by 2046.

2. **Gas power-sector collapse:** OCGT peaker gas demand collapses 98% by 2046 (410 bcm → 9 bcm, model-derived, stream-forecaster). CCGT demand falls from 1,230 bcm to 148 bcm by 2046 — an 88% reduction. Gas displaced by solar by 2030: ~24% of 2024 gas generation; by 2034: ~86% (model-derived, xcurve-analyst).

3. **Heating gas slow displacement:** V3 heating sector gas displacement is slow (HP global stock S-curve: L=33.01%, k=0.1388, x0=2028.9, R²=1.00; stream-forecaster). Residential gas boilers decline from 574 bcm (2024) to 403 bcm (2046) — only a 30% reduction over 20 years, reflecting V3's CONTINGENT status for US markets and slow global adoption ceiling.

**Regional demand dynamics summary** (regional-adopter; note: regional-demand-analyst absent — HIGH degradation):
- China: First to tip V1 (2025) and V2 (2025 per tipping-synthesizer). Fastest oil demand reduction in road transport segment; largest BESS deployment accelerating V2 gas displacement.
- Europe: V1 tipping 2025–2026; V2 tipping 2026; V3 leading globally. European gas demand faces three-vector simultaneous pressure — the most acute exposure of any major region.
- USA: V1 tipping 2027; V2 tipping 2027–2028; V3 structurally constrained by low gas prices. US oil demand decline lags China by ~5 years; US gas power displacement lags Europe by ~2.5 years. Interconnection queue (2,300 GW) is the primary structural bottleneck suppressing otherwise economically inevitable solar deployment.
- Note: Quantitative regional demand breakdowns (mb/d and bcm by region) are unavailable due to the absence of the regional-demand-analyst agent (07d). This represents a HIGH-criticality data gap.

---

## Key Conclusion

BEV will displace ICE oil demand and solar+BESS will displace gas power generation at the global composite tipping window of 2027–2028. Cost parity was reached for V1 in 2020–2021 (cost-parity-checker, confidence 0.65) and V2 in 2023–2024 (cost-parity-checker, confidence 0.82). Capability sufficiency is the binding constraint for both vectors — model parity 2027 for V1 and 2027–2028 for V2 (tipping-synthesizer, capability-parity-checker). Oil demand has already reached structural peak at 2024–2026; gas demand peaks later at 2030–2032 net total. V3 (ASHP vs. gas heating) is CONTINGENT — cost parity not met under US energy prices, with no assigned tipping year within the primary horizon. Confidence: 0.383 (base mean 0.783 across 13 agents; −0.30 for regional-demand-analyst HIGH failure; −0.10 for fleet-modeler MEDIUM failure).

---

## Rupture Window

**V1 (BEV vs. ICE):** 2027 — capability parity binding constraint (fleet-average TCO + cold-weather range, model-derived 2027; tipping-synthesizer)
**V2 (Solar+BESS vs. gas power):** 2027–2028 — capability parity binding constraint (dispatchability index, model-derived 2027–2028; tipping-synthesizer)
**V3 (ASHP vs. gas heating):** CONTINGENT 2035–2043 — cost parity NOT MET (tipping-synthesizer)
**Composite oil/gas:** 2027–2028 (V1+V2 simultaneous)
**Oil demand structural peak:** 2024–2026
**Gas demand structural peak (net total):** 2030–2032

---

## Aggregated Confidence Score

**Step 1 — Base confidence (arithmetic mean of 13 agents that ran):**
mean(domain_disruption=0.82, cost_researcher=0.84, cost_fitter=0.78, capability=0.82, cost_parity=0.69, cap_parity=0.81, adopt_readiness=0.75, tipping_synthesizer=0.75, scurve_fitter=0.82, regional_adopter=0.78, xcurve_analyst=0.75, demand_decomposer=0.80, stream_forecaster=0.77) = **0.783**

**Step 2 — Degradation penalty (Failure Matrix):**
- fleet-modeler (07c): FAILED, Criticality=MEDIUM → −0.10
- regional-demand-analyst (07d): FAILED, Criticality=HIGH → −0.30
- Total penalty: **−0.40**

**Step 3 — Weakest-link cap:** No CRITICAL criterion compliance failures flagged — no 0.50 cap applied.

**Step 4 — Floor check:** 0.783 − 0.40 = 0.383 > 0.10 floor.

**Step 5 — Final confidence: 0.383**

Calculation (lib.tipping_math.confidence_aggregate, verified): mean=0.783; penalty=0.40; critical_cap_applied=False; final=0.383.

The steep −0.30 HIGH penalty for regional-demand-analyst is the dominant driver of the low final score. Without the two missing agents, confidence would have been 0.783 — a strong multi-vector synthesis. The missing regional demand quantification is a material analytical gap for commodity market investors who need market-by-market demand projections.

---

## Risk Factors and Data Gaps

### Critical Data Gaps (aggregated from all agents)

1. **Regional demand quantification absent** (regional-demand-analyst 07d: FAILED HIGH): No market-by-market oil and gas demand projections by region (mb/d and bcm). China, USA, and Europe demand breakdowns are qualitative only.
2. **Fleet-modeler absent** (fleet-modeler 07c: FAILED MEDIUM): BEV fleet stock share modeled via 6-year rolling average approximation (stream-forecaster) rather than full stock-flow accounting (scrappage + new sales). Introduces ±15% uncertainty in fleet-level oil demand at +5yr horizon.
3. **No BEV-HDT adoption S-curve** (demand-decomposer, stream-forecaster): Commercial truck BEV disruption uses passenger car S-curve +3yr. Dedicated BEV-HDT global fleet data is absent.
4. **V3 China heating market data** (regional-adopter): No T1/T2 time series for "heat pump share of new heating installations" in China. T3 estimate (12%) with ±5 pp uncertainty; China's primary heating incumbent is coal district heating, not gas.
5. **V1 Europe low R² warning** (regional-adopter): EU V1 EV fit R²=0.9207 below 0.95 threshold, reflecting German incentive-withdrawal kink. Europe V1 model projections carry wider uncertainty than reported CIs.
6. **Solar-to-gas displacement ratio uncertainty** (demand-decomposer, stream-forecaster): 0.55 global average; true ratio varies 0.30–0.75 by regional grid composition. ±10 pp perturbation is the dominant V2 uncertainty at +10yr.
7. **V3 HP stock S-curve ceiling (L=33.01%)** (stream-forecaster): Constrained by 2040 breakpoint (27.2% stock share). If global HP adoption accelerates, 2046 stock share could reach 40–50%, adding 50–120 bcm additional gas displacement.
8. **Industrial gas (821 bcm) treated as structural floor** (demand-decomposer): No electrolytic hydrogen or process electrification vector within 20-year horizon. Largest single post-2035 uncertainty for gas demand.
9. **V2 full solar LCOE fit R²=0.756** (cost-fitter): Below 0.80 threshold — flagged low confidence on the full-period solar LCOE fit (early period fit R²=0.9506 is acceptable).

### Risk Factors

**Upside risks to disruption speed:**
- Battery manufacturing oversupply (3 TWh capacity vs. 1 TWh demand, 3:1 surplus; adopt-readiness) — costs may decline faster than base rate
- V1+V2 cross-vector amplification: battery supply chain subsidizes BESS cost decline by 1–2 years (tipping-synthesizer)
- China V1+V2 simultaneous tipping (2025) creates a massive market where ICE and gas investments are already economically irrational

**Downside risks to disruption speed:**
- US interconnection queue (2,300 GW, 5-yr average wait) — structurally suppresses V2 even as economics favor solar (adopt-readiness)
- HVAC workforce shortage (80,000-person gap in US; UK at 10% of 2028 HP installation trajectory) — structural V3 constraint (adopt-readiness)
- Low US natural gas prices ($2.19/MMBtu) — V3 cost parity not achievable at current prices; V2 partially cushioned in gas-rich regions
- V3 capability gaps (ducted retrofit complexity 3.5/5 vs. ≤2.5/5 threshold; no trajectory to resolve) — no market-driven solution on the horizon
- Saudi Arabia fiscal stress (break-even ~$80–85/barrel vs. Brent $74) — potential production discipline response that could support oil prices and partially offset demand destruction signal

---

## Regional Analysis

**China — First mover across all three vectors:**
China leads V1 by 5.6 years over the USA at the S-curve inflection (x0=2023.7 vs. 2029.2; regional-adopter). ICE death spiral is already active (model-derived activation 2025.8; xcurve-analyst). V2 tipping designated 2025 by the tipping-synthesizer; China solar generation +52.8% YoY in 2024, with BESS at 45.2% of global installed capacity (+145% YoY). China leads the V2 x0 by 1 year ahead of Europe (x0=2029.5 vs. 2030.5). For V3, China primary heating incumbent is coal district heating rather than gas boilers — V3 gas displacement in China is structurally different from Europe and USA.

**Europe — Three-vector simultaneous pressure:**
Europe faces market-driven disruption on all three vectors simultaneously. V1 EV at 26.91% (rapid_growth; tipping 2025–2026 per tipping-synthesizer), V2 solar at 10.48% (tipping; x0=2030.5; tipping 2026 per tipping-synthesizer), and V3 HP at 24% of new installations (rapid_growth; x0=2028.9). European gas incumbents face the most acute near-term risk of any region. Gas boiler EU death spiral activation modeled at 2029.1 (xcurve-analyst). BESS deployment (53,863 MWh, +62.2% YoY) lags China by 3.1× — a structural constraint on solar utilization speed.

**USA — Delayed V1+V2, structurally constrained V3:**
US V1 EV at 11.59% (tipping; x0=2029.2; 5.6 years behind China). US V2 solar at 6.07% (tipping; x0=2033.0; constrained by interconnection queue). US V3 structurally constrained by low gas prices (Henry Hub $2.19/MMBtu) — V3 cost parity NOT MET, adoption ceiling low. USA is the slowest-disrupting major market across all three vectors. BEV TCO cost-curve dynamics are market-driven and independent of policy — the adoption inflection will arrive regardless of mandate status, simply later than in China or Europe.

**Note:** Quantitative regional demand projections (mb/d and bcm by region) are unavailable due to the absence of regional-demand-analyst (07d). This section relies on qualitative synthesis from regional-adopter (05b) and tipping-synthesizer (04d).

---

## Sources

All data traced to upstream agent outputs from this pipeline run (agents directory):

| Agent | File | Confidence | Status |
|-------|------|-----------|--------|
| Domain Disruption | 01-domain-disruption.md | 0.82 | OK |
| Cost Researcher | 02a-cost-researcher.md | 0.84 | OK |
| Cost Fitter | 02b-cost-fitter.md | 0.78 | OK |
| Capability | 03-capability.md | 0.82 | OK |
| Cost Parity Checker | 04a-cost-parity.md | 0.69 | OK |
| Capability Parity Checker | 04b-cap-parity.md | 0.81 | OK |
| Adoption Readiness Checker | 04c-adopt-readiness.md | 0.75 | OK |
| Tipping Synthesizer | 04d-tipping-synthesizer.md | 0.75 | OK |
| S-Curve Fitter | 05a-scurve-fitter.md | 0.82 | OK |
| Regional Adopter | 05b-regional-adopter.md | 0.78 | OK |
| X-Curve Analyst | 05c-xcurve-analyst.md | 0.75 | OK |
| Demand Decomposer | 07a-demand-decomposer.md | 0.80 | OK |
| Stream Forecaster | 07b-stream-forecaster.md | 0.77 | OK |
| Fleet Modeler | 07c-fleet-modeler.md | — | FAILED (MEDIUM, −0.10) |
| Regional Demand Analyst | 07d-regional-demand.md | — | FAILED (HIGH, −0.30) |

*Output written: 2026-03-20 | Pipeline run: oil-gas-demand-disruption | Agent: stdf-synthesizer*
