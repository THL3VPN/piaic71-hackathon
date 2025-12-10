"""Rich output helpers with safe fallbacks."""
from typing import Iterable

try:  # runtime dependency optional in tests
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
except ImportError:  # pragma: no cover - fallback to None
    Console = None
    Table = None
    Panel = None


_console = Console() if Console else None


def _print(text: str):
    if _console:
        _console.print(text)
    else:  # pragma: no cover
        print(text)


def render_success(message: str):
    _print(f"[green]{message}[/green]" if _console else message)


def render_error(message: str):
    _print(f"[red]{message}[/red]" if _console else message)


def render_cancelled(message: str):
    _print(f"[yellow]{message}[/yellow]" if _console else message)


def render_task_created(task: dict):
    if Panel:
        panel = Panel.fit(
            f"Title: {task.get('title')}\nPriority: {task.get('priority')}\nStatus: {task.get('status')}\nNotes: {task.get('notes')}",
            title="Task Created",
            border_style="green",
        )
        _print(panel)
    else:  # pragma: no cover
        _print(f"Task Created: {task}")


def render_task_table(tasks: Iterable[dict]):
    data = list(tasks)
    if Table and _console:
        table = Table(title="Tasks")
        for col in ["title", "priority", "status", "due_date", "notes"]:
            table.add_column(col.title())
        if not data:
            table.add_row("No tasks", "-", "-", "-", "-" )
        else:
            for t in data:
                table.add_row(
                    str(t.get("title", "")),
                    str(t.get("priority", "")),
                    str(t.get("status", "")),
                    str(t.get("due_date", "")),
                    str(t.get("notes", "")),
                )
        _console.print(table)
    else:  # pragma: no cover
        if not data:
            _print("No tasks")
        else:
            for t in data:
                _print(f"- {t.get('title')} ({t.get('priority')}, {t.get('status')})")
