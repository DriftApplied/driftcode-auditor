"""
Rules: detect maintainability, privacy, architecture issues.
Simple regex + heuristics for MVP. Extensible.
"""

import re
from pathlib import Path
from typing import List, Dict


def check_maintainability(filepath: Path, lines: List[str]) -> List[Dict]:
    issues = []
    for i, line in enumerate(lines, 1):
        if len(line) > 100:
            issues.append({"type": "long_line", "file": str(filepath), "line": i, "msg": "Line >100 chars"})
        if line.strip().startswith("def ") and i + 30 < len(lines):
            issues.append({"type": "long_func", "file": str(filepath), "line": i, "msg": "Potential long function"})
    return issues


def check_privacy(filepath: Path, lines: List[str]) -> List[Dict]:
    issues = []
    secret_patterns = [r"password\s*=\s*['\"][^'\"]+['\"]", r"api_key\s*=\s*['\"][^'\"]+['\"]"]
    pii_patterns = [r"\b(email|ssn|phone)\b", r"\b\d{3}-\d{2}-\d{4}\b"]
    for i, line in enumerate(lines, 1):
        for pat in secret_patterns:
            if re.search(pat, line, re.I):
                issues.append({
                    "type": "secret",
                    "file": str(filepath),
                    "line": i,
                    "msg": "Hardcoded secret",
                    "code": line.strip()
                })
        for pat in pii_patterns:
            if re.search(pat, line, re.I):
                issues.append({
                    "type": "pii",
                    "file": str(filepath),
                    "line": i,
                    "msg": "PII in code",
                    "code": line.strip()
                })
    return issues


def check_architecture(filepath: Path, lines: List[str]) -> List[Dict]:
    issues = []
    if len(lines) > 500:
        issues.append({"type": "large_file", "file": str(filepath), "line": 1, "msg": "File >500 lines"})
    return issues
