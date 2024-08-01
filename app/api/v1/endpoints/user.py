from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.db.models import User
from app.schemas.user import UserCreate

router = APIRouter()

@router.post('/', response_model=UserCreate)
def create_user(*, db: Session = Depends(deps.get_db), user_in: UserCreate):
    user = User(username=user_in.username, hashed_password=user_in.password, email=user_in.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user