"""
Module described forms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    """
    Class that describe Login form
    """
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Sign in'))


class RegistrationForm(FlaskForm):
    """
    Class that describe Registration form
    """
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat password'),
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username)->None:
        """
        Check username at unique
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email)->None:
        """
        Check email at unique
        """
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    """
    Form for get data to reset password
    """
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request password reset'))


class ResetPasswordForm(FlaskForm):
    """
    Form for create new password for user
    """
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat password'), validators=[DataRequired(), \
        EqualTo('password')])
    submit = SubmitField(_l('Request password reset'))
