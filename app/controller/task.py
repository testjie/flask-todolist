from app.controller import bp
from flask import render_template, session, redirect, url_for, request
from app.controller import vues
from app.models.tbl_content import Content
from app.models.tbl_content_type import ContentType
from app.models.tbl_user import User
from app.models.ext import db
import urllib.parse, json

PAGE_PAGING_NO = 15


@bp.route("/tasks/")
def task_manage():
    user_id = session.get("user_id")
    if user_id:
        tasks = Content.query.join(ContentType).filter(ContentType.user_id == user_id, ContentType.content_type == 1,
                                                       Content.type_id == ContentType.id).all()
        if tasks:
            if len(tasks) % PAGE_PAGING_NO != 0:
                page_no = len(tasks) / PAGE_PAGING_NO + 1

            context = {
                "tasks": tasks,
                "page_no": int(page_no)
            }

            return render_template("tasks.html", **context)
    else:
        return redirect(url_for("bp.index"))


@bp.route("/add_task/", methods=["POST"])
def add_task():
    title = request.form.get("content")
    if title == None or title == "":
        return "none"
    content_type = ContentType.query.filter(ContentType.content_type == 1).first()
    if content_type == None:
        content_type = ContentType(content_type=1, user_id=session.get("user_id"))
        content_type.user = User.query.filter(User.id == session.get("user_id")).first()

    content = Content(title=title, status=1, type=1, user_id=session.get("user_id"))
    content.content_type = content_type
    db.session.add(content)
    db.session.commit()

    return "success"
