# 测试socket
# import socketio
#
# sio = socketio.Client()
# sio.connect('http://127.0.0.1:5002',)
#
#
# # 接受消息:huifu是自定义事件名称
# @sio.on('huifu')
# def huifu(data):
#     print(data)
#
# @sio.on('demo')
# def ai(data):
#     print('ai:', data)
#
# sio.wait()   # 等待异步事件
# while True:
#     str = input('你说：')
#     sio.emit('msg', str)
#
import eventlet.wsgi
# 下面的代码是创建服务端
import socketio


server = socketio.Server()  # 服务端

@server.on('connect')
def connect(sid, environ):
    print('你来啦', sid)

@server.on('msg')
def msg(sid, data):
    print('收到消息:', data)
    # 返回消息
    server.emit('demo', '你好我收到了你的消息', room=sid)


if __name__ == '__main__':
    app = socketio.WSGIApp(server)
    socketio.Middleware(server, app)  # 中间件绑定到flask
    # 用eventlet异步方法启动网站
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)