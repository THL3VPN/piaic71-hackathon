from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Status = Literal["pending", "completed"]


@dataclass
class Task:
    id: int
    description: str
    status: Status
