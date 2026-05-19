"""
Minimal gitignore parser (no external dependencies).
Automatically skips common build/dependency directories.
"""

import fnmatch
from pathlib import Path
from typing import List

# Common directories that should always be ignored
DEFAULT_IGNORES = [
    "node_modules",
    ".next",
    "dist",
    "build",
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".cache",
]


def load_gitignore(target: Path) -> List[str]:
    """Load .gitignore patterns from target directory if present."""
    gi = target / ".gitignore"
    if gi.exists():
        patterns = []
        for line in gi.read_text(errors="ignore").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
        return patterns
    return []


def is_ignored(path: Path, patterns: List[str], root: Path) -> bool:
    """Check if path should be ignored based on gitignore + default ignores."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False

    rel_str = str(rel).replace("\\", "/")
    name = path.name

    # Check default ignores first (fast path)
    if name in DEFAULT_IGNORES or any(part in DEFAULT_IGNORES for part in rel.parts):
        return True

    for pat in patterns:
        if pat.startswith("!"):
            continue
        if pat.endswith("/"):
            if rel.is_dir() and fnmatch.fnmatch(rel_str + "/", pat):
                return True
        else:
            if fnmatch.fnmatch(rel_str, pat) or fnmatch.fnmatch(name, pat):
                return True
    return False
