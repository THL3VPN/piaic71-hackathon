from typer.testing import CliRunner

from cli.app import app


def test_menu_end_to_end(monkeypatch):
    calls = []

    def fake_select(msg, choices):
        calls.append("menu")
        return "quit"

    monkeypatch.setattr("cli.app.prompts.prompt_select", fake_select)
    result = CliRunner().invoke(app, ["menu"])
    assert result.exit_code == 0
    assert calls == ["menu"]
