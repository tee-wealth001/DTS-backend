from fastapi import FastAPI
from app.routers import router
from app.database import init_db
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


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


origins = [
    "http://localhost:4200",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
