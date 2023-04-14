from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class MengTextFrom(FlaskForm):
    """ 梦表单(富文本) """
    title = StringField("标题", validators=[DataRequired()])
    # body =  TextAreaField("梦")
    body = CKEditorField("梦境...", validators=[DataRequired()])
    submit = SubmitField("保存记忆")

