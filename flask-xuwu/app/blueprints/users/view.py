from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from .forms import RegisterForm, LoginForm
from app.UModel import User, db
from app.tools.me_email.email import send_mail
from app.tools.captcha.aliyunsms.sms_send import Sample    # 短信
from random import randint
from app.tools.rediss import if_code
import re


users_dp = Blueprint("users", __name__)
# 正则
RE_MAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"    # 邮箱
RE_PHONE = r"1[3-9]\d{9}"   # 号码


# 新用户注册登录
@users_dp.route('/new_register', methods=["POST"])
def register():
    u = request.form.get('username')
    g = request.form.get('gender')
    s = request.form.get('sr')
    m = request.form.get('mail')
    p = request.form.get('phone')
    p1 = request.form.get('pwd')
    p2 = request.form.get('pwd2')
    user_id = randint(100000, 999999)
    # 入库（先不做验证号码邮箱功能，后期在座）
    if g == "男":
        g = 1
    else:
        g = 0
    if p1 == p2:
        user = User(username=u, gender=g, password=p1, email=m, phone=p, birthday=s, user_id=user_id)
        db.session.add(user)
        db.session.commit()
        flash("注册成功", "ok")
        return redirect(url_for("index.index"))
    return "两次密码不一样"


# 密码登录
@users_dp.route('/login_pwd', methods=['GET', 'POST'])
def pwd_login():
    form = RegisterForm()   # 创建工具
    # 渲染表单工具
    if request.method == "POST":
        # 获取网页传来的用户账号和密码
        user = form.username.data   # 用户名
        pwd = form.password.data   # 密码
        if re.match(RE_PHONE, user):   # 手机号登录
            d_user = User.query.filter_by(phone=user).first()  # 查询用户名
            return login_pwd(d_user, pwd)    # 直接调用验证的函数
        elif re.match(r"[1-9]\d{5}", user) and len(user) == 6:    # ID登录，必须符合正则和长度是6
            d_user = User.query.filter_by(user_id=user).first()
            return login_pwd(d_user, pwd)    # 直接调用验证的函数
        elif re.match(RE_MAIL, user):
            d_user = User.query.filter_by(email=user).first()
            return login_pwd(d_user, pwd)
        else:
            flash("登录失败", 'error')
            return redirect(url_for('users.pwd_login'))
    return render_template("users/pwd_login.html", form=form, title="加入？")


# 验证码登录
@users_dp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = form.username.data    # 手机号或者邮箱,id
        # 获取验证码
        code = request.form.get('vif')

        if re.match(RE_PHONE, user):
            d_user = User.query.filter_by(phone=user).first()    # 通过号码查询
            print("能查到号码？", d_user)
            # 如果是不是新账号就直接调用验证开始登录
            if d_user != None:
                print("数据库为None这里应该没有被执行吧？")
                return login_sms(code, user, d_user)   # 验证
            else:
                print("是新用户")
                return render_template('users/register.html')
        else:
            d_user = User.query.filter_by(email=user).first()    # 通过邮箱查询
            return login_sms(code, user, d_user)   # 验证
    return render_template("users/login.html", form=form)


# 退出登录
@users_dp.route('/logout')
def logout():
    session.clear()
    flash("退出成功", 'ok')
    return redirect('/')


# 获取验证码
@users_dp.route('/get_code', methods=['POST'])
def get_code():
    user = request.form.get('username')
    code = randint(100000, 999999)
    if re.match(RE_PHONE, user):
        print(user)
        # 使用手机短信
        if_code.set_code(user, code, 300)    # 保存验证码到redis
        # 调用阿里云短信发送
        lb = [user, "归墟来信", "SMS_270375137", '{"code":"%s"}' % code]
        # Sample.main(lb)
        print("短信验证码是：", code)
    elif re.match(RE_MAIL, user):
        # 使用邮箱验证码
        body = "<h1>%s</h1><p>这是您的登录验证码，五分钟内有效</p>" % code
        send_mail("邮箱登录", user, body)
        # 保存验证码到redis
        if_code.set_code(user, code, 300)
    else:
        return "格式错误"
    return "ok"


# 设置session的函数(公用)
def set_session(d_user):
    session['user_id'] = d_user.id  # 设置登录id
    session.permanent = True  # 永久有效
    flash("登录成功", 'ok')


# 密码登录函数（公用）
def login_pwd(d_user, pwd):
    # 登录验证，验证id、邮箱、手机号登录
    if d_user and d_user.password == pwd:  # 如果用户已经存在
        set_session(d_user)  # 设置session，保持登录状态
        return redirect(url_for('index.index'))
    else:
        flash("登录失败", "error")
        return redirect(url_for('users.pwd_login'))


# 短信登录函数（公用）
def login_sms(code, user, d_user):
    if code == if_code.get_code(user) and d_user:
        set_session(d_user)  # 设置session
        if_code.dal_code(user)  # 登录成功删除验证码
        return redirect(url_for("index.index"))  # 重定向到首页
    else:
        flash("登录失败", "error")
        return redirect("/user/login")


# 判断是否为新用户
# def new_user(d_user):
#     if d_user == None:
#         # 入库