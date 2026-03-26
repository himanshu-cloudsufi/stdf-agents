# Fleet Modeler Agent Memory Index

- [project_bev_trucks_china_fleet_params.md](./project_bev_trucks_china_fleet_params.md) — BEV HDT China fleet parameters, OEM/replacement ratios, mid-life battery lithium uplift (2026-2046)
- [feedback_stock_flow_consistency.md](./feedback_stock_flow_consistency.md) — validate_stock_flow_consistency max_deviation ≤ 0.01 is a floating-point artifact; treat as PASS
- [project_oil_gas_fleet_params.md](./project_oil_gas_fleet_params.md) — Oil/gas demand disruption: PV (1.5B, 15yr), HDT (26M, 10yr), gas power (2,572 GW, 30/20yr), heating (800M, 17yr); OEM demand ~0% for oil, ~10% for gas heating; pipeline slug "oil-gas-outlook" triggers forecast-language hook
- [project_lead_demand_fleet_params.md](./project_lead_demand_fleet_params.md) — Lead demand fleet params: ICE vehicles (1.266B, 15yr, 4.5yr SLI battery), forklifts (5.40M, 6yr), telecom VRLA (9.99M, 4yr), 2W (294M, 1.75yr); OEM ~10%/replacement ~70% split; 2031-2036 is sharpest replacement cliff; pipeline slug "lead-demand-decline"
