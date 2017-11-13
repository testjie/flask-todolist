from app.models.ext import db
from datetime import datetime

"""
    id : 自增
    username：用户名
    password ：密码
    usertype ： 用户类型 0超级管理员，100：普通用户
    regtime ：注册时间

    keep1：保留字段1
    keep2：保留字段2
"""

class User(db.Model):
    __tablename__ = "tbl_user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    usertype = db.Column(db.Integer, nullable=False)
    regtime = db.Column(db.DateTime, default=datetime.now)
    keep1 = db.Column(db.String(100), nullable=True)
    keep2 = db.Column(db.String(100), nullable=True)

    def __init__(self, *args, **kwargs):
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.usertype = kwargs.get("usertype")
        self.keep1 = kwargs.get("kekp1")
        self.keep2 = kwargs.get("keep2")


