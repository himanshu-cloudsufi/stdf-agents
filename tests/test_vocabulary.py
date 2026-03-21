from lib import vocabulary as vocab

def test_scan_banned():
    hits = vocab.scan_banned("This transition is GREEN.")
    terms = {h["term"] for h in hits}
    assert "transition" in terms
    assert "green" in terms

def test_scan_banned_no_false_positives():
    hits = vocab.scan_banned("The greenhouse is large.")
    terms = {h["term"] for h in hits}
    assert "green" not in terms

def test_check_required():
    checks = vocab.check_required("disruption and stellar energy patterns")
    status = {c["term"]: c["present"] for c in checks}
    assert status["disruption"] is True
    assert status["stellar energy"] is True
    assert status["cost-curve dynamics"] is False

def test_vocabulary_report_violations():
    report = vocab.vocabulary_report("Transition to clean energy with disruption.")
    assert "Banned terms found:" in report
    assert "transition" in report.lower()

def test_vocabulary_report_all_clear():
    text = (
        "disruption stellar energy cost-curve dynamics "
        "market-driven disruption incumbent displacement S-curve adoption"
    )
    report = vocab.vocabulary_report(text)
    assert "0" in report or "all clear" in report.lower()


def test_scan_banned_sources_iea_url():
    hits = vocab.scan_banned_sources("See https://www.iea.org/data for details.")
    assert len(hits) >= 1
    assert any("iea" in h["pattern"] for h in hits)


def test_scan_banned_sources_bnef_url():
    hits = vocab.scan_banned_sources("From bnef.com and bloombergnef data.")
    assert len(hits) >= 1
    assert any("bnef" in h["pattern"] for h in hits)


def test_scan_banned_sources_eia_url():
    hits = vocab.scan_banned_sources("Data at eia.gov shows production.")
    assert len(hits) >= 1
    assert any("eia" in h["pattern"] for h in hits)


def test_scan_banned_sources_opec_url():
    hits = vocab.scan_banned_sources("OPEC data from opec.org quarterly report.")
    assert len(hits) >= 1
    assert any("opec" in h["pattern"] for h in hits)


def test_scan_banned_sources_clean():
    hits = vocab.scan_banned_sources("Government statistical agency published data.")
    assert hits == []


def test_scan_banned_sources_iea_inline_without_caution():
    """IEA mentioned inline without CAUTION tag should be a violation."""
    hits = vocab.scan_banned_sources("According to IEA, costs fell 20%.")
    assert len(hits) >= 1
    assert any("IEA" in h.get("reason", "") or "IEA" in h.get("pattern", "") for h in hits)


def test_scan_banned_sources_iea_inline_with_caution():
    """IEA mentioned with [CAUTION: IEA ...] tag on same line should pass."""
    hits = vocab.scan_banned_sources(
        "IEA data [CAUTION: IEA source — historical data only] shows cost decline."
    )
    # Filter to org-name hits only (not URL hits)
    org_hits = [h for h in hits if "mentioned without" in h.get("reason", "")]
    assert org_hits == []


def test_scan_banned_sources_bnef_inline_without_caution():
    """BNEF mentioned inline without CAUTION tag should be a violation."""
    hits = vocab.scan_banned_sources("BNEF reports battery cost at $92/kWh.")
    assert len(hits) >= 1
    assert any("BNEF" in h.get("reason", "") or "BNEF" in h.get("pattern", "") for h in hits)
