from sqlalchemy.orm import Session

from app.db.models.user import User
from app.schemas.user import UserCreate


def create(db: Session, user: UserCreate) -> User:
    hashed_password = user.password # To implement : hash password
    db_user = User(**user.model_dump(exclude={"password"}), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()


def get_by_id(db: Session, id: int) -> User | None:
    return db.query(User).where(User.id == id).first()


def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).where(User.email == email).first()
