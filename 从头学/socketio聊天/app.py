from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit, rooms, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "jdsklf"   # 秘钥
socket = SocketIO(app)
socket.init_app(app, cors_allowed_origins="*")
"""
注意：
    Flask-SocketIO      5.3.1
    gevent-websocket    0.10.1
    gevent              21.12.0
前端：  
    jquery.min.js       3.1.1     
    socket.io.js        4.5.3      
"""

@app.route("/")
def index():
    return render_template("index.html")



zd = {}
# # 客户端连接成功后
@socket.on("connect")
def connect():
    print('加入房间')
# 客户端断开连接后
@socket.on("disconnect")
def disconnect():
    print('离开房间')



# 这个函数用来处理加入房间操作，不是用来发消息
@socket.on('join')
def on_join(data):
    print(data)
    room = data['room']
    # 用sid作为key，房间名作为值代表这个人加入了房间
    zd.update({request.sid: room})
    print("目前有", zd)


@socket.on('laval')
def on_laval(data):
    # 退出房间，并非断开连接
    print(data)
    zd.pop(request.sid)
    print(zd)
    print('退出成功')



# 这个函数才是正正在的收发消息，msg是通道
@socket.on('msg')
def msg_a(msg):
    print('接受成功', msg)
    # 把房间取出来
    sid = request.sid
    room = zd.get(sid)
    dz = '/'+room
    print('msg这里', room,dz)
    # 只有加入房间的人才能看到消息
    emit(room, msg, broadcast=True)    # 把消息转发到dz(房间)



if __name__ == "__main__":
    socket.run(app, host="0.0.0.0", port=5000, debug=True)
