#!/usr/bin/env python3
"""Display the X/Y data points for an STDF empirical curve.

Usage:
    python3 display_curve.py <file_path>     # Display curve data
    python3 display_curve.py --help           # Show this help

The file_path should be relative to the project root, matching
the paths in the data catalog index.json.
"""

import os
import sys

# Ensure lib/ is importable from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.data_catalog import load_curve


def display_curve(file_path):
    """Load and display a curve's metadata and data points."""
    if not os.path.isfile(file_path):
        print(f'ERROR: File not found: {file_path}')
        sys.exit(1)

    curve = load_curve(file_path)
    x, y = curve['X'], curve['Y']

    print(f'Dataset: {curve.get("dataset_name", "N/A")}')
    print(f'Type: {curve.get("type", "N/A")}')
    print(f'Units: {curve.get("units", "N/A")}')
    print(f'Region: {curve.get("region", "Global")}')
    print(f'Source: {curve.get("source", "N/A")}')
    print(f'Points: {len(x)}')
    print(f'Year range: {min(x)}-{max(x)}')
    print()
    print('| Year | Value |')
    print('|------|-------|')
    for xi, yi in zip(x, y):
        print(f'| {int(xi)} | {yi} |')


def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        sys.exit(0)

    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print('ERROR: No file path specified.')
        print('Usage: python3 display_curve.py <file_path>')
        sys.exit(1)

    display_curve(args[0])


if __name__ == '__main__':
    main()
