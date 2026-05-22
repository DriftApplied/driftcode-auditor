"""
Scanner module: walks directory, applies rules for issues.
Respects .gitignore automatically.
"""

import os
import time
from pathlib import Path
from typing import List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from .rules import check_maintainability, check_privacy, check_architecture
from .gitignore import load_gitignore, is_ignored
from .config import load_config, DEFAULT_CONFIG


def _process_file(filepath: Path, privacy: bool, maintainability: bool, pii_allowlist: List[str] = None) -> List[Dict]:
    try:
        if not filepath.is_file():
            return []
        content = filepath.read_text(errors='ignore')
        if not content.strip():
            return []
        lines = content.splitlines()
        issues = []
        if maintainability or not (privacy or maintainability):
            issues.extend(check_maintainability(filepath, lines))
        if privacy or not (privacy or maintainability):
            issues.extend(check_privacy(filepath, lines, pii_allowlist or []))
        issues.extend(check_architecture(filepath, lines))
        return issues
    except (OSError, UnicodeDecodeError, PermissionError):
        # Expected issues when scanning real user codebases (permissions, binary files, encoding, etc.)
        return []


def scan_directory(
    target: Path,
    privacy: bool,
    maintainability: bool,
    *,
    stream: bool = False,
    verbose: bool = False,
    custom_extensions: list = None
) -> Tuple[List[Dict], int, float]:
    """Returns (issues, files_scanned, elapsed_seconds)"""
    start = time.time()
    issues = []
    patterns = load_gitignore(target)
    config = load_config(target)
    if custom_extensions:
        extensions = tuple(custom_extensions)
    else:
        extensions = tuple(config.get("extensions", DEFAULT_CONFIG["extensions"]))
    files_to_scan = []

    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if not is_ignored(Path(root) / d, patterns, target)]
        for file in files:
            if file.endswith(extensions):
                filepath = Path(root) / file
                if not is_ignored(filepath, patterns, target):
                    files_to_scan.append(filepath)

    pii_allowlist = config.get("piiAllowlist", DEFAULT_CONFIG.get("piiAllowlist", []))

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_file = {
            executor.submit(_process_file, f, privacy, maintainability, pii_allowlist): f
            for f in files_to_scan
        }
        for future in as_completed(future_to_file):
            file_issues = future.result()
            if verbose:
                print(f"  → {future_to_file[future]}")
            if stream:
                for issue in file_issues:
                    print(f"[{issue['type']}] {issue['file']}:{issue['line']} - {issue['msg']}")
            issues.extend(file_issues)

    elapsed = time.time() - start
    return issues, len(files_to_scan), elapsed
