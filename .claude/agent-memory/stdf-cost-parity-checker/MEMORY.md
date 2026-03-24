# Cost Parity Checker — Memory Index

## Cost Parity Findings by Sector
- [cost_parity_bev_trucks_china.md](./cost_parity_bev_trucks_china.md) — BEV vs LNG heavy trucks China: TCO parity MET 2019-2020, 1.319 vs 1.806 CNY/km in 2024
- [cost_parity_oil_gas_multi_vector.md](./cost_parity_oil_gas_multi_vector.md) — Oil/gas demand 3-vector: V1 EV/ICE MET 2020-2021 (0.65), V2 Solar+BESS/NGCC MET 2023-2024 (0.82), V3 HP/gas NOT_MET (0.60); aggregate 0.69
- [cost_parity_liion_leadacid.md](./cost_parity_liion_leadacid.md) — Li-ion vs. lead-acid (lead demand): service-level MET pre-2010, nameplate MET 2019-2021; SLI IMMINENT USA (2027-2028) / NOT_MET China (2031-2032); SLI is binding constraint at 62.5% of demand
- [cost_parity_bev_ice_passenger_usa.md](./cost_parity_bev_ice_passenger_usa.md) — BEV entry-level vs ICE sedan USA: purchase price parity MET 2025-2026, ~$29,500/vehicle, R-squared=0.9886, confidence 0.85; battery learning rate 16.81%/yr underlying

## Analytical Patterns
- [patterns_confidence_scoring.md](./patterns_confidence_scoring.md) — How to derive confidence score from cost-fitter R-squared; observed MET cases get +0.05–0.10 boost
- [patterns_dual_threshold.md](./patterns_dual_threshold.md) — TCO parity vs. purchase-price parity: TCO is primary for criterion 5.3, purchase price is secondary evidence
- [patterns_multi_vector_evaluation.md](./patterns_multi_vector_evaluation.md) — Multi-vector disruptions: evaluate each vector independently, report per-vector status table, aggregate confidence is mean; vocabulary note on 'outlook' in path slugs
