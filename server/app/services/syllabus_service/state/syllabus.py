from typing import Optional, List, TypedDict


class SyllabusState(TypedDict):
    background: Optional[str]
    target_company: Optional[str]
    hours_per_day: Optional[int]
    familiar_dsa_topics: Optional[List[str]]
    familiar_system_design_topics: Optional[List[str]]
    coding_languages: Optional[List[str]]
    project_experience: Optional[str]
    interview_experience: Optional[str]
    resume: Optional[str]
    preferred_topics: Optional[List[str]]
    syllabus: Optional[str]
