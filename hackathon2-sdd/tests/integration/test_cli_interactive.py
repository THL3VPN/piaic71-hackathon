from __future__ import annotations

from cli import interactive
from conftest import run_cli
from services import store


def test_interactive_add_and_view_flow(monkeypatch, capsys) -> None:
    store.reset_store()
    actions = iter(["add", "view", "exit"])
    descriptions = iter(["walk dog"])

    class FakeSelect:
        def __init__(self, iterator):
            self.iterator = iterator

        def ask(self):
            return next(self.iterator, None)

    class FakeText:
        def __init__(self, iterator):
            self.iterator = iterator

        def ask(self):
            return next(self.iterator, None)

    class FakeQuestionary:
        def select(self, *_args, **_kwargs):
            return FakeSelect(actions)

        def text(self, *_args, **_kwargs):
            return FakeText(descriptions)

    monkeypatch.setattr(interactive, "questionary", FakeQuestionary())
    monkeypatch.setattr(
        interactive,
        "render_tasks_table",
        lambda tasks: "Tasks:\n" + "\n".join(task.description for task in tasks),
    )
    monkeypatch.setattr(
        interactive, "render_success_panel", lambda message: f"OK: {message}"
    )
    monkeypatch.setattr(
        interactive, "render_error_panel", lambda message: f"ERROR: {message}"
    )

    code, stdout, stderr = run_cli(["interactive"])

    assert code == 0
    assert "Tasks:" in stdout
    assert "walk dog" in stdout
    assert stderr == ""
