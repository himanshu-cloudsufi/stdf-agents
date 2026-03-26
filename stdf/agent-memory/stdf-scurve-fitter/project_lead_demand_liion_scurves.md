---
name: Lead Demand Decline — Li-Ion vs. Lead-Acid S-Curve Parameters
description: Fitted S-curve parameters for all five segments of the lead-demand decline analysis; catalog data paths and key discrepancies with tipping-synthesizer
type: project
---

Five-segment disruption analysis fitted from catalog data for the lead-demand decline pipeline run (`output/lead-demand-decline/`).

**Fitted parameters (2026-03-20):**

| Segment | L | k | x0 | R² | N | L fixed | 2024 share |
|---------|---|---|----|----|---|---------|------------|
| BEV new vehicle sales share | 85% | 0.3492 | 2028.83 | 0.9621 | 15 | Yes | 11.96% |
| BEV fleet stock share | 80% | 0.4155 | 2031.77 | 0.9979 | 15 | Yes | 3.0% |
| Li-Ion telecom UPS share | 85% | 0.3659 | 2024.84 | 0.9620 | 15 | Yes | 33.0% |
| Li-Ion datacenter UPS share | 90% | 0.2569 | 2024.90 | 0.9797 | 15 | Yes | 37.0% |
| EV forklift share (all) | 70.66% | 0.1891 | 2009.61 | 0.9351 | 15 | No | 64.9% |

**Catalog data sources used:**
- BEV sales/fleet: `data/passenger_cars/adoption/Passenger_Vehicle_(BEV)_Annual_Sales_Global.json` (Rethinkx)
- Telecom UPS: `data/telecom_ups/adoption/Telecom_UPS_Battery_Demand_Annual_Capacity_Demand_Global.json` and `...(Lead_Acid)...Global.json`
- Datacenter: `data/datacenter_ups/adoption/Data_Center_Battery_Demand_(Li-Ion)_Annual_Capacity_Demand_Global.json` and total
- Forklift: `data/forklift/adoption/Forklift_(EV)_Annual_Sales_Global.json` and total

**10% lead demand decline crossing: 2028.1 [model-derived]**
Scenario range: 2027.4 (optimistic) to 2028.8 (conservative)

**Key discrepancy with tipping-synthesizer:** tipping-synthesizer used x0=2028 for non-SLI (analytically derived); catalog data shows non-SLI inflection at 2024-2025. This makes non-SLI contribution front-loaded and the 10% milestone more SLI-dependent, pushing it to 2028.1 vs. synthesizer's 2027.5.

**Telecom UPS data gap:** Step-change in 2022 (13% to 28% Li-ion share in one year). Likely 5G buildout driven, but introduces S-curve fitting irregularity. R²=0.962 acceptable but treat telecom projections with wider CIs.

**Why:** Multi-segment architecture needed because SLI (62.5% of lead demand) and non-SLI (37.5%) have fundamentally different inflection timings.

**How to apply:** For any follow-on lead demand analysis, use these exact L/k/x0 values as the primary S-curve inputs. BEV fleet share (Seg2) with x0=2031.77 is the gating curve for SLI demand timing.
