from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from model.student_schema import StudentResponse, StudentUpdate, StudentCreate
from database import crud
from sqlalchemy.orm import Session
from database.db_core import get_db

router = APIRouter()
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


@router.post("/students/", response_model=StudentResponse)
async def add_student(student: StudentCreate, db: Session = Depends(get_db)):  # 自动解析为StudentBase对象
    return crud.create_student(db, student.name, student.sex, student.age, student.s_id, student.score)


@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_students(student_id: str, db: Session = Depends(get_db)):
    s=crud.get_student(db, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s


@router.get("/students/", response_model=list[StudentResponse])
async def get_all_students(db: Session = Depends(get_db)):
    return crud.get_all(db)


@router.delete("/students/{student_id}")
async def delete_student(student_id: str, db: Session = Depends(get_db)):
    if not crud.delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}


@router.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: str, student: StudentUpdate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student.name, student.age,student.sex, student.score)
