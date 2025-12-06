from __future__ import annotations

from conftest import run_cli


def test_cli_delete_removes_task_and_view_shows_remaining():
    code_add1, out_add1, err_add1 = run_cli(["add", "--description", "Buy milk"])
    code_add2, out_add2, err_add2 = run_cli(["add", "--description", "Do laundry"])
    assert code_add1 == 0 and code_add2 == 0
    assert "Created task 1: Buy milk [pending]" in out_add1
    assert "Created task 2: Do laundry [pending]" in out_add2
    assert err_add1 == err_add2 == ""

    code_del, out_del, err_del = run_cli(["delete", "--id", "1"])
    assert code_del == 0
    assert "Deleted task 1" in out_del
    assert err_del == ""

    code_view, out_view, err_view = run_cli(["view"])
    assert code_view == 0
    assert "1:" not in out_view
    assert "2: Do laundry [pending]" in out_view
    assert err_view == ""
