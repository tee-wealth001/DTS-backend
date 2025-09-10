# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting HMCTS Case Management backend...")
    init_db()

    yield

    # Shutdown
    print("🛑 Shutting down HMCTS Case Management backend...")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}
