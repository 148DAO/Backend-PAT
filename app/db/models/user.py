from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from ..base import Base



class User(Base):
    # Model for user data
    
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(150), index=True)
    hashed_password: Mapped[str] = mapped_column(String(150), index=True)
    email: Mapped[str] = mapped_column(String(150), index=True)

