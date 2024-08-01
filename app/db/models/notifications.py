from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class Notification(Base):
    __tablename__ = "notification"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    message: Mapped[str]
    date: Mapped[Date]
    status: Mapped[int]
    
    user: Mapped[User] = relationship()
    

class Reminder(Base):
    __tablename__ = "reminder"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    text: Mapped[str]
    date: Mapped[Date]
    status: Mapped[int]
    
    user: Mapped[User] = relationship()
    