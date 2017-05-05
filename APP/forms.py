from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,PasswordField
from wtforms.validators import DataRequired,length

class LoginForm(FlaskForm):
    UserName = StringField('UserName', validators=[length(5,16),DataRequired()])
    PassWord = PasswordField('PassWord', validators=[DataRequired(),length(6,16)])
    remember_me = BooleanField('记住我')

