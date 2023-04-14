from app import create_app   # 可以导入app包中的__init__文件的函数
from flask import render_template


app = create_app()    # 创建app


@app.route("/")
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run()