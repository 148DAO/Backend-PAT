# # Import all models
# from .models.base import Base
# from .models import user, auth, course, learning_resources, notifications, progress


from app.core.config import settings
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from sqlalchemy import create_engine

engine =  create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
