from flask import render_template
from . import controllers

@controllers.route('/user')
def user():
    return render_template('index.html', msg='The User Controller')
