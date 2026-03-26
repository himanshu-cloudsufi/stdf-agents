---
name: Lead (Pb) demand decomposition — market products, intensity coefficients, coverage
description: Lead demand decomposition for lead-demand-decline slug: 10 market products, catalog-derived MI coefficients, 99.98% coverage, structural floor at 13.8%
type: project
---

# Lead (Pb) Demand Decomposition — lead-demand-decline Pipeline Run

**Total demand (2024):** 12,259 kt [T2: data/lead/adoption/Lead_Annual_Implied_Demand_Global.json, Rethinkx, observed]
**10% decline threshold:** 11,033 kt (−1,226 kt)
**Coverage achieved:** 99.98% (10 market products, 12,256 kt modeled)

**Why:** User asked "when will lead demand drop 10%?" — decomposition is the foundation for the stream-forecaster and fleet-modeler to project per-driver demand trajectories.

**How to apply:** Any future lead demand analysis should start from this tree structure. Intensity coefficients are catalog-derived and can be re-used.

---

## Level 1 Sector Breakdown

| Sector | 2024 kt | Share |
|--------|---------|-------|
| Automotive SLI (all vehicles) | 7,665 | 62.5% |
| Industrial Stationary | 1,987 | 16.2% |
| Industrial Motive Power | 913 | 7.4% |
| Non-Battery Uses | 1,691 | 13.8% |

Disruption-eligible battery demand: 10,565 kt = 86.2%
Non-disruption structural floor: 1,691 kt = 13.8%

---

## Catalog-Derived Material Intensity Coefficients (kg Pb / unit)

All derived using identity: MI = demand_kt × 10^6 / unit_sales

| Market Product | Tech Variant | MI (kg Pb/unit) | Derivation |
|----------------|-------------|-----------------|------------|
| Passenger car — new vehicle | ICE SLI | 13.0 | 810 kt / 62.24M ICE new cars (2024) |
| Passenger car — aftermarket replacement | ICE SLI | 12.0 | 3,377 kt / 281.3M replace events (1,265.8M fleet, 4.5yr) |
| Passenger car — new vehicle | BEV | 0.0 | BEV = zero SLI lead (DC-DC converter from traction pack) |
| Passenger car — new vehicle | PHEV (chimera) | 12.0 | Retains 12V SLI; same as ICE replacement |
| Commercial vehicle — new + replacement | ICE SLI | 17.9 | 319 kt / 17.83M CV sales (2024); replacement consistent |
| 2-wheeler — new + replacement | Lead-acid SLI | 8.3 | 527 kt / 63.82M 2W sales; 868 kt / 105.1M replace events |
| 3-wheeler — new + replacement | Lead-acid SLI | 7.8 / 6.6 | 155 kt / ~20M 3W sales (new); 393 kt / 59.6M events (replace) |
| Telecom tower — VRLA installation | VRLA lead-acid | 363 | 907 kt / 2.5M annual site replacements (10M sites, 4yr) |
| Telecom tower — new installation | LFP-UPS | 0.0 | LFP = zero lead |
| Datacenter — UPS installation | VRLA lead-acid | 2,010 | 503 kt / 250k replacements (1M installs, 4yr) |
| Datacenter — UPS installation | LFP-UPS | 0.0 | LFP = zero lead |
| Industrial forklift — traction | Lead-acid traction | 1,014 | 913 kt / ~900k annual replacements (4.5M fleet, 5yr) |
| Industrial forklift — traction | LFP motive | 0.0 | LFP = zero lead |

---

## Disruption-Addressable Demand by Vector

| Disruption | Market Product | Peak Addressable (kt) | Disruptor Pb Content |
|------------|---------------|----------------------|---------------------|
| BEV new-car sales | Passenger car new-vehicle SLI | 810 | 0 kg |
| BEV fleet turnover | Passenger car aftermarket SLI | 3,377 | 0 kg |
| LFP-UPS telecom | Telecom VRLA | 907 | 0 kg |
| LFP-UPS datacenter | Datacenter VRLA UPS | 503 | 0 kg |
| EV-FL + LFP motive | Forklift traction | 913 | 0 kg |
| No disruptor | All other (2W/3W SLI, CV SLI, other stationary, non-battery) | 4,749 | N/A |

Total disruption-addressable: 6,510 kt (53.1% of total)

---

## Key Catalog Files for Lead Demand Decomposition

- `data/lead/adoption/Lead_Annual_Implied_Demand_Global.json` — total
- `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Sales_Cars_Global.json` — car new
- `data/passenger_cars/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_Cars_Global.json` — car replacement
- `data/commercial_vehicle/adoption/Lead_Annual_Implied_Demand-Sales_Commercial_vehicles_Global.json`
- `data/commercial_vehicle/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_Commercial_Global.json`
- `data/two_wheeler/adoption/Lead_Annual_Implied_Demand-Sales_2_wheelers_Global.json`
- `data/two_wheeler/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_2_wheelers_Global.json`
- `data/three_wheeler/adoption/Lead_Annual_Implied_Demand-Sales_3_wheelers_Global.json`
- `data/three_wheeler/adoption/Lead_Annual_Implied_Demand-Vehicle_replacement_3_wheelers_Global.json`
- `data/lead/adoption/Lead_Annual_Implied_Demand-Industrial_batteries_stationary_Global.json`
- `data/lead/adoption/Lead_Annual_Implied_Demand-Industrial_batteries_motive_power_Global.json`
- `data/lead/adoption/Lead_Annual_Implied_Demand-Non-battery_uses_Global.json`

---

## Key Estimates (Not in Catalog, Must Justify)

- ICE car fleet: 1,265.8M (1,305M total − 39.15M BEV at 3% fleet share, 2024)
- ICE 2W fleet: ~262M (implied from replacement demand / MI / cycle)
- Global CV fleet: ~340M (implied from replacement demand / MI / cycle)
- Global telecom sites: ~10M (reference-class estimate)
- Forklift lead-acid installed base: ~4.5M units
- 3W global sales: ~20M/yr (T3 estimate — no T2 catalog)
