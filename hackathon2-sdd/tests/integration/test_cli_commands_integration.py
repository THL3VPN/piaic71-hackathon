from __future__ import annotations

from conftest import run_cli


def test_full_command_flow_formats_view_output() -> None:
    code, _, _ = run_cli(["add", "--description", "first task"])
    assert code == 0
    code, _, _ = run_cli(["update", "--id", "1", "--description", "first updated"])
    assert code == 0
    code, _, _ = run_cli(["complete", "--id", "1"])
    assert code == 0
    code, _, _ = run_cli(["add", "--description", "second task"])
    assert code == 0

    view_code, stdout, stderr = run_cli(["view"])

    assert view_code == 0
    assert "Tasks:" in stdout
    assert "first updated" in stdout and "second task" in stdout
    assert "completed" in stdout
    assert stderr == ""
