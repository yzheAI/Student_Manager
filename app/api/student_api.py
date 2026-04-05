from repository.student_repo import StudentRepository
from service.student_service import StudentManager
from model.student import Student
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
from model.student_schema import StudentResponse, StudentUpdate, StudentCreate

router = APIRouter()
repo = StudentRepository("data/students.json")
manager = StudentManager(repo)

"""
验证数据类型，
自动生成JSON schema
确保前端请求时数据合法
"""


class StudentBase(BaseModel):
    name: str
    sex: str
    age: int
    student_id: str
    score: int


'''
 response_model=StudentResponse
 自动返回JSON，不需要.to_dict()
 约束返回类型，过滤掉其他类型，如：password
 自动校验数据
'''


@router.post("/students/", response_model=StudentResponse)
async def add_student(student: StudentCreate):  # 自动解析为StudentBase对象
    s = Student(student.name, student.sex, student.age, student.student_id, student.score)
    if not manager.add_student(s):
        raise HTTPException(404, "学生已存在")
    return s


@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_students(student_id: str):
    s = manager.find_student(student_id)
    if not s:
        raise HTTPException(404,"学生不存在")
    return s


@router.get("/students/", response_model=list[StudentResponse])
async def get_all_students():
    students = manager.show_all()
    return students


@router.delete("/students/{student_id}")
async def delete_student(student_id: str):
    is_or = manager.delete_student(student_id)
    if not is_or:
        raise HTTPException(404, "学生不存在")
    return {"msg": "删除成功"}


@router.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: str, student: StudentUpdate):
    s = manager.find_student(student_id)
    if not s:
        raise HTTPException(404, "学生不存在")
    if student.name is not None:
        s.name = student.name
    if student.sex is not None:
        s.sex = student.sex
    if student.age is not None:
        s.age = student.age
    if student.score is not None:
        s.score = student.score
    manager.save_to_file()
    return s

