from __future__ import annotations

import pytest

from models.task import Task
from services import store


def test_add_task_assigns_monotonic_id_and_pending_status():
    task = store.add_task("Buy milk")
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.description == "Buy milk"
    assert task.status == "pending"


def test_add_task_trims_and_rejects_empty_description():
    with pytest.raises(ValueError):
        store.add_task("   ")
