---
name: ev-ice-passenger-usa-cost-fit
description: Validated exponential fit parameters, learning rates, and threshold years for BEV vs. ICE passenger car disruption in the US consumer market (2026-03-24)
type: reference
---

## Analysis Context

BEV vs ICE passenger car, US consumer mass market. Analysis date 2026-03-24.
Primary parity metric: $/vehicle (purchase price).

---

## Battery Pack Fit (Upstream Cost Driver)

- Formula: C(t) = 1,240.70 × exp(−0.1841 × (t − 2010)) $/kWh_capacity
- R² = 0.954, 15 pts, 14-yr span (2010–2024) — all points including 2022 spike
- Secondary (excl. 2022): C(t) = 1,257.75 × exp(−0.1883 × (t − 2010)), R²=0.956
- Learning rate: **16.81%/yr** (NORMAL — within 12–28% expected range for batteries)
- Per-doubling learning rate: 8.47%
- 2024 validation: model=$94 vs actual=$115 (18% deviation — slightly above 15% threshold due to post-lithium-spike lag)
- **Cross-analysis check:** consistent with prior runs: Li-ion/lead-acid (r=0.1841), oil/gas BEV vector (r=0.1797, 16.45%/yr)

## EV Purchase Price USA Entry-Level Fit

- Formula: C(t) = 53,589.48 × exp(−0.0398 × (t − 2010)) $/vehicle
- R² = 0.989, 8 pts, 14-yr span (2010–2024) — HIGH confidence fit
- Learning rate: **3.90%/yr** — flagged IMPLAUSIBLE (below 5.0% floor for ev_vehicle class)
- REASON for implausibility: market-structure artifact — OEM margin recovery, feature-loading, and $7,500 federal tax credit absorb battery cost savings, suppressing observed price decline below underlying cost-curve rate
- Validation: all checkpoints within 3.1% — fit is geometrically accurate despite IMPLAUSIBLE flag

## EV Purchase Price China Fit

- Formula: C(t) = 39,052.04 × exp(−0.0657 × (t − 2010)) $/vehicle
- R² = 0.993, 6 pts, 14-yr span (2010–2024)
- Learning rate: **6.36%/yr** (NORMAL)

## ICE Incumbent Trends (USA)

- ICE mid-size sedan: linear_rising, +$500/yr, R²=1.000, anchor $29,000 (2024)
- ICE mid-size SUV: linear_rising, +$921/yr, R²=0.968, anchor $39,520 (2024)
- NADA all-segment ATP: linear_rising, +$2,139/yr, R²=0.958, anchor $47,652 (2024)
- Structural drivers: regulatory burden (CAFE/NHTSA), loss of scale economies as BEV share grows, feature-loading as competitive defense, commodity exposure

## Thresholds (EV Entry-Level vs ICE Sedan)

- **Competitive threshold (parity):** 2025–2026 (central: 2025.0 at $29,499/vehicle)
  - Sensitivity: r=0.035 → 2026.4; r=0.0398 → 2025.0; r=0.045 → 2023.8
- **70% inflection threshold:** 2031–2032 (EV=$22,866 vs ICE sedan=$32,700)
- **50% inflection threshold:** 2037–2038 (EV=$17,866 vs ICE sedan=$35,800)

## China Thresholds (EV China vs ICE China ~$15,500)

- Competitive threshold: 2024–2025 (already crossing)
- Inflection threshold (70%): 2029–2035

## Battery Pack Component Translation (72 kWh pack)

- 2024: $94/kWh model → $6,787 pack cost (23% of $29K ICE)
- 2027: $54/kWh model → $3,907 pack cost (13% of $29K ICE)
- 2030: $31/kWh model → $2,249 pack cost (8% of $29K ICE)
- Battery pack is no longer the primary cost parity barrier by 2027; non-battery manufacturing and distribution costs dominate

## Key Analytical Caveats

- $7,500 IRA tax credit NOT embedded in parity analysis — including it advances parity ~1-2 years
- Catalog EV series is entry-level only — market-mix EV ATP ($55,544, 2024) is still 17% ABOVE ICE market-mix ATP ($47,652)
- Full market-mix parity requires portfolio expansion into lower price bands, not just battery cost decline
- Energy cost advantage: BEV $0.053/mile vs ICE $0.107/mile (BEV 50% cheaper on energy in 2024–2025)

## Confidence

- Battery pack fit: 0.95 (high — consistent with all prior Li-ion fits in STDF memory)
- EV purchase price parity: 0.85 (entry-level parity well-established; market-mix parity requires additional modeling)
