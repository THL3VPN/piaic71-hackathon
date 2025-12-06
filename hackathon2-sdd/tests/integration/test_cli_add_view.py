from __future__ import annotations

from tests.conftest import run_cli


def test_cli_add_then_view_outputs_task():
    code_add, out_add, err_add = run_cli(["add", "--description", "Buy milk"])
    assert code_add == 0
    assert "Created task 1: Buy milk [pending]" in out_add
    assert err_add == ""

    code_view, out_view, err_view = run_cli(["view"])
    assert code_view == 0
    assert "1: Buy milk [pending]" in out_view
    assert err_view == ""
