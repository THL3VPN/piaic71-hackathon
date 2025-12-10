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
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
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


def test_add_optioninfo_like(monkeypatch):
    class FakeOption:
        pass
    errors: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: errors.append(msg))
    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", lambda **kwargs: None)
    result = CliRunner().invoke(cli_app.app, ["add"], obj=FakeOption())
    assert result.exit_code == 0


def test_view_placeholder(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: None)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view"])
    assert result.exit_code == 0
    assert "No task selected." in messages


def test_delete_missing_id(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: None)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert "No task selected." in messages


def test_delete_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: True)
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "missing")
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: False)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert "Task not found." in messages


def test_delete_force(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete", "--force"])
    assert result.exit_code == 0
    assert "Deleted task" in messages


def test_delete_confirm_true(monkeypatch):
    successes: List[str] = []
    monkeypatch.setattr("cli.app.prompts.confirm_action", lambda msg, default=False: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: successes.append(msg))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.delete_task", lambda tid: True)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["delete"])
    assert result.exit_code == 0
    assert "Deleted task" in successes


def test_list_success(monkeypatch):
    tables: List[list] = []
    monkeypatch.setattr("cli.app.task_service.list_tasks", lambda priority=None, status=None: [{"title": "A"}])
    monkeypatch.setattr("cli.app.output.render_task_table", lambda tasks: tables.append(list(tasks)))

    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["list", "--priority", "low", "--status", "pending"])
    assert result.exit_code == 0
    assert tables and tables[0][0]["title"] == "A"


def test_menu_dispatch_update(monkeypatch):
    calls: List[str] = []
    seq = iter(
        [
            "Update Task – Modify existing task details",
            "Quit",
        ]
    )
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: next(seq))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.update_task", lambda *args, **kwargs: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: calls.append("update"))
    cli_app.menu()
    assert "update" in calls


def test_menu_dispatch_add(monkeypatch):
    calls: List[str] = []
    seq = iter(["Add Task – Create new todo items", "Quit"])
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: next(seq))
    monkeypatch.setattr("cli.app.add", lambda: calls.append("add"))
    cli_app.menu()
    assert "add" in calls


def test_menu_dispatch_delete(monkeypatch):
    calls: List[str] = []
    seq = iter(["Delete Task – Remove tasks from the list", "Quit"])
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: next(seq))
    monkeypatch.setattr("cli.app.delete", lambda: calls.append("delete"))
    cli_app.menu()
    assert "delete" in calls


def test_menu_dispatch_complete(monkeypatch):
    calls: List[str] = []
    seq = iter(
        [
            "Mark as Complete – Toggle task completion status",
            "Quit",
        ]
    )
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: next(seq))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.mark_complete", lambda tid: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: calls.append("complete"))
    cli_app.menu()
    assert "complete" in calls


def test_menu_dispatch_view(monkeypatch):
    calls: List[str] = []
    seq = iter(
        [
            "View Task List – Display all tasks",
            "Quit",
        ]
    )
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: next(seq))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.output.render_task_details", lambda task: calls.append("view"))
    monkeypatch.setattr("cli.app.task_service.get_task", lambda tid: {"id": tid})
    monkeypatch.setattr("cli.app.output.render_task_table", lambda tasks: calls.append("list"))
    monkeypatch.setattr("cli.app.task_service.list_tasks", lambda priority=None, status=None: [{"id": "abc", "title": "T", "status": "pending", "priority": "low", "notes": ""}])
    cli_app.menu()
    assert "list" in calls and "view" in calls


def test_view_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "missing")
    monkeypatch.setattr("cli.app.task_service.get_task", lambda tid: None)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view"])
    assert result.exit_code == 0
    assert "Task not found." in messages


def test_view_success(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.output.render_task_details", lambda task: messages.append(task["id"]))
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.get_task", lambda tid: {"id": tid})
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["view"])
    assert result.exit_code == 0
    assert messages == ["abc"]


def test_complete_success(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.task_service.mark_complete", lambda tid: True)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["complete"])
    assert result.exit_code == 0
    assert "Marked complete" in messages


def test_complete_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    monkeypatch.setattr("cli.app.task_service.mark_complete", lambda tid: False)
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["complete"])
    assert result.exit_code == 0
    assert "Task not found." in messages


def test_update_no_selection(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: None)
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    result = CliRunner().invoke(cli_app.app, ["update"])
    assert result.exit_code == 0
    assert "No task selected." in messages


def test_complete_no_selection(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: None)
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    result = CliRunner().invoke(cli_app.app, ["complete"])
    assert result.exit_code == 0
    assert "No task selected." in messages


def test_menu_prompt_failure(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.prompt_select", lambda msg, choices: (_ for _ in ()).throw(Exception("fail")))
    monkeypatch.setattr("cli.app.output.render_cancelled", lambda msg: messages.append(msg))
    cli_app.menu()
    assert "Goodbye" in messages


def test_update_success(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.update_task", lambda *args, **kwargs: True)
    monkeypatch.setattr("cli.app.output.render_success", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["update", "--title", "New", "--priority", "low", "--notes", "n"])
    assert result.exit_code == 0
    assert "Task updated" in messages


def test_update_not_found(monkeypatch):
    messages: List[str] = []
    monkeypatch.setattr("cli.app.prompts.select_task", lambda tasks: "abc")
    monkeypatch.setattr("cli.app.task_service.update_task", lambda *args, **kwargs: False)
    monkeypatch.setattr("cli.app.output.render_error", lambda msg: messages.append(msg))
    runner = CliRunner()
    result = runner.invoke(cli_app.app, ["update"])
    assert result.exit_code == 0
    assert "Task not found." in messages
