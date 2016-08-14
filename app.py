import sys
import os

from ecore import helpers
from ecore import server
from controllers import *
from models import *
from flask import Flask, render_template

app = Flask(__name__)
app.register_blueprint(controllers) #setting up multiple routes files as controllers

@app.route("/") #default route
def index():
    return render_template('index.html', msg=helpers.hello())


if __name__ == "__main__":
    server.serve(app)
