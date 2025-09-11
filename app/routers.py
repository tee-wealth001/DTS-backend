from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from typing import List

from app.database import get_session
from app.schemas import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from app.crud import create_task, get_tasks, get_task, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Create a task
@router.post("/", response_model=TaskReadSchema, status_code=status.HTTP_201_CREATED)
def api_create_task(task_in: TaskCreateSchema, session: Session = Depends(get_session)):
    task = create_task(session, task_in)
    return task


# Get all tasks
@router.get("/", response_model=List[TaskReadSchema])
def api_get_tasks(session: Session = Depends(get_session)):
    tasks = get_tasks(session)
    return tasks


# Get task by ID
@router.get("/{task_id}", response_model=TaskReadSchema)
def api_get_task(task_id: int, session: Session = Depends(get_session)):
    task = get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Update task
@router.patch("/{task_id}", response_model=TaskReadSchema)
def api_update_task(
    task_id: int, task_in: TaskUpdateSchema, session: Session = Depends(get_session)
):
    task = update_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Add PUT endpoint for complete updates
@router.put("/{task_id}", response_model=TaskReadSchema)
def api_update_task_put(
    task_id: int, task_in: TaskUpdateSchema, session: Session = Depends(get_session)
):
    task = update_task(session, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Delete task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def api_delete_task(task_id: int, session: Session = Depends(get_session)):
    success = delete_task(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return
