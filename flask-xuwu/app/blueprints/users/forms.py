from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """ 注册表单 """
    username = StringField('用户名', validators=[DataRequired(), ])    # 实际上用的是手机号和邮箱问题不大
    password = PasswordField('密码', validators=[DataRequired(), ])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class LoginForm(FlaskForm):
    """ 登陆表单 """
    username = StringField('用户名', validators=[DataRequired(), ])
    password = PasswordField('密码', validators=[DataRequired(), ])
    submit = SubmitField('登录/注册')
