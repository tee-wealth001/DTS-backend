from sqlmodel import Session, select
from app.models import Task
from app.schemas import TaskCreateSchema


# Create
def create_task(session: Session, task_in: TaskCreateSchema) -> Task:
    task = Task.model_validate(task_in)  # map schema -> model
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


# Read by ID
def get_task(session: Session, task_id: int) -> Task | None:
    return session.get(Task, task_id)


# Read all
def get_tasks(session: Session) -> list[Task]:
    return session.exec(select(Task)).all()  # type: ignore
