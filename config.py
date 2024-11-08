import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # POSTGRESQL
    POSTGRESQL_USER: str = os.getenv("POSTGRESQL_USER", "kutay")
    POSTGRESQL_PASSWORD: str = os.getenv("POSTGRESQL_ROOT_PASSWORD", "")
    POSTGRESQL_HOST: str = os.getenv("POSTGRESQL_HOST", "127.0.0.1")
    POSTGRESQL_PORT: str = os.getenv("POSTGRESQL_PORT", "5432")
    POSTGRESQL_DATABASE: str = os.getenv("POSTGRESQL_DATABASE", "testdb")
    SQLALCHEMY_DATABASE_URL: str = (
        f"postgresql+psycopg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}"
    )
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_DB: int = os.getenv("REDIS_DB", 0)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")


configuration = Settings()
