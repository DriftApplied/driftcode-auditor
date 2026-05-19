import tempfile
from pathlib import Path
from src.scanner import scan_directory
from src.reporter import generate_report
from src.gitignore import is_ignored, load_gitignore


def test_scan():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "test.py"
        p.write_text("password = 'secret123'\ndef long_func():\n    pass\n")
        issues = scan_directory(Path(tmp), True, True)
        assert len(issues) > 0


def test_report():
    issues = [{"type": "secret", "file": "x.py", "line": 1, "msg": "test"}]
    r = generate_report(issues, "md", Path("."))
    assert "DriftCode" in r


def test_gitignore_default_ignores():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        # Create node_modules which should be ignored by default
        (root / "node_modules").mkdir()
        (root / "node_modules" / "bad.js").write_text("password = 'secret'")
        
        # Create a normal file that should be scanned
        (root / "good.py").write_text("password = 'secret'")
        
        issues, files_scanned, _ = scan_directory(root, True, False)
        # Should only find the issue in good.py, not inside node_modules
        assert files_scanned == 1
        assert len(issues) == 2  # secret + pii (password)


def test_scan_returns_stats():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "test.py"
        p.write_text("password = 'secret123'")
        issues, files_scanned, elapsed = scan_directory(Path(tmp), True, False)
        assert isinstance(files_scanned, int)
        assert isinstance(elapsed, float)
        assert files_scanned > 0


def test_stream_mode():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "test.py"
        p.write_text("password = 'secret123'")
        # Just ensure it runs without error when stream=True
        issues, _, _ = scan_directory(Path(tmp), True, False, stream=True)
        assert len(issues) > 0
