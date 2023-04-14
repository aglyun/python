# 工厂函数
from flask import Flask
from .settings import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 注册蓝图
    # app.register_blueprint()
    return app


