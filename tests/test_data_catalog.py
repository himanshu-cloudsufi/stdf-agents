import json
from pathlib import Path
import pytest
from lib import data_catalog as dc

@pytest.fixture(autouse=True)
def clear_cache():
    dc._cached_index.cache_clear()
    yield
    dc._cached_index.cache_clear()

@pytest.fixture
def catalog_root(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    entries = [
        {"dataset_name": "Lithium-ion battery cost", "type": "cost", "units": "$/kWh", "region": "Global", "level_name": "Energy Storage", "source": "S1", "description": "Battery pack prices decline", "file_path": "data/battery_cost.json"},
        {"dataset_name": "Solar market share", "type": "adoption", "units": "%", "region": "Europe", "level_name": "Power", "source": "S2", "description": "Solar adoption growth", "file_path": "data/solar_adoption.json"},
        {"dataset_name": "Broken curve", "type": "cost", "units": "$", "region": "Global", "level_name": "Energy Storage", "source": "S4", "description": "Missing XY", "file_path": "data/broken.json"},
    ]
    (data_dir / "index.json").write_text(json.dumps(entries))
    (data_dir / "battery_cost.json").write_text(json.dumps({"X": [2020, 2021], "Y": [120, 100]}))
    (data_dir / "solar_adoption.json").write_text(json.dumps({"X": [2020], "Y": [10]}))
    (data_dir / "broken.json").write_text(json.dumps({"dataset_name": "broken"}))
    return tmp_path, entries

def test_normalize():
    assert dc._normalize("  Lithium-Ion_Battery  ") == "lithium ion battery"

def test_load_index(catalog_root):
    root, entries = catalog_root
    assert dc.load_index(root) == entries

def test_search_curves(catalog_root):
    root, _ = catalog_root
    result = dc.search_curves("battery cost", root=root, limit=2)
    assert len(result) <= 2
    assert result[0]["dataset_name"] == "Lithium-ion battery cost"

def test_filter_entries(catalog_root):
    root, entries = catalog_root
    filtered = dc._filter_entries(entries, type_="COST", sector="energy", region="GLOBAL")
    assert len(filtered) == 2
    assert all(e["type"] == "cost" for e in filtered)

def test_load_curve(catalog_root):
    root, _ = catalog_root
    curve = dc.load_curve("data/battery_cost.json", root=root)
    assert curve["X"] == [2020, 2021]
    assert curve["Y"] == [120, 100]

def test_get_xy_data(catalog_root):
    root, _ = catalog_root
    x, y = dc.get_xy_data("data/battery_cost.json", root=root)
    assert x == [2020, 2021]
    assert y == [120, 100]

def test_get_xy_data_missing_keys(catalog_root):
    root, _ = catalog_root
    with pytest.raises(KeyError):
        dc.get_xy_data("data/broken.json", root=root)

def test_list_sectors_and_types(catalog_root):
    root, _ = catalog_root
    assert "Energy Storage" in dc.list_sectors(root=root)
    assert "cost" in dc.list_types(root=root)
