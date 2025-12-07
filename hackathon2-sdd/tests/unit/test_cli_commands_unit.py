from __future__ import annotations

from typing import Sequence

import pytest

from conftest import run_cli


def test_view_formats_with_header_and_rows() -> None:
    run_cli(["add", "--description", "alpha"])
    run_cli(["add", "--description", "beta"])

    exit_code, stdout, stderr = run_cli(["view"])

    assert exit_code == 0
    assert "Tasks:" in stdout
    assert "alpha" in stdout and "beta" in stdout
    assert stderr == ""


@pytest.mark.parametrize(
    "argv",
    [
        ["update", "--id", "abc", "--description", "new desc"],
        ["complete", "--id", "0"],
        ["delete", "--id", "-3"],
    ],
)
def test_commands_validate_ids(argv: Sequence[str]) -> None:
    exit_code, _, stderr = run_cli(list(argv))

    assert exit_code == 1
    assert "Task id must be a positive integer" in stderr
