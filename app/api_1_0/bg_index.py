from flask import render_template
from app.api_1_0 import bp


@bp.route("/bg_index/", methods=['GET'])
def bp_index():
    return render_template("manager/bg_index.html")
