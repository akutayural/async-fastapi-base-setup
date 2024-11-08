from enum import Enum
from typing import Generic, TypeVar, Optional

from pydantic import BaseModel

DataT = TypeVar('DataT')


class ResponseStatus(str, Enum):
    SUCCESS = "Success"
    WARNING = "Warning"
    FAIL = "Fail"


class ResponseModel(BaseModel, Generic[DataT]):
    data: Optional[DataT] = None
    status: ResponseStatus = ResponseStatus.SUCCESS
    message: str = 'Operation completed successfully.'
    error_code: Optional[str] = None
