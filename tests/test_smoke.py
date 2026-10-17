import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_package_import():
    import dikte

    assert dikte.__version__


def test_help_output():
    proc = subprocess.run(
        [sys.executable, "-m", "dikte", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert proc.returncode == 0
    stdout = (proc.stdout or "") + (proc.stderr or "")
    assert "usage:" in stdout.lower()
    assert "dikte" in stdout.lower()
