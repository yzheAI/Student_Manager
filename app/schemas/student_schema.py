from pydantic import BaseModel, Field
from typing import Optional


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20, description="学生姓名")
    sex: str = Field(..., pattern="^(男|女)$", description="性别")
    age: int = Field(..., description="年龄")
    s_id: str = Field(..., description="学号")
    score: int = Field(..., description="成绩")


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    score: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "李四"  # 只展示要修改的字段
            }
        }
    }


class StudentResponse(BaseModel):
    name: str
    sex: str
    age: int
    s_id: str
    score: int

    model_config = {
        "from_attributes": True
    }


class UserRegister(BaseModel):
    username: str
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str






