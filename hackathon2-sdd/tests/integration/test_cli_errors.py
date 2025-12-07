from __future__ import annotations

from conftest import run_cli


def test_cli_view_when_empty():
    code, out, err = run_cli(["view"])
    assert code == 0
    assert "No tasks yet." in out
    assert err == ""


def test_cli_update_missing_id_reports_error():
    code, out, err = run_cli(["update", "--id", "1", "--description", "x"])
    assert code == 1
    assert "Task 1 not found" in err
    assert out == ""


def test_cli_complete_missing_id_reports_error():
    code, out, err = run_cli(["complete", "--id", "1"])
    assert code == 1
    assert "Task 1 not found" in err
    assert out == ""


def test_cli_delete_missing_id_reports_error():
    code, out, err = run_cli(["delete", "--id", "1"])
    assert code == 1
    assert "Task 1 not found" in err
    assert out == ""
