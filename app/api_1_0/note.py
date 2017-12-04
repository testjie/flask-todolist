from flask import render_template
from app.api_1_0 import bp
from app.api_1_0 import vues


@bp.route("/notes/")
def note_manage():
    return render_template("notes.html")
