from flask import Flask, render_template, request, jsonify, url_for, redirect, session, Blueprint, flash
from flask_login import current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required
from pymongo import MongoClient
from app_config import app, flask_bcrypt, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from forms import LoginForm, RegistationForm
from User import User

flask_bookstory1 = Blueprint('flask_bookstory1',__name__,template_folder='templates',static_folder='static')

@app.route('/',methods=['GET','POST'])
def login():
    if 'username' in session:
        return "Login Already Done!!!!"
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            userObj = User()
            user = userObj.get_by_username_w_password(form.email.data)
            if user:

                if flask_bcrypt.check_password_hash(user.password,
                                                    form.password.data) and user.auth == True:

                    if login_user(user, remember=True):
                        session['email'] = user.email
                        return jsonify({"result":"success"})
                    else:
                        flash("unable to log in")
                elif flask_bcrypt.check_password_hash(user.password,
                                                      form.password.data) and user.auth == False:
                    flash("Sorry You are in the middle of evaluation. Please wait for a while")
                else:
                    flash('Sorry incorrect password')
                return redirect(url_for('login'))
            else:
                flash('Sorry username is not exist')
                return redirect(url_for('login'))
    return render_template('index.html', form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistationForm(request.form)
    if request.method == "POST":

        if form.validate():
            user = db.db.user

            db_user = user.find_one({'email': form.email.data})
            # print(db_user)
            if db_user is None:
                pw_hash = flask_bcrypt.generate_password_hash(form.password.data)
                temp = User()
                birthday = datetime.strptime(form.birthday.data.strftime("%Y-%m-%d"),'%Y-%m-%d')
                temp.save(email=form.email.data,password=pw_hash,nickname=form.nickname.data,auth=True,birthday=birthday,gender=request.form['gender'])

                return redirect(url_for('login'))
            else:
                flash('Sorry, username already taken. Please try another')
                return redirect(url_for('register'))
        else:
            if form.password.data != form.confirm.data:
                flash("Sorry, Password doesn't match. Please try again")
    return render_template('register.html',form=form)

@login_manager.user_loader
def load_user(id):
    temp = User()
    a = temp.get_by_id(id)
    return a

@login_manager.unauthorized_handler
def unauthorized():
    flash('로그인을 해주세요.')
    return redirect(url_for('login'))

# @app.before_request
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=120)