"""In-memory task service for interactive CLI."""
from typing import Any, Dict, List, Optional
from uuid import uuid4

_TASKS: List[Dict[str, Any]] = []


def _match(task: Dict[str, Any], priority: Optional[str], status: Optional[str]) -> bool:
    if priority and task.get("priority") != priority:
        return False
    if status and task.get("status") != status:
        return False
    return True


def create_task(title: str, priority: str, notes: str = "", due_date: Optional[str] = None) -> Dict[str, Any]:
    task = {
        "id": str(uuid4()),
        "title": title,
        "priority": priority,
        "notes": notes,
        "status": "pending",
        "due_date": due_date,
    }
    _TASKS.append(task)
    return task


def list_tasks(priority: Optional[str] = None, status: Optional[str] = None) -> List[Dict[str, Any]]:
    if not _TASKS:
        # seed with a sample for demonstration
        create_task("Sample Task", "high", "", None)
    return [t for t in _TASKS if _match(t, priority, status)]


def get_task(task_id: str) -> Optional[Dict[str, Any]]:
    for task in _TASKS:
        if task.get("id") == task_id:
            return task
    return None


def delete_task(task_id: str) -> bool:
    global _TASKS
    before = len(_TASKS)
    _TASKS = [t for t in _TASKS if t.get("id") != task_id]
    return len(_TASKS) < before


def mark_complete(task_id: str) -> bool:
    task = get_task(task_id)
    if not task:
        return False
    task["status"] = "done"
    return True


def update_task(task_id: str, title: Optional[str] = None, priority: Optional[str] = None, notes: Optional[str] = None) -> bool:
    task = get_task(task_id)
    if not task:
        return False
    if title is not None:
        task["title"] = title
    if priority is not None:
        task["priority"] = priority
    if notes is not None:
        task["notes"] = notes
    return True
