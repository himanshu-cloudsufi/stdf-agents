"""STDF v2 Compliance Checker Framework.

Provides a generic checklist system with CRITICAL / HIGH / MEDIUM severity
levels. Pre-defined criteria constants are included for each STDF agent:
cost-curve, capability, adoption-scurve, and tipping-point.
"""

from dataclasses import dataclass


@dataclass
class Criterion:
    """A single compliance criterion."""

    id: str
    description: str
    severity: str  # "CRITICAL" | "HIGH" | "MEDIUM"
    status: str = "PENDING"  # "PASS" | "FAIL" | "PENDING"
    note: str = ""


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def create_checklist(criteria: list[dict]) -> list[Criterion]:
    """Create a checklist from a list of dicts with keys *id*, *description*, *severity*."""
    return [
        Criterion(id=c["id"], description=c["description"], severity=c["severity"])
        for c in criteria
    ]


def update_criterion(checklist: list[Criterion], criterion_id: str, status: str, note: str = "") -> None:
    """Update the status and optional note for the criterion matching *criterion_id*."""
    for c in checklist:
        if c.id == criterion_id:
            c.status = status
            c.note = note
            return
    raise KeyError(f"Criterion '{criterion_id}' not found in checklist")


def has_critical_failure(checklist: list[Criterion]) -> bool:
    """Return True if ANY CRITICAL criterion has status FAIL."""
    return any(c.severity == "CRITICAL" and c.status == "FAIL" for c in checklist)


def is_compliant(checklist: list[Criterion]) -> bool:
    """Return True if no CRITICAL failures and all HIGH criteria pass."""
    for c in checklist:
        if c.severity == "CRITICAL" and c.status == "FAIL":
            return False
        if c.severity == "HIGH" and c.status != "PASS":
            return False
    return True


def overall_status(checklist: list[Criterion]) -> str:
    """Return 'COMPLIANT', 'NON-COMPLIANT', or 'DEGRADED'.

    - NON-COMPLIANT: any CRITICAL failure, or any HIGH not PASS.
    - DEGRADED: all CRITICAL/HIGH pass but at least one MEDIUM fails.
    - COMPLIANT: everything passes.
    """
    critical_ok = all(c.status == "PASS" for c in checklist if c.severity == "CRITICAL")
    high_ok = all(c.status == "PASS" for c in checklist if c.severity == "HIGH")
    medium_ok = all(c.status == "PASS" for c in checklist if c.severity == "MEDIUM")

    if not critical_ok or not high_ok:
        return "NON-COMPLIANT"
    if not medium_ok:
        return "DEGRADED"
    return "COMPLIANT"


def checklist_to_markdown(checklist: list[Criterion]) -> str:
    """Generate a markdown table summarising the checklist."""
    lines = [
        "| ID | Severity | Status | Description | Note |",
        "|---|---|---|---|---|",
    ]
    status_icon = {"PASS": "PASS", "FAIL": "FAIL", "PENDING": "PENDING"}
    for c in checklist:
        s = status_icon.get(c.status, c.status)
        note = c.note.replace("|", "/")
        lines.append(f"| {c.id} | {c.severity} | {s} | {c.description} | {note} |")
    lines.append("")
    lines.append(f"**Overall: {overall_status(checklist)}**")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Pre-defined criteria constants
# ---------------------------------------------------------------------------

COST_CURVE_CRITERIA: list[dict] = [
    {"id": "2.1",  "severity": "CRITICAL", "description": "Historical disruptor cost trajectory shown (min 3 points over 5+ years)"},
    {"id": "2.2",  "severity": "HIGH",     "description": "Historical incumbent cost trajectory shown"},
    {"id": "2.3",  "severity": "HIGH",     "description": "Current disruptor cost stated with source"},
    {"id": "2.4",  "severity": "HIGH",     "description": "Current incumbent cost stated with source"},
    {"id": "2.5",  "severity": "CRITICAL", "description": "Service-level units used ($/kWh, $/km — NOT hardware cost alone)"},
    {"id": "2.6",  "severity": "HIGH",     "description": "Direct cost comparison (no TCO/DCF)"},
    {"id": "2.7",  "severity": "HIGH",     "description": "Cost curve dynamics applied — empirically observed learning rate from data, NOT assumed ~20%"},
    {"id": "2.8",  "severity": "HIGH",     "description": "Disruptor cost forecast = exponential decay"},
    {"id": "2.9",  "severity": "HIGH",     "description": "Incumbent cost forecast = flat or rising"},
    {"id": "2.10", "severity": "HIGH",     "description": "Competitive threshold identified — cost point + year range"},
    {"id": "2.11", "severity": "MEDIUM",   "description": "Inflection threshold identified — disruptor reaches 50-70% of incumbent cost"},
]

CAPABILITY_CRITERIA: list[dict] = [
    {"id": "3.1", "severity": "CRITICAL", "description": "Min 3 capability dimensions identified with named metrics, units, numeric values"},
    {"id": "3.2", "severity": "HIGH",     "description": "Historical capability trajectory shown (min 3 data points spanning 3+ years per major dimension)"},
    {"id": "3.3", "severity": "MEDIUM",   "description": "Current disruptor capability stated with source"},
    {"id": "3.4", "severity": "MEDIUM",   "description": "Current incumbent capability stated with source"},
    {"id": "3.5", "severity": "HIGH",     "description": "Competitive capability threshold identified per dimension"},
    {"id": "3.6", "severity": "HIGH",     "description": "Multi-dimensional comparison across ALL identified dimensions"},
]

ADOPTION_CRITERIA: list[dict] = [
    {"id": "4.1", "severity": "CRITICAL", "description": "S-curve model required (NO linear extrapolation)"},
    {"id": "4.2", "severity": "HIGH",     "description": "Current market share with source"},
    {"id": "4.3", "severity": "HIGH",     "description": "Adoption phase classification (pre_rupture/rupture/tipping/rapid_growth/saturation)"},
    {"id": "4.4", "severity": "MEDIUM",   "description": "X-curve incumbent decline mapping"},
    {"id": "4.5", "severity": "MEDIUM",   "description": "Market trauma recognition (5 mechanisms)"},
    {"id": "4.6", "severity": "HIGH",     "description": "Regional breakdown (min 3 regions: China, USA, Europe)"},
]

TIPPING_CRITERIA: list[dict] = [
    {"id": "5.1", "severity": "CRITICAL", "description": "Tipping point clearly identified — explicit year/range + defining conditions"},
    {"id": "5.2", "severity": "HIGH",     "description": "All 3 tipping conditions checked simultaneously"},
    {"id": "5.3", "severity": "HIGH",     "description": "Cost parity condition mapped with evidence from Cost Curve agent"},
    {"id": "5.4", "severity": "MEDIUM",   "description": "Capability parity condition mapped with evidence from Capability agent"},
    {"id": "5.5", "severity": "MEDIUM",   "description": "Post-tipping dynamics stated — BOTH incumbent vicious cycle AND disruptor virtuous cycle"},
]

SYNTHESIZER_CRITERIA: list[dict] = [
    {"id": "6.1", "severity": "CRITICAL", "description": "All 7 STDF phases present in narrative"},
    {"id": "6.2", "severity": "CRITICAL", "description": "Every claim traces to a subagent output"},
    {"id": "6.3", "severity": "CRITICAL", "description": "Zero banned vocabulary terms in output"},
    {"id": "6.4", "severity": "HIGH",     "description": "Key conclusion is unambiguous with rupture window"},
    {"id": "6.5", "severity": "HIGH",     "description": "Confidence calculation shown transparently"},
    {"id": "6.6", "severity": "HIGH",     "description": "Data gaps and assumptions aggregated from all subagents"},
    {"id": "6.7", "severity": "MEDIUM",   "description": "Handoff context contains all required keys"},
]

COMMODITY_DEMAND_CRITERIA: list[dict] = [
    {"id": "7.1", "severity": "CRITICAL", "description": "80% demand driver coverage — all drivers >=80% of total demand identified and individually modeled"},
    {"id": "7.2", "severity": "CRITICAL", "description": "Recursive decomposition to market products — NOT intermediate components"},
    {"id": "7.3", "severity": "HIGH",     "description": "Each major demand driver follows full disruption process"},
    {"id": "7.4", "severity": "CRITICAL", "description": "Demand = derivative of product/service forecast, NOT GDP proxies"},
    {"id": "7.5", "severity": "HIGH",     "description": "Material intensity by technology stated with explicit coefficients per variant"},
    {"id": "7.6", "severity": "HIGH",     "description": "Incumbent + Disruptor + Chimera demand tracked as three parallel streams"},
    {"id": "7.7", "severity": "HIGH",     "description": "OEM + Replacement split tracked with explicit lifetimes"},
    {"id": "7.8", "severity": "MEDIUM",   "description": "Stock-flow fleet model consistent: Fleet(t+1) = Fleet(t) + Sales(t) - Scrappage(t)"},
    {"id": "7.9", "severity": "HIGH",     "description": "Regional demand breakdown (China, USA, Europe, RoW) with region-specific parameters"},
]

PIPELINE_CRITERIA: list[dict] = [
    {"id": "P.1", "severity": "CRITICAL", "description": "Zero banned vocabulary across all agent outputs"},
    {"id": "P.2", "severity": "CRITICAL", "description": "No forecast web data cited as observed"},
    {"id": "P.3", "severity": "HIGH",     "description": "All data has provenance tags (T1/T2/T3)"},
    {"id": "P.4", "severity": "HIGH",     "description": "No banned source URLs (IEA, BNEF, EIA, OPEC)"},
    {"id": "P.5", "severity": "MEDIUM",   "description": "All agent output files written successfully"},
    {"id": "P.6", "severity": "MEDIUM",   "description": "Cross-agent consistency (tipping year agrees across agents)"},
]
