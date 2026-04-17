from fastapi import Depends, HTTPException, APIRouter
from app.schemas.student_schema import StudentResponse, StudentUpdate, StudentCreate
from app.db import crud
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.core.response import success, error
from app.schemas.response_schema import ResponseModel

router = APIRouter(prefix="/students", tags=["学生管理"])


'''
 response_model=StudentResponse
 自动返回JSON，不需要.to_dict()
 约束返回类型，过滤掉其他类型，如：password
 自动校验数据
'''


@router.post("/add/", response_model=ResponseModel[StudentResponse], summary="添加学生")
async def add_student(
        student: StudentCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)):  # 自动解析为StudentBase对象
    if user["role"] != "admin":
        return error(code=403, message="只能管理员添加")
    s = crud.create_student(
        db,
        student.name,
        student.sex,
        student.age,
        student.s_id,
        student.score
    )
    return success(StudentResponse.model_validate(s))


@router.get("/get/{student_id}", response_model=ResponseModel[StudentResponse], summary="查找学生")
async def get_students(
        student_id: str,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
        ):
    s = crud.get_student(db, student_id)
    if not s:
        return error(code=403, message="Student not found")
    return success(StudentResponse.model_validate(s))


@router.get("/get_all/", response_model=ResponseModel[list[StudentResponse]], summary="获取所有学生")
async def get_all_students(
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    students = crud.get_all(db)
    return success([
        StudentResponse.model_validate(i)
        for i in students
    ])


@router.delete("/delete/{student_id}", summary="删除学生")
async def delete_student(
        student_id: str,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(code=403, message="只有管理员能删除")
    if not crud.delete_student(db, student_id):
        return error(code=404, message="Student not found")
    return success(message="Student deleted")


@router.put("/update/{student_id}", response_model=ResponseModel[StudentResponse], summary="修改学生信息")
async def update_student(
        student_id: str, student: StudentUpdate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(code=403, message="只能管理员更改")
    update_data = student.dict(exclude_unset=True)
    s = crud.update_student(db, student_id, **update_data)
    if not s:
        return error(code=404, message="Student not found")
    return success(StudentResponse.model_validate(s))
