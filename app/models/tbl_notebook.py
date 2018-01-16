from app.models.ext import db
from datetime import datetime


class NoteBook(db.Model):
    __tablename__ = "tbl_notebook"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("tbl_user.id"), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.user_id = kwargs.get("user_id")
