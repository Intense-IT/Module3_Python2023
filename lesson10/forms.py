from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


# Добавили в форму пользователя пароль
class UserForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    address = StringField('Город проживания', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class AddressForm(FlaskForm):
    town_name = StringField('Название города', validators=[DataRequired()])
    submit = SubmitField('Добавить город')
