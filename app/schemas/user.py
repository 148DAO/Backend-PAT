from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel, EmailStr

if TYPE_CHECKING:
    from app.schemas.progress import ProgressRead, PerformanceRead


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    birth_date: date
    bio: str | None = None
    profile_picture: str | None = None
    
    class Config:
        from_attributes = True


class UserCreate(BaseUser):
    password: str


class UserRead(BaseUser):
    id: int
    
    progresses: list[ProgressRead]
    performances: list[PerformanceRead]
    