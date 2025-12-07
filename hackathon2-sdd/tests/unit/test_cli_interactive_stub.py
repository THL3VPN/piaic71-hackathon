from __future__ import annotations

import pytest

from cli import interactive


def test_prompt_main_menu_stub_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        interactive.prompt_main_menu()


def test_run_interactive_stub_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        interactive.run_interactive(store=None)  # type: ignore[arg-type]
