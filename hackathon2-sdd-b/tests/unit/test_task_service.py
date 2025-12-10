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
