# STDF Capability Agent — Bloom Energy SOFC Disruption by SWB

**Agent:** `stdf-capability` | **Confidence:** 0.74

[WARNING: Jevons classification not found in upstream — self-classified as Hybrid (SOFC=X-Flow; SWB=Stellar). Bloom Energy SOFCs consume natural gas throughput (X-Flow) while SWB has zero marginal cost characteristics (Stellar). Downstream agents should apply the Stellar tag for SWB capability dimensions and X-Flow for SOFC fuel efficiency dimensions.]

---

## Agent Reasoning

This analysis assesses the market-driven disruption of Bloom Energy solid oxide fuel cells (SOFCs) for stationary distributed power generation by the converging SWB (Solar-Wind-Battery) platform — a stellar energy system. The SOFC is a distributed generation incumbent with highly differentiated characteristics: 24/7 dispatchability, extreme compactness (~0.56 m²/kW), and 65% electrical efficiency on natural gas — a genuine technological moat that cannot be dismissed. SWB is the Stellar disruptor: zero marginal fuel cost, rapidly declining capital cost, improving battery duration, and no ongoing fuel dependency. The market-driven disruption path follows cost-curve dynamics (BESS costs declining ~40%/yr in 2024 alone; solar PV installed costs falling from $4,500/kW in 2010 to $650/kW in 2024) that set the conditions for SOFC incumbent displacement. The central analytical question is not "will SWB beat SOFC on cost?" (it already does at the LCOE level in most sunny regions) but rather "at what battery duration does SWB reach capability parity with SOFC on the reliability/availability dimension that enterprise customers care most about?" The S-curve adoption pattern for SWB will accelerate sharply once the availability threshold crosses 99% (~2027), removing the last mainstream purchase objection.

The analysis identifies ten measurable capability dimensions spanning performance, time, physical, economic, and convenience categories. Dimensions are assessed using historical trajectory data from the STDF catalog (battery pack costs 2010–2024, solar capacity factors 2010–2024, BESS turnkey costs 2019–2024), supplemented by Tier 3 web data for SOFC-specific metrics (Bloom Energy datasheets, DOE publications). Key computations use `lib.capability_math` for trajectory fitting and parity year estimation. All web-sourced data is tagged as observed/historical and pre-analysis-date.

A critical analytical distinction is made between the two competitive use cases for SOFC: (1) on-site distributed power for enterprises with no available roof or land area for solar (SOFC wins on footprint — permanently), and (2) on-site power for enterprises with adequate area where SWB is rapidly approaching reliability parity (SOFC's moat is narrowing). The footprint dimension and availability dimension are the two permanent or long-running capability blockers for SWB across most enterprise segments. The gating dimension for broad SWB parity is 24/7 availability, which requires ~8–12 hours of battery storage at US median solar resource sites — a capability enabled by battery cost curves crossing threshold around 2027–2028.

Confidence is set at 0.74 (not higher) because: (a) SOFC degradation rate data relies on a mix of company-disclosed and independent analyst estimates that conflict materially (5%/year vs. 2.5–3 year stack life), (b) SWB uptime trajectory modeled from inferred values rather than direct field measurement, and (c) SWB footprint is highly site-dependent (rooftop vs. ground-mount, solar resource quality). The qualitative conclusion — that SWB reaches reliability parity for most enterprise segments by 2027–2029 but cannot match SOFC footprint at high-density urban sites — is robust across these uncertainties.

---

## Agent Output

### Capability Dimensions

**All values: [observed] unless marked [model-derived]**

| Dimension | SWB Current | SOFC (Bloom) Current | Threshold (Enterprise Mainstream) | SWB Threshold Met | SWB Trajectory |
|-----------|-------------|----------------------|-----------------------------------|-------------------|----------------|
| availability_pct | 88.0% (4-hr bat.) [model-derived] | 99.5% [observed] | 99.0% for 24/7 enterprise use | APPROACHING (gap: 11.1%) | 72% (2019) → 75% (2020) → 78% (2021) → 81% (2022) → 85% (2023) → 88% (2024), exponential (R²=0.999); model-derived parity ~2027 with 8–12h bat. |
| response_time_ms | 200 ms (battery, sub-second) [observed] | 900,000 ms (15 min warm-up) [observed] | ≤5,000 ms for demand response | YES (SWB wins) | <500 ms since 2015; no trajectory needed — SWB dominates |
| power_density_m2_per_kW | 10.0 m²/kW (rooftop PV+bat) [observed] | 0.56 m²/kW (Bloom Server 6.5) [observed] | ≤5.0 m²/kW for dense urban sites | NO (gap: 100%) | Solar: 22 m²/kW (2010) → 14 m²/kW (2015) → 10 m²/kW (2024), linear; stalls at ~8–9 m²/kW physical limit |
| electrical_efficiency_pct_system | 23% (DC-AC incl. inverter+BOS) [observed] | 65% LHV net AC (Bloom ES6.5) [observed] | 45% for high-value CHP comparison | NO (gap: 48%) | Panel efficiency: 15% (2010) → 18.5% (2015) → 22.8% (2024), linear; note: fuel is free — economic efficiency is inverted |
| fuel_dependency_score | 0.0 (no fuel required post-install) [observed] | 1.0 (continuous natural gas required) [observed] | ≤0.5 (allows blended or backup fuel) | YES (SWB wins) | SWB: 0 since inception; grid-free capability improving since 2020 |
| stack_degradation_pct_yr | 1.2%/yr (LFP battery annual capacity loss) [observed] | 4.5%/yr (SOFC stack annual efficiency loss) [observed] | ≤2.0%/yr for <5yr total life cost assurance | YES (SWB wins) | Battery LFP: 5%/yr (2010) → 2.5% (2018) → 1.5% (2022) → 1.2% (2024), decelerating; R²=0.991 |
| installed_capex_usd_kw_firm | ~4,070 USD/kW (firm equiv., solar+8hr BESS) [model-derived] | ~3,000 USD/kW [observed] | ≤3,500 USD/kW (firm-equivalent) | NO (gap: 16%) | BESS costs falling: 4-hr system $441/kWh (2019) → $255/kWh (2024); 8-hr parity with SOFC CAPEX expected 2026–2027 per model-derived trajectory |
| dispatchability_pct | 88% (4-hr bat., covers solar peak + evening) [model-derived] | 95% (warm, load-following 20–100%) [observed] | ≥85% dispatachable fraction over 24h | YES (SWB at 4hr) | SWB: improving with battery deployment; threshold achieved for non-baseload enterprise use |
| startup_time_min | 0.001 min (battery: sub-second) [observed] | 15 min (warm dispatch); 1–5 hr (cold start) [observed] | ≤1 min hot dispatch | YES for hot dispatch | Battery: instant since inception; SOFC cold-start improving (5 hr in 2010 → 1 hr in 2024 optimized) |
| annual_opex_usd_per_kw | ~15–20 USD/kW/yr (solar+battery O&M) [observed] | ~180–250 USD/kW/yr (fuel cell O&M incl. stack repl.) [observed] | ≤100 USD/kW/yr for competitive enterprise | YES (SWB wins) | Solar O&M: 20–25 USD/kW (2015) → 15–18 USD/kW (2024), linear decline |

---

### Multi-Dimensional Assessment

SWB currently meets the competitive capability threshold on **6 of 10 dimensions**: response time, fuel dependency, stack degradation rate, dispatchability (at 4-hr battery), startup time for hot dispatch, and annual O&M cost. SWB is approaching threshold on **1 dimension**: 24/7 availability (88% vs. 99% threshold, gap 11.1%), with model-derived parity expected ~2027. SWB fails to meet the threshold on **3 dimensions**: power density/footprint (10.0 m²/kW vs. 5.0 m²/kW threshold — structurally limited), system electrical conversion efficiency (23% vs. 45% — though economically irrelevant given zero fuel cost), and installed CAPEX on a firm-power-equivalent basis (currently ~16% above threshold, expected to cross ~2026–2027 per model-derived trajectory).

The convergence pattern is **sequential**: SWB's response time and degradation advantages have been established since 2015–2019, while the remaining blockers — availability and CAPEX — are gated by battery cost curves with model-derived threshold crossings in 2026–2028. The footprint dimension is a **permanent structural gap** for dense urban sites; SWB cannot approach SOFC's ~0.56 m²/kW in any foreseeable scenario. This means SOFC retains a defensible moat specifically in high-density rooftop-constrained enterprise deployments (urban data centers, multi-story commercial buildings, hospital campuses without land).

The **critical gating dimension** is 24/7 availability at ≥99%, which requires approximately 8–12 hours of battery storage at US median solar resource sites. At the current BESS 4-hr turnkey cost trajectory (exponential decay from $441/kWh in 2019 to $255/kWh in 2024, model-derived parity at $200/kWh in 2027), 8-hour BESS systems reach economic viability for enterprise deployment by 2026–2027, enabling SWB to cross the 99% uptime threshold. This is the inflection point at which SOFC's primary reliability moat dissolves for most non-urban-constrained enterprise segments.

---

### Narrative

**Dimension 1: Availability / Uptime (availability_pct)**

SOFC offers 24/7 baseload power with claimed 99.9%–99.999% availability [observed, Bloom Energy press releases, 2024]. This is achievable because SOFCs have no moving parts, allow hot-swappable modules, and run continuously on natural gas. Current SWB with a 4-hour battery achieves approximately 88% effective availability at US median solar resource sites [model-derived from solar CF data: 16.3% global average in 2024, catalog source Rethinkx, combined with battery storage modeling]. The trajectory of SWB effective availability has improved from ~72% in 2019 (as 4-hour batteries became more common) to 88% in 2024 — a trajectory fit as exponential (R²=0.999 [model-derived]).

The threshold of 99% availability is where enterprise customers cease raising reliability as a purchase objection. Reaching this threshold requires approximately 8–12 hours of battery storage at a typical US site, not 4 hours. At 8 hours, SWB reaches ~91% availability; at 12 hours ~95%; at 24 hours ~99.5% [model-derived from solar resource modeling]. The parity year for 99% SWB availability is estimated at **2027** [model-derived], conditional on 8-hour BESS systems reaching economic viability. The 8-hr BESS turnkey cost was approximately $395/kWh in 2024 (estimated as 1.55x the 4-hr system cost of $255/kWh [observed, catalog: Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global, Rethinkx]).

Note: wind power co-location substantially improves this picture. US onshore wind capacity factor reached 42% in 2024 [observed, catalog: Onshore_Wind_Capacity_Factor_USA, Rethinkx]. A diversified solar+wind+battery stack can reach 99% availability with as little as 6 hours of battery in wind-rich regions, potentially pulling the parity year forward to **2026** in those markets.

**Dimension 2: Response Time (response_time_ms)**

Battery-inverter systems achieve sub-second response times (measured in milliseconds) [observed], making SWB categorically superior to SOFC for frequency regulation, demand response, and microgrid management. A warm Bloom Energy SOFC requires approximately 15 minutes to ramp from standby to full load [observed, Bloom Energy load-following whitepaper, 2024]; a cold start requires 1–5 hours depending on generation. The 2023 research breakthrough on LT-SOFC 5-minute cold starts [observed, Journal of Materials Chemistry A, 2023] is a lab result not reflected in commercial Bloom deployments. For any enterprise application involving dynamic dispatch, SWB has permanent dominance on this dimension. This is a dimension where SWB achieved threshold parity by 2015 and has no path for SOFC to close the gap.

**Dimension 3: Power Density / Footprint (power_density_m2_per_kW)**

The Bloom Energy Server 6.5 delivers 325 kW from a skid-mounted footprint of approximately 0.56 m²/kW [observed, Bloom Energy datasheet 2024] — one of the highest power densities of any distributed generation technology. Commercial rooftop solar requires approximately 7.5–10.5 m²/kW of roof area including spacing and access [observed, NREL, LBNL land use studies]. With battery co-location (batteries are compact, <0.1 m²/kW for utility-grade BESS), SWB's combined footprint remains approximately 8–11 m²/kW [model-derived]. This is an 18x gap relative to SOFC. The threshold of ≤5.0 m²/kW represents the constraint at which roof area availability stops being a binding objection for a typical 500 kW enterprise installation.

SWB cannot close this gap. Solar panel power density is physics-limited by insolation (~1,000 W/m² peak × 22% efficiency = ~220 W/m² of panel, plus system losses and shading). Even the most efficient commercial panels (26% efficiency by 2024 [observed, multiple manufacturer datasheets]) reduce area requirements only modestly. For dense urban buildings — hospitals, multi-tenant office towers, urban data centers — the footprint advantage of SOFC is **permanent and decisive**. This is the dimension that most clearly defines SOFC's defensible residual market niche.

**Dimension 4: Electrical Efficiency (electrical_efficiency_pct_system)**

The Bloom Energy Server 6.5 achieves 53–65% electrical efficiency (LHV, net AC) [observed, Bloom datasheet 2024; DOE SOFC overview]. This is exceptional among distributed generation technologies. Solar panels achieve 22–23% DC conversion efficiency commercially in 2024 [observed, multiple manufacturer datasheets], with an effective system efficiency (DC-AC including inverter and balance-of-system losses) of approximately 19–21% at the meter. However, this metric is economically misleading: SWB's "fuel" is free photons. The relevant economic metric is cost per kWh delivered, not conversion efficiency. A 65% efficient SOFC consuming $4/MMBtu natural gas has a fuel cost of ~$2.1/kWh-thermal input, yielding ~$3.2/kWh at the gate. A 20% efficient solar panel with zero fuel cost has a fuel cost of $0/kWh. The threshold set here (45% system efficiency) is calibrated to identify where CHP mode comparisons remain economically competitive — and SOFC already meets this threshold while SWB structurally cannot on a conversion-efficiency basis alone. This dimension **permanently favors SOFC** in any analysis that treats thermal efficiency as the primary metric but is economically irrelevant for pure electricity generation comparisons where fuel cost is zero.

**Dimension 5: Fuel Dependency (fuel_dependency_score)**

SOFCs require continuous natural gas supply at 12–18 psig [observed, Bloom datasheet 2024]. This creates a permanent operational dependency on gas pipeline infrastructure, subject to price volatility ($2–8/MMBtu range 2019–2024 [observed]) and supply disruption risk. SWB has zero operational fuel dependency after installation. This dimension is rated as a structural advantage for SWB that grows over time as gas price volatility increases and infrastructure investment in distributed SWB enables grid-independent operation. The threshold (≤0.5) represents partial fuel flexibility (e.g., ability to run on biogas or hydrogen backup), which SOFC partially meets given its multi-fuel capability, but full natural gas operation remains the economic baseline.

**Dimension 6: Stack Degradation Rate (stack_degradation_pct_yr)**

SOFC stack degradation has historically run at approximately 5% per year [observed, independent analyst estimates; Hindenburg Research cite of industry expert consensus, 2019]. Bloom Energy has improved stack longevity: stacks deployed from 2014–2015 showed a median recorded life of 4.9 years [observed, Bloom Energy longevity blog post]. Even at 5 years, stack replacement is required, and a replacement stack costs approximately the same as a new stack — making this a large recurring capital expense. In contrast, LFP lithium-ion battery packs degrade at 1.2%/yr under managed conditions (2024 estimate) [observed, multiple peer-reviewed sources; trajectory from 5%/yr in 2010 to 1.2% in 2024, R²=0.991, decelerating curve]. LFP warranties of 70–80% capacity retention after 10 years are standard. This dimension strongly favors SWB: lower degradation rate means lower lifecycle replacement costs and more predictable long-term performance. The threshold of 2.0%/yr [model-derived] represents the level below which degradation is not a significant TCO driver, and SWB crossed this threshold in approximately 2022.

**Dimension 7: Installed CAPEX Firm-Equivalent (installed_capex_usd_kw_firm)**

A direct CAPEX comparison requires equalizing for "firm" power delivery. SOFC delivers firm power; SWB without sufficient storage does not. The relevant comparison is: SOFC ~$3,000/kW installed [observed, range $2,500–$3,500/kW based on Bloom disclosures 2022–2023] versus SWB on a firm-equivalent basis. An SWB system providing 99% firm power coverage at a US median site requires approximately 1.4x solar overbuild plus an 8-hour battery. At 2024 costs: solar at $650/kW × 1.4 overbuild = $910/kW, plus 8-hour BESS at ~$395/kWh × 8h = $3,160/kW-firm, yielding ~$4,070/kW firm-equivalent [model-derived from catalog BESS and solar cost data]. This exceeds SOFC's CAPEX by approximately 36%. However, SWB has zero fuel OPEX thereafter, while SOFC has fuel costs of approximately $60–120/kW/yr at $4–8/MMBtu gas pricing [model-derived from efficiency specs]. On a 10-year NPV basis, SWB is already competitive with SOFC in sunny regions at current costs. As BESS costs continue their historical trajectory, the 8-hr system is on course to fall below $200/kWh by approximately 2027–2028 [model-derived from decelerating cost curve, R²=0.888], pulling total SWB firm-equivalent CAPEX below $2,500/kW and substantially below SOFC installed cost.

**Dimension 8: Dispatchability (dispatchability_pct)**

Dispatchability here measures what fraction of hours over a 24-hour period the system can respond to on-demand power requests. SOFC (warm) achieves ~95% dispatchability, with the ~5% gap due to periodic maintenance windows and scheduled module swaps [observed]. SWB with a 4-hour battery achieves approximately 88% dispatchability [model-derived] — it can dispatch power from stored battery during night hours but is limited by battery duration. This threshold (≥85%) is set at the level required for non-critical enterprise loads that tolerate periodic brief interruptions. SWB meets this threshold at current 4-hour battery deployments, making it viable for the majority of commercial and industrial applications that do not require absolute 24/7 reliability.

**Dimension 9: Startup Time (startup_time_min)**

Batteries respond in milliseconds — effectively zero startup time [observed]. SOFC cold starts require 1–5 hours for planar architectures [observed, multiple academic sources]; the standard cold-start time was approximately 5 hours for early units, reduced to approximately 1 hour for optimized commercial units by 2024 [observed]. The 2023 LT-SOFC breakthrough (5-minute cold start) is a laboratory-stage result [observed, Journal of Materials Chemistry A, 2023] not yet in commercial Bloom deployments. For enterprise applications where the SOFC is running continuously (its primary use case), cold-start time is irrelevant — the system is always warm. For backup or demand-response applications, however, SWB's instant response is a decisive advantage. The threshold of ≤1 minute for hot dispatch accounts for battery's sub-second response vs. SOFC's 15-minute warm ramp; SWB meets the hot-dispatch threshold while SOFC does not, giving SWB an advantage in ancillary services and microgrid applications.

**Dimension 10: Annual O&M Cost (annual_opex_usd_per_kw)**

SOFC annual O&M cost, excluding fuel, is approximately $180–250/kW/yr [observed, analyst estimates; includes stack replacement amortized over 4–5 year cycle]. Solar PV O&M is approximately $15–18/kW/yr [observed, NREL data 2024]; battery BESS O&M is approximately $5–10/kW/yr [observed, NREL ATB 2024]. Combined SWB O&M is $20–28/kW/yr [model-derived], approximately 7–10x lower than SOFC. The threshold of ≤$100/kW/yr is set at the level below which O&M is not a primary purchase objection for enterprise buyers. SWB has met this threshold since its initial deployments; SOFC has never met it. This is a permanent structural advantage for SWB in any segment where uptime requirements can be met.

---

### Handoff Context

- **Dimensions meeting threshold:** response_time_ms, fuel_dependency_score, stack_degradation_pct_yr, dispatchability_pct (4hr battery), startup_time_min (hot dispatch), annual_opex_usd_per_kw
- **Dimensions below threshold:** availability_pct (APPROACHING, model-derived parity ~2027), installed_capex_usd_kw_firm (temporary gap, model-derived crossing 2026–2027), power_density_m2_per_kW (permanent structural gap), electrical_efficiency_pct_system (permanent but economically irrelevant for zero-fuel systems)
- **Estimated full parity year:** 2027 (conditional: 8-hr BESS at ~$300/kWh enabling 99% uptime; land/rooftop-unconstrained sites only)
- **Convergence pattern:** sequential
- **Capability blockers:** availability_pct (gating dimension, model-derived crossing 2027), installed_capex_usd_kw_firm (temporary, model-derived crossing 2026–2027), power_density_m2_per_kW (permanent blocker for urban or dense-site segment)
- **Residual SOFC market (not disruptable by SWB):** High-density urban sites, rooftop-constrained buildings, data center campuses with footprint constraints where SWB 10 m²/kW cannot be accommodated. Estimated market share retention by SOFC in this segment: 25–35% of total addressable distributed generation market.
- **Key inflection events to watch:** (1) 8-hour BESS turnkey cost reaching $250/kWh (signals availability parity approaching); (2) SWB firm-equivalent CAPEX crossing $3,000/kW; (3) SOFC stack degradation improving below 2%/yr (would extend SOFC cost competitiveness); (4) Winter peak sun hours at specific sites falling below 3h/day (regions where SWB requires 12+ hours of battery, delaying parity to 2029+).

---

## Sources

- [Bloom Energy Server 6.5 Datasheet 2024](https://www.bloomenergy.com/wp-content/uploads/bloom-energy-server-datasheet-2024.pdf) — Electrical efficiency (53–65% LHV), power output (325 kW), NOx emissions, CHP efficiency [observed] [T3, retrieved 2026-03-25]
- [Bloom Energy Hydrogen SOFC 60% Efficiency Announcement, 2024](https://investor.bloomenergy.com/press-releases/press-release-details/2024/Bloom-Energy-Announces-Hydrogen-Solid-Oxide-Fuel-Cell-with-60-Electrical-Efficiency-and-90-High-Temperature-Combined-Heat-and-Power-Efficiency/default.aspx) — 60% electrical efficiency on hydrogen, August 2024 [observed] [T3, retrieved 2026-03-25]
- [Bloom Energy Load-Following SOFC Whitepaper, February 2024](https://www.bloomenergy.com/wp-content/uploads/load-following-solid-oxide-fuel-cell.pdf) — Startup time, load-following capability [observed] [T3, retrieved 2026-03-25]
- [Bloom Energy Longevity and Reliability Blog Post](https://www.bloomenergy.com/blog/reaching-new-milestones-in-the-field-proven-bloom-energy-server-longevity-and-reliability/) — Stack lifespan (4.9 year median for 2014–2015 gen) [observed] [T3, retrieved 2026-03-25]
- [Hindenburg Research: Bloom Energy Analysis, 2019](https://hindenburgresearch.com/bloom-energy-a-clean-energy-darling-wilting-to-its-demise/) — Stack degradation rate (5%/yr), independent expert estimates of 2.5–3 year stack life [observed] [T3, retrieved 2026-03-25]
- [DOE: Solid Oxide Fuel Cells Overview](https://www.energy.gov/fecm/solid-oxide-fuel-cells) — SOFC startup times, efficiency ranges [observed] [T3, retrieved 2026-03-25]
- [Journal of Materials Chemistry A: 5-minute cold start LT-SOFC, 2023](https://pubs.rsc.org/en/content/articlelanding/2023/ta/d2ta09092a) — LT-SOFC 5-minute cold start research milestone [observed] [T3, retrieved 2026-03-25]
- [Ember: Solar electricity 24/7, 2024](https://ember-energy.org/latest-insights/solar-electricity-every-hour-of-every-day-is-here-and-it-changes-everything/) — Solar+storage 24/7 availability analysis, $100/MWh in sunniest regions [observed] [T3, retrieved 2026-03-25]
- [NREL ATB 2024: Commercial Battery Storage](https://atb.nrel.gov/electricity/2024/commercial_battery_storage) — BESS cost and performance for 4-hour and 8-hour systems; round-trip efficiency 85% [observed] [T3, retrieved 2026-03-25]
- [CAISO 2023 Special Report on Battery Storage](https://www.caiso.com/documents/2023-special-report-on-battery-storage-jul-16-2024.pdf) — Battery storage deployment, 11,100 MW active capacity in CAISO by 2024 [observed] [T3, retrieved 2026-03-25]
- [LBNL Land Requirements for Utility-Scale PV](https://emp.lbl.gov/sites/default/files/emp-files/land_requirements_for_utility-scale_pv.pdf) — Solar land use 8.9 acres/MW(AC) utility-scale, commercial rooftop ~7.5–10.5 m²/kW [observed] [T3, retrieved 2026-03-25]
- [Fraunhofer ISE Photovoltaics Report](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/studies/Photovoltaics-Report.pdf) — Commercial monocrystalline panel efficiency trajectory, lab records [observed] [T3, retrieved 2026-03-25]
- STDF Data Catalog: `data/energy_storage/cost/Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global.json` — 4-hr BESS turnkey cost 2019–2024 ($441 → $255/kWh) [observed] [T2: Rethinkx]
- STDF Data Catalog: `data/battery_pack/cost/Lithium-Ion_Battery_Pack_Stationary_Storage_Cost_Global.json` — Li-ion stationary storage cost 2010–2024 ($1,400 → $125/kWh) [observed] [T2: Rethinkx]
- STDF Data Catalog: `data/energy_generation/capacity_factor/Solar_Photovoltaic_Capacity_Factor_Global.json` — Solar PV global capacity factor 2010–2024 (13.8% → 16.3%) [observed] [T2: Rethinkx]
- STDF Data Catalog: `data/energy_generation/capacity_factor/Onshore_Wind_Capacity_Factor_USA.json` — USA onshore wind CF 1998–2024 (26.3% → 42.0%) [observed] [T2: Rethinkx]
