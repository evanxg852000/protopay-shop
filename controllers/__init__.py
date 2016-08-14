from flask import Blueprint
controllers = Blueprint('controllers', __name__)

from .home import *
from .user import *
#any route(controller) file should be imported here
