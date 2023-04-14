from flask import Flask
from .settings import Config 
# 导入蓝图
from .blueprints.demo1.view import demo1_dp
from .blueprints.goods.view import goods_dp
from .blueprints.users.view import users_dp


def create_app():
    # 功能式架构里面的app函数
    app = Flask(__name__)
    app.config.from_object(Config)
    # 注册蓝图 url_prefix代表给路径添加访问前缀 如 /demo1/login
    app.register_blueprint(demo1_dp, url_prefix="/demo1")    # 导入了demo1蓝图
    app.register_blueprint(goods_dp, url_prefix="/goods")
    app.register_blueprint(users_dp, url_prefix="/users")
    
    return app
