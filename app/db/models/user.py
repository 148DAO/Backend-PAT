from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING:
    from .progress import Progress, Performance


class User(Base):
    # Model for user data
    
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[str] = mapped_column(index=True)
    bio: Mapped[str | None]
    birth_date: Mapped[date]
    profile_picture: Mapped[str | None]  # Profile picture path 
    
    progresses: Mapped[list[Progress]] = relationship(back_populates="user")
    performances: Mapped[list[Performance]] = relationship(back_populates="user")
    