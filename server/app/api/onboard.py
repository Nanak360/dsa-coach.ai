from fastapi import APIRouter
from app.services.user_onboarding.collect import get_questions, process_answers
from app.services.user_onboarding.types import UserOnboardingData

router = APIRouter()

@router.get("/questions")
def onboarding_questions():
    return get_questions()

@router.post("/submit")
def onboarding_submit(answers: UserOnboardingData):
    return process_answers(answers)
