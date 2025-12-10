from services import task_service


def test_create_task_stub():
    task = task_service.create_task("t", "high", "n", None)
    assert task["title"] == "t"
    assert task["priority"] == "high"
    assert task["status"] == "pending"


def test_list_tasks_filters():
    tasks = task_service.list_tasks(priority="high", status="pending")
    assert tasks
    assert all(t["priority"] == "high" for t in tasks)
    assert all(t["status"] == "pending" for t in tasks)


def test_list_tasks_no_filters():
    tasks = task_service.list_tasks()
    assert tasks


def test_get_and_delete_task():
    task = task_service.create_task("keep", "medium", "")
    found = task_service.get_task(task["id"])
    assert found and found["title"] == "keep"
    assert task_service.delete_task(task["id"]) is True
    assert task_service.get_task(task["id"]) is None


def test_delete_task_missing():
    assert task_service.delete_task("does-not-exist") is False


def test_list_tasks_seed(monkeypatch):
    monkeypatch.setattr(task_service, "_TASKS", [])
    tasks = task_service.list_tasks()
    assert tasks  # seeded sample


def test_list_tasks_status_filter(monkeypatch):
    monkeypatch.setattr(task_service, "_TASKS", [])
    task_service.create_task("a", "low", "", None)
    task_service.create_task("b", "low", "", None)
    tasks = task_service.list_tasks(status="done")
    assert tasks == []


def test_update_task_missing():
    assert task_service.update_task("none", title="x") is False


def test_mark_complete_missing():
    assert task_service.mark_complete("none") is False


def test_mark_complete_and_update():
    task = task_service.create_task("c", "low", "n", None)
    assert task_service.mark_complete(task["id"]) is True
    updated = task_service.update_task(task["id"], title="new", priority="high", notes="u")
    assert updated is True
    fetched = task_service.get_task(task["id"])
    assert fetched["title"] == "new"
    assert fetched["priority"] == "high"
    assert fetched["status"] == "done"
