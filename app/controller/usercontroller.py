from flask import Blueprint, request
from app.model.usermodel import CreateUserFactory, CreateUser, find_user
from app.components.user import User, requires_roles
from pymongo.errors import DuplicateKeyError
from flask_login import login_user, logout_user
from app.common.loginmanager import session

user_controller = Blueprint('user', __name__)


@user_controller.route('/')
def hello_world():
    return 'Hello World!'


@user_controller.route('/create_user', methods=['POST'])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user_object = CreateUserFactory()
    try:
        user_object.user("admin").create_user(username, password)
        return "OK"
    except DuplicateKeyError:
        return "FAIL"


@user_controller.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # user = mongo.db.user.find_one({'Username': username})['Password']
    # if mongo.db.user.find_one({'Username': username})['Password'] == password:
    #     return "OK"
    user = find_user({'_id': username})
    try:
        if password == user['Password']:
            user_obj = User(user['_id'])
            session['Username'] = user['_id']
            login_user(user_obj)
            return "OK"
        else:
            return "FAIL"
    except TypeError:
        return "FAIL"
    # except KeyError:
    #     return "FAIL"


@user_controller.route('/logout')
def logout():
    logout_user()
    return "OK"


@user_controller.route('/test')
@requires_roles('Admin')
def test():
    return "YES!"
