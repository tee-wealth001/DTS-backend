from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

from app.database import get_async_session
from app.schemas import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from app.crud import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
    patch_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Create a task
@router.post(
    "/",
    tags=["Tasks"],
    response_model=TaskReadSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a new task with a title, description, status, priority, and assigned user.",
)
async def api_create_task(
    task_in: TaskCreateSchema, session: AsyncSession = Depends(get_async_session)
):
    return await create_task(session, task_in)


# Get all tasks
@router.get(
    "/",
    tags=["Tasks"],
    response_model=List[TaskReadSchema],
    summary="Get all tasks",
    description="Retrieve a list of all tasks in the system.",
)
async def api_get_tasks(session: AsyncSession = Depends(get_async_session)):
    return await get_tasks(session)


# Get task by ID
@router.get(
    "/{task_id}",
    tags=["Tasks"],
    response_model=TaskReadSchema,
    summary="Get a task by ID",
    description="Retrieve a single task by its unique ID.",
)
async def api_get_task(
    task_id: int, session: AsyncSession = Depends(get_async_session)
):
    task = await get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Update task (PATCH)
@router.patch(
    "/{task_id}",
    tags=["Tasks"],
    response_model=TaskReadSchema,
    summary="Partially update a task",
    description="Update specific fields of a task by its ID.",
)
async def api_patch_task(
    task_id: int,
    task_in: TaskUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    task = await patch_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Update task (PUT)
@router.put(
    "/{task_id}",
    tags=["Tasks"],
    response_model=TaskReadSchema,
    summary="Fully update a task",
    description="Replace a task with new values for all fields.",
)
async def api_update_task(
    task_id: int,
    task_in: TaskUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    task = await update_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Delete task
@router.delete(
    "/{task_id}",
    tags=["Tasks"],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Delete a task by its ID. Returns 204 No Content on success.",
)
async def api_delete_task(
    task_id: int, session: AsyncSession = Depends(get_async_session)
):
    success = await delete_task(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return
