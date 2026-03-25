import math

import pytest

from lib import cost_curve_math as ccm


@pytest.fixture
def disruptor_exp_series():
    years = [2020, 2021, 2022, 2023]
    costs = [100.0 * math.exp(-0.1 * (y - 2020)) for y in years]
    return years, costs


def test_exponential_fit_happy_path(disruptor_exp_series):
    years, costs = disruptor_exp_series
    result = ccm.exponential_fit(years, costs)

    assert result["ref_year"] == 2020
    assert result["C0"] == pytest.approx(100.0, rel=1e-3)
    assert result["r"] == pytest.approx(0.1, rel=1e-5)
    assert result["r_squared"] == pytest.approx(1.0, rel=1e-4)
    assert all(abs(v) <= 1e-3 for v in result["residuals"])
    assert "C(t) =" in result["formula"]


@pytest.mark.parametrize(
    "years,costs",
    [
        ([2020, 2021], [100, 90]),
        ([2020, 2021, 2022], [100, 90]),
        ([2020, 2021, 2022], [100, 90, 0]),
    ],
)
def test_exponential_fit_errors(years, costs):
    with pytest.raises(ValueError):
        ccm.exponential_fit(years, costs)


def test_learning_rate_from_decay_per_year():
    value = ccm.learning_rate_from_decay(0.1, basis="per_year")
    expected = round((1 - math.exp(-0.1)) * 100, 2)
    assert value == expected


def test_learning_rate_from_decay_per_doubling():
    # After fix: no longer returns constant 50.0 for all r>0
    # For r=0.1: b = 0.1*ln(2) ≈ 0.0693, LR = (1 - 2^-0.0693)*100 ≈ 4.69%
    lr_small = ccm.learning_rate_from_decay(0.1, basis="per_doubling")
    lr_large = ccm.learning_rate_from_decay(0.5, basis="per_doubling")
    assert lr_small > 0
    assert lr_large > lr_small  # larger decay -> larger learning rate
    assert lr_large < 100  # sanity bound


@pytest.mark.parametrize("r", [0.0, -0.01])
def test_learning_rate_from_decay_per_doubling_requires_positive_r(r):
    with pytest.raises(ValueError):
        ccm.learning_rate_from_decay(r, basis="per_doubling")


def test_learning_rate_from_decay_unknown_basis():
    with pytest.raises(ValueError):
        ccm.learning_rate_from_decay(0.1, basis="weekly")


def test_learning_rate_from_deployment_happy_path():
    deployment = [1, 2, 4, 8]
    costs = [100.0, 100.0 / math.sqrt(2), 50.0, 50.0 / math.sqrt(2)]
    result = ccm.learning_rate_from_deployment(costs, deployment)

    assert result["b"] == pytest.approx(0.5, rel=1e-3)
    assert result["learning_rate_pct"] == pytest.approx(29.29, abs=0.05)
    assert result["r_squared"] == pytest.approx(1.0, rel=1e-4)
    assert result["basis"] == "per_doubling_deployment"


@pytest.mark.parametrize(
    "costs,deployment",
    [
        ([100, 90], [1, 2]),
        ([100, 90, 80], [1, 2]),
        ([100, 90, -1], [1, 2, 3]),
        ([100, 90, 80], [1, 0, 3]),
    ],
)
def test_learning_rate_from_deployment_errors(costs, deployment):
    with pytest.raises(ValueError):
        ccm.learning_rate_from_deployment(costs, deployment)


@pytest.mark.parametrize(
    "costs,expected_model",
    [
        ([100.0, 102.0, 104.0], "linear_rising"),
        ([100.0, 98.0, 96.0], "linear_declining"),
        ([100.0, 100.5, 101.0], "flat"),
    ],
)
def test_incumbent_trend_fit_models(costs, expected_model):
    years = [2020, 2021, 2022]
    result = ccm.incumbent_trend_fit(years, costs)
    assert result["model"] == expected_model
    assert "r_squared" in result


def test_incumbent_trend_fit_errors():
    with pytest.raises(ValueError):
        ccm.incumbent_trend_fit([2020], [100])
    with pytest.raises(ValueError):
        ccm.incumbent_trend_fit([2020, 2021], [100])


def test_competitive_threshold_happy_path():
    result = ccm.competitive_threshold(C0=100.0, r=0.1, ref_year=2020, incumbent_cost=50.0)
    expected_year = 2020 + math.log(2) / 0.1

    assert result["crossover_year"] == pytest.approx(round(expected_year, 2), abs=0.01)
    assert result["crossover_year_range"] == (2026, 2027)
    assert result["cost_at_parity"] == 50.0


def test_competitive_threshold_already_at_parity():
    result = ccm.competitive_threshold(C0=50.0, r=0.1, ref_year=2020, incumbent_cost=60.0)
    assert result["crossover_year"] == 2020.0
    assert result["crossover_year_range"] == (2020, 2020)
    assert result["note"] == "Parity already reached at reference year"


@pytest.mark.parametrize(
    "kwargs",
    [
        {"C0": 0, "r": 0.1, "ref_year": 2020, "incumbent_cost": 50},
        {"C0": 100, "r": 0, "ref_year": 2020, "incumbent_cost": 50},
        {"C0": 100, "r": 0.1, "ref_year": 2020, "incumbent_cost": -1},
    ],
)
def test_competitive_threshold_errors(kwargs):
    with pytest.raises(ValueError):
        ccm.competitive_threshold(**kwargs)


def test_inflection_threshold_happy_path():
    result = ccm.inflection_threshold(C0=100.0, r=0.1, ref_year=2020, incumbent_cost=100.0)
    assert result["year_range"] == (2023, 2027)
    assert result["disruptor_cost_range"] == (50.0, 70.0)
    assert result["percent_of_incumbent_range"] == (50.0, 70.0)


def test_inflection_threshold_partial_already_reached():
    result = ccm.inflection_threshold(C0=60.0, r=0.1, ref_year=2020, incumbent_cost=100.0)
    assert result["year_range"][0] == 2020
    assert result["year_range"][1] >= 2021


@pytest.mark.parametrize(
    "kwargs",
    [
        {"C0": 0, "r": 0.1, "ref_year": 2020, "incumbent_cost": 100},
        {"C0": 100, "r": 0, "ref_year": 2020, "incumbent_cost": 100},
        {"C0": 100, "r": 0.1, "ref_year": 2020, "incumbent_cost": 100, "low_pct": 0.8, "high_pct": 0.7},
    ],
)
def test_inflection_threshold_errors(kwargs):
    with pytest.raises(ValueError):
        ccm.inflection_threshold(**kwargs)


def test_convert_solar_wp_to_kwh_happy_and_zero():
    result = ccm.convert_solar_wp_to_kwh(0.5, capacity_factor=0.2, lifetime_years=25, degradation_adj=0.05)
    expected = round((0.5 * 1000) / (0.2 * 8760 * 25 * (1 - 0.05)), 6)
    assert result == expected
    assert ccm.convert_solar_wp_to_kwh(0.0) == 0.0


@pytest.mark.parametrize("cost_per_wp,capacity_factor", [(-0.1, 0.2), (0.5, 0), (0.5, 1)])
def test_convert_solar_wp_to_kwh_errors(cost_per_wp, capacity_factor):
    with pytest.raises(ValueError):
        ccm.convert_solar_wp_to_kwh(cost_per_wp, capacity_factor=capacity_factor)


def test_convert_ev_vehicle_to_km_happy_path():
    result = ccm.convert_ev_vehicle_to_km(30000, 8000, 2000, 200000)
    assert result == round((30000 + 8000 + 2000) / 200000, 6)


def test_convert_ev_vehicle_to_km_errors():
    with pytest.raises(ValueError):
        ccm.convert_ev_vehicle_to_km(30000, 8000, 2000, 0)


def test_convert_storage_cap_to_delivered_happy_path():
    result = ccm.convert_storage_cap_to_delivered(120, cycle_life=4000, round_trip_efficiency=0.9, depth_of_discharge=0.8)
    expected = round(120 / (4000 * 0.9 * 0.8), 6)
    assert result == expected


@pytest.mark.parametrize(
    "kwargs",
    [
        {"cost_per_kwh_cap": 100, "cycle_life": 0},
        {"cost_per_kwh_cap": 100, "cycle_life": 1000, "round_trip_efficiency": 0},
        {"cost_per_kwh_cap": 100, "cycle_life": 1000, "depth_of_discharge": 1.2},
    ],
)
def test_convert_storage_cap_to_delivered_errors(kwargs):
    with pytest.raises(ValueError):
        ccm.convert_storage_cap_to_delivered(**kwargs)


def test_plausibility_check_normal():
    result = ccm.plausibility_check(20.0, "batteries")
    assert result["status"] == "NORMAL"
    assert result["bounds"] == (12.0, 28.0)
    assert result["tech_class"] == "batteries"


def test_plausibility_check_caution():
    # 11% is below 12% range but within 20% margin (floor = 12 * 0.8 = 9.6)
    result = ccm.plausibility_check(11.0, "batteries")
    assert result["status"] == "CAUTION"
    assert "below" in result["explanation"].lower()


def test_plausibility_check_implausible():
    # 5% is far below 12% range and below 20% margin floor of 9.6
    result = ccm.plausibility_check(5.0, "batteries")
    assert result["status"] == "IMPLAUSIBLE"
    assert "far below" in result["explanation"].lower()


def test_plausibility_check_generic_fallback():
    result = ccm.plausibility_check(15.0, "unknown_tech")
    assert result["tech_class"] == "generic"
    assert result["bounds"] == (5.0, 35.0)
    assert result["status"] == "NORMAL"


def test_full_cost_analysis_pipeline():
    result = ccm.full_cost_analysis(
        disruptor_years=[2020, 2021, 2022, 2023],
        disruptor_costs=[100, 90, 81, 72.9],
        incumbent_years=[2020, 2021, 2022],
        incumbent_costs=[120, 121, 122],
    )
    assert set(result.keys()) == {
        "exponential_fit",
        "learning_rate_per_year",
        "learning_rate_per_doubling",
        "plausibility_check",
        "incumbent_trend",
        "competitive_threshold",
        "inflection_threshold",
    }
    assert 0 < result["learning_rate_per_doubling"] < 100
    assert result["plausibility_check"]["status"] in ("NORMAL", "CAUTION", "IMPLAUSIBLE")
