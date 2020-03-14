import os
from flask import Flask, render_template, request, redirect, Blueprint
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/User"
app.config['SECRET_KEY'] = os.urandom(24)
app.config['TESTING'] = False

db = PyMongo(app)

flask_bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)