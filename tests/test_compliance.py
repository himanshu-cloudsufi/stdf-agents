import pytest
from lib import compliance as comp

@pytest.fixture
def criteria():
    return [
        {"id": "c1", "description": "Critical check", "severity": "CRITICAL"},
        {"id": "h1", "description": "High check", "severity": "HIGH"},
        {"id": "m1", "description": "Medium check", "severity": "MEDIUM"},
    ]

def test_create_checklist(criteria):
    checklist = comp.create_checklist(criteria)
    assert len(checklist) == 3
    assert checklist[0].id == "c1"
    assert checklist[0].status == "PENDING"

def test_update_criterion(criteria):
    checklist = comp.create_checklist(criteria)
    comp.update_criterion(checklist, "h1", "PASS", "done")
    assert checklist[1].status == "PASS"
    assert checklist[1].note == "done"

def test_update_missing_id(criteria):
    checklist = comp.create_checklist(criteria)
    with pytest.raises(KeyError):
        comp.update_criterion(checklist, "missing", "PASS")

def test_has_critical_failure(criteria):
    checklist = comp.create_checklist(criteria)
    assert comp.has_critical_failure(checklist) is False
    comp.update_criterion(checklist, "c1", "FAIL")
    assert comp.has_critical_failure(checklist) is True

def test_is_compliant(criteria):
    checklist = comp.create_checklist(criteria)
    comp.update_criterion(checklist, "c1", "PASS")
    comp.update_criterion(checklist, "h1", "PASS")
    assert comp.is_compliant(checklist) is True
    comp.update_criterion(checklist, "h1", "PENDING")
    assert comp.is_compliant(checklist) is False

def test_overall_status(criteria):
    checklist = comp.create_checklist(criteria)
    comp.update_criterion(checklist, "c1", "PASS")
    comp.update_criterion(checklist, "h1", "PASS")
    comp.update_criterion(checklist, "m1", "PASS")
    assert comp.overall_status(checklist) == "COMPLIANT"
    comp.update_criterion(checklist, "m1", "FAIL")
    assert comp.overall_status(checklist) == "DEGRADED"
    comp.update_criterion(checklist, "h1", "FAIL")
    assert comp.overall_status(checklist) == "NON-COMPLIANT"

def test_checklist_to_markdown(criteria):
    checklist = comp.create_checklist(criteria)
    comp.update_criterion(checklist, "c1", "PASS", "ok|pipe")
    md = comp.checklist_to_markdown(checklist)
    assert "| c1 | CRITICAL | PASS |" in md
    assert "ok/pipe" in md
    assert "**Overall:" in md


def test_synthesizer_criteria_defined():
    assert hasattr(comp, "SYNTHESIZER_CRITERIA")
    assert len(comp.SYNTHESIZER_CRITERIA) >= 3
    ids = {c["id"] for c in comp.SYNTHESIZER_CRITERIA}
    assert "6.1" in ids
    assert "6.3" in ids
    # Check that critical criteria exist
    critical = [c for c in comp.SYNTHESIZER_CRITERIA if c["severity"] == "CRITICAL"]
    assert len(critical) >= 2


def test_commodity_demand_criteria_defined():
    assert hasattr(comp, "COMMODITY_DEMAND_CRITERIA")
    assert len(comp.COMMODITY_DEMAND_CRITERIA) >= 9
    ids = {c["id"] for c in comp.COMMODITY_DEMAND_CRITERIA}
    assert "7.1" in ids
    assert "7.4" in ids
    # Check that critical criteria exist (7.1, 7.2, 7.4)
    critical = [c for c in comp.COMMODITY_DEMAND_CRITERIA if c["severity"] == "CRITICAL"]
    assert len(critical) >= 3


def test_pipeline_criteria_defined():
    assert hasattr(comp, "PIPELINE_CRITERIA")
    assert len(comp.PIPELINE_CRITERIA) >= 3
    ids = {c["id"] for c in comp.PIPELINE_CRITERIA}
    assert "P.1" in ids
    assert "P.4" in ids
    # Check that critical criteria exist
    critical = [c for c in comp.PIPELINE_CRITERIA if c["severity"] == "CRITICAL"]
    assert len(critical) >= 1
