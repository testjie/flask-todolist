from app.api_1_0 import bp
from flask import session, redirect, url_for
from app.models.tbl_user import User
from functools import wraps


@bp.context_processor
def context_processor():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {"user": user}
    return {}
