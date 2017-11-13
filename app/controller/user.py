from app.controller import bp
from flask import request, render_template, redirect, session, url_for
from app.models.tbl_user import User
from app.models.ext import db



@bp.route("/login/", methods=['POST'])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter(User.username == username).first()
        if user and user.password == password:
            if user.usertype == 100:
                session["user_id"] = user.id
                return redirect(url_for("bp.index"))
            else:
                pass
        else:
            return "用户名或密码错误"


@bp.route("/reg/",methods=['POST'])
def user_reg():
    username = request.form.get("username")
    password = request.form.get("password")
    invite_code = request.form.get("invite_code")

    if username == "" or username == None or password == "" or password == None:
        return "username或password为空"
    if invite_code != "东京有点热":
        return "邀请码不正确"

    user = User(username=username, password=password, usertype=100)

    db.session.add(user)
    db.session.commit()

    return redirect("index.html")


@bp.route("/logout/", methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for("bp.index"))