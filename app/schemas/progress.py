from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProgressCreate(BaseModel):
    user_id: int
    course_id: int
    lesson_id: int
    completition_status: int
    start_date: date
    completition_date: Optional[date] = None

    class Config:
        orm_mode = True



# UNCOMMENT BELLOW SCHEMA

# class ProgressRead(BaseModel):
#     id: int
#     user_id: int
#     course_id: int
#     lesson_id: int
#     completition_status: int
#     start_date: date
#     completition_date: Optional[date] = None
#     user: Optional[UserRead] = None  # Assuming UserRead schema exists
#     course: Optional[CourseRead] = None  # Assuming CourseRead schema exists
#     lesson: Optional[LessonRead] = None  # Assuming LessonRead schema exists

#     class Config:
#         orm_mode = True