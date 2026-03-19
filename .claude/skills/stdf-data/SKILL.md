---
name: stdf-data
description: Searches and browses the STDF empirical data catalog of 956 curated time series curves covering cost, adoption, capability, and capacity data across energy, transport, compute, and materials sectors. Triggers on 'search data', 'find curves', 'what data do we have for X', 'list sectors', 'data catalog', or '/stdf-data'.
---

# STDF Data Catalog Browser

Provides quick access to the 956 curated empirical time series curves in `data/`. Each curve is a JSON file with X (years) and Y (values) arrays, organized by sector and type.

## Usage

Parse the argument to determine what the user wants:

### Search for curves
`/stdf-data lithium battery cost` or `/stdf-data "solar PV adoption"`

```bash
python3 scripts/query_curves.py --search "<query>" --detail
```

To filter by type:
```bash
python3 scripts/query_curves.py --search "<query>" --type cost --detail
```

### List available sectors
`/stdf-data --sectors` or `/stdf-data list sectors`

```bash
python3 scripts/query_curves.py --list-sectors
```

### List available types
`/stdf-data --types` or `/stdf-data list types`

```bash
python3 scripts/query_curves.py --list-types
```

### Show curve detail
`/stdf-data --detail "Battery_Pack_Cost_Global"`

```bash
python3 scripts/query_curves.py --dataset "<dataset_name>" --detail
```

### Browse a sector
`/stdf-data sector "Passenger Cars"` or `/stdf-data browse passenger_cars`

```bash
python3 scripts/query_curves.py --sector "<sector>" --detail
```

### Display a curve's X/Y data points

If the user wants to see the actual data:
```bash
python3 .claude/skills/stdf-data/scripts/display_curve.py "<file_path>"
```

## Presenting Results

- For search results: show a table with dataset name, type, region, units, and file path
- For curve detail: show metadata + a markdown table of the X/Y data
- For sector browsing: group curves by type within the sector
- Always mention the total number of matches and suggest narrower filters if there are many
