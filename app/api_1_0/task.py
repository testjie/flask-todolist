from app.api_1_0 import bp
from flask import render_template, session, redirect, url_for, request, abort
from app.api_1_0 import vues, errors
from app.models.tbl_content import Content
from app.models.tbl_content_type import ContentType
from app.models.tbl_user import User
from app.models.ext import db
from app.utils.json_utlis import JsonUtils
from app.utils import code_status
from app.api_1_0.filter import login_required

PAGE_PAGING_NO = 15


@bp.route("/tasks/")
def tasks():
    if session.get("user_id"):
        return render_template("tasks.html")
    return redirect(url_for("bp.index"))


"""
    获取task
    args:{"page":1}：开始的下标
"""


@bp.route("/get_tasks/", methods=["GET", "POST"])
@login_required
def get_tasks():
    user_id = session.get("user_id")
    per_page = 15
    page = request.form.get("page", 1, type=int)  # 默认page=1,
    if user_id:
        tasks = Content.query.join(ContentType).filter(ContentType.user_id == user_id, ContentType.content_type == 1,
                                                       Content.type_id == ContentType.id).paginate(page, per_page,
                                                                                                   error_out=False).items

        count = Content.query.join(ContentType).filter(ContentType.user_id == user_id, ContentType.content_type == 1,
                                                       Content.type_id == ContentType.id).all()

        if count:
            # 计算翻页页数
            if len(count) % PAGE_PAGING_NO != 0:
                page_no = len(count) / PAGE_PAGING_NO + 1
            else:
                page_no = len(count) / PAGE_PAGING_NO

            context = {
                "datas": tasks,
                "page_info": {"page_no": int(page_no), "page_total": len(tasks)}
            }

            return JsonUtils(data=context, msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE,
                             url="").get_json()

        return JsonUtils(msg=code_status.SUCCESS_CODE, code=code_status.SUCCESS_CODE, data={}, url="").get_json()



"""
    添加task
"""


@bp.route("/add_task/", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("content")

    if title == None or title == "":
        return JsonUtils(msg=code_status.FAILED_MSG, code=code_status.FAILED_CODE).get_json()

    content_type = ContentType.query.filter(ContentType.content_type == 1,
                                            ContentType.user_id == session.get("user_id")).first()
    if content_type == None:
        content_type = ContentType(content_type=1, user_id=session.get("user_id"))
        content_type.user = User.query.filter(User.id == session.get("user_id")).first()

    content = Content(title=title, status=1, type=1, user_id=session.get("user_id"))
    content.content_type = content_type
    try:
        db.session.add(content)
        db.session.commit()
    except:
        db.session.roll_back()
        abort(500)
    else:
        return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, url="/tasks/").get_json()


"""
    删除task
    args:"123,123,123,"
"""


@bp.route("/del_task/", methods=["POST"])
@login_required
def del_task():
    task_ids = request.form.get("ids").split(",")
    task_ids.remove("")

    if task_ids:
        for task_id in task_ids:
            content = Content.query.filter(Content.id == int(task_id)).first()
            db.session.delete(content)
            db.session.commit()

        return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, url="/tasks/").get_json()
    else:
        return JsonUtils(msg=code_status.FAILED_MSG, code=code_status.FAILED_CODE, url="/tasks/").get_json()


"""
    修改task
    args:{"id":id, "title":title,"status":status}
"""


@bp.route("/update_task/", methods=["POST"])
@login_required
def update_task():
    id = request.form.get("id")
    title = request.form.get("title")
    status = request.form.get("status")

    if id != None and title != None and status != None:
        task_obj = Content.query.filter(Content.id == id).first()
        task_obj.title = title
        task_obj.status = int(status)
        try:
            db.session.commit()
        except:
            db.session.roll_back()
            abort(500)

        return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, url="/tasks/").get_json()

    return JsonUtils(msg=code_status.FAILED_MSG, code=code_status.FAILED_CODE, url="/tasks/").get_json()


@bp.route("/active_task/", methods=["POST"])
@login_required
def active_task():
    id = request.form.get("id")
    if id:
        content = Content.query.filter(Content.id == id).first()
        if content:
            content.status = 1
            try:
                db.session.commit()
                return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, url="/tasks/").get_json()
            except:
                db.session.rollback()
                abort(500)

        abort(500)

    return JsonUtils(msg=code_status.FAILED_MSG, code=code_status.FAILED_CODE, url="/tasks/").get_json()


@bp.route("/finish_task/", methods=["POST"])
@login_required
def finish_task():
    id = request.form.get("id")
    if id:
        content = Content.query.filter(Content.id == id).first()
        if content:
            content.status = 2
            try:
                db.session.commit()
                return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, url="/tasks/").get_json()
            except:
                db.session.rollback()
                abort(500)

        abort(500)

    return JsonUtils(msg=code_status.FAILED_MSG, code=code_status.FAILED_CODE, url="/tasks/").get_json()
