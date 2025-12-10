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


def render_spacing(lines: int = 1):
    for _ in range(lines):
        _print("")


def render_divider(title: str = ""):
    if _console:
        _console.rule(f"[bold cyan]{title}[/bold cyan]" if title else "")
    else:  # pragma: no cover
        _print("-" * 20)


def render_info(message: str):
    _print(f"[cyan]{message}[/cyan]" if _console else message)
    render_spacing()


def render_success(message: str):
    _print(f"[green]{message}[/green]" if _console else message)
    render_spacing()


def render_error(message: str):
    _print(f"[red]{message}[/red]" if _console else message)
    render_spacing()


def render_cancelled(message: str):
    _print(f"[yellow]{message}[/yellow]" if _console else message)
    render_spacing()


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
    render_spacing()


def render_task_details(task: dict):
    if Panel:
        panel = Panel.fit(
            f"Title: {task.get('title')}\nPriority: {task.get('priority')}\nStatus: {task.get('status')}\nDue: {task.get('due_date')}\nNotes: {task.get('notes')}",
            title=f"Task {task.get('id')}",
            border_style="cyan",
        )
        _print(panel)
    else:  # pragma: no cover
        _print(f"Task: {task}")
    render_spacing()


def render_task_table(tasks: Iterable[dict]):
    data = list(tasks)
    render_spacing()
    render_divider("Task List")
    if Table and _console:
        table = Table(title="Tasks")
        for col in ["#", "title", "priority", "status", "due_date", "notes"]:
            table.add_column(col.title())
        if not data:
            table.add_row("-", "No tasks", "-", "-", "-", "-" )
        else:
            for idx, t in enumerate(data, start=1):
                table.add_row(
                    str(idx),
                    str(t.get("title", "")),
                    str(t.get("priority", "")),
                    f"[green]{t.get('status', '')}[/green]" if str(t.get("status", "")).lower() == "done" else str(t.get("status", "")),
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
    render_spacing()
