from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import chat, onboard
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(onboard.router, prefix="/onboarding", tags=["Onboarding"])

@app.get("/")
def read_root():
    return {"message": "Interview AI Coach backend is running!"}