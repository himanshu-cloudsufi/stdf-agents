from lib import markdown_parser as mp

SAMPLE_TEXT = """# STDF Cost Curve Agent — Topic

**Agent:** `stdf-cost-curve` | **Confidence:** 0.87

---

## Agent Reasoning

Reasoning line.

---

## Agent Output

### Metrics

- **Learning Rate:** 12.3%
- **Model**: exponential

### Cost Table

| Year | Cost |
| --- | --- |
| 2020 | 100 |
| 2021 | 90 |

## Sources

- Source A
* Source B
"""

def test_parse_agent_file():
    parsed = mp.parse_agent_file(SAMPLE_TEXT)
    assert parsed["agent_name"] == "stdf-cost-curve"
    assert parsed["confidence"] == 0.87
    assert "Agent Output" in parsed["sections"]
    assert parsed["sources"] == ["Source A", "Source B"]

def test_extract_section():
    assert mp.extract_section(SAMPLE_TEXT, "Missing") is None
    reasoning = mp.extract_section(SAMPLE_TEXT, "Agent Reasoning")
    assert "Reasoning" in reasoning

def test_extract_table():
    table = mp.extract_table(SAMPLE_TEXT)
    assert table[0] == {"Year": "2020", "Cost": "100"}
    assert mp.extract_table("no table here") == []

def test_extract_table_scoped():
    table = mp.extract_table(SAMPLE_TEXT, heading="Cost Table")
    assert table[1] == {"Year": "2021", "Cost": "90"}

def test_extract_key_values():
    text = "- **Alpha:** 1\n- **Beta**: 2\n- **Gamma:** three"
    kv = mp.extract_key_values(text)
    assert kv == {"Alpha": "1", "Beta": "2", "Gamma": "three"}

def test_extract_key_values_scoped():
    scoped = mp.extract_key_values(SAMPLE_TEXT, heading="Metrics")
    assert scoped["Learning Rate"] == "12.3%"
    assert scoped["Model"] == "exponential"

def test_extract_confidence():
    assert mp.extract_confidence("**Confidence:** 0.95") == 0.95
    assert mp.extract_confidence("no confidence here") is None
