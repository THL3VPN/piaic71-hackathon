import pytest

from cli import prompts


def test_collect_task_inputs_uses_mock(monkeypatch):
    monkeypatch.setattr(prompts, "prompt_text", lambda msg: "Title A")
    monkeypatch.setattr(prompts, "prompt_select", lambda msg, choices: "high")
    monkeypatch.setattr(prompts, "prompt_confirm", lambda msg, default=True: True)

    task = prompts.collect_task_inputs(title=None, priority=None, notes=None)
    assert task["title"] == "Title A"
    assert task["priority"] == "high"
    assert task["status"] == "pending"


def test_collect_task_inputs_cancel(monkeypatch):
    monkeypatch.setattr(prompts, "prompt_text", lambda msg: "X")
    monkeypatch.setattr(prompts, "prompt_select", lambda msg, choices: "low")
    monkeypatch.setattr(prompts, "prompt_confirm", lambda msg, default=True: False)

    task = prompts.collect_task_inputs(title=None, priority=None, notes=None)
    assert task is None


def test_stub_list_tasks_filters():
    sample = prompts.stub_list_tasks(priority="high", status="pending")
    assert all(t["priority"] == "high" for t in sample)
    assert all(t["status"] == "pending" for t in sample)


def test_prompt_helpers_use_questionary(monkeypatch):
    class FakePrompt:
        def __init__(self, value):
            self.value = value
        def ask(self):
            return self.value
    class FakeQuestionary:
        def text(self, msg):
            return FakePrompt("txt")
        def select(self, msg, choices):
            return FakePrompt("sel")
        def confirm(self, msg, default=True):
            return FakePrompt(True)
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary())
    assert prompts.prompt_text("m") == "txt"
    assert prompts.prompt_select("m", ["a"]) == "sel"
    assert prompts.prompt_confirm("m") is True


def test_select_task_with_choices(monkeypatch):
    class FakePrompt:
        def __init__(self, value):
            self.value = value
        def ask(self):
            return self.value
    class FakeQuestionary:
        class Choice:
            def __init__(self, title, value):
                self.title = title
                self.value = value
        def select(self, msg, choices):
            return FakePrompt("id-1")
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary())
    task_id = prompts.select_task([{"id": "id-1", "title": "T1", "status": "pending"}])
    assert task_id == "id-1"


def test_select_task_empty_list_returns_none():
    assert prompts.select_task([]) is None


def test_prompt_optional_text_keeps_current(monkeypatch):
    class FakePrompt:
        def ask(self):
            return ""
    class FakeQuestionary:
        def text(self, msg):
            return FakePrompt()
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary())
    assert prompts.prompt_optional_text("Title", "Current") == "Current"


def test_prompt_priority_back(monkeypatch):
    class FakePrompt:
        def __init__(self, value):
            self.value = value
        def ask(self):
            return self.value
    class FakeQuestionary:
        def select(self, msg, choices):
            return FakePrompt("Back")
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary())
    assert prompts.prompt_priority("medium") == "medium"


def test_prompt_priority_change(monkeypatch):
    class FakePrompt:
        def __init__(self, value):
            self.value = value
        def ask(self):
            return self.value
    class FakeQuestionary:
        def select(self, msg, choices):
            return FakePrompt("high")
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary())
    assert prompts.prompt_priority("medium") == "high"


def test_menu_choice_with_questionary(monkeypatch):
    class FakeChoice:
        def __init__(self, title=None, value=None, shortcut_key=None):
            self.title = title
            self.value = value
            self.shortcut_key = shortcut_key
    class FakeQuestionary:
        Choice = FakeChoice
    monkeypatch.setattr(prompts, "questionary", FakeQuestionary)
    choice = prompts.menu_choice("Add", "add", "a")
    assert isinstance(choice, FakeChoice)
    assert choice.value == "add"


def test_menu_choice_without_questionary(monkeypatch):
    monkeypatch.setattr(prompts, "questionary", None)
    assert prompts.menu_choice("Add", "add", "a") == "add"


def test_prompt_unavailable(monkeypatch):
    monkeypatch.setattr(prompts, "questionary", None)
    with pytest.raises(prompts.PromptUnavailable):
        prompts.prompt_text("m")


def test_collect_task_inputs_skips_prompts_when_provided(monkeypatch):
    # ensure branches where title/priority/notes are already provided
    monkeypatch.setattr(prompts, "prompt_confirm", lambda msg, default=True: True)
    task = prompts.collect_task_inputs(title=" t ", priority=" high ", notes=" n ")
    assert task["title"] == "t"
    assert task["priority"] == "high"
    assert task["notes"] == "n"


def test_confirm_action(monkeypatch):
    called = []
    monkeypatch.setattr(prompts, "prompt_confirm", lambda msg, default=False: called.append((msg, default)) or True)
    assert prompts.confirm_action("confirm?", default=False) is True
    assert called == [("confirm?", False)]


def test_stub_list_tasks_status_only():
    tasks = prompts.stub_list_tasks(priority=None, status="pending")
    assert all(t["status"] == "pending" for t in tasks)
