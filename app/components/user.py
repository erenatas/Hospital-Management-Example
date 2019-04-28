from app.common.loginmanager import login, session
from app.model.usermodel import find_user
from functools import wraps
from app.common.loginmanager import sess


class User:

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


@login.user_loader
def load_user(username):
    u = find_user({"_id": username})
    return User(u['_id'])


def error_response():
    print("ERROR")


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)

        return wrapped

    return wrapper

def get_current_user_role():
    user_type = find_user({"_id": session.get("Username")})["Type"]
    if user_type == "0":
        return "Admin"
    if user_type == "1":
        return "Doctor"
    if user_type == "2":
        return "Patient"
