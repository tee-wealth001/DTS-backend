from fastapi import FastAPI
from app.routers import router
from app.database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # ensure DB & tables exist
    yield

    # Shutdown
    print("🛑 Shutting down HMCTS Case Management backend...")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app = FastAPI(lifespan=lifespan)

app.include_router(router)
