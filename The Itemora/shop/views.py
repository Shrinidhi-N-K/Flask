from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from shop.models import User


class RegisterForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField('Email Address', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators=[DataRequired(),Length(min=2),EqualTo('password2','Passwords must match!')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('That email address Already Exists. Please choose a different one.')



class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Purchase Item!')


class SellItemForm(FlaskForm):
    submit = SubmitField('Sell Item!')