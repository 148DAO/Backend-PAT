from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class Resource(Base):
    __tablename__ = "learning_resource"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(63))
    url: Mapped[str] = mapped_column(String(63))
    description: Mapped[str] = mapped_column(String(511))
    
    
class ResourceType(Base):
    __tablename__ = "learning_resource_type"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(63))
    