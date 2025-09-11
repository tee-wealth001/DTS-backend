from enum import Enum


class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in progress"
    completed = "completed"


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
