from typing import List

import pytest
from typer.testing import CliRunner

from cli import app as cli_app


def test_validate_priority_rejects_invalid():
    with pytest.raises(cli_app.errors.UserInputError):
        cli_app._validate_priority("urgent")


def test_validate_priority_allows_none():
    assert cli_app._validate_priority(None) is None


def test_validate_priority_allows_valid():
    assert cli_app._validate_priority("Low") == "low"


def test_list_invalid_priority_renders_error(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["list", "--priority", "urgent"])
    assert result.exit_code == 0
    assert messages and "Priority must be one of" in messages[0]


def test_delete_cancel(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: False)
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert messages == ["Deletion cancelled"]


def test_add_cancel(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", lambda **kwargs: None)
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["add"])
    assert result.exit_code == 0
    assert messages == ["Task creation cancelled"]


def test_add_success(monkeypatch):
    created = {"title": "T", "priority": "low", "notes": "", "status": "pending"}
    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", lambda **kwargs: created)
    monkeypatch.setattr("cli.app.task_service.create_task", lambda **kwargs: created)
    outputs: List[dict] = []
    monkeypatch.setattr("cli.app.output.render_task_created", lambda task: outputs.append(task))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["add"])
    assert result.exit_code == 0
    assert outputs and outputs[0]["title"] == "T"


def test_add_invalid_priority(monkeypatch):
    errors: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: errors.append(msg))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["add", "--priority", "urgent"])
    assert result.exit_code == 0
    assert errors and "Priority must be one of" in errors[0]


def test_view_placeholder(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view"])
    assert result.exit_code == 0
    assert messages and "View not yet implemented" in messages[0]


def test_delete_force(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--force"])
    assert result.exit_code == 0
    assert messages == ["Deleted task (placeholder)"]


def test_delete_confirm_true(monkeypatch):
    confirms: List[bool] = []
    successes: List[str] = []
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: successes.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert successes == ["Deleted task (placeholder)"]


def test_list_success(monkeypatch):
    tasks_called: List[dict] = []
    tables: List[list] = []
    monkeypatch.setattr("cli.app.task_service.list_tasks", lambda priority=None, status=None: [{"title": "A"}])
    monkeypatch.setattr("cli.app.output.render_task_table", lambda tasks: tables.append(list(tasks)))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["list", "--priority", "low", "--status", "pending"])
    assert result.exit_code == 0
    assert tables and tables[0][0]["title"] == "A"
