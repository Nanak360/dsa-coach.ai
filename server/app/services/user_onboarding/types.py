from pydantic import BaseModel
from typing import List, Optional

class UserOnboardingData(BaseModel):
    target_company: List[str]
    known_topics: List[str]
    study_time: int
    learning_style: str
    challenging_topics: Optional[List[str]] = None
    interview_weeks: Optional[int] = None
    mock_experience: Optional[str] = None
    preferred_platform: Optional[str] = None
    current_status: Optional[str] = None
    include_system_design: Optional[bool] = False