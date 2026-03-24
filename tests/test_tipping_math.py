import math
import pytest
from lib import tipping_math as tm

def test_check_tipping_conditions_all_met():
    result = tm.check_tipping_conditions(2028.0, 2030.0, 2029.0)
    assert result["all_met"] is True
    assert result["tipping_year"] == 2030.0
    assert result["binding_constraint"] == "capability_parity"

def test_check_tipping_conditions_partial():
    result = tm.check_tipping_conditions(None, 2030.0, None)
    assert result["all_met"] is False
    assert result["tipping_year"] is None

def test_completion_timeline():
    result = tm.completion_timeline_from_scurve(L=100.0, k=0.2, x0=2030.0, target_pct=80.0)
    expected = 2030.0 - math.log((100.0 - 80.0) / 80.0) / 0.2
    assert result["target_year"] == pytest.approx(round(expected, 1), abs=0.05)

@pytest.mark.parametrize("target", [0.0, -5.0, 100.0, 120.0])
def test_completion_timeline_invalid(target):
    with pytest.raises(ValueError):
        tm.completion_timeline_from_scurve(L=100.0, k=0.2, x0=2030.0, target_pct=target)

def test_confidence_aggregate_basic():
    result = tm.confidence_aggregate({"cost": 0.8, "capability": 0.6, "adoption": 0.7})
    assert result["base"] == pytest.approx(0.7)
    assert result["final"] == pytest.approx(0.7)

def test_confidence_aggregate_critical_cap():
    result = tm.confidence_aggregate({"a": 0.9, "b": 0.8}, penalty=0.1, critical_failures=True)
    assert result["final"] == 0.5
    assert result["critical_cap_applied"] is True

def test_confidence_aggregate_floor():
    result = tm.confidence_aggregate({"a": 0.2, "b": 0.1}, penalty=0.3)
    assert result["final"] == 0.1

def test_regional_tipping():
    regions = [
        {"region": "A", "cost_parity_met": True, "capability_parity_met": True, "adoption_readiness_met": True, "adoption_readiness_year": 2032},
        {"region": "B", "cost_parity_met": True, "capability_parity_met": False, "adoption_readiness_met": False, "adoption_readiness_year": None},
    ]
    result = tm.regional_tipping_assessment(regions)
    assert result[0]["tipping_year"] == 2032.0
    assert result[1]["tipping_year"] is None
