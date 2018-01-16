from flask import render_template, request, session
from app.api_1_0 import bp
from app.models.tbl_user import User
from app.models.tbl_content_type import ContentType
from app.models.tbl_content import Content
from app.models.ext import db
from sqlalchemy import desc
from app.api_1_0 import vues


@bp.route("/")
def index():
    userid = session.get("user_id")
    if userid:
        user = User.query.filter(User.id == userid).first()

        """tasks/notes查询排序
        """
        tasks = Content.query.join(ContentType).filter(
            ContentType.content_type == 1, ContentType.user_id == user.id,
            Content.type_id == ContentType.id).order_by(
            Content.status.desc()).all()

        notes = Content.query.join(ContentType).filter(
            ContentType.content_type == 2, ContentType.user_id == user.id,
            Content.type_id == ContentType.id).order_by(
            Content.status.desc()).all()

        # if user.content_types:
        if len(tasks) > 0 or len(notes) > 0:
            context = {
                "tasks": tasks,
                "note": notes
            }

            return render_template("index.html", **context)
    return render_template("index.html")


@bp.route("/search/")
def search():
    keyword = request.form.get("keyword")
    return "None"
