from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Course(Base):
    __tablename__ = "course"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str]
    
    subjects: Mapped[list["Subject"]] = relationship(back_populates="course")
    
    
class Subject(Base):
    __tablename__ = "subject"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), index=True)
    name: Mapped[str]
    
    course: Mapped[Course] = relationship(back_populates="subjects")
    lessons: Mapped[list["Lesson"]] = relationship(back_populates="subject")
    
    
class Lesson(Base):
    __tablename__ = "lesson"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"), index=True)
    title: Mapped[str]
    content: Mapped[str]
    duration_in_minutes: Mapped[int]
    
    subject: Mapped[Subject] = relationship(back_populates="lessons")
    