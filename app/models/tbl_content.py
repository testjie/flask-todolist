from app.models.ext import db
from datetime import datetime
from app.models.tbl_content_type import ContentType


"""
    id : 自增
    titme：笔记本标题，类型为任务时，此字段可以为空
    content ：内容
    statuss ： 1 未完成，2 完成
    type_id ：类型表外键，通过type_id查询内容所属类型
    create_time ：创建时间，默认为提交时的服务器时间
    
    keep1：保留字段1
    keep2：保留字段2
"""

class Content(db.Model):
    __tablename__ = "tbl_content"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey("tbl_content_type.id"), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    keep1 = db.Column(db.String(100), nullable=True)
    keep2 = db.Column(db.String(100), nullable=True)

    content_type = db.relationship("ContentType", backref=db.backref("contents"))



    def __init__(self, **kwargs):
        self.content = kwargs.get("content")
        self.status = kwargs.get("status")
        self.type_id = kwargs.get("type_id")
        self.user_id = kwargs.get("user_id")
        self.keep1 = kwargs.get("keep1")
        self.keep2 = kwargs.get("keep2")