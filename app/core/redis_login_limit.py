from app.db.redis import redis_client
EXPIRE_TIME = 300
MAX_FAIL = 5


def check_login_fail(username):
    key = f"login_fail:{username}"
    count = redis_client.get(key)
    if count and int(count) >= MAX_FAIL:
        return False
    return True


def record_login_fail(username):
    key = f"login_fail:{username}"
    count = redis_client.incr(key)
    if count == 1:
        redis_client.expire(key, EXPIRE_TIME)


def clear_login_fail(username):
    key = f"login_fail:{username}"
    redis_client.delete(key)


