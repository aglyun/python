from flask import Flask
from .demo1.views import demo1_dp
from .users.views import users_dp
from .settings import Config


def create_app():
    # 这个是分区式架构的app
    app = Flask(__name__)
    app.config.from_object(Config)
    # 注册蓝图
    app.register_blueprint(demo1_dp)
    app.register_blueprint(users_dp,)
    return app