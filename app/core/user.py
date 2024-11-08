from jose import jwt
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.cruds.user import user_crud


class UserCore:
    def __init__(self):
        self.SECRET_KEY = "xxxxx"

    def generate_token(self, user) -> str:
        data = {"sub": user.username, "scopes": ["me"]}
        return jwt.encode(data, self.SECRET_KEY, algorithm="HS256")

    async def authenticate_user(self, db: AsyncSession, username: str, password: str) -> str | None:
        user = await user_crud.get_by_username(db=db, username=username)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        if user.password != password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        return self.generate_token(user)
