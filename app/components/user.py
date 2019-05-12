from app.common.loginmanager import login, session
from app.model.usermodel import find_user
from functools import wraps


class User:

    def __init__(self, username):
        self.username = username

    '''
    To represent users needs to implement these properties and methods:
    https://flask-login.readthedocs.io/en/latest/
    '''

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


'''
This callback is used to reload the user object from the user ID stored in the session. It should take the unicode ID
of a user, and return the corresponding user object. It should return None (not raise an exception) if the ID is not 
valid. (In that case, the ID will manually be removed from the session and processing will continue.)
'''


@login.user_loader
def load_user(username):
    u = find_user({"_id": username})
    return User(u['_id'])


def error_response():
    print("ERROR")


'''requires_roles is a decorator where we can decorate a view function (API) with a role based access functionality.'''


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)

        return wrapped

    return wrapper


'''
get_current_user_role method finds the user's role. 
    0 for Admin,
    1 for Doctor,
    2 for Patient
'''


def get_current_user_role():
    user_type = find_user({"_id": session.get("Username")})["Type"]
    if user_type == "0":
        return "Admin"
    if user_type == "1":
        return "Doctor"
    if user_type == "2":
        return "Patient"

