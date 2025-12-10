from typer.testing import CliRunner

from cli.app import app


def test_add_command_contract(monkeypatch):
    runner = CliRunner()
    created = {}

    def fake_collect(title=None, priority=None, notes=None):
        return {"title": "Contract Task", "priority": "high", "notes": "n", "status": "pending"}

    def fake_create(title, priority, notes="", due_date=None):
        created.update(
            {"title": title, "priority": priority, "notes": notes, "status": "pending", "id": "temp-id", "due_date": due_date}
        )
        return created

    outputs = []

    def fake_render(task):
        outputs.append(task)

    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", fake_collect)
    monkeypatch.setattr("cli.app.task_service.create_task", fake_create)
    monkeypatch.setattr("cli.app.output.render_task_created", fake_render)

    result = runner.invoke(app, ["add"])
    assert result.exit_code == 0
    assert created["title"] == "Contract Task"
    assert outputs and outputs[0]["priority"] == "high"
