---
name: stdf-readme
description: "Generates the README.md index file for a completed STDF pipeline run by scanning agent output files, extracting confidence scores, running validation, and producing a structured summary.\n\nExamples:\n\n- User: \"Generate a README for the energy storage run\"\n  Assistant: \"Launching stdf-readme to scan outputs and produce an index for the energy storage pipeline run.\"\n  [Uses Agent tool with subagent_type: stdf-readme]\n\n- User: \"Summarize the latest pipeline run\"\n  Assistant: \"Generating README.md for the most recent output directory.\"\n  [Uses Agent tool with subagent_type: stdf-readme]"
tools: Bash, Read, Write, Glob, Grep
model: sonnet
---

# STDF README Generator

Generates the `README.md` index file for a completed STDF pipeline run by scanning all agent output files in the output directory.

## Usage

The prompt should specify the path to an output directory. If omitted, use the most recent:
```bash
ls -td output/*/ 2>/dev/null | head -1
```

## Execution

### 1. Scan agent outputs

Read all `*.md` files in `<output-dir>/agents/` and `<output-dir>/00-final-synthesis.md`.

For each file, extract:
- Agent name (from `**Agent:** \`name\`` header)
- Confidence score (from `**Confidence:** score` header)
- File path (relative to output dir)

Use `lib.markdown_parser`:
```python
from lib.markdown_parser import parse_agent_file, extract_confidence
```

### 2. Run validation

```python
from lib.guardrails import full_guardrail_check
```

Check each file and collect pass/fail status.

### 3. Extract key conclusion

From the synthesizer output or `00-final-synthesis.md`, extract the key conclusion and rupture window.

### 4. Generate README

Use `lib.readme_writer`:
```python
from lib.readme_writer import write_readme

content = write_readme(
    slug="<slug>",
    topic="<topic from synthesis>",
    agent_results=[
        {"agent_name": "...", "confidence": 0.85, "status": "OK", "duration_s": 0, "file_path": "agents/..."},
        ...
    ],
    output_dir="output/<slug>",
    conclusion="<key conclusion text>"
)
```

Write to `<output-dir>/README.md`.

### 5. Enhance with additional sections

Add these sections beyond what `write_readme()` produces:

- **Guardrail Validation**: Pass/fail summary from the scan
- **Agents Skipped**: List agents NOT present in the directory (compare against full 16-agent registry)
- **Critical Path**: Identify the tier structure from the files present

### Example output structure

The generated README should look like:
```
# STDF Analysis: Energy Storage
**Preset:** FULL | **Agents:** 12 | **Date:** 2026-03-19
## Key Conclusion
[rupture window and headline from synthesizer]
## Agent Results
| Agent | Confidence | Status | File |
...
```

## Presenting Results

After writing, show:
1. Confirmation that README.md was written
2. Summary: total agents, pass/fail count, overall confidence
3. Key conclusion excerpt
