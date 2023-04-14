from flask import Blueprint, render_template

# 如果每个包中都有templates文件夹，则需要指定（因为是同级目录）
demo1_dp = Blueprint("demo1", __name__, template_folder="templates")

@demo1_dp.route("/login")
def index():
    return render_template("index.html")