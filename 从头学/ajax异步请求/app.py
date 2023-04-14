from flask import Flask, render_template
# 下面这个包可以生成虚拟文章，用于测试
from jinja2.utils import generate_lorem_ipsum


app = Flask(__name__)


@app.route("/post")
def show_post():
    # 虚拟文章生成,n=2代表生成2个虚拟文章
    p = generate_lorem_ipsum(n=2)
    return p 

@app.route('/')
def index():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)