from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, Form
from wtforms.fields.html5 import EmailField, DateField, DateTimeField
from wtforms.validators import DataRequired, ValidationError, Optional, EqualTo, InputRequired

class LoginForm(Form):
    email = EmailField('username',[InputRequired()])
    password = PasswordField('password',[InputRequired()])

class RegistationForm(Form):
    email = EmailField('이메일 주소',[InputRequired()])
    password = PasswordField('Password',[InputRequired(), EqualTo('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    nickname = StringField('닉네임',[InputRequired()])
    birthday = DateField('생일',[InputRequired()])
