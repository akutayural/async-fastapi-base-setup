from fastapi import APIRouter, Depends, Path
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from app.cruds.user import user_crud
from app.dependencies import get_db, get_async_db
from app.schemas import ResponseModel
from app.schemas.user import CreateUserSchema, UserSchema

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/{user_id}", response_model=ResponseModel[UserSchema])
async def get(user_id: int = Path(), db: Session = Depends(get_async_db)):
    user = await user_crud.get(db=db, id=user_id)

    return ResponseModel[UserSchema](data=UserSchema(**user.__dict__))


@router.post("", response_model=ResponseModel)
async def create(user_in: CreateUserSchema, db: Session = Depends(get_async_db)):
    db_obj = await user_crud.create(db=db, obj_in=user_in)
    return ResponseModel()

