from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    # 用户
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)    # 数据库ID
    user_id = db.Column(db.Integer)     # 用户ID
    username = db.Column(db.String(16), nullable=False, unique=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), nullable=True)     # 邮箱
    phone = db.Column(db.String(11), nullable=True, unique=True)    # 手机号

    gender = db.Column(db.Integer, default=1)    # 0女 1男 默认1   这里后期需要改成布尔值类型
    birthday = db.Column(db.DateTime, default=datetime.now)    # 生日，默认是注册日期
    signature = db.Column(db.String(32), default="说的什么吧")   # 个性签名
    # TODO 余额功能，后续添加
    # 加入时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 反查外键，通过posts可以查到有多少文章
    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comments", back_populates="user")    # 通过comments查询评论
    chat_room = db.relationship('ChatRoom', back_populates="user")    # 反查ChatGPT聊天的房间


# 新增加帖子
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 反查作者，注意back_populates的值必须是关系的字段名称
    user = db.relationship('User', back_populates='posts')
    # 所有的评论
    comments = db.relationship('Comments', back_populates='post')
    # 收藏、评论、点赞


# 评论
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(512), nullable=True)
    delete = db.Column(db.Boolean, default=0)   # 是否删除，默认0,1是删除
    create_time = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    # 作者外键:发布评论的本人
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 帖子外键:发布帖子的人
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    # 反查作者：本人的评论
    user = db.relationship('User', back_populates='comments')
    # 反查：既可以通过帖子找到该评论，也可以通过评论找到帖子、
    post = db.relationship("Post", back_populates='comments')
    # 用户点赞 TODO


# ChatGPT的聊天模型
# 聊天房间,保存房间名,绑定user
class ChatRoom(db.Model):
    __tablename__ = "chat_room"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)    # 房间名不能是空白
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_time = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    # 反查作者
    user = db.relationship('User', back_populates='chat_room')
    # 反查该房间中所有的聊天记录（AI，你）
    ai_msg = db.relationship('ChatAi')
    me_msg = db.relationship('ChatMe')


class ChatMe(db.Model):
    __tablename__ = "chat_me"
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('chat_room.id'))
    content = db.Column(db.String(128))    # 你的提问
    create_time = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    # 反查ai的回答
    me_quiz = db.relationship('ChatAi', back_populates='ai_answer')


class ChatAi(db.Model):
    __tablename__ = "chat_ai"
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('chat_room.id'))
    me_id = db.Column(db.Integer, db.ForeignKey('chat_me.id'))    # 绑定提问的人
    content = db.Column(db.UnicodeText)    # ai的回答,UnicodeText不限制长度
    create_time = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    # 反查本人的提问
    ai_answer = db.relationship('ChatMe', back_populates='me_quiz')

