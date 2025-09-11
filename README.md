# Task Management Backend

This is a **FastAPI** backend for managing tasks in a case management system. It supports **CRUD operations** on tasks, async database access, and is fully documented with **OpenAPI/Swagger**.

---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [Environment Variables](#environment-variables)
* [Database Setup](#database-setup)
* [Running the App](#running-the-app)
* [API Documentation](#api-documentation)
* [Testing](#testing)
* [Endpoints](#endpoints)
* [License](#license)

---

## Features

* Create, read, update, delete tasks
* Assign tasks to users
* Track task status (`todo`, `in_progress`, `completed`)
* Set task priority (`low`, `medium`, `high`)
* Async database access using SQLModel + SQLAlchemy
* Auto-generated OpenAPI / Swagger documentation
* Fully testable with pytest and httpx

---

## Tech Stack

* **Python 3.12+**
* **FastAPI** - API framework
* **SQLModel** - ORM for database models
* **SQLAlchemy Async** - Async DB sessions
* **SQLite / PostgreSQL** - Database
* **HTTPX & pytest-asyncio** - Async testing

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=sqlite+aiosqlite:///./tasks.db
# or PostgreSQL
# DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

---

## Database Setup

The database is automatically initialized when the app starts, but you can manually initialize it:

```python
from app.database import init_db

init_db()
```

* Tables are created using SQLModel metadata.

---

## Running the App

```bash
uvicorn app.main:app --reload
```

* **Swagger UI**: `http://127.0.0.1:8000/docs`
* **ReDoc**: `http://127.0.0.1:8000/redoc`
* **Health Check**: `http://127.0.0.1:8000/health`

---

## API Documentation

FastAPI automatically generates documentation:

* OpenAPI JSON: `/openapi.json`
* Swagger UI: `/docs`
* ReDoc: `/redoc`

All endpoints include:

* Request body validation via **Pydantic models**
* Optional `example` values
* Response models
* Summaries and descriptions for clarity

---

## Testing

Tests are written using **pytest** and **httpx** for async HTTP requests.

### Run Tests

```bash
pytest -v
```

Make sure your **test database** URL is configured in `conftest.py`:

```python
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
```

* Tests include **CRUD operations**, **error handling**, and **task filtering**.

---

## Endpoints

### Tasks

| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| POST   | `/tasks/`     | Create a new task     |
| GET    | `/tasks/`     | Get all tasks         |
| GET    | `/tasks/{id}` | Get task by ID        |
| PATCH  | `/tasks/{id}` | Partially update task |
| PUT    | `/tasks/{id}` | Fully update task     |
| DELETE | `/tasks/{id}` | Delete task by ID     |

**Request/Response models** use Pydantic schemas:

* `TaskCreate` – request body for creating a task
* `TaskRead` – response model
* `TaskUpdate` – request body for updating a task

---

### Example Task JSON

```json
{
  "title": "Finish homework",
  "description": "Math and Science exercises",
  "status": "todo",
  "due_at": "2025-09-11T12:00:00Z",
  "case_id": 1,
  "assigned_to": "Alice",
  "priority": "low"
}
```

---

## License

COMING SOON

---
