import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # POSTGRESQL
    SQLALCHEMY_DATABASE_URL: str = (
        f"postgresql+asyncpg://postgresql://kutay:6BO6AkEKxAMsgojspMuLXMonRc77S164@dpg-csmprh1u0jms73frf440-a/testdb_m72u"
    )
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_DB: int = os.getenv("REDIS_DB", 0)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")


configuration = Settings()
