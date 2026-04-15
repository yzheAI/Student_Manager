from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.jwt import decode_token
from app.core.jwt import create_access_token

security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_token(token)
    username = payload.get("sub")
    role = payload.get("role")

    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "username": username,
        "role": role
    }


def login_user(user):
    access_token = create_access_token({
        'sub': user['username'],
        'role': user['role']
    })
    return access_token
