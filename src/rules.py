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
            issues.append({
                "type": "long_line", 
                "file": str(filepath), 
                "line": i, 
                "msg": "Line >100 chars",
                "code": line.strip()
            })
        
        # Long function detection
        if line.strip().startswith("def ") and i + 30 < len(lines):
            issues.append({
                "type": "long_func", 
                "file": str(filepath), 
                "line": i, 
                "msg": "Potential long function (>30 lines)",
                "code": line.strip()
            })
        
        # Too many parameters (simple heuristic)
        if "def " in line and line.count(",") >= 5:
            issues.append({
                "type": "too_many_params",
                "file": str(filepath),
                "line": i,
                "msg": "Function with many parameters",
                "code": line.strip()
            })
        
        # TODO/FIXME comments
        if any(marker in line.upper() for marker in ["TODO", "FIXME", "HACK"]):
            issues.append({
                "type": "todo",
                "file": str(filepath),
                "line": i,
                "msg": "TODO/FIXME/HACK comment",
                "code": line.strip()
            })
        
        # Common AI-generated code smell: overly generic function names
        if line.strip().startswith("def "):
            func_name = line.split("(")[0].replace("def ", "").strip()
            if func_name in ["process", "handle", "execute", "run", "do_something", "main_logic"]:
                issues.append({
                    "type": "generic_function",
                    "file": str(filepath),
                    "line": i,
                    "msg": "Overly generic function name (possible AI-generated code smell)",
                    "code": line.strip()
                })
    return issues


def check_privacy(filepath: Path, lines: List[str], pii_allowlist: List[str] = None) -> List[Dict]:
    issues = []
    secret_patterns = [r"password\s*=\s*['\"][^'\"]+['\"]", r"api_key\s*=\s*['\"][^'\"]+['\"]"]
    pii_patterns = [r"\b(email|ssn|phone)\b", r"\b\d{3}-\d{2}-\d{4}\b"]

    if pii_allowlist is None:
        pii_allowlist = []

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
                # Check against allowlist
                word = re.search(pat, line, re.I)
                if word and word.group(0).lower() not in [w.lower() for w in pii_allowlist]:
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
