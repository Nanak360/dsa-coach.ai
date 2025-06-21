from fastapi import APIRouter, HTTPException
from app.models.chat_model import ChatRequest, ChatResponse
from app.services.llm_service import get_llm_response

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_with_coach(request: ChatRequest):
    try:
        reply = await get_llm_response(request.user_message)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))