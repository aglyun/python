# 测试socket
import socketio

sio = socketio.Client()
sio.connect('http://192.168.1.12:5000',)


# 接受消息:huifu是自定义事件名称
@sio.on('huifu')
def huifu(data):
    print(data)

@sio.on('demo')
def ai(data):
    print('ai:', data)

while True:
    str = input('你说：')
    sio.emit('msg', str)
#sio.wait()   # 等待异步事件
