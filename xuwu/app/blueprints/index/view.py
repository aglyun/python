from flask import Blueprint, render_template, session
from app.UModel import Post, User

index_dp = Blueprint("index", __name__)


# 首页
@index_dp.route('/')
def index():
    p = Post.query.all()
    return render_template('posts/post.html', post=p[::-1])   # 模板需要和蓝图同级目录


# 全局404页面
@index_dp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html')


# 上下文管理器 app_context_processor是蓝图全局的，没有前缀app的是独有的
@index_dp.app_context_processor
def my_context_processor():
    """ 上下文管理器, 每次请求都会执行这个函数"""
    user_id = session.get('user_id')    # 获取一个session
    print("上下文管理器：{}".format(user_id))
    # 如果设置的session存在
    if user_id:
        # 查询用户，并且判断是否查询到，查询成功便返回一个字典，否则返回空白字典
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {"um": user}
    return {}
