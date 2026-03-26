# Spec: STDF Curves Data Layer Restructure

**Status:** Draft
**Date:** 2026-03-13
**Scope:** Replace monolithic `curves_catalog.json` + bash/jq lookup with a per-curve file structure, metadata index, and python3 query script. Update all agent definitions and CLAUDE.md.

---

## Problem

The current data layer has three bottlenecks:

1. **Every query parses 1MB of JSON** — the bash `lookup_curves` script shells out to `jq`, which reads and parses all 956 curves on every invocation (~0.5-1s per call).
2. **High subprocess overhead** — agents make 3-6 Bash calls each. Across 6 agents, that's ~30 subprocess invocations per pipeline run.
3. **External dependency** — `jq` must be installed. The python3 stdlib has everything needed.

## Design Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Primary access pattern | `Read` individual curve files via native tool | Zero subprocess overhead |
| Directory nesting | `data/<sector>/<type>/<name>.json` | Sector-first matches agent mental model; agents work on one sector |
| Sector slug format | Lowercase + underscores | `Passenger Cars` -> `passenger_cars`, matches Python conventions |
| X/Y data format | Parallel arrays (current) | Unchanged from catalog; easy to load into numpy/scipy |
| Index depth | Metadata only (no stats/trends) | ~50KB, agents Read curve files for values |
| Keyword search | Token-based scoring via python3 | Split query into tokens, rank by match count |
| Query output | Configurable `--detail` flag | Default: metadata + file paths. `--detail`: includes full X/Y data |
| Search fields | dataset_name + description only | Precise, avoids false positives |
| Sync strategy | Manual rebuild via `python3 scripts/build_data.py` | Simple, no magic |
| Validation | Dumb split (no validation) | Validation is a separate concern |
| Data quality fixes | Override mapping file (`data/overrides.json`) | Corrects misclassifications without touching source |
| Source file fate | Delete `curves_catalog.json` after migration | Individual files become source of truth |
| SQLite | Not used | Split files + index + python3 search is sufficient |
| Old lookup_curves | Remove entirely | Clean break; agents updated to new patterns |
| Agent definitions | Updated in this spec | Complete deliverable |
| CLAUDE.md | Updated in this spec | Documents new patterns |

---

## Architecture

### File Structure

```
data/
  index.json                                    # Metadata-only manifest (~50KB)
  overrides.json                                # Sector/field corrections for misclassified curves
  passenger_cars/
    cost/
      EV_Cost_Per_Km_USA.json
      EV_Cost_Per_Km_Europe.json
      ...
    adoption/
      EV_Sales_Annual_China.json
      EV_Fleet_Cumulative_USA.json
      ...
  battery_pack/
    cost/
      Battery_Pack_Cost_Per_KWh_World.json
      Battery_Pack_Cost_Per_KWh_China.json
      ...
  energy_generation/
    adoption/
      Solar_PV_Deployment_World.json
      ...
    cost/
      ...
  uav/
    adoption/
      ...
  ...                                           # ~26 sector dirs, ~21 type subdirs, 956 curve files total

scripts/
  build_data.py                                 # Splits curves_catalog.json -> data/ tree
  query_curves.py                               # Token-based keyword search over index.json
```

### Individual Curve File Format

Each file contains a single curve object with the same schema as the current catalog entries:

```json
{
  "dataset_name": "Battery_Pack_Cost_Per_KWh_World",
  "description": "Average lithium-ion battery pack cost globally.",
  "type": "cost",
  "units": "$/kWh",
  "source": "BNEF",
  "region": "World",
  "category": "cost",
  "entity_type": "Technology",
  "level_name": "Battery Pack",
  "X": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
  "Y": [684, 592, 384, 296, 214, 176, 156, 137, 132, 151, 139]
}
```

File name = `dataset_name` + `.json`. Dataset names are already unique identifiers.

### index.json Format

A flat array of metadata objects (no X/Y data):

```json
[
  {
    "dataset_name": "Battery_Pack_Cost_Per_KWh_World",
    "description": "Average lithium-ion battery pack cost globally.",
    "type": "cost",
    "units": "$/kWh",
    "source": "BNEF",
    "region": "World",
    "category": "cost",
    "entity_type": "Technology",
    "level_name": "Battery Pack",
    "file_path": "data/battery_pack/cost/Battery_Pack_Cost_Per_KWh_World.json"
  },
  ...
]
```

The `file_path` field is relative to the project root.

### overrides.json Format

A map from dataset_name to corrected field values. Applied during `build_data.py`:

```json
{
  "5G_Network_5G_Coverage_Land_Area_China": {
    "level_name": "5G Network"
  }
}
```

Only overridden fields are specified. All other fields are preserved from the source.

---

## Scripts

### build_data.py

**Purpose:** One-time (and repeatable) migration script. Reads `curves_catalog.json`, applies overrides, writes 956 individual JSON files + `index.json`.

**Behavior:**
1. Read `curves_catalog.json`
2. Read `data/overrides.json` (if exists) and apply field corrections
3. For each curve:
   - Derive sector slug: `level_name.lower().replace(' ', '_').replace('-', '_')`
   - Derive type slug: `type.lower().replace(' ', '_')`
   - Write to `data/<sector_slug>/<type_slug>/<dataset_name>.json`
4. Build `index.json` from all curves (metadata only, no X/Y, with `file_path`)
5. Write `data/index.json`
6. Print summary: `N curves written to M sector dirs`

**No validation.** If the source has bad data, it gets split as-is (unless overrides.json corrects it).

**Invocation:**
```bash
python3 scripts/build_data.py
```

**Dependencies:** python3 stdlib only (json, os, pathlib).

### query_curves.py

**Purpose:** Token-based keyword search over `data/index.json`. Replaces `lookup_curves` for keyword/discovery queries.

**Behavior:**
1. Load `data/index.json`
2. Parse search query into lowercase tokens
3. For each curve in index, compute a relevance score:
   - Concatenate `dataset_name` + `description` (replace underscores with spaces, lowercase)
   - Count how many query tokens appear as substrings (normalized: strip hyphens/underscores before matching)
   - Score = number of matching tokens
4. Filter to entries with score > 0, sort descending by score
5. Apply optional filters: `--type`, `--sector`, `--region`, `--units`
6. Output:
   - **Default:** Metadata + file_path for each match (markdown table)
   - **`--detail`:** Also reads each curve file and includes full X/Y data

**CLI interface:**
```bash
# Keyword search
python3 scripts/query_curves.py --search "lithium-ion battery" --type cost

# Filtered listing
python3 scripts/query_curves.py --type cost --sector "Battery Pack"

# With full data
python3 scripts/query_curves.py --search "solar" --type adoption --detail

# Discovery
python3 scripts/query_curves.py --list-sectors
python3 scripts/query_curves.py --list-types
python3 scripts/query_curves.py --list-regions

# Exact dataset lookup
python3 scripts/query_curves.py --dataset "Battery_Pack_Cost_Per_KWh_World" --detail
```

**Token matching normalization:** Before matching, both the query token and the target text are normalized by:
- Lowercasing
- Replacing hyphens and underscores with spaces
- Stripping extra whitespace

So `"lithium-ion"` in a query matches `"Lithium_Ion"` in a dataset name, and `"li-ion"` does NOT match `"lithium-ion"` (no fuzzy/abbreviation expansion).

**Dependencies:** python3 stdlib only (json, argparse, pathlib).

---

## Agent Access Patterns

### New primary workflow (replaces all lookup_curves calls)

**Step 1 — Discovery:** Agent reads `data/index.json` to find relevant curves.
```
Read data/index.json
```
Agent scans the metadata to identify dataset_names matching its needs (by type, sector, region).

**Step 2 — Targeted read:** Agent reads specific curve files.
```
Read data/battery_pack/cost/Battery_Pack_Cost_Per_KWh_World.json
```

**Step 3 — (Optional) Keyword search:** When the agent doesn't know exact dataset names, use the query script.
```bash
python3 scripts/query_curves.py --search "lithium-ion battery" --type cost
```

### Tool call comparison

| Scenario | Old (bash+jq) | New |
|---|---|---|
| "Get all cost curves for Battery Pack" | `Bash: lookup_curves -t cost -s "Battery Pack" --detail` (1 subprocess, 1MB parse) | `Read: data/index.json` + `Read: data/battery_pack/cost/*.json` (0 subprocesses, ~50KB + ~15KB) |
| "Search for lithium-ion battery" | `Bash: lookup_curves -q "lithium-ion battery" -t cost --detail` (1 subprocess, 1MB parse) | `Bash: python3 query_curves.py --search "lithium-ion battery" --type cost` (1 subprocess, ~50KB parse) |
| "List available sectors" | `Bash: lookup_curves --list-sectors` (1 subprocess, 1MB parse) | `Bash: python3 query_curves.py --list-sectors` (1 subprocess, ~50KB parse) OR `Read: data/index.json` and scan |
| "Get specific dataset by name" | `Bash: lookup_curves -d "Battery_Pack_Cost_Per_KWh_World" --detail` | `Read: data/battery_pack/cost/Battery_Pack_Cost_Per_KWh_World.json` (0 subprocesses) |

### Agent-specific data access patterns

| Agent | Primary pattern | Typical reads |
|---|---|---|
| **cost-curve** | Read index -> Read all `data/<sector>/cost/*.json` for target sector | 1 index + 5-30 curve files |
| **capability** | Read index -> Read `data/<sector>/capability/*.json`, `performance_benchmark/*.json`, `energy_density/*.json` etc. | 1 index + 5-15 curve files |
| **adoption-scurve** | Read index -> Read `data/<sector>/adoption/*.json` + `market_share/*.json` by region | 1 index + 10-30 curve files |
| **domain-disruption** | Read index -> Read across multiple types for target sector | 1 index + 10-40 curve files |
| **tipping-point** | Primarily reads upstream agent files. May validate with 1-2 targeted curve reads | 0-3 curve files |
| **synthesizer** | Reads upstream agent files only. May verify 1 specific curve if needed | 0-1 curve files |

---

## Agent Definition Updates

All 6 agent files in `.claude/agents/` must be updated. The changes are:

### Replace in all agents

**Remove** all references to:
- `curves_catalog.json`
- `./scripts/lookup_curves`
- `lookup_curves` CLI examples
- jq dependency

**Replace with** (adapted per agent):

```markdown
## Empirical Data Catalog

You have access to 956 curated empirical time series curves in the `data/` directory.

### Primary access: Read files directly

1. **Read the index** to find relevant curves:
   ```
   Read data/index.json
   ```
   The index contains metadata (dataset_name, type, units, region, sector, source) and file paths for all 956 curves. No X/Y data — just enough to identify what you need.

2. **Read specific curve files:**
   ```
   Read data/<sector>/<type>/<dataset_name>.json
   ```
   Each file contains one curve with full X/Y arrays.

3. **Browse a sector's curves:**
   ```
   Glob data/<sector>/<type>/*.json
   ```

### Fallback: Keyword search

When you don't know exact dataset names, use the search script:
```bash
python3 scripts/query_curves.py --search "lithium-ion battery" --type cost
python3 scripts/query_curves.py --search "solar deployment" --type adoption --detail
python3 scripts/query_curves.py --list-sectors
python3 scripts/query_curves.py --list-types
```

Default output shows metadata + file paths. Add `--detail` for full X/Y data.
```

### Per-agent example customization

Each agent's examples should reference the curve types/sectors they typically need:

- **cost-curve:** `Read data/battery_pack/cost/Battery_Pack_Cost_Per_KWh_World.json`
- **capability:** `Glob data/passenger_cars/capability/*.json`, `Glob data/*/energy_density/*.json`
- **adoption-scurve:** `Glob data/passenger_cars/adoption/*.json`, `python3 scripts/query_curves.py --type adoption --region China`
- **domain-disruption:** `Glob data/energy_generation/*/*.json` (all types for a sector)
- **tipping-point:** `Read data/<specific_curve>.json` (targeted validation only)
- **synthesizer:** Upstream files are primary. `Read data/<specific_curve>.json` only for spot-checking.

---

## CLAUDE.md Updates

### Empirical Data Catalog section

Replace the current section with:

```markdown
## Empirical Data Catalog

`data/` contains 956 curated empirical time series curves, organized as individual JSON files in a sector-first directory tree.

### Directory Structure

```
data/
  index.json                                    — Metadata-only manifest (no X/Y data)
  overrides.json                                — Corrections for misclassified curves
  <sector_slug>/
    <type_slug>/
      <dataset_name>.json                       — Single curve with full X/Y arrays
```

Sector slugs: `passenger_cars`, `battery_pack`, `energy_generation`, `uav`, `compute_chipsets`, etc.
Type slugs: `cost`, `adoption`, `capability`, `performance_benchmark`, `labor_impact`, `market_share`, etc.

### Agent Access Pattern

1. **Read `data/index.json`** — metadata manifest with file paths for all 956 curves
2. **Read individual curve files** — `data/<sector>/<type>/<name>.json`
3. **Glob for browsing** — `data/<sector>/<type>/*.json`
4. **Keyword search** — `python3 scripts/query_curves.py --search "query" --type cost`

### Query Script

```bash
python3 scripts/query_curves.py --search "lithium-ion battery" --type cost
python3 scripts/query_curves.py --type adoption --sector "Passenger Cars" --detail
python3 scripts/query_curves.py --list-sectors
python3 scripts/query_curves.py --list-types
python3 scripts/query_curves.py --dataset "Battery_Pack_Cost_Per_KWh_World" --detail
```

### Rebuilding After Catalog Changes

If individual curve files are edited/added, rebuild the index:
```bash
python3 scripts/build_data.py
```
```

### Directory Structure section

Update the tree diagram to reflect:
- `data/` replaces `curves_catalog.json`
- `scripts/query_curves.py` replaces `scripts/lookup_curves`
- `scripts/build_data.py` is new
- `scripts/lookup_curves` is removed

---

## Migration Plan

### Execution order

1. Create `data/overrides.json` with known misclassifications
2. Write `scripts/build_data.py`
3. Run `python3 scripts/build_data.py` to generate `data/` tree from `curves_catalog.json`
4. Write `scripts/query_curves.py`
5. Verify: spot-check 5-10 curve files match source catalog entries
6. Update all 6 `.claude/agents/*.md` files
7. Update `CLAUDE.md`
8. Delete `curves_catalog.json`
9. Delete `scripts/lookup_curves`

### Verification

After migration, confirm:
- `data/index.json` has 956 entries
- Each entry's `file_path` points to an existing file
- `python3 scripts/query_curves.py --search "battery" --type cost` returns results
- `python3 scripts/query_curves.py --list-sectors` output matches original `lookup_curves --list-sectors`
- A sample curve file (e.g., `Battery_Pack_Cost_Per_KWh_World.json`) has identical X/Y data to the original catalog entry

---

## Out of Scope

- Data validation / quality checks (separate task)
- SQLite or any database
- Automated sync / git hooks
- Statistical summaries in index.json
- Fuzzy / abbreviation matching (only normalized substring matching)
- Changes to the STDF pipeline orchestration logic (Steps 0-7 in CLAUDE.md)
