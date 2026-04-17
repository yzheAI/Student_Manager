from typing import Any, Optional


def success(data: Any = None, message: str = "success"):
    return {
        "code": 200,
        "message": message,
        "data": data
    }


def error(code: int = 400, message: str = "error", data: Any = None):
    return {
        "code": code,
        "message": message,
        "data": data
    }
