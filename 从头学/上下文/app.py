from flask import Flask, request, g

"""
上下文：可以理解为当前环境的快照，可以快速就绪工作
上下文分两种：程序和请求
程序：就像鱼儿的水。对flask来说就是必不可少的水
请求：包含请求中的各种信息
"""
app = Flask(__name__)

# 效果：可以把需要在shell里面测试的集成在一起，方便快速使用
@app.shell_context_processor
def ceshi():
    return dict(db="测试数据库",user="admin")

# 请求狗子
# before_first_requet
@app.before_first_request
def first():
    print("我只会执行一次")

@app.before_request
def chongfu():
    # 无论怎么请求，这里都会被预先触发
    # g对象可以把当前请求需要的全局变量存储
    # g.name 是任意属性，也可以写g.xxx g.abc g.nnn
    # g对象类似全局变量，在任何时候都能使用设置的值
    g.name = request.args.get('name')   # 好像没效果，因为前端没有传来
    print(g.name)
    print("欢迎你:",request.remote_addr)   # 获取ip地址

@app.route('/<name>')
def index(name):
    print("成功访问首页")
    return "首页"

# 上下文钩子



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)