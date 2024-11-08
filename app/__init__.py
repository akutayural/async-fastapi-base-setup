from fastapi import FastAPI

from app.database import engine
from app.models import *
from app.models.base import Base
from app.routers import api_router

app = FastAPI(title="API")
app.include_router(router=api_router)

Base.metadata.create_all(engine)
