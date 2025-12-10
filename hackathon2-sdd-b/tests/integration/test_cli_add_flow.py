from typer.testing import CliRunner

from cli.app import app


def test_add_flow_success(monkeypatch):
    runner = CliRunner()

    def fake_collect(title=None, priority=None, notes=None):
        return {"title": "Flow Task", "priority": "medium", "notes": "", "status": "pending"}

    outputs = []

    def fake_render(task):
        outputs.append(task)

    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", fake_collect)
    monkeypatch.setattr("cli.app.output.render_task_created", fake_render)

    result = runner.invoke(app, ["add"])
    assert result.exit_code == 0
    assert outputs and outputs[0]["title"] == "Flow Task"


def test_add_flow_cancel(monkeypatch):
    runner = CliRunner()

    def fake_collect(title=None, priority=None, notes=None):
        return None  # simulate cancel

    messages = []

    def fake_cancel(msg):
        messages.append(msg)

    monkeypatch.setattr("cli.app.prompts.collect_task_inputs", fake_collect)
    monkeypatch.setattr("cli.app.output.render_cancelled", fake_cancel)

    result = runner.invoke(app, ["add"])
    assert result.exit_code == 0
    assert messages == ["Task creation cancelled"]
