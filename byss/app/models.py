# encoding=utf-8

from app.lib.database import db,Model,Column

class User(Model):
    __table_name__ = "user"
    id = Column(db.Integer, primary_key=True)
    account = Column(db.String(128))