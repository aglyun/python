from flask import Blueprint, render_template, session, request
from app.UModel import *

info_dp = Blueprint('info', __name__)


# 个人中心
@info_dp.route('/<user_id>')
def info(user_id):
    # 获取session中的用户id
    s_id = session.get('user_id')
    if s_id == int(user_id):
        # 返回用户数据
        u = User.query.filter_by(id=s_id).first()
        return render_template('info/info.html', user=u)
    return "你无权操作"


# 修改资料
@info_dp.route('/xiugai/<user_id>', methods=['POST'])
def info_push(user_id):
    s_id = session.get("user_id")
    if s_id == int(user_id):
        # 获取前端的数据
        us = request.form.get('username')
        qm = request.form.get('qm')
        m = request.form.get('mail')
        p = request.form.get('phone')
        s = request.form.get('sr')
        g = request.form.get('gender')
        print(g)
        if g == "♂男":
            print("男")
            g = 1
        else:
            print("女")
            g = 0
        u = User.query.filter_by(id=user_id).first()
        u.username=us
        u.signature=qm
        u.email=m
        u.phone=p
        u.birthday=s
        u.gender=g
        db.session.commit()   #提交
        print(u, qm, m, p, s, g)

        return "ok"
    print("访问成功了吧")
    return "你无权操作"

