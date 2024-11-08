from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.user import UserCore
from app.dependencies import get_async_db


router = APIRouter(prefix="/oauth", tags=["Auth"])


@router.post("/token")
async def login(db: AsyncSession = Depends(get_async_db),
                form_data: OAuth2PasswordRequestForm = Depends()):
    token = await UserCore().authenticate_user(db=db,
                                               username=form_data.username,
                                               password=form_data.password)
    if not token:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")

    return {"access_token": token, "token_type": "bearer"}

