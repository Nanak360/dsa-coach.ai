from fastapi import FastAPI
from app.api import chat, onboard

app = FastAPI()

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(onboard.router, prefix="/onboarding", tags=["Onboarding"])

@app.get("/")
def read_root():
    return {"message": "Interview AI Coach backend is running!"}