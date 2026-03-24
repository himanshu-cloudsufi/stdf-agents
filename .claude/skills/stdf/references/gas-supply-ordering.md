# Gas Supply Source Ordering Methodology

Reference specification for the `stdf-gas-supply-decomposer` agent. Defines how to decompose gas demand reduction into supply-source impacts and model LNG displacement cascades.

## Core Principle

When gas demand falls (due to SWB displacement + electrification), the **most expensive supply source is eliminated first**. The cheapest source is served last and displaced last.

For each importing region, the gas supply stack has a cost ordering. LNG is almost always the most expensive source (liquefaction + shipping + regasification costs) and is therefore displaced first.

---

## GWh to BCM Conversion

```
Gas_BCM = Gas_Generation_GWh × 3.6 / (heat_rate × efficiency)
```

Where:
- 3.6 converts GWh to TJ (1 GWh = 3.6 TJ)
- heat_rate = 35.3 MJ/m³ (lower heating value of natural gas)
- efficiency = 0.45 for CCGT, 0.35 for OCGT

Use `lib.energy_math.gwh_to_bcm()`.

**Example**: 1,000 GWh gas generation = 1000 × 3.6 / (35.3 × 0.45) / 1000 = 0.227 BCM

---

## Regional Gas Supply Stacks

### China

**Key insight from Tony**: Coal ALWAYS dispatches before gas in China. Even when gas is needed, China's own domestic production + pipeline imports are always cheaper than LNG. China LNG imports approach **zero** as SWB eliminates remaining gas generation.

**Supply source ordering** (cheapest first, displaced last):

| Priority | Source | Cost Rank | Notes |
|----------|--------|-----------|-------|
| 5 (last displaced) | Domestic conventional gas | Cheapest | Sichuan, Ordos basins |
| 4 | Domestic coal-to-gas (syngas) | Cheap | Coal gasification plants in Xinjiang, Inner Mongolia |
| 3 | Pipeline — Central Asia | Moderate | Turkmenistan via Central Asia-China pipeline |
| 2 | Pipeline — Russia | Moderate | Power of Siberia pipeline |
| 1 (first displaced) | **LNG imports** | **Most expensive** | Spot + long-term contracts (Australia, Qatar, US) |

**China LNG → Zero mechanism**: As SWB displaces gas generation (gas is displaced first because coal MC $35 < gas MC $70), total gas demand falls. Domestic production + pipeline imports satisfy remaining demand at lower cost. LNG, as the marginal (most expensive) source, is eliminated entirely.

### Europe

**Supply source ordering** (cheapest first, displaced last):

| Priority | Source | Cost Rank | Notes |
|----------|--------|-----------|-------|
| 4 (last displaced) | Domestic — North Sea | Cheapest | Declining production (Netherlands, UK, Norway offshore) |
| 3 | Pipeline — Norway | Cheap | No liquefaction cost, short distance |
| 2 | **LNG — Qatar** | Moderate | Lower extraction cost but long shipping distance |
| 1 (first displaced) | **LNG — US** | **Most expensive** | Liquefaction + Atlantic shipping + regasification |

**Europe LNG displacement cascade**: As SWB + offshore wind + heat pumps reduce gas demand, US LNG is displaced first (highest delivered cost), then Qatar LNG. Norwegian pipeline gas is displaced last.

### USA

USA is a **net LNG exporter**. Domestic shale gas production is abundant. LNG imports are minimal.

| Priority | Source | Notes |
|----------|--------|-------|
| 3 (last displaced) | Domestic shale gas | Henry Hub pricing, abundant |
| 2 | Pipeline — Canada | Cross-border |
| 1 (first displaced) | LNG imports | Minimal volume |

**USA export exposure**: As global LNG demand craters (China → zero, Europe declining), US LNG export terminals face stranded capacity. This is a supply-side trauma, not a demand-side one for the US domestic market.

---

## LNG Exporter Vulnerability

### Qualitative Risk Tiers

| Risk Level | Companies | Reason |
|------------|-----------|--------|
| **High** | Venture Global, Woodside (post-Turan), NextDecade, New Fortress, Golar | Spot sales exposure, projects not yet at FID or recently sanctioned |
| **Lower** | Cheniere | Take-or-pay contracts through 2040s provide revenue floor |

### Financial Cascade Logic

When LNG demand falls:
1. **Spot prices collapse** below $5/MMBtu (oversupply)
2. **Marginal exporters** cannot recover liquefaction + shipping costs
3. **Project cancellations** cascade (FID deferrals, construction halts)
4. **Stranded infrastructure** — terminals built for 30-year life face <50% utilization
5. **No stabilization** — unlike the StellarEdge AI's claim, the market does NOT stabilize at 50-60% of peak because the financial cascade eliminates the supply-side response mechanism

---

## Non-Power Gas Demand

Gas demand is not only for electricity. The `stdf-gas-supply-decomposer` must also account for:

| End-Use | Global Share | Disruption Vector | Timeline |
|---------|-------------|-------------------|----------|
| Power generation | ~36% | SWB displacement (merit order) | 2025-2035 |
| Industrial heat | ~25% | Electrification (industrial HP, electric arc) | 2030-2040+ |
| Residential/commercial heating | ~24% | Heat pumps | 2025-2040 |
| Petrochemical feedstock | ~15% | Structural floor (not easily substituted) | Persistent |

The structural floor (~15% of demand as feedstock) means total gas demand does not go to zero globally. But **LNG's share of that remaining demand can go to zero** in import-dependent regions because domestic + pipeline sources are always cheaper.

---

## Data Sources

### In catalog (`data/natural_gas/`):
- NG Consumption: China, Europe, Global, USA (BCM, 1980-2024)
- NG Production: China, Europe, Global, USA (BCM, 1980-2024)
- NG Import/Export: China, Europe, Global, USA (BCM, 1980-2023)
- LNG Import: China, Europe, USA (BCM)
- LNG Export: Europe, USA (BCM)
- LNG Balance of Trade: China, Europe, USA (BCM)
- LNG Prices: USA export/import (USD/Mcf)
- NG Prices: China, Europe, USA (USD/MMBTU)

### Requires web research:
- China domestic gas production breakdown (conventional vs coal-to-gas)
- China pipeline import volumes by source (Central Asia, Russia)
- Europe pipeline import volumes (Norway, North Africa)
- Current LNG spot prices (JKM, TTF)
- LNG exporter project pipeline and FID status
