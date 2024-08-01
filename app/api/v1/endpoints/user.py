from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.user import create_user
from app.schemas.user import UserCreate

router = APIRouter()

@router.post('/users/', response_model=UserCreate)
def create_user_endpoint(user: UserCreate, db: Session = Depends(deps.get_db)):
    return create_user(db=db, user=user)