from __future__ import annotations

from cli.main import build_parser


def test_parser_includes_interactive_command() -> None:
    parser = build_parser()
    args = parser.parse_args(["interactive"])
    assert args.command == "interactive"
