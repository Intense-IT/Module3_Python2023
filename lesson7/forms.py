# Файл с формами приложения
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    text = StringField('Содержимое', validators=[DataRequired()])
    author = StringField('Автор')
    submit = SubmitField('Опубликовать')


class AuthorForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    bio = StringField('Биография')
    submit = SubmitField('Добавить')
