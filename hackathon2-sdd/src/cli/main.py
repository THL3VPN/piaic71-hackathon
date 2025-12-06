"""Placeholder CLI entrypoint for the todo app."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from lib.validation import require_description
from services import store


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="CLI todo application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_cmd = subparsers.add_parser("add", help="Add a new task")
    add_cmd.add_argument("--description", required=True)

    subparsers.add_parser("view", help="View all tasks")

    update_cmd = subparsers.add_parser("update", help="Update a task description")
    update_cmd.add_argument("--id", type=int, required=True)
    update_cmd.add_argument("--description", required=True)

    complete_cmd = subparsers.add_parser("complete", help="Mark a task complete")
    complete_cmd.add_argument("--id", type=int, required=True)

    delete_cmd = subparsers.add_parser("delete", help="Delete a task")
    delete_cmd.add_argument("--id", type=int, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            task = store.add_task(require_description(args.description))
            print(f"Created task {task.id}: {task.description} [{task.status}]")
            return 0

        if args.command == "view":
            tasks = list(store.list_tasks())
            if not tasks:
                print("No tasks yet.")
                return 0
            for task in tasks:
                print(f"{task.id}: {task.description} [{task.status}]")
            return 0

        if args.command == "update":
            task = store.update_task(args.id, require_description(args.description))
            print(f"Updated task {task.id}: {task.description} [{task.status}]")
            return 0

        if args.command == "complete":
            task, already = store.complete_task(args.id)
            if already:
                print(f"Task {task.id} is already completed")
            else:
                print(f"Completed task {task.id}: {task.description}")
            return 0

        if args.command == "delete":  # pragma: no cover
            store.delete_task(args.id)
            print(f"Deleted task {args.id}")
            return 0  # pragma: no cover (covered in later stories)

    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 1  # pragma: no cover


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
