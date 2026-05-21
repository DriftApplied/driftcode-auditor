# Changelog

All notable changes to DriftCode Auditor (free) are documented here.

## [0.2.2] - 2026-05-21

### Fixed
- Improved robustness in error handling (scanner and config loading):
  - Replaced blanket `except Exception` swallows with specific exception handling + re-raise for unexpected errors.
  - Prevents silent failure on file processing and config parsing bugs.
- Changes discovered and validated through dogfooding: running the auditor on its own source code.
- These were classic AI-generated patterns (overly broad exception handling) that the tool is designed to catch.

### Notes
- This is a bugfix release focused on making the tool more reliable when scanning real codebases.
- Version bumped to 0.2.2.
- Requires more real-world testing from users.

## [0.2.1] - 2026-05-20

### Changed
- Acquisition phase work: README polish, GitHub templates, Discussions, good-first issues, and initial visibility assets.
- Contributor example improvements merged and refined.

[0.2.1]: https://github.com/DriftApplied/driftcode-auditor/releases/tag/v0.2.1
