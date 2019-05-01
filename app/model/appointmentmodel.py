from app.common.db import my_connection
from bson.json_util import dumps


def set_appointments(doctor_id, patient_id, date):
    my_connection.db['appointments'].insert_one({
        "doctor": doctor_id,
        "patient": patient_id,
        "date": date
    })
    return 'OK'


def get_appointments(user_id, user_type):
    if user_type is 'Doctor':
        appointments = my_connection.db['appointments'].find({'doctor': user_id})
    if user_type is 'Patient':
        appointments = my_connection.db['appointments'].find({'patient': user_id})
    return dumps(appointments)

