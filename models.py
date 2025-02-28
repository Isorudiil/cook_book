from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cook_book.db'
db = SQLAlchemy(app)


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class PantryItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)