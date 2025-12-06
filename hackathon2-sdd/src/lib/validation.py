from __future__ import annotations


def require_description(raw: str) -> str:
    desc = raw.strip()
    if not desc:
        raise ValueError("Description cannot be empty")
    return desc


def require_id(task_id: int | None) -> int:
    if task_id is None:
        raise ValueError("Task id is required")
    if task_id <= 0:
        raise ValueError("Task id must be positive")
    return task_id
