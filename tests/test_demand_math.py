import pytest

from lib import demand_math as dm


# ---------------------------------------------------------------------------
# decompose_demand
# ---------------------------------------------------------------------------

def test_decompose_demand_compliant():
    drivers = [{"name": "EVs", "demand": 500}, {"name": "Grid", "demand": 400}]
    result = dm.decompose_demand(drivers, 1000)
    assert result["coverage_pct"] == 90.0
    assert result["compliant"] is True
    assert result["covered_demand"] == 900


def test_decompose_demand_non_compliant():
    drivers = [{"name": "EVs", "demand": 300}]
    result = dm.decompose_demand(drivers, 1000)
    assert result["coverage_pct"] == 30.0
    assert result["compliant"] is False


def test_decompose_demand_empty_drivers():
    with pytest.raises(ValueError):
        dm.decompose_demand([], 1000)


def test_decompose_demand_zero_total():
    with pytest.raises(ValueError):
        dm.decompose_demand([{"name": "A", "demand": 10}], 0)


def test_decompose_demand_single_driver():
    drivers = [{"name": "Only", "demand": 850}]
    result = dm.decompose_demand(drivers, 1000)
    assert result["compliant"] is True
    assert result["coverage_pct"] == 85.0


# ---------------------------------------------------------------------------
# material_intensity_demand
# ---------------------------------------------------------------------------

def test_material_intensity_demand_basic():
    assert dm.material_intensity_demand(1000, 2.5) == 2500.0


def test_material_intensity_demand_zero_units():
    assert dm.material_intensity_demand(0, 2.5) == 0.0


# ---------------------------------------------------------------------------
# stock_flow_fleet
# ---------------------------------------------------------------------------

def test_stock_flow_fleet_rate_based():
    result = dm.stock_flow_fleet(
        fleet_current=1000, sales=[100, 100, 100], scrappage_rate=0.1, years=3
    )
    assert len(result) == 3
    assert result[0]["fleet"] == 1000
    assert result[0]["scrappage"] == 100.0  # 1000 * 0.1
    assert result[0]["net_change"] == 0.0  # 100 - 100


def test_stock_flow_fleet_with_lifetime():
    result = dm.stock_flow_fleet(
        fleet_current=1000, sales=[100, 100], scrappage_rate=0.5, years=2, lifetime=10
    )
    # lifetime=10 overrides scrappage_rate to 0.1
    assert result[0]["scrappage"] == 100.0  # 1000 * 0.1


def test_stock_flow_fleet_invalid_rate():
    with pytest.raises(ValueError, match="scrappage_rate"):
        dm.stock_flow_fleet(fleet_current=1000, sales=[100], scrappage_rate=1.5, years=1)


def test_stock_flow_fleet_mismatched_sales():
    with pytest.raises(ValueError, match="sales length"):
        dm.stock_flow_fleet(fleet_current=1000, sales=[100, 100], scrappage_rate=0.1, years=3)


def test_stock_flow_fleet_never_negative():
    # Very high scrappage, low sales → fleet should floor at 0
    result = dm.stock_flow_fleet(
        fleet_current=100, sales=[0, 0, 0], scrappage_rate=0.9, years=3
    )
    for row in result:
        assert row["fleet"] >= 0


# ---------------------------------------------------------------------------
# oem_replacement_split
# ---------------------------------------------------------------------------

def test_oem_replacement_split_basic():
    result = dm.oem_replacement_split(
        fleet_growth_units=500, replacement_units=300,
        intensity_oem=2.0, intensity_replacement=1.5
    )
    assert result["oem_demand"] == 1000.0
    assert result["replacement_demand"] == 450.0
    assert result["total_demand"] == 1450.0
    assert abs(result["oem_share_pct"] + result["replacement_share_pct"] - 100.0) < 0.1


def test_oem_replacement_split_default_intensity():
    result = dm.oem_replacement_split(
        fleet_growth_units=100, replacement_units=50, intensity_oem=3.0
    )
    # intensity_replacement defaults to intensity_oem
    assert result["replacement_demand"] == 150.0  # 50 * 3.0


# ---------------------------------------------------------------------------
# aggregate_demand_by_technology
# ---------------------------------------------------------------------------

def test_aggregate_three_streams():
    tech = {"incumbent": 500, "disruptor": 300, "chimera": 200}
    result = dm.aggregate_demand_by_technology(tech)
    assert result["total_demand"] == 1000.0
    assert result["stream_shares"]["incumbent"] == 50.0
    assert result["stream_shares"]["disruptor"] == 30.0
    assert result["stream_shares"]["chimera"] == 20.0


def test_aggregate_single_stream():
    tech = {"disruptor": 1000}
    result = dm.aggregate_demand_by_technology(tech)
    assert result["total_demand"] == 1000.0
    assert result["stream_shares"]["disruptor"] == 100.0


def test_aggregate_empty():
    result = dm.aggregate_demand_by_technology({})
    assert result["total_demand"] == 0.0
    assert result["streams"] == {}


# ---------------------------------------------------------------------------
# regional_demand_split
# ---------------------------------------------------------------------------

def test_regional_split_basic():
    shares = {"China": 0.4, "USA": 0.25, "Europe": 0.2, "RoW": 0.15}
    result = dm.regional_demand_split(1000, shares)
    assert result["regions"]["China"] == 400.0
    assert result["regions"]["USA"] == 250.0
    assert result["regions"]["Europe"] == 200.0
    assert result["regions"]["RoW"] == 150.0


def test_regional_split_shares_exceed_tolerance():
    shares = {"A": 0.8, "B": 0.5}  # sum = 1.3 > 1.1
    with pytest.raises(ValueError, match="exceeding 1.1"):
        dm.regional_demand_split(1000, shares)


def test_regional_split_negative_share():
    shares = {"A": -0.1, "B": 0.5}
    with pytest.raises(ValueError, match="Negative share"):
        dm.regional_demand_split(1000, shares)


# ---------------------------------------------------------------------------
# project_demand_from_scurve
# ---------------------------------------------------------------------------

def test_project_demand_known_scurve():
    # L=1.0 means 100% saturation, x0=2030, k=0.3
    results = dm.project_demand_from_scurve(
        L=1.0, k=0.3, x0=2030,
        total_market_units=1000,
        intensity_disruptor=80,
        intensity_incumbent=20,
        base_year=2026,
        horizons=[5, 10],
    )
    assert len(results) == 2
    assert results[0]["year"] == 2031
    assert results[1]["year"] == 2036
    # At year 2031 (1 year past inflection), disruptor share should be > 0.5
    assert results[0]["disruptor_share"] > 0.5
    # disruptor demand + incumbent demand should equal total
    for r in results:
        assert abs(r["disruptor_demand"] + r["incumbent_demand"] - r["total_demand"]) < 1.0


def test_project_demand_disruptor_grows_incumbent_falls():
    results = dm.project_demand_from_scurve(
        L=1.0, k=0.5, x0=2025,
        total_market_units=1000,
        intensity_disruptor=50,
        intensity_incumbent=50,
        base_year=2020,
        horizons=[5, 10, 20],
    )
    # Over time, disruptor share should increase
    shares = [r["disruptor_share"] for r in results]
    assert shares == sorted(shares)  # monotonically increasing


# ---------------------------------------------------------------------------
# validate_stock_flow_consistency
# ---------------------------------------------------------------------------

def test_validate_consistent():
    series = [
        {"fleet": 1000, "sales": 100, "scrappage": 50},
        {"fleet": 1050, "sales": 110, "scrappage": 52.5},
        {"fleet": 1107.5, "sales": 120, "scrappage": 55.375},
    ]
    result = dm.validate_stock_flow_consistency(series)
    assert result["consistent"] is True
    assert result["violations"] == []


def test_validate_inconsistent():
    series = [
        {"fleet": 1000, "sales": 100, "scrappage": 50},
        {"fleet": 999, "sales": 100, "scrappage": 50},  # should be 1050
    ]
    result = dm.validate_stock_flow_consistency(series)
    assert result["consistent"] is False
    assert 0 in result["violations"]


# ---------------------------------------------------------------------------
# full_demand_analysis (integration)
# ---------------------------------------------------------------------------

def test_full_demand_analysis():
    result = dm.full_demand_analysis(
        demand_drivers=[
            {"name": "EVs", "demand": 600},
            {"name": "Grid Storage", "demand": 300},
        ],
        total_commodity_demand=1000,
        scurve_params={"L": 0.9, "k": 0.3, "x0": 2030},
        material_intensities={"disruptor": 80, "incumbent": 20},
        market_size=1_000_000,
        regions={"China": 0.4, "USA": 0.25, "Europe": 0.2, "RoW": 0.15},
    )
    assert set(result.keys()) == {
        "decomposition", "projections", "technology_streams", "regional_split",
    }
    assert result["decomposition"]["compliant"] is True
    assert len(result["projections"]) == 3  # default horizons [5, 10, 20]
    assert "China" in result["regional_split"]["regions"]
    assert result["technology_streams"]["total_demand"] > 0
