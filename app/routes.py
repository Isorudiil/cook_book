from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask import (flash, redirect,
                   render_template, request, url_for)
from flask_login import (current_user, login_user,
                         login_required, logout_user)
from urllib.parse import urlsplit
import sqlalchemy as sa


@app.route('/')
@app.route('/index')
@login_required
def index():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass