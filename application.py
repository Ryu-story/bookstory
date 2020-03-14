from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from pymongo import MongoClient
from app_config import app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app1 import flask_bookstory1


app.register_blueprint(flask_bookstory1)


if __name__ == "__main__":
    app.run(debug=True)



