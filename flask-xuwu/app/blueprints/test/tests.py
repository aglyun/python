from flask import Blueprint
from app.UModel import *

# 测试蓝图同名是否可用
test_dp = Blueprint("test", __name__)


@test_dp.route("/db/create")
def create_db():
    # 创建数据库
    db.create_all()
    return "数据库创建成功"


@test_dp.route("/db/drop")
def drop_db():
    # 删除数据库
    db.drop_all()
    return "数据库删除成功"


@test_dp.route("/faker/users")
def users():
    # 创建虚假测试的用户数据
    import faker
    f = faker.Faker(locale="zh_CN")
    for i in range(10):
        name = f.name()
        password = 123
        email = f.email()
        user_id = f.random_int(100000, 999999)
        phone = f.phone_number()
        u = User(user_id=user_id, username=name, password=password,
             email=email, phone=phone,)
        db.session.add_all([u])
    db.session.commit()
    # 插入数据
    return "虚假用户创建成功"


@test_dp.route("/faker/posts")
def posts():
    # 创建虚假测试的用户数据
    import faker
    f = faker.Faker(locale="zh_CN")
    for i in range(10):
        title = f.sentence()
        content = f.text()
        author_id = 1
        p = Post(title=title, content=content, author_id=author_id)
        db.session.add_all([p])
    db.session.commit()
    # 插入数据
    return "虚假文章创建成功"