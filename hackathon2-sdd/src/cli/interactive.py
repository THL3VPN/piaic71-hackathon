from __future__ import annotations

import sys
from typing import Any

import questionary
from questionary import Choice

from lib.cli_output import render_error_panel, render_success_panel, render_tasks_table
from lib.validation import parse_task_id, require_description

MENU_CHOICES = [
    Choice(title="Add task", value="add"),
    Choice(title="View tasks", value="view"),
    Choice(title="Update task", value="update"),
    Choice(title="Complete task", value="complete"),
    Choice(title="Delete task", value="delete"),
    Choice(title="Exit", value="exit"),
]


def prompt_main_menu() -> str | None:
    choice = questionary.select("Choose an action", choices=MENU_CHOICES).ask()
    return str(choice) if choice is not None else None


def _prompt_description(prompt: str = "Task description") -> str:
    answer = questionary.text(prompt).ask()
    if answer is None:
        raise ValueError("Description cannot be empty")
    return require_description(answer)


def _prompt_task_id(prompt: str = "Task id") -> int:
    answer = questionary.text(prompt).ask()
    return parse_task_id(answer)


def run_interactive(store: Any) -> int:
    """Interactive CLI loop using Questionary prompts and Rich-rendered output."""
    while True:
        action = prompt_main_menu()
        if action in (None, "exit"):
            return 0
        try:
            if action == "add":
                desc = _prompt_description()
                task = store.add_task(desc)
                print(render_success_panel(f"Created task {task.id}: {task.description}"))
            elif action == "view":
                tasks = list(store.list_tasks())
                print(render_tasks_table(tasks))
            elif action == "update":
                task_id = _prompt_task_id()
                desc = _prompt_description("New description")
                task = store.update_task(task_id, desc)
                print(render_success_panel(f"Updated task {task.id}: {task.description}"))
            elif action == "complete":
                task_id = _prompt_task_id()
                task, already = store.complete_task(task_id)
                status = "already completed" if already else "Completed"
                print(render_success_panel(f"{status} task {task.id}: {task.description}"))
            elif action == "delete":
                task_id = _prompt_task_id()
                store.delete_task(task_id)
                print(render_success_panel(f"Deleted task {task_id}"))
        except ValueError as exc:
            print(render_error_panel(str(exc)), file=sys.stderr)
