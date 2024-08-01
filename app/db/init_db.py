import os 
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.core.config import settings

DATABASE_URL = os.getenv("DATABASE_URL", settings.database_url)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """This creae databae tables if they don't exists"""

    # This import is only used to show developer which tables have been created already
    from app.db.models import user 


    Base.metadata.create_all(bind=engine)

# def check_tables_exist():
#     inspector = inspect(engine)
#     tables = inspector.get_table_names()
#     return len(tables) > 0


# def create_database_tables():
#     if not check_tables_exist():
#         init_db() 
#     else:
#         # don't create database, it already exists
#         pass

