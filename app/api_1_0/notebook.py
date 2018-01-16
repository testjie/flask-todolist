from flask import render_template, request, session, abort, redirect, url_for
from app.api_1_0 import bp
from app.api_1_0 import vues, errors
from app.utils.json_utlis import JsonUtils
from app.models.tbl_notebook import NoteBook
from app.models.ext import db
from app.utils import code_status
from app.api_1_0.filter import login_required


@bp.route("/get_notebook/", methods=['POST'])
@login_required
def get_notebook():
    user_id = session.get("user_id")
    if user_id:
        note_books = NoteBook.query.filter(NoteBook.user_id == user_id).order_by(NoteBook.create_time.asc()).all()
        return JsonUtils(data=note_books, code=code_status.SUCCESS_CODE, msg=code_status.SUCCESS_MSG, url="").get_json()
    return JsonUtils(data="", code=code_status.PERMISSION_CODE, msg=code_status.PERMISSION_MSG, url="").get_json()


@bp.route("/add_notebook/", methods=['POST'])
@login_required
def add_notebook():
    user_id = session.get("user_id")
    notebook_name = request.form.get("notebook_name")
    if notebook_name and user_id:
        notebook = NoteBook(name=notebook_name, user_id=user_id)
        db.session.add(notebook)
        try:
            db.session.commit()
            return JsonUtils(data="", code=code_status.SUCCESS_CODE, msg=code_status.SUCCESS_MSG, url="").get_json()
        except:
            abort(500)

    return JsonUtils(data="", code=code_status.FAILED_CODE, msg=code_status.FAILED_MSG, url="").get_json()
