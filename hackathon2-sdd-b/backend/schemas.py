import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    completed: bool = Field(default=False)


class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TaskListResponse(BaseModel):
    items: list[TaskRead]
    count: int
