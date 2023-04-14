from flask import Blueprint

goods_dp = Blueprint("goods", __name__)


@goods_dp.route("/login")
def index():
    return "goods ok"