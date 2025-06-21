from app.services.user_onboarding.questions import questions
from app.services.user_onboarding.types import UserOnboardingData

def get_questions():
    return {"questions": questions}

def process_answers(answers: UserOnboardingData):
    # TODO: Save to DB or session
    return {"message": "Onboarding data received", "data": answers}