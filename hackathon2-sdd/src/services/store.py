from __future__ import annotations

from typing import Iterable, Optional

from models.task import Status, Task


def add_task(description: str) -> Task:
    """Append a new task with a generated id (implementation pending)."""
    raise NotImplementedError


def list_tasks() -> Iterable[Task]:
    """Return all tasks in insertion order."""
    raise NotImplementedError


def update_task(task_id: int, description: str) -> Task:
    """Update description for a task with the given id."""
    raise NotImplementedError


def complete_task(task_id: int) -> Task:
    """Mark a task complete by id."""
    raise NotImplementedError


def delete_task(task_id: int) -> Optional[Task]:
    """Delete a task by id and return it if removed."""
    raise NotImplementedError
