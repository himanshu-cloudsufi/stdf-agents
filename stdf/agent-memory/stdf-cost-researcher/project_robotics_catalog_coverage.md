---
name: project_robotics_catalog_coverage
description: What robotics data exists in the local data/ catalog vs. must be filled with web research
type: project
---

## Robotics Catalog Coverage (data/ directory)

**Why:** Knowing this upfront saves search time in future humanoid/robot pipeline runs.

### What IS in the catalog (data/robot/)
- Industrial robot price per installed unit (Automotive, Chemical, Electronics, Food, Metal) — Global, 2016–2024, Statista (T2)
- Industrial robot annual installation volumes by region and industry — Global, China, Europe, USA, 2010s–2024
- Service robot professional annual installation volumes — Global, various sub-sectors
- Humanoid_Robot_Market_Size_Global.json — market size in USD Billion 2021–2025, source: MarketandMarkets (NOT T1; market research firm)

### What is NOT in the catalog
- Humanoid robot unit cost time series — does not exist; must web-search
- Human labor total compensation time series — not in catalog; use FRED/BLS (T1)
- Robot maintenance / operating cost series — does not exist anywhere as a time series

### Compute chipsets relevant to robots (data/compute_chipsets/)
- NVIDIA Jetson Orin Nano for robots/drones — USA + China, 2021–2025
- NVIDIA Jetson Xavier NX for robots/drones — USA + China, 2018–2025
- Ambarella CVflow for robots/drones — USA + China, 2018–2025
- Horizon Robotics Journey Series for automotive L4/L5 — USA + China, 2018–2025
- Source: "Database" (not attributed to specific publisher — treat as T2)

**How to apply:** For any robot disruption analysis, start with data/robot/cost/ for industrial arm incumbent data, then immediately go to web research for humanoid disruptor unit costs.
