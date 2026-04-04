from repository.student_repo import StudentRepository
from service.student_service import StudentManager
from model.student import Student
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel

router = APIRouter()
repo = StudentRepository("data/students.json")
manager = StudentManager(repo)


class StudentBase(BaseModel):
    name: str
    sex: str
    age: int
    student_id: str
    score: int


@router.post("/students/")
async def add_student(student: StudentBase):
    s = Student(student.name, student.sex, student.age, student.student_id, student.score)
    if not manager.add_student(s):
        raise HTTPException(404, "学生已存在")
    return {"mag": "添加成功"}


@router.get("/students/{student_id}")
async def get_students(student_id: str):
    s = manager.find_student(student_id)
    if not s:
        raise HTTPException(404,"学生不存在")
    return s.to_dict()


@router.get("/students/")
async def get_all_students():
    students = manager.show_all()
    return [s.to_dict() for s in students]


@router.delete("/students/{student_id}")
async def delete_student(student_id: str):
    is_or = manager.delete_student(student_id)
    if not is_or:
        raise HTTPException(404, "学生不存在")
    return {"msg": "删除成功"}


@router.put("/students/{student_id}")
async def update_student(student_id: str, student: StudentBase):
    s = Student(student.name, student.sex, student.age, student.student_id, student.score)
    if not manager.update_student(s):
        raise HTTPException(404, "学生不存在")
    return {"msg": "更新成功"}

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import List
# from repository.student_repo import StudentRepository
# from service.student_service import StudentManager
# from model.student import Student
#
# router = APIRouter()
# repo = StudentRepository("data/students.json")
# manager = StudentManager(repo)
#
# # Pydantic schema
# class StudentBase(BaseModel):
#     name: str
#     sex: str
#     age: int
#     student_id: str
#     score: int
#
# # 添加学生
# @router.post("/students/", summary="添加学生")
# async def add_student(student: StudentBase):
#     s = Student(student.name, student.sex, student.age, student.student_id, student.score)
#     if not manager.add_student(s):
#         raise HTTPException(400, "学生已存在")
#     return {"msg": "添加成功"}
#
# # 获取单个学生
# @router.get("/students/{student_id}", summary="获取单个学生")
# async def get_student(student_id: str):
#     s = manager.find_student(student_id)
#     if not s:
#         raise HTTPException(404,"学生不存在")
#     return s.to_dict()
#
# # 获取全部学生
# @router.get("/students/", summary="获取所有学生")
# async def get_all_students():
#     students = manager.show_all()
#     return [s.to_dict() for s in students]
#
# # 删除学生
# @router.delete("/students/{student_id}", summary="删除学生")
# async def delete_student(student_id: str):
#     if not manager.delete_student(student_id):
#         raise HTTPException(404, "学生不存在")
#     return {"msg": "删除成功"}
#
# # 更新学生
# @router.put("/students/{student_id}", summary="更新学生")
# async def update_student(student_id: str, student: StudentBase):
#     s = Student(student.name, student.sex, student.age, student.student_id, student.score)
#     if not manager.update_student(s):
#         raise HTTPException(404, "学生不存在")
#     return {"msg": "更新成功"}