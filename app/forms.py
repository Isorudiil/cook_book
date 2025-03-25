from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField,
                     StringField, SubmitField)
from wtforms.validators import (DataRequired, Email,
                                EqualTo, ValidationError)
import sqlalchemy as sa


class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    pass