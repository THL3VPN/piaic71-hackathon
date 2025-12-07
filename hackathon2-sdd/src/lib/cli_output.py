from __future__ import annotations

import sys
from typing import Iterable

from models.task import Task


def print_created(task: Task) -> None:
    print(f"Created task {task.id}: {task.description} [{task.status}]")


def print_updated(task: Task) -> None:
    print(f"Updated task {task.id}: {task.description} [{task.status}]")


def print_completed(task: Task, already: bool) -> None:
    if already:
        print(f"Task {task.id} is already completed")
    else:
        print(f"Completed task {task.id}: {task.description}")


def print_deleted(task_id: int) -> None:
    print(f"Deleted task {task_id}")


def print_tasks(tasks: Iterable[Task]) -> None:
    print(render_tasks_table(tasks))


def print_error(message: str) -> None:
    print(message, file=sys.stderr)


def render_tasks_table(tasks: Iterable[Task]) -> str:
    """Stub renderer for task list; Rich formatting will be added later."""
    lines = ["Tasks:"]
    for task in tasks:
        lines.append(f"- {task.id}: {task.description} [{task.status}]")
    return "\n".join(lines)


def render_error_panel(message: str) -> str:
    """Stub error panel; returns a string for now."""
    return f"ERROR: {message}"


def render_success_panel(message: str) -> str:
    """Stub success panel; returns a string for now."""
    return f"OK: {message}"
