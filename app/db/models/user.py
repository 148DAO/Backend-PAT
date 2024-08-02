from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING:
    from .progress import Progress, Performance


class User(Base):
    # Model for user data
    
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(63))
    hashed_password: Mapped[str] = mapped_column(Text())
    email: Mapped[str] = mapped_column(String(127), index=True)
    bio: Mapped[str | None] = mapped_column(String(255))
    birth_date: Mapped[date]
    profile_picture: Mapped[str | None] = mapped_column(String(127)) # Profile picture path 
    
    progresses: Mapped[list[Progress]] = relationship(back_populates="user")
    performances: Mapped[list[Performance]] = relationship(back_populates="user")
    