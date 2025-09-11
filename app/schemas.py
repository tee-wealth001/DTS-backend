from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from app.enums import StatusEnum, PriorityEnum


class TaskBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = StatusEnum.todo
    due_at: Optional[datetime] = None
    case_id: Optional[int] = None
    assigned_to: Optional[str] = None
    priority: Optional[str] = PriorityEnum.low


class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_at: Optional[datetime] = None
    case_id: Optional[int] = None
    assigned_to: Optional[str] = None
    priority: Optional[str] = None


class TaskReadSchema(TaskBaseSchema):
    id: int

    class Config:
        orm_mode = True
