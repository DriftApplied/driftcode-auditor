"""
Reporter: generates elegant Markdown or JSON output.
"""

import json
from pathlib import Path
from typing import List, Dict


def generate_report(issues: List[Dict], fmt: str, target: Path, full: bool = False) -> str:
    if fmt == "json":
        return json.dumps({"target": str(target), "issues": issues}, indent=2)

    md = f"# DriftCode Auditor Report\n\n**Target:** {target}\n\n"
    md += f"**Total issues:** {len(issues)}\n\n"

    categories = {"maintainability": [], "privacy": [], "architecture": []}
    for issue in issues:
        if "long" in issue["type"] or "func" in issue["type"]:
            categories["maintainability"].append(issue)
        elif issue["type"] in ["secret", "pii"]:
            categories["privacy"].append(issue)
        else:
            categories["architecture"].append(issue)

    if full:
        # Full detailed report - show everything
        for cat, iss in categories.items():
            if iss:
                md += f"## {cat.capitalize()}\n"
            for i in iss:
                code = f" → `{i.get('code', '')}`" if 'code' in i else ""
                md += f"- **{i['type']}** in `{i['file']}:{i['line']}`: {i['msg']}{code}\n"
                md += "\n"
    else:
        # Summarized report for console
        MAX_SHOWN = 15
        for cat, iss in categories.items():
            if iss:
                md += f"## {cat.capitalize()}\n"
                shown = iss[:MAX_SHOWN]
                for i in shown:
                    code = f" → `{i.get('code', '')}`" if 'code' in i else ""
                    md += f"- **{i['type']}** in `{i['file']}:{i['line']}`: {i['msg']}{code}\n"
                if len(iss) > MAX_SHOWN:
                    md += f"- ... and {len(iss) - MAX_SHOWN} more\n"
                md += "\n"

    md += "## Summary\nClean code recommended. Run with --privacy or --maintainability for focus.\n"
    return md
