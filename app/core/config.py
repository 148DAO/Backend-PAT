import os

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
    MYSQL_HOST: str = get_required_env("MYSQL_HOST")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE: str = get_required_env("MYSQL_DATABASE")
    MYSQL_ROOT_PASSWORD: str = get_required_env("MYSQL_ROOT_PASSWORD")
    
    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"


settings = Settings()

