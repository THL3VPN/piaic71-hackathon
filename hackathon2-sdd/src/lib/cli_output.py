from __future__ import annotations

import io
import sys
from typing import Iterable

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models.task import Task


def _console_buffer() -> tuple[Console, io.StringIO]:
    buffer = io.StringIO()
    console = Console(file=buffer, force_terminal=True, color_system=None, width=80)
    return console, buffer


def print_created(task: Task) -> None:
    print(render_success_panel(f"Created task {task.id}: {task.description} [{task.status}]"))


def print_updated(task: Task) -> None:
    print(render_success_panel(f"Updated task {task.id}: {task.description} [{task.status}]"))


def print_completed(task: Task, already: bool) -> None:
    if already:
        print(render_success_panel(f"Task {task.id} is already completed"))
    else:
        print(render_success_panel(f"Completed task {task.id}: {task.description}"))


def print_deleted(task_id: int) -> None:
    print(render_success_panel(f"Deleted task {task_id}"))


def print_tasks(tasks: Iterable[Task]) -> None:
    print(render_tasks_table(tasks))


def print_error(message: str) -> None:
    print(render_error_panel(message), file=sys.stderr)


def render_tasks_table(tasks: Iterable[Task]) -> str:
    """Render a Rich table to a string while keeping a plain header for tests."""
    console, buffer = _console_buffer()
    table = Table(title="Tasks", box=None, show_header=True, pad_edge=False)
    table.add_column("ID", justify="right")
    table.add_column("Description", overflow="fold")
    table.add_column("Status")
    for task in tasks:
        table.add_row(str(task.id), task.description, task.status)
    console.print(table)
    rendered = buffer.getvalue().rstrip()
    return "Tasks:\n" + rendered


def render_error_panel(message: str) -> str:
    """Render an error panel to string with a clear prefix."""
    console, buffer = _console_buffer()
    console.print(Panel(message, title="Error", border_style="red"))
    rendered = buffer.getvalue().rstrip()
    return f"ERROR: {message}\n{rendered}"


def render_success_panel(message: str) -> str:
    """Render a success panel to string with a clear prefix."""
    console, buffer = _console_buffer()
    console.print(Panel(message, title="OK", border_style="green"))
    rendered = buffer.getvalue().rstrip()
    return f"OK: {message}\n{rendered}"
