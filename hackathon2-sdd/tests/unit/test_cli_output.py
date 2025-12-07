from __future__ import annotations

from lib import cli_output
from models.task import Task


def test_render_tasks_table_stub_includes_rows() -> None:
    tasks = [Task(id=1, description="alpha", status="pending"), Task(id=2, description="beta", status="completed")]
    rendered = cli_output.render_tasks_table(tasks)
    assert "alpha" in rendered
    assert "beta" in rendered
    assert "2" in rendered


def test_render_error_panel_stub_contains_message() -> None:
    message = "something went wrong"
    rendered = cli_output.render_error_panel(message)
    assert message in rendered
    assert rendered.lower().startswith("error")


def test_render_success_panel_stub_contains_message() -> None:
    message = "all good"
    rendered = cli_output.render_success_panel(message)
    assert message in rendered
