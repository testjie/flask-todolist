from flask import render_template, request, session, abort, redirect, url_for
from app.api_1_0 import bp
from app.api_1_0 import vues, errors
from app.utils.json_utlis import JsonUtils
from app.models.tbl_note import Note
from app.models.ext import db
from app.utils import code_status
from app.api_1_0.filter import login_required


@bp.route("/notes/")
def note_manage():
    if session.get("user_id"):
        return render_template("notes.html")
    return redirect(url_for("bp.index"))


@bp.route("/new_note/", methods=["GET"])
def goto_new_page():
    if session.get("user_id"):
        return render_template("edit_notes.html")
    return redirect(url_for("bp.index"))


@bp.route("/add_note/", methods=['POST'])
@login_required
def add_note():
    title = request.form.get("title")
    html = request.form.get("htmlCode")
    markdown = request.form.get("markdownCode")
    notebook_id = request.form.get("notebook_id")

    note = Note(title=title, html_content=html, markdown_content=markdown, notebook_id=notebook_id)
    try:
        db.session.add(note)
        db.session.commit()
        return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, data={}, url="/notes/").get_json()
    except:
        abort(500)


@bp.route("/get_note/", methods=['POST'])
@login_required
def get_note():
    user_id = session.get("user_id")
    title = request.form.get("title")
    html = request.form.get("htmlCode")
    markdown = request.form.get("markdownCode")

    note = Note(title=title, html_content=html, markdown_content=markdown, user_id=user_id)
    try:
        db.session.add(note)
        db.session.commit()
        return JsonUtils(msg=code_status.SUCCESS_MSG, code=code_status.SUCCESS_CODE, data={}, url="/notes/").get_json()
    except:
        abort(500)
