from __future__ import annotations

import pytest

from services import store


def test_delete_task_removes_and_returns_task():
    first = store.add_task("Buy milk")
    second = store.add_task("Do laundry")
    removed = store.delete_task(first.id)
    assert removed.id == first.id
    remaining = list(store.list_tasks())
    assert len(remaining) == 1
    assert remaining[0].id == second.id


def test_delete_task_missing_id_raises():
    with pytest.raises(ValueError):
        store.delete_task(99)
