from app.model.appointment.doctorappointmentmodelstrategy import DoctorAppointmentModelStrategy
from app.model.appointment.patientappointmentmodelstrategy import PatientAppointmentModelStrategy

doctor_report = DoctorAppointmentModelStrategy()
patient_report = PatientAppointmentModelStrategy()


'''
Appointment model is for database operations related to appointments. There are two functions, get_appointments and 
set_appointment. Strategy pattern has been used here for decoupling the client class from the class that is actually 
implementing the details of the algorithm. The main goal of this pattern is to enable a client class to choose between 
different algorithms or procedures to complete the same task. This way, different algorithms can be swapped in and out 
without complicating things. 

If the user type is Doctor, DoctorAppointment is being used, if it is Patient, then the PatientAppointment model is 
being used.

Patient can only get appointments. Meanwhile, Doctor can both get and set appointment(s).

    get_appointments: gets user_id and user_type. returns the appointments that the user has. 
    set_appointment: Used for setting an appointment. Gets user_id, patient_id and date.
'''


class AppointmentModel(object):
    def __init__(self, appointment_strategy):
        self._appointment_strategy = appointment_strategy

    def get_appointments(self, user_id, user_type):
        return self._appointment_strategy.get_appointments(user_id, user_type)

    def set_appointment(self, user_id, patient_id, date):
        return self._appointment_strategy.set_appointment(user_id, patient_id, date)


class DoctorAppointmentModel(AppointmentModel):
    def __init__(self):
        super(DoctorAppointmentModel, self).__init__(doctor_report)


class PatientAppointmentModel(AppointmentModel):
    def __init__(self):
        super(PatientAppointmentModel, self).__init__(patient_report)
