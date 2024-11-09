from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(tags=["Default"])


@router.get("/", response_class=PlainTextResponse)
async def index():
    return PlainTextResponse(content="Hello, world!")


@router.get("/health", response_class=PlainTextResponse)
async def health():
    return PlainTextResponse(content="OK")
