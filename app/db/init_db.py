import logging
import os

from app.core.config import settings


logging.basicConfig(level=logging.INFO)
        
    
def run_migrations() -> None:
    # Run database migrations
    logging.info("Trying to run alembic migrations...")
    # Place in same directory as alembic.ini file
    os.chdir(settings.ROOT_DIRECTORY)
    # Call alembic upgrade command
    result = os.system("alembic upgrade head")
    if result != 0:
        raise RuntimeError("Failed to run alembic migrations")
    logging.info("Sucessfully ran alembic migrations")
