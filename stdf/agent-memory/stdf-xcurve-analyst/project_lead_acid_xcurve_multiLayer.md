---
name: Lead-acid battery X-curve — multi-layer incumbent, recycling death spiral, March 2026 run
description: Key findings, data sources, and patterns from the lead-acid battery X-curve analysis (Li-ion displacement, lead-demand-decline pipeline, March 2026)
type: project
---

## Key Pattern: Three-Layer Incumbent With Different Death Spiral Timings

Lead-acid incumbent is NOT a single entity. Three layers face the X-curve at different paces:
1. **Battery manufacturers** (Clarios, EnerSys, East Penn, Chaowei, Tianneng) -- spiral begins ~2028-2030
2. **Primary/secondary lead smelters** -- spiral begins when feedstock crunch hits (already active in China 2024-2025)
3. **Lead recycling industry** -- EARLIEST crisis because 97-99% recycling rate means entire feedstock pool depends on lead-acid battery scrap

**Why:** Li-ion displacement of non-SLI segments (telecom, datacenter) is already >40-50% in 2026. This means new lead-acid battery installations in those segments dropped sharply 2019-2024. Batteries installed 2019-2024 yield scrap in 2022-2029 (3-7 year lifetimes). So feedstock crunch hits recyclers 3-5 years BEFORE aggregate demand crosses the 10% threshold.

**How to apply:** Always analyze the recycling/smelting layer separately from battery manufacturers. Recycling is the canary -- if it's in crisis, battery manufacturers are 3-5 years behind in the spiral.

## Critical Observed Data Point (China)

China secondary lead smelter operating rate:
- 2024 average: <35% (record low per SMM)
- Early 2025: fell to **22.3%** (Shanghai Metal Market, metal.com, observed)
- Nameplate capacity: 14.6 million tons/year vs. ~7.6 million tons actual supply (shortfall >7Mt)
- Losses: widespread; smelters "considering shutdown" per SMM reports
- Scrap battery prices: 12,200 yuan/mt (e-bike scrap, record high 2024, SMM observed)

This is well below the 65% utilization breakeven. At 22.3% utilization with 57% fixed cost fraction, per-unit cost is +202% above breakeven -- classic death spiral confirmation.

## Source Reliability for Lead-Acid Analyses

**Most reliable primary sources:**
- **USGS Mineral Commodity Summaries (annual)** [T1]: US production, mine count, secondary lead volumes, consumption by sector. PDF downloadable at pubs.usgs.gov. Lead data is extremely well covered annually.
- **Shanghai Metal Market (metal.com)** [T3]: Best source for China secondary lead operating rates, scrap prices, smelter economics. Paywalled for some content but free summaries often available.
- **Battery Council International (batterycouncil.org)** [T3]: US facility closure history, recycling statistics, lobbying positions. Self-interested but factually reliable on facility counts.
- **International Lead and Zinc Study Group (ILZSG)**: global supply/demand balance (often reported by USGS/SMM rather than directly)

**Persistent data gaps:**
- Company-level capex for Clarios, EnerSys, East Penn (private or limited disclosure)
- Workforce/employment numbers for lead mining communities (Missouri Viburnum Trend)
- Talent flight from lead-acid to Li-ion sector -- no primary source found
- Lead-acid wholesale pricing trends at manufacturer level

## Recycling Industry Economic Model

Fixed cost fraction for secondary smelters: ~57% (furnace capital, energy, environmental permits, fixed labor)
Breakeven utilization: ~65%
Cost impact at observed China utilization:
- 35% utilization: +106% cost above baseline
- 22% utilization: +202% cost above baseline

Formula: new_cost_ratio = 0.57 / utilization + 0.43; cost_increase = (new_cost_ratio - 1.0) * 100

## X-Curve Stage Milestones (Lead-Acid, 2026 Baseline)

From the five-segment composite model (S-curve parameters from scurve-fitter):
- 2026: 100% -- Pre-disruption (baseline)
- 2028: 90.5% -- Boundary Pre-disruption/Early volume loss (-10% milestone)
- 2029: 84.6% -- Early volume loss
- 2030: 77.8% -- Accelerating decline (BEV fleet inflection approaching)
- 2032: 62.6% -- Accelerating decline (peak velocity -7.7 pp/yr in 2031-2032)
- 2033: 55.1% -- Death spiral active
- 2035: 43.0% -- Death spiral active
- 2038: 33.1% -- Advanced collapse
- 2045: 28.2% -- Advanced collapse (floor)

Peak velocity: -7.7 pp/year at 2031-2032 (BEV fleet crossing its 2031.77 inflection point)

## Policy Lobbying -- USA Lead-Acid Specifics

Battery Council International (BCI) is lobbying for the "USA Batteries Act" to:
- Eliminate excise tax on lead oxide, antimony, and sulfuric acid (primary lead battery inputs)
- Cited rationale: "foreign manufacturers have unfair cost advantage"
- Context: DOE grants $150M (Clarios) + $198M (EnerSys) to modernize lead smelting -- defensive subsidies, not growth investment
- This is textbook "Policy Lobbying" market trauma mechanism: ADVANCED stage in USA

## EU Batteries Regulation 2023/1542 Impact

- Requires 85% minimum recycled lead content in batteries from 2030
- Mandates free collection of all waste batteries including SLI lead-acid
- Effective 2023 (in force); applied from Feb 2024
- Effect on X-curve: preserves recycling loop's relevance in Europe (protects incumbent recyclers) but raises compliance costs for smaller operators, accelerating consolidation to large integrated players
