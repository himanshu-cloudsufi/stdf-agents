# Electricity Demand Decomposition Methodology

Reference specification for the `stdf-energy-dispatch` agent. Defines how to decompose total electricity demand into baseline + growth vectors, with anti-double-counting safeguards.

## Total Demand Formula

```
Total_Electricity_Demand =
    Baseline_Electricity_Demand (projected)
  + Incremental_EV_Demand (above 2024 baseline)
  + Incremental_Datacenter_Demand (above 2024 baseline)
  + Incremental_Heat_Pump_Demand (above 2024 baseline)
```

**Anti-double-count rule**: Only add incremental growth beyond 2024 for each component. The 2024 baseline already includes existing EV, DC, and HP consumption.

---

## Component 1: Baseline Electricity Demand

**Source**: `data/electricity/adoption/Electricity_Annual_Domestic_Consumption_*.json`

**Method**: Project using `lib.energy_math.blended_cagr()` (equal-weight 3yr/5yr/10yr CAGR).

**2024 Anchors (TWh)**: China ~9,400 | USA ~4,200 | Europe ~3,300 | Global ~27,200

---

## Component 2: EV Electricity Demand

**Formula**:
```
EV_Demand (TWh) = Σ [Fleet_by_type × kWh_per_vehicle_per_year] / 1e9
Incremental = EV_Demand[year] - EV_Demand[2024]
```

**Fleet data**: From STDF pipeline vehicle adoption curves or `data/passenger_cars/`, `data/commercial_vehicle/`

**Consumption by type and region** (kWh/vehicle/year):

| Type | China | USA | Europe | RoW |
|------|-------|-----|--------|-----|
| BEV passenger | 3,300 | 4,500 | 3,000 | 2,500 |
| PHEV | 1,500 | 2,000 | 1,400 | 1,200 |
| E2W (China dominant) | 400 | 500 | 450 | 350 |
| Commercial EV | 10,000 | 12,000 | 9,000 | 8,000 |

Includes 10-15% charging losses. Use `lib.energy_math.ev_charging_demand()`.

**2024 Global EV demand**: ~321 TWh (China ~241 TWh dominates due to 350M e-two-wheelers)

---

## Component 3: Datacenter Electricity Demand

**Formula**:
```
DC_Demand[year] = 415 × (1.12)^(year - 2024)
Incremental = DC_Demand[year] - 415
```

**Parameters**:
- Base: 415 TWh (2024, IEA)
- CAGR: 12% (IEA historical 2019-2024)
- No artificial ceiling — AI compute demand has no obvious upper bound

**Regional shares** (constant): USA 44% | China 25% | Europe 10% | RoW 21%

Use `lib.energy_math.datacenter_demand()`.

**Projections**: 2030: 819 TWh | 2035: 1,443 TWh | 2040: 2,543 TWh

---

## Component 4: Heat Pump Electricity Demand

**Formula**:
```
HP_Electricity (TWh) = (Total_Heating_Demand × HP_Share) / COP
Incremental = HP_Electricity[year] - HP_Electricity[2024]
```

**Addressable market**: ~26,700 TWh-thermal globally

**Regional heat demand** (TWh-th): China 6,900 | Europe 3,300 | USA 2,800 | RoW 13,700

**Regional COP**: China 3.5 | Europe 3.5 | USA 3.2 | RoW 3.0

**Efficiency gain**: Heat pump at COP 3.5 uses 3.5x less energy than gas boiler at 90% efficiency. This means electrification of heating REDUCES total energy consumed while shifting the form from gas to electricity.

**Break-even condition**:
```
HP wins on operating cost when: Elec/Gas price ratio < COP / Boiler_Eff
At COP 3.5: break-even ratio = 3.5 / 0.90 = 3.9
```

**Regional tipping points**: China 2024 | Europe 2023 | USA 2025 | RoW 2027

**Adoption heuristic** (Seba: 10% to 80% in 10 years post-tipping):
```python
if year <= tipping: share = 0.05 + 0.01 * (year - 2020)
elif year <= tipping + 2: share = 0.05 + (year - tp) / 2 * 0.05  # → 10%
elif year <= tipping + 12: share = 0.10 + (year - tp - 2) / 10 * 0.70  # → 80%
elif year <= tipping + 20: share = 0.80 + (year - tp - 12) / 8 * 0.15  # → 95%
```

Use `lib.energy_math.heat_pump_demand()`.

**Key finding**: Heat pumps are the #1 demand growth driver globally (~6,800 TWh incremental by 2040) — larger than EVs + datacenters combined.

---

## 2040 Global Demand Projection

| Component | 2024 (TWh) | 2040 (TWh) | Incremental | Share of Growth |
|-----------|------------|------------|-------------|-----------------|
| Baseline | 27,200 | ~43,000 | +15,800 | 59% |
| EV | 321 | 3,516 | +3,195 | 12% |
| Datacenter | 415 | 2,543 | +2,128 | 8% |
| Heat Pump | 558 | 7,026 | +6,468 | 24% |
| **Total** | **~28,000** | **~54,800** | **+26,800** | **100%** |

---

## Unit Conversions

```
1 Million bbl/day (oil) → TWh/year: × 2.117
1 BCM (natural gas) → TWh: × 10.28
```
