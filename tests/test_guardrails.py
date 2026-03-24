"""Tests for lib.guardrails validation module."""

from lib import guardrails


def test_validate_banned_vocabulary_clean():
    text = "disruption and stellar energy cost-curve dynamics"
    result = guardrails.validate_banned_vocabulary(text)
    assert result == []


def test_validate_banned_vocabulary_with_violations():
    text = "The transition to clean energy requires data."
    result = guardrails.validate_banned_vocabulary(text)
    terms = {v["term"] for v in result}
    assert "transition" in terms
    assert "clean energy" in terms
    assert all(v["count"] >= 1 for v in result)


def test_validate_banned_sources_iea():
    text = "Data from https://www.iea.org/reports/weo-2025 shows..."
    result = guardrails.validate_banned_sources(text)
    assert len(result) >= 1
    assert any("iea" in v["pattern"].lower() for v in result)


def test_validate_banned_sources_bnef():
    text = "According to bloombergnef analysis and bnef.com data..."
    result = guardrails.validate_banned_sources(text)
    assert len(result) >= 1
    assert any("bnef" in v["pattern"].lower() for v in result)


def test_validate_banned_sources_clean():
    text = "Data from government statistical agencies shows cost decline."
    result = guardrails.validate_banned_sources(text)
    assert result == []


def test_validate_no_forecast_language_clean():
    text = "Historical data shows battery cost fell from $1100/kWh in 2010 to $92/kWh in 2024."
    result = guardrails.validate_no_forecast_language(text)
    assert result == []


def test_validate_no_forecast_with_violations():
    text = "Battery costs are projected to reach $50/kWh. The outlook for 2030 is positive. Forecast shows growth."
    result = guardrails.validate_no_forecast_language(text)
    keywords = {v["keyword"].lower() for v in result}
    assert "projected" in keywords
    assert "outlook" in keywords
    assert "forecast" in keywords


def test_validate_anti_patterns_clean():
    text = "S-curve adoption dynamics and exponential cost decline."
    result = guardrails.validate_anti_patterns(text)
    assert result == []


def test_validate_anti_patterns_with_violations():
    text = "Using linear extrapolation we see linear growth. Green hydrogen and net zero target."
    result = guardrails.validate_anti_patterns(text)
    phrases = {v["phrase"].lower() for v in result}
    assert "linear extrapolation" in phrases
    assert "linear growth" in phrases
    assert "green hydrogen" in phrases
    assert "net zero target" in phrases


def test_validate_date_consistency():
    text = "In 2030 the cost was $50/kWh [observed] based on market data."
    result = guardrails.validate_date_consistency(text, "2026-03-16")
    assert len(result) >= 1
    assert result[0]["year_found"] == "2030"


def test_validate_date_consistency_no_issue():
    text = "In 2024 the cost was $92/kWh [observed]."
    result = guardrails.validate_date_consistency(text, "2026-03-16")
    assert result == []


def test_validate_date_consistency_no_date():
    text = "In 2030 costs are [observed]."
    result = guardrails.validate_date_consistency(text, None)
    assert result == []


def test_validate_citation_provenance():
    text = """| Year | Cost | Unit | Source |
|------|------|------|--------|
| 2020 | 137 | $/kWh | BNEF 2020 |
| 2024 | 92 | $/kWh |  |
"""
    result = guardrails.validate_citation_provenance(text)
    assert len(result) >= 1
    assert "Empty Source" in result[0]["issue"]


def test_validate_citation_provenance_clean():
    text = """| Year | Cost | Unit | Source |
|------|------|------|--------|
| 2020 | 137 | $/kWh | BNEF 2020 |
| 2024 | 92 | $/kWh | Industry report 2024 |
"""
    result = guardrails.validate_citation_provenance(text)
    assert result == []


def test_full_guardrail_check_pass():
    text = "disruption and stellar energy cost-curve dynamics. Battery cost: $92/kWh (2024)."
    result = guardrails.full_guardrail_check(text, "2026-03-16")
    assert result["pass"] is True
    assert len(result["critical_violations"]) == 0
    assert "PASS" in result["report"]


def test_full_guardrail_check_fail():
    text = (
        "The transition to clean energy requires IEA data. "
        "Source: https://www.iea.org/reports/weo. "
        "Using linear extrapolation for the outlook."
    )
    result = guardrails.full_guardrail_check(text, "2026-03-16")
    assert result["pass"] is False
    assert len(result["critical_violations"]) > 0
    assert "FAIL" in result["report"]


def test_validate_scenario_range_caught():
    """'scenario range' should be caught as a banned scenario label."""
    text = "The scenario range is 2025-2030 for battery adoption."
    result = guardrails.validate_scenario_labels(text)
    phrases = {v["phrase"].lower() for v in result}
    assert "scenario range" in phrases


def test_validate_confidence_range_not_caught():
    """'confidence range' should NOT be caught — only 'scenario range' is banned."""
    text = "The confidence range is 0.75-0.85."
    result = guardrails.validate_scenario_labels(text)
    assert result == []


def test_full_guardrail_check_scenario_range():
    """full_guardrail_check should catch 'scenario range' as critical."""
    text = "The scenario range is 2025-2030."
    result = guardrails.full_guardrail_check(text)
    assert result["pass"] is False
    assert any("scenario range" in v["detail"].lower() for v in result["critical_violations"])


def test_full_guardrail_check_report_format():
    text = "transition to clean energy"
    result = guardrails.full_guardrail_check(text)
    assert "## Guardrail Validation Report" in result["report"]
    assert "CRITICAL violations:" in result["report"]
