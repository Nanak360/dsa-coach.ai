from typing import TypedDict, Optional, List

class SyllabusState(TypedDict):
    background: Optional[str]
    target_company: Optional[str]
    hours_per_day: Optional[int]
    has_dsa_knowledge: Optional[bool]
    preferred_topics: Optional[List[str]]
    syllabus: Optional[str]