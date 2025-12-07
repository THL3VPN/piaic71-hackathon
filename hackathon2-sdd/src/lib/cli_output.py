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
    for task in tasks:
        print(f"{task.id}: {task.description} [{task.status}]")


def print_error(message: str) -> None:
    print(message, file=sys.stderr)
