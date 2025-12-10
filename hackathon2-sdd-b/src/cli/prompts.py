"""Questionary prompt helpers with safe fallbacks for testing."""
from typing import Any, Dict, Optional

try:  # runtime dependency optional in tests
    import questionary
except ImportError:  # pragma: no cover - handled in tests via monkeypatch
    questionary = None


class PromptUnavailable(Exception):
    """Raised when prompts cannot be used (e.g., missing questionary)."""


def _require_questionary():
    if questionary is None:
        raise PromptUnavailable("Questionary not installed")


def prompt_text(message: str) -> str:
    _require_questionary()
    return questionary.text(message).ask()  # type: ignore[union-attr]


def prompt_select(message: str, choices: list[str]) -> str:
    _require_questionary()
    return questionary.select(message, choices=choices).ask()  # type: ignore[union-attr]


def prompt_confirm(message: str, default: bool = True) -> bool:
    _require_questionary()
    return bool(questionary.confirm(message, default=default).ask())  # type: ignore[union-attr]


def collect_task_inputs(title: Optional[str], priority: Optional[str], notes: Optional[str]) -> Optional[Dict[str, Any]]:
    """Interactive collection with defaults; returns None if cancelled."""
    if title is None:
        title = prompt_text("Title")
    if priority is None:
        priority = prompt_select("Priority", ["low", "medium", "high"])
    if notes is None:
        notes = prompt_text("Notes (optional)") or ""
    confirm = prompt_confirm("Create task?", default=True)
    if not confirm:
        return None
    return {
        "title": title.strip(),
        "priority": priority.strip(),
        "notes": notes.strip(),
        "status": "pending",
    }


def confirm_action(message: str, default: bool = False) -> bool:
    return prompt_confirm(message, default=default)


def stub_list_tasks(priority: Optional[str], status: Optional[str]):
    """Temporary stub for list command until storage wired."""
    # In absence of storage, return sample filtered data
    sample = [
        {"title": "Sample Task", "priority": "high", "status": "pending", "due_date": None, "notes": ""}
    ]
    if priority:
        sample = [t for t in sample if t["priority"] == priority]
    if status:
        sample = [t for t in sample if t["status"] == status]
    return sample


def select_task(tasks: list[dict]) -> Optional[str]:
    """Return selected task id or None if cancelled."""
    if not tasks:
        return None
    _require_questionary()
    choices = [
        questionary.Choice(f"{idx+1}. {t.get('title')} ({t.get('status')})", value=t.get("id"))
        for idx, t in enumerate(tasks)
    ]  # type: ignore[attr-defined]
    return questionary.select("Choose a task", choices=choices).ask()  # type: ignore[union-attr]
