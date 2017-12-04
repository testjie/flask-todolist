from app.models.ext import db
from app.models.tbl_user import User
from datetime import datetime

"""
    id : 自增
    content_type ：内容类型 1：Tase； 2：笔记
    user_id ：用户表外键，通过user_id查询类型所属用户

    keep1：保留字段1
    keep2：保留字段2
"""


class ContentType(db.Model):
    __tablename__ = "tbl_content_type"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content_type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("tbl_user.id"), nullable=False)
    keep1 = db.Column(db.String(100), nullable=True)
    keep2 = db.Column(db.String(100), nullable=True)

    user = db.relationship("User", backref=db.backref("content_types"))

    def __init__(self, **kwargs):
        self.content_type = kwargs.get("content_type")
        self.keep1 = kwargs.get("kekp1")
        self.keep2 = kwargs.get("keep2")
