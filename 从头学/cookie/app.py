from flask import Flask, make_response, request

app = Flask(__name__)

# 设置cookie
@app.route("/<name>")
def set_cookie(name):
    """ 必须通过响应后才能设置cookie"""
    response = make_response("设置成功")
    print(name)
    response.set_cookie('name', "我不知道", max_age=3600)
    return response

# 获取cookie
@app.route("/key")
def key():
    k = request.cookies.get('name', '没有cookie')
    print('保存的cookie值是：',k)
    return k
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)