from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class AuthToken(Base):
    __tablename__ = "auth_token"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    token: Mapped[str] = mapped_column(index=True)
    expiry_date: Mapped[Date]

    user: Mapped[User] = relationship()
