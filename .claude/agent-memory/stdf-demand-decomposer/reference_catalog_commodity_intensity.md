---
name: Data catalog — commodity intensity coverage for demand decomposer
description: Which catalog files are useful for commodity intensity; what gaps exist for HDT/commercial vehicle analysis
type: reference
---

# Catalog Coverage — Commodity Intensity for Demand Decomposer

## AVAILABLE (useful for calibration/cross-check)

### Lithium intensity per EV
- `data/battery_pack/commodity_intensity/Commercial_Vehicle_(EV)_Average_Lithium_content_Global.json`
  - 18.5 kg Li metal/battery (2024–2025) for broad commercial EV mix (NMC-weighted, ~100 kWh average)
  - Scale to HDT: 18.5 × (350/100) = 64.8 kg — higher than LFP-specific because catalog mix includes NMC
- `data/battery_pack/commodity_intensity/Passenger_Vehicle_(EV)_Average_Lithium_content_Global.json`
  - 12.0 kg Li metal/battery (2024–2025)
- `data/battery_pack/commodity_intensity/Two_Wheeler_(EV)_commodity_intensity_Average_Lithium_content_Global.json`
- `data/battery_pack/commodity_intensity/Three_Wheeler_(EV)_commodity_intensity_Average_Lithium_content_Global.json`

### Copper demand (China, sector-level)
- `data/copper/adoption/Copper_Annual_Consumption_China.json` — total China: 15,251 kt (2024)
- `data/copper/adoption/Copper_Demand_Transportation_Percentage_China.json` — transport 20% (2024)
- `data/copper/adoption/Copper_EV_Demand_Percentage_China.json` — EV 9% (2024) = 1,373 kt (all EV + infra)
- `data/copper/adoption/Copper_Electrical_Demand_Percentage_China.json`
- `data/copper/adoption/Copper_Solar_Demand_Percentage_China.json`
- `data/copper/adoption/Copper_Wind_Turbines_Percentage_China.json`

## NOT AVAILABLE (gaps requiring T3 web sources or stoichiometric derivation)

1. **No copper intensity curve per vehicle class** — no per-unit kg Cu for BEV vs. ICE trucks
2. **No iron phosphate (FePO4) intensity curve** — must derive stoichiometrically from LiFePO4
3. **No LNG consumption per truck/year** — must use T3 ICCT sources or user spec
4. **No HDT-specific lithium intensity** — catalog has broad commercial EV mix, not HDT-specific

## Key Derivation: LCE → Fe stoichiometry
LiFePO4 molar ratio Li:Fe:P:O4 = 1:1:1:4
MW: Li=6.941, Fe=55.845, P=30.974, O4=64.0 → MW(LiFePO4)=157.76
LCE factor: Li2CO3/(2×Li) = 73.89/(2×6.941) = 5.323 kg LCE per kg Li metal
If LCE/truck = 280 kg → Li metal = 52.6 kg → mol = 7,578 → Fe = 423.2 kg → FePO4 = 1,143 kg
