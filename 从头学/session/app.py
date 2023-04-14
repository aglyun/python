from flask import Flask, session, request

app = Flask(__name__)
# session的秘钥
app.secret_key = "fgjghguyfyuvvvhjbhjd6788"


@app.route('/')
def login():
    session['user'] = "ABCbsadda"
    session.permanent = True   # 保存永久有效
    return "登录成功"


@app.route("/ls")
def ls():
    # 查看session设置的值
    u = session['user'] 
    print(u)
    return "欢迎您{}".format(u)

@app.route('/logout')
def logout():
    session.clear()
    return "退出成功"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)