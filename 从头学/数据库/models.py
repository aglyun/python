from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 测试
class Demo(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), default="None")