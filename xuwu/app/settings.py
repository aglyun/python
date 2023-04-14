import os
from flask_socketio import SocketIO

socket = SocketIO()  # 套接字


class Config(object):
    DEBUG = False
    SECRET_KEY = "jdsklf"  # 秘钥
    # 数据库
    SQLALCHEMY_DATABASE_URI = "你数据库的地址"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis数据库
    REDIS_DB_URL = {
        'host': '你redis数据库的地址,
        'port': 6379,
        'password': '',
        'db': 0
    }
    # 邮箱
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
