from app import app
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

# app = Flask(__name__)
#
# app.config['MONGO_DBNAME'] = 'hospital'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/hospital'
#
# mongo = PyMongo(app)

if __name__ == '__main__':
    app.run()
