from app.common.db import my_connection
from bson.json_util import dumps
from app.model.appointment.appointmentstrategy import AppointmentStrategyAbstract

'''
DoctorAppointmentModelStrategy implements get_appointments and set_appointment methods for the Doctor. 
'''


class DoctorAppointmentModelStrategy(AppointmentStrategyAbstract):

    def get_appointments(self, user_id):
        appointments = my_connection.db['appointments'].find({'doctor': user_id})
        return dumps(appointments)

    def set_appointment(self, doctor_id, patient_id, date):
        my_connection.db['appointments'].insert_one({
            "doctor": doctor_id,
            "patient": patient_id,
            "date": date
        })
        return 'OK'
