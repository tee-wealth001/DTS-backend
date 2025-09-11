from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from typing import AsyncGenerator
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./tasks.db")

# Async engine
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Async sessionmaker
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Initialize DB
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# FastAPI dependency
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
