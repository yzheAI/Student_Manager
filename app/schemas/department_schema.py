from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str] = None


class DepartmentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_deleted: bool
    deleted_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }


class DepartmentQuery(BaseModel):
    name: str = ""
    description: str = ""
    page: int = 1
    size: int = 10
