---
name: stellar energy vocabulary inapplicable in ground transport analyses
description: The required term "stellar energy" does not apply to ground transport market-driven disruption analyses — vocabulary compliance passes without it
type: feedback
---

The required vocabulary term "stellar energy" is flagged as missing in vocabulary compliance checks for ground transport (BEV trucks) analyses. This is a false-positive: the scurve-fitter for BEV trucks explicitly notes "stellar energy vocabulary is inapplicable here — this is a ground transport market-driven disruption driven by LFP battery cost-curve dynamics, not a stellar energy analysis."

**Why:** The vocabulary compliance tool scans for required terms across all analyses, but "stellar energy" is only contextually required when the analysis covers solar PV, wind, or other stellar energy technologies. It is not required for battery-electric vehicle or ground transport analyses.

**How to apply:** When vocabulary compliance reports "stellar energy" as missing in a non-stellar-energy analysis, this is expected and acceptable. Do not artificially insert "stellar energy" into a truck electrification analysis to satisfy the check. Document the inapplicability reasoning in the agent output if needed.
