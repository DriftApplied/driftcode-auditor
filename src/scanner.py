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


def _process_file(filepath: Path, privacy: bool, maintainability: bool) -> List[Dict]:
    try:
        content = filepath.read_text(errors='ignore')
        lines = content.splitlines()
        issues = []
        if maintainability or not (privacy or maintainability):
            issues.extend(check_maintainability(filepath, lines))
        if privacy or not (privacy or maintainability):
            issues.extend(check_privacy(filepath, lines))
        issues.extend(check_architecture(filepath, lines))
        return issues
    except Exception:
        return []


def scan_directory(target: Path, privacy: bool, maintainability: bool, stream: bool = False) -> Tuple[List[Dict], int, float]:
    """Returns (issues, files_scanned, elapsed_seconds)"""
    start = time.time()
    issues = []
    patterns = load_gitignore(target)
    files_to_scan = []

    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if not is_ignored(Path(root) / d, patterns, target)]
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.java', '.go')):
                filepath = Path(root) / file
                if not is_ignored(filepath, patterns, target):
                    try:
                        # Quick permission check
                        filepath.stat()
                        files_to_scan.append(filepath)
                    except PermissionError:
                        continue

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_file = {
            executor.submit(_process_file, f, privacy, maintainability): f
            for f in files_to_scan
        }
        for future in as_completed(future_to_file):
            file_issues = future.result()
            if stream:
                for issue in file_issues:
                    print(f"[{issue['type']}] {issue['file']}:{issue['line']} - {issue['msg']}")
            issues.extend(file_issues)

    elapsed = time.time() - start
    return issues, len(files_to_scan), elapsed
