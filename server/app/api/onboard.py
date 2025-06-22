from fastapi import APIRouter, Depends
from app.services.user_onboarding.questioner import get_questions
from app.services.user_onboarding.create_user import create_user, save_onboarding_questioner
from app.services.user_onboarding.types import UserDetails, OnboardingQuestioner

from app.db.deps import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/onboarding-questioner", response_model=dict)
def onboarding_questions():
    return get_questions()

@router.post("/register-user", response_model=dict)
async def register_user(answers: UserDetails, db: AsyncSession = Depends(get_db)):
    return await create_user(answers, db)

@router.post("/save-onboarding-questioner", response_model=dict)
async def save_user_onboarding(answers: OnboardingQuestioner, db: AsyncSession = Depends(get_db)):
    return await save_onboarding_questioner(answers, db)
