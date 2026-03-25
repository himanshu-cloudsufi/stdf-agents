"""Trajectory fitting and threshold checking for the STDF capability agent.

Used by stdf-capability (Cat 3) to fit performance trajectories, check whether
capability dimensions have reached competitive parity, and estimate parity years.

Dependencies: numpy, scipy
"""

import numpy as np
from scipy.optimize import curve_fit


def fit_trajectory(years, values):
    """Fit trajectory data to identify the best curve shape.

    Tries exponential and linear fits, selects by R-squared.
    A decelerating trajectory is an exponential fit whose growth rate (b) is
    positive but the second derivative of improvement is decreasing — detected
    when exponential R-squared > linear R-squared but b is very small.

    Args:
        years: List of years.
        values: Corresponding metric values.

    Returns:
        dict with: curve_type, params, r_squared, projected_values (empty list).

    Raises:
        ValueError: If fewer than 2 data points are supplied.
    """
    years = np.asarray(years, dtype=float)
    values = np.asarray(values, dtype=float)

    if len(years) < 2:
        raise ValueError(
            f"Insufficient data: {len(years)} points provided, minimum 2 required."
        )

    ss_tot = np.sum((values - np.mean(values)) ** 2)
    if ss_tot == 0:
        # Constant data — return linear with zero slope.
        return {
            "curve_type": "linear",
            "params": {"a": float(values[0]), "b": 0.0},
            "r_squared": 1.0,
            "projected_values": [],
        }

    # --- Linear fit: v(t) = a + b * t ---
    lin_coeffs = np.polyfit(years, values, 1)
    lin_pred = np.polyval(lin_coeffs, years)
    lin_ss_res = np.sum((values - lin_pred) ** 2)
    lin_r2 = 1.0 - (lin_ss_res / ss_tot)
    lin_params = {"a": float(lin_coeffs[1]), "b": float(lin_coeffs[0])}

    # --- Exponential fit: v(t) = a * exp(b * (t - t0)) ---
    # Normalize time to avoid overflow: use first year as reference.
    t0 = years[0]
    t_norm = years - t0

    exp_r2 = -np.inf
    exp_params = {}
    try:
        def _exp_func(t, a, b):
            return a * np.exp(b * t)

        # Initial guess from log-linear regression where possible.
        if np.all(values > 0):
            log_coeffs = np.polyfit(t_norm, np.log(values), 1)
            a0 = np.exp(log_coeffs[1])
            b0 = log_coeffs[0]
        else:
            a0 = float(values[0]) if values[0] != 0 else 1.0
            b0 = 0.05

        popt, _ = curve_fit(
            _exp_func, t_norm, values, p0=[a0, b0], maxfev=10000
        )
        exp_pred = _exp_func(t_norm, *popt)
        exp_ss_res = np.sum((values - exp_pred) ** 2)
        exp_r2 = 1.0 - (exp_ss_res / ss_tot)
        # Store params in absolute terms: v(t) = a * exp(b * (t - t0))
        exp_params = {"a": float(popt[0]), "b": float(popt[1]), "t0": float(t0)}
    except (RuntimeError, OverflowError, ValueError):
        # Exponential fit failed — fall back to linear.
        pass

    # --- Select best fit ---
    if exp_r2 > lin_r2 and exp_params:
        b_val = exp_params["b"]
        # Classify decelerating: positive growth but very slow (< 0.01/yr)
        # or negative growth rate.
        if b_val < 0:
            curve_type = "decelerating"
        elif b_val < 0.01:
            curve_type = "decelerating"
        else:
            curve_type = "exponential"
        return {
            "curve_type": curve_type,
            "params": exp_params,
            "r_squared": float(exp_r2),
            "projected_values": [],
        }
    else:
        curve_type = "linear"
        if lin_params["b"] < 0:
            curve_type = "decelerating"
        return {
            "curve_type": curve_type,
            "params": lin_params,
            "r_squared": float(lin_r2),
            "projected_values": [],
        }


def threshold_check(current_value, threshold, higher_is_better=True):
    """Check if a capability dimension meets its competitive threshold.

    Args:
        current_value: Current measured value.
        threshold: Competitive parity threshold.
        higher_is_better: True if exceeding threshold = MET (e.g., energy density).
                          False if falling below threshold = MET (e.g., charge time).

    Returns:
        dict with: status, gap_pct, current, threshold.
    """
    if threshold == 0:
        # Avoid division by zero; if threshold is 0 and higher_is_better,
        # any positive value meets it.
        if higher_is_better:
            status = "MET" if current_value >= 0 else "NOT_MET"
        else:
            status = "MET" if current_value <= 0 else "NOT_MET"
        return {
            "status": status,
            "gap_pct": 0.0,
            "current": float(current_value),
            "threshold": float(threshold),
        }

    if higher_is_better:
        if current_value >= threshold:
            status = "MET"
        elif current_value >= threshold * 0.85:
            status = "APPROACHING"
        else:
            status = "NOT_MET"
        gap_pct = ((threshold - current_value) / abs(threshold)) * 100.0
    else:
        # Lower is better (e.g., charge time, cost per unit).
        if current_value <= threshold:
            status = "MET"
        elif current_value <= threshold * 1.15:
            status = "APPROACHING"
        else:
            status = "NOT_MET"
        gap_pct = ((current_value - threshold) / abs(threshold)) * 100.0

    return {
        "status": status,
        "gap_pct": round(float(gap_pct), 2),
        "current": float(current_value),
        "threshold": float(threshold),
    }


def convergence_pattern(dimensions):
    """Determine convergence pattern across multiple capability dimensions.

    Args:
        dimensions: List of dicts, each with keys:
            dimension (str), met_year (int or None), status (str).

    Returns:
        One of: "simultaneous", "sequential", "divergent".
    """
    met_years = [d["met_year"] for d in dimensions if d.get("met_year") is not None]
    not_met = [d for d in dimensions if d.get("status") == "NOT_MET"]

    if not met_years:
        # Nothing has been met.
        return "divergent"

    # If any dimension is NOT_MET with no met_year projection, divergent.
    if not_met and len(met_years) < len(dimensions):
        return "divergent"

    year_span = max(met_years) - min(met_years)
    if year_span <= 3:
        return "simultaneous"
    else:
        return "sequential"


def parity_year_estimate(years, values, threshold, higher_is_better=True):
    """Estimate when a capability dimension crosses its competitive threshold.

    Extrapolates the fitted trajectory to find the crossing year.

    Args:
        years: Historical years.
        values: Historical values.
        threshold: The parity threshold to cross.
        higher_is_better: Direction of improvement.

    Returns:
        Year as float, or None if trajectory does not converge toward threshold.
    """
    # Sort by year to ensure correct ordering
    paired = sorted(zip(years, values), key=lambda x: x[0])
    years_sorted = [p[0] for p in paired]
    values_sorted = [p[1] for p in paired]

    traj = fit_trajectory(years_sorted, values_sorted)
    params = traj["params"]
    curve_type = traj["curve_type"]

    # Check if already met (use last = most recent after sorting).
    current = float(values_sorted[-1])
    check = threshold_check(current, threshold, higher_is_better)
    if check["status"] == "MET":
        return float(years_sorted[-1])

    # Extrapolate year-by-year up to 50 years out.
    last_year = int(max(years_sorted))
    for future_year in range(last_year + 1, last_year + 51):
        if curve_type in ("exponential", "decelerating") and "t0" in params:
            t_norm = future_year - params["t0"]
            projected = params["a"] * np.exp(params["b"] * t_norm)
        else:
            # Linear: v = a + b * t
            projected = params["a"] + params["b"] * future_year

        if higher_is_better and projected >= threshold:
            return float(future_year)
        elif not higher_is_better and projected <= threshold:
            return float(future_year)

    # Trajectory does not converge within 50 years.
    return None


def multi_dimensional_summary(dimensions):
    """Summarize capability assessment across all dimensions.

    Args:
        dimensions: List of dicts with keys: dimension, status, met_year.

    Returns:
        dict with: total, met_count, approaching_count, not_met_count,
                    all_met, convergence_pattern, blocking_dimensions.
    """
    total = len(dimensions)
    met = [d for d in dimensions if d.get("status") == "MET"]
    approaching = [d for d in dimensions if d.get("status") == "APPROACHING"]
    not_met = [d for d in dimensions if d.get("status") == "NOT_MET"]

    pattern = convergence_pattern(dimensions)
    blocking = [d["dimension"] for d in not_met]

    return {
        "total": total,
        "met_count": len(met),
        "approaching_count": len(approaching),
        "not_met_count": len(not_met),
        "all_met": len(met) == total,
        "convergence_pattern": pattern,
        "blocking_dimensions": blocking,
    }
