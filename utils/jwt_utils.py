from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    if SECRET_KEY is None:
        raise ValueError("SECRET_KEY not found in environment variables")

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# 解析JWT token，返回payload内容
def decode_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload


# 从token提取当前用户信息
def get_current_user(token: str):
    payload = decode_token(token)
    username = payload.get("sub")
    return username
