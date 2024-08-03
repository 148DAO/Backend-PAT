import logging
import os
import subprocess
import time

from sqlalchemy_utils import database_exists, create_database

from app.core.config import settings


logging.basicConfig(level=logging.INFO)


def init_database() -> None:
    _create_db()
    _run_migrations()
        

def _create_db():
    # Check if database exists. Create it if not
    while True:
        try:
            exists = database_exists(settings.DATABASE_URL)
        except:
            logging.info("Could not establish connection do database. Retrying in 5 seconds.")
            time.sleep(5)
            continue
        break
    if not exists:
        logging.info(f"Database {settings.DATABASE_URL} not found. Trying to create it..")
        try:
            create_database(settings.DATABASE_URL)
        except Exception as e:
            logging.error(f"Failed to create database : {e}")
            exit(1)
        logging.info(f"Succesfully created database {settings.DATABASE_URL}")
    else:
        logging.info(f"Database {settings.DATABASE_URL} already exists, no need to create it")
        
    
def _run_migrations():
    # Call alembic upgrade command
    logging.info("Trying to run alembic migrations...")
    alembic_directory = os.path.dirname(settings.APP_DIRECTORY)
    os.chdir(alembic_directory)
    process = subprocess.Popen(["alembic", "upgrade", "head"])
    if process.wait() != 0:
        raise RuntimeError(f"Failed to run alembic migrations")
    logging.info("Sucessfully ran alembic migrations")
    