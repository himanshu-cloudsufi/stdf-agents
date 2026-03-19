import pytest
from lib import upstream_reader as ur

SAMPLE_MD = """# STDF Cost Curve Agent — Topic

**Agent:** `stdf-cost-curve` | **Confidence:** 0.91

---

## Agent Reasoning

Reasoning text.

---

## Agent Output

### Disruptor Cost Trajectory

| Year | Cost |
| --- | --- |
| 2020 | 100 |

## Sources

- Source A
"""

def test_read_upstream(tmp_path):
    path = tmp_path / "01-cost-curve.md"
    path.write_text(SAMPLE_MD)
    result = ur.read_upstream(str(path))
    assert result["agent_name"] == "stdf-cost-curve"
    assert result["confidence"] == 0.91

def test_read_upstream_missing():
    with pytest.raises(FileNotFoundError):
        ur.read_upstream("does-not-exist.md")

def test_read_all_upstream(tmp_path):
    p1 = tmp_path / "01-domain-disruption.md"
    p2 = tmp_path / "02-cost-curve.md"
    p1.write_text(SAMPLE_MD)
    p2.write_text(SAMPLE_MD)
    result = ur.read_all_upstream([str(p1), str(p2)])
    assert "domain_disruption" in result
    assert "cost_curve" in result

@pytest.mark.parametrize("stem,expected", [
    ("01-domain-disruption", "domain_disruption"),
    ("10-cost-curve", "cost_curve"),
    ("capability-agent", "capability_agent"),
])
def test_filename_to_slug(stem, expected):
    assert ur._filename_to_slug(stem) == expected

def test_get_cost_trajectory():
    upstream = {"sections": {"Disruptor Cost Trajectory": "| Year | Cost |\n| --- | --- |\n| 2020 | 100 |"}}
    result = ur.get_cost_trajectory(upstream)
    assert result == [{"Year": "2020", "Cost": "100"}]

def test_get_capability_dimensions():
    upstream = {"sections": {"Capability Dimensions": "| Dimension | Status |\n| --- | --- |\n| Density | MET |"}}
    assert ur.get_capability_dimensions(upstream) == [{"Dimension": "Density", "Status": "MET"}]

def test_get_scurve_parameters():
    upstream = {"sections": {"S-Curve Parameters": "- **L:** 90\n- **k:** 0.3"}}
    assert ur.get_scurve_parameters(upstream) == {"L": "90", "k": "0.3"}

def test_get_demand_decomposition():
    upstream = {"sections": {"Demand Decomposition Tree": "| Product | Demand |\n| --- | --- |\n| EVs | 500 |"}}
    result = ur.get_demand_decomposition(upstream)
    assert result == [{"Product": "EVs", "Demand": "500"}]


def test_get_demand_decomposition_empty():
    upstream = {"sections": {"Other Section": "no tables here"}}
    assert ur.get_demand_decomposition(upstream) == []


def test_get_material_intensity():
    upstream = {"sections": {"Material Intensity by Technology": "| Product | Intensity |\n| --- | --- |\n| BEV | 80 |"}}
    result = ur.get_material_intensity(upstream)
    assert result == [{"Product": "BEV", "Intensity": "80"}]


def test_get_material_intensity_empty():
    upstream = {"sections": {"Unrelated": "text"}}
    assert ur.get_material_intensity(upstream) == []


def test_sections_text():
    text = ur._sections_text({"A": "one", "B": "two"})
    assert "### A" in text
    assert "one" in text
