from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app import crud
from app.schemas.user import UserCreate, UserRead


router = APIRouter()


@router.post('/users/', response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)):
    # Check if email is not already in use
    if crud.user.get_by_email(db, user.email) is not None:
        raise HTTPException(status_code=402, detail="Email already used")
    return crud.user.create(db, user)
    

@router.get('/users/', response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    users = crud.user.get_all(db=db, skip=skip, limit=limit)
    return users


