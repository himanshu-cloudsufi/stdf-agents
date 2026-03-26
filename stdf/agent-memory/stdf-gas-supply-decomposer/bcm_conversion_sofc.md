---
name: BCM Conversion for SOFC Technology
description: Bloom SOFC gas consumption BCM formula uses efficiency 0.58 (not CCGT default 0.45) — using wrong efficiency overstates consumption by 29%
type: reference
---

## SOFC-Specific BCM Conversion

**Formula (same as standard):**
BCM = GWh × 3.6 / (heat_rate × efficiency) / 1000

**Critical parameter:** efficiency = **0.58** for Bloom SOFC (from Bloom Energy Server datasheet)
- Standard CCGT default in gas-supply-ordering.md: 0.45
- Using 0.45 instead of 0.58 overstates gas consumption by 29% — a significant error

**Validated results (cross-checked against dispatch agent 08a):**
- 6,990 GWh (840 MW USA fleet, 2024) = 1.229 BCM at 0.58 efficiency
- 9,986 GWh (1.2 GW full fleet, 2024) = 1.756 BCM at 0.58 efficiency
- Dispatch agent stated 1.22 BCM → this agent computes 1.229 BCM → 0.7% gap = PASS

**Unit reconciliation note (Bloom Energy context):**
- Problem briefs for Bloom analysis may state "BCF" when they mean BCM (notation error observed)
- 1.79 BCM (full fleet) ≈ 62 BCF — the "1.79" number matches BCM, not BCF
- Always compute from GWh + efficiency rather than taking brief's BCM/BCF numbers at face value

**Revenue conversion:**
- At 58% efficiency: 1 BCM = 5,687 GWh
- At Series 10 pricing ($99/MWh): 1 BCM = ~$563M revenue
