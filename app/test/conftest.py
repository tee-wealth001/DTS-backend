import pytest_asyncio
from httpx import AsyncClient
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.main import app
from app.database import get_async_session


# Test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(TEST_DATABASE_URL, echo=True, future=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Override dependency
async def get_test_session():
    async with async_session() as session:
        yield session


# Database setup/teardown
@pytest_asyncio.fixture(scope="module", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


# Async HTTP client fixture
@pytest_asyncio.fixture
async def client():
    # Override the dependency for each test
    app.dependency_overrides[get_async_session] = get_test_session
    async with AsyncClient(app=app, base_url="http://testserver") as c:
        yield c
    # Clean up the override after the test
    app.dependency_overrides.pop(get_async_session, None)


# Helper function (not a fixture)
async def create_sample_task(client: AsyncClient, title="Sample Task"):
    payload = {
        "title": title,
        "description": "This is a test task",
        "status": "Todo",
        "due_at": "2025-09-11T12:00:00Z",
        "case_id": 1,
        "assigned_to": "Alice",
        "priority": "Low",
    }
    response = await client.post("/tasks/", json=payload)
    assert response.status_code == 201
    return response.json()
