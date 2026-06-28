from __future__ import annotations

import subprocess
import sys

from costtrace.config import PATHS


def test_full_pipeline_dry_run_smoke() -> None:
    result = subprocess.run(
        [sys.executable, "main.py", "--phase", "all", "--dry-run"],
        cwd=PATHS.root,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "src/costtrace/preparation/audit.py" in result.stdout
    assert "src/costtrace/reporting/notebooks.py" in result.stdout
    assert "dry run completed" in result.stdout


def test_reproducibility_validator_smoke() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_reproducibility.py"],
        cwd=PATHS.root,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "REPRODUCIBILITY_OK" in result.stdout
