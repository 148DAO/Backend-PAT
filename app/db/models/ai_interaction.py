from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class Query(Base):
    __tablename__ = "ai_query"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    text: Mapped[str]
    date: Mapped[date]
    
    user: Mapped[User] = relationship()
    
    
class Response(Base):
    __tablename__ = "ai_response"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    query_id: Mapped[int] = mapped_column(ForeignKey(Query.id))
    text: Mapped[str]
    
    query: Mapped[Query] = relationship()


class Feedback(Base):
    __tablename__ = "ai_response_feedback"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    response_id: Mapped[int] = mapped_column(ForeignKey(Response.id))
    score: Mapped[int]
    
    response: Mapped[Response] = relationship()
    
    @property
    def user(self):
        return self.response.query.user
