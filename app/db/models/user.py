from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    # Model for user data
    
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True)

