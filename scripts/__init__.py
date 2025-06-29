"""Utilities for running the task scripts with correct import paths."""

from __future__ import annotations

import os
import sys


def add_repo_root_to_path() -> None:
    """Append the repository root to ``sys.path`` if not already present."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if root not in sys.path:
        sys.path.insert(0, root)


__all__ = ["add_repo_root_to_path"]
