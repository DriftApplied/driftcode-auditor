# driftcode-auditor

Local-first CLI for auditing code maintainability, privacy risks, and architecture drift.

> **License:** MIT — Free to use, modify, and distribute.

## Features
- Automatically respects `.gitignore` and common build directories (`.next`, `node_modules`, `dist`, `.git`, etc.)
- Parallel scanning for good performance on large codebases
- Reports files scanned + time taken
- `--stream` mode to print issues as they are discovered
- `--quiet` and `--verbose` output modes
- Customizable file extensions via `--ext` or config file
- Configurable PII allowlist to reduce false positives
- Pure local operation — no network calls

**Configuration**
- Project-level: `.driftcode.json` in the scanned directory
- User-level: `~/.config/driftcode/config.json`

## Usage

Basic scan:
```bash
python -m src --path /path/to/project --format md --privacy
```

(You can also use `python -m src.cli`, but `python -m src` is the recommended way.)

Common options:
```bash
python -m src.cli --path . --format md --privacy --maintainability
python -m src.cli --path . --format json --privacy --stream
python -m src.cli --path . --privacy --verbose
python -m src.cli --path . --privacy --ext .py,.ts
```

### Flags
| Flag                | Description                                      |
|---------------------|--------------------------------------------------|
| `--path`            | Directory to scan (default: current dir)         |
| `--format`          | Output format: `md` or `json`                    |
| `--privacy`         | Enable privacy risk detection                    |
| `--maintainability` | Enable maintainability checks                    |
| `--stream`          | Print issues immediately as found                |
| `--output`          | File for full detailed report (default: `driftcode-report.md`) |
| `--quiet`           | Minimal output                                   |
| `--verbose`         | Show every file being scanned                    |
| `--ext`             | Comma-separated list of extensions to scan       |

## Example Output

```
Scanning /home/user/project ... (skipping common build dirs)

# DriftCode Auditor Report
...

## Privacy
- **pii** in `lib/network.ts:42`: PII in code
- ... and 47 more

## Architecture
- **large_file** in `lib/commands.ts:1`: File >500 lines
- ... and 3 more

Scan complete.
Files scanned: 1247
Time taken: 3.21s
Total issues found: 87
```

When many issues are found, only the first 15 per category are shown, followed by a summary count.

## Running Tests
```bash
python -m pytest tests/
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Philosophy
DriftCode Auditor is designed to help developers audit AI-generated code for common and obvious mistakes.

Key goals:
- Catch simple issues that would otherwise go unnoticed
- Be fast and respectful of existing project structure (respects `.gitignore`)
- Stay simple, local-first, and privacy-conscious
- Provide clear, actionable feedback without false security

All scanning happens on your machine with no data leaving your environment.

## Reviewing AI-Generated Code

DriftCode Auditor is designed to help you quickly audit code produced by AI coding assistants (Claude, Cursor, Copilot, etc.).

### Common Issues It Catches
- Missing or fake error handling
- Hardcoded secrets and credentials
- Overly generic function names
- Architectural drift and pattern violations
- Missing edge case handling
- Potential PII / secret leaks

### Recommended Workflow
1. Generate code with your AI assistant
2. Run `driftcode-auditor` on the changed files
3. Review flagged issues (especially security and error handling)
4. Use `--output report.md` for a full detailed report
5. Fix issues before committing

This adds a lightweight but effective safety net when working with AI-generated code.
