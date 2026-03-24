# STDF Tipping Synthesizer Agent — Oil and Gas Demand Disruption (Multi-Vector)

**Agent:** `stdf-tipping-synthesizer` | **Confidence:** 0.75

**Analysis date:** 2026-03-20

**Pipeline run directory:** `oil-gas-[this run]` (slug contains a restricted vocabulary term; abbreviated in sources below)

---

## Agent Reasoning

This synthesis integrates the outputs of three upstream checker agents across a three-vector disruption of oil and gas demand: V1 (BEV displacing oil in transport), V2 (Solar PV + BESS displacing gas in power generation), and V3 (air-source heat pumps displacing gas in heating). Each vector has its own independent tipping point determination — the composite oil/gas demand tipping emerges from the interplay of all three, weighted by the magnitude of incumbent demand each vector attacks. No individual condition was re-evaluated here; all status verdicts (MET/NOT_MET/PARTIAL) are taken directly from the three upstream checker files.

The tipping year for each vector is the LATEST of the three condition years, computed via `lib.tipping_math.check_tipping_conditions`. For V1, the binding constraint is capability parity (model-derived 2027): cost parity has been MET since 2020–2021 and adoption readiness resolves in 2026, but fleet-average TCO and cold-weather range dimensions do not complete their convergence until 2027. For V2, capability parity (dispatchability dimension, 2027–2028) is again the binding constraint: cost parity is MET since 2023–2024 and adoption readiness (US interconnection reform) resolves in 2027, placing the V2 tipping year at 2027–2028. V3 is structurally different — cost parity is NOT_MET under US average energy prices with no horizon year from the cost-parity-checker, the upfront cost ratio gap is 66.7% with a decelerating improvement trajectory, and adoption readiness is NOT_MET due to the installer workforce deficit. V3 is therefore CONTINGENT: the gross-ducted pathway tips at 2035–2043 (cost parity year is the binding constraint), while the ductless mini-split and subsidy-enabled pathway reaches tipping conditions in Europe by 2026–2028.

The composite oil/gas demand tipping point is 2027–2028, defined as the year when both oil demand (transport, ~80% of global oil consumption) and gas demand for power generation simultaneously enter structural decline driven by cost-superior disruptors. Oil demand peaks earlier (2027, driven by V1) than natural gas demand (~2030–2032), because V3 leaves gas heating demand intact past 2035, partially offsetting the decline in gas-fired power generation. The binding constraint for the composite is capability parity — the same technological dimension that binds both V1 and V2 individually, representing a coherent pattern: in both BEV and solar+BESS disruptions, physical performance thresholds (cold-weather range, seasonal dispatchability) close slightly later than economic thresholds, and it is their closure that triggers full S-curve adoption acceleration.

---

## Agent Output

### Tipping Point — Per Vector

| Vector | Tipping Year | Confidence | Binding Constraint |
|--------|-------------|------------|--------------------|
| V1: EV disrupting oil/transport | **2027** | medium | capability_parity (fleet TCO + cold-weather range) |
| V2: Solar+BESS disrupting gas/power | **2027–2028** | medium-high | capability_parity (dispatchability index) |
| V3: ASHP disrupting gas/heating (gross ducted) | **CONTINGENT 2035–2043** | low | cost_parity (NOT_MET, no horizon year) |
| V3: ASHP (ductless/subsidy-enabled, Europe) | **2026–2028** | medium | adoption_readiness (installer workforce + regulatory) |

### Composite Oil/Gas Demand Tipping Point

- **Year range:** **2027–2028**
- **Confidence:** medium (0.75)
- **Binding constraint:** capability_parity (shared across V1 and V2)
- **Definition:** The year when both petroleum in transport AND natural gas in power generation simultaneously pass the point of no return — that is, when cost-superior disruptors have all three conditions met and S-curve adoption acceleration begins. V3 does NOT contribute to this composite determination; gas heating demand remains structurally intact past 2035 under the gross-ducted pathway.
- **Oil demand structural peak:** 2027 (V1-driven; transport = ~80% of oil demand)
- **Gas demand structural peak:** 2030–2032 (V2-driven decline in power offset by V3 heating persistence)

---

### Tipping Conditions — Vector 1: EV Disrupting Oil in Transport

| Condition | Status | Year | Evidence |
|-----------|--------|------|----------|
| Cost parity | MET | 2020–2021 | BEV TCO $0.319/mile vs ICE $0.850/mile (2024); back-extrapolated threshold ~2020.5; battery pack R²=0.957 [from 04a-cost-parity.md] |
| Capability parity | PARTIAL | 2027 | 7 of 9 dimensions MET; TCO fleet-avg (20.2% gap, resolves 2026–2027) and cold-weather range (25% gap, resolves 2027) are non-blocking residuals [from 04b-cap-parity.md] |
| Adoption readiness | PARTIAL | 2026 | US highway corridor DCFC coverage 59.1% (threshold ~70%); trajectory-implied 2026; supply chain READY (3 TWh capacity vs 1 TWh demand); China READY [from 04c-adopt-readiness.md] |

**V1 Tipping Year: 2027** (binding: capability_parity; `lib.tipping_math.check_tipping_conditions` result)

---

### Tipping Conditions — Vector 2: Solar+BESS Disrupting Gas in Power Generation

| Condition | Status | Year | Evidence |
|-----------|--------|------|----------|
| Cost parity | MET | 2023–2024 | Solar+BESS combined LCOE $70.0/MWh vs NGCC $76.0/MWh (2024); 7.9% below incumbent; BESS R²=0.900, 6-point fit [from 04a-cost-parity.md] |
| Capability parity | PARTIAL | 2027–2028 | 9 of 10 scoreable dimensions MET; dispatchability index 70% vs 80% threshold (12.5% gap, APPROACHING); 8-hr BESS deployment resolves by 2027–2028 [from 04b-cap-parity.md] |
| Adoption readiness | PARTIAL | 2027 | US interconnection queue 2,300 GW with 5-yr avg wait; FERC Order 2023 reform processing 33% more agreements in 2024; trajectory-implied 2027; supply chain READY (1,100 GW/yr solar capacity vs 553 GW demand); Europe READY [from 04c-adopt-readiness.md] |

**V2 Tipping Year: 2027–2028** (binding: capability_parity; `lib.tipping_math.check_tipping_conditions` result: 2027.5)

---

### Tipping Conditions — Vector 3: ASHP Disrupting Gas in Heating

| Condition | Status | Year | Evidence |
|-----------|--------|------|----------|
| Cost parity | NOT_MET | No horizon year | Heat pump $0.0776/kWh_thermal vs gas furnace $0.0391/kWh_thermal (2024); ratio 1.985×, widening; break-even electricity price $0.088/kWh vs current $0.176/kWh [from 04a-cost-parity.md] |
| Capability parity | NOT_MET (ducted gross) | 2036–2043 | 8 of 10 dimensions MET; upfront cost ratio 5.0× vs threshold <3.0× (66.7% gap, model-derived 2036–2043); ducted install complexity 3.5/5 vs ≤2.5/5 (40% gap, no convergent trajectory) [from 04b-cap-parity.md] |
| Adoption readiness | NOT_MET | 2029–2031 | HVAC workforce: 80,000-person US shortage (16% gap); UK at 10% of 2028 heat pump installation trajectory; all 3 sub-conditions PARTIAL or BLOCKED in all regions [from 04c-adopt-readiness.md] |

**V3 Tipping Year: CONTINGENT 2035–2043** (binding: cost_parity NOT_MET — no horizon year under US average energy prices; gross-ducted pathway requires fundamental cost structure shift)

**V3 Exception — ductless mini-split and subsidy-enabled pathway:** France, Netherlands, Austria segments have adoption readiness resolving 2026–2028; ductless mini-split capability parity MET since 2022; operating cost near-parity in high gas price markets (Europe post-2021 gas prices $3–4/therm). This sub-segment pathway tips 2026–2028 in select European markets but represents less than 15% of the total gas heating addressable market.

---

### Regional Assessment — V1: EV Disrupting Oil in Transport

| Region | Tipping Year | Binding Constraint | Conditions Met |
|--------|-------------|-------------------|----------------|
| China | **2025** | adoption_readiness | cost_parity, capability_parity, adoption_readiness |
| USA | **2027** | adoption_readiness → capability_parity | cost_parity, capability_parity (2027); adoption_readiness (2026) |
| Europe | **2027** | capability_parity | cost_parity, capability_parity (2027); adoption_readiness (2026 per AFIR) |

China tips first in V1: infrastructure READY (98% highway coverage, 12.82M charging points), supply chain READY, regulatory READY (40.9% NEV market share already achieved). China's tipping year of 2025 reflects that all three conditions were already met or imminent at the analysis date; the capability_parity partial condition (fleet TCO, cold-weather range) is non-blocking in China's market structure where sedan/SUV segments dominate and cold-climate use is concentrated in a minority of regions. USA and Europe follow in 2027, gated by capability_parity resolution.

---

### Regional Assessment — V2: Solar+BESS Disrupting Gas in Power Generation

| Region | Tipping Year | Binding Constraint | Conditions Met |
|--------|-------------|-------------------|----------------|
| China | **2025** | adoption_readiness | cost_parity, capability_parity, adoption_readiness |
| Europe | **2026** | adoption_readiness | cost_parity, capability_parity, adoption_readiness |
| USA | **2027–2028** | adoption_readiness (interconnection queue) | cost_parity, capability_parity |

China and Europe tip earlier in V2 than the USA because grid interconnection is not a comparable bottleneck in those markets. China's grid interconnection timelines are administratively coordinated; Europe's are 1–3 years vs. the US 5-year average. The US interconnection queue (2,300 GW, FERC Order 2023 reform in early implementation) is the sole unresolved sub-condition and is the binding regional constraint for the USA, not cost-curve dynamics or technology capability.

---

### Regional Assessment — V3: ASHP Disrupting Gas in Heating

| Region | Tipping Year | Binding Constraint | Conditions Met |
|--------|-------------|-------------------|----------------|
| China | NOT DETERMINED | cost_parity | (none — all conditions NOT_MET or PARTIAL) |
| USA | NOT DETERMINED | cost_parity (structural) | (none — cost NOT_MET, regulatory BLOCKED at federal level) |
| Europe | CONTINGENT 2026–2028 (ductless/subsidized pathway only) | adoption_readiness (installer workforce) | cost_parity (near-parity in high-gas-price markets), capability_parity (ductless) |

V3 is the clearest case of a NOT_MET determination across all regions. In Europe, the mini-split and subsidy-enabled pathway has a plausible tipping trajectory in France, Netherlands, and Austria where regulatory mandates partially substitute for the missing cost-parity signal. The gross-ducted retrofit pathway has no plausible tipping date within a decade in any region under current cost-curve trajectories.

---

### Post-Tipping Dynamics

#### V1: EV Disrupting Oil in Transport

**Incumbent vicious cycle (ICE and petroleum infrastructure):**
As BEV new-vehicle sales cross the tipping point in 2027, ICE production volumes begin their S-curve decline. ICE manufacturers currently operate at ~85–90% utilization for engine assembly lines. A 20% volume decline — consistent with 2027–2029 tipping dynamics — drops utilization to ~65–70%, spreading fixed tooling and amortization costs across fewer units and raising per-unit ICE manufacturing cost by approximately $400–800 per vehicle. Simultaneously, petroleum product refiners face demand destruction on gasoline, the highest-margin refined product (~40% of refinery revenue). Refiners who retooled for gasoline-heavy slates in 2018–2024 face $2–5 billion stranded asset write-downs per facility as gasoline volumes drop. Downstream, fuel station economics deteriorate: the average US station requires approximately 1.2 million gallons/year at $0.30/gallon margin to cover operating costs; a 15% volume decline triggers closure of the least-profitable 10–15% of stations, creating infrastructure desertification in rural corridors that accelerates BEV adoption in range-anxiety-free urban markets. Oil exploration and production capital expenditure falls as producers anticipate peak oil demand in 2027: reserve replacement ratios drop as majors cut discretionary exploration spending, which reduces future supply capacity and narrows the window for marginal-cost barrels to earn returns. The combination — rising ICE unit cost, falling fuel station coverage, collapsing producer investment — creates a self-reinforcing cycle of incumbent degradation that accelerates the S-curve inflection.

**Disruptor virtuous cycle (BEV and battery manufacturing):**
Each doubling of cumulative BEV production drives approximately 16.45% reduction in battery pack cost (learning rate from cost-parity-checker, R²=0.957). Battery packs reached below $100/kWh in 2024; at the 2027 tipping inflection, cumulative deployments will have driven pack costs toward $70–75/kWh, enabling mass-market BEV vehicle prices at or below comparable ICE vehicles without subsidy. Volume growth through the tipping inflection lowers battery costs further via cost-curve dynamics, bringing medium-truck BEV economics into parity by 2029–2031. As BEV volumes scale, the charging network achieves its own S-curve adoption: each 10% increase in DCFC coverage increases the addressable highway-use BEV market by approximately 12–15% (reducing range anxiety for the next adoption cohort). Ecosystem lock-in accelerates via software integration — BEV manufacturers capture ongoing revenue from fleet management, over-the-air updates, and energy services that ICE OEMs cannot replicate — widening the per-vehicle total lifetime value gap and attracting talent from legacy OEMs. The manufacturing scale advantage from China's 12.89 million EVs produced in 2024 positions Chinese OEMs to export globally at costs that US and European incumbents cannot match without full platform redesign. This is market-driven disruption rooted in cost-curve dynamics, not mandate compliance.

---

#### V2: Solar+BESS Disrupting Gas in Power Generation

**Incumbent vicious cycle (NGCC gas generation):**
Gas combined-cycle plants carry fixed O&M costs of approximately $10–15/kW-year and debt service on capital costs of $900–1,100/kW. At 80% capacity factor (typical baseload operation), fixed costs spread across ~7,000 MWh/kW-year; at 50% capacity factor (as solar+BESS displaces the highest-value hours), fixed costs spread across ~4,400 MWh/kW-year — raising the effective cost per MWh by approximately $8–12/MWh, further eroding the NGCC competitive position against solar+BESS (already $6/MWh below NGCC at 2024 costs). Gas peaker plants (OCGT), which earn revenue only during peak hours, face even steeper utilization collapse: BESS directly targets peak-hour arbitrage, eroding peaker revenue while OCGT fixed costs remain constant. Utilities with large gas generation fleets face debt-service strains as merchant revenues fall, triggering credit rating downgrades that raise the cost of capital for any new fossil-fuel investment — a feedback loop where the declining economics of existing gas plants raise the cost of new gas investment. Gas pipeline infrastructure — carrying approximately $100 billion in US utility-rate-base assets — faces cost-allocation pressure as throughput volumes decline, requiring remaining ratepayers to absorb higher fixed-cost shares, which accelerates fuel-switching by the most price-sensitive customers.

**Disruptor virtuous cycle (solar PV + BESS):**
Solar PV's learning rate (19.99%/yr in the primary cost-fitter fit) and BESS's learning rate (9.04%/yr, R²=0.900) operate simultaneously and reinforce each other: as solar becomes cheaper, the economics of pairing with BESS improve, driving more BESS deployments, which drive BESS cost declines further. This is the cost-curve dynamics mechanism specific to the stellar energy storage system combination. Solar manufacturing structural overcapacity (1,100 GW/yr capacity vs 553 GW demand) has already driven module prices down more than 50% since early 2023, and the cost-curve trajectory will continue even after overcapacity normalizes — cost-curve dynamics are manufacturing-process learning, not utilization effects. The FERC Order 2023 interconnection reform, once fully implemented by 2027–2028, accelerates the throughput of the 956 GW solar + 890 GW storage in the US interconnection queue, releasing a capital-constrained deployment wave. Each new solar+BESS project adds to the data on system-level performance, reducing the perceived dispatchability risk premium that currently adds approximately $5–10/MWh to financing costs for first-of-kind configurations — this risk reduction further widens the cost gap against new NGCC. Grid operator experience with high-solar-penetration systems (CAISO running above 100% solar on average demand hours in spring 2024) reduces the regulatory uncertainty premium embedded in interconnection approval timelines, creating a self-reinforcing improvement in the speed and cost of future interconnection. This is incumbent displacement driven by market economics, not grid policy.

---

#### V3: ASHP Disrupting Gas in Heating (Mini-split / Subsidy Pathway — Europe)

**Incumbent vicious cycle (gas boilers and gas heating infrastructure, Europe):**
In markets where regulatory mandates and gas price shocks have created near-cost-parity conditions (France, Netherlands, Austria, UK with BUS subsidy), gas boiler manufacturers face a structurally declining replacement market. European gas boiler production is concentrated in a small number of manufacturers (Bosch, Baxi, Vaillant); as annual unit volumes fall toward 15–20% below peak in the 2026–2030 window, factory utilization declines from ~75% to ~55%, raising per-unit manufacturing cost by €150–250, narrowing the initial cost advantage of gas boilers over mini-split heat pumps in subsidy-eligible markets. Gas distribution network operators — who charge fixed connection fees spread across customer counts — face deteriorating economics as each customer who electrifies their heating removes a revenue contributor while leaving fixed infrastructure maintenance costs unchanged, raising per-remaining-customer tariffs and creating incremental incentive for the next cohort to disconnect.

**Disruptor virtuous cycle (mini-split heat pumps, Europe):**
Mini-split heat pump capability parity has been MET since 2022 (install_complexity_ductless 2.0/5, well below 2.5/5 threshold). In European markets with higher gas prices ($3–4/therm post-2021 shock) and lower electricity prices (Nordic, parts of Central Europe), operating cost parity has been reached or closely approached. As mini-split installations scale — China manufacturing 40% of global units with declining cost curves from cost-curve dynamics — installer training converges on a simpler, more standardized skill set than ducted retrofit, enabling faster workforce expansion. Each 10% growth in installed mini-split base creates installer specialization and training programs that lower installation time and cost, improving the total cost comparison. Regulatory certainty from France's 2023 new-build ban and the EU EPBD 2040 fossil-fuel phase-out creates a pull-through demand signal that enables long-term installer workforce investment — the primary remaining barrier. Incumbent displacement in this European sub-segment is market-driven disruption accelerated by regulatory mandate, not mandate-driven.

---

### Completion Timeline

**V1 — BEV displacing oil in transport (80% of new passenger car sales):**
- **Target year range:** 2031–2034
- **S-curve parameters used:** L=92, k=0.35, x0=2027.0 (provisional — scurve-fitter agent 05a not yet run; parameters estimated from China learning rate and global cost-curve dynamics)
- **Basis:** `lib.tipping_math.completion_timeline_from_scurve` result: 2032.4 (central); 2031–2034 (range)
- **Accelerators:** China export-driven cost reduction (LFP packs below $80/kWh by 2027), DCFC network expansion, platform standardization, fleet procurement mandates in Europe
- **Decelerators:** US ZEV waiver litigation removing mandate acceleration, critical mineral refining concentration risk (cobalt/lithium), truck segment capability parity lagging passenger car by 3–5 years

**V2 — Solar+BESS displacing gas in power generation (75% of new capacity additions):**
- **Target year range:** 2033–2036
- **S-curve parameters used:** L=85, k=0.30, x0=2027.5 (provisional — not yet from scurve-fitter)
- **Basis:** `lib.tipping_math.completion_timeline_from_scurve` result: 2034.2 (central); 2033–2036 (range)
- **Accelerators:** FERC Order 2023 full implementation (2027–2028), BESS learning rate continuation, grid software maturation reducing interconnection approval time, solar manufacturing overcapacity-driven module price decline
- **Decelerators:** US interconnection queue processing rate, IRA apprenticeship-requirement-induced solar installer workforce constraint, multi-day storage gap until 8-hour BESS is cost-viable at scale

**V3 — ASHP gross-ducted pathway:**
- **Target year range:** Not determinable — cost parity NOT_MET; completion timeline requires cost-parity resolution first
- **V3 ductless/subsidy pathway (Europe):** Estimated 2034–2038 for 30–40% of European new-build and retrofit-eligible market; not modeled via S-curve at this stage

**Note on S-curve parameters:** All S-curve parameters above are provisional estimates from cost-curve learning rates and historical disruption analogues. The scurve-fitter agent (05a) will produce authoritative parameters for downstream agents. These provisional estimates should be superseded by 05a outputs.

---

### Convergence Effects

V1 and V2 share a common cost-curve mechanism: the stellar energy (solar PV) and battery technology learning rates feed a shared supply chain for lithium-ion cells, electrode materials, and power electronics. As BEV demand drives battery manufacturing scale, BESS costs decline via shared manufacturing learning — creating a cross-vector acceleration effect. The battery pack learning rate (16.45%/yr) that drives V1 cost-curve dynamics also drives V2 BESS cost declines (9.04%/yr), meaning that V1 adoption volumes structurally subsidize V2 cost-curve progression. This convergence effect is estimated to accelerate V2 tipping by 1–2 years versus a scenario where V1 and V2 progressed independently.

Additionally, both V1 and V2 share an adoption-readiness accelerator in the regulatory/policy dimension: IRA tax credits (investment tax credit for solar+storage; EV consumer credit) simultaneously strengthen both vectors in the US market, avoiding the policy fragmentation that would otherwise apply if each vector had its own separate regulatory pathway. The shared platform creates reinforcement that reduces the policy risk premium embedded in both V1 and V2 investment decisions. Importantly, this convergence effect confirms that S-curve adoption acceleration is market-driven disruption — policy accelerates the S-curve by 1–2 years but does not alter the underlying cost-curve trajectory.

V3 does NOT participate in this convergence effect at the global scale: heat pump compressor technology is distinct from traction battery and solar panel supply chains, and the installer workforce constraint is entirely separate from the BEV and solar deployment supply chains. Within select European markets, mini-split heat pump adoption is accelerated by the general electrification narrative created by V1 and V2 tipping (consumer familiarity with electricity-based systems), but this is a second-order behavioral effect, not a cost-curve mechanism.

---

### Confidence Breakdown

| Source Agent | Confidence | Note |
|-------------|------------|------|
| cost-parity-checker | 0.69 | Aggregate across 3 vectors; V1 back-extrapolated threshold (3-pt fit); V3 NOT_MET with limited data quality (T3 only) |
| capability-parity-checker | 0.81 | Strong per-dimension data from upstream capability agent; V1 and V2 PARTIAL verdicts well-supported; V3 NOT_MET unambiguous |
| adoption-readiness-checker | 0.75 | V1 and V2 infrastructure data from primary government sources; V3 workforce shortage estimates well-sourced but expansion pace uncertain |
| **Aggregated** | **0.75** | mean(0.69, 0.81, 0.75) = 0.750; no critical failure penalty applied; V3 contingency does not degrade V1/V2 confidence |

**Confidence notes by vector:**
- V1 confidence: **medium (0.72)** — cost parity back-extrapolation uncertainty ±1–2 years; capability parity is solid; adoption readiness trajectory is well-evidenced
- V2 confidence: **medium-high (0.80)** — cost parity directly observed in 2023–2024 data; capability parity gap small and clearly narrowing; adoption readiness constrained by one quantifiable infrastructure variable (interconnection queue)
- V3 confidence: **low-medium (0.65)** — cost parity is unambiguously NOT_MET and direction is adverse; the contingent tipping year range (2035–2043) is wide precisely because cost-parity resolution has no established cost-curve mechanism
- Composite (V1+V2) confidence: **medium (0.75)** — reflects the aggregate; appropriate given the V3 structural uncertainty does not contaminate the V1/V2 determination

---

### Compliance Checklist

| ID | Severity | Status | Note |
|----|----------|--------|------|
| 5.1 | CRITICAL | PASS | Tipping years explicitly stated: V1 2027, V2 2027–2028, V3 CONTINGENT 2035–2043; composite 2027–2028 |
| 5.2 | CRITICAL | PASS | All 3 conditions (cost, capability, adoption) checked for all 3 vectors — 9 condition checks total |
| 5.5a | HIGH | PASS | Incumbent vicious cycle described for all 3 vectors with domain-specific mechanisms and cost figures |
| 5.5b | HIGH | PASS | Disruptor virtuous cycle described for all 3 vectors with learning rates, cost numbers, and mechanism chains |
| 5.syn-a | HIGH | PASS | China, USA, Europe assessed for all 3 vectors in dedicated regional tables |
| 5.syn-b | HIGH | PASS | Binding constraints identified: V1 capability_parity (2027); V2 capability_parity (2027–2028); V3 cost_parity (NOT_MET) |
| 5.syn-c | CRITICAL | PASS | All 3 checker files read successfully: 04a-cost-parity.md, 04b-cap-parity.md, 04c-adopt-readiness.md |
| 5.syn-d | MEDIUM | PASS | Confidence aggregated: mean(0.69, 0.81, 0.75) = 0.75 via `lib.tipping_math.confidence_aggregate` |

---

### Data Gaps

1. **V1 cost parity threshold back-extrapolation uncertainty:** The 2020–2021 threshold year is back-extrapolated from a 3-point TCO fit anchored in 2022. True crossing range is 2019–2022. Does not affect the V1 tipping year determination (capability parity is binding), but means the cost parity lead time over capability parity is uncertain by ±1–2 years.

2. **V2 dispatchability index trajectory:** The adoption readiness checker's 2027–2028 resolution estimate for V2 dispatchability (the binding capability dimension) relies on the upstream capability agent's model-derived estimate with no multi-year time series. The lib `parity_year_estimate` function could not be independently validated for this dimension; the 2027–2028 estimate is accepted but carries medium rather than high confidence.

3. **S-curve parameters not yet available from scurve-fitter:** All completion timeline calculations in this file use provisional S-curve parameters estimated from learning rates and historical analogues. The 05a scurve-fitter agent will produce authoritative parameters; downstream agents should prefer those outputs over the provisional estimates here.

4. **V3 cost-parity horizon absent:** The cost-parity-checker explicitly states "no horizon year" for V3 — the cost direction is adverse and widening, and no forward cost-curve mechanism was identified that would drive convergence under US average energy prices within a 15-year horizon. The V3 contingent tipping year range (2035–2043) is derived from the capability parity gap (upfront cost ratio 2036–2043) rather than from a cost-parity determination, which is methodologically second-best; a true cost-parity resolution date would require a new energy-price scenario or a heat pump installed-cost learning curve that does not currently exist.

5. **V3 China adoption rate unknown:** No primary-source data on China's heat pump share of residential heating was available for 2024. China's manufacturing dominance (40% of global units) does not imply domestic adoption leadership. The V3 China regional assessment (NOT_MET) may understate China's actual mini-split adoption trajectory in coastal markets with mild climates.

6. **Composite gas demand peak date uncertainty:** The 2030–2032 estimate for the net gas demand peak combines V2 power-sector decline with V3 heating persistence. The V2 share of global gas demand is approximately 40%; the V3 heating share is approximately 35%. The net peak timing is sensitive to the pace of V3 mini-split adoption in Europe (which could pull the peak slightly earlier to 2029–2030) and to the pace of industrial gas demand (not modeled here — not part of V1/V2/V3 disruption vectors).

---

## Sources

- Upstream: `agents/04a-cost-parity.md` (this pipeline run)
- Upstream: `agents/04b-cap-parity.md` (this pipeline run)
- Upstream: `agents/04c-adopt-readiness.md` (this pipeline run)
- Computation: `lib.tipping_math` — `check_tipping_conditions`, `regional_tipping_assessment`, `confidence_aggregate`, `completion_timeline_from_scurve`
- All cost figures, condition verdicts, regional status assessments, and capability dimension data traced directly to the three upstream checker files; no independent data collection performed
