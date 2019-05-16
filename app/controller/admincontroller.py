from flask import Blueprint, request
from app.model.usermodel import CreateUserFactory
from pymongo.errors import DuplicateKeyError
from app.components.user import requires_roles

admin_controller = Blueprint('admin', __name__)


'''
This controller method is for creating a user. CreateUserFactory class is being used for creating a user. user_object
gets the user's role and then create_user method is being called. 
'''


@admin_controller.route('/create_user', methods=['POST'])
@requires_roles('Admin')
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    user_object = CreateUserFactory()
    try:
        user_object.user(role).create_user(username, password)
        return "OK"
    except DuplicateKeyError:
        return "FAIL"
