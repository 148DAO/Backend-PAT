from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User
from .course import Course, Lesson


class Progress(Base):
    __tablename__ = "progress"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey(Course.id), index=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey(Lesson.id), index=True)
    completition_status: Mapped[int]
    start_date: Mapped[date]
    completition_date: Mapped[date | None]

    user: Mapped[User] = relationship(back_populates="progresses")
    course: Mapped[Course] = relationship(Course)
    lesson: Mapped[Lesson] = relationship(Lesson)
    

class Performance(Base):
    __tablename__ = "performance"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey(Course.id), index=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey(Lesson.id), index=True)
    score: Mapped[int]
    feedback: Mapped[str | None] = mapped_column(String(1023))
    
    user: Mapped[User] = relationship(back_populates="performances")
    course: Mapped[Course] = relationship()
    lesson: Mapped[Lesson] = relationship()
