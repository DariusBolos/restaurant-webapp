from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import os

templateDir = os.path.abspath('../restaurantwebapp/interface/templates')
staticDir = os.path.abspath('../restaurantwebapp/interface/static')
dataDir = os.path.abspath(os.getcwd()) + "\database\database.db"

app = Flask(__name__, template_folder=templateDir, static_folder=staticDir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dataDir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'
app.app_context().push()
db = SQLAlchemy(app)


def checkEmptyFields(*args):
    for arg in args:
        if not arg:
            return False
    return True
