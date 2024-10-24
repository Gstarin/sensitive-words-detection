from flask_wtf import FlaskForm
from wtforms.fields.choices import RadioField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

# 定义用于添加或更新敏感词的表单类
class WordForm(FlaskForm):
    # 输入敏感词的字段，不能为空
    word = StringField('Word', validators=[DataRequired()])
    # 输入正则表达式的字段，可以为空
    regex = StringField('WordRegex')
    # 类型选择，使用单选按钮，必选项
    type = RadioField('Type', choices=[('0', 'Type 0'), ('1', 'Type 1')], validators=[DataRequired()])
    # 提交按钮
    submit = SubmitField('Submit')
