import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MYSQL_USER: str | None = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str | None = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST: str | None = os.getenv("MYSQL_HOST")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE: str | None = os.getenv("MYSQL_DATABASE")
    MYSQL_ROOT_PASSWORD: str | None = os.getenv("MYSQL_ROOT_PASSWORD")
    