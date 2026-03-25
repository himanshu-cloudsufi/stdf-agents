# STDF v2 Disruption Analysis: Lead Demand Decline — Li-Ion vs. Lead-Acid

**Sector:** Materials — Lead (Pb) metal commodity demand | **Framework:** STDF v2 | **Date:** 2026-03-20
**Pipeline Confidence:** 0.82 | **Rupture Window:** 2027–2028

---

## Executive Summary

Global lead demand will cross the 10%-below-2024 threshold in **2027** (median path; range 2027.4–2028.8). The 2024 observed baseline is 12,259 kt (domain-disruption); the 10% threshold is 11,033 kt (stream-forecaster). By 2026, demand is already at 11,095 kt — only 62 kt above the threshold — driven by the post-inflection collapse of telecom VRLA (907→441 kt, 2024–2026) and datacenter UPS displacement (503→245 kt, 2024–2026) as Li-ion incumbent displacement moves through its S-curve adoption inflection in non-SLI segments. The binding constraint for the remaining 62 kt is BEV new-vehicle SLI displacement: cost parity is IMMINENT in USA/Europe at 2027–2028 (cost-parity-checker), and adoption readiness reaches the 80% EV highway corridor threshold in 2028 (adoption-readiness-checker). Non-SLI segments (37.5% of total demand) already tipped in 2021–2024; SLI automotive (62.5%) tips in 2027–2028 for USA/Europe and 2031–2032 for China, where the cost_parity constraint persists ($100/unit vs. $25/unit target). The disruptor streams — BEV, LFP-UPS, LFP traction — carry 0.0 kg Pb per unit: all disruption appears as incumbent stream compression with no demand substitution. This is a market-driven disruption, driven entirely by cost-curve dynamics and S-curve adoption mechanics — not by policy mandates or regulatory schedules. Pipeline confidence: 0.82 (high agreement across all 15 agents; primary uncertainty in 2W/3W S-curve parameters and NEVI guidance rescission impact on USA EV corridor build-out).

---

## 7-Phase Narrative

### Phase 1: Sector Scoping

**Sector boundary:** Lead (Pb) metal commodity demand, global, 2024–2046 horizon. Total addressable baseline: 12,259 kt (2024, domain-disruption [observed]).

**Sub-domains and 2024 demand allocation (domain-disruption):**
- Automotive SLI new-vehicle batteries: 1,404 kt (11.5%)
- Automotive SLI replacement/aftermarket: 7,261 kt (59.2%) — largest single sub-domain
- Industrial stationary backup (telecom UPS, datacenter UPS, grid): 1,524 kt (12.4%)
- Industrial motive power (lead-acid forklifts): 379 kt (3.1%)
- Non-battery lead (shielding, alloys, shot): 1,691 kt (13.8%) — structural floor, no identified disruptor

**Primary disruptors:**
1. Battery electric vehicles (BEV) — displaces ICE new-car sales, eliminating SLI demand at point of production; all BEV variants carry 0.0 kg Pb per vehicle (demand-decomposer confirmed)
2. LFP-UPS systems — displaces VRLA lead-acid in telecom and datacenter backup
3. LFP motive power (EV forklifts) — displaces lead-acid traction batteries in warehouse logistics

**Primary incumbents:**
- Lead-acid SLI batteries (automotive market): $25/unit (China), $55/unit (USA) (cost-researcher [observed])
- VRLA lead-acid batteries (telecom and datacenter UPS)
- Lead-acid traction batteries (forklift sector)

**Disruption-addressable demand:** 10,568 kt (86.2%); non-battery floor 1,691 kt is not addressable by any current disruptor (demand-decomposer).

### Phase 2: Technology Inventory

**Disruptor cost trajectory — Li-ion pack (cost-researcher + cost-fitter):**
- 2010: $1,436/kWh [T2: Rethinkx observed] → 2024: $115/kWh [T2: observed]
- Exponential fit: C(t) = 1,240.70 × exp(−0.1841 × (t−2010)), R²=0.954 (cost-fitter)
- Learning rate: 16.81%/yr (cost-fitter); SLI-specific fit: 14.84%/yr, R²=0.990
- Terminal deviation at 2024: 18% below model curve — flagged as non-fatal; actual costs outpacing the fit (cost-fitter)
- China 2024: $94/kWh pack; USA 2024: $115/kWh pack (cost-researcher [observed])

**Disruptor cost — SLI unit (cost-researcher):**
- Li-ion SLI China: $900/unit (2010) → $100/unit (2024) [T2: observed]
- Li-ion SLI USA: $135/unit (2024) [T2: observed]
- Service-level advantage: $0.050/kWh delivered (Li-ion) vs. $1.22/kWh (lead-acid) — 24x superiority (cost-fitter)
- Levelized cost parity: achieved ~2014 (capability + cost-fitter)

**Incumbent cost — lead-acid (cost-researcher):**
- Pack: $300/kWh (2010) → $180/kWh (2023) [T2: BLS PPI, 25 data points, 2000–2024, T1]
- SLI unit China: flat at $25–$30/unit (2010–2024) [T2: observed]
- SLI unit USA: $55/unit (2024) [T2: observed]
- Cost-reduction learning rate: ~2%/yr (cost-researcher [observed])

**Competitive threshold** (cost-fitter): Li-ion SLI nameplate parity with lead-acid — USA 2019–2020, China 2020–2021.
**Inflection threshold** (cost-fitter): SLI unit cost parity — USA 2027–2028, China 2031–2032.

**Capability comparison (capability):**
- Energy density: 195 Wh/kg (Li-ion) vs. 35–50 Wh/kg (lead-acid) — 4–5x advantage
- Cycle life: 5,000 cycles (Li-ion) vs. 300 cycles (lead-acid) — 16x advantage
- 11/13 capability dimensions MET; only SLI unit cost (China: 300% gap, USA: 140% gap) and recycling rate (30% vs. 70% threshold) remain NOT_MET

### Phase 3: Convergence Analysis

The disruption is driven by three convergence combinations that amplify S-curve acceleration (domain-disruption):

**Convergence 1 — Li-BEV (Li-ion + Battery Electric Vehicle):** The cost-curve dynamics of Li-ion pack manufacturing ($1,436→$115/kWh at 16.81%/yr) directly enables BEV economics. Each percentage point of BEV new-car share permanently eliminates SLI demand from future fleet replacement cycles. The 4-year lag between BEV new-car tipping and fleet replacement demand collapse is quantified by the fleet model (fleet-modeler: ICE fleet lifetime 15 years, SLI replacement cycle 4.5 years).

**Convergence 2 — LFP-UPS (LFP chemistry + stationary UPS):** LFP cell manufacturing scale spills over from BEV production into stationary backup applications. Telecom UPS disruption inflected in 2022–2023 (T2 observed: Li-ion share jumped from 13% to 28% in a single year — scurve-fitter). Datacenter UPS followed with x0=2024.90 (scurve-fitter). Both segments are well past their inflection points by 2026.

**Convergence 3 — EV-FL (EV forklift + LFP motive):** EV forklift S-curve is the most advanced: x0=2009.61, currently 64.9% penetration (2024), post-inflection rapid growth phase (scurve-fitter). This convergence is near-complete and contributes to pre-threshold demand compression.

**Cross-segment manufacturing subsidy:** LFP production scale across all three convergence vectors creates a virtuous cycle — each new application reduces per-unit cost for all others. The tipping-synthesizer identifies this as the disruptor virtuous cycle mechanism, amplifying the 14.84%/yr SLI learning rate.

The **competitive threshold** (nameplate pack parity, 2019–2021) and **inflection threshold** (SLI unit parity, 2027–2028 for USA/Europe) from cost-fitter define the two-stage crossing that separates the non-SLI disruption cluster (already past threshold) from the SLI cluster (crossing 2027–2031).

### Phase 4: Disruption Pattern

**Disruption type:** Sequential multi-segment incumbent displacement. The pattern follows a 3-cluster structure (capability-parity-checker), not a single-wave disruption:

- **Cluster 1 (pre-2010 to ~2014):** Physics-level advantages — energy density, cycle life, self-discharge. Li-ion establishes levelized cost superiority ~2014. Telecom and datacenter segments begin adoption.
- **Cluster 2 (2014–2020):** Operational and economic dimensions — operational cost, total cost of ownership, weight, form factor. Non-SLI segments (forklift, telecom, datacenter) tip in 2021–2024 as all conditions reach MET status.
- **Cluster 3 (2027–2031):** SLI unit price and recycling infrastructure. USA/Europe SLI tip in 2027–2028; China SLI tips in 2031–2032.

**Capability parity status (capability-parity-checker):** PARTIAL overall.
- FULLY MET for telecom/datacenter/stationary/forklift (converged 2019–2021)
- PARTIAL for automotive SLI — 11/13 dimensions MET; SLI unit cost (China 300% gap, closing at 14.84%/yr) and recycling rate (30% vs. 70% threshold, estimated ~2029 parity) remain below threshold

The lib classification of "divergent" (implying widening gaps) was overridden to "sequential" by the capability-parity-checker agent, citing the observable 3-cluster convergence trajectory. This override is documented with rationale in the agent output.

**Disruption velocity:** The 2022 jump in telecom Li-ion share (13%→28%, T2 observed) demonstrates that non-SLI segments can move faster than the S-curve model anticipates. The scurve-fitter telecom fit (k=0.3659, x0=2024.84, R²=0.9620) captures this jump in its steepness parameter.

### Phase 5: Business Model Shift

**Cost parity crossing (cost-parity-checker):**
- Service-level parity: MET pre-2010 (24x advantage, $0.050 vs. $1.22/kWh delivered)
- Nameplate pack parity: MET 2019–2021 (USA 2019–2020, China 2020–2021)
- SLI unit parity USA/Europe: IMMINENT — expected 2027–2028 at 14.84%/yr learning rate
- SLI unit parity China: NOT_MET — $100/unit vs. $25/unit target (4x gap); parity year 2031–2032

**Business model implications:**
The zero-content disruptor structure (0.0 kg Pb per BEV, per LFP-UPS installation, per EV forklift) means there is no substitution demand stream — all disruption appears as incumbent stream compression. Lead producers face declining volumes with no product substitution pathway.

The incumbent vicious cycle (tipping-synthesizer): at 80% → 50% utilization, lead-acid SLI fixed costs rise $20→$32/unit, compressing margins precisely as Li-ion SLI achieves unit cost parity. This death spiral mechanism is already ACTIVE in China's secondary smelter layer (22–35% utilization, xcurve-analyst).

The disruptor virtuous cycle (tipping-synthesizer): LFP cross-segment manufacturing subsidizes cost reduction across all three convergence vectors simultaneously — BEV, LFP-UPS, and EV forklift production share production lines with stellar energy BESS (battery energy storage systems) manufacturing, enabling faster cost reduction than any single application alone.

**Post-tipping revenue model shift:**
- Lead-acid SLI manufacturers face margin compression from both ends: volume decline (BEV penetration) and per-unit cost increase (utilization-driven fixed cost inflation)
- Recycling infrastructure becomes the last economic moat: 70% recycling rate threshold (capability) is the final MET condition outstanding; lead recyclers with low-cost smelting operations are the most durable incumbents

#### Lead Demand Commodity Dynamics

The 10 market products across 5 disruption vectors decompose as follows (demand-decomposer, 99.98% coverage = 12,256 of 12,259 kt):

| Market Product | 2024 Demand (kt) | Material Intensity | Disruption Vector |
|---|---|---|---|
| Automotive SLI new-vehicle | 1,404 | 13.0 kg/vehicle | Li-BEV (BEV new-car) |
| Automotive SLI aftermarket | 7,261 | 12.0 kg/event | Li-BEV (fleet replacement) |
| Telecom VRLA backup | 907 | 363 kg/site | LFP-UPS |
| Datacenter UPS | 503 | 2,010 kg/installation | LFP-UPS |
| Grid backup VRLA | 114 | model-derived | LFP-UPS (partial) |
| Lead-acid traction (forklifts) | 379 | 1,014 kg/unit | EV-FL |
| 2W/3W SLI | 1,010 | model-derived | LFP-SLI (pre-inflection) |
| Commercial vehicle SLI | 294 | model-derived | slow-moving |
| Non-battery lead | 1,691 | N/A | structural floor |
| Chimera (PHEV SLI) | 13 (2024) | 12.0 kg/vehicle | transient demand |

**3-stream demand projections (stream-forecaster, P50 median path):**

| Year | Incumbent Stream (kt) | Disruptor Stream (kt) | Chimera PHEV (kt) | Total (kt) |
|---|---|---|---|---|
| 2026 (baseline) | 11,041 | 0 | 54 | 11,095 |
| 2031 (+5yr) | 9,133 | 0 | 72 | 9,205 |
| 2036 (+10yr) | 7,223 | 0 | 49 | 7,272 |
| 2046 (+20yr) | 6,269 | 0 | 7 | 6,276 |

The chimera PHEV demand hump peaks in 2031 at 72 kt (0.78% of 9,205 kt total) — economically insignificant but confirming the chimera dynamics from fleet-modeler.

**Stock-flow fleet dynamics (fleet-modeler):**

The 4-fleet model (ICE passenger 1.266B vehicles, lead-acid forklifts 5.40M, VRLA telecom 9.99M sites, 2W batteries 294M) shows:
- OEM demand: 10% of total (shrinks fastest as BEV new-car penetration rises)
- Replacement demand: 69.1% of total (70% replacement-driven demand)
- Non-fleet (telecom, datacenter, grid): 20.5%
- Sharpest demand cliff: 2031–2036 (replacement demand 2,390→1,172 kt — a 51% drop in 5 years)
- All 4 fleet models pass consistency check (max deviation 0.01, fleet-modeler)

The 4-year SLI replacement cycle means that even full BEV sales saturation in 2028 would leave 4 years of aftermarket demand before the ICE fleet shrinks. This lag is the primary buffer against faster demand decline.

### Phase 6: Adoption and S-Curve Dynamics

**S-curve parameters (scurve-fitter, 5-segment fit):**

| Segment | L (ceiling) | k (steepness) | x0 (inflection year) | Current penetration (2024) | Phase | R² |
|---|---|---|---|---|---|---|
| BEV new-car sales | 85% | 0.3492 | 2028.83 | 11.96% | tipping | 0.9621 |
| BEV fleet share | 80% | 0.4155 | 2031.77 | 3.0% | rupture | 0.9979 |
| Telecom UPS Li-ion | 85% | 0.3659 | 2024.84 | ~33% | rapid growth (post-inflection) | 0.9620 |
| Datacenter UPS Li-ion | 90% | 0.2569 | 2024.90 | ~37% | rapid growth (post-inflection) | 0.9797 |
| EV forklift | 70.66% | 0.1891 | 2009.61 | 64.9% | rapid growth (near saturation) | 0.9351 |

**Composite 10% milestone:** 2028.1 (scurve-fitter), vs. stream-forecaster median 2027. The 7-month difference is explained by the scurve-fitter composite model not having access to the full 10-driver demand decomposition that the stream-forecaster used.

**Regional S-curve adoption (regional-adopter):**

| Region | BEV Share (2024) | x0 (year) | k | R² | Lead in Years vs. USA |
|---|---|---|---|---|---|
| China | 26.82% | 2025.4 | 0.4089 | 0.9551 | +4.1 years ahead |
| Europe | 18.62% | 2027.2 | 0.3558 | N/A | +2.4 years ahead |
| USA | 9.15% | 2029.6 | 0.3635 | N/A | baseline |
| RoW | 4.91% | 2029.6 | 0.4999 | N/A | parity with USA |
| India | ~2.1% | T3 only | N/A | N/A | rupture phase only |

China leads USA by 4.1 years in BEV S-curve adoption. India is in rupture phase only — 2W/3W vehicles comprise 64% of India demand and have no cost-curve-supported S-curve fit at T2.

**Incumbent decline dynamics (xcurve-analyst):**
- Aggregate level: Pre-disruption stage (2026 baseline = 100% of demand; demand decline has begun but the X-curve cross has not yet occurred)
- China: Death spiral ALREADY ACTIVE in secondary smelter layer — 22–35% utilization; feedstock shortfall of 6.9M tonnes (14.6M nameplate vs. 7.6M actual supply)
- Peak decline velocity: −7.7 pp/year in 2031–2032 (xcurve-analyst model-derived)
- 5-mechanism market trauma documented for China, USA, Europe (xcurve-analyst)

The China smelter situation is the leading indicator for global recycling infrastructure collapse: as BEV penetration removes SLI batteries from the used-battery supply chain, secondary smelters lose their primary feedstock. The China utilization drop (22–35%) is a T2-observed precursor to the full X-curve crossover expected in 2031–2032.

### Phase 7: Synthesis and Tipping Point

**Integrated tipping point assessment (tipping-synthesizer, all agents):**

Three conditions must be met for tipping. Each is evaluated by a dedicated checker agent:

| Condition | Non-SLI Segments | SLI USA/Europe | SLI China |
|---|---|---|---|
| Cost parity | MET (pre-2019) | IMMINENT (2027–2028) | NOT_MET (2031–2032) |
| Capability parity | MET (2019–2021) | PARTIAL (11/13 dims) | PARTIAL (11/13 dims) |
| Adoption readiness | MET | PARTIAL (EV corridor 59.1%) | MET |
| **Tipping status** | **TIPPED (2021–2024)** | **2027–2028** | **2031–2032** |
| **Binding constraint** | — | adoption_readiness | cost_parity |

**Rupture window:** 2027–2028 (global 10% threshold crossing on median path, stream-forecaster).

**Tipping mechanism:** USA EV highway corridor coverage reaches 80% in 2028 (model-derived, adoption-readiness-checker), co-binding with Li-ion SLI unit cost parity at $55/unit in USA (cost-parity-checker). When both trip simultaneously in 2027–2028, SLI automotive — the largest sub-domain at 8,665 kt combined — enters its tipping phase. The 62 kt gap between 2026 demand (11,095 kt) and the threshold (11,033 kt) is closed by this initial SLI displacement wave.

**Post-tipping dynamics (tipping-synthesizer):**
- Disruptor virtuous cycle: LFP cross-segment manufacturing scale reduces per-unit cost for all three convergence vectors simultaneously; BEV + stellar energy BESS + LFP-UPS + EV-FL production lines share manufacturing infrastructure
- Incumbent vicious cycle: $20→$32/unit fixed cost increase at 80%→50% utilization (documented for lead-acid SLI manufacturers); secondary smelters lose feedstock as BEV displaces ICE aftermarket batteries
- Completion timeline: 80% of disruption-addressable demand (10,568 kt) displaced by 2036–2041 (tipping-synthesizer model-derived)

**10% demand threshold crossing (authoritative answer — stream-forecaster):**
- 2024 baseline: 12,259 kt [T2: observed]
- 10% threshold: 11,033 kt (stream-forecaster)
- 2026 demand: 11,095 kt — 62 kt above threshold
- Median threshold crossing: **2027**
- Scenario range: 2027.4 (P25) – 2028.8 (P75) (scurve-fitter Monte Carlo envelope)

#### Lead Demand Commodity Summary

**Demand trajectory at key horizons (stream-forecaster, P50):**

| Horizon | Total Demand (kt) | vs. 2024 Baseline | Key Driver |
|---|---|---|---|
| 2026 | 11,095 | −9.5% | Non-SLI post-inflection collapse |
| 2027 | ~11,033 | −10.0% | **10% threshold crossing (median)** |
| 2031 | 9,205 | −24.9% | BEV fleet replacement demand cliff begins |
| 2036 | 7,272 | −40.7% | Replacement demand halved (2,390→1,172 kt) |
| 2046 | 6,276 | −48.8% | Structural floor approached |

**Structural floor:** ~6,276 kt (non-battery lead + residual ICE aftermarket + slow-declining 2W/3W markets). This floor declines at −0.3%/yr with no identified disruptor in the non-battery segment (demand-decomposer).

**Regional demand projections and sequence (regional-demand-analyst):**

| Region | 2026 Demand (kt) | 10% Threshold Crossing | 2036 Share | Structural Notes |
|---|---|---|---|---|
| China | 3,598 | ~2028.1 | declining | 2nd-largest BEV market; smelter death spiral ACTIVE |
| Europe | 1,700 | ~2028.9 | declining | BEV at 18.62% (2024) |
| USA | 1,689 | ~2029.6 | declining | EV corridor binding; NEVI rescission risk |
| RoW | 2,428 | ~2029.7 | declining | parity with USA timeline |
| India | 1,681 | ~2031.0 | rising to 17.7% by 2036 | 2W/3W structural lag; no T2 fit available |

India is the last to cross the 10%-from-2026 threshold (~2031.0) and rises to 17.7% of global demand by 2036 as all other regions decline faster. The India structural defense rests on the 2W/3W fleet (64% of India demand) which has no cost-curve-supported Li-ion S-curve fit at T2 — this is the primary data gap in the regional analysis.

**Cross-segment commodity implications:**
- Lead recycling infrastructure faces structural feedstock shortfall as BEV removes SLI batteries from the used-battery supply chain. China's 22–35% utilization precursor (xcurve-analyst) will propagate globally with a 3–4 year lag corresponding to the BEV-ICE S-curve gap between China and the rest of the world.
- Secondary lead smelters require full BEV fleet penetration at scale before feedstock collapse becomes acute globally — the 2031–2036 replacement demand cliff (fleet-modeler) is the inflection for global smelter utilization.
- The chimera PHEV hump (72 kt peak in 2031) provides a marginal buffer to the 2031 decline but is economically insignificant at 0.78% of total demand.

---

## Key Conclusion

Global lead demand will cross 10% below its 2024 level of 12,259 kt by **2027** (median path; scenario range 2027.4–2028.8). Demand is already at 11,095 kt in 2026 — only 62 kt above the 11,033 kt threshold — following the post-inflection collapse of telecom VRLA (907→441 kt) and datacenter UPS displacement (503→245 kt) as non-SLI segments move through S-curve rapid growth phase. The binding constraint for the final 62 kt is BEV new-vehicle SLI displacement: adoption readiness (USA EV highway corridor reaching 80% in 2028) co-binds with cost parity (Li-ion SLI unit reaching $55/unit in USA, 2027–2028). Non-SLI segments (37.5% of demand) have already tipped; SLI automotive (62.5%) tips in 2027–2028 for USA/Europe and 2031–2032 for China (cost_parity binding). Confidence: 0.82 — high agreement across all 15 agents; primary uncertainty in 2W/3W S-curve parameters (no T2 data) and NEVI guidance rescission (February 2025) impact on USA EV corridor build-out pace.

---

## Rupture Window

**2027–2028** — global lead demand 10% below 2024 baseline.

- Median threshold crossing: 2027 (stream-forecaster, full 10-driver demand model)
- S-curve composite milestone: 2028.1 (scurve-fitter, 5-segment composite)
- Interpolated tipping point: 2027.5 (tipping-synthesizer)
- Scenario range: 2027.4 (P25) – 2028.8 (P75) (scurve-fitter Monte Carlo envelope)

The 2027–2028 rupture window is the GLOBAL aggregate answer. Regional sequences: China ~2028.1 (first to cross from 2026 baseline); Europe ~2028.9; USA ~2029.6; India ~2031.0 (last, structural 2W/3W defense).

---

## Aggregated Confidence Score

**Final confidence: 0.82**

Calculation (from `lib.tipping_math.confidence_aggregate`):
- Step 1 — Base mean: 0.817 = mean(0.82, 0.88, 0.87, 0.82, 0.87, 0.84, 0.82, 0.82, 0.82, 0.75, 0.74, 0.85, 0.82, 0.80, 0.74) across all 15 agents
- Step 2 — Degradation penalty: 0.0 — no CRITICAL, HIGH, or MEDIUM agent failures
- Step 3 — Weakest-link cap: NOT APPLIED — no CRITICAL criterion failures in any compliance checklist
- Step 4 — Floor: not triggered (0.817 > 0.10)
- Step 5 — Final: 0.82 (rounded down from 0.817 for the interpretive synthesis step — stream-forecaster median reconciled against scurve-fitter scenario range)

Two lowest-confidence agents (xcurve-analyst: 0.74; regional-demand-analyst: 0.74) are both MEDIUM criticality. No confidence penalty applies.

---

## Risk Factors and Data Gaps

**Critical data gaps (aggregated from all agents):**
1. No T2 data on Li-ion penetration of 2W/3W market (India 64% of demand, RoW component) — largest regional uncertainty
2. No CV (commercial vehicle) S-curve fit — conservative estimate used (demand-decomposer)
3. No T2 regional breakdown for telecom/datacenter/forklift segment demand by region
4. PHEV global sales schedule ±20% uncertainty (stream-forecaster Monte Carlo)
5. Forklift fleet size ±22% uncertainty (fleet-modeler)
6. DOT NEVI guidance rescission (February 2025) — impact on USA EV corridor build-out pace unquantified; could delay adoption readiness from 2028 to 2029–2030
7. No levelized cost T1/T2 time series available for direct verification
8. Lead-acid 2024 pack cost is model-derived (catalog terminates at 2023 observed)
9. 18% terminal deviation in Li-ion cost fit (2024 actual below model curve) — if costs continue falling faster than model, SLI parity years advance

**Critical assumptions:**
1. BEV = 0.0 kg Pb per vehicle at all horizons — confirmed (demand-decomposer), but assumes no future BEV design incorporating lead
2. LFP-UPS = 0.0 kg Pb per installation
3. LFP traction = 0.0 kg Pb per forklift unit
4. ICE passenger car replacement cycle = 4.5 years (fleet-modeler)
5. Vehicle lifetime = 15 years (fleet-modeler)
6. Li-ion SLI incumbent target = $25/unit (China), $55/unit (USA) — if targets shift, parity years shift
7. Non-battery floor (~1,691 kt) declines at −0.3%/yr with no disruptor — structural assumption
8. EV forklift S-curve ceiling = 70.66% (post-inflection, catalog-fitted)
9. Total new vehicle sales = 72M/yr (flat through 2046) — if EV adoption reshapes total fleet size, demand changes non-linearly

---

## Regional Dynamics

**China** — Earliest threshold crossing (~2028.1). BEV new-car share 26.82% (2024, T2), x0=2025.4, 4.1 years ahead of USA. Non-SLI Li-ion ~50% telecom penetration. However, SLI China cost_parity is NOT_MET until 2031–2032 ($100/unit vs. $25/unit target). China secondary smelters already in death spiral at 22–35% utilization. China demand: 3,598 kt (32.4% of global, 2026 baseline).

**Europe** — Mid-field (~2028.9). BEV at 18.62% (2024), x0=2027.2. Adoption readiness PARTIAL. Europe demand: 1,700 kt. Policy support robust but cost-curve dynamics are the primary driver.

**USA** — Lagging (~2029.6). BEV at 9.15% (2024), x0=2029.6. Adoption readiness NOT_MET (EV corridor 59.1% as of Q4 2024; 80% threshold model-derived for 2028). NEVI guidance rescission (February 2025) introduces uncertainty — if corridor build-out stalls, USA threshold crossing could slip to 2030–2031. Cost parity IMMINENT (2027–2028). USA demand: 1,689 kt.

**India** — Last to cross (~2031.0). BEV ~2.1% (2024, T3 only). 2W/3W vehicles = 64% of India lead demand, with no T2 S-curve fit available. India rises to 17.7% of global demand by 2036 as faster-adopting regions decline. India represents the primary uncertainty band in the scenario range.

**RoW** — Parity with USA timeline (~2029.7). BEV 4.91% (2024), x0=2029.6.

---

## Sources

All 15 upstream agent outputs:

- `output/lead-demand-decline/agents/01-domain-disruption.md` — 12,259 kt baseline, 5 disruption vectors, 10% threshold
- `output/lead-demand-decline/agents/02a-cost-researcher.md` — Li-ion and lead-acid cost histories (T1/T2)
- `output/lead-demand-decline/agents/02b-cost-fitter.md` — Exponential fit R²=0.954, 16.81%/yr learning rate
- `output/lead-demand-decline/agents/03-capability.md` — 13-dimension capability matrix; 11/13 MET
- `output/lead-demand-decline/agents/04a-cost-parity.md` — Segment-level cost parity status
- `output/lead-demand-decline/agents/04b-cap-parity.md` — PARTIAL parity ruling; 3-cluster convergence
- `output/lead-demand-decline/agents/04c-adopt-readiness.md` — NOT_MET aggregate; USA corridor 59.1%
- `output/lead-demand-decline/agents/04d-tipping-synthesizer.md` — Tipping years, binding constraints, post-tipping dynamics
- `output/lead-demand-decline/agents/05a-scurve-fitter.md` — 5-segment S-curve fits; composite 10% milestone 2028.1
- `output/lead-demand-decline/agents/05b-regional-adopter.md` — Regional BEV S-curves; China 26.82%
- `output/lead-demand-decline/agents/05c-xcurve-analyst.md` — Incumbent X-curve; China smelter death spiral ACTIVE
- `output/lead-demand-decline/agents/07a-demand-decomposer.md` — 10-product demand tree; 99.98% coverage
- `output/lead-demand-decline/agents/07b-stream-forecaster.md` — 3-stream projections; 10% threshold 2027 (median)
- `output/lead-demand-decline/agents/07c-fleet-modeler.md` — OEM/replacement split; demand cliff 2031–2036
- `output/lead-demand-decline/agents/07d-regional-demand.md` — Regional demand breakdown; China first, India last
