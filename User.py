import os
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, current_user, login_required, login_user, UserMixin, AnonymousUserMixin, confirm_login
from app_config import db

class User(UserMixin):
    def __init__(self,email=None,password=None,auth=False,nickname=None,birthday=None,gender=None):
        self.email = email
        self.nickname = nickname
        self.password = password
        self.auth = auth
        self.birthday = birthday
        self.gender = gender
        self.id = None

    def save(self,email,password,nickname,auth,birthday,gender):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.auth = auth
        self.birthday = birthday
        self.gender = gender

        x = db.db.user.insert_one(vars(self))
        self.id = x.inserted_id
        return self.id

    def get_by_username(self, id):
        dbUser = db.db.user.find_one({'_id':id})

        if dbUser:
            self.email = dbUser['email']
            self.nickname = dbUser['nickname']
            self.password = dbUser['password']

            self.auth = dbUser['auth']
            self.birthday = dbUser['birthday']
            self.gender = dbUser['gender']
            self.id = dbUser['_id']
            return self
        else:
            return None

    def get_by_username_w_password(self,email):
        try:

            dbUser = db.db.user.find_one({'email': email})

            if dbUser:
                self.email = dbUser['email']
                self.password = dbUser['password']
                self.nickname = dbUser['nickname']
                self.auth = dbUser['auth']
                self.birthday = dbUser['birthday']
                self.gender = dbUser['gender']
                self.id = dbUser['_id']

                return self
            else:
                return None
        except Exception as ex:
            print(ex)
            print("there was an error")
            return None

    def get_by_id(self, id):
        dbUser = db.db.user.find_one({'_id': ObjectId(id)})

        if dbUser:

            self.email = dbUser['email']
            self.nickname = dbUser['nickname']
            self.password = dbUser['password']
            self.auth = dbUser['auth']
            self.birthday = dbUser['birthday']
            self.gender = dbUser['gender']
            self.id = dbUser['_id']
            return self
        else:
            return None

    def is_auth(self):
        return self.auth


class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"