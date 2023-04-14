from flask import Blueprint, render_template

demo1_dp = Blueprint("demo1", __name__)


# 视图
@demo1_dp.route('/login')
def index():
    # return "demo1 ok"
    return render_template('demo1/index.html')   # 模板需要和蓝图同级目录