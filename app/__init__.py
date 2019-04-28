from flask import Flask
from app.controller.usercontroller import user_controller
from app.common.db import mongo
from app.common.loginmanager import login, sess


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'hospital'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/hospital'
app.config['SESSION_TYPE'] = 'mongodb'
app.config['SECRET_KEY'] = 'super secret key'

mongo.init_app(app)
login.init_app(app)
app.config.from_object(__name__)
sess.init_app(app)
app.register_blueprint(blueprint=user_controller, url_prefix='/user')

# @app.route('/test')
# def test():
#     cars = [{'name': 'Audi', 'price': 52642},
#             {'name': 'Mercedes', 'price': 57127},
#             {'name': 'Skoda', 'price': 9000},
#             {'name': 'Volvo', 'price': 29000},
#             {'name': 'Bentley', 'price': 350000},
#             {'name': 'Citroen', 'price': 21000},
#             {'name': 'Hummer', 'price': 41400},
#             {'name': 'Volkswagen', 'price': 21600}]
#     doc = mongo.db.cars.insert_many(cars)
#     return "Inserted"
