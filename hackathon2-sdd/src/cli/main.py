"""Placeholder CLI entrypoint for the todo app."""

from __future__ import annotations

import argparse
from typing import Sequence

from lib import cli_output
from lib.validation import parse_task_id, require_description
from cli import interactive
from services import store


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="CLI todo application", add_help=True)
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_cmd = subparsers.add_parser("add", help="Add a new task")
    add_cmd.add_argument("--description", required=True)

    subparsers.add_parser("view", help="View all tasks")

    update_cmd = subparsers.add_parser("update", help="Update a task description")
    update_cmd.add_argument("--id", required=True)
    update_cmd.add_argument("--description", required=True)

    complete_cmd = subparsers.add_parser("complete", help="Mark a task complete")
    complete_cmd.add_argument("--id", required=True)

    delete_cmd = subparsers.add_parser("delete", help="Delete a task")
    delete_cmd.add_argument("--id", required=True)

    subparsers.add_parser("interactive", help="Run interactive mode")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit:
        # argparse already printed usage; treat as error exit
        return 1

    try:
        if args.command == "add":
            task = store.add_task(require_description(args.description))
            cli_output.print_created(task)
            return 0

        if args.command == "view":
            tasks = list(store.list_tasks())
            if not tasks:
                print("No tasks yet.")
                return 0
            cli_output.print_tasks(tasks)
            return 0

        if args.command == "update":
            task_id = parse_task_id(args.id)
            task = store.update_task(task_id, require_description(args.description))
            cli_output.print_updated(task)
            return 0

        if args.command == "complete":
            task_id = parse_task_id(args.id)
            task, already = store.complete_task(task_id)
            cli_output.print_completed(task, already)
            return 0

        if args.command == "delete":  # pragma: no cover
            task_id = parse_task_id(args.id)
            store.delete_task(task_id)
            cli_output.print_deleted(task_id)
            return 0  # pragma: no cover (covered in later stories)

        if args.command == "interactive":  # pragma: no cover
            interactive.run_interactive(store)
            return 0

    except ValueError as exc:
        cli_output.print_error(str(exc))
        return 1

    return 1  # pragma: no cover


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
