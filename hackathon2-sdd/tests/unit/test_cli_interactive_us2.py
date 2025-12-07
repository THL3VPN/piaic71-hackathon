from __future__ import annotations

from typing import Iterable

import pytest

from cli import interactive
from models.task import Task
from services import store


class FakeSelect:
    def __init__(self, iterator: Iterable[str]):
        self.iterator = iterator

    def ask(self) -> str | None:
        return next(self.iterator, None)


class FakeText:
    def __init__(self, iterator: Iterable[str]):
        self.iterator = iterator

    def ask(self) -> str | None:
        return next(self.iterator, None)


class FakeQuestionary:
    def __init__(self, actions: Iterable[str], descriptions: Iterable[str]):
        self._actions = iter(actions)
        self._descriptions = iter(descriptions)

    def select(self, *_args, **_kwargs):
        return FakeSelect(self._actions)

    def text(self, *_args, **_kwargs):
        return FakeText(self._descriptions)


def test_interactive_add_and_view_flow(monkeypatch, capsys) -> None:
    store.reset_store()
    fake_q = FakeQuestionary(actions=["add", "view", "exit"], descriptions=["alpha"])
    monkeypatch.setattr(interactive, "questionary", fake_q)
    monkeypatch.setattr(
        interactive,
        "render_tasks_table",
        lambda tasks: "Tasks:\n" + "\n".join(task.description for task in tasks),
    )
    monkeypatch.setattr(
        interactive,
        "render_success_panel",
        lambda message: f"OK: {message}",
    )
    monkeypatch.setattr(
        interactive,
        "render_error_panel",
        lambda message: f"ERROR: {message}",
    )

    exit_code = interactive.run_interactive(store)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Tasks:" in captured.out
    assert "alpha" in captured.out
    assert captured.err == ""


def test_interactive_handles_cancel(monkeypatch, capsys) -> None:
    store.reset_store()
    fake_q = FakeQuestionary(actions=["exit"], descriptions=[])
    monkeypatch.setattr(interactive, "questionary", fake_q)
    monkeypatch.setattr(
        interactive,
        "render_success_panel",
        lambda message: f"OK: {message}",
    )
    monkeypatch.setattr(
        interactive,
        "render_error_panel",
        lambda message: f"ERROR: {message}",
    )
    monkeypatch.setattr(
        interactive,
        "render_tasks_table",
        lambda tasks: f"Tasks: {len(list(tasks))}",
    )

    exit_code = interactive.run_interactive(store)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == ""
    assert captured.err == ""


def test_interactive_update_complete_delete_and_error(monkeypatch, capsys) -> None:
    store.reset_store()
    store.add_task("one")
    store.add_task("two")
    actions = iter(["update", "complete", "delete", "complete", "exit"])
    texts = iter(["1", "renamed", "1", "2", "abc"])
    fake_q = FakeQuestionary(actions=actions, descriptions=texts)
    monkeypatch.setattr(interactive, "questionary", fake_q)
    monkeypatch.setattr(interactive, "render_tasks_table", lambda tasks: f"Tasks: {len(list(tasks))}")
    monkeypatch.setattr(interactive, "render_success_panel", lambda message: f"OK: {message}")
    monkeypatch.setattr(interactive, "render_error_panel", lambda message: f"ERROR: {message}")

    exit_code = interactive.run_interactive(store)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Updated task 1" in captured.out
    assert "Completed task 1" in captured.out
    assert "Deleted task 2" in captured.out or "Deleted task 2" in captured.out
    assert "ERROR: Task id must be a positive integer" in captured.err


def test_prompt_description_none_raises(monkeypatch) -> None:
    class FakeText:
        def ask(self):
            return None

    monkeypatch.setattr(interactive.questionary, "text", lambda *_args, **_kwargs: FakeText())
    with pytest.raises(ValueError):
        interactive._prompt_description()  # type: ignore[attr-defined]
