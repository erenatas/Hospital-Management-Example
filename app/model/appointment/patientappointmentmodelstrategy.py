from app.common.db import my_connection
from bson.json_util import dumps
from app.model.appointment.appointmentstrategy import AppointmentStrategyAbstract


'''
PatientAppointmentModelStrategy implements get_appointments and set_appointment methods for the Patient. 
'''


class PatientAppointmentModelStrategy(AppointmentStrategyAbstract):

    def get_appointments(self, user_id):
        appointments = my_connection.db['appointments'].find({'patient': user_id})
        return dumps(appointments)

    def set_appointment(self, doctor_id, patient_id, date):
        return 'Error, patient cannot set any appointments'
