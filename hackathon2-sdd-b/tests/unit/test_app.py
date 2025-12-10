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
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--task-id", "abc"])
    assert result.exit_code == 0
    assert "Deletion cancelled" in messages


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
    assert messages and "provide a task id" in messages[0]


def test_delete_force(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--force", "--task-id", "abc"])
    assert result.exit_code == 0
    assert "Deleted task" in messages


def test_delete_confirm_true(monkeypatch):
    confirms: List[bool] = []
    successes: List[str] = []
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: successes.append(msg))
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--task-id", "abc"])
    assert result.exit_code == 0
    assert "Deleted task" in successes


def test_list_success(monkeypatch):
    tasks_called: List[dict] = []
    tables: List[list] = []
    monkeypatch.setattr("cli.app.task_service.list_tasks", lambda priority=None, status=None: [{"title": "A"}])
    monkeypatch.setattr("cli.app.output.render_task_table", lambda tasks: tables.append(list(tasks)))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["list", "--priority", "low", "--status", "pending"])
    assert result.exit_code == 0
    assert tables and tables[0][0]["title"] == "A"


def test_menu_dispatch_add(monkeypatch):
    calls: List[str] = []
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: "add")
    monkeypatch.setattr("cli.app.add", lambda: calls.append("add"))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["menu"])
    assert result.exit_code == 0
    assert calls == ["add"]


def test_menu_dispatch_list(monkeypatch):
    calls: List[str] = []
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: "list")
    monkeypatch.setattr("cli.app.list", lambda: calls.append("list"))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["menu"])
    assert result.exit_code == 0
    assert calls == ["list"]


def test_menu_dispatch_delete(monkeypatch):
    calls: List[str] = []
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: "delete")
    monkeypatch.setattr("cli.app.delete", lambda: calls.append("delete"))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["menu"])
    assert result.exit_code == 0
    assert calls == ["delete"]


def test_menu_quit(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: "quit")
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["menu"])
    assert result.exit_code == 0
    assert messages == ["Goodbye"]


def test_delete_missing_id(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert "provide a task id" in messages[0]


def test_delete_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: True)
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: False)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--task-id", "missing"])
    assert result.exit_code == 0
    assert "Task not found." in messages


def test_view_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.task_service.get_task", lambda tid: None)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view", "--task-id", "missing"])
    assert result.exit_code == 0
    assert "Task not found." in messages


def test_view_success(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_task_details", lambda task: messages.append(task["id"]))
    monkeypatch.setattr("cli.app.task_service.get_task", lambda tid: {"id": tid})
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view", "--task-id", "abc"])
    assert result.exit_code == 0
    assert messages == ["abc"]
