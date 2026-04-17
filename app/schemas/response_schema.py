from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):  # Generic[T] = 支持泛型，也就是支持任意类型 data
    code: int
    message: str
    data: Optional[T] = None
