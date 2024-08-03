import os
import sys

from dotenv import load_dotenv


load_dotenv()


def get_required_env(key: str, /) -> str:
    # Return the env variable, raise ValueError if key was not found
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Could not find required {key} in .env file")
    return value


class Settings:
    MYSQL_USER: str = get_required_env("MYSQL_USER")
    MYSQL_PASSWORD: str = get_required_env("MYSQL_PASSWORD")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE: str = get_required_env("MYSQL_DATABASE")
    MYSQL_ROOT_PASSWORD: str = get_required_env("MYSQL_ROOT_PASSWORD")
    DATABASE_URL: str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

    @property
    def APP_DIRECTORY(self) -> str:
        # This file is located at app/core/config.py 
        config_file_path = os.path.abspath(__file__)
        core_directory = os.path.dirname(config_file_path)
        app_directory = os.path.dirname(core_directory)
        return app_directory
    
    @property
    def ROOT_DIRECTORY(self) -> str:
        root_directory = os.path.dirname(self.APP_DIRECTORY)
        return root_directory
   
    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"


settings = Settings()

# Add app directory in sys.path if not present
if settings.APP_DIRECTORY not in sys.path:
    sys.path.append(settings.APP_DIRECTORY)
    