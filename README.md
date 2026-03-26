# STDF v2 Agents

Multi-agent pipeline for technology disruption analysis using the **Seba Technology Disruption Framework (STDF)**. 18 specialized agents orchestrated through a dynamic DAG, backed by 956 empirical time series curves and 15 Python computation modules.

## Quick Start

```bash
# Run a full disruption analysis
/stdf "Analyze the energy storage disruption"

# Headless mode (no interactive prompts)
claude -p "Analyze the energy storage disruption using the STDF framework"
```

## Agents

The pipeline coordinates 18 agents organized into execution tiers. Agents communicate exclusively through files — each agent writes a markdown output that downstream agents read.

### Tier 1 — Foundation (parallel)

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-domain-disruption` | `01-domain-disruption.md` | Maps disruption landscape: disruptors, incumbents, chimeras, convergence combinations |
| `stdf-cost-researcher` | `02a-cost-researcher.md` | Collects historical cost data from empirical catalog and web sources |
| `stdf-capability` | `03-capability.md` | Multi-dimensional capability comparison between disruptors and incumbents |

### Tier 2 — Cost Fitting

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-cost-fitter` | `02b-cost-fitter.md` | Fits exponential cost curves, derives learning rates and competitive thresholds |

### Tier 3 — Tipping Conditions (parallel)

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-cost-parity-checker` | `04a-cost-parity.md` | Evaluates whether disruptor has reached cost parity with incumbent |
| `stdf-capability-parity-checker` | `04b-cap-parity.md` | Assesses capability parity across performance dimensions |
| `stdf-adoption-readiness-checker` | `04c-adopt-readiness.md` | Checks infrastructure, supply chain maturity, and regulatory readiness |

### Tier 4 — Tipping Synthesis

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-tipping-synthesizer` | `04d-tipping-synthesizer.md` | Integrates all three tipping conditions into a unified tipping point determination |

### Tier 5 — Adoption Modeling (parallel)

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-scurve-fitter` | `05a-scurve-fitter.md` | Fits logistic S-curve to historical adoption data, projects forward with confidence intervals |
| `stdf-regional-adopter` | `05b-regional-adopter.md` | Per-region adoption breakdown with phase classification |
| `stdf-xcurve-analyst` | `05c-xcurve-analyst.md` | Incumbent decline mapping and market trauma assessment |

### Tier 6 — Commodity Demand Chain (conditional)

Activated when the query involves commodity demand (copper, lithium, etc.).

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-demand-decomposer` | `07a-demand-decomposer.md` | Decomposes commodity demand into market products with material intensity coefficients |
| `stdf-stream-forecaster` | `07b-stream-forecaster.md` | Projects demand across 3 technology streams: incumbent, disruptor, chimera |
| `stdf-fleet-modeler` | `07c-fleet-modeler.md` | Stock-flow fleet modeling with OEM vs replacement demand splitting |
| `stdf-regional-demand-analyst` | `07d-regional-demand.md` | Disaggregates global commodity demand by region |

### Tier 7 — Energy Dispatch Chain (conditional)

Activated for energy sector analyses involving generation, dispatch, or grid modeling.

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-energy-dispatch` | `08a-energy-dispatch.md` | SWB merit order dispatch: demand decomposition, generation shares, displacement schedule |
| `stdf-gas-supply-decomposer` | `08b-gas-supply.md` | Gas supply source decomposition and LNG displacement cascade |

### Final — Synthesis (always runs)

| Agent | Output | Description |
|-------|--------|-------------|
| `stdf-synthesizer` | `00-final-synthesis.md` | Merges all agent outputs into a unified 7-phase disruption narrative |

## Skills (Slash Commands)

Run these directly in Claude Code:

| Command | Description |
|---------|-------------|
| `/stdf "query"` | Full pipeline — detects preset, resolves DAG, executes agents, validates, synthesizes |
| `/stdf-data "query"` | Search the 956-curve empirical data catalog |
| `/stdf-validate [path]` | Guardrail audit: banned vocabulary, forecast language, source provenance |
| `/stdf-compliance <file>` | Structural compliance check for a specific agent output |
| `/stdf-readme [dir]` | Generate/regenerate the README index for a pipeline run |
| `/show-report` | Start local HTTP server and open the STDF progress report in browser |

### Examples

```bash
# Full disruption analysis
/stdf "Analyze battery storage disrupting gas peakers"

# Quick cost-focused analysis
/stdf "Quick overview of solar cost trajectory"

# Tipping point only
/stdf "When does autonomous transport tip?"

# With commodity demand chain
/stdf "Analyze copper demand implications of the EV disruption"

# With energy dispatch chain
/stdf "Model SWB displacement of coal and gas in European power generation"

# Search the data catalog
/stdf-data "lithium battery cost"
/stdf-data "solar capacity"

# Validate outputs
/stdf-validate output/energy-storage/
/stdf-compliance output/energy-storage/agents/02b-cost-fitter.md

# Generate run index
/stdf-readme output/energy-storage/
```

## Pipeline Presets

The `/stdf` skill auto-detects the appropriate preset from the query:

| Preset | Trigger Keywords | Agents Included |
|--------|-----------------|-----------------|
| **FULL** | Default | Foundation + tipping + adoption + synthesis |
| **QUICK** | "quick", "brief", "overview" | Cost-fitter + synthesis |
| **TIPPING_ONLY** | "tipping point", "when does X tip" | Through tipping-synthesizer + synthesis |
| **COST_FOCUS** | "cost trajectory", "learning rate", "price" | Cost-fitter + capability + synthesis |
| **ADOPTION_FOCUS** | "market share", "adoption" | S-curve + regional + X-curve + synthesis |
| **FULL+COMMODITY** | Commodity keyword + "demand"/"supply" | FULL + commodity demand chain |
| **ENERGY_FULL** | Energy sector + "dispatch"/"grid"/"SWB" | FULL + energy dispatch chain |
| **ENERGY_GAS** | "LNG", "natural gas" + supply/demand | FULL + energy + gas supply chain |

## Failure Handling

| Criticality | On Failure | Effect |
|-------------|-----------|--------|
| **CRITICAL** | Hard fail — pipeline stops | No synthesis produced |
| **HIGH** | Continue with warning | Degraded output, noted in README |
| **MEDIUM** | Continue silently | Minor gap, noted in synthesis |

## Project Structure

```
stdf-agents/
├── .claude/
│   ├── agents/            # 18 agent definitions
│   ├── skills/            # 6 skill definitions (slash commands)
│   ├── agent-memory/      # Persistent per-agent memory
│   └── shared-rules.md    # Vocabulary, guardrails, computation rules
├── lib/                   # Python computation modules
│   ├── cost_curve_math.py    # Exponential fitting, learning rates
│   ├── scurve_math.py        # Logistic S-curve fitting (scipy)
│   ├── capability_math.py    # Multi-dimensional capability scoring
│   ├── tipping_math.py       # Tipping condition integration
│   ├── demand_math.py        # Commodity demand decomposition
│   ├── energy_math.py        # Merit order dispatch modeling
│   ├── data_catalog.py       # Empirical catalog search/access
│   ├── guardrails.py         # Vocabulary and compliance validation
│   ├── compliance.py         # Structural compliance checking
│   ├── vocabulary.py         # Banned terms and forecast language rules
│   ├── markdown_parser.py    # Agent output parsing
│   ├── upstream_reader.py    # Cross-agent file reading
│   ├── output_writer.py      # Standardized output formatting
│   ├── readme_writer.py      # Pipeline run README generation
│   └── __init__.py
├── data/                  # 956 empirical time series curves (JSON)
│   ├── battery_pack/         # Battery cost, capacity, density
│   ├── energy_storage/       # Grid storage deployment
│   ├── passenger_cars/       # EV adoption, cost, fleet
│   ├── energy_generation/    # Solar, wind, fossil generation
│   ├── energy_sector/        # Dispatch config, marginal costs
│   ├── copper/               # Copper demand, pricing
│   ├── artificial_intelligence/ # AI capability, cost
│   └── ...                   # 28 sectors total
├── scripts/
│   ├── query_curves.py       # CLI: search and inspect data curves
│   └── build_data.py         # CLI: rebuild data index
├── output/                # Pipeline run outputs (one dir per analysis)
├── reports/               # Audit reports and progress dashboards
├── docs/                  # Project documentation
│   ├── plans/                # Roadmap and implementation plans
│   ├── specs/                # Design specifications
│   └── *.md                  # Chat UI, implementation, eval docs
├── archive/               # Legacy/historical content
│   ├── old_prompts/          # v1 prompt files (pre-agent era)
│   └── chat_exports/         # User session exports
├── server/                # Python backend (WebSocket API)
├── frontend/              # Vite/React web UI
└── tests/                 # Python test suite
```

## Data Catalog

956 curated time series curves organized by sector, covering:

- **Cost** — Technology cost trajectories ($/kWh, $/W, $/unit)
- **Adoption** — Market share, sales volumes, fleet sizes
- **Capability** — Performance metrics (energy density, efficiency, range)
- **Capacity** — Installed capacity, production volumes

Search with `/stdf-data "query"` or programmatically via `lib/data_catalog.py`.

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Python 3 with scipy, numpy (for curve fitting agents)
