#!/usr/bin/env python3
"""
DriftCode Auditor - Local-first code quality scanner.
Privacy-conscious: no network, scans for risks locally.
"""

import argparse
import os
import re
from pathlib import Path
from typing import List, Dict, Any

from .scanner import scan_directory
from .reporter import generate_report


def main():
    parser = argparse.ArgumentParser(description="DriftCode Auditor: Local code audit tool")
    parser.add_argument("--path", default=".", help="Target directory to scan")
    parser.add_argument("--format", choices=["md", "json"], default="md", help="Output format")
    parser.add_argument("--privacy", action="store_true", help="Focus on privacy risks")
    parser.add_argument("--maintainability", action="store_true", help="Focus on maintainability")
    parser.add_argument("--stream", action="store_true", help="Print issues as they are found")
    parser.add_argument("--output", default="driftcode-report.md", help="File to write full detailed report")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print("Error: Path does not exist")
        return

    print(f"Scanning {target} ... (skipping common build dirs)")
    issues, files_scanned, elapsed = scan_directory(
        target, args.privacy, args.maintainability, stream=args.stream
    )

    # Always generate full detailed report
    full_report = generate_report(issues, args.format, target, full=True)
    Path(args.output).write_text(full_report)

    if not args.stream:
        summary_report = generate_report(issues, args.format, target, full=False)
        print(summary_report)

    print(f"\nScan complete.")
    print(f"Files scanned: {files_scanned}")
    print(f"Time taken: {elapsed:.2f}s")
    print(f"Total issues found: {len(issues)}")
    print(f"Full report saved to: {args.output}")


if __name__ == "__main__":
    main()
