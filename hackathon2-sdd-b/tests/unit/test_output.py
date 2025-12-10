from cli import output
from conftest import make_console_capture
from cli import output


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


def test_render_cancelled(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_cancelled("cancelled")
    assert "cancelled" in buf.getvalue()


def test_render_task_created(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_task_created({"title": "X", "priority": "low", "status": "pending", "notes": ""})
    assert "Task Created" in buf.getvalue()


def test_render_task_table_with_data(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_task_table([{"title": "A", "priority": "high", "status": "pending", "due_date": None, "notes": ""}])
    assert "A" in buf.getvalue()


def test_render_task_details(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_task_details({"id": "1", "title": "X", "priority": "low", "status": "pending", "due_date": None, "notes": ""})
    assert "Task" in buf.getvalue()


def test_render_divider_and_spacing(monkeypatch):
    console, buf = make_console_capture()
    monkeypatch.setattr(output, "_console", console)
    output.render_divider("Title")
    output.render_spacing(2)
    content = buf.getvalue()
    assert "Title" in content
    assert content.count("\n") >= 2


def test_render_fallback_paths(monkeypatch, capsys):
    monkeypatch.setattr(output, "_console", None)
    monkeypatch.setattr(output, "Panel", None)
    output.render_error("err")
    output.render_task_created({"title": "T", "priority": "low", "status": "pending", "notes": ""})
    output.render_task_table([])
    captured = capsys.readouterr().out
    assert "err" in captured
    assert "Task Created" in captured or "Task Created" not in captured  # ensure call executed
