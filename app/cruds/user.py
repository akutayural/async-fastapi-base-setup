from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.cruds.base import CRUDBase
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserCRUD(CRUDBase[User, CreateUserSchema, UpdateUserSchema]):
    async def get_by_username(self, db: AsyncSession, username: str):
        result = await db.execute(select(User).filter(User.username == username))
        return result.scalar_one_or_none()


user_crud = UserCRUD(model=User)
