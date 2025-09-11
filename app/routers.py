from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

from app.database import get_async_session
from app.schemas import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from app.crud import create_task, get_tasks, get_task, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Create a task
@router.post("/", response_model=TaskReadSchema, status_code=status.HTTP_201_CREATED)
async def api_create_task(
    task_in: TaskCreateSchema, session: AsyncSession = Depends(get_async_session)
):
    return await create_task(session, task_in)


# Get all tasks
@router.get("/", response_model=List[TaskReadSchema])
async def api_get_tasks(session: AsyncSession = Depends(get_async_session)):
    return await get_tasks(session)


# Get task by ID
@router.get("/{task_id}", response_model=TaskReadSchema)
async def api_get_task(
    task_id: int, session: AsyncSession = Depends(get_async_session)
):
    task = await get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Update task (PATCH)
@router.patch("/{task_id}", response_model=TaskReadSchema)
async def api_update_task(
    task_id: int,
    task_in: TaskUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    task = await update_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Update task (PUT)
@router.put("/{task_id}", response_model=TaskReadSchema)
async def api_update_task_put(
    task_id: int,
    task_in: TaskUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    task = await update_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Delete task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_task(
    task_id: int, session: AsyncSession = Depends(get_async_session)
):
    success = await delete_task(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return
