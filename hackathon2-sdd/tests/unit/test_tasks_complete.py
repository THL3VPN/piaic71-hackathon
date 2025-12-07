from __future__ import annotations

from services import store


def test_complete_task_marks_completed():
    created = store.add_task("Buy milk")
    task, already = store.complete_task(created.id)
    assert task.status == "completed"
    assert already is False


def test_complete_task_idempotent():
    created = store.add_task("Buy milk")
    store.complete_task(created.id)
    task, already = store.complete_task(created.id)
    assert task.status == "completed"
    assert already is True
