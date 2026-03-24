---
name: Li-Ion vs. Lead-Acid — Cost Parity Finding (Lead Demand Decline)
description: Multi-segment cost parity status for Li-ion vs. lead-acid batteries; service-level and nameplate MET, SLI automotive IMMINENT/NOT_MET
type: project
---

Li-ion vs. lead-acid battery disruption has three structurally distinct cost comparison segments with different parity outcomes.

**Segment 1 — Service-level ($/kWh delivered):**
Status: **MET** (predates 2010). Li-ion C0 = $0.54/kWh_del at 2010 already below lead-acid USA $1.60 and China $1.33. By 2024: Li-ion $0.050/kWh_del vs. lead-acid USA $0.960 (5.2% ratio, 19x advantage). Inflection concluded; incumbent displacement governed by installed-base replacement, not cost competition.

**Segment 2 — Nameplate pack cost ($/kWh):**
Status: **MET**. USA parity: 2019–2020 at $228.6/kWh. China parity: 2020–2021 at $186.9/kWh. By 2024: Li-ion $115/kWh (50.3% of USA incumbent, 61.5% of China incumbent). R²=0.9541, 15 data points.

**Segment 3 — SLI automotive unit cost ($/battery, 62.5% of lead demand):**
Status: **IMMINENT** (USA), **NOT_MET** (China). USA parity 2027–2028 (Li-ion $135 vs. lead-acid $55). China parity 2031–2032 (Li-ion $100 vs. lead-acid $25). SLI fit: R²=0.9897, 8 data points. USA parity is within 2 years of analysis date 2026-03-20 → IMMINENT. China is 5+ years away → NOT_MET.

**Confidence:** 0.87 (inherited from cost-fitter; R² high but 18% terminal deviation at 2024 flagged).

**Key structural note:** SLI (62.5% of lead demand) still has 4x price premium for Li-ion in China and 2.5x in USA. The nameplate MET result does not translate to demand displacement — actual lead displacement requires SLI parity as the binding constraint.

**Why:** Lead demand decline pipeline analysis as of 2026-03-20.

**How to apply:** When this disruption is referenced in future runs, use the segment table. Tipping synthesizer should note that SLI parity (NOT_MET China) is the binding constraint on actual lead demand displacement despite stationary/nameplate parity being MET.
