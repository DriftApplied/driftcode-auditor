"""
Configuration loader for DriftCode Auditor.
Supports:
- User-level config: ~/.config/driftcode/config.json
- Project-level config: .driftcode.json (in scanned directory)
Project-level config takes precedence over user-level.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any


DEFAULT_CONFIG = {
    "extensions": [".py", ".js", ".ts", ".java", ".go"],
    "piiAllowlist": ["email", "phone", "userEmail", "user_id"],
    "ignore": [],
    "maxFileSizeKB": 2048
}


def _load_json_config(path: Path) -> Dict[str, Any]:
    """Safely load a JSON config file."""
    if path.exists():
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def load_config(target: Path) -> Dict[str, Any]:
    """
    Load configuration with the following priority (highest first):
    1. Project-level: <target>/.driftcode.json
    2. User-level: ~/.config/driftcode/config.json
    3. Built-in defaults
    """
    config = DEFAULT_CONFIG.copy()

    # User-level config
    user_config_path = Path.home() / ".config" / "driftcode" / "config.json"
    user_config = _load_json_config(user_config_path)
    config.update(user_config)

    # Project-level config (highest priority)
    project_config_path = target / ".driftcode.json"
    project_config = _load_json_config(project_config_path)
    config.update(project_config)

    return config
