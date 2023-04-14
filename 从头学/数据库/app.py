from flask import Flask
from models import db, Demo


app = Flask(__name__)
db.init_app(app)

# 数据库驱动
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:agl001@127.0.0.1:3306/demo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 如果出现错误，多数是没有安装 mysqlclient pip命令安装一下即可

@app.route("/")
def index():
    db.create_all()
    return "数据库章节访问成功"

@app.route("/insert")
def insert():
    """插入数据"""
    d1 = Demo(name="小明")
    d2 = Demo(name="小红")
    d3 = Demo(name="小东")
    db.session.add(d1)
    db.session.add(d2)
    db.session.add(d3)
    db.session.commit()
    return "数据新增成功"


if __name__ == "__main__":
    app.run()