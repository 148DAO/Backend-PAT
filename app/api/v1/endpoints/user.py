from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.user import create_new_user, get_users
from app.schemas.user import UserCreate, UserRead
from typing import List


router = APIRouter()

@router.post('/users/', response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)):
    try:
        return create_new_user(db=db, user=user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@router.get('/users/', response_model=List[UserRead], status_code=status.HTTP_200_OK)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    try:
        users = get_users(db=db, skip=skip, limit=limit)
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
