"""Tipping-point condition checking and confidence aggregation for STDF agents.

Used by stdf-tipping-point (Cat 5) and stdf-synthesizer to evaluate when all
three tipping conditions are met and to aggregate pipeline confidence scores.

Dependencies: numpy
"""

import numpy as np


def check_tipping_conditions(cost_parity_year, capability_parity_year,
                             adoption_readiness_year):
    """Determine the tipping point from the three prerequisite conditions.

    The tipping point is the year when ALL three conditions are simultaneously
    satisfied — i.e., the maximum of the three condition years.

    Args:
        cost_parity_year: Year cost parity is reached (float or None).
        capability_parity_year: Year capability parity is reached (float or None).
        adoption_readiness_year: Year adoption readiness is reached (float or None).

    Returns:
        dict with: tipping_year, binding_constraint, all_met, conditions.
    """
    conditions = [
        {"name": "cost_parity", "year": cost_parity_year,
         "met": cost_parity_year is not None},
        {"name": "capability_parity", "year": capability_parity_year,
         "met": capability_parity_year is not None},
        {"name": "adoption_readiness", "year": adoption_readiness_year,
         "met": adoption_readiness_year is not None},
    ]

    all_met = all(c["met"] for c in conditions)

    if all_met:
        years = [cost_parity_year, capability_parity_year, adoption_readiness_year]
        tipping_year = float(max(years))
        # The binding constraint is whichever condition is met last.
        binding = max(conditions, key=lambda c: c["year"])["name"]
    else:
        tipping_year = None
        # Binding constraint is the first unmet condition found.
        unmet = [c["name"] for c in conditions if not c["met"]]
        binding = unmet[0] if unmet else None

    return {
        "tipping_year": tipping_year,
        "binding_constraint": binding,
        "all_met": all_met,
        "conditions": conditions,
    }


def completion_timeline_from_scurve(L, k, x0, target_pct=80.0):
    """Compute completion timeline with uncertainty from S-curve parameters.

    Uses the same inversion formula as scurve_math.completion_year, plus
    optimistic/pessimistic bounds from k +/- 15%.

    Args:
        L: Saturation level.
        k: Growth rate.
        x0: Inflection year.
        target_pct: Target market share in absolute percent (default 80.0).

    Returns:
        dict with: target_year, year_range, L, k, x0.

    Raises:
        ValueError: If target_pct >= L or target_pct <= 0.
    """
    if target_pct <= 0.0:
        raise ValueError("target_pct must be positive.")
    if target_pct >= L:
        raise ValueError(
            f"target_pct ({target_pct}) must be less than L ({L})."
        )

    def _solve(k_val):
        return x0 - np.log((L - target_pct) / target_pct) / k_val

    target_year = float(_solve(k))
    year_optimistic = float(_solve(k * 1.15))  # Faster adoption
    year_pessimistic = float(_solve(k * 0.85))  # Slower adoption

    lo = int(np.floor(min(year_optimistic, year_pessimistic)))
    hi = int(np.ceil(max(year_optimistic, year_pessimistic)))

    return {
        "target_year": round(target_year, 1),
        "year_range": (lo, hi),
        "L": float(L),
        "k": float(k),
        "x0": float(x0),
    }


def confidence_aggregate(subagent_scores, penalty=0.0, critical_failures=False):
    """Aggregate confidence scores across all STDF subagents.

    Pipeline:
      1. Base = arithmetic mean of non-None scores.
      2. Subtract penalty (from degraded/missing agents).
      3. If critical_failures, cap at 0.50.
      4. Floor at 0.10.

    Args:
        subagent_scores: Dict mapping agent name -> confidence float (or None).
        penalty: Numeric penalty to subtract (default 0.0).
        critical_failures: Whether any critical agent has failed (default False).

    Returns:
        dict with: base, penalty, critical_cap_applied, final, calculation.
    """
    valid_scores = {k: v for k, v in subagent_scores.items() if v is not None}

    if not valid_scores:
        return {
            "base": 0.0,
            "penalty": float(penalty),
            "critical_cap_applied": critical_failures,
            "final": 0.10,
            "calculation": "No valid subagent scores; floor applied -> 0.10",
        }

    base = float(np.mean(list(valid_scores.values())))
    adjusted = base - penalty

    steps = [f"mean({', '.join(f'{k}={v:.2f}' for k, v in valid_scores.items())}) = {base:.3f}"]

    if penalty > 0:
        steps.append(f"- penalty {penalty:.2f} = {adjusted:.3f}")

    cap_applied = False
    if critical_failures and adjusted > 0.50:
        adjusted = 0.50
        cap_applied = True
        steps.append(f"critical failure cap -> {adjusted:.3f}")

    if adjusted < 0.10:
        adjusted = 0.10
        steps.append(f"floor applied -> {adjusted:.3f}")

    final = round(adjusted, 3)
    steps.append(f"final = {final:.3f}")

    return {
        "base": round(base, 3),
        "penalty": float(penalty),
        "critical_cap_applied": cap_applied,
        "final": final,
        "calculation": "; ".join(steps),
    }


def regional_tipping_assessment(regions):
    """Assess tipping conditions per region.

    Args:
        regions: List of dicts, each with keys:
            region (str), cost_parity_met (bool), capability_parity_met (bool),
            adoption_readiness_met (bool), adoption_readiness_year (float | None).

    Returns:
        List of dicts with: region, tipping_year, binding_constraint, conditions_met.
    """
    results = []
    for r in regions:
        conditions_met = []
        if r.get("cost_parity_met"):
            conditions_met.append("cost_parity")
        if r.get("capability_parity_met"):
            conditions_met.append("capability_parity")
        if r.get("adoption_readiness_met"):
            conditions_met.append("adoption_readiness")

        all_met = len(conditions_met) == 3

        if all_met:
            tipping_year = r.get("adoption_readiness_year")
            binding = "adoption_readiness"
        else:
            tipping_year = None
            # Binding constraint is the first unmet condition.
            all_conditions = ["cost_parity", "capability_parity", "adoption_readiness"]
            unmet = [c for c in all_conditions if c not in conditions_met]
            binding = unmet[0] if unmet else None

        results.append({
            "region": r["region"],
            "tipping_year": float(tipping_year) if tipping_year is not None else None,
            "binding_constraint": binding,
            "conditions_met": conditions_met,
        })

    return results
