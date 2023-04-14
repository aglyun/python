from flask import Blueprint


users_dp = Blueprint("users", __name__)


@users_dp.route("/login")
def index():
    return "users访问成功"