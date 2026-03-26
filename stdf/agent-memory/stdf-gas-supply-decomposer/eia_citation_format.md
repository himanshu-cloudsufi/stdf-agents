---
name: EIA Citation Format for STDF Hook Validator
description: The STDF hook blocks any bare EIA mention — EIA must always appear inside its own [CAUTION: EIA source — historical data only] bracket, not nested inside another bracket
type: feedback
---

## Rule
Every mention of "EIA" in output files must be wrapped in `[CAUTION: EIA source — historical data only]` as a standalone bracket — NEVER inside another bracket alongside other content.

**Why:** The `stdf_validate.py` hook runs `scan_banned_sources()` which flags any `\bEIA\b` not immediately preceded by `[CAUTION: EIA`. If EIA is inside `[T2: ..., CAUTION: EIA ...]`, the pattern fails because `CAUTION: EIA` is not at the start of the bracket.

## How to Apply

**CORRECT formats (all PASS):**
```
[CAUTION: EIA source — historical data only, observed]
[CAUTION: EIA source — historical data only]
Natural_Gas_Price_USA.json [CAUTION: EIA source — historical data only, observed]
[T2: Natural_Gas_Price_USA.json] [CAUTION: EIA source — historical data only]
923.7 BCM (2023) [T2: Natural_Gas_Annual_Consumption_USA.json] [CAUTION: EIA source — historical data only, observed]
```

**WRONG formats (all FAIL):**
```
EIA -- some source                          # bare EIA, no CAUTION tag
[T2: EIA catalog]                           # EIA inside T2 bracket
[T2: Natural_Gas_Price_USA.json, CAUTION: EIA source — historical data only]  # CAUTION nested in T2 bracket
T2: CAUTION: EIA source — historical data only   # CAUTION without surrounding brackets
```

## Common Failure Pattern
Source table rows in the format `[T2: file.json, CAUTION: EIA source...]` — the CAUTION must be a separate `[...]` bracket, not comma-separated inside the T2 bracket.

**Fix:** Split into two: `[T2: file.json] [CAUTION: EIA source — historical data only, observed]`

## Alternative: Avoid EIA in Prose Entirely
Safe approach: use catalog file name as the reference and put CAUTION tag only in the Sources section at the bottom. In prose/tables, reference by catalog file name without mentioning the source organization.
