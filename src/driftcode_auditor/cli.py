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
    parser = argparse.ArgumentParser(
        description="DriftCode Auditor - Audit AI-generated code for common mistakes",
        epilog="Examples:\n"
               "  python -m src --path . --privacy --maintainability\n"
               "  python -m src --path . --privacy --verbose\n"
               "  python -m src --path . --ext .py,.ts --output report.md"
    )
    parser.add_argument("--path", default=".", help="Target directory to scan")
    parser.add_argument("--format", choices=["md", "json"], default="md", help="Output format")
    parser.add_argument("--privacy", action="store_true", help="Focus on privacy risks")
    parser.add_argument("--maintainability", action="store_true", help="Focus on maintainability")
    parser.add_argument("--stream", action="store_true", help="Print issues as they are found")
    parser.add_argument("--output", default="driftcode-report.md", help="File to write full detailed report")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")
    parser.add_argument("--verbose", action="store_true", help="Show every file being scanned")
    parser.add_argument("--ext", help="Comma-separated list of extensions to scan (e.g. .py,.js,.ts)")
    parser.add_argument("--version", action="version", version="DriftCode Auditor 0.2.1")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print("Error: Path does not exist")
        return

    if not args.quiet:
        print(f"Scanning {target} ... (skipping common build dirs)")

    custom_extensions = args.ext.split(",") if args.ext else None
    issues, files_scanned, elapsed = scan_directory(
        target, args.privacy, args.maintainability, stream=args.stream, verbose=args.verbose,
        custom_extensions=custom_extensions
    )

    # Always generate full detailed report
    full_report = generate_report(issues, args.format, target, full=True)
    Path(args.output).write_text(full_report, encoding="utf-8")

    if not args.quiet and not args.stream:
        summary_report = generate_report(issues, args.format, target, full=False)
        print(summary_report)

    if not args.quiet:
        print(f"\nScan complete.")
        print(f"Files scanned: {files_scanned}")
        print(f"Time taken: {elapsed:.2f}s")
        print(f"Total issues found: {len(issues)}")
        print(f"Full report saved to: {args.output}")


if __name__ == "__main__":
    main()
