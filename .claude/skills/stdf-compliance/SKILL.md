---
name: stdf-compliance
description: Evaluates a single STDF agent output file against its structural and analytical compliance criteria (CRITICAL/HIGH/MEDIUM). Different from stdf-validate which checks vocabulary — this checks whether required tables, data points, units, and analyses are present. Triggers on 'check compliance', 'is this compliant', 'run checklist', or '/stdf-compliance'.
---

# STDF Compliance Checker

Evaluates a single agent output file against its compliance criteria checklist. Each agent has specific CRITICAL, HIGH, and MEDIUM criteria that must be met.

## Usage

`/stdf-compliance output/energy-storage/agents/02b-cost-fitter.md`

The argument should be a path to an agent output file.

## Execution

### 1. Identify the agent

Read the file. If the file does not exist, report the error and stop — do not guess the agent name.

Extract the agent name from the `**Agent:** \`agent-name\`` header line.

### 2. Select the criteria

Use `lib.compliance` to load the appropriate criteria set:

```python
from lib.compliance import (
    COST_CURVE_CRITERIA, CAPABILITY_CRITERIA, ADOPTION_CRITERIA,
    TIPPING_CRITERIA, SYNTHESIZER_CRITERIA, COMMODITY_DEMAND_CRITERIA,
    create_checklist, checklist_to_markdown, update_criterion, overall_status
)
```

Map agent names to criteria:

| Agent slug | Criteria constant |
|-----------|------------------|
| stdf-cost-researcher | COST_CURVE_CRITERIA (2.1-2.4 only) |
| stdf-cost-fitter | COST_CURVE_CRITERIA |
| stdf-capability | CAPABILITY_CRITERIA |
| stdf-capability-parity-checker | CAPABILITY_CRITERIA (3.5-3.6 only) |
| stdf-cost-parity-checker | TIPPING_CRITERIA (5.3 only) |
| stdf-adoption-readiness-checker | TIPPING_CRITERIA (5.2 only) |
| stdf-tipping-synthesizer | TIPPING_CRITERIA |
| stdf-scurve-fitter | ADOPTION_CRITERIA (4.1-4.3 only) |
| stdf-regional-adopter | ADOPTION_CRITERIA (4.6 only) |
| stdf-xcurve-analyst | ADOPTION_CRITERIA (4.4-4.5 only) |
| stdf-demand-decomposer | COMMODITY_DEMAND_CRITERIA (7.1-7.5) |
| stdf-stream-forecaster | COMMODITY_DEMAND_CRITERIA (7.3, 7.6) |
| stdf-fleet-modeler | COMMODITY_DEMAND_CRITERIA (7.7-7.8) |
| stdf-regional-demand-analyst | COMMODITY_DEMAND_CRITERIA (7.9) |
| stdf-synthesizer | SYNTHESIZER_CRITERIA |

If the agent name doesn't match any row above, report that the agent is not recognized and list the valid slugs.

### 3. Evaluate each criterion

Read the agent output file and check each criterion by examining the structured content:

- Look for required sections (tables, key-value pairs)
- Check data point counts
- Verify units are service-level
- Confirm required analyses are present
- Check for S-curve (not linear) models

Use `update_criterion(checklist, id, "PASS"/"FAIL", note)` for each.

### 4. Generate report

```python
checklist = create_checklist(CRITERIA)
# ... evaluate each criterion ...
print(checklist_to_markdown(checklist))
print(f"\nOverall: {overall_status(checklist)}")
```

## Presenting Results

Show:
1. The compliance checklist table (ID, Severity, Status, Description, Note)
2. Overall status: COMPLIANT / DEGRADED / NON-COMPLIANT
3. For any FAIL criteria, explain what's missing and how to fix it
4. If the agent has CRITICAL failures, flag that this would cause a pipeline hard-fail
