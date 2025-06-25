"""Scripts to reproduce the tutorial tasks.

This package also provides a small helper to ensure the repository
root is on ``sys.path`` when running scripts directly. Import and call
``add_repo_root_to_path()`` at the top of a script so relative imports
from ``src`` work regardless of the current working directory.
"""

from __future__ import annotations

import os
import sys


def add_repo_root_to_path() -> None:
    """Append the repository root to ``sys.path`` if not already present."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if root not in sys.path:
        sys.path.insert(0, root)


__all__ = ["add_repo_root_to_path"]
