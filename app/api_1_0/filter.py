from flask import session
from functools import wraps
from app.utils import code_status
from app.utils.json_utlis import JsonUtils


# 登陆限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user_id"):
            return func(*args, **kwargs)
        return JsonUtils(msg=code_status.PERMISSION_MSG, code=code_status.PERMISSION_CODE, url="/").get_json()

    return wrapper
