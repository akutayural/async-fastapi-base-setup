import datetime

from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    birth_date: Mapped[datetime.date] = mapped_column(Date, nullable=True)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    username: Mapped[str] = mapped_column(String(64), unique=True)
    password: Mapped[str] = mapped_column(String(128))




