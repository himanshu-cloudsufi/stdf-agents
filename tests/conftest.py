"""Shared fixtures for STDF lib tests."""

import sys
from pathlib import Path

# Ensure lib/ is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
