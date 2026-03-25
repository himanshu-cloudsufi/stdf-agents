---
name: Transportation Sector — BEV disruption of ICE vehicles (March 2026, updated)
description: Key data anchors and findings from the EV vs ICE disruption analysis for reuse in future analyses — updated with TIPPING_ONLY run data
type: project
---

Analysis completed: March 2026 (updated March 2026 for TIPPING_ONLY preset). Sector: Transportation. Sub-domains: mass-market BEV passenger cars, luxury/performance BEV, PHEV chimera, FCEV chimera, BEV commercial vehicles, two- and three-wheeler BEV, autonomous robotaxi / TaaS, BEV charging infrastructure, vehicle-to-grid (V2G) grid services.

Output written to:
- `output/electric-vehicles/agents/01-domain-disruption.md` (original run)
- `output/give-me-tipping-point-of-evs-20260321-083514/agents/01-domain-disruption.md` (TIPPING_ONLY run, March 2026)
- `output/ev-tipping-point/agents/01-domain-disruption.md` (TIPPING_ONLY run #2, March 2026)
- `output/give-me-tipping-point-of-evs-20260322-185253/agents/01-domain-disruption.md` (TIPPING_ONLY run #3, March 2026)
- `output/give-me-tipping-point-of-ev-vehicles-20260323-200327/agents/01-domain-disruption.md` (TIPPING_ONLY run #4, 2026-03-24)


**Key cost data anchors (from local catalog + web research, March 2026):**
- Li-ion battery pack median global: $1,436/kWh (2010) → $115/kWh (2024); 92% decline (Rethinkx)
- Passenger BEV battery pack: $179/kWh (2019) → $97/kWh (2024) (Rethinkx)
- LFP cell-level (BYD, China): ~$60–65/kWh (2025)
- BEV median purchase price (China): $16,200 (2024) vs ICE median sedan $19,000 — parity achieved
- BEV median purchase price (USA): $31,000 (2024) vs ICE median sedan $29,000 — near parity, not yet crossed
- Lowest-cost BEV (China, <200 mile range): $7,800 (2025); $38,600 (2013) — 80% decline
- ICE personal vehicle cost/mile (10k mi/yr): $1.10–1.35/mile (2022–2025, AAA)
- Waymo autonomous rideshare: $1.66–2.50/mile (2025 consumer price); projected $0.25/mile by 2035
- LiDAR (low-cost ADAS, China): $2,000 (2018) → $200 (2025); 90% decline
- V2G market: $5.75B (2025) → $19.5B (2030) projected

**Key adoption data anchors:**
- Global BEV annual sales: 5,000 (2010) → 11,000,000 (2024) (Rethinkx)
- Global BEV fleet: 39 million (2024) out of ~1.5B total fleet (~2.6% fleet share)
- China BEV sales: 6.4M of 11M global BEV sales in 2024 (58% of global)
- China NEV share: ~50% of new sales 2025 (BEV ~35%, PHEV ~15%)
- Europe BEV sales: 2.2M (2024)
- USA BEV sales: 1.2M (2024), ~7–8% share
- Global public charging points: 184,000 (2015) → 5.44M (2024); 30x in 9 years
- China public charging points: 3.58M (2024); 66% of global infrastructure
- BYD: 2.26M BEVs (2025), global BEV leader, overtook Tesla
- Tesla: 1.64M deliveries (2025, -1.2% YoY)
- ICE global sales: down 30% from 2017 peak; June 2025 monthly ICE units down 9% YoY
- Waymo fleet: 2,500 robotaxis (Nov 2025), 450,000+ weekly rides

**Key convergence labels:**
- A-EV: Autonomous driving + BEV → enables TaaS at sub-$0.50/mile at scale
- TaaS: A-EV + ride-hailing platforms + fleet management software → personal vehicle ownership disruption
- V2G-EV: BEV bidirectional charging + VPP aggregation software → distributed grid storage
- SDV-EV: Software-defined vehicle + BEV platform → subscription/OTA revenue model, Tier 1 supplier displacement
- SWB-EV: Solar PV + Wind + Battery storage + BEV charging → integrated stellar energy mobility system

**Chimeras confirmed:**
- PHEV: retains ICE drivetrain + fossil fuel dependency; growing in China (~15–19% NEV share) but structurally cannot reach BEV cost floor
- FCEV (light vehicle): ~23,000 units globally (2024); refueling infrastructure gap (~1,160 HRS vs 5.4M EV chargers)
- Incumbent OEM EV divisions (VW ID/MEB, GM Ultium, Ford Mustang Mach-E): ~20% higher manufacturing cost than BYD equivalent; grafted onto legacy ECU architectures
- ADAS Level 2+ systems: retains human driver requirement; chimera of AV disruption

**S-curve position:**
- Global BEV new car share: ~14–16% (2025); early-to-mid growth phase globally
- China: approaching inflection (~35% BEV, 50% NEV)
- Norway: post-inflection (>60% BEV)
- USA: early growth (~7–8%), policy headwinds
- Autonomous driving (L4 robotaxi): embryonic/early commercial phase

**Why:** These data points are frequently needed by downstream agents (cost-curve, tipping-point, adoption). Saves re-research time.

**How to apply:** When a Transportation sector query arrives, check these anchors first before re-searching. Update if data is >6 months old or a new pipeline run produces updated figures.
