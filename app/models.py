from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

from enums import StatusEnum, PriorityEnum


class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str = Field(
        default=StatusEnum.todo, description="todo | in progress | completed"
    )
    due_at: Optional[datetime] = None

    # Case management–specific fields
    case_id: Optional[int] = Field(default=None, description="Related case identifier")
    assigned_to: Optional[str] = Field(
        default=None, description="Caseworker username or ID"
    )
    priority: Optional[str] = Field(
        default=PriorityEnum.low, description="low | medium | high"
    )


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_at: Optional[datetime] = None
    case_id: Optional[int] = None
    assigned_to: Optional[str] = None
    priority: Optional[str] = None
