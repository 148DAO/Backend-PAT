from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    # Model for user data
    
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[str] 
       
