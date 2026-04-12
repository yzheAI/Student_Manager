import uuid
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database.crud import create_user, get_user, verify_user
from model.student_schema import UserRegister, UserLogin, TokenResponse
from database.db_core import get_db
from utils.jwt_utils import create_access_token, get_current_user
router = APIRouter(prefix="/users", tags=["用户管理"])


@router.post("/register", summary="用户注册")
async def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(400, "学生已存在")
    return create_user(db, user.username, user.password)


@router.post("/login", summary="用户登录", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if not db_user or not verify_user(user.password, db_user.password):
        raise HTTPException(400, "用户名或密码错误")
    access_token = create_access_token({
        'sub': user.username,
    })
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/students/")
def get_all(user=Depends(get_current_user)):
    return {"message":  f"Hello, {user}! You have access to this data."}