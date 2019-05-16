from flask import Blueprint, request
from app.model.usermodel import find_user
from app.components.user import User, requires_roles
from flask_login import login_user, logout_user
from app.common.loginmanager import session

user_controller = Blueprint('user', __name__)

'''
This controller is for logging in. After the user logs in, it's session id is being registered into the system. In this
case, it is mongodb.
'''


@user_controller.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
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


'''
This controller is for logging out. Session id of the user gets deleted from the system.
'''


@user_controller.route('/logout')
@requires_roles('Admin', 'Doctor', 'Patient')
def logout():
    logout_user()
    return "OK"


'''
This controller tells the user's username.
'''


@user_controller.route('/current_user', methods=['GET'])
@requires_roles('Admin', 'Doctor', 'Patient')
def current_user():
    return session.get('user_id')


# @requires_roles('Admin')
@user_controller.route('/')
def test():
    return "Hello world!"
