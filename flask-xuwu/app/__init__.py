from flask import Flask

from app.settings import Config
from app.UModel import db
# 导入蓝图
from .blueprints.index.view import index_dp
from .blueprints.users.view import *
from .blueprints.post.view import *
from .blueprints.info.view import *
from .blueprints.chat.view import *
# 测试数据的蓝图
from .blueprints.test.tests import *
from .blueprints.admin.view import admin_dp
# 数据库迁移
from flask_migrate import Migrate
# 邮箱
from .tools.me_email.email import mail
# 聊天
from .settings import socket
# 跨域
from flask_cors import CORS


def create_app():
    # 功能式架构里面的app函数
    app = Flask(__name__)  # app
    db.init_app(app)    # 数据库
    app.config.from_object(Config)    # 配置
    ym = ['http://127.0.0.1:80']  # 跨域列表
    # CORS(app, resources="/*")    # 允许全部域名
    # CORS(app, resources={r'/*':{'origins': ym}})    # 允许全部域名


    mail.init_app(app)    # 邮箱
    migrate = Migrate(app, db)      # 实例化数据库迁移

    # 注册蓝图 url_prefix代表给路径添加访问前缀
    app.register_blueprint(index_dp)    # 首页
    # 用户的蓝图，包括登录注册
    app.register_blueprint(users_dp, url_prefix="/user")
    # 一些测试数据：创建和删除数据库
    app.register_blueprint(test_dp, url_prefix="/test")
    # 帖子相关，富文本
    app.register_blueprint(post_dp, url_prefix="/post")
    # 后台：用户中心
    app.register_blueprint(info_dp, url_prefix="/info")
    # 管理员
    app.register_blueprint(admin_dp, url_prefix="/admin")
    # chat
    app.register_blueprint(chat_dp, url_prefix="/chat")
    # 聊天
    socket.init_app(app, cors_allowed_origins="*")

    return [socket, app]


