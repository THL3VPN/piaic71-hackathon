from __future__ import annotations

from conftest import run_cli


def test_missing_args_prints_usage_and_error() -> None:
    code, stdout, stderr = run_cli(["add"])
    assert code != 0
    assert "usage:" in stderr.lower()
    assert "description" in stderr.lower()
    assert stdout == ""


def test_invalid_command_prints_usage() -> None:
    code, stdout, stderr = run_cli(["bogus"])
    assert code != 0
    assert "usage:" in stderr.lower()
    assert stdout == ""
