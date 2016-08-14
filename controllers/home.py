from flask import render_template
from . import controllers

@controllers.route('/home')
def home():
    return render_template('index.html', msg='The Home Controller')
