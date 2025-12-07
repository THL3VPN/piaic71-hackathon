from __future__ import annotations

from cli.main import build_parser, main
from lib import cli_output


def test_missing_required_flag_shows_usage(capsys) -> None:
    parser = build_parser()
    try:
        parser.parse_args(["add"])
    except SystemExit:
        pass

    # argparse already printed to stderr
    captured = capsys.readouterr()
    assert "usage:" in captured.err.lower()
    assert captured.out == ""


def test_unknown_command_shows_usage(capsys) -> None:
    exit_code = main(["unknown"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "usage:" in captured.err.lower()


def test_render_error_panel_has_prefix() -> None:
    msg = "bad input"
    rendered = cli_output.render_error_panel(msg)
    assert msg in rendered
    assert rendered.startswith("ERROR:")
