from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MailForm(FlaskForm):
    """ 登陆表单 """
    subject = StringField('主题', validators=[DataRequired(), ])
    to = StringField('收件人', validators=[DataRequired(), ])
    body = StringField('内容', validators=[DataRequired(), ])
    submit = SubmitField('发送')