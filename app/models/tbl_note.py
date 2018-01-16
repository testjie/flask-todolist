from app.models.ext import db
from datetime import datetime


class Note(db.Model):
    __tablename__ = "tbl_note"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    html_content = db.Column(db.Text, nullable=False)
    markdown_content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    notebook_id = db.Column(db.Integer, db.ForeignKey("tbl_notebook.id"), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.title = kwargs.get("title")
        self.html_content = kwargs.get("html_content")
        self.markdown_content = kwargs.get("markdown_content")
        self.notebook_id = kwargs.get("notebook_id")
