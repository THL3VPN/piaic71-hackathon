from __future__ import annotations

from services import store


def test_view_tasks_lists_all_with_status():
    store.add_task("Buy milk")
    store.add_task("Do laundry")
    tasks = list(store.list_tasks())
    assert len(tasks) == 2
    assert tasks[0].description == "Buy milk"
    assert tasks[0].status == "pending"
    assert tasks[1].description == "Do laundry"


def test_view_tasks_when_empty_returns_empty_list():
    tasks = list(store.list_tasks())
    assert tasks == []
