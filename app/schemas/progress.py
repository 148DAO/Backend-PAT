from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from app.schemas.user import UserRead


class ProgressBase(BaseModel):
    user_id: int
    lesson_id: int
    course_id: int
    completition_status: int
    start_date: date
    completition_date: date | None = None
    
    class Config:
        from_attributes = True
        

class ProgressCreate(ProgressBase):
    pass

    
class ProgressRead(ProgressBase):
    id: int
    
    user: UserRead = Field(exclude=True)
    #course: Optional[CourseRead] = None  # Assuming CourseRead schema exists
    #lesson: Optional[LessonRead] = None  # Assuming LessonRead schema exists


class PerformanceBase(BaseModel):
    user_id: int
    lesson_id: int
    course_id: int
    score: int 
    feedback: str | None
    
    class Config:
        from_attributes = True
    
    
class PerformanceCreate(PerformanceBase):
    pass
    
    
class PerformanceRead(PerformanceBase):
    id: int
    
    user: UserRead = Field(exclude=True)
    