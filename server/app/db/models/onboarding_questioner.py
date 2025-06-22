from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class OnboardingQuestionerDbSchema(Base):
    __tablename__ = "onboarding_questioner"

    id = Column(Integer, primary_key=True)
    email = Column(String, ForeignKey("users.email", ondelete="CASCADE"))
    target_company = Column(String)
    known_topics = Column(String)
    study_time = Column(String)
    learning_style = Column(String)
    challenging_topics = Column(String)
    interview_weeks = Column(Integer)
    mock_experience = Column(String)
    preferred_platform = Column(String)
    current_status = Column(String)