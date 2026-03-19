from lib import output_writer as ow

def test_display_name():
    assert ow._display_name("stdf-cost-curve") == "Cost Curve"
    assert ow._display_name("stdf-custom-agent") == "Custom Agent"

def test_build_header():
    header = ow.build_header("stdf-cost-curve", "Battery Economics", 0.87)
    assert "Cost Curve" in header
    assert "0.87" in header
    assert "---" in header

def test_build_reasoning_section():
    section = ow.build_reasoning_section("  hello world  ")
    assert "## Agent Reasoning" in section
    assert "hello world" in section

def test_build_sources_section():
    assert "No sources cited" in ow.build_sources_section([])
    non_empty = ow.build_sources_section(["S1", "S2"])
    assert "- S1" in non_empty
    assert "- S2" in non_empty

def test_build_agent_output():
    output = ow.build_agent_output("stdf-capability", "EV", 0.8, "Reason", "Body", ["src"])
    assert "## Agent Reasoning" in output
    assert "## Agent Output" in output
    assert "## Sources" in output

def test_table_to_markdown():
    table = ow.table_to_markdown(["A", "B"], [["1"], ["2", "3", "EXTRA"]])
    assert "| A | B |" in table
    assert "| --- | --- |" in table

def test_key_values_to_markdown():
    assert ow.key_values_to_markdown({}) == ""
    kv = ow.key_values_to_markdown({"L": 90, "k": 0.3})
    assert "- **L:** 90" in kv
    assert "- **k:** 0.3" in kv
