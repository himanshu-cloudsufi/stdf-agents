"""STDF v2 Energy Sector Mathematical Functions.

Pre-built computational module for energy-sector STDF agents. Provides
merit order dispatch, SWB generation modeling, displacement scheduling,
SCOE calculation, gas unit conversion, supply source decomposition,
energy balance validation, and electricity demand growth projections.

Dependencies: numpy (consistent with other lib modules).
"""

from __future__ import annotations

from typing import Any

import numpy as np


# ---------------------------------------------------------------------------
# 1. Merit order dispatch — cheapest-first residual allocation
# ---------------------------------------------------------------------------

def merit_order_dispatch(
    residual_demand_gwh: float,
    sources: list[dict],
    reserve_floors: dict[str, float] | None = None,
) -> dict:
    """Dispatch generation sources cheapest-first to fill residual demand.

    Parameters
    ----------
    residual_demand_gwh : float
        Residual demand (GWh) after SWB and non-SWB generation.
    sources : list of dict
        Each dict must have keys ``"name"`` (str), ``"marginal_cost"``
        (float, $/MWh), and ``"available_gwh"`` (float).
    reserve_floors : dict or None
        Optional minimum generation floors as fraction of available_gwh.
        E.g. ``{"coal": 0.10, "gas": 0.15}``.

    Returns
    -------
    dict with keys: dispatched (list of dicts with name, gwh, marginal_cost),
    total_dispatched_gwh, unmet_gwh.
    """
    if residual_demand_gwh < 0:
        residual_demand_gwh = 0.0

    # Sort sources by marginal cost ascending (cheapest first)
    sorted_sources = sorted(sources, key=lambda s: s["marginal_cost"])

    # Apply reserve floors — ensure minimum generation per source
    floors = {}
    if reserve_floors:
        for src in sorted_sources:
            name = src["name"]
            if name in reserve_floors:
                floors[name] = src["available_gwh"] * reserve_floors[name]

    dispatched = []
    remaining = residual_demand_gwh

    for src in sorted_sources:
        name = src["name"]
        available = src["available_gwh"]
        floor = floors.get(name, 0.0)

        allocated = min(remaining, available)
        # Ensure at least the floor is dispatched (if residual permits)
        allocated = max(allocated, min(floor, available))

        dispatched.append({
            "name": name,
            "gwh": round(allocated, 2),
            "marginal_cost": src["marginal_cost"],
        })
        remaining = max(0.0, remaining - allocated)

    total_dispatched = sum(d["gwh"] for d in dispatched)
    return {
        "dispatched": dispatched,
        "total_dispatched_gwh": round(total_dispatched, 2),
        "unmet_gwh": round(max(0.0, residual_demand_gwh - total_dispatched), 2),
    }


# ---------------------------------------------------------------------------
# 2. Displacement schedule — per-fuel displacement from SWB growth
# ---------------------------------------------------------------------------

def displacement_schedule(
    fossil_generation: dict[str, float],
    swb_increase_gwh: float,
    marginal_costs: dict[str, float],
    reserve_floors: dict[str, float] | None = None,
) -> dict:
    """Compute how much each fossil fuel is displaced by SWB growth.

    Expensive fuel is displaced first (displacement-first logic from the
    energy-sector skill).

    Parameters
    ----------
    fossil_generation : dict
        Current generation by fuel, e.g. ``{"coal": 5000, "gas": 3000}``.
    swb_increase_gwh : float
        Additional SWB generation displacing fossil fuels.
    marginal_costs : dict
        Marginal cost per fuel, e.g. ``{"coal": 35, "gas": 70}``.
    reserve_floors : dict or None
        Minimum fraction of historical generation to maintain per fuel.

    Returns
    -------
    dict with keys: displaced (dict per fuel), remaining (dict per fuel),
    total_displaced_gwh, shares (dict per fuel as fraction of original total).
    """
    if swb_increase_gwh <= 0:
        return {
            "displaced": {f: 0.0 for f in fossil_generation},
            "remaining": dict(fossil_generation),
            "total_displaced_gwh": 0.0,
            "shares": {f: 1.0 for f in fossil_generation},
        }

    # Sort fuels by marginal cost DESCENDING (most expensive displaced first)
    fuels_by_cost = sorted(
        fossil_generation.keys(),
        key=lambda f: marginal_costs.get(f, 0),
        reverse=True,
    )

    floors = {}
    if reserve_floors:
        for fuel in fuels_by_cost:
            if fuel in reserve_floors:
                floors[fuel] = fossil_generation[fuel] * reserve_floors[fuel]

    displaced = {}
    remaining_dict = {}
    to_displace = swb_increase_gwh

    for fuel in fuels_by_cost:
        gen = fossil_generation[fuel]
        floor = floors.get(fuel, 0.0)
        max_displaceable = max(0.0, gen - floor)

        fuel_displaced = min(to_displace, max_displaceable)
        displaced[fuel] = round(fuel_displaced, 2)
        remaining_dict[fuel] = round(gen - fuel_displaced, 2)
        to_displace = max(0.0, to_displace - fuel_displaced)

    original_total = sum(fossil_generation.values())
    shares = {}
    for fuel in fossil_generation:
        if original_total > 0:
            shares[fuel] = round(remaining_dict[fuel] / original_total, 4)
        else:
            shares[fuel] = 0.0

    return {
        "displaced": displaced,
        "remaining": remaining_dict,
        "total_displaced_gwh": round(sum(displaced.values()), 2),
        "shares": shares,
    }


# ---------------------------------------------------------------------------
# 3. SWB generation from S-curve share
# ---------------------------------------------------------------------------

def swb_generation(
    total_demand_gwh: float,
    swb_share: float,
    solar_fraction: float = 0.55,
    wind_fraction: float = 0.35,
    battery_fraction: float = 0.10,
) -> dict:
    """Compute SWB generation stack by component.

    Parameters
    ----------
    total_demand_gwh : float
        Total electricity demand (GWh).
    swb_share : float
        SWB market share from S-curve (0 to 1).
    solar_fraction, wind_fraction, battery_fraction : float
        Component fractions within SWB stack (must sum to ~1.0).

    Returns
    -------
    dict with keys: total_swb_gwh, solar_gwh, wind_gwh, battery_gwh.
    """
    swb_share = max(0.0, min(1.0, swb_share))
    total_swb = total_demand_gwh * swb_share

    return {
        "total_swb_gwh": round(total_swb, 2),
        "solar_gwh": round(total_swb * solar_fraction, 2),
        "wind_gwh": round(total_swb * wind_fraction, 2),
        "battery_gwh": round(total_swb * battery_fraction, 2),
    }


# ---------------------------------------------------------------------------
# 4. Energy balance validation
# ---------------------------------------------------------------------------

def energy_balance_check(
    total_demand_gwh: float,
    total_generation_gwh: float,
    tolerance_pct: float = 2.0,
) -> dict:
    """Validate generation equals demand within tolerance.

    Parameters
    ----------
    total_demand_gwh : float
        Total electricity demand (GWh).
    total_generation_gwh : float
        Total generation from all sources (GWh).
    tolerance_pct : float
        Acceptable percentage deviation (default 2%).

    Returns
    -------
    dict with keys: balanced (bool), gap_gwh, gap_pct.
    """
    if total_demand_gwh <= 0:
        return {"balanced": False, "gap_gwh": 0.0, "gap_pct": 0.0}

    gap = total_generation_gwh - total_demand_gwh
    gap_pct = abs(gap / total_demand_gwh) * 100

    return {
        "balanced": gap_pct <= tolerance_pct,
        "gap_gwh": round(gap, 2),
        "gap_pct": round(gap_pct, 4),
    }


# ---------------------------------------------------------------------------
# 5. SCOE — Storage Cost of Energy
# ---------------------------------------------------------------------------

def scoe(
    battery_capex_per_kwh: float,
    cycle_life: int,
    duration_hours: float,
    round_trip_efficiency: float,
    fixed_om_per_kwh_year: float = 0.0,
) -> float:
    """Compute Storage Cost of Energy (SCOE).

    Formula: SCOE = [Capex * 1000] / [Cycles * Duration * RTE] + Fixed_OM

    Parameters
    ----------
    battery_capex_per_kwh : float
        Battery capital cost ($/kWh capacity).
    cycle_life : int
        Total cycle life of the battery.
    duration_hours : float
        Discharge duration (hours).
    round_trip_efficiency : float
        Round-trip efficiency (0 to 1).
    fixed_om_per_kwh_year : float
        Annual fixed O&M cost ($/kWh-year). Default 0.

    Returns
    -------
    float : SCOE in $/MWh.
    """
    if cycle_life <= 0 or duration_hours <= 0 or round_trip_efficiency <= 0:
        raise ValueError("cycle_life, duration_hours, and RTE must be positive")

    scoe_val = (battery_capex_per_kwh * 1000) / (
        cycle_life * duration_hours * round_trip_efficiency
    ) + fixed_om_per_kwh_year

    return round(scoe_val, 2)


# ---------------------------------------------------------------------------
# 6. SWB stack cost
# ---------------------------------------------------------------------------

def swb_stack_cost(
    solar_lcoe: float,
    wind_lcoe: float,
    scoe_value: float,
) -> float:
    """Compute SWB stack cost (conservative method).

    Formula: SWB_stack = MAX(Solar_LCOE, Wind_LCOE) + SCOE

    Returns
    -------
    float : SWB stack cost in $/MWh.
    """
    return round(max(solar_lcoe, wind_lcoe) + scoe_value, 2)


# ---------------------------------------------------------------------------
# 7. Battery sizing from solar capacity
# ---------------------------------------------------------------------------

def battery_sizing(
    solar_capacity_gw: float,
    duration_hours: float = 4.0,
) -> float:
    """Compute battery energy capacity from solar capacity.

    Formula: Battery_Energy (GWh) = Solar_Capacity (GW) * Duration (hours)

    Returns
    -------
    float : Battery energy capacity in GWh.
    """
    return round(solar_capacity_gw * duration_hours, 2)


# ---------------------------------------------------------------------------
# 8. Blended CAGR (equal weight 3yr/5yr/10yr)
# ---------------------------------------------------------------------------

def blended_cagr(
    values: list[float],
    years: list[int],
) -> dict:
    """Compute blended CAGR as equal-weight average of 3yr, 5yr, 10yr CAGRs.

    Parameters
    ----------
    values : list of float
        Time series values (must be positive).
    years : list of int
        Corresponding years, same length as values.

    Returns
    -------
    dict with keys: cagr_3yr, cagr_5yr, cagr_10yr, blended.
    Returns None for any CAGR where insufficient data exists.
    """
    if len(values) != len(years) or len(values) < 2:
        raise ValueError("values and years must have same length >= 2")

    # Sort by year
    paired = sorted(zip(years, values))
    sorted_years, sorted_values = zip(*paired)

    last_year = sorted_years[-1]
    last_val = sorted_values[-1]

    def _cagr(lookback: int):
        target_year = last_year - lookback
        # Find closest year >= target_year
        for i, y in enumerate(sorted_years):
            if y >= target_year:
                base_val = sorted_values[i]
                actual_span = last_year - y
                if actual_span <= 0 or base_val <= 0:
                    return None
                return (last_val / base_val) ** (1.0 / actual_span) - 1.0
        return None

    cagr_3 = _cagr(3)
    cagr_5 = _cagr(5)
    cagr_10 = _cagr(10)

    available = [c for c in [cagr_3, cagr_5, cagr_10] if c is not None]
    blended = np.mean(available) if available else None

    return {
        "cagr_3yr": round(cagr_3, 6) if cagr_3 is not None else None,
        "cagr_5yr": round(cagr_5, 6) if cagr_5 is not None else None,
        "cagr_10yr": round(cagr_10, 6) if cagr_10 is not None else None,
        "blended": round(float(blended), 6) if blended is not None else None,
    }


# ---------------------------------------------------------------------------
# 9. GWh to BCM conversion (natural gas)
# ---------------------------------------------------------------------------

def gwh_to_bcm(
    gas_gen_gwh: float,
    heat_rate_mj_per_m3: float = 35.3,
    plant_efficiency: float = 0.45,
) -> float:
    """Convert gas-fired power generation to gas volume consumed.

    Formula: BCM = Gas_Gen_GWh * 3.6 / (heat_rate * efficiency)

    The 3.6 converts GWh to TJ (1 GWh = 3.6 TJ).
    heat_rate is MJ/m3 (lower heating value of natural gas ~35.3).
    efficiency is thermal efficiency of gas plant (~0.45 for CCGT).

    Parameters
    ----------
    gas_gen_gwh : float
        Gas-fired electricity generation in GWh.
    heat_rate_mj_per_m3 : float
        Heat content of natural gas (MJ/m3). Default 35.3.
    plant_efficiency : float
        Thermal efficiency of gas plant. Default 0.45 (CCGT).

    Returns
    -------
    float : Gas volume consumed in BCM (billion cubic metres).
    """
    if heat_rate_mj_per_m3 <= 0 or plant_efficiency <= 0:
        raise ValueError("heat_rate and efficiency must be positive")

    # GWh * 3.6 gives TJ; divide by (MJ/m3 * efficiency) gives m3
    # Then divide by 1e9 to get BCM
    bcm = (gas_gen_gwh * 3.6) / (heat_rate_mj_per_m3 * plant_efficiency) / 1e3

    return round(bcm, 4)


# ---------------------------------------------------------------------------
# 10. Supply source ordering (gas)
# ---------------------------------------------------------------------------

def supply_source_ordering(
    total_gas_bcm: float,
    sources: list[dict],
) -> list[dict]:
    """Order gas supply sources by displacement priority.

    Sources with higher priority numbers are displaced first (most expensive).
    Lower priority sources are served last (cheapest, most resilient).

    Parameters
    ----------
    total_gas_bcm : float
        Total gas demand to allocate across sources (BCM).
    sources : list of dict
        Each dict must have keys ``"name"`` (str), ``"bcm"`` (float,
        current supply volume), and ``"priority"`` (int, higher =
        displaced first).

    Returns
    -------
    list of dict, each with: name, current_bcm, displaced_bcm,
    remaining_bcm, displacement_order.
    """
    if total_gas_bcm < 0:
        total_gas_bcm = 0.0

    # Sort by priority descending (highest priority displaced first)
    sorted_sources = sorted(sources, key=lambda s: s["priority"], reverse=True)

    current_total = sum(s["bcm"] for s in sorted_sources)
    reduction = max(0.0, current_total - total_gas_bcm)

    result = []
    remaining_reduction = reduction

    for i, src in enumerate(sorted_sources):
        displaceable = src["bcm"]
        displaced = min(remaining_reduction, displaceable)
        remaining_reduction = max(0.0, remaining_reduction - displaced)

        result.append({
            "name": src["name"],
            "current_bcm": round(src["bcm"], 4),
            "displaced_bcm": round(displaced, 4),
            "remaining_bcm": round(src["bcm"] - displaced, 4),
            "displacement_order": i + 1,
        })

    return result


# ---------------------------------------------------------------------------
# 11. LNG displacement cascade
# ---------------------------------------------------------------------------

def lng_displacement_cascade(
    total_lng_reduction_bcm: float,
    lng_sources: list[dict],
) -> dict:
    """Model LNG import reduction by source origin.

    Higher-cost LNG sources are displaced first. Each source dict
    specifies current volume and priority (higher = displaced first).

    Parameters
    ----------
    total_lng_reduction_bcm : float
        Total LNG import reduction (BCM).
    lng_sources : list of dict
        Each dict: ``{"origin": str, "bcm": float, "priority": int}``.

    Returns
    -------
    dict with keys: displaced_by_source (list), total_displaced_bcm,
    total_remaining_bcm.
    """
    if total_lng_reduction_bcm <= 0:
        return {
            "displaced_by_source": [
                {"origin": s["origin"], "displaced_bcm": 0.0,
                 "remaining_bcm": s["bcm"]}
                for s in lng_sources
            ],
            "total_displaced_bcm": 0.0,
            "total_remaining_bcm": sum(s["bcm"] for s in lng_sources),
        }

    sorted_sources = sorted(lng_sources, key=lambda s: s["priority"], reverse=True)
    remaining_reduction = total_lng_reduction_bcm
    result = []

    for src in sorted_sources:
        displaced = min(remaining_reduction, src["bcm"])
        remaining_reduction = max(0.0, remaining_reduction - displaced)
        result.append({
            "origin": src["origin"],
            "displaced_bcm": round(displaced, 4),
            "remaining_bcm": round(src["bcm"] - displaced, 4),
        })

    return {
        "displaced_by_source": result,
        "total_displaced_bcm": round(
            sum(r["displaced_bcm"] for r in result), 4
        ),
        "total_remaining_bcm": round(
            sum(r["remaining_bcm"] for r in result), 4
        ),
    }


# ---------------------------------------------------------------------------
# 12. EV charging demand
# ---------------------------------------------------------------------------

def ev_charging_demand(
    fleet_by_type: dict[str, float],
    kwh_per_year_by_type: dict[str, float],
) -> dict:
    """Compute total EV electricity demand from fleet composition.

    Parameters
    ----------
    fleet_by_type : dict
        Vehicle count by type, e.g. ``{"BEV": 50e6, "PHEV": 10e6}``.
    kwh_per_year_by_type : dict
        Annual consumption per vehicle by type (kWh/vehicle/year).

    Returns
    -------
    dict with keys: demand_by_type (dict, TWh), total_twh.
    """
    demand_by_type = {}
    for vtype, count in fleet_by_type.items():
        kwh = kwh_per_year_by_type.get(vtype, 0)
        demand_by_type[vtype] = round(count * kwh / 1e9, 4)  # kWh → TWh

    return {
        "demand_by_type": demand_by_type,
        "total_twh": round(sum(demand_by_type.values()), 4),
    }


# ---------------------------------------------------------------------------
# 13. Datacenter demand projection
# ---------------------------------------------------------------------------

def datacenter_demand(
    base_twh: float = 415.0,
    base_year: int = 2024,
    cagr: float = 0.12,
    target_year: int = 2030,
) -> float:
    """Project datacenter electricity demand using CAGR.

    Parameters
    ----------
    base_twh : float
        Base year demand (TWh). Default 415 (IEA 2024).
    base_year : int
        Base year. Default 2024.
    cagr : float
        Compound annual growth rate. Default 0.12 (12%).
    target_year : int
        Year to project to.

    Returns
    -------
    float : Projected demand in TWh.
    """
    years_out = target_year - base_year
    if years_out < 0:
        raise ValueError("target_year must be >= base_year")

    return round(base_twh * (1 + cagr) ** years_out, 2)


# ---------------------------------------------------------------------------
# 14. Heat pump electricity demand
# ---------------------------------------------------------------------------

def heat_pump_demand(
    units: float,
    avg_consumption_kwh_per_unit: float,
    cop: float = 3.0,
) -> dict:
    """Compute electricity demand from heat pumps.

    Parameters
    ----------
    units : float
        Number of heat pump units installed.
    avg_consumption_kwh_per_unit : float
        Average annual thermal demand served per unit (kWh-thermal).
    cop : float
        Coefficient of Performance. Default 3.0.

    Returns
    -------
    dict with keys: electricity_twh (actual electricity consumed),
    thermal_twh (thermal energy delivered), cop.
    """
    thermal_twh = units * avg_consumption_kwh_per_unit / 1e9
    electricity_twh = thermal_twh / cop

    return {
        "electricity_twh": round(electricity_twh, 4),
        "thermal_twh": round(thermal_twh, 4),
        "cop": cop,
    }


# ---------------------------------------------------------------------------
# 15. Full energy dispatch pipeline (one-call convenience wrapper)
# ---------------------------------------------------------------------------

def full_energy_dispatch(
    total_demand_gwh: float,
    swb_share: float,
    non_swb_gwh: float,
    fossil_sources: list[dict],
    reserve_floors: dict[str, float] | None = None,
) -> dict:
    """Run the complete merit order dispatch pipeline in one call.

    Steps: SWB generation → residual → merit order dispatch → balance check.

    Parameters
    ----------
    total_demand_gwh : float
        Total electricity demand (GWh).
    swb_share : float
        SWB market share from S-curve (0 to 1).
    non_swb_gwh : float
        Non-SWB generation (hydro + nuclear, GWh).
    fossil_sources : list of dict
        Each: ``{"name": str, "marginal_cost": float, "available_gwh": float}``.
    reserve_floors : dict or None
        Minimum generation floors per fuel.

    Returns
    -------
    dict with keys: demand, swb, non_swb, residual, dispatch,
    displacement, shares, balance.
    """
    # Step 1: SWB generation
    swb = swb_generation(total_demand_gwh, swb_share)

    # Step 2: Residual
    residual = max(0.0, total_demand_gwh - swb["total_swb_gwh"] - non_swb_gwh)

    # Step 3: Merit order dispatch
    dispatch = merit_order_dispatch(residual, fossil_sources, reserve_floors)

    # Step 4: Compute displacement vs historical
    fossil_gen = {s["name"]: s["available_gwh"] for s in fossil_sources}
    marginal_costs = {s["name"]: s["marginal_cost"] for s in fossil_sources}
    swb_increase = swb["total_swb_gwh"]  # Simplified: treat all SWB as displacement
    disp = displacement_schedule(fossil_gen, swb_increase, marginal_costs, reserve_floors)

    # Step 5: Energy balance
    total_gen = swb["total_swb_gwh"] + non_swb_gwh + dispatch["total_dispatched_gwh"]
    balance = energy_balance_check(total_demand_gwh, total_gen)

    return {
        "demand_gwh": round(total_demand_gwh, 2),
        "swb": swb,
        "non_swb_gwh": round(non_swb_gwh, 2),
        "residual_gwh": round(residual, 2),
        "dispatch": dispatch,
        "displacement": disp,
        "balance": balance,
    }
