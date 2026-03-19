import math

import numpy as np
import pytest

from lib import scurve_math as sm


@pytest.fixture
def logistic_fixture():
    years = list(range(2010, 2021))
    L, k, x0 = 90.0, 0.35, 2016.0
    shares = sm.logistic(years, L, k, x0).tolist()
    return years, shares, L, k, x0


def test_logistic_scalar_and_array():
    scalar = sm.logistic(2030, 100, 0.2, 2030)
    arr = sm.logistic([2029, 2030, 2031], 100, 0.2, 2030)

    assert scalar == pytest.approx(50.0)
    assert arr.shape == (3,)
    assert arr[0] < arr[1] < arr[2]


def test_fit_scurve_happy_path(logistic_fixture):
    years, shares, L, k, x0 = logistic_fixture
    result = sm.fit_scurve(years, shares, p0=[85.0, 0.3, 2015.0])

    assert result["data_points"] == len(years)
    assert result["L_fixed"] is False
    assert result["L"] == pytest.approx(L, rel=1e-2)
    assert result["k"] == pytest.approx(k, rel=1e-2)
    assert result["x0"] == pytest.approx(x0, rel=1e-2)
    assert result["r_squared"] > 0.999


def test_fit_scurve_with_fixed_L(logistic_fixture):
    years, shares, L, _, _ = logistic_fixture
    result = sm.fit_scurve(years, shares, L_fixed=L, p0=[0.3, 2015.0])

    assert result["L_fixed"] is True
    assert result["L"] == pytest.approx(L, rel=1e-6)
    assert result["r_squared"] > 0.999


def test_fit_scurve_requires_minimum_points():
    with pytest.raises(ValueError):
        sm.fit_scurve([2020, 2021], [1, 2])


def test_project_scurve_fields_and_confidence_bounds():
    results = sm.project_scurve(L=100, k=0.2, x0=2030, base_year=2020, horizons=[5, 10])

    assert len(results) == 2
    for row in results:
        assert set(row.keys()) == {"horizon", "year", "market_share_pct", "confidence_interval"}
        low, high = row["confidence_interval"]
        assert low <= row["market_share_pct"] <= high


def test_project_scurve_empty_horizons():
    assert sm.project_scurve(L=100, k=0.2, x0=2030, horizons=[]) == []


@pytest.mark.parametrize(
    "share,expected",
    [
        (0.0, "pre_rupture"),
        (1.99, "pre_rupture"),
        (2.0, "rupture"),
        (4.99, "rupture"),
        (5.0, "tipping"),
        (14.99, "tipping"),
        (15.0, "rapid_growth"),
        (80.0, "rapid_growth"),
        (80.01, "saturation"),
    ],
)
def test_classify_phase_boundaries(share, expected):
    assert sm.classify_phase(share) == expected


def test_completion_year_math_verification():
    year = sm.completion_year(L=100.0, k=0.2, x0=2030.0, target_pct=80.0)
    expected = 2030.0 - math.log((100.0 - 80.0) / 80.0) / 0.2
    assert year == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize("target", [0.0, -1.0, 100.0, 120.0])
def test_completion_year_invalid_targets(target):
    with pytest.raises(ValueError):
        sm.completion_year(L=100.0, k=0.2, x0=2030.0, target_pct=target)


def test_xcurve_decline_happy_and_zip_truncation():
    result = sm.xcurve_decline(disruptor_share_pct=[10, 20, 30], years=[2020, 2021])
    assert result == [
        {"year": 2020, "incumbent_share_pct": 90.0},
        {"year": 2021, "incumbent_share_pct": 80.0},
    ]
