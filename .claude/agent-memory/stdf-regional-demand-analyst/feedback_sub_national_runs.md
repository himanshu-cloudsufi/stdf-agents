---
name: Sub-national runs depart from standard cross-national breakdown
description: When pipeline is China-domestic, provide 5 sub-national regions instead of China/USA/Europe/RoW; include international as supplementary only
type: feedback
---

The bev-trucks-china pipeline run explicitly targets within-China geographic heterogeneity. The standard cross-national breakdown (China, USA, Europe, RoW) was replaced with five sub-national China regions (Eastern/YRD, Southern/PRD, Northern/BTH, Central, Western).

**Why:** 05b-regional-adopter already disaggregated into sub-national regions with independently fitted S-curves. Using cross-national breakdown would discard that upstream work and flatten meaningful geographic variation.

**How to apply:** When upstream 05b-regional-adopter produces sub-national regions instead of cross-national, follow the same sub-national structure in 07d. Include cross-national context table as supplementary (not primary) output to satisfy compliance criterion 6.9 in spirit while serving the actual analysis goal.
