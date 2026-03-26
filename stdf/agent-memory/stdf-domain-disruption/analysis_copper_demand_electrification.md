---
name: Copper demand electrification disruption analysis
description: Materials sector: copper demand reshaped by BEV, solar PV, wind, BESS, and grid T&D electrification disruption vectors (March 2026)
type: project
---

Copper demand disruption analysis completed March 2026. Key facts:

- **Baseline**: 27,347 kt global copper demand (2024) [T2 catalog, observed]
- **China share**: 55.8% = 15,251 kt (2024)
- **Demand CAGR 2015-2024**: 1.9%/yr aggregate — masks 12-52%/yr growth in electrification sub-vectors

**End-use structure (2024)**:
- Electrical & Electronics: 33% = 9,025 kt
- Building & Construction: 26% = 7,110 kt
- Transportation: 15% = 4,102 kt
- Industrial Machinery: 12% = 3,282 kt
- Consumer Products: 10% = 2,735 kt
- Other: 4% = 1,094 kt

**Disruption vectors mapped**:
1. BEV displacing ICE in transport (From Above): 5% of global = 1,367 kt in 2024; grew from 1% in 2015 at 19.6%/yr share growth. BEV = ~70 kg/vehicle vs ICE = ~23 kg/vehicle (3x intensity)
2. Solar PV displacing coal/gas generation (From Below): 2% of global = 547 kt in 2024; grew from 0.7% in 2015 at 12.4%/yr
3. Onshore/offshore wind displacing fossil-fuel generation (From Below): 1.5% of global = 410 kt in 2024; grew from 0.7% in 2015
4. LFP BESS displacing gas peakers (Big Bang): BESS CAGR 69.6%/yr; no dedicated copper % in catalog
5. Grid T&D electrification infrastructure expansion (Systemic): largest incremental demand vector; not disaggregated in catalog
6. Aluminum substitution counter-vector: per-BEV copper declining ~83 kg (2015) → ~70 kg (2024) → ~62 kg (2030 est.); aluminum harness at 12.1% CAGR

**Convergence labels**: SWB (Solar+Wind+Battery), SWB+EV, SWB+HP, BSAF

**Supply cost dynamics**:
- Mining cost 2024: $4,600/mt (up 77% from $2,600/mt in 2012) at 4.9%/yr CAGR
- Market price 2024: $4.15/lb = $9,148/mt
- ICSG deficit 2024: ~167,000 kt refined copper

**Technology flow classification**:
- Copper itself: X-Flow (Jevons applies)
- BEV: Hybrid (X-Flow dominant)
- Solar PV, Wind, BESS: Stellar (Jevons does NOT apply)
- Grid T&D: X-Flow (Jevons applies)

**Data gaps**: Grid T&D copper time series absent from catalog; BESS copper intensity not verified; aluminum substitution quantity curve absent; building sector electrification copper not quantified

**Output file**: `/Users/himanshuchauhan/TONY/STDF/stdf-agents/output/copper-demand-electrification/agents/01-domain-disruption.md`

**Why:** User asked to analyze copper demand drivers and how electrification, EVs, solar, wind, and battery storage disruptions impact copper demand.

**How to apply:** When continuing this pipeline run, downstream cost-fitter needs copper mining cost curve (T2 catalog) and should model copper intensity coefficients as time-varying (declining) for BEV, solar, and wind. Demand-decomposer needs kg-Cu/unit intensity data for each disruptor technology. Key unresolved question: does volume growth dominate over thrifting in determining net copper demand trajectory?
