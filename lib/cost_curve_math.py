"""STDF v2 Cost Curve Mathematical Functions.

Pre-built computational module for the stdf-cost-curve agent. Provides
exponential fitting, learning-rate derivation, incumbent trend analysis,
threshold computation, and unit conversion functions so the agent does not
need to write inline python3 code from scratch on every run.

Dependencies: numpy, scipy (both expected in the environment).
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
from scipy import stats


# ---------------------------------------------------------------------------
# 1. Exponential fit  C(t) = C0 * exp(-r * (t - t_ref))
# ---------------------------------------------------------------------------

def exponential_fit(years: list, costs: list) -> dict:
    """Fit an exponential decay model to disruptor cost data.

    Uses OLS regression on ln(cost) vs. year to derive the decay rate.

    Parameters
    ----------
    years : list of int/float
        Calendar years for each data point.
    costs : list of float
        Cost values (must be positive) corresponding to each year.

    Returns
    -------
    dict with keys: C0, r, ref_year, r_squared, residuals, formula

    Raises
    ------
    ValueError
        If fewer than 3 data points or any cost is non-positive.
    """
    if len(years) < 3 or len(costs) < 3:
        raise ValueError(f"Need at least 3 data points; got {min(len(years), len(costs))}")
    if len(years) != len(costs):
        raise ValueError(f"years ({len(years)}) and costs ({len(costs)}) must have same length")

    y_arr = np.asarray(years, dtype=float)
    c_arr = np.asarray(costs, dtype=float)

    if np.any(c_arr <= 0):
        raise ValueError("All cost values must be positive for exponential fit")

    ref_year = int(y_arr[0])
    t = y_arr - ref_year
    ln_c = np.log(c_arr)

    slope, intercept, r_value, _p_value, _std_err = stats.linregress(t, ln_c)

    # slope = -r,  intercept = ln(C0)
    r = -slope
    C0 = math.exp(intercept)
    r_squared = r_value ** 2

    # Residuals in original cost space
    fitted = C0 * np.exp(-r * t)
    residuals = (c_arr - fitted).tolist()

    return {
        "C0": round(C0, 4),
        "r": round(r, 6),
        "ref_year": ref_year,
        "r_squared": round(r_squared, 4),
        "residuals": [round(v, 4) for v in residuals],
        "formula": f"C(t) = {C0:.2f} * exp(-{r:.4f} * (t - {ref_year}))",
    }


# ---------------------------------------------------------------------------
# 2. Learning rate from decay rate
# ---------------------------------------------------------------------------

def learning_rate_from_decay(r: float, basis: str = "per_year") -> float:
    """Convert exponential decay rate *r* to a learning-rate percentage.

    Parameters
    ----------
    r : float
        Decay rate from :func:`exponential_fit`.
    basis : str
        ``"per_year"`` — percentage cost reduction each year.
        ``"per_doubling"`` — approximate percentage cost reduction per
        doubling of time elapsed (uses doubling_time = ln(2)/r).

    Returns
    -------
    float  Learning rate as a percentage (e.g. 19.0 means 19%).
    """
    if basis == "per_year":
        return round((1 - math.exp(-r)) * 100, 2)
    elif basis == "per_doubling":
        if r <= 0:
            raise ValueError("Decay rate must be positive for per_doubling basis")
        doubling_time = math.log(2) / r
        return round((1 - math.exp(-r * doubling_time)) * 100, 2)
    else:
        raise ValueError(f"Unknown basis '{basis}'; use 'per_year' or 'per_doubling'")


# ---------------------------------------------------------------------------
# 3. Learning rate from deployment (experience curve)
# ---------------------------------------------------------------------------

def learning_rate_from_deployment(costs: list, cumulative_deployment: list) -> dict:
    """Derive learning rate from cost vs. cumulative deployment data.

    Fits log(cost) = a - b * log(cumulative_deployment) and computes the
    classic experience-curve learning rate = (1 - 2^{-b}) * 100.

    Parameters
    ----------
    costs : list of float
        Cost values (positive).
    cumulative_deployment : list of float
        Cumulative deployment/production values (positive, monotonically
        increasing expected but not enforced).

    Returns
    -------
    dict with keys: learning_rate_pct, b, r_squared, basis
    """
    if len(costs) < 3 or len(cumulative_deployment) < 3:
        raise ValueError(f"Need at least 3 data points; got {min(len(costs), len(cumulative_deployment))}")
    if len(costs) != len(cumulative_deployment):
        raise ValueError("costs and cumulative_deployment must have same length")

    c_arr = np.asarray(costs, dtype=float)
    d_arr = np.asarray(cumulative_deployment, dtype=float)

    if np.any(c_arr <= 0) or np.any(d_arr <= 0):
        raise ValueError("All cost and deployment values must be positive")

    log_c = np.log(c_arr)
    log_d = np.log(d_arr)

    slope, _intercept, r_value, _p_value, _std_err = stats.linregress(log_d, log_c)

    b = -slope  # slope is negative (cost falls as deployment rises)
    lr_pct = (1 - 2 ** (-b)) * 100
    r_squared = r_value ** 2

    return {
        "learning_rate_pct": round(lr_pct, 2),
        "b": round(b, 4),
        "r_squared": round(r_squared, 4),
        "basis": "per_doubling_deployment",
    }


# ---------------------------------------------------------------------------
# 4. Incumbent trend fit
# ---------------------------------------------------------------------------

def incumbent_trend_fit(years: list, costs: list) -> dict:
    """Fit a linear model to incumbent cost data and classify the trend.

    Classification:
    - ``"flat"`` if |slope| < 1% of mean cost per year
    - ``"linear_rising"`` if slope > 0 (beyond threshold)
    - ``"linear_declining"`` if slope < 0 (beyond threshold)

    Parameters
    ----------
    years : list of int/float
    costs : list of float

    Returns
    -------
    dict with keys: model, slope_per_year, intercept, r_squared, mean_cost
    """
    if len(years) < 2 or len(costs) < 2:
        raise ValueError(f"Need at least 2 data points; got {min(len(years), len(costs))}")
    if len(years) != len(costs):
        raise ValueError("years and costs must have same length")

    y_arr = np.asarray(years, dtype=float)
    c_arr = np.asarray(costs, dtype=float)

    slope, intercept, r_value, _p_value, _std_err = stats.linregress(y_arr, c_arr)
    r_squared = r_value ** 2
    mean_cost = float(np.mean(c_arr))

    threshold = 0.01 * mean_cost  # 1% of mean cost per year
    if abs(slope) < threshold:
        model = "flat"
    elif slope > 0:
        model = "linear_rising"
    else:
        model = "linear_declining"

    return {
        "model": model,
        "slope_per_year": round(slope, 4),
        "intercept": round(intercept, 4),
        "r_squared": round(r_squared, 4),
        "mean_cost": round(mean_cost, 4),
    }


# ---------------------------------------------------------------------------
# 5. Competitive threshold (cost parity crossover)
# ---------------------------------------------------------------------------

def competitive_threshold(
    C0: float, r: float, ref_year: int, incumbent_cost: float
) -> dict:
    """Solve for the year when disruptor cost equals incumbent cost.

    Assumes disruptor follows C(t) = C0 * exp(-r * (t - ref_year)) and
    incumbent cost is constant.

    Returns
    -------
    dict with keys: crossover_year, crossover_year_range, cost_at_parity
    """
    if C0 <= 0 or incumbent_cost <= 0:
        raise ValueError("C0 and incumbent_cost must be positive")
    if r <= 0:
        raise ValueError("Decay rate r must be positive")

    if C0 <= incumbent_cost:
        return {
            "crossover_year": float(ref_year),
            "crossover_year_range": (ref_year, ref_year),
            "cost_at_parity": round(C0, 2),
            "note": "Parity already reached at reference year",
        }

    t_cross = ref_year + (math.log(C0) - math.log(incumbent_cost)) / r
    cost_at_parity = round(incumbent_cost, 2)
    low_year = int(math.floor(t_cross))
    high_year = int(math.ceil(t_cross))

    return {
        "crossover_year": round(t_cross, 2),
        "crossover_year_range": (low_year, high_year),
        "cost_at_parity": cost_at_parity,
    }


# ---------------------------------------------------------------------------
# 6. Inflection threshold (50-70% of incumbent)
# ---------------------------------------------------------------------------

def inflection_threshold(
    C0: float,
    r: float,
    ref_year: int,
    incumbent_cost: float,
    low_pct: float = 0.5,
    high_pct: float = 0.7,
) -> dict:
    """Solve for when disruptor cost falls to low_pct-high_pct of incumbent.

    Parameters
    ----------
    low_pct : float
        Lower bound fraction (default 0.5 = 50%).
    high_pct : float
        Upper bound fraction (default 0.7 = 70%).

    Returns
    -------
    dict with keys: year_range, disruptor_cost_range, percent_of_incumbent_range
    """
    if C0 <= 0 or incumbent_cost <= 0:
        raise ValueError("C0 and incumbent_cost must be positive")
    if r <= 0:
        raise ValueError("Decay rate r must be positive")
    if not (0 < low_pct < high_pct <= 1.0):
        raise ValueError(f"Need 0 < low_pct < high_pct <= 1.0; got ({low_pct}, {high_pct})")

    target_high = high_pct * incumbent_cost  # reached first (less decline needed)
    target_low = low_pct * incumbent_cost    # reached second (more decline needed)

    def _solve_year(target: float) -> float:
        if C0 <= target:
            return float(ref_year)
        return ref_year + (math.log(C0) - math.log(target)) / r

    t_high = _solve_year(target_high)
    t_low = _solve_year(target_low)

    return {
        "year_range": (int(math.floor(t_high)), int(math.ceil(t_low))),
        "disruptor_cost_range": (round(target_low, 2), round(target_high, 2)),
        "percent_of_incumbent_range": (round(low_pct * 100, 1), round(high_pct * 100, 1)),
    }


# ---------------------------------------------------------------------------
# 7. Unit conversion functions
# ---------------------------------------------------------------------------

def convert_solar_wp_to_kwh(
    cost_per_wp: float,
    capacity_factor: float = 0.20,
    lifetime_years: int = 25,
    degradation_adj: float = 0.05,
) -> float:
    """Convert solar $/Wp to $/kWh delivered over system lifetime.

    Formula: $/kWh = ($/Wp * 1000) / (capacity_factor * 8760 * lifetime_years * (1 - degradation_adj))
    The factor of 1000 converts from Wp to kW (1 kW = 1000 Wp).
    """
    if cost_per_wp < 0:
        raise ValueError("cost_per_wp must be non-negative")
    if not (0 < capacity_factor < 1):
        raise ValueError("capacity_factor must be between 0 and 1")

    total_kwh = capacity_factor * 8760 * lifetime_years * (1 - degradation_adj)
    cost_per_kwh = (cost_per_wp * 1000) / total_kwh
    return round(cost_per_kwh, 6)


def convert_ev_vehicle_to_km(
    vehicle_cost: float,
    energy_cost: float,
    maintenance_cost: float,
    lifetime_km: float,
) -> float:
    """Convert EV total ownership costs to $/km.

    Formula: $/km = (vehicle_cost + energy_cost + maintenance_cost) / lifetime_km
    """
    if lifetime_km <= 0:
        raise ValueError("lifetime_km must be positive")
    total = vehicle_cost + energy_cost + maintenance_cost
    return round(total / lifetime_km, 6)


def convert_storage_cap_to_delivered(
    cost_per_kwh_cap: float,
    cycle_life: int,
    round_trip_efficiency: float = 0.90,
    depth_of_discharge: float = 0.90,
) -> float:
    """Convert $/kWh capacity to $/kWh delivered over lifetime.

    Formula: $/kWh_delivered = $/kWh_capacity / (cycle_life * RTE * DoD)
    """
    if cycle_life <= 0:
        raise ValueError("cycle_life must be positive")
    if not (0 < round_trip_efficiency <= 1):
        raise ValueError("round_trip_efficiency must be in (0, 1]")
    if not (0 < depth_of_discharge <= 1):
        raise ValueError("depth_of_discharge must be in (0, 1]")

    delivered = cost_per_kwh_cap / (cycle_life * round_trip_efficiency * depth_of_discharge)
    return round(delivered, 6)


# ---------------------------------------------------------------------------
# 8. Full cost analysis pipeline
# ---------------------------------------------------------------------------

def full_cost_analysis(
    disruptor_years: list,
    disruptor_costs: list,
    incumbent_years: list,
    incumbent_costs: list,
) -> dict[str, Any]:
    """Run the complete cost-curve analysis pipeline in one call.

    Steps:
    1. Exponential fit on disruptor data
    2. Learning rate derived from the fitted decay rate
    3. Linear trend fit on incumbent data
    4. Competitive threshold (cost parity year)
    5. Inflection threshold (50-70% of incumbent)

    Parameters
    ----------
    disruptor_years, disruptor_costs : lists
        Disruptor historical data (min 3 points).
    incumbent_years, incumbent_costs : lists
        Incumbent historical data (min 2 points).

    Returns
    -------
    dict with keys: exponential_fit, learning_rate_per_year,
    learning_rate_per_doubling, incumbent_trend, competitive_threshold,
    inflection_threshold
    """
    # Step 1: Exponential fit
    exp_fit = exponential_fit(disruptor_years, disruptor_costs)

    # Step 2: Learning rate (both bases)
    lr_year = learning_rate_from_decay(exp_fit["r"], basis="per_year")
    lr_doubling = learning_rate_from_decay(exp_fit["r"], basis="per_doubling")

    # Step 3: Incumbent trend
    inc_trend = incumbent_trend_fit(incumbent_years, incumbent_costs)

    # Use mean incumbent cost as the reference for threshold calculations
    inc_cost = inc_trend["mean_cost"]

    # Step 4: Competitive threshold
    comp_thresh = competitive_threshold(
        exp_fit["C0"], exp_fit["r"], exp_fit["ref_year"], inc_cost
    )

    # Step 5: Inflection threshold
    infl_thresh = inflection_threshold(
        exp_fit["C0"], exp_fit["r"], exp_fit["ref_year"], inc_cost
    )

    return {
        "exponential_fit": exp_fit,
        "learning_rate_per_year": lr_year,
        "learning_rate_per_doubling": lr_doubling,
        "incumbent_trend": inc_trend,
        "competitive_threshold": comp_thresh,
        "inflection_threshold": infl_thresh,
    }
