---
name: China BEV HDT Material Intensity Coefficients
description: Regional material intensity values for China BEV heavy trucks — uniform across regions due to LFP platform standardization
type: reference
---

For China BEV heavy trucks (49t GVW, LFP chemistry), material intensity is uniform across all five sub-national regions. No regional differentiation warranted.

**Lithium:** 280 kg LCE/unit (BEV); 0 kg LCE/unit (LNG/diesel incumbent)
- Basis: 350 kWh avg pack × 0.8 kg LCE/kWh (LFP cathode)
- Infrastructure add-on: ~0.00303 swap stations/BEV unit × 11,280 kg LCE/station

**Copper:** 100 kg Cu/unit (BEV); 27.5 kg Cu/unit (LNG/diesel incumbent)
- BEV:incumbent ratio = 3.6× — drives monotonic copper demand increase

**Source:** 07a-demand-decomposer.md, 07b-stream-forecaster.md, bev-trucks-china pipeline run, 2026-03-20

**Cross-national note (from supplementary context):**
- USA Class 8 BEV trucks would need higher MI (larger packs, >400 kWh average)
- Europe BEV heavy trucks: intermediate (350–380 kWh range)
- These are placeholders; a dedicated cross-national run would calibrate them.
