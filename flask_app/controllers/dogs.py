from flask import redirect,render_template
from flask_app import app

@app.route('/dogs')
def dog():
    return "dogs"


@app.route('/dogs/new')
def new_dog():
    return "new dog"


@app.route('/dogs/create', methods=['POST'])
def create_dog():
    redirect ('/dogs')