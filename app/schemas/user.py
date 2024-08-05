from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class UserCreate(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    bio: Optional[str] = None
    birth_date: date
    profile_picture: Optional[str] = None

    class Config:
        orm_mode = True

# UNCOMMENT THE RELATIONSHIPS BELLOW AND CREATE SHOW SCHEMAS I COMMENTED

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    bio: Optional[str] = None
    birth_date: date
    profile_picture: Optional[str] = None
    # progresses: List[Progress] = []  # Assuming Progress schema exists
    # performances: List[Performance] = []  # Assuming Performance schema exists

    class Config:
        orm_mode = True