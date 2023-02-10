from flask import redirect,render_template
from flask_app import app

@app.route('/owners')
def owner():
    return "owners"


@app.route('/owners/new')
def new_owner():
    return "new owner"


@app.route('/owners/create', methods=['POST'])
def create_owner():
    redirect ('/owners')

