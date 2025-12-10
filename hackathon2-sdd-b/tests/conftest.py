"""Test helpers for CLI."""
from io import StringIO
from typing import Any, Dict

import pytest

try:
    from rich.console import Console
except ImportError:  # pragma: no cover
    Console = None


def make_console_capture():
    """Return console and buffer for capturing rich output."""
    buf = StringIO()
    if Console:
        console = Console(file=buf, force_terminal=True, color_system=None)
    else:  # pragma: no cover
        class Dummy:
            def print(self, *args, **kwargs):
                print(*args, file=buf)
        console = Dummy()
    return console, buf


@pytest.fixture()
def questionary_mock(monkeypatch):
    """Provide a minimal Questionary mock with preset responses."""
    calls: Dict[str, Any] = {}

    class Prompt:
        def __init__(self, name):
            self.name = name
        def ask(self):  # noqa: D401
            return calls.get(self.name)

    class FakeQuestionary:
        def __init__(self):
            self.calls = calls
        def text(self, message):
            self.calls['text_message'] = message
            return Prompt('text')
        def select(self, message, choices):
            self.calls['select_message'] = message
            self.calls['choices'] = choices
            return Prompt('select')
        def confirm(self, message, default=True):
            self.calls['confirm_message'] = message
            self.calls['confirm_default'] = default
            return Prompt('confirm')

    fake = FakeQuestionary()
    monkeypatch.setitem(__import__('sys').modules, 'questionary', fake)
    return fake
