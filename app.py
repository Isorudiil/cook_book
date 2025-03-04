from flask import render_template, redirect, url_for, request
from models import db, Recipes, PantryItems, app
import csv


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-recipe')
def add_recipe():
    return render_template('add-recipe.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
