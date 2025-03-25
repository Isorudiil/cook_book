from app import db, login
from datetime import datetime, timezone
from flask_login import UserMixin
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(UserMixin, db.Model):
    pass


class Recipe(db.Model):
    pass


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))