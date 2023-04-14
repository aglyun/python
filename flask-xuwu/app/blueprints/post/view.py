from flask import Blueprint, session, request, flash, redirect, render_template, url_for, jsonify
from datetime import datetime
from .forms import MengTextFrom
from app.UModel import *

post_dp = Blueprint("post", __name__)    # 帖子相关的蓝图


# 富文本编辑
@post_dp.route("/editor", methods=["GET", "POST"])
def editor():
    s_id = session.get('user_id')  # 获取一个session
    if not s_id:
        return "请登录再试"
    form = MengTextFrom()
    if request.method == "POST":
        t = form.title.data
        e = request.form.get("e")
        print(t)
        print(e)
        # c = form.body.data
        # 数据入库
        d = datetime.now()
        s = d.strftime("%Y-%m-%d %H:%M")
        print(s)
        p = Post(title=t, content=e, create_time=s, author_id=s_id)
        db.session.add(p)
        db.session.commit()
        flash("记忆成功", "ok")
        return redirect('/')
    return render_template("Ckeditor/mengCkeditor.html", form=form, title="记录梦境")


# 帖子详情
@post_dp.route("/details/<id>")
def post_details(id):
    post = Post.query.filter_by(id=id).first()
    # 评论
    comments = post.comments
    print(comments)
    return render_template("posts/postdetails.html", post=post, comments=comments)


# 查询自己写的帖子
@post_dp.route('/me/<user_id>')
def me_post(user_id):
    s_id = session.get('user_id')
    if s_id == int(user_id):
        # 身份确认通过后使用用户ID来查询帖子
        u = User.query.filter_by(id=s_id).first()
        p = u.posts    # 得到一个帖子集合
        if p == []:
            p = None
            return render_template('info/info_bottom.html', p=p, user=user_id)
        return render_template('info/info_bottom.html', p=p[::-1], user=user_id)
    return '您无权操作'


# 删除帖子
@post_dp.route('/delete/<user_id>/<post_id>')
def post_delete(user_id, post_id):
    s_id = session.get("user_id")
    if s_id == int(user_id):
        p = Post.query.filter_by(id=post_id).first()
        db.session.delete(p)
        db.session.commit()
        flash("删除成功", 'ok')
        return redirect(url_for('post.me_post', user_id=s_id))
    return redirect(url_for('info.info', user_id=s_id))


# 删除评论
@post_dp.route('/delete/<user_id>/<comment_id>/<post_id>')
def comment_delete(user_id, comment_id, post_id):
    s_id = session.get('user_id')
    if s_id == int(user_id):
        c = Comments.query.filter_by(id=comment_id).first()    # 查询评论ID
        p = Post.query.filter_by(id=post_id).first()           # 查询帖子ID
        # 判断评论是否本人，或者帖子是否是本人的都有权删除
        if c.user.id == s_id or p.user.id == s_id:
            db.session.delete(c)
            db.session.commit()
            flash("删除成功", 'ok')
        return redirect(url_for('post.post_details', id=post_id))
    return "请求出错"


# 写评论
@post_dp.route('/write/comment/<user_id>/<post_id>', methods=['POST'])
def comment_write(user_id, post_id):
    s_id = session.get('user_id')
    print(s_id, user_id, post_id)
    if s_id == int(user_id):
        com = request.form.get('comment')
        print("你的评论是：", com)
        c = Comments(content=com, author_id=user_id, post_id=post_id)
        db.session.add(c)
        db.session.commit()
        return "ok"
    return "error"