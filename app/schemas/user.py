from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        orm_mode = True

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        orm_mode = True

