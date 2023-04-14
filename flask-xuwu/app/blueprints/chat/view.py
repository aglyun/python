# coding=utf-8
from app.settings import socket
from flask import Blueprint, request, render_template, session, jsonify
from app.UModel import ChatRoom, ChatAi, ChatMe, db, User
from .ai import ChatGPT
import time


chat_dp = Blueprint('chat', __name__)


# 显示所有房间
@chat_dp.route('/<user_id>')
def chat_s(user_id):
    u = User.query.filter_by(id=user_id).first()
    rooms = u.chat_room
    return render_template('admin/chatgpt.html', rooms=rooms)  # 返回该房间中所有的提问和所有房间


# 返回该房间所有聊天记录
@chat_dp.route('/post/<room>', methods=['POST'])
def chat_all_msg(room):
    r = ChatRoom.query.filter_by(title=room).first()
    # 赋值改变房间名字和地址
    msg = r.me_msg
    if msg == []:
        return "空白"
    lb = []
    # 反之拼接数据
    for i in msg:
        tiwen = i.content    # 提问
        answer = i.me_quiz[0].content    # 答案
        me_time = i.create_time     # 提问的时间
        ai_time = i.me_quiz[0].create_time   # 答案的时间
        lb.append(
            {'me': tiwen, 'ai': answer, 'mt': me_time, 'at': ai_time})

        # 格式
        # [{me:, ai, mt, at}, {}, {}]
    data = {
        'me':'python的for',
        'ai':'这个我会',
    }
    # for i in range(5):
    #     lb.append(data)
    # print(lb)
    # time.sleep(3)
    return jsonify(lb)


# 创建房间的
@chat_dp.route("/create_room/<user_id>", methods=["POST"])
def create_room(user_id):
    s_id = session.get('user_id')
    if int(user_id) == s_id:
        n = request.form.get("room_name")
        r = ChatRoom(title=n, author_id=user_id)
        db.session.add(r)
        db.session.commit()
        print("创建成功")
        return "ok"
    return "error"


zd = {}   # 这个字典用于保存房间
chats = {}  # 这个字典用来存储机器人的对象

# 连接成功
@socket.on("connect")
def connect():
    # 连接成功后创建机器人
    c = ChatGPT()  # 机器人
    chats[request.sid] = c
    print(chats)  # 查看有多少机器人对象

    print("你上线了,机器人创建成功", chats)


# 客户端断开连接后
@socket.on("disconnect")
def disconnect():
    # 删除chat对象
    try:
        chats.pop(request.sid)
    except KeyError as e:
        print(e)
    print('还剩下机器人', chats)
    print('断开会话连接了')


# 这个函数专门用来加入房间
@socket.on('join')
def on_join(data):
    room = data['room']
    sid = request.sid
    zd[sid] = room
    print('加入成功', zd)


# 这个函数是用来退出
@socket.on('leave')
def on_leave():
    sid = request.sid
    zd.pop(sid)
    print(zd)
    # 删除chat对象
    try:
        chats.pop(sid)
    except KeyError as e:
        print(e)
    print('还剩下机器人', chats)
    print('退出房间成功')


# 接受/发送消息的函数,ceshi是接口，可以随意命名
@socket.on('msg')
def send(msg):
    s_id = session.get('user_id')
    # 立即返回提问者的消息
    socket.emit('huifu', msg)
    # msg得到前端发来的数据, 放入机器人中
    # 用会话模式
    # print("msg是否有数据", msg)
    # chat = chats.get(request.sid)
    # ai_msg = str(chat.session_chat(msg).encode("unicode_escape").decode("unicode_escape"))
    # print("旧",ai_msg)
    #
    # new_msg = ai_msg.replace('\n', '<br>')
    # new_msg = new_msg.replace(" ", '&nbsp;')
    # print('ChatGPT: ', new_msg)   # 把换行换成html的格式
    # 调用SavaChat函数保存到数据库（不保存也行）
    # SaveChat(me_content=msg, ai_content=new_msg, room_id=)

    # sid = request.sid
    # room = zd[sid]   # 获取房间
    # 过一段时间再返回ai的回答
    # socket.emit(房间名, 消息, namespace=地址)
    new_msg = "正在修复中..."
    room = 'demo'
    time.sleep(1)
    socket.emit(room, new_msg)


def SaveChat(room_id, me_content, ai_content):
    # 保存消息进数据库
    try:
        me = ChatMe(room_id=room_id, content=me_content)
        db.session.add(me)
        db.session.commit()
        # 先提交再提交ai的
        ai = ChatAi(room_id=room_id, me_id=me.id, content=ai_content)
        db.session.add(ai)
        db.session.commit()
        return "ok"
    except Exception as e:
        print(e)
        return "保存失败"
