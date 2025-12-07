from __future__ import annotations

import pytest

from services import store


def test_update_task_changes_description_retains_status():
    created = store.add_task("Buy milk")
    updated = store.update_task(created.id, "Buy oat milk")
    assert updated.description == "Buy oat milk"
    assert updated.status == "pending"


def test_update_task_rejects_empty_description():
    created = store.add_task("Task")
    with pytest.raises(ValueError):
        store.update_task(created.id, "   ")
