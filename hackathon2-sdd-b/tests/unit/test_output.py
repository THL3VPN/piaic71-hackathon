from cli import output
from tests.conftest import make_console_capture


def test_render_task_table_handles_empty(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_task_table([])
    assert "No tasks" in buf.getvalue()


def test_render_success_message(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_success("ok")
    assert "ok" in buf.getvalue()
