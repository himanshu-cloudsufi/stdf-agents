#!/usr/bin/env python3
"""STDF Guardrail Validator — validates agent output files against compliance guardrails.

Usage:
    python3 validate_pipeline.py <path>          # Single file or directory
    python3 validate_pipeline.py                  # Validate most recent output dir
    python3 validate_pipeline.py --help           # Show this help

Options:
    --date YYYY-MM-DD    Override analysis date (default: today)
"""

import datetime
import glob
import os
import sys

# Ensure lib/ is importable from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.guardrails import full_guardrail_check
from lib.vocabulary import vocabulary_report


def find_most_recent_output():
    """Find the most recent output directory."""
    dirs = sorted(glob.glob('output/*/'), key=os.path.getmtime, reverse=True)
    return dirs[0] if dirs else None


def validate_directory(dir_path, analysis_date):
    """Validate all .md files in a pipeline output directory.

    Returns the number of critical violations found, or -1 on error.
    """
    files = sorted(
        glob.glob(os.path.join(dir_path, 'agents', '*.md'))
        + glob.glob(os.path.join(dir_path, '00-final-synthesis.md'))
    )

    if not files:
        print(f'ERROR: No .md output files found in {dir_path}')
        return -1

    total_critical = 0
    total_warnings = 0
    results = []

    for f in files:
        if os.path.getsize(f) == 0:
            results.append((f, 'EMPTY', 0, 0))
            continue

        text = open(f).read()
        result = full_guardrail_check(text, analysis_date)
        nc = len(result['critical_violations'])
        nw = len(result['warnings'])
        total_critical += nc
        total_warnings += nw
        status = 'PASS' if result['pass'] else 'FAIL'
        results.append((f, status, nc, nw))

    print('## STDF Guardrail Validation Report\n')
    print(f'**Date:** {analysis_date}')
    print(f'**Directory:** {dir_path}\n')
    print('| File | Status | Critical | Warnings |')
    print('|------|--------|----------|----------|')
    for f, status, nc, nw in results:
        fname = os.path.basename(f)
        print(f'| {fname} | {status} | {nc} | {nw} |')

    print(f'\n**Total: {total_critical} critical violations, {total_warnings} warnings across {len(files)} files**')
    print(f'**Result: {"PASS" if total_critical == 0 else "FAIL"}**')
    return total_critical


def validate_single_file(file_path, analysis_date):
    """Validate a single agent output file with detailed report.

    Returns the number of critical violations found, or -1 on error.
    """
    if not os.path.isfile(file_path):
        print(f'ERROR: File not found: {file_path}')
        return -1

    if os.path.getsize(file_path) == 0:
        print(f'WARNING: File is empty: {file_path}')
        return 0

    text = open(file_path).read()
    result = full_guardrail_check(text, analysis_date)
    print(result['report'])
    print()
    print(vocabulary_report(text))
    return len(result['critical_violations'])


def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        sys.exit(0)

    # Parse --date flag
    analysis_date = datetime.date.today().isoformat()
    args = list(sys.argv[1:])
    if '--date' in args:
        idx = args.index('--date')
        if idx + 1 < len(args):
            analysis_date = args[idx + 1]
            del args[idx:idx + 2]
        else:
            print('ERROR: --date requires a YYYY-MM-DD value')
            sys.exit(1)

    # Determine target
    positional = [a for a in args if not a.startswith('--')]
    if positional:
        target = positional[0]
    else:
        target = find_most_recent_output()
        if not target:
            print('ERROR: No output directories found and no path specified.')
            sys.exit(1)
        print(f'Using most recent output: {target}\n')

    if os.path.isdir(target):
        violations = validate_directory(target, analysis_date)
    elif os.path.isfile(target):
        violations = validate_single_file(target, analysis_date)
    else:
        print(f'ERROR: Path not found: {target}')
        sys.exit(1)

    sys.exit(1 if violations != 0 else 0)


if __name__ == '__main__':
    main()
