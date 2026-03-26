---
name: sofc_swb_capability_benchmarks
description: Bloom Energy SOFC vs SWB capability benchmarks — 10 dimensions, all thresholds, parity years, permanent gaps (validated 2026-03-25)
type: project
---

## SOFC vs SWB (Solar+Wind+Battery) Capability Benchmarks

Validated for distributed/on-site power generation, enterprise segment. Analysis date: 2026-03-25.

### Bloom Energy SOFC (Server 6.5) Key Specs [observed]
- Electrical efficiency: 53–65% LHV net AC (natural gas); 60% on hydrogen (2024)
- Power output: 325 kW per server
- Footprint: ~0.56 m²/kW (one of the most compact distributed generation technologies)
- Availability: 99.9%–99.999% (hot-swap modules, no moving parts)
- Warm dispatch: ~15 min (load-following 20–100%)
- Cold start: 1–5 hr (commercial); LT-SOFC lab: 5 min (2023 research only)
- Stack degradation: ~4.5–5%/yr historical; median stack life 4.9 yr (2014–2015 gen)
- Annual O&M (excl. fuel): ~$180–250/kW/yr
- Installed CAPEX: ~$3,000/kW (range $2,500–3,500, 2022–2023)
- Fuel: natural gas at 12–18 psig (continuous)
- CHP efficiency: >90%

### SWB (Solar+Battery) Key Specs (2024)
- Availability: 88% effective (4-hr battery); 91% (8-hr); 95% (12-hr); 99.5% (24-hr)
- Footprint: ~10 m²/kW (rooftop commercial); physics-limited to ~8–9 m²/kW
- Response time: sub-second (<200 ms for battery dispatch)
- Panel efficiency: 22.8% commercial; 26.0% lab record (2024)
- Battery degradation (LFP): 1.2%/yr (2024), down from 5%/yr in 2010
- Annual O&M: ~$20–28/kW/yr (solar + battery)
- BESS 4-hr turnkey cost: $255/kWh (2024); $441/kWh (2019)
- BESS 8-hr cost: ~$395/kWh (2024, estimated 1.55x 4-hr)
- SWB firm-equivalent CAPEX: ~$4,070/kW (solar overbuild 1.4x + 8-hr BESS, 2024)
- Wind CF USA: 42% (2024); onshore wind adds >10 percentage points to SWB uptime

### Capability Threshold Table
| Dimension | SWB Status | Threshold | Parity Year |
|-----------|-----------|-----------|-------------|
| availability_pct | APPROACHING (88% vs 99%) | 99.0% | 2027 [model-derived] |
| response_time_ms | YES | ≤5,000 ms | achieved 2015 |
| power_density_m2_per_kW | NO (PERMANENT) | ≤5.0 m²/kW | never |
| electrical_efficiency_pct | NO (PERMANENT but irrelevant) | 45% | never (zero fuel cost) |
| fuel_dependency | YES | ≤0.5 | achieved at inception |
| stack_degradation_pct_yr | YES | ≤2.0%/yr | crossed 2022 |
| installed_capex_usd_kw_firm | NO (temporary) | ≤3,500/kW | ~2026–2027 |
| dispatchability_pct | YES (4hr) | ≥85% | achieved 2022 |
| startup_time_min | YES (hot) | ≤1 min hot | achieved |
| annual_opex_usd_per_kw | YES | ≤100/kW/yr | achieved at inception |

### Convergence Pattern: Sequential
- Most dimensions already met by SWB
- Gating dimension: availability_pct (needs 8–12hr battery)
- Parity year: 2027 for non-footprint-constrained sites
- Permanent SOFC moat: footprint (0.56 vs 10 m²/kW) in dense urban/data center sites

### Key Data Sources
- STDF Catalog: Battery_Energy_Storage_System_(4-hour_Turnkey)_Cost_Global (Rethinkx)
- STDF Catalog: Lithium-Ion_Battery_Pack_Stationary_Storage_Cost_Global (Rethinkx)
- STDF Catalog: Solar_Photovoltaic_Capacity_Factor_Global (Rethinkx)
- STDF Catalog: Onshore_Wind_Capacity_Factor_USA (Rethinkx)
- Bloom Energy Server 6.5 Datasheet 2024 (bloomenergy.com)
- NREL ATB 2024: Commercial Battery Storage
- Hindenburg Research Bloom Energy analysis (2019) — stack degradation data

**Why:** Reference for any STDF analysis involving distributed power generation, on-site power, data center power, or SOFC/fuel cell incumbent displacement.
**How to apply:** Use these thresholds and parity years directly in downstream agents. The footprint gap is permanent — do not model SWB winning the urban-constrained segment.
