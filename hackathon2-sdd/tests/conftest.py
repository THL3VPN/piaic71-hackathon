from __future__ import annotations

import contextlib
import io
import sys
from pathlib import Path
from typing import Sequence, Tuple

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from cli.main import main  # noqa: E402
from services import store  # noqa: E402


@pytest.fixture(autouse=True)
def reset_store_state():
    store.reset_store()
    yield
    store.reset_store()


def _run_cli(argv: Sequence[str] | None = None) -> Tuple[int, str, str]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    exit_code = 0
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            result = main(argv or [])
            if isinstance(result, int):
                exit_code = result
        except SystemExit as exc:  # pragma: no cover
            exit_code = int(exc.code) if isinstance(exc.code, int) else 1
    return exit_code, stdout.getvalue(), stderr.getvalue()


def run_cli(argv: Sequence[str] | None = None) -> Tuple[int, str, str]:
    """Invoke the CLI with argv and capture output."""
    return _run_cli(argv)
