from fastapi import Header

from app.database import DBSession, sessionmanager


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


async def get_async_db():
    async with sessionmanager.session() as session:
        yield session



def get_list_headers(page_number: int = Header(default=0, alias="page"),
                     page_length: int = Header(default=100, alias="pagesize"),
                     page_search: str = Header(default=None, alias="page-search")):
    return {
        "page": page_number,
        "pagesize": page_length,
        "page-search": "%{}%".format(page_search) if page_search else None
    }

