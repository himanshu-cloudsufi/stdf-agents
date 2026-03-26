# Plan 09: GitHub Actions — Scheduled & CI Pipeline Runs

> **Verified against official Claude Code docs on 2026-03-14**

## Verification Summary

| Claim | Status | Notes |
|-------|--------|-------|
| `anthropics/claude-code-action@v1` exists | VERIFIED | Correct action reference |
| `max-turns` as direct `with:` input | INCORRECT | Must use `claude_args: "--max-turns 200"` (v1.0 breaking change) |
| `anthropic-api-key` (hyphen) | INCORRECT | Must be `anthropic_api_key` (underscore) |
| `workflow_dispatch` with inputs | VERIFIED | Standard GitHub Actions pattern |
| Only `ANTHROPIC_API_KEY` secret needed | INCOMPLETE | Also need Claude GitHub App installed for write access to PRs |
| Action can post PR comments | VERIFIED | Requires Claude GitHub App installation |
| `claude -p "..."` for headless CI | VERIFIED | Docs call this "programmatic CLI mode" |
| Tool restrictions | VERIFIED | Via `claude_args: "--allowedTools Read,Edit,Bash"` |
| `permissions:` block on workflows | MISSING from plan | Required for write access to contents/PRs |
| 30-minute timeout | RISKY | 6-agent pipeline likely exceeds 30 min; use 60 |

### Critical Corrections

1. **`anthropic-api-key` → `anthropic_api_key`** (underscore, not hyphen)
2. **`max-turns: 200` is not a `with:` input** — must be `claude_args: "--max-turns 200"`
3. **Add `permissions:` block** to all workflows for write access
4. **Install Claude GitHub App** before expecting PR comment functionality
5. **Increase timeout** from 30 to 60 minutes for full pipeline runs

### v1.0 Action Inputs (Official)

| Parameter | Description | Required |
|-----------|-------------|----------|
| `prompt` | Instructions for Claude (text or skill name) | No |
| `claude_args` | All CLI arguments passed to Claude Code | No |
| `anthropic_api_key` | Claude API key (underscore!) | Yes |
| `github_token` | GitHub token for API access | No |
| `trigger_phrase` | Custom trigger phrase (default: `@claude`) | No |
| `use_bedrock` | Use AWS Bedrock | No |
| `use_vertex` | Use Google Vertex AI | No |

All other configuration (model, max-turns, allowed-tools) goes through `claude_args`.

## What We Get

- **Automated weekly disruption tracking** — scheduled STDF analyses run without human intervention
- **PR-triggered validation** — agent definition changes trigger automatic compliance checks
- **Versioned output history** — analyses committed to repo, creating a time-series of disruption assessments
- **Sector monitoring** — track how cost curves and tipping points shift over time

## How We Do This

### Workflow 1: Weekly Scheduled Analysis (Corrected)

**`.github/workflows/stdf-weekly.yml`**

```yaml
name: STDF Weekly Analysis

permissions:
  contents: write
  pull-requests: write
  issues: write

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
  workflow_dispatch:
    inputs:
      sector:
        description: 'Sector to analyze'
        required: true
        default: 'energy storage disruption'

jobs:
  stdf-analysis:
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install numpy scipy matplotlib

      - name: Run STDF Analysis
        uses: anthropics/claude-code-action@v1
        with:
          prompt: |
            Run STDF analysis on ${{ github.event.inputs.sector || 'energy storage disruption' }}.
            Follow the pipeline in CLAUDE.md. Write all outputs to the output/ directory.
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          claude_args: "--max-turns 200"

      - name: Commit results
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add output/
          git commit -m "STDF analysis: ${{ github.event.inputs.sector || 'energy storage' }} ($(date +%Y-%m-%d))" || echo "No changes"
          git push
```

**Corrections from original:**
- `anthropic-api-key` → `anthropic_api_key`
- `max-turns: 200` → `claude_args: "--max-turns 200"`
- Added `permissions:` block
- Increased `timeout-minutes` from 30 to 60

### Workflow 2: Agent Definition Validation (Corrected)

**`.github/workflows/stdf-validate.yml`**

```yaml
name: STDF Agent Validation

permissions:
  contents: read
  pull-requests: write
  issues: write

on:
  pull_request:
    paths:
      - '.claude/agents/**'
      - 'CLAUDE.md'
      - 'scripts/hooks/**'
      - '.claude/rules/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4

      - name: Validate Agent Definitions
        uses: anthropics/claude-code-action@v1
        with:
          prompt: |
            Validate the STDF agent definitions in .claude/agents/.
            For each agent file, check:
            1. Valid YAML frontmatter (name, description, model, memory, tools)
            2. Compliance criteria sections present
            3. Output contract sections defined
            4. No banned vocabulary in agent prompts
            Report results as a PR comment.
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          claude_args: "--max-turns 30"
```

**Prerequisite**: The Claude GitHub App must be installed on the repository at https://github.com/apps/claude for PR comment functionality. Without it, Claude can analyze files but cannot post comments.

### Workflow 3: Smoke Test on Push (No Changes Needed)

**`.github/workflows/stdf-smoke.yml`**

```yaml
name: STDF Smoke Test
on:
  push:
    branches: [development]
    paths:
      - '.claude/agents/**'
      - 'scripts/**'
      - 'curves_catalog.json'

jobs:
  smoke-test:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      - name: Test lookup_curves script
        run: |
          chmod +x scripts/lookup_curves
          ./scripts/lookup_curves --list-sectors
          ./scripts/lookup_curves --type cost --sector "Energy Storage" --detail | head -20

      - name: Validate curves_catalog.json
        run: python3 -c "import json; d=json.load(open('curves_catalog.json')); print(f'{len(d)} curves loaded')"
```

No Claude API calls — no corrections needed.

### Alternative: Raw CLI in CI (Without the Action)

```bash
# Install Claude Code on runner
npm install -g @anthropic-ai/claude-code

# Run in programmatic CLI mode
claude -p "Run STDF analysis on energy storage" --allowedTools "Read,Edit,Bash,WebSearch,WebFetch" --max-turns 200
```

### Prerequisites Checklist

- [ ] `ANTHROPIC_API_KEY` added to GitHub repository secrets
- [ ] Claude GitHub App installed on the repository (for PR comments)
- [ ] `permissions:` block added to all workflows that need write access
- [ ] Test with `workflow_dispatch` (manual trigger) before enabling schedule

### Cost Considerations

- Weekly analysis: ~$2-5 per run (6 agents on Sonnet) = ~$8-20/month (estimate, not from docs)
- PR validation: ~$0.50 per PR (lightweight checks)
- Smoke tests: free (no Claude API calls)
- Use `--max-turns` to cap runaway costs
- Set `timeout-minutes` to prevent hung jobs

### Output Versioning Strategy

Each weekly run commits to `output/<slug>/`:
```
output/energy-storage/
  README.md                    ← Updated each run
  00-final-synthesis.md        ← Latest synthesis
  agents/                      ← Latest agent outputs
  history/
    2026-03-14/               ← Archived previous run
    2026-03-07/               ← Archived previous run
```

## Files to Create

```
.github/workflows/
  stdf-weekly.yml
  stdf-validate.yml
  stdf-smoke.yml
```

## Files to Modify

```
CLAUDE.md  — add CI/CD section documenting the workflows
```

## Dependencies

- GitHub repository with Actions enabled
- `ANTHROPIC_API_KEY` secret configured
- Claude GitHub App installed (for PR write access)
- `anthropics/claude-code-action@v1` (public GitHub Action)
