from flask import Blueprint, Flask, blueprints, render_template

user_blueprint = Blueprint('user', '__name__')

@user_blueprint.route('/')
def index():
    return render_template('users.html')

@user_blueprint.route('/login')
def login():
    return render_template('login.html')