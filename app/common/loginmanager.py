'''
This is where the authentication/authorization classes are being called and instantiated.
'''
from flask_login import LoginManager
from flask_session import Session
from flask import session

'''
The login manager contains the code that lets your application and Flask-Login work together, such as how to load a user
from an ID, where to send users when they need to log in, and the like.
'''
login = LoginManager()
sess = Session()

