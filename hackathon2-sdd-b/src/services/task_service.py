"""Task service stubs to be implemented when storage is available."""
from typing import Any, Dict, List, Optional


def create_task(title: str, priority: str, notes: str = "", due_date: Optional[str] = None) -> Dict[str, Any]:
    # Placeholder stub for later integration with storage
    return {
        "id": "temp-id",
        "title": title,
        "priority": priority,
        "notes": notes,
        "status": "pending",
        "due_date": due_date,
    }


def list_tasks(priority: Optional[str] = None, status: Optional[str] = None) -> List[Dict[str, Any]]:
    tasks = [
        {"id": "temp-id", "title": "Sample Task", "priority": "high", "status": "pending", "due_date": None, "notes": ""}
    ]
    if priority:
        tasks = [t for t in tasks if t.get("priority") == priority]
    if status:
        tasks = [t for t in tasks if t.get("status") == status]
    return tasks
