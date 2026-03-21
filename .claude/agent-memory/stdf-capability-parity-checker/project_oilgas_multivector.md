---
name: Oil/Gas Multi-Vector Capability Parity Results
description: Capability parity condition results for the 3-vector oil/gas disruption analysis (BEV/ICE, Solar+BESS/NatGas, ASHP/GasFurnace)
type: project
---

## Results (evaluated 2026-03-20)

- **V1 BEV vs ICE:** PARTIAL — 7/9 MET, sequential convergence, model-derived full parity 2027
- **V2 Solar+BESS vs Natural Gas:** PARTIAL — 9/10 scoreable MET, sequential convergence, model-derived full parity 2027–2028
- **V3 ASHP vs Gas Furnace:** NOT_MET (ducted gross path) | PARTIAL (ductless/subsidized path) — 8/10 MET, divergent convergence, gross parity model-derived 2036–2043

**Why:** Oil/gas demand disruption analysis for the STDF pipeline. Multi-vector structure means each vector has independent parity status feeding the tipping synthesizer (04d).

**How to apply:** When the tipping synthesizer reads this file, V1 and V2 both contribute PARTIAL capability parity signals (close to full), while V3 is the lagging vector. The heating disruption is gated by capital access, not performance. The transport and power generation disruptions are within 1–3 years of full capability parity.

## Key per-vector notes

**V1 TCO nuance:** Fleet-average TCO (20.2% gap) overstates the blocker. Sedan/SUV segments already at TCO parity; truck segment drags the average. Do not treat fleet-average TCO as a uniform barrier.

**V2 capacity factor exclusion:** Standalone solar CF (16.3%) is NOT a valid parity dimension for a firmed solar+BESS system. Upstream capability agent explicitly excluded it. Only the dispatchability_index (12.5% gap, APPROACHING) is the live dimension to watch.

**V3 upfront cost range:** lib computes 2043; upstream estimates 2036 with more data. Report range 2036–2043. With subsidy, net cost ratio is ~2.0x (crosses <1.5x threshold near-term in subsidy-eligible markets). Ductless mini-split has NO capital cost barrier — already MET since 2022.

**V3 install complexity — no trajectory:** Ducted retrofit install complexity (3.5/5) has no multi-year trajectory. It is a contractor supply chain / labor constraint. Do not attempt to model-derive a parity year for this dimension in future iterations without new data.

## Vocabulary warning for future runs

The word "outlook" appears in the pipeline run directory name (`oil-gas-outlook`). The stdf_validate.py hook flags this as forecast language when it appears in agent output files. Avoid writing the full directory path in Sources sections — use `agents/03-capability.md` notation instead of the full path.
