"""Typer application entrypoint for interactive CLI UX."""
from typing import Optional

import typer

from . import prompts, output, errors
from services import task_service

app = typer.Typer(help="Interactive CLI for tasks")

ALLOWED_PRIORITIES = {"low", "medium", "high"}


def _validate_priority(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    val = value.strip().lower()
    if val not in ALLOWED_PRIORITIES:
        raise errors.UserInputError(
            f"Priority must be one of {sorted(ALLOWED_PRIORITIES)}. Try again."
        )
    return val


@app.callback()
def main():
    """Root command placeholder."""


@app.command()
def add(
    title: Optional[str] = typer.Option(None),
    priority: Optional[str] = typer.Option(None),
    notes: Optional[str] = typer.Option(None),
):
    """Add a task interactively or via flags."""
    try:
        priority = _validate_priority(priority)
        task_input = prompts.collect_task_inputs(
            title=title, priority=priority, notes=notes
        )
        if not task_input:
            output.render_cancelled("Task creation cancelled")
            return
        created = task_service.create_task(
            title=task_input["title"],
            priority=task_input["priority"],
            notes=task_input.get("notes", ""),
            due_date=task_input.get("due_date"),
        )
        output.render_task_created(created)
    except errors.UserInputError as exc:
        output.render_error(errors.format_error(str(exc)))


@app.command()
def list(priority: Optional[str] = typer.Option(None), status: Optional[str] = typer.Option(None)):
    """List tasks with optional filters."""
    try:
        priority = _validate_priority(priority)
    except errors.UserInputError as exc:
        output.render_error(errors.format_error(str(exc)))
        return

    tasks = task_service.list_tasks(priority=priority, status=status)
    output.render_task_table(tasks)


@app.command()
def view(task_id: Optional[str] = typer.Option(None)):
    """Show task details."""
    if not task_id:
        output.render_error("Please provide a task id (use list to find one).")
        return
    task = task_service.get_task(task_id)
    if not task:
        output.render_error("Task not found.")
        return
    output.render_task_details(task)


@app.command()
def delete(task_id: Optional[str] = typer.Option(None), force: bool = typer.Option(False)):
    """Delete a task by id."""
    if not task_id:
        output.render_error("Please provide a task id (use list to find one).")
        return
    if not force:
        confirm = prompts.confirm_action("Delete task?", default=False)
        if not confirm:
            output.render_cancelled("Deletion cancelled")
            return
    deleted = task_service.delete_task(task_id)
    if deleted:
        output.render_success("Deleted task")
    else:
        output.render_error("Task not found.")


@app.command()
def menu():
    """Interactive menu to choose CLI action."""
    choice = prompts.prompt_select("What do you want to do?", ["add", "list", "delete", "quit"])
    if choice == "add":
        add()
    elif choice == "list":
        list()
    elif choice == "delete":
        delete()
    else:
        output.render_cancelled("Goodbye")


def run():  # pragma: no cover - convenience wrapper
    app()


if __name__ == "__main__":  # pragma: no cover
    run()
