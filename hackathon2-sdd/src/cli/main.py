"""Placeholder CLI entrypoint for the todo app."""

from __future__ import annotations

import argparse
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="CLI todo application")
    subparsers = parser.add_subparsers(dest="command")
    # Subcommands will be wired during implementation.
    subparsers.add_parser("add")
    subparsers.add_parser("view")
    subparsers.add_parser("update")
    subparsers.add_parser("complete")
    subparsers.add_parser("delete")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    # Placeholder behavior until implementation tasks wire real actions.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
