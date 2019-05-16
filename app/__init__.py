from flask import Flask

from app.controller.usercontroller import user_controller
from app.controller.admincontroller import admin_controller
from app.controller.doctorcontroller import doctor_controller
from app.controller.patientcontroller import patient_controller
from app.common import db
from app.common.loginmanager import login, sess

'''
This is where Flask is initialized. 
'''
app = Flask(__name__)

'''
This is where Flask is configured flask and it's session type.
'''
# app.config['MONGO_DBNAME'] = 'hospital'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/hospital'
app.config['SESSION_TYPE'] = 'mongodb'
# app.config['SECRET_KEY'] = 'super secret key'


# mongo.init_app(app)
login.init_app(app)
app.config.from_object(__name__)
sess.init_app(app)

'''
This is where the blueprints are registered in order to keep the MVC model organized. 
'''
app.register_blueprint(blueprint=user_controller, url_prefix='/user')
app.register_blueprint(blueprint=admin_controller, url_prefix='/admin')
app.register_blueprint(blueprint=doctor_controller, url_prefix='/doctor')
app.register_blueprint(blueprint=patient_controller, url_prefix='/patient')