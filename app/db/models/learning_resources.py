from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Resource(Base):
    __tablename__ = "learning_resource"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    url: Mapped[str]
    description: Mapped[str]
    
    
class ResourceType(Base):
    __tablename__ = "learning_resource_type"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    