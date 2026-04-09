from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from model.student_schema import StudentResponse, StudentUpdate, StudentCreate
from database import crud
from sqlalchemy.orm import Session
from database.db_core import get_db

router = APIRouter(prefix="/students", tags=["学生管理"])
"""
验证数据类型，
自动生成JSON schema
确保前端请求时数据合法
"""


class StudentBase(BaseModel):
    name: str
    sex: str
    age: int
    s_id: str
    score: int


'''
 response_model=StudentResponse
 自动返回JSON，不需要.to_dict()
 约束返回类型，过滤掉其他类型，如：password
 自动校验数据
'''


@router.post("/", response_model=StudentResponse, summary="添加学生")
async def add_student(student: StudentCreate, db: Session = Depends(get_db)):  # 自动解析为StudentBase对象
    return crud.create_student(db, student.name, student.sex, student.age, student.s_id, student.score)


@router.get("/{student_id}", response_model=StudentResponse, summary="查找学生")
async def get_students(student_id: str, db: Session = Depends(get_db)):
    s=crud.get_student(db, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s


@router.get("/", response_model=list[StudentResponse], summary="获取所有学生")
async def get_all_students(db: Session = Depends(get_db)):
    return crud.get_all(db)


@router.delete("/{student_id}", summary="删除学生")
async def delete_student(student_id: str, db: Session = Depends(get_db)):
    if not crud.delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}


@router.put("/{student_id}", response_model=StudentResponse, summary="修改学生信息")
async def update_student(student_id: str, student: StudentUpdate, db: Session = Depends(get_db)):
    update_data = student.dict(exclude_unset=True)
    s = crud.update_student(db, student_id, **update_data)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s
