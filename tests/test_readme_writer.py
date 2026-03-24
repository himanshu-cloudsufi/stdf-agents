from datetime import date as real_date
from lib import readme_writer as rw

class FakeDate:
    @staticmethod
    def today():
        return real_date(2026, 3, 14)

def test_write_readme_with_conclusion(monkeypatch):
    monkeypatch.setattr(rw, "date", FakeDate)
    content = rw.write_readme(
        slug="energy-storage",
        topic="Energy Storage",
        agent_results=[
            {"agent_name": "stdf-cost-curve", "confidence": 0.9123, "status": "OK", "duration_s": 12.34, "file_path": "02-cost-curve.md"},
            {"agent_name": "stdf-capability", "confidence": None, "status": "FAILED", "duration_s": None, "file_path": "03-capability.md"},
        ],
        output_dir="output/energy-storage",
        conclusion="Storage disruption is likely before 2035.",
    )
    assert "# STDF Analysis — Energy Storage" in content
    assert "**Run date:** 2026-03-14" in content
    assert "stdf-cost-curve" in content
    assert "stdf-capability" in content
    assert "Storage disruption is likely before 2035." in content

def test_write_readme_default_conclusion(monkeypatch):
    monkeypatch.setattr(rw, "date", FakeDate)
    content = rw.write_readme(
        slug="topic",
        topic="Topic",
        agent_results=[],
        output_dir="output/topic",
        conclusion="",
    )
    assert "00-final-synthesis.md" in content
