---
name: Lead Demand Fleet Parameters
description: Lead (Pb) fleet model parameters for the lead-demand-decline pipeline run: ICE vehicles, forklifts, telecom VRLA, 2-wheelers; OEM/replacement ratios and key structural insights
type: project
---

Lead demand pipeline slug: `lead-demand-decline`. Four fleet models built.

**Fleet 1: ICE Passenger Vehicles**
- 2024 fleet: 1.266B (back-calc from PC replacement SLI demand 3,377 kt at 12 kg/unit, 4.5yr battery lifetime)
- Total vehicle sales: 72M/yr (back-calc from 810 kt new SLI, 13 kg/unit, 86.7% ICE share in 2024)
- Vehicle lifetime: 15yr, scrappage rate: 1/15 = 6.67%
- SLI battery lifetime: 4.5yr (drives aftermarket replacement demand)
- OEM intensity: 13 kg Pb/vehicle; Replacement intensity: 12 kg Pb/battery
- OEM split: PC new-vehicle SLI = 100% OEM; PC aftermarket SLI = 100% replacement
- BEV fleet 2024: 134M (= 1.4B total - 1.266B ICE)

**Fleet 2: Lead-Acid Forklifts**
- 2024 fleet: 5.40M units (back-calc from 913 kt at 1,014 kg/unit, 6yr lifetime)
- Battery lifetime: 6yr, scrappage rate: 1/6 = 16.7%
- OEM = 0 (near-saturated EV disruption ceiling 70.66%; lead-acid share is retention market)
- Replacement = 100%
- Demand erodes only ~−1.5%/yr through 2046; very resilient

**Fleet 3: VRLA Telecom Sites**
- 2024 fleet: 9.99M effective VRLA sites (back-calc from 907 kt at 363 kg/site, 4yr lifetime)
- Battery lifetime: 4yr, scrappage rate: 0.25
- OEM = 0 post-tipping (x0=2024.84 LFP stock share S-curve; past inflection in 2024)
- Replacement = 100%; but the stream-forecaster models demand directly via S-curve-on-stock
- Physical fleet model produces higher demand than SF; use SF values as authoritative
- SF models LFP as penetrating the INSTALLED STOCK, not just new installs

**Fleet 4: Lead-Acid 2-Wheeler Batteries**
- 2024 fleet: 294M units (back-calc from 1,395 kt at 8.3 kg/unit, 1.75yr lifetime)
- Battery lifetime: 1.75yr (1.5–2yr range), scrappage rate: 0.571
- OEM = 5%, Replacement = 95%
- Most stable driver; 25% Li-ion ceiling means 78% lead-acid share persists to 2046

**OEM vs Replacement Splits by Driver:**
| Driver | OEM % | Replacement % | Rationale |
|--------|-------:|---------------:|-----------|
| PC new SLI | 100% | 0% | New vehicle purchase = OEM event |
| PC aftermarket SLI | 0% | 100% | Mid-life battery swap = pure replacement |
| CV total | 20% | 80% | 10yr vehicle / 4yr battery ratio |
| 2W/3W | 5% | 95% | Near-stable fleet, high battery turnover |
| Telecom VRLA | 0% | 100% | Post-tipping, no new VRLA site installs |
| Datacenter VRLA | 0% | 100% | Same as telecom |
| Forklift | 0% | 100% | Saturated EV disruption, retention segment |

**Key Lead-Specific Structural Insight:**
Battery lifetime (4.5yr SLI) << vehicle lifetime (15yr) creates a multi-year lag between BEV new-sales disruption and replacement demand compression. OEM demand collapses ~49% by 2031 (tracks new-sales S-curve). Replacement demand collapses only ~29% by 2031 (tracks fleet S-curve, x0=2031.77 vs 2028.83 for new sales). The sharpest replacement cliff is 2031–2036: −51% in 5 years as the 2024–2030 BEV cohort eliminates their would-be battery replacement cycles.

**10% demand decline crossing:** 2027 (median path). Fleet model confirms: ICE fleet still 1.195B in 2027, generating 661 kt OEM + 3,186 kt replacement = 3,847 kt from PC alone.

**Non-fleet structural floor:** 2,268 kt in 2024 (other industrial + non-battery). Grows as a share from 18.5% to 34.9% by 2046 as fleet-sensitive demand falls.

**Why:** Pipeline run for `lead-demand-decline` slug. User asked "When will lead demand drop 10%?" — threshold crossed 2027. Fleet model confirms mechanics via OEM/replacement decomposition.

**How to apply:** When running lead demand analysis in future sessions, re-use these anchored fleet parameters. The PC fleet back-calculation from observed replacement demand (3,377 kt ÷ 12 kg × 4.5yr = 1.266B) is the reliable anchor; do not use population-based estimates.
