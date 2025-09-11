from fastapi import FastAPI
from app.routers import router
from app.database import init_db
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


# Async lifespan for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure DB & tables exist
    await init_db()
    print("||||||||||||||| Database initialized |||||||||||||||")

    yield

    # Shutdown actions
    print("||||||||||||||| Shutting down HMCTS Case Management backend |||||||||||||||")


# FastAPI app
app = FastAPI(lifespan=lifespan)


# Health check
@app.get("/health")
def health_check():
    return {"status": "ok"}


# CORS configuration
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

# Include task router
app.include_router(router)
