from __future__ import annotations


def require_description(raw: str) -> str:
    desc = raw.strip()
    if not desc:
        raise ValueError("Description cannot be empty")
    return desc


def require_id(task_id: int | None) -> int:
    if task_id is None:
        raise ValueError("Task id must be a positive integer")
    if task_id <= 0:
        raise ValueError("Task id must be a positive integer")
    return task_id


def parse_task_id(raw: str | int | None) -> int:
    """Validate and normalize a task id from CLI input."""
    if raw is None:
        raise ValueError("Task id must be a positive integer")
    if isinstance(raw, int):
        value = raw
    else:
        text = raw.strip()
        if not text.isdigit():
            raise ValueError("Task id must be a positive integer")
        value = int(text)
    if value <= 0:
        raise ValueError("Task id must be a positive integer")
    return value
