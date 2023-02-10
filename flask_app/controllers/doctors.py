from flask import redirect,render_template
from flask_app import app

@app.route('/doctors')
def doctor():
    return "doctors"


@app.route('/doctors/new')
def new_doctor():
    return "new owner"


@app.route('/doctors/create', methods=['POST'])
def create_doctor():
    redirect ('/doctors')