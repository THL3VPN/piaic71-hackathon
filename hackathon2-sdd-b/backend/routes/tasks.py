from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend import auth
from backend.db import get_session
from backend.models import Task
from backend.schemas import TaskCreate, TaskRead, TaskUpdate, TaskListResponse


router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])


async def ensure_same_user(path_user_id: str, token_user_id: str) -> None:
    if path_user_id != token_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User mismatch",
        )


@router.get("/", response_model=TaskListResponse)
async def list_tasks(
    user_id: str = Path(..., description="Authenticated user id"),
    status_filter: Optional[str] = Query(
        None, alias="status", description="pending|done"
    ),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    sort: str = Query("created_at", regex="^(created_at|updated_at)$"),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)

    stmt = select(Task).where(Task.user_id == user_id)
    if status_filter == "pending":
        stmt = stmt.where(Task.completed.is_(False))
    elif status_filter == "done":
        stmt = stmt.where(Task.completed.is_(True))

    if sort == "updated_at":
        stmt = stmt.order_by(Task.updated_at.desc())
    else:
        stmt = stmt.order_by(Task.created_at.desc())

    total_stmt = select(func.count()).select_from(Task).where(Task.user_id == user_id)
    result = await session.execute(stmt.limit(limit).offset(offset))
    tasks = result.scalars().all()
    total = await session.scalar(total_stmt)

    return TaskListResponse(items=tasks, count=total or 0)


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    payload: TaskCreate,
    user_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)
    task = Task(user_id=user_id, **payload.dict())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: str,
    user_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    payload: TaskUpdate,
    task_id: str,
    user_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    task.title = payload.title
    task.description = payload.description
    task.completed = payload.completed
    await session.commit()
    await session.refresh(task)
    return task


@router.patch("/{task_id}/complete", response_model=TaskRead)
async def complete_task(
    task_id: str,
    user_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    task.completed = True
    await session.commit()
    await session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: str,
    user_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
    token_user_id: str = Depends(auth.get_current_user_id),
):
    await ensure_same_user(user_id, token_user_id)
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    await session.delete(task)
    await session.commit()
    return None
