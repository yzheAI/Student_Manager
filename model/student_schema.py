from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    sex: str
    age: int
    s_id: str
    score: int


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    score: Optional[int] = None


class StudentResponse(BaseModel):
    name: str
    sex: str
    age: int
    s_id: str
    score: int









