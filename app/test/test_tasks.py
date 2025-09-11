import pytest
from app.test.conftest import create_sample_task


@pytest.mark.asyncio
async def test_create_task(client):
    task = await create_sample_task(client, "Async Create")
    assert task["title"] == "Async Create"


@pytest.mark.asyncio
async def test_get_tasks(client):
    await create_sample_task(client, "Task 1")
    await create_sample_task(client, "Task 2")
    response = await client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) >= 2


@pytest.mark.asyncio
async def test_get_task_by_id(client):
    task = await create_sample_task(client, "Single Task")
    task_id = task["id"]
    response = await client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Single Task"


@pytest.mark.asyncio
async def test_update_task_patch(client):
    task = await create_sample_task(client, "Patch Task")
    task_id = task["id"]
    response = await client.patch(f"/tasks/{task_id}", json={"title": "Updated Patch"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Patch"


@pytest.mark.asyncio
async def test_update_task_put(client):
    task = await create_sample_task(client, "Put Task")
    task_id = task["id"]
    payload = {
        "title": "Updated Put",
        "description": "Updated description",
        "status": "In_progress",
        "due_at": "2025-10-01T12:00:00Z",
        "case_id": 2,
        "assigned_to": "Bob",
        "priority": "High",
    }
    response = await client.put(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Put"
    assert data["priority"] == "High"


@pytest.mark.asyncio
async def test_delete_task(client):
    task = await create_sample_task(client, "Delete Task")
    task_id = task["id"]
    response = await client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    # Ensure task is gone
    response = await client.get(f"/tasks/{task_id}")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_task_not_found(client):
    response = await client.get("/tasks/99999")
    assert response.status_code == 404

    response = await client.patch("/tasks/99999", json={"title": "No Task"})
    assert response.status_code == 404

    response = await client.put("/tasks/99999", json={"title": "No Task"})
    assert response.status_code == 404

    response = await client.delete("/tasks/99999")
    assert response.status_code == 404
