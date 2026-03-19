import pytest
from lib import capability_math as cm

def test_fit_trajectory_min_points():
    with pytest.raises(ValueError):
        cm.fit_trajectory([2020], [100])

def test_fit_trajectory_constant():
    result = cm.fit_trajectory([2020, 2021, 2022], [10, 10, 10])
    assert result["curve_type"] == "linear"
    assert result["params"]["b"] == 0.0
    assert result["r_squared"] == 1.0

def test_fit_trajectory_linear_fallback(monkeypatch):
    def _raise(*args, **kwargs):
        raise RuntimeError("fit failure")
    monkeypatch.setattr(cm, "curve_fit", _raise)
    result = cm.fit_trajectory([2020, 2021, 2022], [10, 12, 14])
    assert result["curve_type"] == "linear"
    assert result["params"]["b"] > 0

@pytest.mark.parametrize(
    "current,threshold,hib,status,gap",
    [
        (110, 100, True, "MET", -10.0),
        (90, 100, True, "APPROACHING", 10.0),
        (70, 100, True, "NOT_MET", 30.0),
        (90, 100, False, "MET", -10.0),
        (110, 100, False, "APPROACHING", 10.0),
        (130, 100, False, "NOT_MET", 30.0),
    ],
)
def test_threshold_check(current, threshold, hib, status, gap):
    result = cm.threshold_check(current, threshold, higher_is_better=hib)
    assert result["status"] == status
    assert result["gap_pct"] == pytest.approx(gap, abs=0.01)

def test_convergence_pattern():
    assert cm.convergence_pattern([{"dimension": "a", "status": "NOT_MET", "met_year": None}]) == "divergent"
    assert cm.convergence_pattern([
        {"dimension": "a", "status": "MET", "met_year": 2030},
        {"dimension": "b", "status": "MET", "met_year": 2032},
        {"dimension": "c", "status": "MET", "met_year": 2033},
    ]) == "simultaneous"
    assert cm.convergence_pattern([
        {"dimension": "a", "status": "MET", "met_year": 2030},
        {"dimension": "b", "status": "MET", "met_year": 2038},
    ]) == "sequential"

def test_parity_year_already_met():
    year = cm.parity_year_estimate([2020, 2021], [100, 120], threshold=110, higher_is_better=True)
    assert year == 2021.0

def test_multi_dimensional_summary():
    dims = [
        {"dimension": "density", "status": "MET", "met_year": 2030},
        {"dimension": "cost", "status": "APPROACHING", "met_year": 2032},
        {"dimension": "speed", "status": "NOT_MET", "met_year": None},
    ]
    result = cm.multi_dimensional_summary(dims)
    assert result["total"] == 3
    assert result["met_count"] == 1
    assert result["all_met"] is False
    assert "speed" in result["blocking_dimensions"]
