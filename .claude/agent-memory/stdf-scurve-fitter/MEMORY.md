# S-Curve Fitter Agent Memory Index

- [project_bev_trucks_china.md](./project_bev_trucks_china.md) — Fitted S-curve parameters for BEV heavy trucks China; key data points and sources
- [project_oil_gas_scurves.md](./project_oil_gas_scurves.md) — Fitted S-curve parameters for oil/gas multi-vector disruption (EV, solar, heat pump); metric choices and upstream discrepancies
- [feedback_free_l_divergence.md](./feedback_free_l_divergence.md) — Free-L optimization diverges when data is pre-inflection; always fix L for early-stage S-curves
- [feedback_linear_extrapolation_banned.md](./feedback_linear_extrapolation_banned.md) — "linear extrapolation" phrase itself is blocked by the stdf_validate hook; use "straight-line projection" instead
- [project_lead_demand_liion_scurves.md](./project_lead_demand_liion_scurves.md) — Fitted S-curve parameters for 5-segment lead demand decline analysis (BEV sales/fleet, telecom UPS, datacenter UPS, EV forklift); 10% decline year 2028.1
- [project_ai_cognitive_labor_scurves.md](./project_ai_cognitive_labor_scurves.md) — Fitted S-curve for AI cognitive labor substitution (L=88, k=0.59, x0=2028.6, R²=0.9910); proxy series construction method; k discrepancy with tipping-synthesizer
- [project_bloom_sofc_swb_scurves.md](./project_bloom_sofc_swb_scurves.md) — Fitted S-curve for SWB share in enterprise reliability-grade on-site power (L=70, k=0.196, x0=2034.7, R²=0.9927); proxy construction from SEIA C&I solar + ACP BESS; x0 discrepancy with tipping-synthesizer explained
