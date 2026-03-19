"""S-curve fitting and projection for STDF adoption and tipping-point agents.

Used by stdf-adoption-scurve (Cat 4) and stdf-tipping-point (Cat 5) agents
to fit logistic S-curves to historical market-share data and project forward.

Dependencies: numpy, scipy
"""

import numpy as np
from scipy.optimize import curve_fit


def logistic(t, L, k, x0):
    """Standard logistic S-curve.

    f(t) = L / (1 + exp(-k * (t - x0)))

    Args:
        t: Time value(s) — scalar or array-like.
        L: Saturation level (asymptotic maximum, typically 0-100 for %).
        k: Growth rate (steepness of the curve).
        x0: Inflection point (year of fastest growth).

    Returns:
        float or ndarray of logistic values.
    """
    t = np.asarray(t, dtype=float)
    return L / (1.0 + np.exp(-k * (t - x0)))


def fit_scurve(years, market_share, L_fixed=None, p0=None):
    """Fit logistic S-curve to historical adoption data.

    Args:
        years: List of years (ints or floats).
        market_share: Corresponding market-share values (percent, 0-100).
        L_fixed: If provided, fix the saturation level and fit only k and x0.
        p0: Initial parameter guess [L, k, x0] (or [k, x0] if L_fixed).

    Returns:
        dict with keys: L, k, x0, r_squared, pcov, data_points, L_fixed.

    Raises:
        ValueError: If fewer than 3 data points are supplied.
    """
    years = np.asarray(years, dtype=float)
    market_share = np.asarray(market_share, dtype=float)

    if len(years) < 3:
        raise ValueError(
            f"Insufficient data: {len(years)} points provided, minimum 3 required "
            "for S-curve fitting."
        )

    ss_tot = np.sum((market_share - np.mean(market_share)) ** 2)

    if L_fixed is not None:
        # Fit only k and x0 with L held constant.
        def _partial(t, k, x0):
            return logistic(t, L_fixed, k, x0)

        if p0 is None:
            p0_inner = [0.3, float(np.max(years)) + 5.0]
        else:
            p0_inner = p0

        popt, pcov = curve_fit(
            _partial, years, market_share, p0=p0_inner, maxfev=10000
        )
        k_fit, x0_fit = popt
        L_fit = float(L_fixed)
        is_fixed = True
    else:
        if p0 is None:
            p0_inner = [90.0, 0.3, float(np.max(years)) + 5.0]
        else:
            p0_inner = p0

        popt, pcov = curve_fit(
            logistic, years, market_share, p0=p0_inner, maxfev=10000
        )
        L_fit, k_fit, x0_fit = popt
        is_fixed = False

    predicted = logistic(years, L_fit, k_fit, x0_fit)
    ss_res = np.sum((market_share - predicted) ** 2)
    r_squared = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    return {
        "L": float(L_fit),
        "k": float(k_fit),
        "x0": float(x0_fit),
        "r_squared": float(r_squared),
        "pcov": pcov.tolist(),
        "data_points": int(len(years)),
        "L_fixed": is_fixed,
    }


def project_scurve(L, k, x0, base_year=2026, horizons=None):
    """Project adoption forward from base_year at specified horizons.

    Confidence intervals are computed by varying k by +/-15% to produce
    optimistic (faster adoption) and pessimistic (slower adoption) bounds.

    Args:
        L: Saturation level.
        k: Growth rate.
        x0: Inflection year.
        base_year: Year to project from (default 2026).
        horizons: List of year offsets (default [5, 10, 20]).

    Returns:
        List of dicts with horizon, year, market_share_pct, confidence_interval.
    """
    if horizons is None:
        horizons = [5, 10, 20]

    k_optimistic = k * 1.15
    k_pessimistic = k * 0.85

    results = []
    for h in horizons:
        year = base_year + h
        share = float(logistic(year, L, k, x0))
        share_hi = float(logistic(year, L, k_optimistic, x0))
        share_lo = float(logistic(year, L, k_pessimistic, x0))
        results.append({
            "horizon": h,
            "year": year,
            "market_share_pct": round(share, 2),
            "confidence_interval": [round(min(share_lo, share_hi), 2),
                                    round(max(share_lo, share_hi), 2)],
        })
    return results


def classify_phase(market_share_pct):
    """Classify adoption phase based on current market share.

    Args:
        market_share_pct: Current market share as a percentage (0-100).

    Returns:
        One of: "pre_rupture", "rupture", "tipping", "rapid_growth", "saturation".
    """
    if market_share_pct < 2.0:
        return "pre_rupture"
    elif market_share_pct < 5.0:
        return "rupture"
    elif market_share_pct < 15.0:
        return "tipping"
    elif market_share_pct <= 80.0:
        return "rapid_growth"
    else:
        return "saturation"


def completion_year(L, k, x0, target_pct=80.0):
    """Compute the year when adoption reaches target_pct.

    Solves L / (1 + exp(-k*(t - x0))) = target_pct for t.

    Args:
        L: Saturation level.
        k: Growth rate.
        x0: Inflection year.
        target_pct: Target market share in absolute percent (default 80.0).

    Returns:
        Year as float (e.g., 2032.7).

    Raises:
        ValueError: If target_pct >= L (unreachable) or target_pct <= 0.
    """
    if target_pct <= 0.0:
        raise ValueError("target_pct must be positive.")
    if target_pct >= L:
        raise ValueError(
            f"target_pct ({target_pct}) must be less than L ({L}); "
            "the S-curve never reaches or exceeds its saturation level."
        )
    if k <= 0:
        raise ValueError(f"Growth rate k must be positive; got {k}")
    # Solve: L / (1 + exp(-k*(t-x0))) = target_pct
    # => 1 + exp(-k*(t-x0)) = L / target_pct
    # => exp(-k*(t-x0)) = (L / target_pct) - 1 = (L - target_pct) / target_pct
    # => -k*(t-x0) = ln((L - target_pct) / target_pct)
    # => t = x0 - ln((L - target_pct) / target_pct) / k
    t = x0 - np.log((L - target_pct) / target_pct) / k
    return float(t)


def xcurve_decline(disruptor_share_pct, years):
    """Compute the mirror incumbent decline curve (X-curve).

    Args:
        disruptor_share_pct: List of disruptor market-share percentages.
        years: Corresponding list of years.

    Returns:
        List of dicts with year and incumbent_share_pct.
    """
    results = []
    for yr, share in zip(years, disruptor_share_pct):
        results.append({
            "year": int(yr),
            "incumbent_share_pct": round(100.0 - float(share), 2),
        })
    return results
