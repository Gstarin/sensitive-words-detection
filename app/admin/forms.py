from flask_wtf import FlaskForm
from wtforms.fields.choices import RadioField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class WordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    regex = StringField('WordRegex')
    type = RadioField('Type', choices=[('0', 'Type 0'), ('1', 'Type 1')], validators=[DataRequired()])
    submit = SubmitField('Submit')
