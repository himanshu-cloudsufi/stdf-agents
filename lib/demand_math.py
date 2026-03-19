"""STDF v2 Commodity Demand Decomposition Mathematical Functions.

Pre-built computational module for the stdf-commodity-demand agent. Provides
demand decomposition, material intensity calculation, stock-flow fleet modeling,
OEM/replacement splitting, technology stream aggregation, regional disaggregation,
and S-curve-based demand projection.

Dependencies: numpy (consistent with other lib modules).
"""

from __future__ import annotations

from typing import Any

import numpy as np


# ---------------------------------------------------------------------------
# 1. Demand decomposition — validate >=80% coverage (7.1)
# ---------------------------------------------------------------------------

def decompose_demand(drivers: list[dict], total_demand: float) -> dict:
    """Validate that identified demand drivers cover >=80% of total demand.

    Parameters
    ----------
    drivers : list of dict
        Each dict must have keys ``"name"`` (str) and ``"demand"`` (float).
    total_demand : float
        Total commodity demand to decompose.

    Returns
    -------
    dict with keys: drivers, total_demand, covered_demand, coverage_pct,
    compliant (bool — True if coverage >= 80%).

    Raises
    ------
    ValueError
        If total_demand <= 0 or drivers is empty.
    """
    if total_demand <= 0:
        raise ValueError(f"total_demand must be positive; got {total_demand}")
    if not drivers:
        raise ValueError("drivers list must not be empty")

    covered = sum(d["demand"] for d in drivers)
    coverage_pct = round((covered / total_demand) * 100, 2)

    return {
        "drivers": drivers,
        "total_demand": total_demand,
        "covered_demand": round(covered, 4),
        "coverage_pct": coverage_pct,
        "compliant": coverage_pct >= 80.0,
    }


# ---------------------------------------------------------------------------
# 2. Material intensity demand — units * intensity (7.5)
# ---------------------------------------------------------------------------

def material_intensity_demand(units_sold: float, intensity_per_unit: float) -> float:
    """Compute commodity demand from unit sales and material intensity.

    Parameters
    ----------
    units_sold : float
        Number of units sold (e.g., vehicles, appliances).
    intensity_per_unit : float
        Commodity content per unit (e.g., kg copper per vehicle).

    Returns
    -------
    float  Total commodity demand (units_sold * intensity_per_unit).
    """
    return round(units_sold * intensity_per_unit, 4)


# ---------------------------------------------------------------------------
# 3. Stock-flow fleet model (7.8)
# ---------------------------------------------------------------------------

def stock_flow_fleet(
    fleet_current: float,
    sales: list[float],
    scrappage_rate: float,
    years: int,
    lifetime: float | None = None,
) -> list[dict]:
    """Model fleet evolution using stock-flow accounting.

    Fleet(t+1) = Fleet(t) + Sales(t) - Scrappage(t)

    Scrappage is computed as: fleet * scrappage_rate (rate-based).
    If ``lifetime`` is provided, scrappage_rate is overridden with 1/lifetime.

    Parameters
    ----------
    fleet_current : float
        Current fleet size.
    sales : list of float
        Annual sales for each year. Length must equal *years*.
    scrappage_rate : float
        Annual scrappage rate (fraction, 0 < rate < 1).
    years : int
        Number of years to project.
    lifetime : float, optional
        Average vehicle/unit lifetime in years. If given, overrides
        scrappage_rate with 1/lifetime.

    Returns
    -------
    list of dict with keys: year (0-indexed), fleet, sales, scrappage, net_change.

    Raises
    ------
    ValueError
        If scrappage_rate not in (0, 1), years != len(sales), or fleet < 0.
    """
    if lifetime is not None:
        if lifetime <= 0:
            raise ValueError(f"lifetime must be positive; got {lifetime}")
        scrappage_rate = 1.0 / lifetime

    if not (0 < scrappage_rate < 1):
        raise ValueError(f"scrappage_rate must be in (0, 1); got {scrappage_rate}")
    if fleet_current < 0:
        raise ValueError(f"fleet_current must be non-negative; got {fleet_current}")
    if len(sales) != years:
        raise ValueError(f"sales length ({len(sales)}) must equal years ({years})")

    results = []
    fleet = fleet_current

    for t in range(years):
        scrappage = fleet * scrappage_rate
        net_change = sales[t] - scrappage
        fleet_next = max(fleet + net_change, 0)  # fleet never negative
        results.append({
            "year": t,
            "fleet": round(fleet, 2),
            "sales": round(sales[t], 2),
            "scrappage": round(scrappage, 2),
            "net_change": round(net_change, 2),
        })
        fleet = fleet_next

    return results


# ---------------------------------------------------------------------------
# 4. OEM + replacement demand split (7.7)
# ---------------------------------------------------------------------------

def oem_replacement_split(
    fleet_growth_units: float,
    replacement_units: float,
    intensity_oem: float,
    intensity_replacement: float | None = None,
) -> dict:
    """Split commodity demand into OEM (new fleet growth) and replacement.

    Parameters
    ----------
    fleet_growth_units : float
        Net new units added to fleet (OEM demand driver).
    replacement_units : float
        Units replacing scrapped fleet (replacement demand driver).
    intensity_oem : float
        Commodity intensity per new unit (kg/unit).
    intensity_replacement : float, optional
        Commodity intensity per replacement unit. Defaults to intensity_oem.

    Returns
    -------
    dict with keys: oem_demand, replacement_demand, total_demand,
    oem_share_pct, replacement_share_pct.
    """
    if intensity_replacement is None:
        intensity_replacement = intensity_oem

    oem = fleet_growth_units * intensity_oem
    replacement = replacement_units * intensity_replacement
    total = oem + replacement
    oem_pct = round((oem / total) * 100, 2) if total > 0 else 0.0
    repl_pct = round((replacement / total) * 100, 2) if total > 0 else 0.0

    return {
        "oem_demand": round(oem, 4),
        "replacement_demand": round(replacement, 4),
        "total_demand": round(total, 4),
        "oem_share_pct": oem_pct,
        "replacement_share_pct": repl_pct,
    }


# ---------------------------------------------------------------------------
# 5. Aggregate demand by technology stream (7.6)
# ---------------------------------------------------------------------------

def aggregate_demand_by_technology(tech_demands: dict[str, float]) -> dict:
    """Sum demand across incumbent/disruptor/chimera technology streams.

    Parameters
    ----------
    tech_demands : dict
        Keys are technology stream names (e.g., ``"incumbent"``,
        ``"disruptor"``, ``"chimera"``), values are demand amounts.

    Returns
    -------
    dict with keys: streams (copy of input), total_demand, stream_shares.
    """
    if not tech_demands:
        return {"streams": {}, "total_demand": 0.0, "stream_shares": {}}

    total = sum(tech_demands.values())
    shares = {}
    for name, demand in tech_demands.items():
        shares[name] = round((demand / total) * 100, 2) if total > 0 else 0.0

    return {
        "streams": dict(tech_demands),
        "total_demand": round(total, 4),
        "stream_shares": shares,
    }


# ---------------------------------------------------------------------------
# 6. Regional demand split (7.9)
# ---------------------------------------------------------------------------

def regional_demand_split(
    global_demand: float,
    regional_shares: dict[str, float],
) -> dict:
    """Split global demand into regional buckets.

    Parameters
    ----------
    global_demand : float
        Total global demand.
    regional_shares : dict
        Region name -> share (fraction, 0-1). Sum should be ~1.0.

    Returns
    -------
    dict with keys: global_demand, regions (dict of name -> demand).

    Raises
    ------
    ValueError
        If any share is negative or sum exceeds 1.1.
    """
    for region, share in regional_shares.items():
        if share < 0:
            raise ValueError(f"Negative share for region '{region}': {share}")

    total_share = sum(regional_shares.values())
    if total_share > 1.1:
        raise ValueError(
            f"Regional shares sum to {total_share:.2f}, exceeding 1.1 tolerance"
        )

    regions = {}
    for region, share in regional_shares.items():
        regions[region] = round(global_demand * share, 4)

    return {
        "global_demand": global_demand,
        "regions": regions,
    }


# ---------------------------------------------------------------------------
# 7. Project demand from S-curve (7.4)
# ---------------------------------------------------------------------------

def project_demand_from_scurve(
    L: float,
    k: float,
    x0: float,
    total_market_units: float,
    intensity_disruptor: float,
    intensity_incumbent: float,
    base_year: int = 2026,
    horizons: list[int] | None = None,
) -> list[dict]:
    """Project commodity demand using S-curve adoption + material intensities.

    The disruptor's market share follows: share(t) = L / (1 + exp(-k*(t - x0)))
    Incumbent share = 1 - disruptor share.

    Demand at each horizon:
        disruptor_demand = total_market_units * share * intensity_disruptor
        incumbent_demand = total_market_units * (1 - share) * intensity_incumbent

    Parameters
    ----------
    L : float
        S-curve saturation level (fraction, 0-1).
    k : float
        S-curve growth rate.
    x0 : float
        S-curve inflection year.
    total_market_units : float
        Total market size in units per year.
    intensity_disruptor : float
        Commodity intensity per disruptor unit (kg/unit).
    intensity_incumbent : float
        Commodity intensity per incumbent unit (kg/unit).
    base_year : int
        Year to project from (default 2026).
    horizons : list of int, optional
        Year offsets from base_year (default [5, 10, 20]).

    Returns
    -------
    list of dict with keys: horizon, year, disruptor_share, incumbent_share,
    disruptor_demand, incumbent_demand, total_demand, net_change_pct.
    """
    if horizons is None:
        horizons = [5, 10, 20]

    base_share = L / (1.0 + np.exp(-k * (base_year - x0)))
    base_demand = (
        total_market_units * base_share * intensity_disruptor
        + total_market_units * (1.0 - base_share) * intensity_incumbent
    )

    results = []
    for h in horizons:
        year = base_year + h
        share = float(L / (1.0 + np.exp(-k * (year - x0))))
        inc_share = 1.0 - share

        d_demand = total_market_units * share * intensity_disruptor
        i_demand = total_market_units * inc_share * intensity_incumbent
        total = d_demand + i_demand

        net_change = ((total - base_demand) / base_demand * 100) if base_demand > 0 else 0.0

        results.append({
            "horizon": h,
            "year": year,
            "disruptor_share": round(share, 4),
            "incumbent_share": round(inc_share, 4),
            "disruptor_demand": round(d_demand, 2),
            "incumbent_demand": round(i_demand, 2),
            "total_demand": round(total, 2),
            "net_change_pct": round(net_change, 2),
        })

    return results


# ---------------------------------------------------------------------------
# 8. Validate stock-flow consistency (7.8)
# ---------------------------------------------------------------------------

def validate_stock_flow_consistency(fleet_series: list[dict]) -> dict:
    """Check that Fleet(t+1) == Fleet(t) + Sales(t) - Scrappage(t).

    Parameters
    ----------
    fleet_series : list of dict
        Each dict must have keys: fleet, sales, scrappage.

    Returns
    -------
    dict with keys: consistent (bool), violations (list of year indices),
    max_deviation.
    """
    violations = []
    max_dev = 0.0

    for i in range(len(fleet_series) - 1):
        current = fleet_series[i]
        next_row = fleet_series[i + 1]
        expected = current["fleet"] + current["sales"] - current["scrappage"]
        expected = max(expected, 0)  # floor at zero
        actual = next_row["fleet"]
        deviation = abs(actual - expected)
        if deviation > 0.01:  # tolerance for rounding
            violations.append(i)
            max_dev = max(max_dev, deviation)

    return {
        "consistent": len(violations) == 0,
        "violations": violations,
        "max_deviation": round(max_dev, 4),
    }


# ---------------------------------------------------------------------------
# 9. Full demand analysis pipeline
# ---------------------------------------------------------------------------

def full_demand_analysis(
    demand_drivers: list[dict],
    total_commodity_demand: float,
    scurve_params: dict,
    material_intensities: dict,
    market_size: float,
    regions: dict[str, float],
) -> dict[str, Any]:
    """Run the complete demand decomposition pipeline in one call.

    Steps:
    1. Decompose demand into drivers (validate 80% coverage)
    2. Project demand using S-curve + material intensities
    3. Aggregate by technology stream
    4. Regionalize demand

    Parameters
    ----------
    demand_drivers : list of dict
        Each with "name" and "demand" keys.
    total_commodity_demand : float
        Total commodity demand to decompose.
    scurve_params : dict
        Keys: L, k, x0 (S-curve parameters).
    material_intensities : dict
        Keys: disruptor, incumbent (kg/unit each).
    market_size : float
        Total market units per year.
    regions : dict
        Region name -> share (fraction).

    Returns
    -------
    dict with keys: decomposition, projections, technology_streams,
    regional_split, validation.
    """
    # Step 1: Decompose
    decomposition = decompose_demand(demand_drivers, total_commodity_demand)

    # Step 2: Project using S-curve
    projections = project_demand_from_scurve(
        L=scurve_params["L"],
        k=scurve_params["k"],
        x0=scurve_params["x0"],
        total_market_units=market_size,
        intensity_disruptor=material_intensities["disruptor"],
        intensity_incumbent=material_intensities["incumbent"],
    )

    # Step 3: Aggregate by technology (use latest projection for current split)
    if projections:
        latest = projections[-1]
        tech_demands = {
            "disruptor": latest["disruptor_demand"],
            "incumbent": latest["incumbent_demand"],
        }
    else:
        tech_demands = {}
    technology_streams = aggregate_demand_by_technology(tech_demands)

    # Step 4: Regionalize (use current total)
    current_total = projections[0]["total_demand"] if projections else total_commodity_demand
    regional_split = regional_demand_split(current_total, regions)

    return {
        "decomposition": decomposition,
        "projections": projections,
        "technology_streams": technology_streams,
        "regional_split": regional_split,
    }
