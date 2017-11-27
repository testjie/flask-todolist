from flask import render_template
from app.controller import bp
from app.controller import vues


@bp.route("/notes/")
def note_manage():
    return render_template("notes.html")
