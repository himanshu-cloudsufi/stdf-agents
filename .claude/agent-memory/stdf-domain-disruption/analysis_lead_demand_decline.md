---
name: Lead demand decline analysis
description: Materials sector: lead (Pb) demand disruption via LFP/BEV across automotive SLI, stationary backup, and motive power sub-domains (March 2026)
type: project
---

Lead demand disruption analysis completed March 2026. Key facts:

- **Baseline**: 12,259 kt global lead demand (2024, Rethinkx catalog) [observed]
- **10% threshold**: 11,033 kt (1,226 kt reduction required)
- **Demand structure**: 62.5% automotive SLI; 16.2% stationary backup; 7.4% motive power; 13.8% non-battery
- **Largest single component**: car SLI replacement/aftermarket = 3,377 kt (27.5% of total) — still growing in 2024
- **ICE fleet**: 1.305B units in 2024; net contraction beginning (~−24.8M/yr); replacement demand lagged by 10–15 years
- **BEV share**: 15.0% of new car sales (2024); 11M BEVs globally

**Disruption vectors mapped**:
1. BEV eliminating SLI new-vehicle demand (From Above) — 810 kt, declining
2. BEV fleet turnover shrinking SLI aftermarket (From Above, lagged) — 3,377 kt, slow decline beginning
3. LFP-UPS displacing VRLA in telecom/datacenter backup (Big Bang) — 1,987 kt; Li-ion 33% share in telecom (2024)
4. EV-FL displacing lead-acid traction in forklifts (From Below, mature) — 913 kt; 65% EV forklift share
5. LFP direct 12V SLI substitution (pre-inflection) — cost gap closing in China ~2030

**Chimeras**: PHEV (retains 12V SLI), 48V mild hybrid AGM, EFB start-stop

**Cost crossovers**:
- LFP vs lead-acid pack $/kWh: already crossed in China (circa 2019), USA/Europe still 2–3x
- LFP SLI 12V vs lead-acid SLI: approaching in China ~2030 (LFP $100 → $32; LA flat at $25)

**Output file**: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/lead-demand-decline/agents/01-domain-disruption.md`

**Why:** User asked when lead demand drops 10% relative to 2024 — requires full disruption map as input to demand-decomposer and scurve-fitter agents.

**How to apply:** When continuing this pipeline run, downstream agents should read this file via UPSTREAM_FILES. Key handoff: ICE fleet just turned negative, LFP-UPS is at S-curve inflection, 2W/3W Li-ion penetration in Asia is an unresolved critical gap.
