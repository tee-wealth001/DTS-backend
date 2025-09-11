from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models import Task
from app.schemas import TaskCreateSchema, TaskUpdateSchema


# Create
async def create_task(session: AsyncSession, task_in: TaskCreateSchema) -> Task:
    task = Task.model_validate(task_in)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


# Read by ID
async def get_task(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)


# Read all
async def get_tasks(session: AsyncSession) -> list[Task]:
    result = await session.exec(select(Task))
    return result.all() # type: ignore


# Update
async def update_task(
    session: AsyncSession, task_id: int, task_in: TaskUpdateSchema
) -> Task | None:
    task = await session.get(Task, task_id)
    if not task:
        return None
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


# Delete
async def delete_task(session: AsyncSession, task_id: int) -> bool:
    task = await session.get(Task, task_id)
    if not task:
        return False
    await session.delete(task)
    await session.commit()
    return True
