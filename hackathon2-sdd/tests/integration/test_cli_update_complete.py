from __future__ import annotations

from conftest import run_cli


def test_cli_update_and_complete_flow():
    code_add, out_add, err_add = run_cli(["add", "--description", "Buy milk"])
    assert code_add == 0
    assert "Created task 1: Buy milk [pending]" in out_add
    assert err_add == ""

    code_update, out_update, err_update = run_cli(
        ["update", "--id", "1", "--description", "Buy oat milk"]
    )
    assert code_update == 0
    assert "Updated task 1: Buy oat milk [pending]" in out_update
    assert err_update == ""

    code_complete, out_complete, err_complete = run_cli(["complete", "--id", "1"])
    assert code_complete == 0
    assert "Completed task 1: Buy oat milk" in out_complete
    assert err_complete == ""

    code_complete2, out_complete2, err_complete2 = run_cli(["complete", "--id", "1"])
    assert code_complete2 == 0
    assert "Task 1 is already completed" in out_complete2
    assert err_complete2 == ""


def test_cli_update_rejects_empty_description():
    run_cli(["add", "--description", "Task"])
    code, out, err = run_cli(["update", "--id", "1", "--description", "   "])
    assert code == 1
    assert "Description cannot be empty" in err
    assert out == ""
