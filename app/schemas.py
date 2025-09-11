from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.enums import StatusEnum, PriorityEnum


class TaskBaseSchema(BaseModel):
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

    model_config = ConfigDict(from_attributes=True)
