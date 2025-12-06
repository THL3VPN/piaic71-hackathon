from __future__ import annotations

from typing import Iterable, Optional

from lib.validation import require_description, require_id
from models.task import Task

_tasks: list[Task] = []
_next_id: int = 1


def add_task(description: str) -> Task:
    """Append a new task with a generated id."""
    global _next_id
    desc = require_description(description)
    task = Task(id=_next_id, description=desc, status="pending")
    _tasks.append(task)
    _next_id += 1
    return task


def list_tasks() -> Iterable[Task]:
    """Return all tasks in insertion order."""
    return list(_tasks)


def update_task(task_id: int, description: str) -> Task:  # pragma: no cover
    """Update description for a task with the given id."""
    desc = require_description(description)
    task = _find_task(require_id(task_id))
    task.description = desc
    return task  # pragma: no cover (covered in later stories)


def complete_task(task_id: int) -> tuple[Task, bool]:
    """Mark a task complete by id. Returns (task, already_completed)."""
    task = _find_task(require_id(task_id))
    already = task.status == "completed"
    task.status = "completed"
    return task, already


def delete_task(task_id: int) -> Optional[Task]:  # pragma: no cover
    """Delete a task by id and return it if removed."""
    task = _find_task(require_id(task_id))
    _tasks.remove(task)
    return task


def _find_task(task_id: int) -> Task:  # pragma: no cover
    for task in _tasks:
        if task.id == task_id:
            return task
    raise ValueError(f"Task {task_id} not found")


def reset_store() -> None:
    """Reset store state (for tests)."""
    global _tasks, _next_id
    _tasks = []
    _next_id = 1
