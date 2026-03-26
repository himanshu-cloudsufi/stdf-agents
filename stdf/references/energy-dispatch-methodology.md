# Energy Dispatch Methodology — 9-Step SWB Merit Order Pipeline

Reference specification for the `stdf-energy-dispatch` agent. This document defines the canonical computation pipeline for modeling SWB (Solar + Wind + Battery) displacement of fossil fuels in electricity generation.

## Pipeline Overview

```
Step 1: Total Demand → Step 2: SWB Generation → Step 3: Non-SWB Baseline
→ Step 4: Residual Demand → Step 5: Load Marginal Costs
→ Step 6: Merit Order Dispatch → Step 7: Displacement Schedule
→ Step 8: Reserve Floors → Step 9: Energy Balance Validation
```

---

## Step 1: Total Electricity Demand

```
Total_Demand (GWh) = Baseline_Demand + Incremental_EV + Incremental_DC + Incremental_HP
```

- **Baseline**: Historical electricity consumption extrapolated via blended CAGR
- **Incremental EV**: Fleet × kWh/vehicle/year — ONLY add growth above 2024 baseline
- **Incremental DC**: 415 TWh (2024) at 12% CAGR — ONLY add growth above 2024
- **Incremental HP**: COP-adjusted heat pump electricity — ONLY add growth above 2024

**Anti-double-count rule**: Each component adds ONLY incremental demand above the 2024 baseline. The baseline already includes 2024-level EV, DC, and HP consumption.

See `electricity-demand-decomposition.md` for detailed methodology per component.

## Step 2: SWB Generation

```
SWB_Gen (GWh) = Total_Demand × SWB_Share
```

Where `SWB_Share` comes from the `stdf-scurve-fitter` S-curve at year T.

Component breakdown (for reporting, not separate computation):
```
Solar_Gen = SWB_Gen × Solar_Fraction
Wind_Gen = SWB_Gen × Wind_Fraction
Battery_Dispatch = SWB_Gen × Battery_Fraction
```

Use `lib.energy_math.swb_generation()`.

## Step 3: Non-SWB Baseline (Hydro + Nuclear + Biomass)

```
Non_SWB = Total_Historical_Gen - SWB_Gen - Coal_Gen - Gas_Gen
Non_SWB = max(0, Non_SWB)
```

Non-SWB is derived from historical residuals, not forecasted independently. Extrapolate forward using blended CAGR with `lib.energy_math.blended_cagr()`.

**Germany exception**: Nuclear = 0 from April 2023 onwards (discrete closure, not gradual).

## Step 4: Residual Demand for Fossil Fuels

```
Residual (GWh) = Total_Demand - SWB_Gen - Non_SWB_Gen
Residual = max(0, Residual)
```

If residual is negative, SWB exceeds total demand — report this as "SWB exceeds demand" milestone.

## Step 5: Load Regional Marginal Costs

Read from `data/energy_sector/config/dispatch_parameters.json`:

| Region | Coal MC ($/MWh) | Gas MC ($/MWh) | Merit Priority |
|--------|----------------|----------------|----------------|
| China | 35 | 70 | Coal runs first (cheaper) |
| USA | 40 | 35 | Gas runs first (cheaper) |
| Europe | 50 | 60 | Coal runs first (cheaper) |
| RoW | 45 | 55 | Coal runs first (cheaper) |

**Use marginal cost, NOT LCOE.** LCOE includes sunk capital costs and understates the price at which incumbents actually dispatch. Marginal cost = fuel + variable O&M.

## Step 6: Merit Order Dispatch

The cheapest fuel fills residual demand first. The expensive fuel is displaced first as SWB grows.

```python
# Displacement-first logic (canonical):
if coal_mc <= gas_mc:  # Coal cheaper — coal runs, gas displaced first
    coal_gen = min(residual, historical_coal_gen)
    gas_gen = max(0, residual - coal_gen)
else:  # Gas cheaper — gas runs, coal displaced first
    gas_gen = min(residual, historical_gas_gen)
    coal_gen = max(0, residual - gas_gen)
```

**Growth scenario** (residual ≥ historical fossil total):
```python
growth_factor = residual / historical_total
coal_gen = historical_coal * growth_factor
gas_gen = historical_gas * growth_factor
```

Use `lib.energy_math.merit_order_dispatch()` or `displacement_schedule()`.

## Step 7: Displacement Schedule

Compute per-fuel displacement at +5, +10, +20 year horizons:

```
Displaced_GWh[fuel] = Historical_Gen[fuel] - Current_Gen[fuel]
```

Use `lib.energy_math.displacement_schedule()`.

## Step 8: Apply Reserve Floors

```
Coal minimum: 10% of peak historical capacity
Gas minimum: 15% of peak historical capacity
```

These floors prevent the model from showing instantaneous shutdown. Real-world grid stability requires backup capacity even when economically non-viable.

## Step 9: Energy Balance Validation

```
|SWB + Non_SWB + Coal + Gas - Total_Demand| / Total_Demand < 2%
```

Use `lib.energy_math.energy_balance_check()`. If balance fails, re-check demand inputs and generation computations before proceeding.

---

## Key Formulas Reference

| Formula | Expression | Unit |
|---------|-----------|------|
| Battery sizing | Solar_Capacity_GW × Duration_hours | GWh |
| SCOE | [Capex×1000] / [Cycles×Duration×RTE] + Fixed_OM | $/MWh |
| SWB stack cost | MAX(Solar_LCOE, Wind_LCOE) + SCOE | $/MWh |
| Blended CAGR | mean(CAGR_3yr, CAGR_5yr, CAGR_10yr) | fraction |
| GWh to BCM | Gas_Gen_GWh × 3.6 / (35.3 × 0.45) / 1000 | BCM |

## Critical Warnings

1. **China solar CF = 0.11** (not 0.17). Using 0.17 causes 55% generation overstatement.
2. **Never use LCOE** for incumbent dispatch comparison. Use marginal cost.
3. **Never present forecasts as historical data.** Label all projected values.
4. **If forecast peak < historical max**, investigate — do not silently accept.
