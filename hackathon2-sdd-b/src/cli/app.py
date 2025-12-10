"""Typer application entrypoint for interactive CLI UX."""
import json
from pathlib import Path
from typing import Dict, Optional, Tuple

import typer

from . import prompts, output, errors
from services import task_service

app = typer.Typer(help="Interactive CLI for tasks")

ALLOWED_PRIORITIES = {"low", "medium", "high"}
_STATE_PATH = Path(__file__).resolve().parents[2] / ".cli_state.json"


def _load_state() -> Dict[str, Dict[str, Optional[str]]]:
    if _STATE_PATH.exists():
        try:
            return json.loads(_STATE_PATH.read_text())
        except json.JSONDecodeError:  # pragma: no cover - defensive
            return {"last_filter": {"priority": None, "status": None}}
    return {"last_filter": {"priority": None, "status": None}}


def _save_state(state: Dict[str, Dict[str, Optional[str]]]):
    _STATE_PATH.write_text(json.dumps(state))


def _remember_filter(priority: Optional[str], status: Optional[str]):
    state = _load_state()
    state["last_filter"] = {"priority": priority, "status": status}
    _save_state(state)


def _get_last_filter() -> Tuple[Optional[str], Optional[str]]:
    state = _load_state()
    last = state.get("last_filter", {})
    return last.get("priority"), last.get("status")


def _validate_priority(value: Optional[str]) -> Optional[str]:
    if value is None or not isinstance(value, str):
        return None
    val = value.strip().lower()
    if val not in ALLOWED_PRIORITIES:
        raise errors.UserInputError(
            f"Priority must be one of {sorted(ALLOWED_PRIORITIES)}. Try again."
        )
    return val


def _coerce_arg(value: Optional[str]) -> Optional[str]:
    return value if isinstance(value, str) else None


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
        title = _coerce_arg(title)
        priority = _validate_priority(_coerce_arg(priority))
        notes = _coerce_arg(notes)
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
def list(
    priority: Optional[str] = typer.Option(None),
    status: Optional[str] = typer.Option(None),
    display_label: Optional[str] = typer.Option(None, hidden=True),
):
    """List tasks with optional filters."""
    try:
        priority = _validate_priority(_coerce_arg(priority))
        status = _coerce_arg(status)
    except errors.UserInputError as exc:
        output.render_error(errors.format_error(str(exc)))
        return

    tasks = task_service.list_tasks(priority=priority, status=status)
    if display_label:
        output.render_info(display_label)
    pending = len([t for t in tasks if str(t.get("status")).lower() != "done"])
    done = len(tasks) - pending
    summary = f"{len(tasks)} total • {pending} pending • {done} done"
    if priority:
        summary += f" • priority={priority}"
    if status:
        summary += f" • status={status}"
    output.render_info(summary)
    output.render_task_table(tasks)


@app.command()
def view(task_id: Optional[str] = typer.Option(None)):
    """Show task details."""
    task_id = _coerce_arg(task_id)
    if not task_id:
        output.render_task_table(task_service.list_tasks())
        return
    task = task_service.get_task(task_id)
    if not task:
        output.render_error("Task not found.")
        return
    output.render_task_details(task)


@app.command()
def delete(task_id: Optional[str] = typer.Option(None), force: bool = typer.Option(False)):
    """Delete a task by id."""
    tasks = task_service.list_tasks()
    task_id = _coerce_arg(task_id) or prompts.select_task(tasks)
    if not task_id:
        output.render_cancelled("No task selected.")
        return
    if not force:
        confirm = prompts.confirm_action("Delete task?", default=False)
        if not confirm:
            output.render_cancelled("Deletion cancelled")
            return
    deleted = task_service.delete_task(task_id)
    if deleted:
        output.render_success("Deleted task")
        output.render_info("Task removed from list.")
    else:
        output.render_error("Task not found.")


@app.command()
def update(
    task_id: Optional[str] = typer.Option(None),
    title: Optional[str] = typer.Option(None),
    priority: Optional[str] = typer.Option(None),
    notes: Optional[str] = typer.Option(None),
):
    """Update task details."""
    tasks = task_service.list_tasks()
    task_id = _coerce_arg(task_id) or prompts.select_task(tasks)
    if not task_id:
        output.render_cancelled("No task selected.")
        return
    existing = task_service.get_task(task_id)
    if not existing:
        output.render_error("Task not found.")
        return
    priority = _validate_priority(_coerce_arg(priority))
    title = _coerce_arg(title)
    notes = _coerce_arg(notes)
    if title is None:
        title = prompts.prompt_optional_text("Title", existing.get("title", ""))
    if priority is None:
        priority = _validate_priority(prompts.prompt_priority(existing.get("priority", "low")))
    if notes is None:
        notes = prompts.prompt_optional_text("Notes", existing.get("notes", ""))
    output.render_info(
        f"Preview changes: Title '{existing.get('title','')}' → '{title}', "
        f"Priority {existing.get('priority','')} → {priority}, Notes length {len(notes or '')}"
    )
    if not prompts.confirm_action("Save updates?", default=True):
        output.render_cancelled("Update cancelled")
        return
    if task_service.update_task(task_id, title=title, priority=priority, notes=notes):
        output.render_success(f"Task updated: {title}")
    else:
        output.render_error("Task not found.")


@app.command()
def complete(task_id: Optional[str] = typer.Option(None)):
    """Mark a task as complete."""
    tasks = task_service.list_tasks()
    task_id = _coerce_arg(task_id) or prompts.select_task(tasks)
    if not task_id:
        output.render_cancelled("No task selected.")
        return
    if task_service.mark_complete(task_id):
        output.render_success("Marked complete")
        output.render_info("Great job! Task status is now done.")
    else:
        output.render_error("Task not found.")


def _choose_filters_for_view() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    last_priority, last_status = _get_last_filter()
    try:
        choice = prompts.prompt_select(
            "Choose a view",
            [
                "All tasks",
                "Pending only",
                "Done only",
                "Priority: high",
                "Priority: medium",
                "Priority: low",
                "Use last filter",
                "Back",
            ],
        )
    except Exception:
        return None, None, None

    label = "All tasks"
    priority = None
    status = None
    if choice == "All tasks":
        label = "Showing all tasks"
    elif choice == "Pending only":
        status = "pending"
        label = "Pending tasks"
    elif choice == "Done only":
        status = "done"
        label = "Completed tasks"
    elif choice.startswith("Priority"):
        priority = choice.split(":")[1].strip()
        label = f"Priority {priority}"
    elif choice == "Use last filter":
        priority = last_priority
        status = last_status
        label = "Last used filter"
    else:
        return None, None, None
    _remember_filter(priority, status)
    return priority, status, label


@app.command()
def menu():
    """Interactive menu to choose CLI action."""
    while True:
        try:
            output.render_divider("Main Menu")
            output.render_info("Shortcuts: [a]dd, [d]elete, [u]pdate, [v]iew, [c]omplete, [q]uit")
            choice = prompts.prompt_select(
                "Select an option",
                [
                    "Add Task [a] – Create new todo items",
                    "Delete Task [d] – Remove tasks from the list",
                    "Update Task [u] – Modify existing task details",
                    "View Task List [v] – Display all tasks",
                    "Mark as Complete [c] – Toggle task completion status",
                    "Quit [q]",
                ],
            )
        except Exception:
            output.render_cancelled("Goodbye")
            break
        if choice.startswith("Add Task"):
            add()
            output.render_spacing()
        elif choice.startswith("Delete Task"):
            delete()
            output.render_spacing()
        elif choice.startswith("Update Task"):
            update()
            output.render_spacing()
        elif choice.startswith("View Task List"):
            priority, status, label = _choose_filters_for_view()
            if label:
                list(priority=priority, status=status, display_label=label)
            output.render_spacing()
        elif choice.startswith("Mark as Complete"):
            complete()
            output.render_spacing()
        else:
            output.render_cancelled("Goodbye")
            break


def run():  # pragma: no cover - convenience wrapper
    app()


if __name__ == "__main__":  # pragma: no cover
    run()
