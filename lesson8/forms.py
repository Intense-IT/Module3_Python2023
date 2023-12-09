from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    address = StringField('Город проживания', validators=[DataRequired()])
    submit = SubmitField('Добавить')
