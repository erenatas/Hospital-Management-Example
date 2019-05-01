from flask import Blueprint, request
from app.model.usermodel import CreateUserFactory
from pymongo.errors import DuplicateKeyError
from app.components.user import requires_roles

admin_controller = Blueprint('admin', __name__)


@requires_roles('Admin')
@admin_controller.route('/create_user', methods=['POST'])
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

