from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.database import get_session
from app.schemas import TaskCreateSchema, TaskReadSchema
from app.crud import create_task, get_tasks

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
