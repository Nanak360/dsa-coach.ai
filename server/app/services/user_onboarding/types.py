from pydantic import BaseModel
from typing import List, Optional


class OnboardingQuestioner(BaseModel):
    user_email: str
    target_company: List[str] = []
    known_topics: List[str] = []
    study_time: int = 1  # hours/day
    learning_style: str = "Generic"
    challenging_topics: List[str] = []
    interview_weeks: Optional[int] = None
    mock_experience: Optional[str] = None
    preferred_platform: Optional[str] = None
    current_status: Optional[str] = None


class UserDetails(BaseModel):
    email: str
    phone: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = (
        None  # ISO format string, or use datetime if you prefer
    )
    profile_picture: Optional[str] = None
    bio: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    twitter_url: Optional[str] = None
    website_url: Optional[str] = None
    location: Optional[str] = None
    occupation: Optional[str] = None
    education: Optional[str] = None
    skills: Optional[List[str]] = []
