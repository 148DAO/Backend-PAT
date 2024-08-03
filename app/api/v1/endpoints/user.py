from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.user import create_user, get_users
from app.schemas.user import UserCreate, UserRead
from typing import List

router = APIRouter()

@router.post('/users/', response_model=UserCreate)
def create_user_endpoint(user: UserCreate, db: Session = Depends(deps.get_db)):
    return create_user(db=db, user=user)


@router.get('/users/', response_model=List[UserRead])
def get_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return get_users(db=db, skip=skip, limit=limit)