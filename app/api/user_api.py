from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.crud import create_user, get_user, verify_user
from app.schemas.student_schema import UserRegister, UserLogin, TokenResponse
from app.db.session import get_db
from app.core.security import get_current_user, login_user
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
    access_token = login_user(user)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/students/")
def get_all(user=Depends(get_current_user)):
    return {"message":  f"Hello, {user}! You have access to this data."}
