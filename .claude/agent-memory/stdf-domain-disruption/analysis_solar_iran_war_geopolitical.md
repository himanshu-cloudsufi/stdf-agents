---
name: Solar Energy Disruption — Iran War Geopolitical Context Analysis (March 2026)
description: Energy sector solar PV disruption analysis with Iran war as geopolitical shock scenario; four-channel impact model; LCOE sensitivity table; SWB convergence
type: project
---

Analysis completed: March 2026. Output: `output/how-will-iran-war-impact-solar-20260323-215917/agents/01-domain-disruption.md`

Sector: Energy
Sub-domains: utility-scale solar PV electricity generation, CCGT gas-fired, coal-fired, oil-fired (MENA), grid-scale BESS

**Why:** Query explicitly asked for Iran war scenario effect on solar disruption — requires both baseline solar disruption analysis AND geopolitical shock channel modeling against observed analogues (2022 Russia-Ukraine).

**How to apply:** When a query combines energy disruption with geopolitical risk scenarios (Middle East conflict, oil price shock, Hormuz closure), use this four-channel framework. The asymmetric fuel cost sensitivity model is the core insight: solar LCOE is structurally insensitive to gas/oil price shocks; CCGT LCOE scales at $6.5/MWh per $1/MMBtu gas price.

---

## Key Data Anchors

### Solar PV Baseline
- Installed cost (Global): $5,310/kW (2010) → $700/kW (2024); annual decay 14.6%/yr, R²=0.986; learning rate 30.8%/doubling [T2: Rethinkx]
- Installed capacity: 41 GW (2010) → 1,865 GW (2024); CAGR 31.3% [T2: Rethinkx]
- Solar generation 2024: 2,131 TWh = 6.9% of global 30,856 TWh [T1: Ember 2025]
- Module price 2024: $0.13/W [T3: Fraunhofer ISE/CPIA, observed]
- S-curve phase: Growth phase (6.9% share, 28%/yr growth)
- Disruption type: Big Bang (most markets) + From Below (MENA)

### BESS Baseline
- 2-hr turnkey cost (Global): $441/kWh (2019) → $269/kWh (2024) [T2: Rethinkx]
- China BESS 2024: $101/kWh [T2: Rethinkx]
- CAGR: 72%/yr (2010-2024)
- S-curve phase: Early Adopter

### Gas Generation
- Global gas power gen peaked: 6,312 TWh (2022) → 6,278 TWh (2024); -0.5% from peak [T2: Rethinkx]
- First confirmed post-peak signal for global gas power generation

### Iran Geopolitical Data
- Iran oil exports: ~1.6 Mbpd (2024) [T3: US EIA, observed]
- Hormuz transit: ~20 Mbpd = 20% global consumption [T3: US EIA, observed]
- Hormuz bypass capacity: ~2.6 Mbpd (Saudi+UAE pipelines)
- Net Hormuz closure shock: 17.4 Mbpd = 17% of global demand
- MENA oil-fired electricity: 20% of regional generation, ~1.8 Mbpd [T3: IEA, observed]

### LCOE Sensitivity Table (CCGT vs Solar)
| Gas Price | CCGT LCOE | Solar LCOE | Ratio |
|---|---|---|---|
| US $2.19/MMBtu | $29/MWh | $44/MWh | CCGT cheaper |
| EU $10.89/MMBtu | $86/MWh | $44/MWh | Solar 1.9x |
| Conflict $20/MMBtu | $145/MWh | $44/MWh | Solar 3.3x |
| Conflict $30/MMBtu | $210/MWh | $44/MWh | Solar 4.8x |
| Peak 2022 $37.52/MMBtu | $259/MWh | $44/MWh | Solar 5.9x |

### Chimeras Identified
- Gas-solar hybrid plants (Hybrid X-Flow + Stellar)
- Coal + CCS
- Small modular reactors (SMR): $7,000-15,000/kW, 10-20yr build

### Convergence Labels
- SWB: Solar PV + Wind + BESS (primary)
- IRES: Intermittent Stellar Generation + Storage + Smart Grid
- SWB-Middle East: SWB applied to MENA high-irradiance context ($25-35/MWh LCOE)

### Four-Channel Iran War Impact Model
1. Fuel price shock: widens solar LCOE advantage vs CCGT (primary channel, quantified above)
2. MENA oil-fired generation: direct sub-domain disruption (20% of MENA power from oil)
3. Supply chain: transient headwind only (China manufacturing unaffected; shipping delay 14 days)
4. Energy security capital allocation signal: compresses S-curve adoption timeline (2022 Ukraine analogue)

### US Exception
US domestic gas at $2.19/MMBtu means CCGT LCOE ($29/MWh) is cheaper than solar ($44/MWh). US is the only major market where solar has not yet crossed raw LCOE parity for new builds without storage. Iran war does not directly disrupt US domestic gas supply.
