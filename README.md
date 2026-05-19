# driftcode-auditor

Local-first CLI for auditing code maintainability, privacy risks, and architecture drift.

## Features
- Automatically respects `.gitignore` and common build directories (`.next`, `node_modules`, `dist`, `.git`, etc.)
- Parallel scanning for good performance on large codebases
- Reports files scanned + time taken
- `--stream` mode to print issues as they are discovered
- Pure local operation — no network calls

## Usage

Basic scan:
```bash
python -m src.cli --path /path/to/project --format md --privacy
```

Common options:
```bash
python -m src.cli --path . --format md --privacy --maintainability
python -m src.cli --path . --format json --privacy --stream
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

## Philosophy
DriftCode Auditor is designed to be:
- Fast enough for real-world projects
- Respectful of existing project structure
- Simple and dependency-light
- Local-first and privacy-conscious

All scanning happens on your machine with no data leaving your environment.
