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

## Installation

**Recommended** (avoids system Python conflicts on modern distributions):

```bash
pipx install driftcode-auditor
```

Or with a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install driftcode-auditor
```

Then run:

```bash
driftcode-auditor --help
```

**Windows users**: If `driftcode-auditor` is not found after `pip install`, use the module form instead:

```cmd
python -m driftcode_auditor --help
```

### Troubleshooting: externally-managed-environment error
This error occurs on PEP 668 systems (Ubuntu 23.04+, Debian 12+, etc.). Use `pipx` or an explicit virtual environment as shown above.

## Usage

Basic scan:
```bash
driftcode-auditor --path /path/to/project --format md --privacy
```

Or run directly from source:
```bash
python -m driftcode_auditor --path /path/to/project --format md --privacy
```

Common options:
```bash
driftcode-auditor --path . --format md --privacy --maintainability
driftcode-auditor --path . --format json --privacy --stream
driftcode-auditor --path . --privacy --verbose
driftcode-auditor --path . --privacy --ext .py,.ts
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

## Support the Project

DriftCode Auditor is free and open source, and will remain that way.

If you find it valuable — especially when auditing AI-generated code — consider sponsoring its development on [GitHub Sponsors](https://github.com/sponsors/DriftApplied).

Pro sponsors receive a manual invitation to a private repository containing advanced AI rules, priority support, and early access to new features.

Your support helps sustain focused work on the tool, funds new rule development, and keeps the project moving forward as AI coding practices evolve.

Every sponsor directly contributes to making reliable AI code review more accessible.

See [CHANGELOG.md](CHANGELOG.md) for release history.

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
3. Review flagged issues before committing
4. Use `--output report.md` for a full detailed report

### Example: Catching a Common AI Mistake

**AI-generated code:**
```python
def get_user(user_id):
    return db.query("SELECT * FROM users WHERE id = " + user_id)
```

**DriftCode Auditor output:**
```
- **pii** in `user_service.py:12`: PII in code → `return db.query("SELECT * FROM users WHERE id = " + user_id)`
- **secret** in `user_service.py:12`: Potential SQL injection risk
```

This helps catch problems that are easy to miss in normal code review.

This adds a lightweight but effective safety net when working with AI-generated code.

## DriftCode Auditor Pro (Paid)

Pro features are delivered via a separate private repository for sponsors (see [PAID_OFFERING.md](PAID_OFFERING.md)). The free CLI has no access to paid features.
