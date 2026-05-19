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
        
        # Missing error handling in try blocks (simple heuristic)
        if line.strip().startswith("try:"):
            # Look ahead up to 15 lines for an except clause
            found_except = False
            for j in range(i, min(i + 15, len(lines))):
                if lines[j].strip().startswith(("except", "finally")):
                    found_except = True
                    break
            if not found_except:
                issues.append({
                    "type": "missing_except",
                    "file": str(filepath),
                    "line": i,
                    "msg": "try block without visible except/finally clause",
                    "code": line.strip()
                })
        
        # Overly broad except clause (common AI mistake)
        if line.strip().startswith("except:") or line.strip().startswith("except Exception:"):
            issues.append({
                "type": "broad_except",
                "file": str(filepath),
                "line": i,
                "msg": "Overly broad except clause (catches everything)",
                "code": line.strip()
            })
    return issues


def check_privacy(filepath: Path, lines: List[str], pii_allowlist: List[str] = None) -> List[Dict]:
    issues = []

    # Skip PII detection inside rules.py to avoid self-flagging on regex patterns
    if filepath.name == "rules.py":
        return issues

    secret_patterns = [
        r"password\s*=\s*['\"][^'\"]+['\"]",
        r"api_key\s*=\s*['\"][^'\"]+['\"]",
        r"secret\s*=\s*['\"][^'\"]+['\"]",
        r"token\s*=\s*['\"][^'\"]+['\"]"
    ]
    pii_patterns = [
        r"\b(email|ssn|phone|password|creditcard|credit_card)\b",
        r"\b\d{3}-\d{2}-\d{4}\b",           # SSN format
        r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"     # Credit card format
    ]

    if pii_allowlist is None:
        pii_allowlist = []

    allowlist_lower = [w.lower() for w in pii_allowlist]

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
            matches = re.finditer(pat, line, re.I)
            for match in matches:
                word = match.group(0).lower()
                if word not in allowlist_lower:
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
